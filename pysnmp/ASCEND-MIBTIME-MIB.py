# SNMP MIB module (ASCEND-MIBTIME-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ASCEND-MIBTIME-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:42:27 2024
# On host MacBook-Pro.local platform Darwin version 24.0.0 by user lextm
# Using Python version 3.12.0 (main, Nov 14 2023, 23:52:11) [Clang 15.0.0 (clang-1500.0.40.1)]

if 'mibBuilder' not in globals():
    import sys

    sys.stderr.write(__doc__)
    sys.exit(1)

# Import base ASN.1 objects even if this MIB does not use it

(Integer,
 OctetString,
 ObjectIdentifier) = mibBuilder.importSymbols(
    "ASN1",
    "Integer",
    "OctetString",
    "ObjectIdentifier")

(NamedValues,) = mibBuilder.importSymbols(
    "ASN1-ENUMERATION",
    "NamedValues")
(ConstraintsIntersection,
 SingleValueConstraint,
 ValueRangeConstraint,
 ValueSizeConstraint,
 ConstraintsUnion) = mibBuilder.importSymbols(
    "ASN1-REFINEMENT",
    "ConstraintsIntersection",
    "SingleValueConstraint",
    "ValueRangeConstraint",
    "ValueSizeConstraint",
    "ConstraintsUnion")

# Import SMI symbols from the MIBs this MIB depends on

(configuration,) = mibBuilder.importSymbols(
    "ASCEND-MIB",
    "configuration")

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

(Bits,
 Counter32,
 Counter64,
 Gauge32,
 Integer32,
 IpAddress,
 ModuleIdentity,
 MibIdentifier,
 NotificationType,
 ObjectIdentity,
 MibScalar,
 MibTable,
 MibTableRow,
 MibTableColumn,
 TimeTicks,
 Unsigned32,
 iso) = mibBuilder.importSymbols(
    "SNMPv2-SMI",
    "Bits",
    "Counter32",
    "Counter64",
    "Gauge32",
    "Integer32",
    "IpAddress",
    "ModuleIdentity",
    "MibIdentifier",
    "NotificationType",
    "ObjectIdentity",
    "MibScalar",
    "MibTable",
    "MibTableRow",
    "MibTableColumn",
    "TimeTicks",
    "Unsigned32",
    "iso")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions



class DisplayString(OctetString):
    """Custom type DisplayString based on OctetString"""



# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_MibtimeDateProfile_ObjectIdentity = ObjectIdentity
mibtimeDateProfile = _MibtimeDateProfile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 529, 23, 130)
)
_MibtimeDateProfileTable_Object = MibTable
mibtimeDateProfileTable = _MibtimeDateProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 130, 1)
)
if mibBuilder.loadTexts:
    mibtimeDateProfileTable.setStatus("mandatory")
_MibtimeDateProfileEntry_Object = MibTableRow
mibtimeDateProfileEntry = _MibtimeDateProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 130, 1, 1)
)
mibtimeDateProfileEntry.setIndexNames(
    (0, "ASCEND-MIBTIME-MIB", "timeDateProfile-Index-o"),
)
if mibBuilder.loadTexts:
    mibtimeDateProfileEntry.setStatus("mandatory")
_TimeDateProfile_Index_o_Type = Integer32
_TimeDateProfile_Index_o_Object = MibScalar
timeDateProfile_Index_o = _TimeDateProfile_Index_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 130, 1, 1, 1),
    _TimeDateProfile_Index_o_Type()
)
timeDateProfile_Index_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    timeDateProfile_Index_o.setStatus("mandatory")
_TimeDateProfile_Time_Hour_Type = Integer32
_TimeDateProfile_Time_Hour_Object = MibScalar
timeDateProfile_Time_Hour = _TimeDateProfile_Time_Hour_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 130, 1, 1, 2),
    _TimeDateProfile_Time_Hour_Type()
)
timeDateProfile_Time_Hour.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    timeDateProfile_Time_Hour.setStatus("mandatory")
_TimeDateProfile_Time_Minute_Type = Integer32
_TimeDateProfile_Time_Minute_Object = MibScalar
timeDateProfile_Time_Minute = _TimeDateProfile_Time_Minute_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 130, 1, 1, 3),
    _TimeDateProfile_Time_Minute_Type()
)
timeDateProfile_Time_Minute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    timeDateProfile_Time_Minute.setStatus("mandatory")
_TimeDateProfile_Time_Second_Type = Integer32
_TimeDateProfile_Time_Second_Object = MibScalar
timeDateProfile_Time_Second = _TimeDateProfile_Time_Second_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 130, 1, 1, 4),
    _TimeDateProfile_Time_Second_Type()
)
timeDateProfile_Time_Second.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    timeDateProfile_Time_Second.setStatus("mandatory")


class _TimeDateProfile_Date_Weekday_Type(Integer32):
    """Custom type timeDateProfile_Date_Weekday based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("friday", 7),
          ("monday", 3),
          ("saturday", 8),
          ("sunday", 2),
          ("thursday", 6),
          ("tuesday", 4),
          ("wednesday", 5))
    )


_TimeDateProfile_Date_Weekday_Type.__name__ = "Integer32"
_TimeDateProfile_Date_Weekday_Object = MibScalar
timeDateProfile_Date_Weekday = _TimeDateProfile_Date_Weekday_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 130, 1, 1, 5),
    _TimeDateProfile_Date_Weekday_Type()
)
timeDateProfile_Date_Weekday.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    timeDateProfile_Date_Weekday.setStatus("mandatory")


class _TimeDateProfile_Date_Month_Type(Integer32):
    """Custom type timeDateProfile_Date_Month based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13)
        )
    )
    namedValues = NamedValues(
        *(("april", 5),
          ("august", 9),
          ("december", 13),
          ("february", 3),
          ("january", 2),
          ("july", 8),
          ("june", 7),
          ("march", 4),
          ("may", 6),
          ("november", 12),
          ("october", 11),
          ("september", 10))
    )


_TimeDateProfile_Date_Month_Type.__name__ = "Integer32"
_TimeDateProfile_Date_Month_Object = MibScalar
timeDateProfile_Date_Month = _TimeDateProfile_Date_Month_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 130, 1, 1, 6),
    _TimeDateProfile_Date_Month_Type()
)
timeDateProfile_Date_Month.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    timeDateProfile_Date_Month.setStatus("mandatory")
_TimeDateProfile_Date_Year_Type = Integer32
_TimeDateProfile_Date_Year_Object = MibScalar
timeDateProfile_Date_Year = _TimeDateProfile_Date_Year_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 130, 1, 1, 7),
    _TimeDateProfile_Date_Year_Type()
)
timeDateProfile_Date_Year.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    timeDateProfile_Date_Year.setStatus("mandatory")
_TimeDateProfile_Date_Day_Type = Integer32
_TimeDateProfile_Date_Day_Object = MibScalar
timeDateProfile_Date_Day = _TimeDateProfile_Date_Day_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 130, 1, 1, 8),
    _TimeDateProfile_Date_Day_Type()
)
timeDateProfile_Date_Day.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    timeDateProfile_Date_Day.setStatus("mandatory")


class _TimeDateProfile_Action_o_Type(Integer32):
    """Custom type timeDateProfile_Action_o based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("createProfile", 2),
          ("deleteProfile", 3),
          ("noAction", 1))
    )


_TimeDateProfile_Action_o_Type.__name__ = "Integer32"
_TimeDateProfile_Action_o_Object = MibScalar
timeDateProfile_Action_o = _TimeDateProfile_Action_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 130, 1, 1, 9),
    _TimeDateProfile_Action_o_Type()
)
timeDateProfile_Action_o.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    timeDateProfile_Action_o.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ASCEND-MIBTIME-MIB",
    **{"DisplayString": DisplayString,
       "mibtimeDateProfile": mibtimeDateProfile,
       "mibtimeDateProfileTable": mibtimeDateProfileTable,
       "mibtimeDateProfileEntry": mibtimeDateProfileEntry,
       "timeDateProfile-Index-o": timeDateProfile_Index_o,
       "timeDateProfile-Time-Hour": timeDateProfile_Time_Hour,
       "timeDateProfile-Time-Minute": timeDateProfile_Time_Minute,
       "timeDateProfile-Time-Second": timeDateProfile_Time_Second,
       "timeDateProfile-Date-Weekday": timeDateProfile_Date_Weekday,
       "timeDateProfile-Date-Month": timeDateProfile_Date_Month,
       "timeDateProfile-Date-Year": timeDateProfile_Date_Year,
       "timeDateProfile-Date-Day": timeDateProfile_Date_Day,
       "timeDateProfile-Action-o": timeDateProfile_Action_o}
)
