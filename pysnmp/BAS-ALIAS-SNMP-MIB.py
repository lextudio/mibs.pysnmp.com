# SNMP MIB module (BAS-ALIAS-SNMP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/BAS-ALIAS-SNMP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:45:18 2024
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

(BasChassisId,
 BasInterfaceId,
 BasLogicalPortId,
 BasSlotId,
 basAliasSnmp) = mibBuilder.importSymbols(
    "BAS-MIB",
    "BasChassisId",
    "BasInterfaceId",
    "BasLogicalPortId",
    "BasSlotId",
    "basAliasSnmp")

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
 TextualConvention,
 TimeStamp) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TimeStamp")


# MODULE-IDENTITY

basAliasSnmpMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 1, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_BasSnmp_ObjectIdentity = ObjectIdentity
basSnmp = _BasSnmp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 1, 1, 1)
)
_BasSnmpTable_Object = MibTable
basSnmpTable = _BasSnmpTable_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 1, 1, 1, 1)
)
if mibBuilder.loadTexts:
    basSnmpTable.setStatus("current")
_BasSnmpEntry_Object = MibTableRow
basSnmpEntry = _BasSnmpEntry_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 1, 1, 1, 1, 1)
)
basSnmpEntry.setIndexNames(
    (0, "BAS-ALIAS-SNMP-MIB", "basSnmpChassis"),
    (0, "BAS-ALIAS-SNMP-MIB", "basSnmpSlot"),
    (0, "BAS-ALIAS-SNMP-MIB", "basSnmpIf"),
    (0, "BAS-ALIAS-SNMP-MIB", "basSnmpLPort"),
)
if mibBuilder.loadTexts:
    basSnmpEntry.setStatus("current")
_BasSnmpInPkts_Type = Counter32
_BasSnmpInPkts_Object = MibTableColumn
basSnmpInPkts = _BasSnmpInPkts_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 1, 1, 1, 1, 1, 1),
    _BasSnmpInPkts_Type()
)
basSnmpInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basSnmpInPkts.setStatus("current")
_BasSnmpInBadVersions_Type = Counter32
_BasSnmpInBadVersions_Object = MibTableColumn
basSnmpInBadVersions = _BasSnmpInBadVersions_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 1, 1, 1, 1, 1, 3),
    _BasSnmpInBadVersions_Type()
)
basSnmpInBadVersions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basSnmpInBadVersions.setStatus("current")
_BasSnmpInBadCommunityNames_Type = Counter32
_BasSnmpInBadCommunityNames_Object = MibTableColumn
basSnmpInBadCommunityNames = _BasSnmpInBadCommunityNames_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 1, 1, 1, 1, 1, 4),
    _BasSnmpInBadCommunityNames_Type()
)
basSnmpInBadCommunityNames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basSnmpInBadCommunityNames.setStatus("current")
_BasSnmpInBadCommunityUses_Type = Counter32
_BasSnmpInBadCommunityUses_Object = MibTableColumn
basSnmpInBadCommunityUses = _BasSnmpInBadCommunityUses_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 1, 1, 1, 1, 1, 5),
    _BasSnmpInBadCommunityUses_Type()
)
basSnmpInBadCommunityUses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basSnmpInBadCommunityUses.setStatus("current")
_BasSnmpInASNParseErrs_Type = Counter32
_BasSnmpInASNParseErrs_Object = MibTableColumn
basSnmpInASNParseErrs = _BasSnmpInASNParseErrs_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 1, 1, 1, 1, 1, 6),
    _BasSnmpInASNParseErrs_Type()
)
basSnmpInASNParseErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basSnmpInASNParseErrs.setStatus("current")


class _BasSnmpEnableAuthenTraps_Type(Integer32):
    """Custom type basSnmpEnableAuthenTraps based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_BasSnmpEnableAuthenTraps_Type.__name__ = "Integer32"
_BasSnmpEnableAuthenTraps_Object = MibTableColumn
basSnmpEnableAuthenTraps = _BasSnmpEnableAuthenTraps_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 1, 1, 1, 1, 1, 30),
    _BasSnmpEnableAuthenTraps_Type()
)
basSnmpEnableAuthenTraps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basSnmpEnableAuthenTraps.setStatus("current")
_BasSnmpSilentDrops_Type = Counter32
_BasSnmpSilentDrops_Object = MibTableColumn
basSnmpSilentDrops = _BasSnmpSilentDrops_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 1, 1, 1, 1, 1, 31),
    _BasSnmpSilentDrops_Type()
)
basSnmpSilentDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basSnmpSilentDrops.setStatus("current")
_BasSnmpProxyDrops_Type = Counter32
_BasSnmpProxyDrops_Object = MibTableColumn
basSnmpProxyDrops = _BasSnmpProxyDrops_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 1, 1, 1, 1, 1, 32),
    _BasSnmpProxyDrops_Type()
)
basSnmpProxyDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basSnmpProxyDrops.setStatus("current")
_BasSnmpChassis_Type = BasChassisId
_BasSnmpChassis_Object = MibTableColumn
basSnmpChassis = _BasSnmpChassis_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 1, 1, 1, 1, 1, 33),
    _BasSnmpChassis_Type()
)
basSnmpChassis.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    basSnmpChassis.setStatus("current")
_BasSnmpSlot_Type = BasSlotId
_BasSnmpSlot_Object = MibTableColumn
basSnmpSlot = _BasSnmpSlot_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 1, 1, 1, 1, 1, 34),
    _BasSnmpSlot_Type()
)
basSnmpSlot.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    basSnmpSlot.setStatus("current")
_BasSnmpIf_Type = BasInterfaceId
_BasSnmpIf_Object = MibTableColumn
basSnmpIf = _BasSnmpIf_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 1, 1, 1, 1, 1, 35),
    _BasSnmpIf_Type()
)
basSnmpIf.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    basSnmpIf.setStatus("current")
_BasSnmpLPort_Type = BasLogicalPortId
_BasSnmpLPort_Object = MibTableColumn
basSnmpLPort = _BasSnmpLPort_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 1, 1, 1, 1, 1, 36),
    _BasSnmpLPort_Type()
)
basSnmpLPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    basSnmpLPort.setStatus("current")
_BasSystem_ObjectIdentity = ObjectIdentity
basSystem = _BasSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 1, 1, 2)
)
_BasSysTable_Object = MibTable
basSysTable = _BasSysTable_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 1, 1, 2, 1)
)
if mibBuilder.loadTexts:
    basSysTable.setStatus("current")
_BasSysEntry_Object = MibTableRow
basSysEntry = _BasSysEntry_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 1, 1, 2, 1, 1)
)
basSysEntry.setIndexNames(
    (0, "BAS-ALIAS-SNMP-MIB", "basSysChassis"),
    (0, "BAS-ALIAS-SNMP-MIB", "basSysSlot"),
    (0, "BAS-ALIAS-SNMP-MIB", "basSysIf"),
    (0, "BAS-ALIAS-SNMP-MIB", "basSysLPort"),
)
if mibBuilder.loadTexts:
    basSysEntry.setStatus("current")


class _BasSysDescr_Type(DisplayString):
    """Custom type basSysDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_BasSysDescr_Type.__name__ = "DisplayString"
_BasSysDescr_Object = MibTableColumn
basSysDescr = _BasSysDescr_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 1, 1, 2, 1, 1, 1),
    _BasSysDescr_Type()
)
basSysDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basSysDescr.setStatus("current")
_BasSysObjectID_Type = ObjectIdentifier
_BasSysObjectID_Object = MibTableColumn
basSysObjectID = _BasSysObjectID_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 1, 1, 2, 1, 1, 2),
    _BasSysObjectID_Type()
)
basSysObjectID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basSysObjectID.setStatus("current")
_BasSysUpTime_Type = TimeTicks
_BasSysUpTime_Object = MibTableColumn
basSysUpTime = _BasSysUpTime_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 1, 1, 2, 1, 1, 3),
    _BasSysUpTime_Type()
)
basSysUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basSysUpTime.setStatus("current")


class _BasSysContact_Type(DisplayString):
    """Custom type basSysContact based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_BasSysContact_Type.__name__ = "DisplayString"
_BasSysContact_Object = MibTableColumn
basSysContact = _BasSysContact_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 1, 1, 2, 1, 1, 4),
    _BasSysContact_Type()
)
basSysContact.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basSysContact.setStatus("current")


class _BasSysName_Type(DisplayString):
    """Custom type basSysName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_BasSysName_Type.__name__ = "DisplayString"
_BasSysName_Object = MibTableColumn
basSysName = _BasSysName_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 1, 1, 2, 1, 1, 5),
    _BasSysName_Type()
)
basSysName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basSysName.setStatus("current")


class _BasSysLocation_Type(DisplayString):
    """Custom type basSysLocation based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_BasSysLocation_Type.__name__ = "DisplayString"
_BasSysLocation_Object = MibTableColumn
basSysLocation = _BasSysLocation_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 1, 1, 2, 1, 1, 6),
    _BasSysLocation_Type()
)
basSysLocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basSysLocation.setStatus("current")


class _BasSysServices_Type(Integer32):
    """Custom type basSysServices based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_BasSysServices_Type.__name__ = "Integer32"
_BasSysServices_Object = MibTableColumn
basSysServices = _BasSysServices_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 1, 1, 2, 1, 1, 7),
    _BasSysServices_Type()
)
basSysServices.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basSysServices.setStatus("current")
_BasSysORLastChange_Type = TimeStamp
_BasSysORLastChange_Object = MibTableColumn
basSysORLastChange = _BasSysORLastChange_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 1, 1, 2, 1, 1, 8),
    _BasSysORLastChange_Type()
)
basSysORLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basSysORLastChange.setStatus("current")
_BasSysChassis_Type = BasChassisId
_BasSysChassis_Object = MibTableColumn
basSysChassis = _BasSysChassis_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 1, 1, 2, 1, 1, 9),
    _BasSysChassis_Type()
)
basSysChassis.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    basSysChassis.setStatus("current")
_BasSysSlot_Type = BasSlotId
_BasSysSlot_Object = MibTableColumn
basSysSlot = _BasSysSlot_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 1, 1, 2, 1, 1, 10),
    _BasSysSlot_Type()
)
basSysSlot.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    basSysSlot.setStatus("current")
_BasSysIf_Type = BasInterfaceId
_BasSysIf_Object = MibTableColumn
basSysIf = _BasSysIf_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 1, 1, 2, 1, 1, 11),
    _BasSysIf_Type()
)
basSysIf.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    basSysIf.setStatus("current")
_BasSysLPort_Type = BasLogicalPortId
_BasSysLPort_Object = MibTableColumn
basSysLPort = _BasSysLPort_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 1, 1, 2, 1, 1, 12),
    _BasSysLPort_Type()
)
basSysLPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    basSysLPort.setStatus("current")
_BasSysORTable_Object = MibTable
basSysORTable = _BasSysORTable_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 1, 1, 2, 2)
)
if mibBuilder.loadTexts:
    basSysORTable.setStatus("current")
_BasSysOREntry_Object = MibTableRow
basSysOREntry = _BasSysOREntry_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 1, 1, 2, 2, 1)
)
basSysOREntry.setIndexNames(
    (0, "BAS-ALIAS-SNMP-MIB", "basSysORChassis"),
    (0, "BAS-ALIAS-SNMP-MIB", "basSysORSlot"),
    (0, "BAS-ALIAS-SNMP-MIB", "basSysORIf"),
    (0, "BAS-ALIAS-SNMP-MIB", "basSysORLPort"),
    (0, "BAS-ALIAS-SNMP-MIB", "basSysORIndex"),
)
if mibBuilder.loadTexts:
    basSysOREntry.setStatus("current")


class _BasSysORIndex_Type(Integer32):
    """Custom type basSysORIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_BasSysORIndex_Type.__name__ = "Integer32"
_BasSysORIndex_Object = MibTableColumn
basSysORIndex = _BasSysORIndex_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 1, 1, 2, 2, 1, 1),
    _BasSysORIndex_Type()
)
basSysORIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    basSysORIndex.setStatus("current")
_BasSysORID_Type = ObjectIdentifier
_BasSysORID_Object = MibTableColumn
basSysORID = _BasSysORID_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 1, 1, 2, 2, 1, 2),
    _BasSysORID_Type()
)
basSysORID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basSysORID.setStatus("current")
_BasSysORDescr_Type = DisplayString
_BasSysORDescr_Object = MibTableColumn
basSysORDescr = _BasSysORDescr_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 1, 1, 2, 2, 1, 3),
    _BasSysORDescr_Type()
)
basSysORDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basSysORDescr.setStatus("current")
_BasSysORUpTime_Type = TimeStamp
_BasSysORUpTime_Object = MibTableColumn
basSysORUpTime = _BasSysORUpTime_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 1, 1, 2, 2, 1, 4),
    _BasSysORUpTime_Type()
)
basSysORUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basSysORUpTime.setStatus("current")
_BasSysORChassis_Type = BasChassisId
_BasSysORChassis_Object = MibTableColumn
basSysORChassis = _BasSysORChassis_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 1, 1, 2, 2, 1, 5),
    _BasSysORChassis_Type()
)
basSysORChassis.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    basSysORChassis.setStatus("current")
_BasSysORSlot_Type = BasSlotId
_BasSysORSlot_Object = MibTableColumn
basSysORSlot = _BasSysORSlot_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 1, 1, 2, 2, 1, 6),
    _BasSysORSlot_Type()
)
basSysORSlot.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    basSysORSlot.setStatus("current")
_BasSysORIf_Type = BasInterfaceId
_BasSysORIf_Object = MibTableColumn
basSysORIf = _BasSysORIf_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 1, 1, 2, 2, 1, 7),
    _BasSysORIf_Type()
)
basSysORIf.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    basSysORIf.setStatus("current")
_BasSysORLPort_Type = BasLogicalPortId
_BasSysORLPort_Object = MibTableColumn
basSysORLPort = _BasSysORLPort_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 1, 1, 2, 2, 1, 8),
    _BasSysORLPort_Type()
)
basSysORLPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    basSysORLPort.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BAS-ALIAS-SNMP-MIB",
    **{"basAliasSnmpMib": basAliasSnmpMib,
       "basSnmp": basSnmp,
       "basSnmpTable": basSnmpTable,
       "basSnmpEntry": basSnmpEntry,
       "basSnmpInPkts": basSnmpInPkts,
       "basSnmpInBadVersions": basSnmpInBadVersions,
       "basSnmpInBadCommunityNames": basSnmpInBadCommunityNames,
       "basSnmpInBadCommunityUses": basSnmpInBadCommunityUses,
       "basSnmpInASNParseErrs": basSnmpInASNParseErrs,
       "basSnmpEnableAuthenTraps": basSnmpEnableAuthenTraps,
       "basSnmpSilentDrops": basSnmpSilentDrops,
       "basSnmpProxyDrops": basSnmpProxyDrops,
       "basSnmpChassis": basSnmpChassis,
       "basSnmpSlot": basSnmpSlot,
       "basSnmpIf": basSnmpIf,
       "basSnmpLPort": basSnmpLPort,
       "basSystem": basSystem,
       "basSysTable": basSysTable,
       "basSysEntry": basSysEntry,
       "basSysDescr": basSysDescr,
       "basSysObjectID": basSysObjectID,
       "basSysUpTime": basSysUpTime,
       "basSysContact": basSysContact,
       "basSysName": basSysName,
       "basSysLocation": basSysLocation,
       "basSysServices": basSysServices,
       "basSysORLastChange": basSysORLastChange,
       "basSysChassis": basSysChassis,
       "basSysSlot": basSysSlot,
       "basSysIf": basSysIf,
       "basSysLPort": basSysLPort,
       "basSysORTable": basSysORTable,
       "basSysOREntry": basSysOREntry,
       "basSysORIndex": basSysORIndex,
       "basSysORID": basSysORID,
       "basSysORDescr": basSysORDescr,
       "basSysORUpTime": basSysORUpTime,
       "basSysORChassis": basSysORChassis,
       "basSysORSlot": basSysORSlot,
       "basSysORIf": basSysORIf,
       "basSysORLPort": basSysORLPort}
)
