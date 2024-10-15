# SNMP MIB module (TIMETRA-SAS-IEEE8021-CFM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/TIMETRA-SAS-IEEE8021-CFM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:04:22 2024
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

(dot1agCfmMepEntry,) = mibBuilder.importSymbols(
    "IEEE8021-CFM-MIB",
    "dot1agCfmMepEntry")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TruthValue")

(timetraSASConfs,
 timetraSASModules,
 timetraSASObjs) = mibBuilder.importSymbols(
    "TIMETRA-SAS-GLOBAL-MIB",
    "timetraSASConfs",
    "timetraSASModules",
    "timetraSASObjs")


# MODULE-IDENTITY

timetraSASIEEE8021CfmMIBModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 1, 1, 11)
)
timetraSASIEEE8021CfmMIBModule.setRevisions(
        ("1910-01-01 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_TmnxSASDot1agMIBConformance_ObjectIdentity = ObjectIdentity
tmnxSASDot1agMIBConformance = _TmnxSASDot1agMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 1, 7)
)
_TmnxSASDot1agCfmCompliances_ObjectIdentity = ObjectIdentity
tmnxSASDot1agCfmCompliances = _TmnxSASDot1agCfmCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 1, 7, 1)
)
_TmnxSASDot1agCfmGroups_ObjectIdentity = ObjectIdentity
tmnxSASDot1agCfmGroups = _TmnxSASDot1agCfmGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 1, 7, 2)
)
_TmnxSASDot1agMIBObjs_ObjectIdentity = ObjectIdentity
tmnxSASDot1agMIBObjs = _TmnxSASDot1agMIBObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 11)
)
_TmnxSASDot1agCfmMep_ObjectIdentity = ObjectIdentity
tmnxSASDot1agCfmMep = _TmnxSASDot1agCfmMep_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 11, 1)
)
_TmnxDot1agCfmMepExtnTable_Object = MibTable
tmnxDot1agCfmMepExtnTable = _TmnxDot1agCfmMepExtnTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 11, 1, 1)
)
if mibBuilder.loadTexts:
    tmnxDot1agCfmMepExtnTable.setStatus("current")
_TmnxDot1agCfmMepExtnEntry_Object = MibTableRow
tmnxDot1agCfmMepExtnEntry = _TmnxDot1agCfmMepExtnEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 11, 1, 1, 1)
)
if mibBuilder.loadTexts:
    tmnxDot1agCfmMepExtnEntry.setStatus("current")


class _TmnxDot1agCfmMepSendAisOnPortDown_Type(TruthValue):
    """Custom type tmnxDot1agCfmMepSendAisOnPortDown based on TruthValue"""


_TmnxDot1agCfmMepSendAisOnPortDown_Object = MibTableColumn
tmnxDot1agCfmMepSendAisOnPortDown = _TmnxDot1agCfmMepSendAisOnPortDown_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 11, 1, 1, 1, 1),
    _TmnxDot1agCfmMepSendAisOnPortDown_Type()
)
tmnxDot1agCfmMepSendAisOnPortDown.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDot1agCfmMepSendAisOnPortDown.setStatus("current")


class _TmnxDot1agCfmMepControlSapTag_Type(Unsigned32):
    """Custom type tmnxDot1agCfmMepControlSapTag based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4096),
    )


_TmnxDot1agCfmMepControlSapTag_Type.__name__ = "Unsigned32"
_TmnxDot1agCfmMepControlSapTag_Object = MibTableColumn
tmnxDot1agCfmMepControlSapTag = _TmnxDot1agCfmMepControlSapTag_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 11, 1, 1, 1, 2),
    _TmnxDot1agCfmMepControlSapTag_Type()
)
tmnxDot1agCfmMepControlSapTag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDot1agCfmMepControlSapTag.setStatus("current")
_TmnxSASDot1agNotificationsPrefix_ObjectIdentity = ObjectIdentity
tmnxSASDot1agNotificationsPrefix = _TmnxSASDot1agNotificationsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 11, 2)
)
_TmnxSASDot1agNotifications_ObjectIdentity = ObjectIdentity
tmnxSASDot1agNotifications = _TmnxSASDot1agNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 11, 2, 1)
)
dot1agCfmMepEntry.registerAugmentions(
    ("TIMETRA-SAS-IEEE8021-CFM-MIB",
     "tmnxDot1agCfmMepExtnEntry")
)
tmnxDot1agCfmMepExtnEntry.setIndexNames(*dot1agCfmMepEntry.getIndexNames())

# Managed Objects groups

tmnxSASDot1agCfmMepGroupV2v0 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 1, 7, 2, 1)
)
tmnxSASDot1agCfmMepGroupV2v0.setObjects(
    ("TIMETRA-SAS-IEEE8021-CFM-MIB", "tmnxDot1agCfmMepSendAisOnPortDown")
)
if mibBuilder.loadTexts:
    tmnxSASDot1agCfmMepGroupV2v0.setStatus("current")

tmnxSASDot1agCfmMepGroupV4v0 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 1, 7, 2, 2)
)
tmnxSASDot1agCfmMepGroupV4v0.setObjects(
      *(("TIMETRA-SAS-IEEE8021-CFM-MIB", "tmnxDot1agCfmMepSendAisOnPortDown"),
        ("TIMETRA-SAS-IEEE8021-CFM-MIB", "tmnxDot1agCfmMepControlSapTag"))
)
if mibBuilder.loadTexts:
    tmnxSASDot1agCfmMepGroupV4v0.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

tmnxSASDot1agCfmComplianceV2v0 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 1, 7, 1, 2)
)
if mibBuilder.loadTexts:
    tmnxSASDot1agCfmComplianceV2v0.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TIMETRA-SAS-IEEE8021-CFM-MIB",
    **{"timetraSASIEEE8021CfmMIBModule": timetraSASIEEE8021CfmMIBModule,
       "tmnxSASDot1agMIBConformance": tmnxSASDot1agMIBConformance,
       "tmnxSASDot1agCfmCompliances": tmnxSASDot1agCfmCompliances,
       "tmnxSASDot1agCfmComplianceV2v0": tmnxSASDot1agCfmComplianceV2v0,
       "tmnxSASDot1agCfmGroups": tmnxSASDot1agCfmGroups,
       "tmnxSASDot1agCfmMepGroupV2v0": tmnxSASDot1agCfmMepGroupV2v0,
       "tmnxSASDot1agCfmMepGroupV4v0": tmnxSASDot1agCfmMepGroupV4v0,
       "tmnxSASDot1agMIBObjs": tmnxSASDot1agMIBObjs,
       "tmnxSASDot1agCfmMep": tmnxSASDot1agCfmMep,
       "tmnxDot1agCfmMepExtnTable": tmnxDot1agCfmMepExtnTable,
       "tmnxDot1agCfmMepExtnEntry": tmnxDot1agCfmMepExtnEntry,
       "tmnxDot1agCfmMepSendAisOnPortDown": tmnxDot1agCfmMepSendAisOnPortDown,
       "tmnxDot1agCfmMepControlSapTag": tmnxDot1agCfmMepControlSapTag,
       "tmnxSASDot1agNotificationsPrefix": tmnxSASDot1agNotificationsPrefix,
       "tmnxSASDot1agNotifications": tmnxSASDot1agNotifications}
)
