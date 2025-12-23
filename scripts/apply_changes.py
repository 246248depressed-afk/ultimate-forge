# file: scripts/apply_changes.py

import sys
import os

def main():
    """
    محرك بسيط جدًا: يقرأ الكود من المدخلات ويكتب فوق ملف محدد.
    """
    # الوسيط الأول: مسار المجلد الهدف للمشروع
    target_dir = sys.argv[1]
    # الوسيط الثاني: اسم الملف الذي سيتم تعديله
    file_to_modify = sys.argv[2]
    
    print(f"🚀 المحرك الذكي بدأ العمل...")
    print(f"📁 المجلد الهدف: {target_dir}")
    print(f"✍️ الملف المستهدف للتعديل: {file_to_modify}")

    # قراءة الكود الجديد الذي أرسله الـ AI من المدخل القياسي (stdin)
    ai_generated_code = sys.stdin.read()

    if not ai_generated_code:
        print("⚠️ لم يتم استلام أي كود من الـ AI. سيتم إنهاء العملية.")
        sys.exit(0)

    # بناء المسار الكامل للملف
    full_path = os.path.join(target_dir, file_to_modify)

    try:
        print(f"📝 جاري كتابة الكود الجديد في الملف: {full_path}")
        with open(full_path, 'w', encoding='utf-8') as f:
            f.write(ai_generated_code)
        print("✅ تمت الكتابة بنجاح!")
    except FileNotFoundError:
        print(f"❌ خطأ: الملف الهدف غير موجود: {full_path}")
        sys.exit(1)
    except Exception as e:
        print(f"❌ حدث خطأ غير متوقع أثناء الكتابة: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
