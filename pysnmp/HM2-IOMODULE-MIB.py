# SNMP MIB module (HM2-IOMODULE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HM2-IOMODULE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:55:58 2024
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

(HmEnabledStatus,
 hm2ConfigurationMibs) = mibBuilder.importSymbols(
    "HM2-TC-MIB",
    "HmEnabledStatus",
    "hm2ConfigurationMibs")

(InetAddress,
 InetAddressType,
 InetPortNumber) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType",
    "InetPortNumber")

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

hm2IOModuleMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 100)
)
hm2IOModuleMib.setRevisions(
        ("2012-02-10 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Hm2IOModuleMibNotifications_ObjectIdentity = ObjectIdentity
hm2IOModuleMibNotifications = _Hm2IOModuleMibNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 100, 0)
)
_Hm2IOModuleMibObjects_ObjectIdentity = ObjectIdentity
hm2IOModuleMibObjects = _Hm2IOModuleMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 100, 1)
)
_Hm2IOModConfigGroup_ObjectIdentity = ObjectIdentity
hm2IOModConfigGroup = _Hm2IOModConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 100, 1, 1)
)
_Hm2IOModConfigCommon_ObjectIdentity = ObjectIdentity
hm2IOModConfigCommon = _Hm2IOModConfigCommon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 100, 1, 1, 1)
)


class _Hm2IOModConfigDigInputAdminState_Type(HmEnabledStatus):
    """Custom type hm2IOModConfigDigInputAdminState based on HmEnabledStatus"""


_Hm2IOModConfigDigInputAdminState_Object = MibScalar
hm2IOModConfigDigInputAdminState = _Hm2IOModConfigDigInputAdminState_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 100, 1, 1, 1, 1),
    _Hm2IOModConfigDigInputAdminState_Type()
)
hm2IOModConfigDigInputAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2IOModConfigDigInputAdminState.setStatus("current")


class _Hm2IOModConfigDigOutputAdminState_Type(HmEnabledStatus):
    """Custom type hm2IOModConfigDigOutputAdminState based on HmEnabledStatus"""


_Hm2IOModConfigDigOutputAdminState_Object = MibScalar
hm2IOModConfigDigOutputAdminState = _Hm2IOModConfigDigOutputAdminState_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 100, 1, 1, 1, 2),
    _Hm2IOModConfigDigOutputAdminState_Type()
)
hm2IOModConfigDigOutputAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2IOModConfigDigOutputAdminState.setStatus("current")


class _Hm2IOModConfigDigInputRefreshInterval_Type(Integer32):
    """Custom type hm2IOModConfigDigInputRefreshInterval based on Integer32"""
    defaultValue = 1000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1000, 10000),
    )


_Hm2IOModConfigDigInputRefreshInterval_Type.__name__ = "Integer32"
_Hm2IOModConfigDigInputRefreshInterval_Object = MibScalar
hm2IOModConfigDigInputRefreshInterval = _Hm2IOModConfigDigInputRefreshInterval_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 100, 1, 1, 1, 3),
    _Hm2IOModConfigDigInputRefreshInterval_Type()
)
hm2IOModConfigDigInputRefreshInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2IOModConfigDigInputRefreshInterval.setStatus("current")


class _Hm2IOModConfigDigOutputRefreshInterval_Type(Integer32):
    """Custom type hm2IOModConfigDigOutputRefreshInterval based on Integer32"""
    defaultValue = 1000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1000, 10000),
    )


_Hm2IOModConfigDigOutputRefreshInterval_Type.__name__ = "Integer32"
_Hm2IOModConfigDigOutputRefreshInterval_Object = MibScalar
hm2IOModConfigDigOutputRefreshInterval = _Hm2IOModConfigDigOutputRefreshInterval_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 100, 1, 1, 1, 4),
    _Hm2IOModConfigDigOutputRefreshInterval_Type()
)
hm2IOModConfigDigOutputRefreshInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2IOModConfigDigOutputRefreshInterval.setStatus("current")


class _Hm2IOModConfigDigOutputRetryCount_Type(Integer32):
    """Custom type hm2IOModConfigDigOutputRetryCount based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_Hm2IOModConfigDigOutputRetryCount_Type.__name__ = "Integer32"
_Hm2IOModConfigDigOutputRetryCount_Object = MibScalar
hm2IOModConfigDigOutputRetryCount = _Hm2IOModConfigDigOutputRetryCount_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 100, 1, 1, 1, 5),
    _Hm2IOModConfigDigOutputRetryCount_Type()
)
hm2IOModConfigDigOutputRetryCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2IOModConfigDigOutputRetryCount.setStatus("current")
_Hm2IOModConfigDigInputTable_Object = MibTable
hm2IOModConfigDigInputTable = _Hm2IOModConfigDigInputTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 100, 1, 1, 2)
)
if mibBuilder.loadTexts:
    hm2IOModConfigDigInputTable.setStatus("current")
_Hm2IOModConfigDigInputEntry_Object = MibTableRow
hm2IOModConfigDigInputEntry = _Hm2IOModConfigDigInputEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 100, 1, 1, 2, 1)
)
hm2IOModConfigDigInputEntry.setIndexNames(
    (0, "HM2-IOMODULE-MIB", "hm2IOModConfigDigInputModID"),
    (0, "HM2-IOMODULE-MIB", "hm2IOModConfigDigInputID"),
)
if mibBuilder.loadTexts:
    hm2IOModConfigDigInputEntry.setStatus("current")


class _Hm2IOModConfigDigInputModID_Type(Integer32):
    """Custom type hm2IOModConfigDigInputModID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Hm2IOModConfigDigInputModID_Type.__name__ = "Integer32"
_Hm2IOModConfigDigInputModID_Object = MibTableColumn
hm2IOModConfigDigInputModID = _Hm2IOModConfigDigInputModID_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 100, 1, 1, 2, 1, 1),
    _Hm2IOModConfigDigInputModID_Type()
)
hm2IOModConfigDigInputModID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hm2IOModConfigDigInputModID.setStatus("current")


class _Hm2IOModConfigDigInputID_Type(Integer32):
    """Custom type hm2IOModConfigDigInputID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_Hm2IOModConfigDigInputID_Type.__name__ = "Integer32"
_Hm2IOModConfigDigInputID_Object = MibTableColumn
hm2IOModConfigDigInputID = _Hm2IOModConfigDigInputID_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 100, 1, 1, 2, 1, 2),
    _Hm2IOModConfigDigInputID_Type()
)
hm2IOModConfigDigInputID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hm2IOModConfigDigInputID.setStatus("current")


class _Hm2IOModConfigDigInputLogEvent_Type(HmEnabledStatus):
    """Custom type hm2IOModConfigDigInputLogEvent based on HmEnabledStatus"""


_Hm2IOModConfigDigInputLogEvent_Object = MibTableColumn
hm2IOModConfigDigInputLogEvent = _Hm2IOModConfigDigInputLogEvent_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 100, 1, 1, 2, 1, 3),
    _Hm2IOModConfigDigInputLogEvent_Type()
)
hm2IOModConfigDigInputLogEvent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2IOModConfigDigInputLogEvent.setStatus("current")


class _Hm2IOModConfigDigInputSnmpTrap_Type(HmEnabledStatus):
    """Custom type hm2IOModConfigDigInputSnmpTrap based on HmEnabledStatus"""


_Hm2IOModConfigDigInputSnmpTrap_Object = MibTableColumn
hm2IOModConfigDigInputSnmpTrap = _Hm2IOModConfigDigInputSnmpTrap_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 100, 1, 1, 2, 1, 4),
    _Hm2IOModConfigDigInputSnmpTrap_Type()
)
hm2IOModConfigDigInputSnmpTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2IOModConfigDigInputSnmpTrap.setStatus("current")
_Hm2IOModConfigDigOutputTable_Object = MibTable
hm2IOModConfigDigOutputTable = _Hm2IOModConfigDigOutputTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 100, 1, 1, 3)
)
if mibBuilder.loadTexts:
    hm2IOModConfigDigOutputTable.setStatus("current")
_Hm2IOModConfigDigOutputEntry_Object = MibTableRow
hm2IOModConfigDigOutputEntry = _Hm2IOModConfigDigOutputEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 100, 1, 1, 3, 1)
)
hm2IOModConfigDigOutputEntry.setIndexNames(
    (0, "HM2-IOMODULE-MIB", "hm2IOModConfigDigOutputModID"),
    (0, "HM2-IOMODULE-MIB", "hm2IOModConfigDigOutputID"),
)
if mibBuilder.loadTexts:
    hm2IOModConfigDigOutputEntry.setStatus("current")


class _Hm2IOModConfigDigOutputModID_Type(Integer32):
    """Custom type hm2IOModConfigDigOutputModID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Hm2IOModConfigDigOutputModID_Type.__name__ = "Integer32"
_Hm2IOModConfigDigOutputModID_Object = MibTableColumn
hm2IOModConfigDigOutputModID = _Hm2IOModConfigDigOutputModID_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 100, 1, 1, 3, 1, 1),
    _Hm2IOModConfigDigOutputModID_Type()
)
hm2IOModConfigDigOutputModID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hm2IOModConfigDigOutputModID.setStatus("current")


class _Hm2IOModConfigDigOutputID_Type(Integer32):
    """Custom type hm2IOModConfigDigOutputID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_Hm2IOModConfigDigOutputID_Type.__name__ = "Integer32"
_Hm2IOModConfigDigOutputID_Object = MibTableColumn
hm2IOModConfigDigOutputID = _Hm2IOModConfigDigOutputID_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 100, 1, 1, 3, 1, 2),
    _Hm2IOModConfigDigOutputID_Type()
)
hm2IOModConfigDigOutputID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hm2IOModConfigDigOutputID.setStatus("current")


class _Hm2IOModConfigDigOutputLogEvent_Type(HmEnabledStatus):
    """Custom type hm2IOModConfigDigOutputLogEvent based on HmEnabledStatus"""


_Hm2IOModConfigDigOutputLogEvent_Object = MibTableColumn
hm2IOModConfigDigOutputLogEvent = _Hm2IOModConfigDigOutputLogEvent_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 100, 1, 1, 3, 1, 3),
    _Hm2IOModConfigDigOutputLogEvent_Type()
)
hm2IOModConfigDigOutputLogEvent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2IOModConfigDigOutputLogEvent.setStatus("current")


class _Hm2IOModConfigDigOutputSnmpTrap_Type(HmEnabledStatus):
    """Custom type hm2IOModConfigDigOutputSnmpTrap based on HmEnabledStatus"""


_Hm2IOModConfigDigOutputSnmpTrap_Object = MibTableColumn
hm2IOModConfigDigOutputSnmpTrap = _Hm2IOModConfigDigOutputSnmpTrap_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 100, 1, 1, 3, 1, 4),
    _Hm2IOModConfigDigOutputSnmpTrap_Type()
)
hm2IOModConfigDigOutputSnmpTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2IOModConfigDigOutputSnmpTrap.setStatus("current")


class _Hm2IOModConfigDigOutputSourceAddressType_Type(InetAddressType):
    """Custom type hm2IOModConfigDigOutputSourceAddressType based on InetAddressType"""


_Hm2IOModConfigDigOutputSourceAddressType_Object = MibTableColumn
hm2IOModConfigDigOutputSourceAddressType = _Hm2IOModConfigDigOutputSourceAddressType_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 100, 1, 1, 3, 1, 5),
    _Hm2IOModConfigDigOutputSourceAddressType_Type()
)
hm2IOModConfigDigOutputSourceAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2IOModConfigDigOutputSourceAddressType.setStatus("current")


class _Hm2IOModConfigDigOutputSourceAddress_Type(InetAddress):
    """Custom type hm2IOModConfigDigOutputSourceAddress based on InetAddress"""
    defaultHexValue = "00000000"


_Hm2IOModConfigDigOutputSourceAddress_Object = MibTableColumn
hm2IOModConfigDigOutputSourceAddress = _Hm2IOModConfigDigOutputSourceAddress_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 100, 1, 1, 3, 1, 6),
    _Hm2IOModConfigDigOutputSourceAddress_Type()
)
hm2IOModConfigDigOutputSourceAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2IOModConfigDigOutputSourceAddress.setStatus("current")


class _Hm2IOModConfigDigOutputSourcePort_Type(InetPortNumber):
    """Custom type hm2IOModConfigDigOutputSourcePort based on InetPortNumber"""
    defaultValue = 161


_Hm2IOModConfigDigOutputSourcePort_Object = MibTableColumn
hm2IOModConfigDigOutputSourcePort = _Hm2IOModConfigDigOutputSourcePort_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 100, 1, 1, 3, 1, 7),
    _Hm2IOModConfigDigOutputSourcePort_Type()
)
hm2IOModConfigDigOutputSourcePort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2IOModConfigDigOutputSourcePort.setStatus("current")


class _Hm2IOModConfigDigOutputSourceModID_Type(Integer32):
    """Custom type hm2IOModConfigDigOutputSourceModID based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Hm2IOModConfigDigOutputSourceModID_Type.__name__ = "Integer32"
_Hm2IOModConfigDigOutputSourceModID_Object = MibTableColumn
hm2IOModConfigDigOutputSourceModID = _Hm2IOModConfigDigOutputSourceModID_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 100, 1, 1, 3, 1, 8),
    _Hm2IOModConfigDigOutputSourceModID_Type()
)
hm2IOModConfigDigOutputSourceModID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2IOModConfigDigOutputSourceModID.setStatus("current")


class _Hm2IOModConfigDigOutputSourceID_Type(Integer32):
    """Custom type hm2IOModConfigDigOutputSourceID based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_Hm2IOModConfigDigOutputSourceID_Type.__name__ = "Integer32"
_Hm2IOModConfigDigOutputSourceID_Object = MibTableColumn
hm2IOModConfigDigOutputSourceID = _Hm2IOModConfigDigOutputSourceID_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 100, 1, 1, 3, 1, 9),
    _Hm2IOModConfigDigOutputSourceID_Type()
)
hm2IOModConfigDigOutputSourceID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2IOModConfigDigOutputSourceID.setStatus("current")
_Hm2IOModValueGroup_ObjectIdentity = ObjectIdentity
hm2IOModValueGroup = _Hm2IOModValueGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 100, 1, 2)
)
_Hm2IOModValueDigInputTable_Object = MibTable
hm2IOModValueDigInputTable = _Hm2IOModValueDigInputTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 100, 1, 2, 1)
)
if mibBuilder.loadTexts:
    hm2IOModValueDigInputTable.setStatus("current")
_Hm2IOModValueDigInputEntry_Object = MibTableRow
hm2IOModValueDigInputEntry = _Hm2IOModValueDigInputEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 100, 1, 2, 1, 1)
)
hm2IOModValueDigInputEntry.setIndexNames(
    (0, "HM2-IOMODULE-MIB", "hm2IOModValueDigInputModID"),
    (0, "HM2-IOMODULE-MIB", "hm2IOModValueDigInputID"),
)
if mibBuilder.loadTexts:
    hm2IOModValueDigInputEntry.setStatus("current")


class _Hm2IOModValueDigInputModID_Type(Integer32):
    """Custom type hm2IOModValueDigInputModID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Hm2IOModValueDigInputModID_Type.__name__ = "Integer32"
_Hm2IOModValueDigInputModID_Object = MibTableColumn
hm2IOModValueDigInputModID = _Hm2IOModValueDigInputModID_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 100, 1, 2, 1, 1, 1),
    _Hm2IOModValueDigInputModID_Type()
)
hm2IOModValueDigInputModID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hm2IOModValueDigInputModID.setStatus("current")


class _Hm2IOModValueDigInputID_Type(Integer32):
    """Custom type hm2IOModValueDigInputID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_Hm2IOModValueDigInputID_Type.__name__ = "Integer32"
_Hm2IOModValueDigInputID_Object = MibTableColumn
hm2IOModValueDigInputID = _Hm2IOModValueDigInputID_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 100, 1, 2, 1, 1, 2),
    _Hm2IOModValueDigInputID_Type()
)
hm2IOModValueDigInputID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hm2IOModValueDigInputID.setStatus("current")


class _Hm2IOModValueDigInputValue_Type(Integer32):
    """Custom type hm2IOModValueDigInputValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("high", 1),
          ("low", 2),
          ("not-available", 0))
    )


_Hm2IOModValueDigInputValue_Type.__name__ = "Integer32"
_Hm2IOModValueDigInputValue_Object = MibTableColumn
hm2IOModValueDigInputValue = _Hm2IOModValueDigInputValue_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 100, 1, 2, 1, 1, 3),
    _Hm2IOModValueDigInputValue_Type()
)
hm2IOModValueDigInputValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2IOModValueDigInputValue.setStatus("current")
_Hm2IOModValueDigOutputTable_Object = MibTable
hm2IOModValueDigOutputTable = _Hm2IOModValueDigOutputTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 100, 1, 2, 2)
)
if mibBuilder.loadTexts:
    hm2IOModValueDigOutputTable.setStatus("current")
_Hm2IOModValueDigOutputEntry_Object = MibTableRow
hm2IOModValueDigOutputEntry = _Hm2IOModValueDigOutputEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 100, 1, 2, 2, 1)
)
hm2IOModValueDigOutputEntry.setIndexNames(
    (0, "HM2-IOMODULE-MIB", "hm2IOModValueDigOutputModID"),
    (0, "HM2-IOMODULE-MIB", "hm2IOModValueDigOutputID"),
)
if mibBuilder.loadTexts:
    hm2IOModValueDigOutputEntry.setStatus("current")


class _Hm2IOModValueDigOutputModID_Type(Integer32):
    """Custom type hm2IOModValueDigOutputModID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Hm2IOModValueDigOutputModID_Type.__name__ = "Integer32"
_Hm2IOModValueDigOutputModID_Object = MibTableColumn
hm2IOModValueDigOutputModID = _Hm2IOModValueDigOutputModID_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 100, 1, 2, 2, 1, 1),
    _Hm2IOModValueDigOutputModID_Type()
)
hm2IOModValueDigOutputModID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hm2IOModValueDigOutputModID.setStatus("current")


class _Hm2IOModValueDigOutputID_Type(Integer32):
    """Custom type hm2IOModValueDigOutputID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_Hm2IOModValueDigOutputID_Type.__name__ = "Integer32"
_Hm2IOModValueDigOutputID_Object = MibTableColumn
hm2IOModValueDigOutputID = _Hm2IOModValueDigOutputID_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 100, 1, 2, 2, 1, 2),
    _Hm2IOModValueDigOutputID_Type()
)
hm2IOModValueDigOutputID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hm2IOModValueDigOutputID.setStatus("current")


class _Hm2IOModValueDigOutputValue_Type(Integer32):
    """Custom type hm2IOModValueDigOutputValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("high", 1),
          ("invalid", 3),
          ("low", 2),
          ("not-available", 0),
          ("not-configured", 4))
    )


_Hm2IOModValueDigOutputValue_Type.__name__ = "Integer32"
_Hm2IOModValueDigOutputValue_Object = MibTableColumn
hm2IOModValueDigOutputValue = _Hm2IOModValueDigOutputValue_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 100, 1, 2, 2, 1, 3),
    _Hm2IOModValueDigOutputValue_Type()
)
hm2IOModValueDigOutputValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2IOModValueDigOutputValue.setStatus("current")

# Managed Objects groups


# Notification objects

hm2IOModDigInputChangeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 248, 11, 100, 0, 1)
)
hm2IOModDigInputChangeTrap.setObjects(
    ("HM2-IOMODULE-MIB", "hm2IOModValueDigInputValue")
)
if mibBuilder.loadTexts:
    hm2IOModDigInputChangeTrap.setStatus(
        "current"
    )

hm2IOModDigOutputChangeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 248, 11, 100, 0, 2)
)
hm2IOModDigOutputChangeTrap.setObjects(
    ("HM2-IOMODULE-MIB", "hm2IOModValueDigOutputValue")
)
if mibBuilder.loadTexts:
    hm2IOModDigOutputChangeTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HM2-IOMODULE-MIB",
    **{"hm2IOModuleMib": hm2IOModuleMib,
       "hm2IOModuleMibNotifications": hm2IOModuleMibNotifications,
       "hm2IOModDigInputChangeTrap": hm2IOModDigInputChangeTrap,
       "hm2IOModDigOutputChangeTrap": hm2IOModDigOutputChangeTrap,
       "hm2IOModuleMibObjects": hm2IOModuleMibObjects,
       "hm2IOModConfigGroup": hm2IOModConfigGroup,
       "hm2IOModConfigCommon": hm2IOModConfigCommon,
       "hm2IOModConfigDigInputAdminState": hm2IOModConfigDigInputAdminState,
       "hm2IOModConfigDigOutputAdminState": hm2IOModConfigDigOutputAdminState,
       "hm2IOModConfigDigInputRefreshInterval": hm2IOModConfigDigInputRefreshInterval,
       "hm2IOModConfigDigOutputRefreshInterval": hm2IOModConfigDigOutputRefreshInterval,
       "hm2IOModConfigDigOutputRetryCount": hm2IOModConfigDigOutputRetryCount,
       "hm2IOModConfigDigInputTable": hm2IOModConfigDigInputTable,
       "hm2IOModConfigDigInputEntry": hm2IOModConfigDigInputEntry,
       "hm2IOModConfigDigInputModID": hm2IOModConfigDigInputModID,
       "hm2IOModConfigDigInputID": hm2IOModConfigDigInputID,
       "hm2IOModConfigDigInputLogEvent": hm2IOModConfigDigInputLogEvent,
       "hm2IOModConfigDigInputSnmpTrap": hm2IOModConfigDigInputSnmpTrap,
       "hm2IOModConfigDigOutputTable": hm2IOModConfigDigOutputTable,
       "hm2IOModConfigDigOutputEntry": hm2IOModConfigDigOutputEntry,
       "hm2IOModConfigDigOutputModID": hm2IOModConfigDigOutputModID,
       "hm2IOModConfigDigOutputID": hm2IOModConfigDigOutputID,
       "hm2IOModConfigDigOutputLogEvent": hm2IOModConfigDigOutputLogEvent,
       "hm2IOModConfigDigOutputSnmpTrap": hm2IOModConfigDigOutputSnmpTrap,
       "hm2IOModConfigDigOutputSourceAddressType": hm2IOModConfigDigOutputSourceAddressType,
       "hm2IOModConfigDigOutputSourceAddress": hm2IOModConfigDigOutputSourceAddress,
       "hm2IOModConfigDigOutputSourcePort": hm2IOModConfigDigOutputSourcePort,
       "hm2IOModConfigDigOutputSourceModID": hm2IOModConfigDigOutputSourceModID,
       "hm2IOModConfigDigOutputSourceID": hm2IOModConfigDigOutputSourceID,
       "hm2IOModValueGroup": hm2IOModValueGroup,
       "hm2IOModValueDigInputTable": hm2IOModValueDigInputTable,
       "hm2IOModValueDigInputEntry": hm2IOModValueDigInputEntry,
       "hm2IOModValueDigInputModID": hm2IOModValueDigInputModID,
       "hm2IOModValueDigInputID": hm2IOModValueDigInputID,
       "hm2IOModValueDigInputValue": hm2IOModValueDigInputValue,
       "hm2IOModValueDigOutputTable": hm2IOModValueDigOutputTable,
       "hm2IOModValueDigOutputEntry": hm2IOModValueDigOutputEntry,
       "hm2IOModValueDigOutputModID": hm2IOModValueDigOutputModID,
       "hm2IOModValueDigOutputID": hm2IOModValueDigOutputID,
       "hm2IOModValueDigOutputValue": hm2IOModValueDigOutputValue}
)
