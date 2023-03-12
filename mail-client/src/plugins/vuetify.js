import "vuetify/styles";
import "@mdi/font/css/materialdesignicons.css";

import { createVuetify } from "vuetify";

export default createVuetify({
  theme: {
    defaultTheme: "lightTheme",
    themes: {
      lightTheme: {
        dark: false,
        colors: {
          background: "#FAFAFA",
          surface: "#FFFFFF",
          primary: "#3DB374",
          secondary: "#242424",
          error: "#FF513D",
          "light-primary": "#4DE594",
          "light-secondary": "#96EABD",
          "primary-text": "#242424",
          "secondary-text": "#5E5E5E",
          "modal-background": "#00000040",
          border: "#D9E0E6",
        },
      },
    },
  },
});
