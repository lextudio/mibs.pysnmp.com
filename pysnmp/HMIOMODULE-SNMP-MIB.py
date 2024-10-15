# SNMP MIB module (HMIOMODULE-SNMP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HMIOMODULE-SNMP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:56:38 2024
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

(hmChassis,
 hmChassisEvent) = mibBuilder.importSymbols(
    "HMPRIV-MGMT-SNMP-MIB",
    "hmChassis",
    "hmChassisEvent")

(InetPortNumber,) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
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

hmIOModuleGroup = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 248, 14, 1, 13)
)
hmIOModuleGroup.setRevisions(
        ("2010-11-08 15:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class HmEnabledStatus(Integer32, TextualConvention):
    status = "current"
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



# MIB Managed Objects in the order of their OIDs

_HmIOModuleConfigGroup_ObjectIdentity = ObjectIdentity
hmIOModuleConfigGroup = _HmIOModuleConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 14, 1, 13, 1)
)
_HmIOModConfigCommon_ObjectIdentity = ObjectIdentity
hmIOModConfigCommon = _HmIOModConfigCommon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 14, 1, 13, 1, 1)
)


class _HmIOModConfigDigInputAdminState_Type(HmEnabledStatus):
    """Custom type hmIOModConfigDigInputAdminState based on HmEnabledStatus"""


_HmIOModConfigDigInputAdminState_Object = MibScalar
hmIOModConfigDigInputAdminState = _HmIOModConfigDigInputAdminState_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 1, 13, 1, 1, 1),
    _HmIOModConfigDigInputAdminState_Type()
)
hmIOModConfigDigInputAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmIOModConfigDigInputAdminState.setStatus("current")


class _HmIOModConfigDigOutputAdminState_Type(HmEnabledStatus):
    """Custom type hmIOModConfigDigOutputAdminState based on HmEnabledStatus"""


_HmIOModConfigDigOutputAdminState_Object = MibScalar
hmIOModConfigDigOutputAdminState = _HmIOModConfigDigOutputAdminState_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 1, 13, 1, 1, 2),
    _HmIOModConfigDigOutputAdminState_Type()
)
hmIOModConfigDigOutputAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmIOModConfigDigOutputAdminState.setStatus("current")


class _HmIOModConfigDigInputRefreshInterval_Type(Integer32):
    """Custom type hmIOModConfigDigInputRefreshInterval based on Integer32"""
    defaultValue = 1000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(500, 10000),
    )


_HmIOModConfigDigInputRefreshInterval_Type.__name__ = "Integer32"
_HmIOModConfigDigInputRefreshInterval_Object = MibScalar
hmIOModConfigDigInputRefreshInterval = _HmIOModConfigDigInputRefreshInterval_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 1, 13, 1, 1, 3),
    _HmIOModConfigDigInputRefreshInterval_Type()
)
hmIOModConfigDigInputRefreshInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmIOModConfigDigInputRefreshInterval.setStatus("current")


class _HmIOModConfigDigOutputRefreshInterval_Type(Integer32):
    """Custom type hmIOModConfigDigOutputRefreshInterval based on Integer32"""
    defaultValue = 1000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(500, 10000),
    )


_HmIOModConfigDigOutputRefreshInterval_Type.__name__ = "Integer32"
_HmIOModConfigDigOutputRefreshInterval_Object = MibScalar
hmIOModConfigDigOutputRefreshInterval = _HmIOModConfigDigOutputRefreshInterval_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 1, 13, 1, 1, 4),
    _HmIOModConfigDigOutputRefreshInterval_Type()
)
hmIOModConfigDigOutputRefreshInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmIOModConfigDigOutputRefreshInterval.setStatus("current")


class _HmIOModConfigDigOutputRetryCount_Type(Integer32):
    """Custom type hmIOModConfigDigOutputRetryCount based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_HmIOModConfigDigOutputRetryCount_Type.__name__ = "Integer32"
_HmIOModConfigDigOutputRetryCount_Object = MibScalar
hmIOModConfigDigOutputRetryCount = _HmIOModConfigDigOutputRetryCount_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 1, 13, 1, 1, 5),
    _HmIOModConfigDigOutputRetryCount_Type()
)
hmIOModConfigDigOutputRetryCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmIOModConfigDigOutputRetryCount.setStatus("current")
_HmIOModConfigDigInputTable_Object = MibTable
hmIOModConfigDigInputTable = _HmIOModConfigDigInputTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 1, 13, 1, 2)
)
if mibBuilder.loadTexts:
    hmIOModConfigDigInputTable.setStatus("current")
_HmIOModConfigDigInputEntry_Object = MibTableRow
hmIOModConfigDigInputEntry = _HmIOModConfigDigInputEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 1, 13, 1, 2, 1)
)
hmIOModConfigDigInputEntry.setIndexNames(
    (0, "HMIOMODULE-SNMP-MIB", "hmIOModConfigDigInputModID"),
    (0, "HMIOMODULE-SNMP-MIB", "hmIOModConfigDigInputID"),
)
if mibBuilder.loadTexts:
    hmIOModConfigDigInputEntry.setStatus("current")


class _HmIOModConfigDigInputModID_Type(Integer32):
    """Custom type hmIOModConfigDigInputModID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7),
    )


_HmIOModConfigDigInputModID_Type.__name__ = "Integer32"
_HmIOModConfigDigInputModID_Object = MibTableColumn
hmIOModConfigDigInputModID = _HmIOModConfigDigInputModID_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 1, 13, 1, 2, 1, 1),
    _HmIOModConfigDigInputModID_Type()
)
hmIOModConfigDigInputModID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hmIOModConfigDigInputModID.setStatus("current")


class _HmIOModConfigDigInputID_Type(Integer32):
    """Custom type hmIOModConfigDigInputID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_HmIOModConfigDigInputID_Type.__name__ = "Integer32"
_HmIOModConfigDigInputID_Object = MibTableColumn
hmIOModConfigDigInputID = _HmIOModConfigDigInputID_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 1, 13, 1, 2, 1, 2),
    _HmIOModConfigDigInputID_Type()
)
hmIOModConfigDigInputID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hmIOModConfigDigInputID.setStatus("current")


class _HmIOModConfigDigInputLogEvent_Type(HmEnabledStatus):
    """Custom type hmIOModConfigDigInputLogEvent based on HmEnabledStatus"""


_HmIOModConfigDigInputLogEvent_Object = MibTableColumn
hmIOModConfigDigInputLogEvent = _HmIOModConfigDigInputLogEvent_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 1, 13, 1, 2, 1, 3),
    _HmIOModConfigDigInputLogEvent_Type()
)
hmIOModConfigDigInputLogEvent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmIOModConfigDigInputLogEvent.setStatus("current")


class _HmIOModConfigDigInputSnmpTrap_Type(HmEnabledStatus):
    """Custom type hmIOModConfigDigInputSnmpTrap based on HmEnabledStatus"""


_HmIOModConfigDigInputSnmpTrap_Object = MibTableColumn
hmIOModConfigDigInputSnmpTrap = _HmIOModConfigDigInputSnmpTrap_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 1, 13, 1, 2, 1, 4),
    _HmIOModConfigDigInputSnmpTrap_Type()
)
hmIOModConfigDigInputSnmpTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmIOModConfigDigInputSnmpTrap.setStatus("current")
_HmIOModConfigDigOutputTable_Object = MibTable
hmIOModConfigDigOutputTable = _HmIOModConfigDigOutputTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 1, 13, 1, 3)
)
if mibBuilder.loadTexts:
    hmIOModConfigDigOutputTable.setStatus("current")
_HmIOModConfigDigOutputEntry_Object = MibTableRow
hmIOModConfigDigOutputEntry = _HmIOModConfigDigOutputEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 1, 13, 1, 3, 1)
)
hmIOModConfigDigOutputEntry.setIndexNames(
    (0, "HMIOMODULE-SNMP-MIB", "hmIOModConfigDigOutputModID"),
    (0, "HMIOMODULE-SNMP-MIB", "hmIOModConfigDigOutputID"),
)
if mibBuilder.loadTexts:
    hmIOModConfigDigOutputEntry.setStatus("current")


class _HmIOModConfigDigOutputModID_Type(Integer32):
    """Custom type hmIOModConfigDigOutputModID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7),
    )


_HmIOModConfigDigOutputModID_Type.__name__ = "Integer32"
_HmIOModConfigDigOutputModID_Object = MibTableColumn
hmIOModConfigDigOutputModID = _HmIOModConfigDigOutputModID_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 1, 13, 1, 3, 1, 1),
    _HmIOModConfigDigOutputModID_Type()
)
hmIOModConfigDigOutputModID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hmIOModConfigDigOutputModID.setStatus("current")


class _HmIOModConfigDigOutputID_Type(Integer32):
    """Custom type hmIOModConfigDigOutputID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_HmIOModConfigDigOutputID_Type.__name__ = "Integer32"
_HmIOModConfigDigOutputID_Object = MibTableColumn
hmIOModConfigDigOutputID = _HmIOModConfigDigOutputID_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 1, 13, 1, 3, 1, 2),
    _HmIOModConfigDigOutputID_Type()
)
hmIOModConfigDigOutputID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hmIOModConfigDigOutputID.setStatus("current")


class _HmIOModConfigDigOutputLogEvent_Type(HmEnabledStatus):
    """Custom type hmIOModConfigDigOutputLogEvent based on HmEnabledStatus"""


_HmIOModConfigDigOutputLogEvent_Object = MibTableColumn
hmIOModConfigDigOutputLogEvent = _HmIOModConfigDigOutputLogEvent_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 1, 13, 1, 3, 1, 3),
    _HmIOModConfigDigOutputLogEvent_Type()
)
hmIOModConfigDigOutputLogEvent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmIOModConfigDigOutputLogEvent.setStatus("current")


class _HmIOModConfigDigOutputSnmpTrap_Type(HmEnabledStatus):
    """Custom type hmIOModConfigDigOutputSnmpTrap based on HmEnabledStatus"""


_HmIOModConfigDigOutputSnmpTrap_Object = MibTableColumn
hmIOModConfigDigOutputSnmpTrap = _HmIOModConfigDigOutputSnmpTrap_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 1, 13, 1, 3, 1, 4),
    _HmIOModConfigDigOutputSnmpTrap_Type()
)
hmIOModConfigDigOutputSnmpTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmIOModConfigDigOutputSnmpTrap.setStatus("current")


class _HmIOModConfigDigOutputSourceIP_Type(IpAddress):
    """Custom type hmIOModConfigDigOutputSourceIP based on IpAddress"""
    defaultValue = OctetString("0.0.0.0")


_HmIOModConfigDigOutputSourceIP_Object = MibTableColumn
hmIOModConfigDigOutputSourceIP = _HmIOModConfigDigOutputSourceIP_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 1, 13, 1, 3, 1, 5),
    _HmIOModConfigDigOutputSourceIP_Type()
)
hmIOModConfigDigOutputSourceIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmIOModConfigDigOutputSourceIP.setStatus("current")


class _HmIOModConfigDigOutputSourceModID_Type(Integer32):
    """Custom type hmIOModConfigDigOutputSourceModID based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7),
    )


_HmIOModConfigDigOutputSourceModID_Type.__name__ = "Integer32"
_HmIOModConfigDigOutputSourceModID_Object = MibTableColumn
hmIOModConfigDigOutputSourceModID = _HmIOModConfigDigOutputSourceModID_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 1, 13, 1, 3, 1, 6),
    _HmIOModConfigDigOutputSourceModID_Type()
)
hmIOModConfigDigOutputSourceModID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmIOModConfigDigOutputSourceModID.setStatus("current")


class _HmIOModConfigDigOutputSourceID_Type(Integer32):
    """Custom type hmIOModConfigDigOutputSourceID based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_HmIOModConfigDigOutputSourceID_Type.__name__ = "Integer32"
_HmIOModConfigDigOutputSourceID_Object = MibTableColumn
hmIOModConfigDigOutputSourceID = _HmIOModConfigDigOutputSourceID_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 1, 13, 1, 3, 1, 7),
    _HmIOModConfigDigOutputSourceID_Type()
)
hmIOModConfigDigOutputSourceID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmIOModConfigDigOutputSourceID.setStatus("current")


class _HmIOModConfigDigOutputSourcePort_Type(InetPortNumber):
    """Custom type hmIOModConfigDigOutputSourcePort based on InetPortNumber"""
    defaultValue = 161


_HmIOModConfigDigOutputSourcePort_Object = MibTableColumn
hmIOModConfigDigOutputSourcePort = _HmIOModConfigDigOutputSourcePort_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 1, 13, 1, 3, 1, 8),
    _HmIOModConfigDigOutputSourcePort_Type()
)
hmIOModConfigDigOutputSourcePort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmIOModConfigDigOutputSourcePort.setStatus("current")
_HmIOModuleValueGroup_ObjectIdentity = ObjectIdentity
hmIOModuleValueGroup = _HmIOModuleValueGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 14, 1, 13, 2)
)
_HmIOModValueDigInputTable_Object = MibTable
hmIOModValueDigInputTable = _HmIOModValueDigInputTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 1, 13, 2, 1)
)
if mibBuilder.loadTexts:
    hmIOModValueDigInputTable.setStatus("current")
_HmIOModValueDigInputEntry_Object = MibTableRow
hmIOModValueDigInputEntry = _HmIOModValueDigInputEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 1, 13, 2, 1, 1)
)
hmIOModValueDigInputEntry.setIndexNames(
    (0, "HMIOMODULE-SNMP-MIB", "hmIOModValueDigInputModID"),
    (0, "HMIOMODULE-SNMP-MIB", "hmIOModValueDigInputID"),
)
if mibBuilder.loadTexts:
    hmIOModValueDigInputEntry.setStatus("current")


class _HmIOModValueDigInputModID_Type(Integer32):
    """Custom type hmIOModValueDigInputModID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7),
    )


_HmIOModValueDigInputModID_Type.__name__ = "Integer32"
_HmIOModValueDigInputModID_Object = MibTableColumn
hmIOModValueDigInputModID = _HmIOModValueDigInputModID_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 1, 13, 2, 1, 1, 1),
    _HmIOModValueDigInputModID_Type()
)
hmIOModValueDigInputModID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hmIOModValueDigInputModID.setStatus("current")


class _HmIOModValueDigInputID_Type(Integer32):
    """Custom type hmIOModValueDigInputID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_HmIOModValueDigInputID_Type.__name__ = "Integer32"
_HmIOModValueDigInputID_Object = MibTableColumn
hmIOModValueDigInputID = _HmIOModValueDigInputID_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 1, 13, 2, 1, 1, 2),
    _HmIOModValueDigInputID_Type()
)
hmIOModValueDigInputID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hmIOModValueDigInputID.setStatus("current")


class _HmIOModValueDigInputValue_Type(Integer32):
    """Custom type hmIOModValueDigInputValue based on Integer32"""
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


_HmIOModValueDigInputValue_Type.__name__ = "Integer32"
_HmIOModValueDigInputValue_Object = MibTableColumn
hmIOModValueDigInputValue = _HmIOModValueDigInputValue_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 1, 13, 2, 1, 1, 3),
    _HmIOModValueDigInputValue_Type()
)
hmIOModValueDigInputValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmIOModValueDigInputValue.setStatus("current")
_HmIOModValueDigOutputTable_Object = MibTable
hmIOModValueDigOutputTable = _HmIOModValueDigOutputTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 1, 13, 2, 2)
)
if mibBuilder.loadTexts:
    hmIOModValueDigOutputTable.setStatus("current")
_HmIOModValueDigOutputEntry_Object = MibTableRow
hmIOModValueDigOutputEntry = _HmIOModValueDigOutputEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 1, 13, 2, 2, 1)
)
hmIOModValueDigOutputEntry.setIndexNames(
    (0, "HMIOMODULE-SNMP-MIB", "hmIOModValueDigOutputModID"),
    (0, "HMIOMODULE-SNMP-MIB", "hmIOModValueDigOutputID"),
)
if mibBuilder.loadTexts:
    hmIOModValueDigOutputEntry.setStatus("current")


class _HmIOModValueDigOutputModID_Type(Integer32):
    """Custom type hmIOModValueDigOutputModID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7),
    )


_HmIOModValueDigOutputModID_Type.__name__ = "Integer32"
_HmIOModValueDigOutputModID_Object = MibTableColumn
hmIOModValueDigOutputModID = _HmIOModValueDigOutputModID_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 1, 13, 2, 2, 1, 1),
    _HmIOModValueDigOutputModID_Type()
)
hmIOModValueDigOutputModID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hmIOModValueDigOutputModID.setStatus("current")


class _HmIOModValueDigOutputID_Type(Integer32):
    """Custom type hmIOModValueDigOutputID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_HmIOModValueDigOutputID_Type.__name__ = "Integer32"
_HmIOModValueDigOutputID_Object = MibTableColumn
hmIOModValueDigOutputID = _HmIOModValueDigOutputID_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 1, 13, 2, 2, 1, 2),
    _HmIOModValueDigOutputID_Type()
)
hmIOModValueDigOutputID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hmIOModValueDigOutputID.setStatus("current")


class _HmIOModValueDigOutputValue_Type(Integer32):
    """Custom type hmIOModValueDigOutputValue based on Integer32"""
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


_HmIOModValueDigOutputValue_Type.__name__ = "Integer32"
_HmIOModValueDigOutputValue_Object = MibTableColumn
hmIOModValueDigOutputValue = _HmIOModValueDigOutputValue_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 1, 13, 2, 2, 1, 3),
    _HmIOModValueDigOutputValue_Type()
)
hmIOModValueDigOutputValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmIOModValueDigOutputValue.setStatus("current")

# Managed Objects groups


# Notification objects

hmIOModDigInputChangeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 248, 14, 1, 0, 16)
)
hmIOModDigInputChangeTrap.setObjects(
    ("HMIOMODULE-SNMP-MIB", "hmIOModValueDigInputValue")
)
if mibBuilder.loadTexts:
    hmIOModDigInputChangeTrap.setStatus(
        "current"
    )

hmIOModDigOutputChangeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 248, 14, 1, 0, 17)
)
hmIOModDigOutputChangeTrap.setObjects(
    ("HMIOMODULE-SNMP-MIB", "hmIOModValueDigOutputValue")
)
if mibBuilder.loadTexts:
    hmIOModDigOutputChangeTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HMIOMODULE-SNMP-MIB",
    **{"HmEnabledStatus": HmEnabledStatus,
       "hmIOModDigInputChangeTrap": hmIOModDigInputChangeTrap,
       "hmIOModDigOutputChangeTrap": hmIOModDigOutputChangeTrap,
       "hmIOModuleGroup": hmIOModuleGroup,
       "hmIOModuleConfigGroup": hmIOModuleConfigGroup,
       "hmIOModConfigCommon": hmIOModConfigCommon,
       "hmIOModConfigDigInputAdminState": hmIOModConfigDigInputAdminState,
       "hmIOModConfigDigOutputAdminState": hmIOModConfigDigOutputAdminState,
       "hmIOModConfigDigInputRefreshInterval": hmIOModConfigDigInputRefreshInterval,
       "hmIOModConfigDigOutputRefreshInterval": hmIOModConfigDigOutputRefreshInterval,
       "hmIOModConfigDigOutputRetryCount": hmIOModConfigDigOutputRetryCount,
       "hmIOModConfigDigInputTable": hmIOModConfigDigInputTable,
       "hmIOModConfigDigInputEntry": hmIOModConfigDigInputEntry,
       "hmIOModConfigDigInputModID": hmIOModConfigDigInputModID,
       "hmIOModConfigDigInputID": hmIOModConfigDigInputID,
       "hmIOModConfigDigInputLogEvent": hmIOModConfigDigInputLogEvent,
       "hmIOModConfigDigInputSnmpTrap": hmIOModConfigDigInputSnmpTrap,
       "hmIOModConfigDigOutputTable": hmIOModConfigDigOutputTable,
       "hmIOModConfigDigOutputEntry": hmIOModConfigDigOutputEntry,
       "hmIOModConfigDigOutputModID": hmIOModConfigDigOutputModID,
       "hmIOModConfigDigOutputID": hmIOModConfigDigOutputID,
       "hmIOModConfigDigOutputLogEvent": hmIOModConfigDigOutputLogEvent,
       "hmIOModConfigDigOutputSnmpTrap": hmIOModConfigDigOutputSnmpTrap,
       "hmIOModConfigDigOutputSourceIP": hmIOModConfigDigOutputSourceIP,
       "hmIOModConfigDigOutputSourceModID": hmIOModConfigDigOutputSourceModID,
       "hmIOModConfigDigOutputSourceID": hmIOModConfigDigOutputSourceID,
       "hmIOModConfigDigOutputSourcePort": hmIOModConfigDigOutputSourcePort,
       "hmIOModuleValueGroup": hmIOModuleValueGroup,
       "hmIOModValueDigInputTable": hmIOModValueDigInputTable,
       "hmIOModValueDigInputEntry": hmIOModValueDigInputEntry,
       "hmIOModValueDigInputModID": hmIOModValueDigInputModID,
       "hmIOModValueDigInputID": hmIOModValueDigInputID,
       "hmIOModValueDigInputValue": hmIOModValueDigInputValue,
       "hmIOModValueDigOutputTable": hmIOModValueDigOutputTable,
       "hmIOModValueDigOutputEntry": hmIOModValueDigOutputEntry,
       "hmIOModValueDigOutputModID": hmIOModValueDigOutputModID,
       "hmIOModValueDigOutputID": hmIOModValueDigOutputID,
       "hmIOModValueDigOutputValue": hmIOModValueDigOutputValue}
)
