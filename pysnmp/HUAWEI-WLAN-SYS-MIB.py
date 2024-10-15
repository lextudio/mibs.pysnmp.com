# SNMP MIB module (HUAWEI-WLAN-SYS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HUAWEI-WLAN-SYS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:06:44 2024
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

(hwWlan,) = mibBuilder.importSymbols(
    "HUAWEI-WLAN-MIB",
    "hwWlan")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

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

hwWlanSysManagement = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 1)
)
hwWlanSysManagement.setRevisions(
        ("2014-10-23 16:00",
         "2014-03-21 16:00",
         "2013-12-20 09:58",
         "2013-11-12 10:16",
         "2013-11-12 10:16",
         "2013-10-23 17:22",
         "2013-05-23 00:00",
         "2010-11-01 00:00",
         "2010-09-27 00:00",
         "2010-09-15 00:00",
         "2010-09-10 00:00",
         "2010-07-06 00:00",
         "2010-06-08 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HwWlanTrapRestrain_ObjectIdentity = ObjectIdentity
hwWlanTrapRestrain = _HwWlanTrapRestrain_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 1, 1)
)


class _HwWlanTrapRestrainAll_Type(Integer32):
    """Custom type hwWlanTrapRestrainAll based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_HwWlanTrapRestrainAll_Type.__name__ = "Integer32"
_HwWlanTrapRestrainAll_Object = MibScalar
hwWlanTrapRestrainAll = _HwWlanTrapRestrainAll_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 1, 1, 1),
    _HwWlanTrapRestrainAll_Type()
)
hwWlanTrapRestrainAll.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwWlanTrapRestrainAll.setStatus("current")
_HwWlanTrapSeverityRestrain_ObjectIdentity = ObjectIdentity
hwWlanTrapSeverityRestrain = _HwWlanTrapSeverityRestrain_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 1, 1, 2)
)


class _HwWlanTrapSeverityRestrainSeverity_Type(Integer32):
    """Custom type hwWlanTrapSeverityRestrainSeverity based on Integer32"""
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
        *(("critical", 1),
          ("major", 2),
          ("minor", 3),
          ("none", 5),
          ("warning", 4))
    )


_HwWlanTrapSeverityRestrainSeverity_Type.__name__ = "Integer32"
_HwWlanTrapSeverityRestrainSeverity_Object = MibScalar
hwWlanTrapSeverityRestrainSeverity = _HwWlanTrapSeverityRestrainSeverity_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 1, 1, 2, 1),
    _HwWlanTrapSeverityRestrainSeverity_Type()
)
hwWlanTrapSeverityRestrainSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwWlanTrapSeverityRestrainSeverity.setStatus("current")
_HwWlanApRegionTrapRestrain_ObjectIdentity = ObjectIdentity
hwWlanApRegionTrapRestrain = _HwWlanApRegionTrapRestrain_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 1, 1, 3)
)
_HwWlanApRegionTrapRestrainRegionIndexMask_Type = OctetString
_HwWlanApRegionTrapRestrainRegionIndexMask_Object = MibScalar
hwWlanApRegionTrapRestrainRegionIndexMask = _HwWlanApRegionTrapRestrainRegionIndexMask_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 1, 1, 3, 1),
    _HwWlanApRegionTrapRestrainRegionIndexMask_Type()
)
hwWlanApRegionTrapRestrainRegionIndexMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwWlanApRegionTrapRestrainRegionIndexMask.setStatus("current")
_HwWlanApTrapRestrain_ObjectIdentity = ObjectIdentity
hwWlanApTrapRestrain = _HwWlanApTrapRestrain_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 1, 1, 4)
)
_HwWlanApTrapRestrainApIndexMask_Type = OctetString
_HwWlanApTrapRestrainApIndexMask_Object = MibScalar
hwWlanApTrapRestrainApIndexMask = _HwWlanApTrapRestrainApIndexMask_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 1, 1, 4, 1),
    _HwWlanApTrapRestrainApIndexMask_Type()
)
hwWlanApTrapRestrainApIndexMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwWlanApTrapRestrainApIndexMask.setStatus("current")
_HwWlanSysPara_ObjectIdentity = ObjectIdentity
hwWlanSysPara = _HwWlanSysPara_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 1, 2)
)


class _HwWlanCarrierId_Type(Integer32):
    """Custom type hwWlanCarrierId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              65535)
        )
    )
    namedValues = NamedValues(
        *(("cmcc", 1),
          ("ctc", 2),
          ("cuc", 3),
          ("other", 65535))
    )


_HwWlanCarrierId_Type.__name__ = "Integer32"
_HwWlanCarrierId_Object = MibScalar
hwWlanCarrierId = _HwWlanCarrierId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 1, 2, 1),
    _HwWlanCarrierId_Type()
)
hwWlanCarrierId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwWlanCarrierId.setStatus("current")
_HwWlanAcId_Type = Integer32
_HwWlanAcId_Object = MibScalar
hwWlanAcId = _HwWlanAcId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 1, 2, 2),
    _HwWlanAcId_Type()
)
hwWlanAcId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwWlanAcId.setStatus("current")


class _HwWlanForwardMode_Type(Integer32):
    """Custom type hwWlanForwardMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ap", 2),
          ("ess", 1))
    )


_HwWlanForwardMode_Type.__name__ = "Integer32"
_HwWlanForwardMode_Object = MibScalar
hwWlanForwardMode = _HwWlanForwardMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 1, 2, 3),
    _HwWlanForwardMode_Type()
)
hwWlanForwardMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwWlanForwardMode.setStatus("current")
_HwWlanAcNEnumber_Type = OctetString
_HwWlanAcNEnumber_Object = MibScalar
hwWlanAcNEnumber = _HwWlanAcNEnumber_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 1, 2, 4),
    _HwWlanAcNEnumber_Type()
)
hwWlanAcNEnumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwWlanAcNEnumber.setStatus("current")
_HwWlanAcAccessMaxApNumber_Type = Integer32
_HwWlanAcAccessMaxApNumber_Object = MibScalar
hwWlanAcAccessMaxApNumber = _HwWlanAcAccessMaxApNumber_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 1, 2, 5),
    _HwWlanAcAccessMaxApNumber_Type()
)
hwWlanAcAccessMaxApNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwWlanAcAccessMaxApNumber.setStatus("current")
_HwAcCountryCode_Type = OctetString
_HwAcCountryCode_Object = MibScalar
hwAcCountryCode = _HwAcCountryCode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 1, 2, 6),
    _HwAcCountryCode_Type()
)
hwAcCountryCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwAcCountryCode.setStatus("current")


class _HwWlanApUsername_Type(OctetString):
    """Custom type hwWlanApUsername based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 31),
    )


_HwWlanApUsername_Type.__name__ = "OctetString"
_HwWlanApUsername_Object = MibScalar
hwWlanApUsername = _HwWlanApUsername_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 1, 2, 8),
    _HwWlanApUsername_Type()
)
hwWlanApUsername.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwWlanApUsername.setStatus("current")


class _HwWlanApPassword_Type(OctetString):
    """Custom type hwWlanApPassword based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 32),
    )


_HwWlanApPassword_Type.__name__ = "OctetString"
_HwWlanApPassword_Object = MibScalar
hwWlanApPassword = _HwWlanApPassword_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 1, 2, 9),
    _HwWlanApPassword_Type()
)
hwWlanApPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwWlanApPassword.setStatus("current")
_HwWlanUsernamePasswordApId_Type = Integer32
_HwWlanUsernamePasswordApId_Object = MibScalar
hwWlanUsernamePasswordApId = _HwWlanUsernamePasswordApId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 1, 2, 10),
    _HwWlanUsernamePasswordApId_Type()
)
hwWlanUsernamePasswordApId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwWlanUsernamePasswordApId.setStatus("current")


class _HwWlanApLldpSwitch_Type(Integer32):
    """Custom type hwWlanApLldpSwitch based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_HwWlanApLldpSwitch_Type.__name__ = "Integer32"
_HwWlanApLldpSwitch_Object = MibScalar
hwWlanApLldpSwitch = _HwWlanApLldpSwitch_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 1, 2, 11),
    _HwWlanApLldpSwitch_Type()
)
hwWlanApLldpSwitch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwWlanApLldpSwitch.setStatus("current")
_HwWlanAcAccessMaxStaNumber_Type = Integer32
_HwWlanAcAccessMaxStaNumber_Object = MibScalar
hwWlanAcAccessMaxStaNumber = _HwWlanAcAccessMaxStaNumber_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 1, 2, 12),
    _HwWlanAcAccessMaxStaNumber_Type()
)
hwWlanAcAccessMaxStaNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwWlanAcAccessMaxStaNumber.setStatus("current")


class _HwWlanAcDtlsSwitch_Type(Integer32):
    """Custom type hwWlanAcDtlsSwitch based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_HwWlanAcDtlsSwitch_Type.__name__ = "Integer32"
_HwWlanAcDtlsSwitch_Object = MibScalar
hwWlanAcDtlsSwitch = _HwWlanAcDtlsSwitch_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 1, 2, 13),
    _HwWlanAcDtlsSwitch_Type()
)
hwWlanAcDtlsSwitch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwWlanAcDtlsSwitch.setStatus("current")


class _HwWlanAcDtlsPsk_Type(OctetString):
    """Custom type hwWlanAcDtlsPsk based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_HwWlanAcDtlsPsk_Type.__name__ = "OctetString"
_HwWlanAcDtlsPsk_Object = MibScalar
hwWlanAcDtlsPsk = _HwWlanAcDtlsPsk_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 1, 2, 14),
    _HwWlanAcDtlsPsk_Type()
)
hwWlanAcDtlsPsk.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwWlanAcDtlsPsk.setStatus("current")
_HwWlanApLogManualBackupApId_Type = Integer32
_HwWlanApLogManualBackupApId_Object = MibScalar
hwWlanApLogManualBackupApId = _HwWlanApLogManualBackupApId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 1, 2, 15),
    _HwWlanApLogManualBackupApId_Type()
)
hwWlanApLogManualBackupApId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwWlanApLogManualBackupApId.setStatus("current")


class _HwWlanAcDtlsDefaultPskSwitch_Type(Integer32):
    """Custom type hwWlanAcDtlsDefaultPskSwitch based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_HwWlanAcDtlsDefaultPskSwitch_Type.__name__ = "Integer32"
_HwWlanAcDtlsDefaultPskSwitch_Object = MibScalar
hwWlanAcDtlsDefaultPskSwitch = _HwWlanAcDtlsDefaultPskSwitch_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 1, 2, 16),
    _HwWlanAcDtlsDefaultPskSwitch_Type()
)
hwWlanAcDtlsDefaultPskSwitch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwWlanAcDtlsDefaultPskSwitch.setStatus("current")


class _HwWlanWorkMode_Type(Integer32):
    """Custom type hwWlanWorkMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ac", 1),
          ("ap", 2))
    )


_HwWlanWorkMode_Type.__name__ = "Integer32"
_HwWlanWorkMode_Object = MibScalar
hwWlanWorkMode = _HwWlanWorkMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 1, 2, 17),
    _HwWlanWorkMode_Type()
)
hwWlanWorkMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwWlanWorkMode.setStatus("current")


class _HwWlanIpv6Enable_Type(Integer32):
    """Custom type hwWlanIpv6Enable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_HwWlanIpv6Enable_Type.__name__ = "Integer32"
_HwWlanIpv6Enable_Object = MibScalar
hwWlanIpv6Enable = _HwWlanIpv6Enable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 1, 2, 18),
    _HwWlanIpv6Enable_Type()
)
hwWlanIpv6Enable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwWlanIpv6Enable.setStatus("current")


class _HwWlanInterAcDtlsEncrpyt_Type(Integer32):
    """Custom type hwWlanInterAcDtlsEncrpyt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_HwWlanInterAcDtlsEncrpyt_Type.__name__ = "Integer32"
_HwWlanInterAcDtlsEncrpyt_Object = MibScalar
hwWlanInterAcDtlsEncrpyt = _HwWlanInterAcDtlsEncrpyt_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 1, 2, 19),
    _HwWlanInterAcDtlsEncrpyt_Type()
)
hwWlanInterAcDtlsEncrpyt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwWlanInterAcDtlsEncrpyt.setStatus("current")


class _HwWlanInterAcDtlsPsk_Type(OctetString):
    """Custom type hwWlanInterAcDtlsPsk based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_HwWlanInterAcDtlsPsk_Type.__name__ = "OctetString"
_HwWlanInterAcDtlsPsk_Object = MibScalar
hwWlanInterAcDtlsPsk = _HwWlanInterAcDtlsPsk_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 1, 2, 20),
    _HwWlanInterAcDtlsPsk_Type()
)
hwWlanInterAcDtlsPsk.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwWlanInterAcDtlsPsk.setStatus("current")


class _HwWlanStaIpv6Switch_Type(Integer32):
    """Custom type hwWlanStaIpv6Switch based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_HwWlanStaIpv6Switch_Type.__name__ = "Integer32"
_HwWlanStaIpv6Switch_Object = MibScalar
hwWlanStaIpv6Switch = _HwWlanStaIpv6Switch_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 1, 2, 21),
    _HwWlanStaIpv6Switch_Type()
)
hwWlanStaIpv6Switch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwWlanStaIpv6Switch.setStatus("current")
_HwWlanAcSourceInterface_ObjectIdentity = ObjectIdentity
hwWlanAcSourceInterface = _HwWlanAcSourceInterface_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 1, 3)
)
_HwWlanAcSourceInterfaceValue_Type = Integer32
_HwWlanAcSourceInterfaceValue_Object = MibScalar
hwWlanAcSourceInterfaceValue = _HwWlanAcSourceInterfaceValue_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 1, 3, 1),
    _HwWlanAcSourceInterfaceValue_Type()
)
hwWlanAcSourceInterfaceValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwWlanAcSourceInterfaceValue.setStatus("current")


class _HwWlanAcSourceInterfaceMethod_Type(Integer32):
    """Custom type hwWlanAcSourceInterfaceMethod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("default", 1),
          ("ipaddress", 4),
          ("loopback", 3),
          ("vlanif", 2))
    )


_HwWlanAcSourceInterfaceMethod_Type.__name__ = "Integer32"
_HwWlanAcSourceInterfaceMethod_Object = MibScalar
hwWlanAcSourceInterfaceMethod = _HwWlanAcSourceInterfaceMethod_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 1, 3, 2),
    _HwWlanAcSourceInterfaceMethod_Type()
)
hwWlanAcSourceInterfaceMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwWlanAcSourceInterfaceMethod.setStatus("current")
_HwWlanAcSourceIPv4Address_Type = IpAddress
_HwWlanAcSourceIPv4Address_Object = MibScalar
hwWlanAcSourceIPv4Address = _HwWlanAcSourceIPv4Address_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 1, 3, 3),
    _HwWlanAcSourceIPv4Address_Type()
)
hwWlanAcSourceIPv4Address.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwWlanAcSourceIPv4Address.setStatus("current")
_HwWlanBatchQuery_ObjectIdentity = ObjectIdentity
hwWlanBatchQuery = _HwWlanBatchQuery_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 1, 4)
)


class _HwWlanBatchQueryType_Type(Integer32):
    """Custom type hwWlanBatchQueryType based on Integer32"""
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
              65535)
        )
    )
    namedValues = NamedValues(
        *(("apBlackListMac", 4),
          ("apBlackListSn", 5),
          ("apId", 8),
          ("apIdState", 9),
          ("apIdStateRegionName", 10),
          ("apProfName", 1),
          ("apRegionId", 6),
          ("apRegionIdModeName", 7),
          ("apWhiteListMac", 2),
          ("apWhiteListSn", 3),
          ("authMacStateType", 19),
          ("clear", 65535),
          ("essNameSsid", 15),
          ("radioBalanceGroupName", 13),
          ("radioProfName", 12),
          ("secProfName", 18),
          ("trafficProfName", 17),
          ("unauthApIdMac", 11),
          ("uncontrolApIdBssidAuthApId", 14),
          ("wmmProfName", 16))
    )


_HwWlanBatchQueryType_Type.__name__ = "Integer32"
_HwWlanBatchQueryType_Object = MibScalar
hwWlanBatchQueryType = _HwWlanBatchQueryType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 1, 4, 1),
    _HwWlanBatchQueryType_Type()
)
hwWlanBatchQueryType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwWlanBatchQueryType.setStatus("current")
_HwWlanBatchRequestNum_Type = Integer32
_HwWlanBatchRequestNum_Object = MibScalar
hwWlanBatchRequestNum = _HwWlanBatchRequestNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 1, 4, 2),
    _HwWlanBatchRequestNum_Type()
)
hwWlanBatchRequestNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwWlanBatchRequestNum.setStatus("current")
_HwWlanBatchStartCount_Type = Integer32
_HwWlanBatchStartCount_Object = MibScalar
hwWlanBatchStartCount = _HwWlanBatchStartCount_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 1, 4, 3),
    _HwWlanBatchStartCount_Type()
)
hwWlanBatchStartCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwWlanBatchStartCount.setStatus("current")


class _HwWlanBatchRequestIdList_Type(OctetString):
    """Custom type hwWlanBatchRequestIdList based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 2048),
    )


_HwWlanBatchRequestIdList_Type.__name__ = "OctetString"
_HwWlanBatchRequestIdList_Object = MibScalar
hwWlanBatchRequestIdList = _HwWlanBatchRequestIdList_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 1, 4, 4),
    _HwWlanBatchRequestIdList_Type()
)
hwWlanBatchRequestIdList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwWlanBatchRequestIdList.setStatus("current")
_HwWlanBatchRequestIdSize_Type = Integer32
_HwWlanBatchRequestIdSize_Object = MibScalar
hwWlanBatchRequestIdSize = _HwWlanBatchRequestIdSize_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 1, 4, 5),
    _HwWlanBatchRequestIdSize_Type()
)
hwWlanBatchRequestIdSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwWlanBatchRequestIdSize.setStatus("current")
_HwWlanBatchRequestIdNum_Type = Integer32
_HwWlanBatchRequestIdNum_Object = MibScalar
hwWlanBatchRequestIdNum = _HwWlanBatchRequestIdNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 1, 4, 6),
    _HwWlanBatchRequestIdNum_Type()
)
hwWlanBatchRequestIdNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwWlanBatchRequestIdNum.setStatus("current")


class _HwWlanBatchValueList_Type(OctetString):
    """Custom type hwWlanBatchValueList based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 6144),
    )


_HwWlanBatchValueList_Type.__name__ = "OctetString"
_HwWlanBatchValueList_Object = MibScalar
hwWlanBatchValueList = _HwWlanBatchValueList_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 1, 4, 7),
    _HwWlanBatchValueList_Type()
)
hwWlanBatchValueList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwWlanBatchValueList.setStatus("current")
_HwWlanBatchReturnNum_Type = Integer32
_HwWlanBatchReturnNum_Object = MibScalar
hwWlanBatchReturnNum = _HwWlanBatchReturnNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 1, 4, 8),
    _HwWlanBatchReturnNum_Type()
)
hwWlanBatchReturnNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwWlanBatchReturnNum.setStatus("current")
_HwWlanBatchTotalNum_Type = Integer32
_HwWlanBatchTotalNum_Object = MibScalar
hwWlanBatchTotalNum = _HwWlanBatchTotalNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 1, 4, 9),
    _HwWlanBatchTotalNum_Type()
)
hwWlanBatchTotalNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwWlanBatchTotalNum.setStatus("current")
_HwWlanCapwapConfig_ObjectIdentity = ObjectIdentity
hwWlanCapwapConfig = _HwWlanCapwapConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 1, 5)
)
_HwWlanCapwapKeepAliveInterval_Type = Integer32
_HwWlanCapwapKeepAliveInterval_Object = MibScalar
hwWlanCapwapKeepAliveInterval = _HwWlanCapwapKeepAliveInterval_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 1, 5, 1),
    _HwWlanCapwapKeepAliveInterval_Type()
)
hwWlanCapwapKeepAliveInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwWlanCapwapKeepAliveInterval.setStatus("current")
_HwWlanCapwapKeepAliveTimes_Type = Integer32
_HwWlanCapwapKeepAliveTimes_Object = MibScalar
hwWlanCapwapKeepAliveTimes = _HwWlanCapwapKeepAliveTimes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 1, 5, 2),
    _HwWlanCapwapKeepAliveTimes_Type()
)
hwWlanCapwapKeepAliveTimes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwWlanCapwapKeepAliveTimes.setStatus("current")
_HwWlanCapwapControlPriorityACToAP_Type = Integer32
_HwWlanCapwapControlPriorityACToAP_Object = MibScalar
hwWlanCapwapControlPriorityACToAP = _HwWlanCapwapControlPriorityACToAP_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 1, 5, 3),
    _HwWlanCapwapControlPriorityACToAP_Type()
)
hwWlanCapwapControlPriorityACToAP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwWlanCapwapControlPriorityACToAP.setStatus("current")
_HwWlanCapwapControlPriorityAPToAC_Type = Integer32
_HwWlanCapwapControlPriorityAPToAC_Object = MibScalar
hwWlanCapwapControlPriorityAPToAC = _HwWlanCapwapControlPriorityAPToAC_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 1, 5, 4),
    _HwWlanCapwapControlPriorityAPToAC_Type()
)
hwWlanCapwapControlPriorityAPToAC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwWlanCapwapControlPriorityAPToAC.setStatus("current")
_HwWlanAcProtect_ObjectIdentity = ObjectIdentity
hwWlanAcProtect = _HwWlanAcProtect_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 1, 6)
)
_HwWlanAcProtectIpAddress_Type = IpAddress
_HwWlanAcProtectIpAddress_Object = MibScalar
hwWlanAcProtectIpAddress = _HwWlanAcProtectIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 1, 6, 1),
    _HwWlanAcProtectIpAddress_Type()
)
hwWlanAcProtectIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwWlanAcProtectIpAddress.setStatus("current")


class _HwWlanAcProtectPriority_Type(Unsigned32):
    """Custom type hwWlanAcProtectPriority based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_HwWlanAcProtectPriority_Type.__name__ = "Unsigned32"
_HwWlanAcProtectPriority_Object = MibScalar
hwWlanAcProtectPriority = _HwWlanAcProtectPriority_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 1, 6, 2),
    _HwWlanAcProtectPriority_Type()
)
hwWlanAcProtectPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwWlanAcProtectPriority.setStatus("current")


class _HwWlanAcProtectSwitch_Type(Integer32):
    """Custom type hwWlanAcProtectSwitch based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_HwWlanAcProtectSwitch_Type.__name__ = "Integer32"
_HwWlanAcProtectSwitch_Object = MibScalar
hwWlanAcProtectSwitch = _HwWlanAcProtectSwitch_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 1, 6, 3),
    _HwWlanAcProtectSwitch_Type()
)
hwWlanAcProtectSwitch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwWlanAcProtectSwitch.setStatus("current")


class _HwWlanAcProtectRestoreSwitch_Type(Integer32):
    """Custom type hwWlanAcProtectRestoreSwitch based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_HwWlanAcProtectRestoreSwitch_Type.__name__ = "Integer32"
_HwWlanAcProtectRestoreSwitch_Object = MibScalar
hwWlanAcProtectRestoreSwitch = _HwWlanAcProtectRestoreSwitch_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 1, 6, 4),
    _HwWlanAcProtectRestoreSwitch_Type()
)
hwWlanAcProtectRestoreSwitch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwWlanAcProtectRestoreSwitch.setStatus("current")
_HwUndoWlanAcProtectIpAddress_Type = Integer32
_HwUndoWlanAcProtectIpAddress_Object = MibScalar
hwUndoWlanAcProtectIpAddress = _HwUndoWlanAcProtectIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 1, 6, 5),
    _HwUndoWlanAcProtectIpAddress_Type()
)
hwUndoWlanAcProtectIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwUndoWlanAcProtectIpAddress.setStatus("current")
_HwUndoWlanAcProtectPriority_Type = Integer32
_HwUndoWlanAcProtectPriority_Object = MibScalar
hwUndoWlanAcProtectPriority = _HwUndoWlanAcProtectPriority_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 1, 6, 6),
    _HwUndoWlanAcProtectPriority_Type()
)
hwUndoWlanAcProtectPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwUndoWlanAcProtectPriority.setStatus("current")


class _HwWlanAcProtectIpv6Address_Type(OctetString):
    """Custom type hwWlanAcProtectIpv6Address based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 46),
    )


_HwWlanAcProtectIpv6Address_Type.__name__ = "OctetString"
_HwWlanAcProtectIpv6Address_Object = MibScalar
hwWlanAcProtectIpv6Address = _HwWlanAcProtectIpv6Address_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 1, 6, 7),
    _HwWlanAcProtectIpv6Address_Type()
)
hwWlanAcProtectIpv6Address.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwWlanAcProtectIpv6Address.setStatus("current")
_HwWlanConfigChannel_ObjectIdentity = ObjectIdentity
hwWlanConfigChannel = _HwWlanConfigChannel_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 1, 7)
)
_HwWlan24G20MconfigChannel_Type = OctetString
_HwWlan24G20MconfigChannel_Object = MibScalar
hwWlan24G20MconfigChannel = _HwWlan24G20MconfigChannel_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 1, 7, 1),
    _HwWlan24G20MconfigChannel_Type()
)
hwWlan24G20MconfigChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwWlan24G20MconfigChannel.setStatus("current")
_HwWlan24G40MPlusConfigChannel_Type = OctetString
_HwWlan24G40MPlusConfigChannel_Object = MibScalar
hwWlan24G40MPlusConfigChannel = _HwWlan24G40MPlusConfigChannel_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 1, 7, 2),
    _HwWlan24G40MPlusConfigChannel_Type()
)
hwWlan24G40MPlusConfigChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwWlan24G40MPlusConfigChannel.setStatus("current")
_HwWlan24G40MMinusConfigChannel_Type = OctetString
_HwWlan24G40MMinusConfigChannel_Object = MibScalar
hwWlan24G40MMinusConfigChannel = _HwWlan24G40MMinusConfigChannel_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 1, 7, 3),
    _HwWlan24G40MMinusConfigChannel_Type()
)
hwWlan24G40MMinusConfigChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwWlan24G40MMinusConfigChannel.setStatus("current")
_HwWlan5G20MConfigChannel_Type = OctetString
_HwWlan5G20MConfigChannel_Object = MibScalar
hwWlan5G20MConfigChannel = _HwWlan5G20MConfigChannel_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 1, 7, 4),
    _HwWlan5G20MConfigChannel_Type()
)
hwWlan5G20MConfigChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwWlan5G20MConfigChannel.setStatus("current")
_HwWlan5G40MPlusConfigChannel_Type = OctetString
_HwWlan5G40MPlusConfigChannel_Object = MibScalar
hwWlan5G40MPlusConfigChannel = _HwWlan5G40MPlusConfigChannel_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 1, 7, 5),
    _HwWlan5G40MPlusConfigChannel_Type()
)
hwWlan5G40MPlusConfigChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwWlan5G40MPlusConfigChannel.setStatus("current")
_HwWlan5G40MMinusConfigChannel_Type = OctetString
_HwWlan5G40MMinusConfigChannel_Object = MibScalar
hwWlan5G40MMinusConfigChannel = _HwWlan5G40MMinusConfigChannel_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 1, 7, 6),
    _HwWlan5G40MMinusConfigChannel_Type()
)
hwWlan5G40MMinusConfigChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwWlan5G40MMinusConfigChannel.setStatus("current")
_HwWlanConfigChannelApId_Type = Integer32
_HwWlanConfigChannelApId_Object = MibScalar
hwWlanConfigChannelApId = _HwWlanConfigChannelApId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 1, 7, 7),
    _HwWlanConfigChannelApId_Type()
)
hwWlanConfigChannelApId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwWlanConfigChannelApId.setStatus("current")
_HwWlan24G80MConfigChannel_Type = OctetString
_HwWlan24G80MConfigChannel_Object = MibScalar
hwWlan24G80MConfigChannel = _HwWlan24G80MConfigChannel_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 1, 7, 8),
    _HwWlan24G80MConfigChannel_Type()
)
hwWlan24G80MConfigChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwWlan24G80MConfigChannel.setStatus("current")
_HwWlan5G80MConfigChannel_Type = OctetString
_HwWlan5G80MConfigChannel_Object = MibScalar
hwWlan5G80MConfigChannel = _HwWlan5G80MConfigChannel_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 1, 7, 9),
    _HwWlan5G80MConfigChannel_Type()
)
hwWlan5G80MConfigChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwWlan5G80MConfigChannel.setStatus("current")
_HwWlanStaLoadbalance_ObjectIdentity = ObjectIdentity
hwWlanStaLoadbalance = _HwWlanStaLoadbalance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 1, 8)
)
_HwWlanStaLoadbalanceEnable_Type = Integer32
_HwWlanStaLoadbalanceEnable_Object = MibScalar
hwWlanStaLoadbalanceEnable = _HwWlanStaLoadbalanceEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 1, 8, 1),
    _HwWlanStaLoadbalanceEnable_Type()
)
hwWlanStaLoadbalanceEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwWlanStaLoadbalanceEnable.setStatus("current")
_HwWlanStaLoadbalanceMode_Type = Integer32
_HwWlanStaLoadbalanceMode_Object = MibScalar
hwWlanStaLoadbalanceMode = _HwWlanStaLoadbalanceMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 1, 8, 2),
    _HwWlanStaLoadbalanceMode_Type()
)
hwWlanStaLoadbalanceMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwWlanStaLoadbalanceMode.setStatus("current")
_HwWlanStaLoadbalanceSessionGap_Type = Integer32
_HwWlanStaLoadbalanceSessionGap_Object = MibScalar
hwWlanStaLoadbalanceSessionGap = _HwWlanStaLoadbalanceSessionGap_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 1, 8, 3),
    _HwWlanStaLoadbalanceSessionGap_Type()
)
hwWlanStaLoadbalanceSessionGap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwWlanStaLoadbalanceSessionGap.setStatus("current")
_HwWlanStaLoadbalanceTrafficGap_Type = Integer32
_HwWlanStaLoadbalanceTrafficGap_Object = MibScalar
hwWlanStaLoadbalanceTrafficGap = _HwWlanStaLoadbalanceTrafficGap_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 1, 8, 4),
    _HwWlanStaLoadbalanceTrafficGap_Type()
)
hwWlanStaLoadbalanceTrafficGap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwWlanStaLoadbalanceTrafficGap.setStatus("current")
_HwWlanStaLoadbalanceAssociateThreshold_Type = Integer32
_HwWlanStaLoadbalanceAssociateThreshold_Object = MibScalar
hwWlanStaLoadbalanceAssociateThreshold = _HwWlanStaLoadbalanceAssociateThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 1, 8, 5),
    _HwWlanStaLoadbalanceAssociateThreshold_Type()
)
hwWlanStaLoadbalanceAssociateThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwWlanStaLoadbalanceAssociateThreshold.setStatus("current")
_HwWlanHsbConfig_ObjectIdentity = ObjectIdentity
hwWlanHsbConfig = _HwWlanHsbConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 1, 9)
)


class _HwWlanHsbServiceType_Type(Integer32):
    """Custom type hwWlanHsbServiceType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("hsbGroup", 2),
          ("hsbService", 3))
    )


_HwWlanHsbServiceType_Type.__name__ = "Integer32"
_HwWlanHsbServiceType_Object = MibScalar
hwWlanHsbServiceType = _HwWlanHsbServiceType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 1, 9, 1),
    _HwWlanHsbServiceType_Type()
)
hwWlanHsbServiceType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwWlanHsbServiceType.setStatus("current")
_HwWlanHsbGroupId_Type = Unsigned32
_HwWlanHsbGroupId_Object = MibScalar
hwWlanHsbGroupId = _HwWlanHsbGroupId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 1, 9, 2),
    _HwWlanHsbGroupId_Type()
)
hwWlanHsbGroupId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwWlanHsbGroupId.setStatus("current")
_HwWlanHsbTunnelId_Type = Unsigned32
_HwWlanHsbTunnelId_Object = MibScalar
hwWlanHsbTunnelId = _HwWlanHsbTunnelId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 1, 9, 3),
    _HwWlanHsbTunnelId_Type()
)
hwWlanHsbTunnelId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwWlanHsbTunnelId.setStatus("current")
_HwWlanLocation_ObjectIdentity = ObjectIdentity
hwWlanLocation = _HwWlanLocation_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 1, 10)
)
_HwWlanLocationServerIP_Type = IpAddress
_HwWlanLocationServerIP_Object = MibScalar
hwWlanLocationServerIP = _HwWlanLocationServerIP_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 1, 10, 1),
    _HwWlanLocationServerIP_Type()
)
hwWlanLocationServerIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwWlanLocationServerIP.setStatus("current")
_HwWlanLocationServerPort_Type = Integer32
_HwWlanLocationServerPort_Object = MibScalar
hwWlanLocationServerPort = _HwWlanLocationServerPort_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 1, 10, 2),
    _HwWlanLocationServerPort_Type()
)
hwWlanLocationServerPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwWlanLocationServerPort.setStatus("current")
_HwWlanLocationSourceIP_Type = IpAddress
_HwWlanLocationSourceIP_Object = MibScalar
hwWlanLocationSourceIP = _HwWlanLocationSourceIP_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 1, 10, 3),
    _HwWlanLocationSourceIP_Type()
)
hwWlanLocationSourceIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwWlanLocationSourceIP.setStatus("current")
_HwWlanLocationApReportToAC_Type = Integer32
_HwWlanLocationApReportToAC_Object = MibScalar
hwWlanLocationApReportToAC = _HwWlanLocationApReportToAC_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 1, 10, 4),
    _HwWlanLocationApReportToAC_Type()
)
hwWlanLocationApReportToAC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwWlanLocationApReportToAC.setStatus("current")
_HwWlanLocationApReportToServerIp_Type = IpAddress
_HwWlanLocationApReportToServerIp_Object = MibScalar
hwWlanLocationApReportToServerIp = _HwWlanLocationApReportToServerIp_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 1, 10, 5),
    _HwWlanLocationApReportToServerIp_Type()
)
hwWlanLocationApReportToServerIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwWlanLocationApReportToServerIp.setStatus("current")
_HwWlanLocationApReportToUdpPort_Type = Integer32
_HwWlanLocationApReportToUdpPort_Object = MibScalar
hwWlanLocationApReportToUdpPort = _HwWlanLocationApReportToUdpPort_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 1, 10, 6),
    _HwWlanLocationApReportToUdpPort_Type()
)
hwWlanLocationApReportToUdpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwWlanLocationApReportToUdpPort.setStatus("current")


class _HwWlanLocationApReportToIpv6Addr_Type(OctetString):
    """Custom type hwWlanLocationApReportToIpv6Addr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 46),
    )


_HwWlanLocationApReportToIpv6Addr_Type.__name__ = "OctetString"
_HwWlanLocationApReportToIpv6Addr_Object = MibScalar
hwWlanLocationApReportToIpv6Addr = _HwWlanLocationApReportToIpv6Addr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 1, 10, 7),
    _HwWlanLocationApReportToIpv6Addr_Type()
)
hwWlanLocationApReportToIpv6Addr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwWlanLocationApReportToIpv6Addr.setStatus("current")


class _HwWlanLocationAcReportToIpv6Addr_Type(OctetString):
    """Custom type hwWlanLocationAcReportToIpv6Addr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 46),
    )


_HwWlanLocationAcReportToIpv6Addr_Type.__name__ = "OctetString"
_HwWlanLocationAcReportToIpv6Addr_Object = MibScalar
hwWlanLocationAcReportToIpv6Addr = _HwWlanLocationAcReportToIpv6Addr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 1, 10, 8),
    _HwWlanLocationAcReportToIpv6Addr_Type()
)
hwWlanLocationAcReportToIpv6Addr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwWlanLocationAcReportToIpv6Addr.setStatus("current")
_HwWlanSpectrumAnalysis_ObjectIdentity = ObjectIdentity
hwWlanSpectrumAnalysis = _HwWlanSpectrumAnalysis_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 1, 11)
)
_HwWlanSpectrumAnalysisServerIP_Type = IpAddress
_HwWlanSpectrumAnalysisServerIP_Object = MibScalar
hwWlanSpectrumAnalysisServerIP = _HwWlanSpectrumAnalysisServerIP_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 1, 11, 1),
    _HwWlanSpectrumAnalysisServerIP_Type()
)
hwWlanSpectrumAnalysisServerIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwWlanSpectrumAnalysisServerIP.setStatus("current")
_HwWlanSpectrumAnalysisServerPort_Type = Integer32
_HwWlanSpectrumAnalysisServerPort_Object = MibScalar
hwWlanSpectrumAnalysisServerPort = _HwWlanSpectrumAnalysisServerPort_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 1, 11, 2),
    _HwWlanSpectrumAnalysisServerPort_Type()
)
hwWlanSpectrumAnalysisServerPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwWlanSpectrumAnalysisServerPort.setStatus("current")
_HwWlanNonWifiDeviceAgeTime_Type = Integer32
_HwWlanNonWifiDeviceAgeTime_Object = MibScalar
hwWlanNonWifiDeviceAgeTime = _HwWlanNonWifiDeviceAgeTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 1, 11, 3),
    _HwWlanNonWifiDeviceAgeTime_Type()
)
hwWlanNonWifiDeviceAgeTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwWlanNonWifiDeviceAgeTime.setStatus("current")
_HwWlanSpectrogramServerIP_Type = IpAddress
_HwWlanSpectrogramServerIP_Object = MibScalar
hwWlanSpectrogramServerIP = _HwWlanSpectrogramServerIP_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 1, 11, 4),
    _HwWlanSpectrogramServerIP_Type()
)
hwWlanSpectrogramServerIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwWlanSpectrogramServerIP.setStatus("current")
_HwWlanSpectrogramServerPort_Type = Integer32
_HwWlanSpectrogramServerPort_Object = MibScalar
hwWlanSpectrogramServerPort = _HwWlanSpectrogramServerPort_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 1, 11, 5),
    _HwWlanSpectrogramServerPort_Type()
)
hwWlanSpectrogramServerPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwWlanSpectrogramServerPort.setStatus("current")


class _HwWlanSpectrumAnalysisServerIPv6Addr_Type(OctetString):
    """Custom type hwWlanSpectrumAnalysisServerIPv6Addr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 46),
    )


_HwWlanSpectrumAnalysisServerIPv6Addr_Type.__name__ = "OctetString"
_HwWlanSpectrumAnalysisServerIPv6Addr_Object = MibScalar
hwWlanSpectrumAnalysisServerIPv6Addr = _HwWlanSpectrumAnalysisServerIPv6Addr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 1, 11, 6),
    _HwWlanSpectrumAnalysisServerIPv6Addr_Type()
)
hwWlanSpectrumAnalysisServerIPv6Addr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwWlanSpectrumAnalysisServerIPv6Addr.setStatus("current")


class _HwWlanSpectrogramServerIPv6Addr_Type(OctetString):
    """Custom type hwWlanSpectrogramServerIPv6Addr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 46),
    )


_HwWlanSpectrogramServerIPv6Addr_Type.__name__ = "OctetString"
_HwWlanSpectrogramServerIPv6Addr_Object = MibScalar
hwWlanSpectrogramServerIPv6Addr = _HwWlanSpectrogramServerIPv6Addr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 1, 11, 7),
    _HwWlanSpectrogramServerIPv6Addr_Type()
)
hwWlanSpectrogramServerIPv6Addr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwWlanSpectrogramServerIPv6Addr.setStatus("current")
_HwWlanSysManagementObjects_ObjectIdentity = ObjectIdentity
hwWlanSysManagementObjects = _HwWlanSysManagementObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 1, 12)
)
_HwWlanLBSConfig_ObjectIdentity = ObjectIdentity
hwWlanLBSConfig = _HwWlanLBSConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 1, 12, 1)
)
_HwWlanLBSAeServerPort_Type = Integer32
_HwWlanLBSAeServerPort_Object = MibScalar
hwWlanLBSAeServerPort = _HwWlanLBSAeServerPort_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 1, 12, 1, 1),
    _HwWlanLBSAeServerPort_Type()
)
hwWlanLBSAeServerPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwWlanLBSAeServerPort.setStatus("current")


class _HwWlanLBSAeApReportMode_Type(Integer32):
    """Custom type hwWlanLBSAeApReportMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("toAc", 2),
          ("toServer", 3))
    )


_HwWlanLBSAeApReportMode_Type.__name__ = "Integer32"
_HwWlanLBSAeApReportMode_Object = MibScalar
hwWlanLBSAeApReportMode = _HwWlanLBSAeApReportMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 1, 12, 1, 2),
    _HwWlanLBSAeApReportMode_Type()
)
hwWlanLBSAeApReportMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwWlanLBSAeApReportMode.setStatus("current")
_HwWlanLBSAeApReportPort_Type = Integer32
_HwWlanLBSAeApReportPort_Object = MibScalar
hwWlanLBSAeApReportPort = _HwWlanLBSAeApReportPort_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 1, 12, 1, 3),
    _HwWlanLBSAeApReportPort_Type()
)
hwWlanLBSAeApReportPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwWlanLBSAeApReportPort.setStatus("current")
_HwWlanLBSEkServerIp_Type = IpAddress
_HwWlanLBSEkServerIp_Object = MibScalar
hwWlanLBSEkServerIp = _HwWlanLBSEkServerIp_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 1, 12, 1, 4),
    _HwWlanLBSEkServerIp_Type()
)
hwWlanLBSEkServerIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwWlanLBSEkServerIp.setStatus("current")
_HwWlanLBSEkServerPort_Type = Integer32
_HwWlanLBSEkServerPort_Object = MibScalar
hwWlanLBSEkServerPort = _HwWlanLBSEkServerPort_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 1, 12, 1, 5),
    _HwWlanLBSEkServerPort_Type()
)
hwWlanLBSEkServerPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwWlanLBSEkServerPort.setStatus("current")


class _HwWlanLBSEkApReportMode_Type(Integer32):
    """Custom type hwWlanLBSEkApReportMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("toAc", 2),
          ("toServer", 3))
    )


_HwWlanLBSEkApReportMode_Type.__name__ = "Integer32"
_HwWlanLBSEkApReportMode_Object = MibScalar
hwWlanLBSEkApReportMode = _HwWlanLBSEkApReportMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 1, 12, 1, 6),
    _HwWlanLBSEkApReportMode_Type()
)
hwWlanLBSEkApReportMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwWlanLBSEkApReportMode.setStatus("current")
_HwWlanLBSEkApReportIp_Type = IpAddress
_HwWlanLBSEkApReportIp_Object = MibScalar
hwWlanLBSEkApReportIp = _HwWlanLBSEkApReportIp_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 1, 12, 1, 7),
    _HwWlanLBSEkApReportIp_Type()
)
hwWlanLBSEkApReportIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwWlanLBSEkApReportIp.setStatus("current")
_HwWlanLBSEkApReportPort_Type = Integer32
_HwWlanLBSEkApReportPort_Object = MibScalar
hwWlanLBSEkApReportPort = _HwWlanLBSEkApReportPort_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 1, 12, 1, 8),
    _HwWlanLBSEkApReportPort_Type()
)
hwWlanLBSEkApReportPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwWlanLBSEkApReportPort.setStatus("current")
_HwWlanLBSSourceIp_Type = IpAddress
_HwWlanLBSSourceIp_Object = MibScalar
hwWlanLBSSourceIp = _HwWlanLBSSourceIp_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 1, 12, 1, 9),
    _HwWlanLBSSourceIp_Type()
)
hwWlanLBSSourceIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwWlanLBSSourceIp.setStatus("current")
_HwWlanLBSAeCompoundTime_Type = Integer32
_HwWlanLBSAeCompoundTime_Object = MibScalar
hwWlanLBSAeCompoundTime = _HwWlanLBSAeCompoundTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 1, 12, 1, 10),
    _HwWlanLBSAeCompoundTime_Type()
)
hwWlanLBSAeCompoundTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwWlanLBSAeCompoundTime.setStatus("current")


class _HwWlanLBSEkServerIpv6Addr_Type(OctetString):
    """Custom type hwWlanLBSEkServerIpv6Addr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 46),
    )


_HwWlanLBSEkServerIpv6Addr_Type.__name__ = "OctetString"
_HwWlanLBSEkServerIpv6Addr_Object = MibScalar
hwWlanLBSEkServerIpv6Addr = _HwWlanLBSEkServerIpv6Addr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 1, 12, 1, 11),
    _HwWlanLBSEkServerIpv6Addr_Type()
)
hwWlanLBSEkServerIpv6Addr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwWlanLBSEkServerIpv6Addr.setStatus("current")


class _HwWlanLBSEkApReportIpv6Addr_Type(OctetString):
    """Custom type hwWlanLBSEkApReportIpv6Addr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 46),
    )


_HwWlanLBSEkApReportIpv6Addr_Type.__name__ = "OctetString"
_HwWlanLBSEkApReportIpv6Addr_Object = MibScalar
hwWlanLBSEkApReportIpv6Addr = _HwWlanLBSEkApReportIpv6Addr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 1, 12, 1, 12),
    _HwWlanLBSEkApReportIpv6Addr_Type()
)
hwWlanLBSEkApReportIpv6Addr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwWlanLBSEkApReportIpv6Addr.setStatus("current")


class _HwWlanLBSSourceIpv6Addr_Type(OctetString):
    """Custom type hwWlanLBSSourceIpv6Addr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 46),
    )


_HwWlanLBSSourceIpv6Addr_Type.__name__ = "OctetString"
_HwWlanLBSSourceIpv6Addr_Object = MibScalar
hwWlanLBSSourceIpv6Addr = _HwWlanLBSSourceIpv6Addr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 1, 12, 1, 13),
    _HwWlanLBSSourceIpv6Addr_Type()
)
hwWlanLBSSourceIpv6Addr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwWlanLBSSourceIpv6Addr.setStatus("current")
_HwInterAcManagement_ObjectIdentity = ObjectIdentity
hwInterAcManagement = _HwInterAcManagement_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 1, 13)
)


class _HwMasterControllerSwitch_Type(Integer32):
    """Custom type hwMasterControllerSwitch based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_HwMasterControllerSwitch_Type.__name__ = "Integer32"
_HwMasterControllerSwitch_Object = MibScalar
hwMasterControllerSwitch = _HwMasterControllerSwitch_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 1, 13, 1),
    _HwMasterControllerSwitch_Type()
)
hwMasterControllerSwitch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMasterControllerSwitch.setStatus("current")


class _HwConnectMasterControllerSwitch_Type(Integer32):
    """Custom type hwConnectMasterControllerSwitch based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("connect", 2),
          ("disconnect", 1))
    )


_HwConnectMasterControllerSwitch_Type.__name__ = "Integer32"
_HwConnectMasterControllerSwitch_Object = MibScalar
hwConnectMasterControllerSwitch = _HwConnectMasterControllerSwitch_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 1, 13, 2),
    _HwConnectMasterControllerSwitch_Type()
)
hwConnectMasterControllerSwitch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwConnectMasterControllerSwitch.setStatus("current")
_HwConnectMasterControllerIPv4Address_Type = IpAddress
_HwConnectMasterControllerIPv4Address_Object = MibScalar
hwConnectMasterControllerIPv4Address = _HwConnectMasterControllerIPv4Address_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 1, 13, 3),
    _HwConnectMasterControllerIPv4Address_Type()
)
hwConnectMasterControllerIPv4Address.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwConnectMasterControllerIPv4Address.setStatus("current")
_HwConnectMasterControllerIPv6Address_Type = OctetString
_HwConnectMasterControllerIPv6Address_Object = MibScalar
hwConnectMasterControllerIPv6Address = _HwConnectMasterControllerIPv6Address_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 1, 13, 4),
    _HwConnectMasterControllerIPv6Address_Type()
)
hwConnectMasterControllerIPv6Address.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwConnectMasterControllerIPv6Address.setStatus("current")
_HwWlanSysManagementConformance_ObjectIdentity = ObjectIdentity
hwWlanSysManagementConformance = _HwWlanSysManagementConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 1, 14)
)
_HwWlanSysManagementCompliances_ObjectIdentity = ObjectIdentity
hwWlanSysManagementCompliances = _HwWlanSysManagementCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 1, 14, 1)
)
_HwWlanSysManagementObjectGroups_ObjectIdentity = ObjectIdentity
hwWlanSysManagementObjectGroups = _HwWlanSysManagementObjectGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 1, 14, 2)
)

# Managed Objects groups

hwWlanTrapRestrainGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 1, 14, 2, 1)
)
hwWlanTrapRestrainGroup.setObjects(
      *(("HUAWEI-WLAN-SYS-MIB", "hwWlanTrapRestrainAll"),
        ("HUAWEI-WLAN-SYS-MIB", "hwWlanTrapSeverityRestrainSeverity"),
        ("HUAWEI-WLAN-SYS-MIB", "hwWlanApRegionTrapRestrainRegionIndexMask"),
        ("HUAWEI-WLAN-SYS-MIB", "hwWlanApTrapRestrainApIndexMask"))
)
if mibBuilder.loadTexts:
    hwWlanTrapRestrainGroup.setStatus("current")

hwWlanSysParaGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 1, 14, 2, 2)
)
hwWlanSysParaGroup.setObjects(
      *(("HUAWEI-WLAN-SYS-MIB", "hwWlanCarrierId"),
        ("HUAWEI-WLAN-SYS-MIB", "hwWlanAcId"),
        ("HUAWEI-WLAN-SYS-MIB", "hwWlanForwardMode"),
        ("HUAWEI-WLAN-SYS-MIB", "hwWlanAcNEnumber"),
        ("HUAWEI-WLAN-SYS-MIB", "hwWlanAcAccessMaxApNumber"),
        ("HUAWEI-WLAN-SYS-MIB", "hwAcCountryCode"),
        ("HUAWEI-WLAN-SYS-MIB", "hwWlanApUsername"),
        ("HUAWEI-WLAN-SYS-MIB", "hwWlanApPassword"),
        ("HUAWEI-WLAN-SYS-MIB", "hwWlanUsernamePasswordApId"),
        ("HUAWEI-WLAN-SYS-MIB", "hwWlanApLldpSwitch"),
        ("HUAWEI-WLAN-SYS-MIB", "hwWlanAcAccessMaxStaNumber"),
        ("HUAWEI-WLAN-SYS-MIB", "hwWlanAcDtlsSwitch"),
        ("HUAWEI-WLAN-SYS-MIB", "hwWlanAcDtlsPsk"),
        ("HUAWEI-WLAN-SYS-MIB", "hwWlanApLogManualBackupApId"),
        ("HUAWEI-WLAN-SYS-MIB", "hwWlanAcDtlsDefaultPskSwitch"),
        ("HUAWEI-WLAN-SYS-MIB", "hwWlanWorkMode"),
        ("HUAWEI-WLAN-SYS-MIB", "hwWlanIpv6Enable"),
        ("HUAWEI-WLAN-SYS-MIB", "hwWlanInterAcDtlsEncrpyt"),
        ("HUAWEI-WLAN-SYS-MIB", "hwWlanInterAcDtlsPsk"),
        ("HUAWEI-WLAN-SYS-MIB", "hwWlanStaIpv6Switch"))
)
if mibBuilder.loadTexts:
    hwWlanSysParaGroup.setStatus("current")

hwWlanAcSourceInterfaceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 1, 14, 2, 3)
)
hwWlanAcSourceInterfaceGroup.setObjects(
      *(("HUAWEI-WLAN-SYS-MIB", "hwWlanAcSourceInterfaceValue"),
        ("HUAWEI-WLAN-SYS-MIB", "hwWlanAcSourceInterfaceMethod"),
        ("HUAWEI-WLAN-SYS-MIB", "hwWlanAcSourceIPv4Address"))
)
if mibBuilder.loadTexts:
    hwWlanAcSourceInterfaceGroup.setStatus("current")

hwWlanBatchQueryGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 1, 14, 2, 4)
)
hwWlanBatchQueryGroup.setObjects(
      *(("HUAWEI-WLAN-SYS-MIB", "hwWlanBatchQueryType"),
        ("HUAWEI-WLAN-SYS-MIB", "hwWlanBatchRequestNum"),
        ("HUAWEI-WLAN-SYS-MIB", "hwWlanBatchStartCount"),
        ("HUAWEI-WLAN-SYS-MIB", "hwWlanBatchRequestIdList"),
        ("HUAWEI-WLAN-SYS-MIB", "hwWlanBatchRequestIdSize"),
        ("HUAWEI-WLAN-SYS-MIB", "hwWlanBatchRequestIdNum"),
        ("HUAWEI-WLAN-SYS-MIB", "hwWlanBatchValueList"),
        ("HUAWEI-WLAN-SYS-MIB", "hwWlanBatchReturnNum"),
        ("HUAWEI-WLAN-SYS-MIB", "hwWlanBatchTotalNum"))
)
if mibBuilder.loadTexts:
    hwWlanBatchQueryGroup.setStatus("current")

hwWlanCapwapConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 1, 14, 2, 5)
)
hwWlanCapwapConfigGroup.setObjects(
      *(("HUAWEI-WLAN-SYS-MIB", "hwWlanCapwapKeepAliveInterval"),
        ("HUAWEI-WLAN-SYS-MIB", "hwWlanCapwapKeepAliveTimes"),
        ("HUAWEI-WLAN-SYS-MIB", "hwWlanCapwapControlPriorityACToAP"),
        ("HUAWEI-WLAN-SYS-MIB", "hwWlanCapwapControlPriorityAPToAC"))
)
if mibBuilder.loadTexts:
    hwWlanCapwapConfigGroup.setStatus("current")

hwWlanAcProtectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 1, 14, 2, 6)
)
hwWlanAcProtectGroup.setObjects(
      *(("HUAWEI-WLAN-SYS-MIB", "hwWlanAcProtectIpAddress"),
        ("HUAWEI-WLAN-SYS-MIB", "hwWlanAcProtectPriority"),
        ("HUAWEI-WLAN-SYS-MIB", "hwWlanAcProtectSwitch"),
        ("HUAWEI-WLAN-SYS-MIB", "hwWlanAcProtectRestoreSwitch"),
        ("HUAWEI-WLAN-SYS-MIB", "hwUndoWlanAcProtectIpAddress"),
        ("HUAWEI-WLAN-SYS-MIB", "hwUndoWlanAcProtectPriority"),
        ("HUAWEI-WLAN-SYS-MIB", "hwWlanAcProtectIpv6Address"))
)
if mibBuilder.loadTexts:
    hwWlanAcProtectGroup.setStatus("current")

hwWlanConfigChannelGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 1, 14, 2, 7)
)
hwWlanConfigChannelGroup.setObjects(
      *(("HUAWEI-WLAN-SYS-MIB", "hwWlan24G20MconfigChannel"),
        ("HUAWEI-WLAN-SYS-MIB", "hwWlan24G40MPlusConfigChannel"),
        ("HUAWEI-WLAN-SYS-MIB", "hwWlan24G40MMinusConfigChannel"),
        ("HUAWEI-WLAN-SYS-MIB", "hwWlan5G20MConfigChannel"),
        ("HUAWEI-WLAN-SYS-MIB", "hwWlan5G40MPlusConfigChannel"),
        ("HUAWEI-WLAN-SYS-MIB", "hwWlan5G40MMinusConfigChannel"),
        ("HUAWEI-WLAN-SYS-MIB", "hwWlanConfigChannelApId"),
        ("HUAWEI-WLAN-SYS-MIB", "hwWlan24G80MConfigChannel"),
        ("HUAWEI-WLAN-SYS-MIB", "hwWlan5G80MConfigChannel"))
)
if mibBuilder.loadTexts:
    hwWlanConfigChannelGroup.setStatus("current")

hwWlanStaLoadbalanceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 1, 14, 2, 8)
)
hwWlanStaLoadbalanceGroup.setObjects(
      *(("HUAWEI-WLAN-SYS-MIB", "hwWlanStaLoadbalanceEnable"),
        ("HUAWEI-WLAN-SYS-MIB", "hwWlanStaLoadbalanceMode"),
        ("HUAWEI-WLAN-SYS-MIB", "hwWlanStaLoadbalanceSessionGap"),
        ("HUAWEI-WLAN-SYS-MIB", "hwWlanStaLoadbalanceTrafficGap"),
        ("HUAWEI-WLAN-SYS-MIB", "hwWlanStaLoadbalanceAssociateThreshold"))
)
if mibBuilder.loadTexts:
    hwWlanStaLoadbalanceGroup.setStatus("current")

hwWlanHsbConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 1, 14, 2, 9)
)
hwWlanHsbConfigGroup.setObjects(
      *(("HUAWEI-WLAN-SYS-MIB", "hwWlanHsbServiceType"),
        ("HUAWEI-WLAN-SYS-MIB", "hwWlanHsbGroupId"),
        ("HUAWEI-WLAN-SYS-MIB", "hwWlanHsbTunnelId"))
)
if mibBuilder.loadTexts:
    hwWlanHsbConfigGroup.setStatus("current")

hwWlanLocationGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 1, 14, 2, 10)
)
hwWlanLocationGroup.setObjects(
      *(("HUAWEI-WLAN-SYS-MIB", "hwWlanLocationServerIP"),
        ("HUAWEI-WLAN-SYS-MIB", "hwWlanLocationServerPort"),
        ("HUAWEI-WLAN-SYS-MIB", "hwWlanLocationSourceIP"),
        ("HUAWEI-WLAN-SYS-MIB", "hwWlanLocationApReportToAC"),
        ("HUAWEI-WLAN-SYS-MIB", "hwWlanLocationApReportToServerIp"),
        ("HUAWEI-WLAN-SYS-MIB", "hwWlanLocationApReportToUdpPort"),
        ("HUAWEI-WLAN-SYS-MIB", "hwWlanLocationApReportToIpv6Addr"),
        ("HUAWEI-WLAN-SYS-MIB", "hwWlanLocationAcReportToIpv6Addr"))
)
if mibBuilder.loadTexts:
    hwWlanLocationGroup.setStatus("current")

hwWlanSpectrumAnalysisGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 1, 14, 2, 11)
)
hwWlanSpectrumAnalysisGroup.setObjects(
      *(("HUAWEI-WLAN-SYS-MIB", "hwWlanSpectrumAnalysisServerIP"),
        ("HUAWEI-WLAN-SYS-MIB", "hwWlanSpectrumAnalysisServerPort"),
        ("HUAWEI-WLAN-SYS-MIB", "hwWlanNonWifiDeviceAgeTime"),
        ("HUAWEI-WLAN-SYS-MIB", "hwWlanSpectrogramServerIP"),
        ("HUAWEI-WLAN-SYS-MIB", "hwWlanSpectrogramServerPort"),
        ("HUAWEI-WLAN-SYS-MIB", "hwWlanSpectrumAnalysisServerIPv6Addr"),
        ("HUAWEI-WLAN-SYS-MIB", "hwWlanSpectrogramServerIPv6Addr"))
)
if mibBuilder.loadTexts:
    hwWlanSpectrumAnalysisGroup.setStatus("current")

hwWlanLBSConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 1, 14, 2, 12)
)
hwWlanLBSConfigGroup.setObjects(
      *(("HUAWEI-WLAN-SYS-MIB", "hwWlanLBSAeServerPort"),
        ("HUAWEI-WLAN-SYS-MIB", "hwWlanLBSAeApReportMode"),
        ("HUAWEI-WLAN-SYS-MIB", "hwWlanLBSAeApReportPort"),
        ("HUAWEI-WLAN-SYS-MIB", "hwWlanLBSEkServerIp"),
        ("HUAWEI-WLAN-SYS-MIB", "hwWlanLBSEkServerPort"),
        ("HUAWEI-WLAN-SYS-MIB", "hwWlanLBSEkApReportMode"),
        ("HUAWEI-WLAN-SYS-MIB", "hwWlanLBSEkApReportIp"),
        ("HUAWEI-WLAN-SYS-MIB", "hwWlanLBSEkApReportPort"),
        ("HUAWEI-WLAN-SYS-MIB", "hwWlanLBSSourceIp"),
        ("HUAWEI-WLAN-SYS-MIB", "hwWlanLBSAeCompoundTime"),
        ("HUAWEI-WLAN-SYS-MIB", "hwWlanLBSEkServerIpv6Addr"),
        ("HUAWEI-WLAN-SYS-MIB", "hwWlanLBSEkApReportIpv6Addr"),
        ("HUAWEI-WLAN-SYS-MIB", "hwWlanLBSSourceIpv6Addr"))
)
if mibBuilder.loadTexts:
    hwWlanLBSConfigGroup.setStatus("current")

hwInterAcManagementGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 1, 14, 2, 13)
)
hwInterAcManagementGroup.setObjects(
      *(("HUAWEI-WLAN-SYS-MIB", "hwMasterControllerSwitch"),
        ("HUAWEI-WLAN-SYS-MIB", "hwConnectMasterControllerSwitch"),
        ("HUAWEI-WLAN-SYS-MIB", "hwConnectMasterControllerIPv4Address"),
        ("HUAWEI-WLAN-SYS-MIB", "hwConnectMasterControllerIPv6Address"))
)
if mibBuilder.loadTexts:
    hwInterAcManagementGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

hwWlanSysManagementCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 1, 14, 1, 1)
)
if mibBuilder.loadTexts:
    hwWlanSysManagementCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HUAWEI-WLAN-SYS-MIB",
    **{"hwWlanSysManagement": hwWlanSysManagement,
       "hwWlanTrapRestrain": hwWlanTrapRestrain,
       "hwWlanTrapRestrainAll": hwWlanTrapRestrainAll,
       "hwWlanTrapSeverityRestrain": hwWlanTrapSeverityRestrain,
       "hwWlanTrapSeverityRestrainSeverity": hwWlanTrapSeverityRestrainSeverity,
       "hwWlanApRegionTrapRestrain": hwWlanApRegionTrapRestrain,
       "hwWlanApRegionTrapRestrainRegionIndexMask": hwWlanApRegionTrapRestrainRegionIndexMask,
       "hwWlanApTrapRestrain": hwWlanApTrapRestrain,
       "hwWlanApTrapRestrainApIndexMask": hwWlanApTrapRestrainApIndexMask,
       "hwWlanSysPara": hwWlanSysPara,
       "hwWlanCarrierId": hwWlanCarrierId,
       "hwWlanAcId": hwWlanAcId,
       "hwWlanForwardMode": hwWlanForwardMode,
       "hwWlanAcNEnumber": hwWlanAcNEnumber,
       "hwWlanAcAccessMaxApNumber": hwWlanAcAccessMaxApNumber,
       "hwAcCountryCode": hwAcCountryCode,
       "hwWlanApUsername": hwWlanApUsername,
       "hwWlanApPassword": hwWlanApPassword,
       "hwWlanUsernamePasswordApId": hwWlanUsernamePasswordApId,
       "hwWlanApLldpSwitch": hwWlanApLldpSwitch,
       "hwWlanAcAccessMaxStaNumber": hwWlanAcAccessMaxStaNumber,
       "hwWlanAcDtlsSwitch": hwWlanAcDtlsSwitch,
       "hwWlanAcDtlsPsk": hwWlanAcDtlsPsk,
       "hwWlanApLogManualBackupApId": hwWlanApLogManualBackupApId,
       "hwWlanAcDtlsDefaultPskSwitch": hwWlanAcDtlsDefaultPskSwitch,
       "hwWlanWorkMode": hwWlanWorkMode,
       "hwWlanIpv6Enable": hwWlanIpv6Enable,
       "hwWlanInterAcDtlsEncrpyt": hwWlanInterAcDtlsEncrpyt,
       "hwWlanInterAcDtlsPsk": hwWlanInterAcDtlsPsk,
       "hwWlanStaIpv6Switch": hwWlanStaIpv6Switch,
       "hwWlanAcSourceInterface": hwWlanAcSourceInterface,
       "hwWlanAcSourceInterfaceValue": hwWlanAcSourceInterfaceValue,
       "hwWlanAcSourceInterfaceMethod": hwWlanAcSourceInterfaceMethod,
       "hwWlanAcSourceIPv4Address": hwWlanAcSourceIPv4Address,
       "hwWlanBatchQuery": hwWlanBatchQuery,
       "hwWlanBatchQueryType": hwWlanBatchQueryType,
       "hwWlanBatchRequestNum": hwWlanBatchRequestNum,
       "hwWlanBatchStartCount": hwWlanBatchStartCount,
       "hwWlanBatchRequestIdList": hwWlanBatchRequestIdList,
       "hwWlanBatchRequestIdSize": hwWlanBatchRequestIdSize,
       "hwWlanBatchRequestIdNum": hwWlanBatchRequestIdNum,
       "hwWlanBatchValueList": hwWlanBatchValueList,
       "hwWlanBatchReturnNum": hwWlanBatchReturnNum,
       "hwWlanBatchTotalNum": hwWlanBatchTotalNum,
       "hwWlanCapwapConfig": hwWlanCapwapConfig,
       "hwWlanCapwapKeepAliveInterval": hwWlanCapwapKeepAliveInterval,
       "hwWlanCapwapKeepAliveTimes": hwWlanCapwapKeepAliveTimes,
       "hwWlanCapwapControlPriorityACToAP": hwWlanCapwapControlPriorityACToAP,
       "hwWlanCapwapControlPriorityAPToAC": hwWlanCapwapControlPriorityAPToAC,
       "hwWlanAcProtect": hwWlanAcProtect,
       "hwWlanAcProtectIpAddress": hwWlanAcProtectIpAddress,
       "hwWlanAcProtectPriority": hwWlanAcProtectPriority,
       "hwWlanAcProtectSwitch": hwWlanAcProtectSwitch,
       "hwWlanAcProtectRestoreSwitch": hwWlanAcProtectRestoreSwitch,
       "hwUndoWlanAcProtectIpAddress": hwUndoWlanAcProtectIpAddress,
       "hwUndoWlanAcProtectPriority": hwUndoWlanAcProtectPriority,
       "hwWlanAcProtectIpv6Address": hwWlanAcProtectIpv6Address,
       "hwWlanConfigChannel": hwWlanConfigChannel,
       "hwWlan24G20MconfigChannel": hwWlan24G20MconfigChannel,
       "hwWlan24G40MPlusConfigChannel": hwWlan24G40MPlusConfigChannel,
       "hwWlan24G40MMinusConfigChannel": hwWlan24G40MMinusConfigChannel,
       "hwWlan5G20MConfigChannel": hwWlan5G20MConfigChannel,
       "hwWlan5G40MPlusConfigChannel": hwWlan5G40MPlusConfigChannel,
       "hwWlan5G40MMinusConfigChannel": hwWlan5G40MMinusConfigChannel,
       "hwWlanConfigChannelApId": hwWlanConfigChannelApId,
       "hwWlan24G80MConfigChannel": hwWlan24G80MConfigChannel,
       "hwWlan5G80MConfigChannel": hwWlan5G80MConfigChannel,
       "hwWlanStaLoadbalance": hwWlanStaLoadbalance,
       "hwWlanStaLoadbalanceEnable": hwWlanStaLoadbalanceEnable,
       "hwWlanStaLoadbalanceMode": hwWlanStaLoadbalanceMode,
       "hwWlanStaLoadbalanceSessionGap": hwWlanStaLoadbalanceSessionGap,
       "hwWlanStaLoadbalanceTrafficGap": hwWlanStaLoadbalanceTrafficGap,
       "hwWlanStaLoadbalanceAssociateThreshold": hwWlanStaLoadbalanceAssociateThreshold,
       "hwWlanHsbConfig": hwWlanHsbConfig,
       "hwWlanHsbServiceType": hwWlanHsbServiceType,
       "hwWlanHsbGroupId": hwWlanHsbGroupId,
       "hwWlanHsbTunnelId": hwWlanHsbTunnelId,
       "hwWlanLocation": hwWlanLocation,
       "hwWlanLocationServerIP": hwWlanLocationServerIP,
       "hwWlanLocationServerPort": hwWlanLocationServerPort,
       "hwWlanLocationSourceIP": hwWlanLocationSourceIP,
       "hwWlanLocationApReportToAC": hwWlanLocationApReportToAC,
       "hwWlanLocationApReportToServerIp": hwWlanLocationApReportToServerIp,
       "hwWlanLocationApReportToUdpPort": hwWlanLocationApReportToUdpPort,
       "hwWlanLocationApReportToIpv6Addr": hwWlanLocationApReportToIpv6Addr,
       "hwWlanLocationAcReportToIpv6Addr": hwWlanLocationAcReportToIpv6Addr,
       "hwWlanSpectrumAnalysis": hwWlanSpectrumAnalysis,
       "hwWlanSpectrumAnalysisServerIP": hwWlanSpectrumAnalysisServerIP,
       "hwWlanSpectrumAnalysisServerPort": hwWlanSpectrumAnalysisServerPort,
       "hwWlanNonWifiDeviceAgeTime": hwWlanNonWifiDeviceAgeTime,
       "hwWlanSpectrogramServerIP": hwWlanSpectrogramServerIP,
       "hwWlanSpectrogramServerPort": hwWlanSpectrogramServerPort,
       "hwWlanSpectrumAnalysisServerIPv6Addr": hwWlanSpectrumAnalysisServerIPv6Addr,
       "hwWlanSpectrogramServerIPv6Addr": hwWlanSpectrogramServerIPv6Addr,
       "hwWlanSysManagementObjects": hwWlanSysManagementObjects,
       "hwWlanLBSConfig": hwWlanLBSConfig,
       "hwWlanLBSAeServerPort": hwWlanLBSAeServerPort,
       "hwWlanLBSAeApReportMode": hwWlanLBSAeApReportMode,
       "hwWlanLBSAeApReportPort": hwWlanLBSAeApReportPort,
       "hwWlanLBSEkServerIp": hwWlanLBSEkServerIp,
       "hwWlanLBSEkServerPort": hwWlanLBSEkServerPort,
       "hwWlanLBSEkApReportMode": hwWlanLBSEkApReportMode,
       "hwWlanLBSEkApReportIp": hwWlanLBSEkApReportIp,
       "hwWlanLBSEkApReportPort": hwWlanLBSEkApReportPort,
       "hwWlanLBSSourceIp": hwWlanLBSSourceIp,
       "hwWlanLBSAeCompoundTime": hwWlanLBSAeCompoundTime,
       "hwWlanLBSEkServerIpv6Addr": hwWlanLBSEkServerIpv6Addr,
       "hwWlanLBSEkApReportIpv6Addr": hwWlanLBSEkApReportIpv6Addr,
       "hwWlanLBSSourceIpv6Addr": hwWlanLBSSourceIpv6Addr,
       "hwInterAcManagement": hwInterAcManagement,
       "hwMasterControllerSwitch": hwMasterControllerSwitch,
       "hwConnectMasterControllerSwitch": hwConnectMasterControllerSwitch,
       "hwConnectMasterControllerIPv4Address": hwConnectMasterControllerIPv4Address,
       "hwConnectMasterControllerIPv6Address": hwConnectMasterControllerIPv6Address,
       "hwWlanSysManagementConformance": hwWlanSysManagementConformance,
       "hwWlanSysManagementCompliances": hwWlanSysManagementCompliances,
       "hwWlanSysManagementCompliance": hwWlanSysManagementCompliance,
       "hwWlanSysManagementObjectGroups": hwWlanSysManagementObjectGroups,
       "hwWlanTrapRestrainGroup": hwWlanTrapRestrainGroup,
       "hwWlanSysParaGroup": hwWlanSysParaGroup,
       "hwWlanAcSourceInterfaceGroup": hwWlanAcSourceInterfaceGroup,
       "hwWlanBatchQueryGroup": hwWlanBatchQueryGroup,
       "hwWlanCapwapConfigGroup": hwWlanCapwapConfigGroup,
       "hwWlanAcProtectGroup": hwWlanAcProtectGroup,
       "hwWlanConfigChannelGroup": hwWlanConfigChannelGroup,
       "hwWlanStaLoadbalanceGroup": hwWlanStaLoadbalanceGroup,
       "hwWlanHsbConfigGroup": hwWlanHsbConfigGroup,
       "hwWlanLocationGroup": hwWlanLocationGroup,
       "hwWlanSpectrumAnalysisGroup": hwWlanSpectrumAnalysisGroup,
       "hwWlanLBSConfigGroup": hwWlanLBSConfigGroup,
       "hwInterAcManagementGroup": hwInterAcManagementGroup}
)
