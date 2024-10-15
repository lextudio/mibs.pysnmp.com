# SNMP MIB module (ASCEND-MIBSYS1-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ASCEND-MIBSYS1-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:42:23 2024
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

_MibsystemProfile_ObjectIdentity = ObjectIdentity
mibsystemProfile = _MibsystemProfile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 529, 23, 125)
)
_MibsystemProfileTable_Object = MibTable
mibsystemProfileTable = _MibsystemProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 125, 1)
)
if mibBuilder.loadTexts:
    mibsystemProfileTable.setStatus("mandatory")
_MibsystemProfileEntry_Object = MibTableRow
mibsystemProfileEntry = _MibsystemProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 125, 1, 1)
)
mibsystemProfileEntry.setIndexNames(
    (0, "ASCEND-MIBSYS1-MIB", "systemProfile-Index-o"),
)
if mibBuilder.loadTexts:
    mibsystemProfileEntry.setStatus("mandatory")
_SystemProfile_Index_o_Type = Integer32
_SystemProfile_Index_o_Object = MibScalar
systemProfile_Index_o = _SystemProfile_Index_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 125, 1, 1, 1),
    _SystemProfile_Index_o_Type()
)
systemProfile_Index_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemProfile_Index_o.setStatus("mandatory")
_SystemProfile_Name_Type = DisplayString
_SystemProfile_Name_Object = MibScalar
systemProfile_Name = _SystemProfile_Name_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 125, 1, 1, 2),
    _SystemProfile_Name_Type()
)
systemProfile_Name.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemProfile_Name.setStatus("mandatory")
_SystemProfile_Contact_Type = DisplayString
_SystemProfile_Contact_Object = MibScalar
systemProfile_Contact = _SystemProfile_Contact_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 125, 1, 1, 3),
    _SystemProfile_Contact_Type()
)
systemProfile_Contact.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemProfile_Contact.setStatus("mandatory")
_SystemProfile_Location_Type = DisplayString
_SystemProfile_Location_Object = MibScalar
systemProfile_Location = _SystemProfile_Location_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 125, 1, 1, 4),
    _SystemProfile_Location_Type()
)
systemProfile_Location.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemProfile_Location.setStatus("mandatory")


class _SystemProfile_TermRate_Type(Integer32):
    """Custom type systemProfile_TermRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("n-115200Bps", 9),
          ("n-1200Bps", 2),
          ("n-19200Bps", 6),
          ("n-2400Bps", 3),
          ("n-300Bps", 1),
          ("n-38400Bps", 7),
          ("n-4800Bps", 4),
          ("n-57600Bps", 8),
          ("n-9600Bps", 5))
    )


_SystemProfile_TermRate_Type.__name__ = "Integer32"
_SystemProfile_TermRate_Object = MibScalar
systemProfile_TermRate = _SystemProfile_TermRate_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 125, 1, 1, 5),
    _SystemProfile_TermRate_Type()
)
systemProfile_TermRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemProfile_TermRate.setStatus("mandatory")


class _SystemProfile_Console_Type(Integer32):
    """Custom type systemProfile_Console based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("limited", 2),
          ("mif", 3),
          ("standard", 1))
    )


_SystemProfile_Console_Type.__name__ = "Integer32"
_SystemProfile_Console_Object = MibScalar
systemProfile_Console = _SystemProfile_Console_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 125, 1, 1, 6),
    _SystemProfile_Console_Type()
)
systemProfile_Console.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemProfile_Console.setStatus("mandatory")


class _SystemProfile_ConsoleSecurity_Type(Integer32):
    """Custom type systemProfile_ConsoleSecurity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("consoleSecurityAuthSetting", 3),
          ("consoleSecurityNone", 1),
          ("consoleSecurityProfile", 2))
    )


_SystemProfile_ConsoleSecurity_Type.__name__ = "Integer32"
_SystemProfile_ConsoleSecurity_Object = MibScalar
systemProfile_ConsoleSecurity = _SystemProfile_ConsoleSecurity_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 125, 1, 1, 7),
    _SystemProfile_ConsoleSecurity_Type()
)
systemProfile_ConsoleSecurity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemProfile_ConsoleSecurity.setStatus("mandatory")


class _SystemProfile_SystemRmtMgmt_Type(Integer32):
    """Custom type systemProfile_SystemRmtMgmt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_SystemProfile_SystemRmtMgmt_Type.__name__ = "Integer32"
_SystemProfile_SystemRmtMgmt_Object = MibScalar
systemProfile_SystemRmtMgmt = _SystemProfile_SystemRmtMgmt_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 125, 1, 1, 8),
    _SystemProfile_SystemRmtMgmt_Type()
)
systemProfile_SystemRmtMgmt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemProfile_SystemRmtMgmt.setStatus("mandatory")


class _SystemProfile_SubAddressMode_Type(Integer32):
    """Custom type systemProfile_SubAddressMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("noSubaddress", 1),
          ("routingSubaddress", 2),
          ("termselSubaddress", 3))
    )


_SystemProfile_SubAddressMode_Type.__name__ = "Integer32"
_SystemProfile_SubAddressMode_Object = MibScalar
systemProfile_SubAddressMode = _SystemProfile_SubAddressMode_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 125, 1, 1, 9),
    _SystemProfile_SubAddressMode_Type()
)
systemProfile_SubAddressMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemProfile_SubAddressMode.setStatus("mandatory")
_SystemProfile_SerialSubaddress_Type = Integer32
_SystemProfile_SerialSubaddress_Object = MibScalar
systemProfile_SerialSubaddress = _SystemProfile_SerialSubaddress_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 125, 1, 1, 10),
    _SystemProfile_SerialSubaddress_Type()
)
systemProfile_SerialSubaddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemProfile_SerialSubaddress.setStatus("mandatory")
_SystemProfile_LanSubaddress_Type = Integer32
_SystemProfile_LanSubaddress_Object = MibScalar
systemProfile_LanSubaddress = _SystemProfile_LanSubaddress_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 125, 1, 1, 11),
    _SystemProfile_LanSubaddress_Type()
)
systemProfile_LanSubaddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemProfile_LanSubaddress.setStatus("mandatory")
_SystemProfile_DmSubaddress_Type = Integer32
_SystemProfile_DmSubaddress_Object = MibScalar
systemProfile_DmSubaddress = _SystemProfile_DmSubaddress_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 125, 1, 1, 12),
    _SystemProfile_DmSubaddress_Type()
)
systemProfile_DmSubaddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemProfile_DmSubaddress.setStatus("mandatory")
_SystemProfile_V110Subaddress_Type = Integer32
_SystemProfile_V110Subaddress_Object = MibScalar
systemProfile_V110Subaddress = _SystemProfile_V110Subaddress_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 125, 1, 1, 13),
    _SystemProfile_V110Subaddress_Type()
)
systemProfile_V110Subaddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemProfile_V110Subaddress.setStatus("mandatory")


class _SystemProfile_UseTrunkGroups_Type(Integer32):
    """Custom type systemProfile_UseTrunkGroups based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_SystemProfile_UseTrunkGroups_Type.__name__ = "Integer32"
_SystemProfile_UseTrunkGroups_Object = MibScalar
systemProfile_UseTrunkGroups = _SystemProfile_UseTrunkGroups_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 125, 1, 1, 14),
    _SystemProfile_UseTrunkGroups_Type()
)
systemProfile_UseTrunkGroups.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemProfile_UseTrunkGroups.setStatus("mandatory")
_SystemProfile_NumDigitsTrunkGroups_Type = Integer32
_SystemProfile_NumDigitsTrunkGroups_Object = MibScalar
systemProfile_NumDigitsTrunkGroups = _SystemProfile_NumDigitsTrunkGroups_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 125, 1, 1, 15),
    _SystemProfile_NumDigitsTrunkGroups_Type()
)
systemProfile_NumDigitsTrunkGroups.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemProfile_NumDigitsTrunkGroups.setStatus("mandatory")


class _SystemProfile_AutoLogout_Type(Integer32):
    """Custom type systemProfile_AutoLogout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_SystemProfile_AutoLogout_Type.__name__ = "Integer32"
_SystemProfile_AutoLogout_Object = MibScalar
systemProfile_AutoLogout = _SystemProfile_AutoLogout_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 125, 1, 1, 16),
    _SystemProfile_AutoLogout_Type()
)
systemProfile_AutoLogout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemProfile_AutoLogout.setStatus("mandatory")
_SystemProfile_IdleLogout_Type = Integer32
_SystemProfile_IdleLogout_Object = MibScalar
systemProfile_IdleLogout = _SystemProfile_IdleLogout_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 125, 1, 1, 17),
    _SystemProfile_IdleLogout_Type()
)
systemProfile_IdleLogout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemProfile_IdleLogout.setStatus("mandatory")


class _SystemProfile_P50SwitchUsage_Type(Integer32):
    """Custom type systemProfile_P50SwitchUsage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("switchNumberOfUses", 3),
          ("switchSerialWan", 2),
          ("switchUnused", 1))
    )


_SystemProfile_P50SwitchUsage_Type.__name__ = "Integer32"
_SystemProfile_P50SwitchUsage_Object = MibScalar
systemProfile_P50SwitchUsage = _SystemProfile_P50SwitchUsage_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 125, 1, 1, 18),
    _SystemProfile_P50SwitchUsage_Type()
)
systemProfile_P50SwitchUsage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemProfile_P50SwitchUsage.setStatus("mandatory")


class _SystemProfile_oDS0MinRst_Type(Integer32):
    """Custom type systemProfile_oDS0MinRst based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("daily", 2),
          ("monthly", 3),
          ("off", 1))
    )


_SystemProfile_oDS0MinRst_Type.__name__ = "Integer32"
_SystemProfile_oDS0MinRst_Object = MibScalar
systemProfile_oDS0MinRst = _SystemProfile_oDS0MinRst_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 125, 1, 1, 19),
    _SystemProfile_oDS0MinRst_Type()
)
systemProfile_oDS0MinRst.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemProfile_oDS0MinRst.setStatus("mandatory")
_SystemProfile_MaxSystemDS0Mins_Type = Integer32
_SystemProfile_MaxSystemDS0Mins_Object = MibScalar
systemProfile_MaxSystemDS0Mins = _SystemProfile_MaxSystemDS0Mins_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 125, 1, 1, 20),
    _SystemProfile_MaxSystemDS0Mins_Type()
)
systemProfile_MaxSystemDS0Mins.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemProfile_MaxSystemDS0Mins.setStatus("mandatory")
_SystemProfile_MaxDialoutTime_Type = Integer32
_SystemProfile_MaxDialoutTime_Object = MibScalar
systemProfile_MaxDialoutTime = _SystemProfile_MaxDialoutTime_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 125, 1, 1, 21),
    _SystemProfile_MaxDialoutTime_Type()
)
systemProfile_MaxDialoutTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemProfile_MaxDialoutTime.setStatus("mandatory")
_SystemProfile_ParallelDialing_Type = Integer32
_SystemProfile_ParallelDialing_Object = MibScalar
systemProfile_ParallelDialing = _SystemProfile_ParallelDialing_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 125, 1, 1, 22),
    _SystemProfile_ParallelDialing_Type()
)
systemProfile_ParallelDialing.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemProfile_ParallelDialing.setStatus("mandatory")


class _SystemProfile_SingleFileIncoming_Type(Integer32):
    """Custom type systemProfile_SingleFileIncoming based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_SystemProfile_SingleFileIncoming_Type.__name__ = "Integer32"
_SystemProfile_SingleFileIncoming_Object = MibScalar
systemProfile_SingleFileIncoming = _SystemProfile_SingleFileIncoming_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 125, 1, 1, 23),
    _SystemProfile_SingleFileIncoming_Type()
)
systemProfile_SingleFileIncoming.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemProfile_SingleFileIncoming.setStatus("mandatory")


class _SystemProfile_DelayDualPortDialing_Type(Integer32):
    """Custom type systemProfile_DelayDualPortDialing based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_SystemProfile_DelayDualPortDialing_Type.__name__ = "Integer32"
_SystemProfile_DelayDualPortDialing_Object = MibScalar
systemProfile_DelayDualPortDialing = _SystemProfile_DelayDualPortDialing_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 125, 1, 1, 24),
    _SystemProfile_DelayDualPortDialing_Type()
)
systemProfile_DelayDualPortDialing.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemProfile_DelayDualPortDialing.setStatus("mandatory")
_SystemProfile_EditNumber_Type = DisplayString
_SystemProfile_EditNumber_Object = MibScalar
systemProfile_EditNumber = _SystemProfile_EditNumber_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 125, 1, 1, 25),
    _SystemProfile_EditNumber_Type()
)
systemProfile_EditNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemProfile_EditNumber.setStatus("mandatory")


class _SystemProfile_AnalogEncoding_Type(Integer32):
    """Custom type systemProfile_AnalogEncoding based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("aLaw", 2),
          ("uLaw", 1))
    )


_SystemProfile_AnalogEncoding_Type.__name__ = "Integer32"
_SystemProfile_AnalogEncoding_Object = MibScalar
systemProfile_AnalogEncoding = _SystemProfile_AnalogEncoding_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 125, 1, 1, 26),
    _SystemProfile_AnalogEncoding_Type()
)
systemProfile_AnalogEncoding.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemProfile_AnalogEncoding.setStatus("mandatory")
_SystemProfile_SessionidBase_Type = Integer32
_SystemProfile_SessionidBase_Object = MibScalar
systemProfile_SessionidBase = _SystemProfile_SessionidBase_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 125, 1, 1, 27),
    _SystemProfile_SessionidBase_Type()
)
systemProfile_SessionidBase.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemProfile_SessionidBase.setStatus("mandatory")


class _SystemProfile_TOnline_Type(Integer32):
    """Custom type systemProfile_TOnline based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_SystemProfile_TOnline_Type.__name__ = "Integer32"
_SystemProfile_TOnline_Object = MibScalar
systemProfile_TOnline = _SystemProfile_TOnline_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 125, 1, 1, 28),
    _SystemProfile_TOnline_Type()
)
systemProfile_TOnline.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemProfile_TOnline.setStatus("mandatory")


class _SystemProfile_TOnlineMostAvailChan_Type(Integer32):
    """Custom type systemProfile_TOnlineMostAvailChan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_SystemProfile_TOnlineMostAvailChan_Type.__name__ = "Integer32"
_SystemProfile_TOnlineMostAvailChan_Object = MibScalar
systemProfile_TOnlineMostAvailChan = _SystemProfile_TOnlineMostAvailChan_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 125, 1, 1, 29),
    _SystemProfile_TOnlineMostAvailChan_Type()
)
systemProfile_TOnlineMostAvailChan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemProfile_TOnlineMostAvailChan.setStatus("mandatory")
_SystemProfile_T302Timer_Type = Integer32
_SystemProfile_T302Timer_Object = MibScalar
systemProfile_T302Timer = _SystemProfile_T302Timer_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 125, 1, 1, 30),
    _SystemProfile_T302Timer_Type()
)
systemProfile_T302Timer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemProfile_T302Timer.setStatus("mandatory")


class _SystemProfile_CallRoutingSortMethod_Type(Integer32):
    """Custom type systemProfile_CallRoutingSortMethod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("itemFirst", 1),
          ("slotFirst", 2))
    )


_SystemProfile_CallRoutingSortMethod_Type.__name__ = "Integer32"
_SystemProfile_CallRoutingSortMethod_Object = MibScalar
systemProfile_CallRoutingSortMethod = _SystemProfile_CallRoutingSortMethod_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 125, 1, 1, 31),
    _SystemProfile_CallRoutingSortMethod_Type()
)
systemProfile_CallRoutingSortMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemProfile_CallRoutingSortMethod.setStatus("mandatory")


class _SystemProfile_DigitalCallRoutingSortMethod_Type(Integer32):
    """Custom type systemProfile_DigitalCallRoutingSortMethod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("itemFirst", 1),
          ("slotFirst", 2))
    )


_SystemProfile_DigitalCallRoutingSortMethod_Type.__name__ = "Integer32"
_SystemProfile_DigitalCallRoutingSortMethod_Object = MibScalar
systemProfile_DigitalCallRoutingSortMethod = _SystemProfile_DigitalCallRoutingSortMethod_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 125, 1, 1, 32),
    _SystemProfile_DigitalCallRoutingSortMethod_Type()
)
systemProfile_DigitalCallRoutingSortMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemProfile_DigitalCallRoutingSortMethod.setStatus("mandatory")


class _SystemProfile_ExactMatchCallRouting_Type(Integer32):
    """Custom type systemProfile_ExactMatchCallRouting based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_SystemProfile_ExactMatchCallRouting_Type.__name__ = "Integer32"
_SystemProfile_ExactMatchCallRouting_Object = MibScalar
systemProfile_ExactMatchCallRouting = _SystemProfile_ExactMatchCallRouting_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 125, 1, 1, 33),
    _SystemProfile_ExactMatchCallRouting_Type()
)
systemProfile_ExactMatchCallRouting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemProfile_ExactMatchCallRouting.setStatus("mandatory")


class _SystemProfile_ShelfControllerType_Type(Integer32):
    """Custom type systemProfile_ShelfControllerType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("master", 2),
          ("slave", 3),
          ("standalone", 1))
    )


_SystemProfile_ShelfControllerType_Type.__name__ = "Integer32"
_SystemProfile_ShelfControllerType_Object = MibScalar
systemProfile_ShelfControllerType = _SystemProfile_ShelfControllerType_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 125, 1, 1, 34),
    _SystemProfile_ShelfControllerType_Type()
)
systemProfile_ShelfControllerType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemProfile_ShelfControllerType.setStatus("mandatory")
_SystemProfile_MasterShelfController_Type = Integer32
_SystemProfile_MasterShelfController_Object = MibScalar
systemProfile_MasterShelfController = _SystemProfile_MasterShelfController_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 125, 1, 1, 35),
    _SystemProfile_MasterShelfController_Type()
)
systemProfile_MasterShelfController.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemProfile_MasterShelfController.setStatus("mandatory")


class _SystemProfile_NewNasPortIdFormat_Type(Integer32):
    """Custom type systemProfile_NewNasPortIdFormat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_SystemProfile_NewNasPortIdFormat_Type.__name__ = "Integer32"
_SystemProfile_NewNasPortIdFormat_Object = MibScalar
systemProfile_NewNasPortIdFormat = _SystemProfile_NewNasPortIdFormat_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 125, 1, 1, 36),
    _SystemProfile_NewNasPortIdFormat_Type()
)
systemProfile_NewNasPortIdFormat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemProfile_NewNasPortIdFormat.setStatus("mandatory")
_SystemProfile_ModemPriTypeOfNumber_Type = Integer32
_SystemProfile_ModemPriTypeOfNumber_Object = MibScalar
systemProfile_ModemPriTypeOfNumber = _SystemProfile_ModemPriTypeOfNumber_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 125, 1, 1, 37),
    _SystemProfile_ModemPriTypeOfNumber_Type()
)
systemProfile_ModemPriTypeOfNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemProfile_ModemPriTypeOfNumber.setStatus("mandatory")
_SystemProfile_ModemPriNumberingPlanId_Type = Integer32
_SystemProfile_ModemPriNumberingPlanId_Object = MibScalar
systemProfile_ModemPriNumberingPlanId = _SystemProfile_ModemPriNumberingPlanId_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 125, 1, 1, 38),
    _SystemProfile_ModemPriNumberingPlanId_Type()
)
systemProfile_ModemPriNumberingPlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemProfile_ModemPriNumberingPlanId.setStatus("mandatory")


class _SystemProfile_WanInterface_Type(Integer32):
    """Custom type systemProfile_WanInterface based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("wanSwan", 2),
          ("wanT1", 1))
    )


_SystemProfile_WanInterface_Type.__name__ = "Integer32"
_SystemProfile_WanInterface_Object = MibScalar
systemProfile_WanInterface = _SystemProfile_WanInterface_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 125, 1, 1, 39),
    _SystemProfile_WanInterface_Type()
)
systemProfile_WanInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemProfile_WanInterface.setStatus("mandatory")


class _SystemProfile_PermConnUpdMode_Type(Integer32):
    """Custom type systemProfile_PermConnUpdMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("all", 1),
          ("changed", 2))
    )


_SystemProfile_PermConnUpdMode_Type.__name__ = "Integer32"
_SystemProfile_PermConnUpdMode_Object = MibScalar
systemProfile_PermConnUpdMode = _SystemProfile_PermConnUpdMode_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 125, 1, 1, 40),
    _SystemProfile_PermConnUpdMode_Type()
)
systemProfile_PermConnUpdMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemProfile_PermConnUpdMode.setStatus("mandatory")
_SystemProfile_UserstatFormat_Type = DisplayString
_SystemProfile_UserstatFormat_Object = MibScalar
systemProfile_UserstatFormat = _SystemProfile_UserstatFormat_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 125, 1, 1, 41),
    _SystemProfile_UserstatFormat_Type()
)
systemProfile_UserstatFormat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemProfile_UserstatFormat.setStatus("mandatory")


class _SystemProfile_ControlBusType_Type(Integer32):
    """Custom type systemProfile_ControlBusType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dpram", 1),
          ("pbus", 2))
    )


_SystemProfile_ControlBusType_Type.__name__ = "Integer32"
_SystemProfile_ControlBusType_Object = MibScalar
systemProfile_ControlBusType = _SystemProfile_ControlBusType_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 125, 1, 1, 42),
    _SystemProfile_ControlBusType_Type()
)
systemProfile_ControlBusType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemProfile_ControlBusType.setStatus("mandatory")
_SystemProfile_BootSrVersion_Type = DisplayString
_SystemProfile_BootSrVersion_Object = MibScalar
systemProfile_BootSrVersion = _SystemProfile_BootSrVersion_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 125, 1, 1, 43),
    _SystemProfile_BootSrVersion_Type()
)
systemProfile_BootSrVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemProfile_BootSrVersion.setStatus("mandatory")
_SystemProfile_SysModemProfile_oATAnswerString_Type = DisplayString
_SystemProfile_SysModemProfile_oATAnswerString_Object = MibScalar
systemProfile_SysModemProfile_oATAnswerString = _SystemProfile_SysModemProfile_oATAnswerString_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 125, 1, 1, 44),
    _SystemProfile_SysModemProfile_oATAnswerString_Type()
)
systemProfile_SysModemProfile_oATAnswerString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemProfile_SysModemProfile_oATAnswerString.setStatus("mandatory")
_SystemProfile_CallByCall_Type = Integer32
_SystemProfile_CallByCall_Object = MibScalar
systemProfile_CallByCall = _SystemProfile_CallByCall_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 125, 1, 1, 45),
    _SystemProfile_CallByCall_Type()
)
systemProfile_CallByCall.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemProfile_CallByCall.setStatus("mandatory")


class _SystemProfile_Country_Type(Integer32):
    """Custom type systemProfile_Country based on Integer32"""
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
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23)
        )
    )
    namedValues = NamedValues(
        *(("argentina", 2),
          ("australia", 3),
          ("belgium", 4),
          ("brazil", 23),
          ("china", 5),
          ("costaRica", 6),
          ("finland", 7),
          ("france", 8),
          ("germany", 9),
          ("hongKong", 10),
          ("italy", 11),
          ("japan", 12),
          ("korea", 13),
          ("mexico", 14),
          ("netherlands", 15),
          ("newZealand", 16),
          ("singapore", 17),
          ("spain", 18),
          ("sweden", 19),
          ("switzerland", 20),
          ("uk", 21),
          ("us", 22))
    )


_SystemProfile_Country_Type.__name__ = "Integer32"
_SystemProfile_Country_Object = MibScalar
systemProfile_Country = _SystemProfile_Country_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 125, 1, 1, 46),
    _SystemProfile_Country_Type()
)
systemProfile_Country.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemProfile_Country.setStatus("mandatory")
_SystemProfile_PotsDigitTimeout_Type = Integer32
_SystemProfile_PotsDigitTimeout_Object = MibScalar
systemProfile_PotsDigitTimeout = _SystemProfile_PotsDigitTimeout_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 125, 1, 1, 47),
    _SystemProfile_PotsDigitTimeout_Type()
)
systemProfile_PotsDigitTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemProfile_PotsDigitTimeout.setStatus("mandatory")


class _SystemProfile_System8kClock_Type(Integer32):
    """Custom type systemProfile_System8kClock based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("ami8k", 5),
          ("bits", 4),
          ("controller", 2),
          ("limOrTrunkModule", 3))
    )


_SystemProfile_System8kClock_Type.__name__ = "Integer32"
_SystemProfile_System8kClock_Object = MibScalar
systemProfile_System8kClock = _SystemProfile_System8kClock_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 125, 1, 1, 48),
    _SystemProfile_System8kClock_Type()
)
systemProfile_System8kClock.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemProfile_System8kClock.setStatus("mandatory")


class _SystemProfile_SupportDbcs_Type(Integer32):
    """Custom type systemProfile_SupportDbcs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_SystemProfile_SupportDbcs_Type.__name__ = "Integer32"
_SystemProfile_SupportDbcs_Object = MibScalar
systemProfile_SupportDbcs = _SystemProfile_SupportDbcs_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 125, 1, 1, 49),
    _SystemProfile_SupportDbcs_Type()
)
systemProfile_SupportDbcs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemProfile_SupportDbcs.setStatus("mandatory")


class _SystemProfile_IncCallDistrib_Type(Integer32):
    """Custom type systemProfile_IncCallDistrib based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("fairShare", 3),
          ("firstAvailable", 2))
    )


_SystemProfile_IncCallDistrib_Type.__name__ = "Integer32"
_SystemProfile_IncCallDistrib_Object = MibScalar
systemProfile_IncCallDistrib = _SystemProfile_IncCallDistrib_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 125, 1, 1, 50),
    _SystemProfile_IncCallDistrib_Type()
)
systemProfile_IncCallDistrib.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemProfile_IncCallDistrib.setStatus("mandatory")


class _SystemProfile_IgnoreLineup_Type(Integer32):
    """Custom type systemProfile_IgnoreLineup based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_SystemProfile_IgnoreLineup_Type.__name__ = "Integer32"
_SystemProfile_IgnoreLineup_Object = MibScalar
systemProfile_IgnoreLineup = _SystemProfile_IgnoreLineup_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 125, 1, 1, 51),
    _SystemProfile_IgnoreLineup_Type()
)
systemProfile_IgnoreLineup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemProfile_IgnoreLineup.setStatus("mandatory")


class _SystemProfile_Action_o_Type(Integer32):
    """Custom type systemProfile_Action_o based on Integer32"""
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


_SystemProfile_Action_o_Type.__name__ = "Integer32"
_SystemProfile_Action_o_Object = MibScalar
systemProfile_Action_o = _SystemProfile_Action_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 125, 1, 1, 52),
    _SystemProfile_Action_o_Type()
)
systemProfile_Action_o.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemProfile_Action_o.setStatus("mandatory")
_SystemProfile_JamFileComponents_JamFile1_Type = DisplayString
_SystemProfile_JamFileComponents_JamFile1_Object = MibScalar
systemProfile_JamFileComponents_JamFile1 = _SystemProfile_JamFileComponents_JamFile1_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 125, 1, 1, 53),
    _SystemProfile_JamFileComponents_JamFile1_Type()
)
systemProfile_JamFileComponents_JamFile1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemProfile_JamFileComponents_JamFile1.setStatus("mandatory")
_SystemProfile_JamFileComponents_JamFile2_Type = DisplayString
_SystemProfile_JamFileComponents_JamFile2_Object = MibScalar
systemProfile_JamFileComponents_JamFile2 = _SystemProfile_JamFileComponents_JamFile2_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 125, 1, 1, 54),
    _SystemProfile_JamFileComponents_JamFile2_Type()
)
systemProfile_JamFileComponents_JamFile2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemProfile_JamFileComponents_JamFile2.setStatus("mandatory")
_SystemProfile_JamFileComponents_JamFile3_Type = DisplayString
_SystemProfile_JamFileComponents_JamFile3_Object = MibScalar
systemProfile_JamFileComponents_JamFile3 = _SystemProfile_JamFileComponents_JamFile3_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 125, 1, 1, 55),
    _SystemProfile_JamFileComponents_JamFile3_Type()
)
systemProfile_JamFileComponents_JamFile3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemProfile_JamFileComponents_JamFile3.setStatus("mandatory")
_SystemProfile_JamFileComponents_JamFile4_Type = DisplayString
_SystemProfile_JamFileComponents_JamFile4_Object = MibScalar
systemProfile_JamFileComponents_JamFile4 = _SystemProfile_JamFileComponents_JamFile4_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 125, 1, 1, 56),
    _SystemProfile_JamFileComponents_JamFile4_Type()
)
systemProfile_JamFileComponents_JamFile4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemProfile_JamFileComponents_JamFile4.setStatus("mandatory")
_SystemProfile_JamFileComponents_JamFile5_Type = DisplayString
_SystemProfile_JamFileComponents_JamFile5_Object = MibScalar
systemProfile_JamFileComponents_JamFile5 = _SystemProfile_JamFileComponents_JamFile5_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 125, 1, 1, 57),
    _SystemProfile_JamFileComponents_JamFile5_Type()
)
systemProfile_JamFileComponents_JamFile5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemProfile_JamFileComponents_JamFile5.setStatus("mandatory")
_SystemProfile_JamFileComponents_JamFile6_Type = DisplayString
_SystemProfile_JamFileComponents_JamFile6_Object = MibScalar
systemProfile_JamFileComponents_JamFile6 = _SystemProfile_JamFileComponents_JamFile6_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 125, 1, 1, 58),
    _SystemProfile_JamFileComponents_JamFile6_Type()
)
systemProfile_JamFileComponents_JamFile6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemProfile_JamFileComponents_JamFile6.setStatus("mandatory")


class _SystemProfile_NasPortFormat_Type(Integer32):
    """Custom type systemProfile_NasPortFormat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("n-122", 4),
          ("n-1233", 5),
          ("n-2455", 2),
          ("n-655", 3),
          ("notApplicable", 1))
    )


_SystemProfile_NasPortFormat_Type.__name__ = "Integer32"
_SystemProfile_NasPortFormat_Object = MibScalar
systemProfile_NasPortFormat = _SystemProfile_NasPortFormat_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 125, 1, 1, 59),
    _SystemProfile_NasPortFormat_Type()
)
systemProfile_NasPortFormat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemProfile_NasPortFormat.setStatus("mandatory")
_MibsystemProfile_StatusNumberTable_Object = MibTable
mibsystemProfile_StatusNumberTable = _MibsystemProfile_StatusNumberTable_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 125, 2)
)
if mibBuilder.loadTexts:
    mibsystemProfile_StatusNumberTable.setStatus("mandatory")
_MibsystemProfile_StatusNumberEntry_Object = MibTableRow
mibsystemProfile_StatusNumberEntry = _MibsystemProfile_StatusNumberEntry_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 125, 2, 1)
)
mibsystemProfile_StatusNumberEntry.setIndexNames(
    (0, "ASCEND-MIBSYS1-MIB", "systemProfile-StatusNumber-Index-o"),
    (0, "ASCEND-MIBSYS1-MIB", "systemProfile-StatusNumber-Index1-o"),
)
if mibBuilder.loadTexts:
    mibsystemProfile_StatusNumberEntry.setStatus("mandatory")
_SystemProfile_StatusNumber_Index_o_Type = Integer32
_SystemProfile_StatusNumber_Index_o_Object = MibScalar
systemProfile_StatusNumber_Index_o = _SystemProfile_StatusNumber_Index_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 125, 2, 1, 1),
    _SystemProfile_StatusNumber_Index_o_Type()
)
systemProfile_StatusNumber_Index_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemProfile_StatusNumber_Index_o.setStatus("mandatory")
_SystemProfile_StatusNumber_Index1_o_Type = Integer32
_SystemProfile_StatusNumber_Index1_o_Object = MibScalar
systemProfile_StatusNumber_Index1_o = _SystemProfile_StatusNumber_Index1_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 125, 2, 1, 2),
    _SystemProfile_StatusNumber_Index1_o_Type()
)
systemProfile_StatusNumber_Index1_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemProfile_StatusNumber_Index1_o.setStatus("mandatory")
_SystemProfile_StatusNumber_Type = DisplayString
_SystemProfile_StatusNumber_Object = MibScalar
systemProfile_StatusNumber = _SystemProfile_StatusNumber_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 125, 2, 1, 3),
    _SystemProfile_StatusNumber_Type()
)
systemProfile_StatusNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemProfile_StatusNumber.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ASCEND-MIBSYS1-MIB",
    **{"DisplayString": DisplayString,
       "mibsystemProfile": mibsystemProfile,
       "mibsystemProfileTable": mibsystemProfileTable,
       "mibsystemProfileEntry": mibsystemProfileEntry,
       "systemProfile-Index-o": systemProfile_Index_o,
       "systemProfile-Name": systemProfile_Name,
       "systemProfile-Contact": systemProfile_Contact,
       "systemProfile-Location": systemProfile_Location,
       "systemProfile-TermRate": systemProfile_TermRate,
       "systemProfile-Console": systemProfile_Console,
       "systemProfile-ConsoleSecurity": systemProfile_ConsoleSecurity,
       "systemProfile-SystemRmtMgmt": systemProfile_SystemRmtMgmt,
       "systemProfile-SubAddressMode": systemProfile_SubAddressMode,
       "systemProfile-SerialSubaddress": systemProfile_SerialSubaddress,
       "systemProfile-LanSubaddress": systemProfile_LanSubaddress,
       "systemProfile-DmSubaddress": systemProfile_DmSubaddress,
       "systemProfile-V110Subaddress": systemProfile_V110Subaddress,
       "systemProfile-UseTrunkGroups": systemProfile_UseTrunkGroups,
       "systemProfile-NumDigitsTrunkGroups": systemProfile_NumDigitsTrunkGroups,
       "systemProfile-AutoLogout": systemProfile_AutoLogout,
       "systemProfile-IdleLogout": systemProfile_IdleLogout,
       "systemProfile-P50SwitchUsage": systemProfile_P50SwitchUsage,
       "systemProfile-oDS0MinRst": systemProfile_oDS0MinRst,
       "systemProfile-MaxSystemDS0Mins": systemProfile_MaxSystemDS0Mins,
       "systemProfile-MaxDialoutTime": systemProfile_MaxDialoutTime,
       "systemProfile-ParallelDialing": systemProfile_ParallelDialing,
       "systemProfile-SingleFileIncoming": systemProfile_SingleFileIncoming,
       "systemProfile-DelayDualPortDialing": systemProfile_DelayDualPortDialing,
       "systemProfile-EditNumber": systemProfile_EditNumber,
       "systemProfile-AnalogEncoding": systemProfile_AnalogEncoding,
       "systemProfile-SessionidBase": systemProfile_SessionidBase,
       "systemProfile-TOnline": systemProfile_TOnline,
       "systemProfile-TOnlineMostAvailChan": systemProfile_TOnlineMostAvailChan,
       "systemProfile-T302Timer": systemProfile_T302Timer,
       "systemProfile-CallRoutingSortMethod": systemProfile_CallRoutingSortMethod,
       "systemProfile-DigitalCallRoutingSortMethod": systemProfile_DigitalCallRoutingSortMethod,
       "systemProfile-ExactMatchCallRouting": systemProfile_ExactMatchCallRouting,
       "systemProfile-ShelfControllerType": systemProfile_ShelfControllerType,
       "systemProfile-MasterShelfController": systemProfile_MasterShelfController,
       "systemProfile-NewNasPortIdFormat": systemProfile_NewNasPortIdFormat,
       "systemProfile-ModemPriTypeOfNumber": systemProfile_ModemPriTypeOfNumber,
       "systemProfile-ModemPriNumberingPlanId": systemProfile_ModemPriNumberingPlanId,
       "systemProfile-WanInterface": systemProfile_WanInterface,
       "systemProfile-PermConnUpdMode": systemProfile_PermConnUpdMode,
       "systemProfile-UserstatFormat": systemProfile_UserstatFormat,
       "systemProfile-ControlBusType": systemProfile_ControlBusType,
       "systemProfile-BootSrVersion": systemProfile_BootSrVersion,
       "systemProfile-SysModemProfile-oATAnswerString": systemProfile_SysModemProfile_oATAnswerString,
       "systemProfile-CallByCall": systemProfile_CallByCall,
       "systemProfile-Country": systemProfile_Country,
       "systemProfile-PotsDigitTimeout": systemProfile_PotsDigitTimeout,
       "systemProfile-System8kClock": systemProfile_System8kClock,
       "systemProfile-SupportDbcs": systemProfile_SupportDbcs,
       "systemProfile-IncCallDistrib": systemProfile_IncCallDistrib,
       "systemProfile-IgnoreLineup": systemProfile_IgnoreLineup,
       "systemProfile-Action-o": systemProfile_Action_o,
       "systemProfile-JamFileComponents-JamFile1": systemProfile_JamFileComponents_JamFile1,
       "systemProfile-JamFileComponents-JamFile2": systemProfile_JamFileComponents_JamFile2,
       "systemProfile-JamFileComponents-JamFile3": systemProfile_JamFileComponents_JamFile3,
       "systemProfile-JamFileComponents-JamFile4": systemProfile_JamFileComponents_JamFile4,
       "systemProfile-JamFileComponents-JamFile5": systemProfile_JamFileComponents_JamFile5,
       "systemProfile-JamFileComponents-JamFile6": systemProfile_JamFileComponents_JamFile6,
       "systemProfile-NasPortFormat": systemProfile_NasPortFormat,
       "mibsystemProfile-StatusNumberTable": mibsystemProfile_StatusNumberTable,
       "mibsystemProfile-StatusNumberEntry": mibsystemProfile_StatusNumberEntry,
       "systemProfile-StatusNumber-Index-o": systemProfile_StatusNumber_Index_o,
       "systemProfile-StatusNumber-Index1-o": systemProfile_StatusNumber_Index1_o,
       "systemProfile-StatusNumber": systemProfile_StatusNumber}
)
