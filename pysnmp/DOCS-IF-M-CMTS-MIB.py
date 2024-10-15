# SNMP MIB module (DOCS-IF-M-CMTS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/DOCS-IF-M-CMTS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:32:43 2024
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

(clabProjDocsis,) = mibBuilder.importSymbols(
    "CLAB-DEF-MIB",
    "clabProjDocsis")

(TenthdBmV,) = mibBuilder.importSymbols(
    "DOCS-IF-MIB",
    "TenthdBmV")

(docsQosServiceFlowId,) = mibBuilder.importSymbols(
    "DOCS-QOS-MIB",
    "docsQosServiceFlowId")

(PhysicalIndex,
 PhysicalIndexOrZero,
 entPhysicalAlias,
 entPhysicalAssetID,
 entPhysicalClass,
 entPhysicalSerialNum,
 entityGeneralGroup,
 entityLogical2Group,
 entityMappingGroup,
 entityPhysical2Group,
 entityPhysical3Group,
 entityPhysicalGroup) = mibBuilder.importSymbols(
    "ENTITY-MIB",
    "PhysicalIndex",
    "PhysicalIndexOrZero",
    "entPhysicalAlias",
    "entPhysicalAssetID",
    "entPhysicalClass",
    "entPhysicalSerialNum",
    "entityGeneralGroup",
    "entityLogical2Group",
    "entityMappingGroup",
    "entityPhysical2Group",
    "entityPhysical3Group",
    "entityPhysicalGroup")

(InterfaceIndex,
 InterfaceIndexOrZero,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "InterfaceIndexOrZero",
    "ifIndex")

(InetAddress,
 InetAddressType,
 InetPortNumber) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType",
    "InetPortNumber")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

(SnmpTagValue,) = mibBuilder.importSymbols(
    "SNMP-TARGET-MIB",
    "SnmpTagValue")

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

(AutonomousType,
 DisplayString,
 RowStatus,
 StorageType,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "AutonomousType",
    "DisplayString",
    "RowStatus",
    "StorageType",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

docsIfMCmtsMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 6)
)
docsIfMCmtsMib.setRevisions(
        ("2005-11-16 00:00",
         "2005-08-05 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_DocsIfMCmtsNotifications_ObjectIdentity = ObjectIdentity
docsIfMCmtsNotifications = _DocsIfMCmtsNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 6, 0)
)
_DocsIfMCmtsObjects_ObjectIdentity = ObjectIdentity
docsIfMCmtsObjects = _DocsIfMCmtsObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 6, 1)
)
_DocsIfMCmtsBaseObjects_ObjectIdentity = ObjectIdentity
docsIfMCmtsBaseObjects = _DocsIfMCmtsBaseObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 6, 1, 1)
)
_DocsIfMCmtsBaseAdmin_ObjectIdentity = ObjectIdentity
docsIfMCmtsBaseAdmin = _DocsIfMCmtsBaseAdmin_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 6, 1, 1, 1)
)
if mibBuilder.loadTexts:
    docsIfMCmtsBaseAdmin.setStatus("current")
_DocsPHYParamFixValue_ObjectIdentity = ObjectIdentity
docsPHYParamFixValue = _DocsPHYParamFixValue_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 6, 1, 1, 1, 1)
)
if mibBuilder.loadTexts:
    docsPHYParamFixValue.setStatus("current")
_DocsPHYParamSameValue_ObjectIdentity = ObjectIdentity
docsPHYParamSameValue = _DocsPHYParamSameValue_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 6, 1, 1, 1, 2)
)
if mibBuilder.loadTexts:
    docsPHYParamSameValue.setStatus("current")
_DocsPHYParamAdjacentValues_ObjectIdentity = ObjectIdentity
docsPHYParamAdjacentValues = _DocsPHYParamAdjacentValues_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 6, 1, 1, 1, 3)
)
if mibBuilder.loadTexts:
    docsPHYParamAdjacentValues.setStatus("current")
_DocsPHYParamFrequencyRange_ObjectIdentity = ObjectIdentity
docsPHYParamFrequencyRange = _DocsPHYParamFrequencyRange_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 6, 1, 1, 1, 4)
)
if mibBuilder.loadTexts:
    docsPHYParamFrequencyRange.setStatus("current")
_DocsIfMCmtsCoreObjects_ObjectIdentity = ObjectIdentity
docsIfMCmtsCoreObjects = _DocsIfMCmtsCoreObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 6, 1, 2)
)
_DocsIfMCmtsCoreDownstreamTable_Object = MibTable
docsIfMCmtsCoreDownstreamTable = _DocsIfMCmtsCoreDownstreamTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 6, 1, 2, 1)
)
if mibBuilder.loadTexts:
    docsIfMCmtsCoreDownstreamTable.setStatus("current")
_DocsIfMCmtsCoreDownstreamEntry_Object = MibTableRow
docsIfMCmtsCoreDownstreamEntry = _DocsIfMCmtsCoreDownstreamEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 6, 1, 2, 1, 1)
)
docsIfMCmtsCoreDownstreamEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    docsIfMCmtsCoreDownstreamEntry.setStatus("current")


class _DocsIfMCmtsCoreDownstreamType_Type(Integer32):
    """Custom type docsIfMCmtsCoreDownstreamType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("external", 2),
          ("integrated", 1))
    )


_DocsIfMCmtsCoreDownstreamType_Type.__name__ = "Integer32"
_DocsIfMCmtsCoreDownstreamType_Object = MibTableColumn
docsIfMCmtsCoreDownstreamType = _DocsIfMCmtsCoreDownstreamType_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 6, 1, 2, 1, 1, 1),
    _DocsIfMCmtsCoreDownstreamType_Type()
)
docsIfMCmtsCoreDownstreamType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIfMCmtsCoreDownstreamType.setStatus("current")


class _DocsIfMCmtsCoreDownstreamPhyDependencies_Type(Bits):
    """Custom type docsIfMCmtsCoreDownstreamPhyDependencies based on Bits"""
    defaultHexValue = "00000000"

    namedValues = NamedValues(
        *(("bandwidth", 1),
          ("frequency", 0),
          ("interleaver", 4),
          ("j83Annex", 5),
          ("modulation", 3),
          ("mute", 7),
          ("power", 2),
          ("symbolRate", 6))
    )

_DocsIfMCmtsCoreDownstreamPhyDependencies_Type.__name__ = "Bits"
_DocsIfMCmtsCoreDownstreamPhyDependencies_Object = MibTableColumn
docsIfMCmtsCoreDownstreamPhyDependencies = _DocsIfMCmtsCoreDownstreamPhyDependencies_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 6, 1, 2, 1, 1, 2),
    _DocsIfMCmtsCoreDownstreamPhyDependencies_Type()
)
docsIfMCmtsCoreDownstreamPhyDependencies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIfMCmtsCoreDownstreamPhyDependencies.setStatus("current")
_DocsIfMCmtsEqamObjects_ObjectIdentity = ObjectIdentity
docsIfMCmtsEqamObjects = _DocsIfMCmtsEqamObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 6, 1, 3)
)
_DocsIfMCmtsEqamDownstreamTable_Object = MibTable
docsIfMCmtsEqamDownstreamTable = _DocsIfMCmtsEqamDownstreamTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 6, 1, 3, 1)
)
if mibBuilder.loadTexts:
    docsIfMCmtsEqamDownstreamTable.setStatus("current")
_DocsIfMCmtsEqamDownstreamEntry_Object = MibTableRow
docsIfMCmtsEqamDownstreamEntry = _DocsIfMCmtsEqamDownstreamEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 6, 1, 3, 1, 1)
)
docsIfMCmtsEqamDownstreamEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    docsIfMCmtsEqamDownstreamEntry.setStatus("current")


class _DocsIfMCmtsEqamDownstreamTSID_Type(Unsigned32):
    """Custom type docsIfMCmtsEqamDownstreamTSID based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DocsIfMCmtsEqamDownstreamTSID_Type.__name__ = "Unsigned32"
_DocsIfMCmtsEqamDownstreamTSID_Object = MibTableColumn
docsIfMCmtsEqamDownstreamTSID = _DocsIfMCmtsEqamDownstreamTSID_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 6, 1, 3, 1, 1, 1),
    _DocsIfMCmtsEqamDownstreamTSID_Type()
)
docsIfMCmtsEqamDownstreamTSID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsIfMCmtsEqamDownstreamTSID.setStatus("current")


class _DocsIfMCmtsEqamDownstreamPhyDependencies_Type(Bits):
    """Custom type docsIfMCmtsEqamDownstreamPhyDependencies based on Bits"""
    defaultHexValue = "00000000"

    namedValues = NamedValues(
        *(("bandwidth", 1),
          ("frequency", 0),
          ("interleaver", 4),
          ("j83Annex", 5),
          ("modulation", 3),
          ("mute", 7),
          ("power", 2),
          ("symbolRate", 6))
    )

_DocsIfMCmtsEqamDownstreamPhyDependencies_Type.__name__ = "Bits"
_DocsIfMCmtsEqamDownstreamPhyDependencies_Object = MibTableColumn
docsIfMCmtsEqamDownstreamPhyDependencies = _DocsIfMCmtsEqamDownstreamPhyDependencies_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 6, 1, 3, 1, 1, 2),
    _DocsIfMCmtsEqamDownstreamPhyDependencies_Type()
)
docsIfMCmtsEqamDownstreamPhyDependencies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIfMCmtsEqamDownstreamPhyDependencies.setStatus("current")


class _DocsIfMCmtsEqamDownstreamDevicePhyParamLock_Type(Bits):
    """Custom type docsIfMCmtsEqamDownstreamDevicePhyParamLock based on Bits"""
    namedValues = NamedValues(
        *(("bandwidth", 1),
          ("frequency", 0),
          ("interleaver", 4),
          ("j83Annex", 5),
          ("modulation", 3),
          ("mute", 7),
          ("power", 2),
          ("symbolRate", 6))
    )

_DocsIfMCmtsEqamDownstreamDevicePhyParamLock_Type.__name__ = "Bits"
_DocsIfMCmtsEqamDownstreamDevicePhyParamLock_Object = MibTableColumn
docsIfMCmtsEqamDownstreamDevicePhyParamLock = _DocsIfMCmtsEqamDownstreamDevicePhyParamLock_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 6, 1, 3, 1, 1, 3),
    _DocsIfMCmtsEqamDownstreamDevicePhyParamLock_Type()
)
docsIfMCmtsEqamDownstreamDevicePhyParamLock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIfMCmtsEqamDownstreamDevicePhyParamLock.setStatus("current")


class _DocsIfMCmtsEqamDownstreamDeviceConfigPhyParamLock_Type(Bits):
    """Custom type docsIfMCmtsEqamDownstreamDeviceConfigPhyParamLock based on Bits"""
    namedValues = NamedValues(
        *(("bandwidth", 1),
          ("frequency", 0),
          ("interleaver", 4),
          ("j83Annex", 5),
          ("modulation", 3),
          ("mute", 7),
          ("power", 2),
          ("symbolRate", 6))
    )

_DocsIfMCmtsEqamDownstreamDeviceConfigPhyParamLock_Type.__name__ = "Bits"
_DocsIfMCmtsEqamDownstreamDeviceConfigPhyParamLock_Object = MibTableColumn
docsIfMCmtsEqamDownstreamDeviceConfigPhyParamLock = _DocsIfMCmtsEqamDownstreamDeviceConfigPhyParamLock_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 6, 1, 3, 1, 1, 4),
    _DocsIfMCmtsEqamDownstreamDeviceConfigPhyParamLock_Type()
)
docsIfMCmtsEqamDownstreamDeviceConfigPhyParamLock.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsIfMCmtsEqamDownstreamDeviceConfigPhyParamLock.setStatus("current")


class _DocsIfMCmtsEqamDownstreamAllocationType_Type(Integer32):
    """Custom type docsIfMCmtsEqamDownstreamAllocationType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("any", 3),
          ("docsisOnly", 1),
          ("videoOnly", 2))
    )


_DocsIfMCmtsEqamDownstreamAllocationType_Type.__name__ = "Integer32"
_DocsIfMCmtsEqamDownstreamAllocationType_Object = MibTableColumn
docsIfMCmtsEqamDownstreamAllocationType = _DocsIfMCmtsEqamDownstreamAllocationType_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 6, 1, 3, 1, 1, 5),
    _DocsIfMCmtsEqamDownstreamAllocationType_Type()
)
docsIfMCmtsEqamDownstreamAllocationType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsIfMCmtsEqamDownstreamAllocationType.setStatus("current")


class _DocsIfMCmtsEqamDownstreamAllocationStatus_Type(Bits):
    """Custom type docsIfMCmtsEqamDownstreamAllocationStatus based on Bits"""
    namedValues = NamedValues(
        *(("docsisDepi", 1),
          ("docsisErm", 2),
          ("other", 0),
          ("videoErm", 3))
    )

_DocsIfMCmtsEqamDownstreamAllocationStatus_Type.__name__ = "Bits"
_DocsIfMCmtsEqamDownstreamAllocationStatus_Object = MibTableColumn
docsIfMCmtsEqamDownstreamAllocationStatus = _DocsIfMCmtsEqamDownstreamAllocationStatus_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 6, 1, 3, 1, 1, 6),
    _DocsIfMCmtsEqamDownstreamAllocationStatus_Type()
)
docsIfMCmtsEqamDownstreamAllocationStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIfMCmtsEqamDownstreamAllocationStatus.setStatus("current")


class _DocsIfMCmtsEqamDownstreamAllocationTimeout_Type(Unsigned32):
    """Custom type docsIfMCmtsEqamDownstreamAllocationTimeout based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 120),
    )


_DocsIfMCmtsEqamDownstreamAllocationTimeout_Type.__name__ = "Unsigned32"
_DocsIfMCmtsEqamDownstreamAllocationTimeout_Object = MibTableColumn
docsIfMCmtsEqamDownstreamAllocationTimeout = _DocsIfMCmtsEqamDownstreamAllocationTimeout_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 6, 1, 3, 1, 1, 7),
    _DocsIfMCmtsEqamDownstreamAllocationTimeout_Type()
)
docsIfMCmtsEqamDownstreamAllocationTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsIfMCmtsEqamDownstreamAllocationTimeout.setStatus("current")
if mibBuilder.loadTexts:
    docsIfMCmtsEqamDownstreamAllocationTimeout.setUnits("seconds")


class _DocsIfMCmtsEqamDownstreamDRRPAdvertizing_Type(TruthValue):
    """Custom type docsIfMCmtsEqamDownstreamDRRPAdvertizing based on TruthValue"""


_DocsIfMCmtsEqamDownstreamDRRPAdvertizing_Object = MibTableColumn
docsIfMCmtsEqamDownstreamDRRPAdvertizing = _DocsIfMCmtsEqamDownstreamDRRPAdvertizing_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 6, 1, 3, 1, 1, 8),
    _DocsIfMCmtsEqamDownstreamDRRPAdvertizing_Type()
)
docsIfMCmtsEqamDownstreamDRRPAdvertizing.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsIfMCmtsEqamDownstreamDRRPAdvertizing.setStatus("current")
_DocsIfMCmtsEqamDownstreamUdpPortMapping_Type = InetPortNumber
_DocsIfMCmtsEqamDownstreamUdpPortMapping_Object = MibTableColumn
docsIfMCmtsEqamDownstreamUdpPortMapping = _DocsIfMCmtsEqamDownstreamUdpPortMapping_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 6, 1, 3, 1, 1, 9),
    _DocsIfMCmtsEqamDownstreamUdpPortMapping_Type()
)
docsIfMCmtsEqamDownstreamUdpPortMapping.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIfMCmtsEqamDownstreamUdpPortMapping.setStatus("current")
_DocsIfMCmtsEqamDownstreamCapabilitiesTable_Object = MibTable
docsIfMCmtsEqamDownstreamCapabilitiesTable = _DocsIfMCmtsEqamDownstreamCapabilitiesTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 6, 1, 3, 2)
)
if mibBuilder.loadTexts:
    docsIfMCmtsEqamDownstreamCapabilitiesTable.setStatus("current")
_DocsIfMCmtsEqamDownstreamCapabilitiesEntry_Object = MibTableRow
docsIfMCmtsEqamDownstreamCapabilitiesEntry = _DocsIfMCmtsEqamDownstreamCapabilitiesEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 6, 1, 3, 2, 1)
)
docsIfMCmtsEqamDownstreamCapabilitiesEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    docsIfMCmtsEqamDownstreamCapabilitiesEntry.setStatus("current")


class _DocsIfMCmtsEqamDownstreamCapabFrequency_Type(Bits):
    """Custom type docsIfMCmtsEqamDownstreamCapabFrequency based on Bits"""
    namedValues = NamedValues(
        *(("adjacentChannel", 1),
          ("adjacentChannelOrder", 2),
          ("eqamDependency", 0))
    )

_DocsIfMCmtsEqamDownstreamCapabFrequency_Type.__name__ = "Bits"
_DocsIfMCmtsEqamDownstreamCapabFrequency_Object = MibTableColumn
docsIfMCmtsEqamDownstreamCapabFrequency = _DocsIfMCmtsEqamDownstreamCapabFrequency_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 6, 1, 3, 2, 1, 1),
    _DocsIfMCmtsEqamDownstreamCapabFrequency_Type()
)
docsIfMCmtsEqamDownstreamCapabFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIfMCmtsEqamDownstreamCapabFrequency.setStatus("current")


class _DocsIfMCmtsEqamDownstreamCapabBandwidth_Type(Bits):
    """Custom type docsIfMCmtsEqamDownstreamCapabBandwidth based on Bits"""
    namedValues = NamedValues(
        *(("chan6Mhz", 1),
          ("chan8Mhz", 2),
          ("eqamDependency", 0))
    )

_DocsIfMCmtsEqamDownstreamCapabBandwidth_Type.__name__ = "Bits"
_DocsIfMCmtsEqamDownstreamCapabBandwidth_Object = MibTableColumn
docsIfMCmtsEqamDownstreamCapabBandwidth = _DocsIfMCmtsEqamDownstreamCapabBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 6, 1, 3, 2, 1, 2),
    _DocsIfMCmtsEqamDownstreamCapabBandwidth_Type()
)
docsIfMCmtsEqamDownstreamCapabBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIfMCmtsEqamDownstreamCapabBandwidth.setStatus("current")


class _DocsIfMCmtsEqamDownstreamCapabPower_Type(Bits):
    """Custom type docsIfMCmtsEqamDownstreamCapabPower based on Bits"""
    namedValues = NamedValues(
        ("eqamDependency", 0)
    )

_DocsIfMCmtsEqamDownstreamCapabPower_Type.__name__ = "Bits"
_DocsIfMCmtsEqamDownstreamCapabPower_Object = MibTableColumn
docsIfMCmtsEqamDownstreamCapabPower = _DocsIfMCmtsEqamDownstreamCapabPower_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 6, 1, 3, 2, 1, 3),
    _DocsIfMCmtsEqamDownstreamCapabPower_Type()
)
docsIfMCmtsEqamDownstreamCapabPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIfMCmtsEqamDownstreamCapabPower.setStatus("current")


class _DocsIfMCmtsEqamDownstreamCapabModulation_Type(Bits):
    """Custom type docsIfMCmtsEqamDownstreamCapabModulation based on Bits"""
    namedValues = NamedValues(
        *(("eqamDependency", 0),
          ("qam256", 2),
          ("qam64", 1))
    )

_DocsIfMCmtsEqamDownstreamCapabModulation_Type.__name__ = "Bits"
_DocsIfMCmtsEqamDownstreamCapabModulation_Object = MibTableColumn
docsIfMCmtsEqamDownstreamCapabModulation = _DocsIfMCmtsEqamDownstreamCapabModulation_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 6, 1, 3, 2, 1, 4),
    _DocsIfMCmtsEqamDownstreamCapabModulation_Type()
)
docsIfMCmtsEqamDownstreamCapabModulation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIfMCmtsEqamDownstreamCapabModulation.setStatus("current")


class _DocsIfMCmtsEqamDownstreamCapabInterleaver_Type(Bits):
    """Custom type docsIfMCmtsEqamDownstreamCapabInterleaver based on Bits"""
    namedValues = NamedValues(
        *(("eqamDependency", 0),
          ("taps128Increment1", 5),
          ("taps128increment2", 7),
          ("taps128increment3", 8),
          ("taps128increment4", 9),
          ("taps128increment5", 10),
          ("taps128increment6", 11),
          ("taps128increment7", 12),
          ("taps128increment8", 13),
          ("taps12increment17", 6),
          ("taps16Increment8", 2),
          ("taps32Increment4", 3),
          ("taps64Increment2", 4),
          ("taps8Increment16", 1))
    )

_DocsIfMCmtsEqamDownstreamCapabInterleaver_Type.__name__ = "Bits"
_DocsIfMCmtsEqamDownstreamCapabInterleaver_Object = MibTableColumn
docsIfMCmtsEqamDownstreamCapabInterleaver = _DocsIfMCmtsEqamDownstreamCapabInterleaver_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 6, 1, 3, 2, 1, 5),
    _DocsIfMCmtsEqamDownstreamCapabInterleaver_Type()
)
docsIfMCmtsEqamDownstreamCapabInterleaver.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIfMCmtsEqamDownstreamCapabInterleaver.setStatus("current")


class _DocsIfMCmtsEqamDownstreamCapabJ83Annex_Type(Bits):
    """Custom type docsIfMCmtsEqamDownstreamCapabJ83Annex based on Bits"""
    namedValues = NamedValues(
        *(("annexA", 1),
          ("annexB", 2),
          ("annexC", 3),
          ("eqamDependency", 0))
    )

_DocsIfMCmtsEqamDownstreamCapabJ83Annex_Type.__name__ = "Bits"
_DocsIfMCmtsEqamDownstreamCapabJ83Annex_Object = MibTableColumn
docsIfMCmtsEqamDownstreamCapabJ83Annex = _DocsIfMCmtsEqamDownstreamCapabJ83Annex_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 6, 1, 3, 2, 1, 6),
    _DocsIfMCmtsEqamDownstreamCapabJ83Annex_Type()
)
docsIfMCmtsEqamDownstreamCapabJ83Annex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIfMCmtsEqamDownstreamCapabJ83Annex.setStatus("current")


class _DocsIfMCmtsEqamDownstreamCapabConcurrentServices_Type(Bits):
    """Custom type docsIfMCmtsEqamDownstreamCapabConcurrentServices based on Bits"""
    namedValues = NamedValues(
        *(("eqamDependency", 0),
          ("videoAndDocsis", 1))
    )

_DocsIfMCmtsEqamDownstreamCapabConcurrentServices_Type.__name__ = "Bits"
_DocsIfMCmtsEqamDownstreamCapabConcurrentServices_Object = MibTableColumn
docsIfMCmtsEqamDownstreamCapabConcurrentServices = _DocsIfMCmtsEqamDownstreamCapabConcurrentServices_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 6, 1, 3, 2, 1, 7),
    _DocsIfMCmtsEqamDownstreamCapabConcurrentServices_Type()
)
docsIfMCmtsEqamDownstreamCapabConcurrentServices.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIfMCmtsEqamDownstreamCapabConcurrentServices.setStatus("current")


class _DocsIfMCmtsEqamDownstreamCapabServicesTransport_Type(Bits):
    """Custom type docsIfMCmtsEqamDownstreamCapabServicesTransport based on Bits"""
    namedValues = NamedValues(
        *(("dmpt", 2),
          ("mpeg2OverIP", 1),
          ("psp", 3),
          ("qamDependency", 0))
    )

_DocsIfMCmtsEqamDownstreamCapabServicesTransport_Type.__name__ = "Bits"
_DocsIfMCmtsEqamDownstreamCapabServicesTransport_Object = MibTableColumn
docsIfMCmtsEqamDownstreamCapabServicesTransport = _DocsIfMCmtsEqamDownstreamCapabServicesTransport_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 6, 1, 3, 2, 1, 8),
    _DocsIfMCmtsEqamDownstreamCapabServicesTransport_Type()
)
docsIfMCmtsEqamDownstreamCapabServicesTransport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIfMCmtsEqamDownstreamCapabServicesTransport.setStatus("current")


class _DocsIfMCmtsEqamDownstreamCapabMuting_Type(Bits):
    """Custom type docsIfMCmtsEqamDownstreamCapabMuting based on Bits"""
    namedValues = NamedValues(
        ("eqamDependency", 0)
    )

_DocsIfMCmtsEqamDownstreamCapabMuting_Type.__name__ = "Bits"
_DocsIfMCmtsEqamDownstreamCapabMuting_Object = MibTableColumn
docsIfMCmtsEqamDownstreamCapabMuting = _DocsIfMCmtsEqamDownstreamCapabMuting_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 6, 1, 3, 2, 1, 9),
    _DocsIfMCmtsEqamDownstreamCapabMuting_Type()
)
docsIfMCmtsEqamDownstreamCapabMuting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIfMCmtsEqamDownstreamCapabMuting.setStatus("current")
_DocsIfMCmtsEqamGroupDependencyTable_Object = MibTable
docsIfMCmtsEqamGroupDependencyTable = _DocsIfMCmtsEqamGroupDependencyTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 6, 1, 3, 3)
)
if mibBuilder.loadTexts:
    docsIfMCmtsEqamGroupDependencyTable.setStatus("current")
_DocsIfMCmtsEqamGroupDependencyEntry_Object = MibTableRow
docsIfMCmtsEqamGroupDependencyEntry = _DocsIfMCmtsEqamGroupDependencyEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 6, 1, 3, 3, 1)
)
docsIfMCmtsEqamGroupDependencyEntry.setIndexNames(
    (0, "DOCS-IF-M-CMTS-MIB", "docsIfMCmtsEqamGroupDependencyPhyParam"),
    (0, "DOCS-IF-M-CMTS-MIB", "docsIfMCmtsEqamGroupDependencyPhysicalIndex"),
)
if mibBuilder.loadTexts:
    docsIfMCmtsEqamGroupDependencyEntry.setStatus("current")


class _DocsIfMCmtsEqamGroupDependencyPhyParam_Type(Integer32):
    """Custom type docsIfMCmtsEqamGroupDependencyPhyParam based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
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
        *(("all", 1),
          ("annex", 7),
          ("bandwidth", 3),
          ("frequency", 2),
          ("interleave", 6),
          ("modulation", 5),
          ("mute", 9),
          ("noDependencies", 0),
          ("power", 4),
          ("symbolRate", 8))
    )


_DocsIfMCmtsEqamGroupDependencyPhyParam_Type.__name__ = "Integer32"
_DocsIfMCmtsEqamGroupDependencyPhyParam_Object = MibTableColumn
docsIfMCmtsEqamGroupDependencyPhyParam = _DocsIfMCmtsEqamGroupDependencyPhyParam_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 6, 1, 3, 3, 1, 1),
    _DocsIfMCmtsEqamGroupDependencyPhyParam_Type()
)
docsIfMCmtsEqamGroupDependencyPhyParam.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    docsIfMCmtsEqamGroupDependencyPhyParam.setStatus("current")
_DocsIfMCmtsEqamGroupDependencyPhysicalIndex_Type = PhysicalIndexOrZero
_DocsIfMCmtsEqamGroupDependencyPhysicalIndex_Object = MibTableColumn
docsIfMCmtsEqamGroupDependencyPhysicalIndex = _DocsIfMCmtsEqamGroupDependencyPhysicalIndex_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 6, 1, 3, 3, 1, 2),
    _DocsIfMCmtsEqamGroupDependencyPhysicalIndex_Type()
)
docsIfMCmtsEqamGroupDependencyPhysicalIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    docsIfMCmtsEqamGroupDependencyPhysicalIndex.setStatus("current")


class _DocsIfMCmtsEqamGroupDependencyGroupID_Type(Unsigned32):
    """Custom type docsIfMCmtsEqamGroupDependencyGroupID based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 127),
    )


_DocsIfMCmtsEqamGroupDependencyGroupID_Type.__name__ = "Unsigned32"
_DocsIfMCmtsEqamGroupDependencyGroupID_Object = MibTableColumn
docsIfMCmtsEqamGroupDependencyGroupID = _DocsIfMCmtsEqamGroupDependencyGroupID_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 6, 1, 3, 3, 1, 3),
    _DocsIfMCmtsEqamGroupDependencyGroupID_Type()
)
docsIfMCmtsEqamGroupDependencyGroupID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIfMCmtsEqamGroupDependencyGroupID.setStatus("current")
_DocsIfMCmtsEqamGroupDependencyType_Type = AutonomousType
_DocsIfMCmtsEqamGroupDependencyType_Object = MibTableColumn
docsIfMCmtsEqamGroupDependencyType = _DocsIfMCmtsEqamGroupDependencyType_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 6, 1, 3, 3, 1, 4),
    _DocsIfMCmtsEqamGroupDependencyType_Type()
)
docsIfMCmtsEqamGroupDependencyType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIfMCmtsEqamGroupDependencyType.setStatus("current")
_DocsIfMCmtsEqamGlobCfgDownTable_Object = MibTable
docsIfMCmtsEqamGlobCfgDownTable = _DocsIfMCmtsEqamGlobCfgDownTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 6, 1, 3, 4)
)
if mibBuilder.loadTexts:
    docsIfMCmtsEqamGlobCfgDownTable.setStatus("current")
_DocsIfMCmtsEqamGlobCfgDownEntry_Object = MibTableRow
docsIfMCmtsEqamGlobCfgDownEntry = _DocsIfMCmtsEqamGlobCfgDownEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 6, 1, 3, 4, 1)
)
docsIfMCmtsEqamGlobCfgDownEntry.setIndexNames(
    (0, "DOCS-IF-M-CMTS-MIB", "docsIfMCmtsEqamGlobCfgDownIndex"),
)
if mibBuilder.loadTexts:
    docsIfMCmtsEqamGlobCfgDownEntry.setStatus("current")
_DocsIfMCmtsEqamGlobCfgDownIndex_Type = Unsigned32
_DocsIfMCmtsEqamGlobCfgDownIndex_Object = MibTableColumn
docsIfMCmtsEqamGlobCfgDownIndex = _DocsIfMCmtsEqamGlobCfgDownIndex_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 6, 1, 3, 4, 1, 1),
    _DocsIfMCmtsEqamGlobCfgDownIndex_Type()
)
docsIfMCmtsEqamGlobCfgDownIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    docsIfMCmtsEqamGlobCfgDownIndex.setStatus("current")
_DocsIfMCmtsEqamGlobCfgDownPhysicalIndex_Type = PhysicalIndexOrZero
_DocsIfMCmtsEqamGlobCfgDownPhysicalIndex_Object = MibTableColumn
docsIfMCmtsEqamGlobCfgDownPhysicalIndex = _DocsIfMCmtsEqamGlobCfgDownPhysicalIndex_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 6, 1, 3, 4, 1, 2),
    _DocsIfMCmtsEqamGlobCfgDownPhysicalIndex_Type()
)
docsIfMCmtsEqamGlobCfgDownPhysicalIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsIfMCmtsEqamGlobCfgDownPhysicalIndex.setStatus("current")


class _DocsIfMCmtsEqamGlobCfgDownBandwidth_Type(Integer32):
    """Custom type docsIfMCmtsEqamGlobCfgDownBandwidth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(6000000, 6000000),
        ValueRangeConstraint(8000000, 8000000),
    )


_DocsIfMCmtsEqamGlobCfgDownBandwidth_Type.__name__ = "Integer32"
_DocsIfMCmtsEqamGlobCfgDownBandwidth_Object = MibTableColumn
docsIfMCmtsEqamGlobCfgDownBandwidth = _DocsIfMCmtsEqamGlobCfgDownBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 6, 1, 3, 4, 1, 3),
    _DocsIfMCmtsEqamGlobCfgDownBandwidth_Type()
)
docsIfMCmtsEqamGlobCfgDownBandwidth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsIfMCmtsEqamGlobCfgDownBandwidth.setStatus("current")
if mibBuilder.loadTexts:
    docsIfMCmtsEqamGlobCfgDownBandwidth.setUnits("hertz")
_DocsIfMCmtsEqamGlobCfgDownPower_Type = TenthdBmV
_DocsIfMCmtsEqamGlobCfgDownPower_Object = MibTableColumn
docsIfMCmtsEqamGlobCfgDownPower = _DocsIfMCmtsEqamGlobCfgDownPower_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 6, 1, 3, 4, 1, 4),
    _DocsIfMCmtsEqamGlobCfgDownPower_Type()
)
docsIfMCmtsEqamGlobCfgDownPower.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsIfMCmtsEqamGlobCfgDownPower.setStatus("current")
if mibBuilder.loadTexts:
    docsIfMCmtsEqamGlobCfgDownPower.setUnits("dBmV")


class _DocsIfMCmtsEqamGlobCfgDownModulation_Type(Integer32):
    """Custom type docsIfMCmtsEqamGlobCfgDownModulation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("qam256", 4),
          ("qam64", 3))
    )


_DocsIfMCmtsEqamGlobCfgDownModulation_Type.__name__ = "Integer32"
_DocsIfMCmtsEqamGlobCfgDownModulation_Object = MibTableColumn
docsIfMCmtsEqamGlobCfgDownModulation = _DocsIfMCmtsEqamGlobCfgDownModulation_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 6, 1, 3, 4, 1, 5),
    _DocsIfMCmtsEqamGlobCfgDownModulation_Type()
)
docsIfMCmtsEqamGlobCfgDownModulation.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsIfMCmtsEqamGlobCfgDownModulation.setStatus("current")


class _DocsIfMCmtsEqamGlobCfgDownInterleave_Type(Integer32):
    """Custom type docsIfMCmtsEqamGlobCfgDownInterleave based on Integer32"""
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
              15)
        )
    )
    namedValues = NamedValues(
        *(("other", 2),
          ("tabs128increment2", 9),
          ("tabs128increment3", 10),
          ("tabs128increment4", 11),
          ("tabs128increment5", 12),
          ("tabs128increment6", 13),
          ("tabs128increment7", 14),
          ("tabs128increment8", 15),
          ("taps128Increment1", 7),
          ("taps12increment17", 8),
          ("taps16Increment8", 4),
          ("taps32Increment4", 5),
          ("taps64Increment2", 6),
          ("taps8Increment16", 3),
          ("unknown", 1))
    )


_DocsIfMCmtsEqamGlobCfgDownInterleave_Type.__name__ = "Integer32"
_DocsIfMCmtsEqamGlobCfgDownInterleave_Object = MibTableColumn
docsIfMCmtsEqamGlobCfgDownInterleave = _DocsIfMCmtsEqamGlobCfgDownInterleave_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 6, 1, 3, 4, 1, 6),
    _DocsIfMCmtsEqamGlobCfgDownInterleave_Type()
)
docsIfMCmtsEqamGlobCfgDownInterleave.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsIfMCmtsEqamGlobCfgDownInterleave.setStatus("current")


class _DocsIfMCmtsEqamGlogCfgDownAnnex_Type(Integer32):
    """Custom type docsIfMCmtsEqamGlogCfgDownAnnex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("annexA", 3),
          ("annexB", 4),
          ("annexC", 5))
    )


_DocsIfMCmtsEqamGlogCfgDownAnnex_Type.__name__ = "Integer32"
_DocsIfMCmtsEqamGlogCfgDownAnnex_Object = MibTableColumn
docsIfMCmtsEqamGlogCfgDownAnnex = _DocsIfMCmtsEqamGlogCfgDownAnnex_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 6, 1, 3, 4, 1, 7),
    _DocsIfMCmtsEqamGlogCfgDownAnnex_Type()
)
docsIfMCmtsEqamGlogCfgDownAnnex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsIfMCmtsEqamGlogCfgDownAnnex.setStatus("current")


class _DocsIfMCmtsEqamGlobCfgDownSymbolRateM_Type(Unsigned32):
    """Custom type docsIfMCmtsEqamGlobCfgDownSymbolRateM based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_DocsIfMCmtsEqamGlobCfgDownSymbolRateM_Type.__name__ = "Unsigned32"
_DocsIfMCmtsEqamGlobCfgDownSymbolRateM_Object = MibTableColumn
docsIfMCmtsEqamGlobCfgDownSymbolRateM = _DocsIfMCmtsEqamGlobCfgDownSymbolRateM_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 6, 1, 3, 4, 1, 8),
    _DocsIfMCmtsEqamGlobCfgDownSymbolRateM_Type()
)
docsIfMCmtsEqamGlobCfgDownSymbolRateM.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsIfMCmtsEqamGlobCfgDownSymbolRateM.setStatus("current")


class _DocsIfMCmtsEqamGlobCfgDownSymbolRateN_Type(Unsigned32):
    """Custom type docsIfMCmtsEqamGlobCfgDownSymbolRateN based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_DocsIfMCmtsEqamGlobCfgDownSymbolRateN_Type.__name__ = "Unsigned32"
_DocsIfMCmtsEqamGlobCfgDownSymbolRateN_Object = MibTableColumn
docsIfMCmtsEqamGlobCfgDownSymbolRateN = _DocsIfMCmtsEqamGlobCfgDownSymbolRateN_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 6, 1, 3, 4, 1, 9),
    _DocsIfMCmtsEqamGlobCfgDownSymbolRateN_Type()
)
docsIfMCmtsEqamGlobCfgDownSymbolRateN.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsIfMCmtsEqamGlobCfgDownSymbolRateN.setStatus("current")


class _DocsIfMCmtsEqamGlobCfgDownLockParams_Type(Bits):
    """Custom type docsIfMCmtsEqamGlobCfgDownLockParams based on Bits"""
    defaultHexValue = "00000000"

    namedValues = NamedValues(
        *(("bandwidth", 1),
          ("frequency", 0),
          ("interleaver", 4),
          ("j83Annex", 5),
          ("modulation", 3),
          ("power", 2),
          ("symbolRate", 6))
    )

_DocsIfMCmtsEqamGlobCfgDownLockParams_Type.__name__ = "Bits"
_DocsIfMCmtsEqamGlobCfgDownLockParams_Object = MibTableColumn
docsIfMCmtsEqamGlobCfgDownLockParams = _DocsIfMCmtsEqamGlobCfgDownLockParams_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 6, 1, 3, 4, 1, 10),
    _DocsIfMCmtsEqamGlobCfgDownLockParams_Type()
)
docsIfMCmtsEqamGlobCfgDownLockParams.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsIfMCmtsEqamGlobCfgDownLockParams.setStatus("current")


class _DocsIfMCmtsEqamGlobCfgDownExecutionCode_Type(Integer32):
    """Custom type docsIfMCmtsEqamGlobCfgDownExecutionCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("complete", 1),
          ("errorNoCommitted", 5),
          ("errorNoPhysIndex", 2),
          ("errorNoQAMChannels", 3),
          ("errorOther", 7),
          ("errorSetFailures", 4),
          ("warningDependencies", 6))
    )


_DocsIfMCmtsEqamGlobCfgDownExecutionCode_Type.__name__ = "Integer32"
_DocsIfMCmtsEqamGlobCfgDownExecutionCode_Object = MibTableColumn
docsIfMCmtsEqamGlobCfgDownExecutionCode = _DocsIfMCmtsEqamGlobCfgDownExecutionCode_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 6, 1, 3, 4, 1, 12),
    _DocsIfMCmtsEqamGlobCfgDownExecutionCode_Type()
)
docsIfMCmtsEqamGlobCfgDownExecutionCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIfMCmtsEqamGlobCfgDownExecutionCode.setStatus("current")
_DocsIfMCmtsEqamGlobCfgDownErrorsCount_Type = Gauge32
_DocsIfMCmtsEqamGlobCfgDownErrorsCount_Object = MibTableColumn
docsIfMCmtsEqamGlobCfgDownErrorsCount = _DocsIfMCmtsEqamGlobCfgDownErrorsCount_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 6, 1, 3, 4, 1, 13),
    _DocsIfMCmtsEqamGlobCfgDownErrorsCount_Type()
)
docsIfMCmtsEqamGlobCfgDownErrorsCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIfMCmtsEqamGlobCfgDownErrorsCount.setStatus("current")
_DocsIfMCmtsEqamGlobCfgDownRowStatus_Type = RowStatus
_DocsIfMCmtsEqamGlobCfgDownRowStatus_Object = MibTableColumn
docsIfMCmtsEqamGlobCfgDownRowStatus = _DocsIfMCmtsEqamGlobCfgDownRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 6, 1, 3, 4, 1, 14),
    _DocsIfMCmtsEqamGlobCfgDownRowStatus_Type()
)
docsIfMCmtsEqamGlobCfgDownRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsIfMCmtsEqamGlobCfgDownRowStatus.setStatus("current")
_DocsIfMCmtsChannelBlockTable_Object = MibTable
docsIfMCmtsChannelBlockTable = _DocsIfMCmtsChannelBlockTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 6, 1, 3, 5)
)
if mibBuilder.loadTexts:
    docsIfMCmtsChannelBlockTable.setStatus("current")
_DocsIfMCmtsChannelBlockEntry_Object = MibTableRow
docsIfMCmtsChannelBlockEntry = _DocsIfMCmtsChannelBlockEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 6, 1, 3, 5, 1)
)
docsIfMCmtsChannelBlockEntry.setIndexNames(
    (0, "DOCS-IF-M-CMTS-MIB", "docsIfMCmtsChannelBlockPhysicalIndex"),
)
if mibBuilder.loadTexts:
    docsIfMCmtsChannelBlockEntry.setStatus("current")
_DocsIfMCmtsChannelBlockPhysicalIndex_Type = PhysicalIndex
_DocsIfMCmtsChannelBlockPhysicalIndex_Object = MibTableColumn
docsIfMCmtsChannelBlockPhysicalIndex = _DocsIfMCmtsChannelBlockPhysicalIndex_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 6, 1, 3, 5, 1, 1),
    _DocsIfMCmtsChannelBlockPhysicalIndex_Type()
)
docsIfMCmtsChannelBlockPhysicalIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    docsIfMCmtsChannelBlockPhysicalIndex.setStatus("current")
_DocsIfMCmtsChannelBlockNumberChannels_Type = Unsigned32
_DocsIfMCmtsChannelBlockNumberChannels_Object = MibTableColumn
docsIfMCmtsChannelBlockNumberChannels = _DocsIfMCmtsChannelBlockNumberChannels_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 6, 1, 3, 5, 1, 2),
    _DocsIfMCmtsChannelBlockNumberChannels_Type()
)
docsIfMCmtsChannelBlockNumberChannels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIfMCmtsChannelBlockNumberChannels.setStatus("current")


class _DocsIfMCmtsChannelBlockCfgNumberChannels_Type(Unsigned32):
    """Custom type docsIfMCmtsChannelBlockCfgNumberChannels based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 119),
    )


_DocsIfMCmtsChannelBlockCfgNumberChannels_Type.__name__ = "Unsigned32"
_DocsIfMCmtsChannelBlockCfgNumberChannels_Object = MibTableColumn
docsIfMCmtsChannelBlockCfgNumberChannels = _DocsIfMCmtsChannelBlockCfgNumberChannels_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 6, 1, 3, 5, 1, 3),
    _DocsIfMCmtsChannelBlockCfgNumberChannels_Type()
)
docsIfMCmtsChannelBlockCfgNumberChannels.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsIfMCmtsChannelBlockCfgNumberChannels.setStatus("current")
_DocsIfMCmtsChannelBlockMute_Type = TruthValue
_DocsIfMCmtsChannelBlockMute_Object = MibTableColumn
docsIfMCmtsChannelBlockMute = _DocsIfMCmtsChannelBlockMute_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 6, 1, 3, 5, 1, 4),
    _DocsIfMCmtsChannelBlockMute_Type()
)
docsIfMCmtsChannelBlockMute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsIfMCmtsChannelBlockMute.setStatus("current")


class _DocsIfMCmtsChannelBlockTestType_Type(Integer32):
    """Custom type docsIfMCmtsChannelBlockTestType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("allOff", 3),
          ("clockTest", 7),
          ("cwOnOthersNormal", 6),
          ("cwOnOthersOff", 5),
          ("noTest", 1),
          ("offOthersNormal", 2),
          ("onOthersOff", 4))
    )


_DocsIfMCmtsChannelBlockTestType_Type.__name__ = "Integer32"
_DocsIfMCmtsChannelBlockTestType_Object = MibTableColumn
docsIfMCmtsChannelBlockTestType = _DocsIfMCmtsChannelBlockTestType_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 6, 1, 3, 5, 1, 5),
    _DocsIfMCmtsChannelBlockTestType_Type()
)
docsIfMCmtsChannelBlockTestType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIfMCmtsChannelBlockTestType.setStatus("current")
_DocsIfMCmtsChannelBlockTestIfIndex_Type = InterfaceIndexOrZero
_DocsIfMCmtsChannelBlockTestIfIndex_Object = MibTableColumn
docsIfMCmtsChannelBlockTestIfIndex = _DocsIfMCmtsChannelBlockTestIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 6, 1, 3, 5, 1, 6),
    _DocsIfMCmtsChannelBlockTestIfIndex_Type()
)
docsIfMCmtsChannelBlockTestIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsIfMCmtsChannelBlockTestIfIndex.setStatus("current")
_DocsIfMCmtsDepiObjects_ObjectIdentity = ObjectIdentity
docsIfMCmtsDepiObjects = _DocsIfMCmtsDepiObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 6, 1, 4)
)
_DocsIfMCmtsDepiSessionObjects_ObjectIdentity = ObjectIdentity
docsIfMCmtsDepiSessionObjects = _DocsIfMCmtsDepiSessionObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 6, 1, 4, 1)
)
_DocsIfMCmtsDepiSessionConfigTable_Object = MibTable
docsIfMCmtsDepiSessionConfigTable = _DocsIfMCmtsDepiSessionConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 6, 1, 4, 1, 1)
)
if mibBuilder.loadTexts:
    docsIfMCmtsDepiSessionConfigTable.setStatus("current")
_DocsIfMCmtsDepiSessionConfigEntry_Object = MibTableRow
docsIfMCmtsDepiSessionConfigEntry = _DocsIfMCmtsDepiSessionConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 6, 1, 4, 1, 1, 1)
)
docsIfMCmtsDepiSessionConfigEntry.setIndexNames(
    (0, "DOCS-IF-M-CMTS-MIB", "docsIfMCmtsDepiSessionConfigIndex"),
)
if mibBuilder.loadTexts:
    docsIfMCmtsDepiSessionConfigEntry.setStatus("current")


class _DocsIfMCmtsDepiSessionConfigIndex_Type(Unsigned32):
    """Custom type docsIfMCmtsDepiSessionConfigIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_DocsIfMCmtsDepiSessionConfigIndex_Type.__name__ = "Unsigned32"
_DocsIfMCmtsDepiSessionConfigIndex_Object = MibTableColumn
docsIfMCmtsDepiSessionConfigIndex = _DocsIfMCmtsDepiSessionConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 6, 1, 4, 1, 1, 1, 1),
    _DocsIfMCmtsDepiSessionConfigIndex_Type()
)
docsIfMCmtsDepiSessionConfigIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    docsIfMCmtsDepiSessionConfigIndex.setStatus("current")
_DocsIfMCmtsDepiSessionConfigCableMacIfIndex_Type = InterfaceIndexOrZero
_DocsIfMCmtsDepiSessionConfigCableMacIfIndex_Object = MibTableColumn
docsIfMCmtsDepiSessionConfigCableMacIfIndex = _DocsIfMCmtsDepiSessionConfigCableMacIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 6, 1, 4, 1, 1, 1, 2),
    _DocsIfMCmtsDepiSessionConfigCableMacIfIndex_Type()
)
docsIfMCmtsDepiSessionConfigCableMacIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsIfMCmtsDepiSessionConfigCableMacIfIndex.setStatus("current")


class _DocsIfMCmtsDepiSessionConfigCableMCmtsDownIfIndex_Type(InterfaceIndexOrZero):
    """Custom type docsIfMCmtsDepiSessionConfigCableMCmtsDownIfIndex based on InterfaceIndexOrZero"""
    defaultValue = 0


_DocsIfMCmtsDepiSessionConfigCableMCmtsDownIfIndex_Object = MibTableColumn
docsIfMCmtsDepiSessionConfigCableMCmtsDownIfIndex = _DocsIfMCmtsDepiSessionConfigCableMCmtsDownIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 6, 1, 4, 1, 1, 1, 3),
    _DocsIfMCmtsDepiSessionConfigCableMCmtsDownIfIndex_Type()
)
docsIfMCmtsDepiSessionConfigCableMCmtsDownIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsIfMCmtsDepiSessionConfigCableMCmtsDownIfIndex.setStatus("current")


class _DocsIfMCmtsDepiSessionConfigAddrType_Type(InetAddressType):
    """Custom type docsIfMCmtsDepiSessionConfigAddrType based on InetAddressType"""


_DocsIfMCmtsDepiSessionConfigAddrType_Object = MibTableColumn
docsIfMCmtsDepiSessionConfigAddrType = _DocsIfMCmtsDepiSessionConfigAddrType_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 6, 1, 4, 1, 1, 1, 4),
    _DocsIfMCmtsDepiSessionConfigAddrType_Type()
)
docsIfMCmtsDepiSessionConfigAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsIfMCmtsDepiSessionConfigAddrType.setStatus("current")


class _DocsIfMCmtsDepiSessionConfigLocalAddr_Type(InetAddress):
    """Custom type docsIfMCmtsDepiSessionConfigLocalAddr based on InetAddress"""
    defaultHexValue = ""


_DocsIfMCmtsDepiSessionConfigLocalAddr_Object = MibTableColumn
docsIfMCmtsDepiSessionConfigLocalAddr = _DocsIfMCmtsDepiSessionConfigLocalAddr_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 6, 1, 4, 1, 1, 1, 5),
    _DocsIfMCmtsDepiSessionConfigLocalAddr_Type()
)
docsIfMCmtsDepiSessionConfigLocalAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsIfMCmtsDepiSessionConfigLocalAddr.setStatus("current")


class _DocsIfMCmtsDepiSessionConfigRemoteAddr_Type(InetAddress):
    """Custom type docsIfMCmtsDepiSessionConfigRemoteAddr based on InetAddress"""
    defaultHexValue = ""


_DocsIfMCmtsDepiSessionConfigRemoteAddr_Object = MibTableColumn
docsIfMCmtsDepiSessionConfigRemoteAddr = _DocsIfMCmtsDepiSessionConfigRemoteAddr_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 6, 1, 4, 1, 1, 1, 6),
    _DocsIfMCmtsDepiSessionConfigRemoteAddr_Type()
)
docsIfMCmtsDepiSessionConfigRemoteAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsIfMCmtsDepiSessionConfigRemoteAddr.setStatus("current")


class _DocsIfMCmtsDepiSessionConfigL2TPv3HeaderType_Type(Integer32):
    """Custom type docsIfMCmtsDepiSessionConfigL2TPv3HeaderType based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ip", 1),
          ("udp", 2))
    )


_DocsIfMCmtsDepiSessionConfigL2TPv3HeaderType_Type.__name__ = "Integer32"
_DocsIfMCmtsDepiSessionConfigL2TPv3HeaderType_Object = MibTableColumn
docsIfMCmtsDepiSessionConfigL2TPv3HeaderType = _DocsIfMCmtsDepiSessionConfigL2TPv3HeaderType_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 6, 1, 4, 1, 1, 1, 7),
    _DocsIfMCmtsDepiSessionConfigL2TPv3HeaderType_Type()
)
docsIfMCmtsDepiSessionConfigL2TPv3HeaderType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsIfMCmtsDepiSessionConfigL2TPv3HeaderType.setStatus("current")


class _DocsIfMCmtsDepiSessionConfigMethod_Type(Integer32):
    """Custom type docsIfMCmtsDepiSessionConfigMethod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("l2tpControl", 2),
          ("other", 1))
    )


_DocsIfMCmtsDepiSessionConfigMethod_Type.__name__ = "Integer32"
_DocsIfMCmtsDepiSessionConfigMethod_Object = MibTableColumn
docsIfMCmtsDepiSessionConfigMethod = _DocsIfMCmtsDepiSessionConfigMethod_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 6, 1, 4, 1, 1, 1, 8),
    _DocsIfMCmtsDepiSessionConfigMethod_Type()
)
docsIfMCmtsDepiSessionConfigMethod.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsIfMCmtsDepiSessionConfigMethod.setStatus("current")


class _DocsIfMCmtsDepiSessionConfigTSID_Type(Unsigned32):
    """Custom type docsIfMCmtsDepiSessionConfigTSID based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DocsIfMCmtsDepiSessionConfigTSID_Type.__name__ = "Unsigned32"
_DocsIfMCmtsDepiSessionConfigTSID_Object = MibTableColumn
docsIfMCmtsDepiSessionConfigTSID = _DocsIfMCmtsDepiSessionConfigTSID_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 6, 1, 4, 1, 1, 1, 9),
    _DocsIfMCmtsDepiSessionConfigTSID_Type()
)
docsIfMCmtsDepiSessionConfigTSID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsIfMCmtsDepiSessionConfigTSID.setStatus("current")


class _DocsIfMCmtsDepiSessionConfigDEPIMode_Type(Integer32):
    """Custom type docsIfMCmtsDepiSessionConfigDEPIMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dmpt", 1),
          ("psp", 2))
    )


_DocsIfMCmtsDepiSessionConfigDEPIMode_Type.__name__ = "Integer32"
_DocsIfMCmtsDepiSessionConfigDEPIMode_Object = MibTableColumn
docsIfMCmtsDepiSessionConfigDEPIMode = _DocsIfMCmtsDepiSessionConfigDEPIMode_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 6, 1, 4, 1, 1, 1, 10),
    _DocsIfMCmtsDepiSessionConfigDEPIMode_Type()
)
docsIfMCmtsDepiSessionConfigDEPIMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsIfMCmtsDepiSessionConfigDEPIMode.setStatus("current")


class _DocsIfMCmtsDepiSessionConfigRsrcAllocReq_Type(Unsigned32):
    """Custom type docsIfMCmtsDepiSessionConfigRsrcAllocReq based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_DocsIfMCmtsDepiSessionConfigRsrcAllocReq_Type.__name__ = "Unsigned32"
_DocsIfMCmtsDepiSessionConfigRsrcAllocReq_Object = MibTableColumn
docsIfMCmtsDepiSessionConfigRsrcAllocReq = _DocsIfMCmtsDepiSessionConfigRsrcAllocReq_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 6, 1, 4, 1, 1, 1, 11),
    _DocsIfMCmtsDepiSessionConfigRsrcAllocReq_Type()
)
docsIfMCmtsDepiSessionConfigRsrcAllocReq.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsIfMCmtsDepiSessionConfigRsrcAllocReq.setStatus("current")
_DocsIfMCmtsDepiSessionConfigCinPhbIdPolicy_Type = SnmpTagValue
_DocsIfMCmtsDepiSessionConfigCinPhbIdPolicy_Object = MibTableColumn
docsIfMCmtsDepiSessionConfigCinPhbIdPolicy = _DocsIfMCmtsDepiSessionConfigCinPhbIdPolicy_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 6, 1, 4, 1, 1, 1, 12),
    _DocsIfMCmtsDepiSessionConfigCinPhbIdPolicy_Type()
)
docsIfMCmtsDepiSessionConfigCinPhbIdPolicy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsIfMCmtsDepiSessionConfigCinPhbIdPolicy.setStatus("current")


class _DocsIfMCmtsDepiSessionConfigSyncEnabled_Type(TruthValue):
    """Custom type docsIfMCmtsDepiSessionConfigSyncEnabled based on TruthValue"""


_DocsIfMCmtsDepiSessionConfigSyncEnabled_Object = MibTableColumn
docsIfMCmtsDepiSessionConfigSyncEnabled = _DocsIfMCmtsDepiSessionConfigSyncEnabled_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 6, 1, 4, 1, 1, 1, 13),
    _DocsIfMCmtsDepiSessionConfigSyncEnabled_Type()
)
docsIfMCmtsDepiSessionConfigSyncEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsIfMCmtsDepiSessionConfigSyncEnabled.setStatus("current")


class _DocsIfMCmtsDepiSessionConfigSyncInterval_Type(Unsigned32):
    """Custom type docsIfMCmtsDepiSessionConfigSyncInterval based on Unsigned32"""
    defaultValue = 1000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 1000),
    )


_DocsIfMCmtsDepiSessionConfigSyncInterval_Type.__name__ = "Unsigned32"
_DocsIfMCmtsDepiSessionConfigSyncInterval_Object = MibTableColumn
docsIfMCmtsDepiSessionConfigSyncInterval = _DocsIfMCmtsDepiSessionConfigSyncInterval_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 6, 1, 4, 1, 1, 1, 14),
    _DocsIfMCmtsDepiSessionConfigSyncInterval_Type()
)
docsIfMCmtsDepiSessionConfigSyncInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsIfMCmtsDepiSessionConfigSyncInterval.setStatus("current")
if mibBuilder.loadTexts:
    docsIfMCmtsDepiSessionConfigSyncInterval.setUnits("docsisSyncSteps")


class _DocsIfMCmtsDepiSessionConfigPhyParamsFlag_Type(Bits):
    """Custom type docsIfMCmtsDepiSessionConfigPhyParamsFlag based on Bits"""
    defaultHexValue = "00000000"

    namedValues = NamedValues(
        *(("bandwidth", 1),
          ("frequency", 0),
          ("interleaver", 4),
          ("j83Annex", 5),
          ("modulation", 3),
          ("mute", 7),
          ("power", 2),
          ("symbolRate", 6))
    )

_DocsIfMCmtsDepiSessionConfigPhyParamsFlag_Type.__name__ = "Bits"
_DocsIfMCmtsDepiSessionConfigPhyParamsFlag_Object = MibTableColumn
docsIfMCmtsDepiSessionConfigPhyParamsFlag = _DocsIfMCmtsDepiSessionConfigPhyParamsFlag_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 6, 1, 4, 1, 1, 1, 15),
    _DocsIfMCmtsDepiSessionConfigPhyParamsFlag_Type()
)
docsIfMCmtsDepiSessionConfigPhyParamsFlag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsIfMCmtsDepiSessionConfigPhyParamsFlag.setStatus("current")


class _DocsIfMCmtsDepiSessionConfigChannelFrequency_Type(Unsigned32):
    """Custom type docsIfMCmtsDepiSessionConfigChannelFrequency based on Unsigned32"""
    defaultValue = 0


_DocsIfMCmtsDepiSessionConfigChannelFrequency_Object = MibTableColumn
docsIfMCmtsDepiSessionConfigChannelFrequency = _DocsIfMCmtsDepiSessionConfigChannelFrequency_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 6, 1, 4, 1, 1, 1, 16),
    _DocsIfMCmtsDepiSessionConfigChannelFrequency_Type()
)
docsIfMCmtsDepiSessionConfigChannelFrequency.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsIfMCmtsDepiSessionConfigChannelFrequency.setStatus("current")


class _DocsIfMCmtsDepiSessionConfigChannelModulation_Type(Integer32):
    """Custom type docsIfMCmtsDepiSessionConfigChannelModulation based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("qam256", 4),
          ("qam64", 3),
          ("unknown", 1))
    )


_DocsIfMCmtsDepiSessionConfigChannelModulation_Type.__name__ = "Integer32"
_DocsIfMCmtsDepiSessionConfigChannelModulation_Object = MibTableColumn
docsIfMCmtsDepiSessionConfigChannelModulation = _DocsIfMCmtsDepiSessionConfigChannelModulation_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 6, 1, 4, 1, 1, 1, 17),
    _DocsIfMCmtsDepiSessionConfigChannelModulation_Type()
)
docsIfMCmtsDepiSessionConfigChannelModulation.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsIfMCmtsDepiSessionConfigChannelModulation.setStatus("current")


class _DocsIfMCmtsDepiSessionConfigChannelInterleave_Type(Integer32):
    """Custom type docsIfMCmtsDepiSessionConfigChannelInterleave based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
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
              15)
        )
    )
    namedValues = NamedValues(
        *(("tabs128increment2", 9),
          ("tabs128increment3", 10),
          ("tabs128increment4", 11),
          ("tabs128increment5", 12),
          ("tabs128increment6", 13),
          ("tabs128increment7", 14),
          ("tabs128increment8", 15),
          ("taps128Increment1", 7),
          ("taps12increment17", 8),
          ("taps16Increment8", 4),
          ("taps32Increment4", 5),
          ("taps64Increment2", 6),
          ("taps8Increment16", 3),
          ("unknown", 1))
    )


_DocsIfMCmtsDepiSessionConfigChannelInterleave_Type.__name__ = "Integer32"
_DocsIfMCmtsDepiSessionConfigChannelInterleave_Object = MibTableColumn
docsIfMCmtsDepiSessionConfigChannelInterleave = _DocsIfMCmtsDepiSessionConfigChannelInterleave_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 6, 1, 4, 1, 1, 1, 18),
    _DocsIfMCmtsDepiSessionConfigChannelInterleave_Type()
)
docsIfMCmtsDepiSessionConfigChannelInterleave.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsIfMCmtsDepiSessionConfigChannelInterleave.setStatus("current")


class _DocsIfMCmtsDepiSessionConfigChannelPower_Type(TenthdBmV):
    """Custom type docsIfMCmtsDepiSessionConfigChannelPower based on TenthdBmV"""
    defaultValue = 0


_DocsIfMCmtsDepiSessionConfigChannelPower_Object = MibTableColumn
docsIfMCmtsDepiSessionConfigChannelPower = _DocsIfMCmtsDepiSessionConfigChannelPower_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 6, 1, 4, 1, 1, 1, 19),
    _DocsIfMCmtsDepiSessionConfigChannelPower_Type()
)
docsIfMCmtsDepiSessionConfigChannelPower.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsIfMCmtsDepiSessionConfigChannelPower.setStatus("current")


class _DocsIfMCmtsDepiSessionConfigChannelAnnex_Type(Integer32):
    """Custom type docsIfMCmtsDepiSessionConfigChannelAnnex based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("annexA", 3),
          ("annexB", 4),
          ("annexC", 5),
          ("unknown", 1))
    )


_DocsIfMCmtsDepiSessionConfigChannelAnnex_Type.__name__ = "Integer32"
_DocsIfMCmtsDepiSessionConfigChannelAnnex_Object = MibTableColumn
docsIfMCmtsDepiSessionConfigChannelAnnex = _DocsIfMCmtsDepiSessionConfigChannelAnnex_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 6, 1, 4, 1, 1, 1, 20),
    _DocsIfMCmtsDepiSessionConfigChannelAnnex_Type()
)
docsIfMCmtsDepiSessionConfigChannelAnnex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsIfMCmtsDepiSessionConfigChannelAnnex.setStatus("current")


class _DocsIfMCmtsDepiSessionConfigChannelSymbolRateM_Type(Unsigned32):
    """Custom type docsIfMCmtsDepiSessionConfigChannelSymbolRateM based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_DocsIfMCmtsDepiSessionConfigChannelSymbolRateM_Type.__name__ = "Unsigned32"
_DocsIfMCmtsDepiSessionConfigChannelSymbolRateM_Object = MibTableColumn
docsIfMCmtsDepiSessionConfigChannelSymbolRateM = _DocsIfMCmtsDepiSessionConfigChannelSymbolRateM_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 6, 1, 4, 1, 1, 1, 21),
    _DocsIfMCmtsDepiSessionConfigChannelSymbolRateM_Type()
)
docsIfMCmtsDepiSessionConfigChannelSymbolRateM.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsIfMCmtsDepiSessionConfigChannelSymbolRateM.setStatus("current")


class _DocsIfMCmtsDepiSessionConfigChannelSymbolRateN_Type(Unsigned32):
    """Custom type docsIfMCmtsDepiSessionConfigChannelSymbolRateN based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_DocsIfMCmtsDepiSessionConfigChannelSymbolRateN_Type.__name__ = "Unsigned32"
_DocsIfMCmtsDepiSessionConfigChannelSymbolRateN_Object = MibTableColumn
docsIfMCmtsDepiSessionConfigChannelSymbolRateN = _DocsIfMCmtsDepiSessionConfigChannelSymbolRateN_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 6, 1, 4, 1, 1, 1, 22),
    _DocsIfMCmtsDepiSessionConfigChannelSymbolRateN_Type()
)
docsIfMCmtsDepiSessionConfigChannelSymbolRateN.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsIfMCmtsDepiSessionConfigChannelSymbolRateN.setStatus("current")


class _DocsIfMCmtsDepiSessionConfigChannelOutputRate_Type(Unsigned32):
    """Custom type docsIfMCmtsDepiSessionConfigChannelOutputRate based on Unsigned32"""
    defaultValue = 99

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_DocsIfMCmtsDepiSessionConfigChannelOutputRate_Type.__name__ = "Unsigned32"
_DocsIfMCmtsDepiSessionConfigChannelOutputRate_Object = MibTableColumn
docsIfMCmtsDepiSessionConfigChannelOutputRate = _DocsIfMCmtsDepiSessionConfigChannelOutputRate_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 6, 1, 4, 1, 1, 1, 23),
    _DocsIfMCmtsDepiSessionConfigChannelOutputRate_Type()
)
docsIfMCmtsDepiSessionConfigChannelOutputRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsIfMCmtsDepiSessionConfigChannelOutputRate.setStatus("current")
_DocsIfMCmtsDepiSessionConfigChannelBurstSize_Type = Unsigned32
_DocsIfMCmtsDepiSessionConfigChannelBurstSize_Object = MibTableColumn
docsIfMCmtsDepiSessionConfigChannelBurstSize = _DocsIfMCmtsDepiSessionConfigChannelBurstSize_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 6, 1, 4, 1, 1, 1, 24),
    _DocsIfMCmtsDepiSessionConfigChannelBurstSize_Type()
)
docsIfMCmtsDepiSessionConfigChannelBurstSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsIfMCmtsDepiSessionConfigChannelBurstSize.setStatus("current")
_DocsIfMCmtsDepiSessionConfigStorage_Type = StorageType
_DocsIfMCmtsDepiSessionConfigStorage_Object = MibTableColumn
docsIfMCmtsDepiSessionConfigStorage = _DocsIfMCmtsDepiSessionConfigStorage_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 6, 1, 4, 1, 1, 1, 25),
    _DocsIfMCmtsDepiSessionConfigStorage_Type()
)
docsIfMCmtsDepiSessionConfigStorage.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsIfMCmtsDepiSessionConfigStorage.setStatus("current")
_DocsIfMCmtsDepiSessionConfigRowStatus_Type = RowStatus
_DocsIfMCmtsDepiSessionConfigRowStatus_Object = MibTableColumn
docsIfMCmtsDepiSessionConfigRowStatus = _DocsIfMCmtsDepiSessionConfigRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 6, 1, 4, 1, 1, 1, 26),
    _DocsIfMCmtsDepiSessionConfigRowStatus_Type()
)
docsIfMCmtsDepiSessionConfigRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsIfMCmtsDepiSessionConfigRowStatus.setStatus("current")
_DocsIfMCmtsDepiSessionConfigChannelId_Type = Unsigned32
_DocsIfMCmtsDepiSessionConfigChannelId_Object = MibTableColumn
docsIfMCmtsDepiSessionConfigChannelId = _DocsIfMCmtsDepiSessionConfigChannelId_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 6, 1, 4, 1, 1, 1, 27),
    _DocsIfMCmtsDepiSessionConfigChannelId_Type()
)
docsIfMCmtsDepiSessionConfigChannelId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsIfMCmtsDepiSessionConfigChannelId.setStatus("current")
_DocsIfMCmtsDepiSessionInfoTable_Object = MibTable
docsIfMCmtsDepiSessionInfoTable = _DocsIfMCmtsDepiSessionInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 6, 1, 4, 1, 2)
)
if mibBuilder.loadTexts:
    docsIfMCmtsDepiSessionInfoTable.setStatus("current")
_DocsIfMCmtsDepiSessionInfoEntry_Object = MibTableRow
docsIfMCmtsDepiSessionInfoEntry = _DocsIfMCmtsDepiSessionInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 6, 1, 4, 1, 2, 1)
)
docsIfMCmtsDepiSessionInfoEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    docsIfMCmtsDepiSessionInfoEntry.setStatus("current")


class _DocsIfMCmtsDepiSessionInfoCfgIndex_Type(Unsigned32):
    """Custom type docsIfMCmtsDepiSessionInfoCfgIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_DocsIfMCmtsDepiSessionInfoCfgIndex_Type.__name__ = "Unsigned32"
_DocsIfMCmtsDepiSessionInfoCfgIndex_Object = MibTableColumn
docsIfMCmtsDepiSessionInfoCfgIndex = _DocsIfMCmtsDepiSessionInfoCfgIndex_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 6, 1, 4, 1, 2, 1, 1),
    _DocsIfMCmtsDepiSessionInfoCfgIndex_Type()
)
docsIfMCmtsDepiSessionInfoCfgIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIfMCmtsDepiSessionInfoCfgIndex.setStatus("current")
_DocsIfMCmtsDepiSessionInfoUdpPort_Type = InetPortNumber
_DocsIfMCmtsDepiSessionInfoUdpPort_Object = MibTableColumn
docsIfMCmtsDepiSessionInfoUdpPort = _DocsIfMCmtsDepiSessionInfoUdpPort_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 6, 1, 4, 1, 2, 1, 2),
    _DocsIfMCmtsDepiSessionInfoUdpPort_Type()
)
docsIfMCmtsDepiSessionInfoUdpPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIfMCmtsDepiSessionInfoUdpPort.setStatus("current")


class _DocsIfMCmtsDepiSessionInfoMaxPayload_Type(Unsigned32):
    """Custom type docsIfMCmtsDepiSessionInfoMaxPayload based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_DocsIfMCmtsDepiSessionInfoMaxPayload_Type.__name__ = "Unsigned32"
_DocsIfMCmtsDepiSessionInfoMaxPayload_Object = MibTableColumn
docsIfMCmtsDepiSessionInfoMaxPayload = _DocsIfMCmtsDepiSessionInfoMaxPayload_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 6, 1, 4, 1, 2, 1, 3),
    _DocsIfMCmtsDepiSessionInfoMaxPayload_Type()
)
docsIfMCmtsDepiSessionInfoMaxPayload.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIfMCmtsDepiSessionInfoMaxPayload.setStatus("current")


class _DocsIfMCmtsDepiSessionInfoPathPayload_Type(Unsigned32):
    """Custom type docsIfMCmtsDepiSessionInfoPathPayload based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_DocsIfMCmtsDepiSessionInfoPathPayload_Type.__name__ = "Unsigned32"
_DocsIfMCmtsDepiSessionInfoPathPayload_Object = MibTableColumn
docsIfMCmtsDepiSessionInfoPathPayload = _DocsIfMCmtsDepiSessionInfoPathPayload_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 6, 1, 4, 1, 2, 1, 4),
    _DocsIfMCmtsDepiSessionInfoPathPayload_Type()
)
docsIfMCmtsDepiSessionInfoPathPayload.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIfMCmtsDepiSessionInfoPathPayload.setStatus("current")


class _DocsIfMCmtsDepiSessionInfoIncludeDOCSISMsgs_Type(TruthValue):
    """Custom type docsIfMCmtsDepiSessionInfoIncludeDOCSISMsgs based on TruthValue"""


_DocsIfMCmtsDepiSessionInfoIncludeDOCSISMsgs_Object = MibTableColumn
docsIfMCmtsDepiSessionInfoIncludeDOCSISMsgs = _DocsIfMCmtsDepiSessionInfoIncludeDOCSISMsgs_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 6, 1, 4, 1, 2, 1, 5),
    _DocsIfMCmtsDepiSessionInfoIncludeDOCSISMsgs_Type()
)
docsIfMCmtsDepiSessionInfoIncludeDOCSISMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIfMCmtsDepiSessionInfoIncludeDOCSISMsgs.setStatus("current")


class _DocsIfMCmtsDepiSessionInfoRsrcAllocResp_Type(Unsigned32):
    """Custom type docsIfMCmtsDepiSessionInfoRsrcAllocResp based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_DocsIfMCmtsDepiSessionInfoRsrcAllocResp_Type.__name__ = "Unsigned32"
_DocsIfMCmtsDepiSessionInfoRsrcAllocResp_Object = MibTableColumn
docsIfMCmtsDepiSessionInfoRsrcAllocResp = _DocsIfMCmtsDepiSessionInfoRsrcAllocResp_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 6, 1, 4, 1, 2, 1, 6),
    _DocsIfMCmtsDepiSessionInfoRsrcAllocResp_Type()
)
docsIfMCmtsDepiSessionInfoRsrcAllocResp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIfMCmtsDepiSessionInfoRsrcAllocResp.setStatus("current")
_DocsIfMCmtsDepiSessionInfoConnCtrlID_Type = Unsigned32
_DocsIfMCmtsDepiSessionInfoConnCtrlID_Object = MibTableColumn
docsIfMCmtsDepiSessionInfoConnCtrlID = _DocsIfMCmtsDepiSessionInfoConnCtrlID_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 6, 1, 4, 1, 2, 1, 7),
    _DocsIfMCmtsDepiSessionInfoConnCtrlID_Type()
)
docsIfMCmtsDepiSessionInfoConnCtrlID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIfMCmtsDepiSessionInfoConnCtrlID.setStatus("current")
_DocsIfMCmtsDepiSessionInfoEQAMSessionID_Type = Unsigned32
_DocsIfMCmtsDepiSessionInfoEQAMSessionID_Object = MibTableColumn
docsIfMCmtsDepiSessionInfoEQAMSessionID = _DocsIfMCmtsDepiSessionInfoEQAMSessionID_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 6, 1, 4, 1, 2, 1, 8),
    _DocsIfMCmtsDepiSessionInfoEQAMSessionID_Type()
)
docsIfMCmtsDepiSessionInfoEQAMSessionID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIfMCmtsDepiSessionInfoEQAMSessionID.setStatus("current")


class _DocsIfMCmtsDepiSessionInfoOwner_Type(Integer32):
    """Custom type docsIfMCmtsDepiSessionInfoOwner based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dynamic", 2),
          ("management", 1))
    )


_DocsIfMCmtsDepiSessionInfoOwner_Type.__name__ = "Integer32"
_DocsIfMCmtsDepiSessionInfoOwner_Object = MibTableColumn
docsIfMCmtsDepiSessionInfoOwner = _DocsIfMCmtsDepiSessionInfoOwner_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 6, 1, 4, 1, 2, 1, 9),
    _DocsIfMCmtsDepiSessionInfoOwner_Type()
)
docsIfMCmtsDepiSessionInfoOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIfMCmtsDepiSessionInfoOwner.setStatus("current")


class _DocsIfMCmtsDepiSessionInfoState_Type(Integer32):
    """Custom type docsIfMCmtsDepiSessionInfoState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("depiSessionError", 3),
          ("depiSessionUp", 2),
          ("other", 1))
    )


_DocsIfMCmtsDepiSessionInfoState_Type.__name__ = "Integer32"
_DocsIfMCmtsDepiSessionInfoState_Object = MibTableColumn
docsIfMCmtsDepiSessionInfoState = _DocsIfMCmtsDepiSessionInfoState_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 6, 1, 4, 1, 2, 1, 10),
    _DocsIfMCmtsDepiSessionInfoState_Type()
)
docsIfMCmtsDepiSessionInfoState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIfMCmtsDepiSessionInfoState.setStatus("current")


class _DocsIfMCmtsDepiSessionInfoErrorCode_Type(Integer32):
    """Custom type docsIfMCmtsDepiSessionInfoErrorCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("ifAdminStatusSetToDown", 6),
          ("invalidDSInterfaceValue", 3),
          ("invalidMACInterfaceValue", 2),
          ("l2tpv3Error", 5),
          ("noResourcesForDSInterfaceIndex", 4),
          ("none", 1))
    )


_DocsIfMCmtsDepiSessionInfoErrorCode_Type.__name__ = "Integer32"
_DocsIfMCmtsDepiSessionInfoErrorCode_Object = MibTableColumn
docsIfMCmtsDepiSessionInfoErrorCode = _DocsIfMCmtsDepiSessionInfoErrorCode_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 6, 1, 4, 1, 2, 1, 11),
    _DocsIfMCmtsDepiSessionInfoErrorCode_Type()
)
docsIfMCmtsDepiSessionInfoErrorCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIfMCmtsDepiSessionInfoErrorCode.setStatus("current")
_DocsIfMCmtsDepiSessionInfoCreationTime_Type = TimeStamp
_DocsIfMCmtsDepiSessionInfoCreationTime_Object = MibTableColumn
docsIfMCmtsDepiSessionInfoCreationTime = _DocsIfMCmtsDepiSessionInfoCreationTime_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 6, 1, 4, 1, 2, 1, 12),
    _DocsIfMCmtsDepiSessionInfoCreationTime_Type()
)
docsIfMCmtsDepiSessionInfoCreationTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIfMCmtsDepiSessionInfoCreationTime.setStatus("current")
_DocsIfMCmtsDepiSessionInfoStorage_Type = StorageType
_DocsIfMCmtsDepiSessionInfoStorage_Object = MibTableColumn
docsIfMCmtsDepiSessionInfoStorage = _DocsIfMCmtsDepiSessionInfoStorage_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 6, 1, 4, 1, 2, 1, 13),
    _DocsIfMCmtsDepiSessionInfoStorage_Type()
)
docsIfMCmtsDepiSessionInfoStorage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIfMCmtsDepiSessionInfoStorage.setStatus("current")
_DocsIfMCmtsDepiRsrcAllocTable_Object = MibTable
docsIfMCmtsDepiRsrcAllocTable = _DocsIfMCmtsDepiRsrcAllocTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 6, 1, 4, 1, 3)
)
if mibBuilder.loadTexts:
    docsIfMCmtsDepiRsrcAllocTable.setStatus("current")
_DocsIfMCmtsDepiRsrcAllocEntry_Object = MibTableRow
docsIfMCmtsDepiRsrcAllocEntry = _DocsIfMCmtsDepiRsrcAllocEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 6, 1, 4, 1, 3, 1)
)
docsIfMCmtsDepiRsrcAllocEntry.setIndexNames(
    (0, "DOCS-IF-M-CMTS-MIB", "docsIfMCmtsDepiRsrcAllocIndex"),
    (0, "DOCS-IF-M-CMTS-MIB", "docsIfMCmtsDepiRsrcAllocSeq"),
)
if mibBuilder.loadTexts:
    docsIfMCmtsDepiRsrcAllocEntry.setStatus("current")


class _DocsIfMCmtsDepiRsrcAllocIndex_Type(Unsigned32):
    """Custom type docsIfMCmtsDepiRsrcAllocIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_DocsIfMCmtsDepiRsrcAllocIndex_Type.__name__ = "Unsigned32"
_DocsIfMCmtsDepiRsrcAllocIndex_Object = MibTableColumn
docsIfMCmtsDepiRsrcAllocIndex = _DocsIfMCmtsDepiRsrcAllocIndex_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 6, 1, 4, 1, 3, 1, 1),
    _DocsIfMCmtsDepiRsrcAllocIndex_Type()
)
docsIfMCmtsDepiRsrcAllocIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    docsIfMCmtsDepiRsrcAllocIndex.setStatus("current")


class _DocsIfMCmtsDepiRsrcAllocSeq_Type(Unsigned32):
    """Custom type docsIfMCmtsDepiRsrcAllocSeq based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_DocsIfMCmtsDepiRsrcAllocSeq_Type.__name__ = "Unsigned32"
_DocsIfMCmtsDepiRsrcAllocSeq_Object = MibTableColumn
docsIfMCmtsDepiRsrcAllocSeq = _DocsIfMCmtsDepiRsrcAllocSeq_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 6, 1, 4, 1, 3, 1, 2),
    _DocsIfMCmtsDepiRsrcAllocSeq_Type()
)
docsIfMCmtsDepiRsrcAllocSeq.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    docsIfMCmtsDepiRsrcAllocSeq.setStatus("current")


class _DocsIfMCmtsDepiRsrcAllocPhbId_Type(Unsigned32):
    """Custom type docsIfMCmtsDepiRsrcAllocPhbId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_DocsIfMCmtsDepiRsrcAllocPhbId_Type.__name__ = "Unsigned32"
_DocsIfMCmtsDepiRsrcAllocPhbId_Object = MibTableColumn
docsIfMCmtsDepiRsrcAllocPhbId = _DocsIfMCmtsDepiRsrcAllocPhbId_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 6, 1, 4, 1, 3, 1, 3),
    _DocsIfMCmtsDepiRsrcAllocPhbId_Type()
)
docsIfMCmtsDepiRsrcAllocPhbId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsIfMCmtsDepiRsrcAllocPhbId.setStatus("current")


class _DocsIfMCmtsDepiRsrcAllocFlowId_Type(Unsigned32):
    """Custom type docsIfMCmtsDepiRsrcAllocFlowId based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 4294967295),
    )


_DocsIfMCmtsDepiRsrcAllocFlowId_Type.__name__ = "Unsigned32"
_DocsIfMCmtsDepiRsrcAllocFlowId_Object = MibTableColumn
docsIfMCmtsDepiRsrcAllocFlowId = _DocsIfMCmtsDepiRsrcAllocFlowId_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 6, 1, 4, 1, 3, 1, 4),
    _DocsIfMCmtsDepiRsrcAllocFlowId_Type()
)
docsIfMCmtsDepiRsrcAllocFlowId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsIfMCmtsDepiRsrcAllocFlowId.setStatus("current")


class _DocsIfMCmtsDepiRsrcAllocUdpPort_Type(InetPortNumber):
    """Custom type docsIfMCmtsDepiRsrcAllocUdpPort based on InetPortNumber"""
    defaultValue = 0


_DocsIfMCmtsDepiRsrcAllocUdpPort_Object = MibTableColumn
docsIfMCmtsDepiRsrcAllocUdpPort = _DocsIfMCmtsDepiRsrcAllocUdpPort_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 6, 1, 4, 1, 3, 1, 5),
    _DocsIfMCmtsDepiRsrcAllocUdpPort_Type()
)
docsIfMCmtsDepiRsrcAllocUdpPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsIfMCmtsDepiRsrcAllocUdpPort.setStatus("current")
_DocsIfMCmtsDepiRsrcAllocPolicyScnTags_Type = SnmpTagValue
_DocsIfMCmtsDepiRsrcAllocPolicyScnTags_Object = MibTableColumn
docsIfMCmtsDepiRsrcAllocPolicyScnTags = _DocsIfMCmtsDepiRsrcAllocPolicyScnTags_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 6, 1, 4, 1, 3, 1, 6),
    _DocsIfMCmtsDepiRsrcAllocPolicyScnTags_Type()
)
docsIfMCmtsDepiRsrcAllocPolicyScnTags.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsIfMCmtsDepiRsrcAllocPolicyScnTags.setStatus("current")


class _DocsIfMCmtsDepiRsrcAllocStorage_Type(StorageType):
    """Custom type docsIfMCmtsDepiRsrcAllocStorage based on StorageType"""


_DocsIfMCmtsDepiRsrcAllocStorage_Object = MibTableColumn
docsIfMCmtsDepiRsrcAllocStorage = _DocsIfMCmtsDepiRsrcAllocStorage_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 6, 1, 4, 1, 3, 1, 7),
    _DocsIfMCmtsDepiRsrcAllocStorage_Type()
)
docsIfMCmtsDepiRsrcAllocStorage.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsIfMCmtsDepiRsrcAllocStorage.setStatus("current")
_DocsIfMCmtsDepiRsrcAllocRowStatus_Type = RowStatus
_DocsIfMCmtsDepiRsrcAllocRowStatus_Object = MibTableColumn
docsIfMCmtsDepiRsrcAllocRowStatus = _DocsIfMCmtsDepiRsrcAllocRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 6, 1, 4, 1, 3, 1, 8),
    _DocsIfMCmtsDepiRsrcAllocRowStatus_Type()
)
docsIfMCmtsDepiRsrcAllocRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsIfMCmtsDepiRsrcAllocRowStatus.setStatus("current")
_DocsIfMCmtsDepiSessionStatsTable_Object = MibTable
docsIfMCmtsDepiSessionStatsTable = _DocsIfMCmtsDepiSessionStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 6, 1, 4, 1, 4)
)
if mibBuilder.loadTexts:
    docsIfMCmtsDepiSessionStatsTable.setStatus("current")
_DocsIfMCmtsDepiSessionStatsEntry_Object = MibTableRow
docsIfMCmtsDepiSessionStatsEntry = _DocsIfMCmtsDepiSessionStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 6, 1, 4, 1, 4, 1)
)
docsIfMCmtsDepiSessionStatsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    docsIfMCmtsDepiSessionStatsEntry.setStatus("current")
_DocsIfMCmtsDepiSessionInfoOutOfSequencePkts_Type = Counter32
_DocsIfMCmtsDepiSessionInfoOutOfSequencePkts_Object = MibTableColumn
docsIfMCmtsDepiSessionInfoOutOfSequencePkts = _DocsIfMCmtsDepiSessionInfoOutOfSequencePkts_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 6, 1, 4, 1, 4, 1, 1),
    _DocsIfMCmtsDepiSessionInfoOutOfSequencePkts_Type()
)
docsIfMCmtsDepiSessionInfoOutOfSequencePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIfMCmtsDepiSessionInfoOutOfSequencePkts.setStatus("current")
_DocsIfMCmtsDepiSessionCinLatency_ObjectIdentity = ObjectIdentity
docsIfMCmtsDepiSessionCinLatency = _DocsIfMCmtsDepiSessionCinLatency_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 6, 1, 4, 1, 5)
)


class _DocsIfMCmtsDepiSessionCinLatencyInterval_Type(Unsigned32):
    """Custom type docsIfMCmtsDepiSessionCinLatencyInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 420),
    )


_DocsIfMCmtsDepiSessionCinLatencyInterval_Type.__name__ = "Unsigned32"
_DocsIfMCmtsDepiSessionCinLatencyInterval_Object = MibScalar
docsIfMCmtsDepiSessionCinLatencyInterval = _DocsIfMCmtsDepiSessionCinLatencyInterval_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 6, 1, 4, 1, 5, 1),
    _DocsIfMCmtsDepiSessionCinLatencyInterval_Type()
)
docsIfMCmtsDepiSessionCinLatencyInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsIfMCmtsDepiSessionCinLatencyInterval.setStatus("current")
if mibBuilder.loadTexts:
    docsIfMCmtsDepiSessionCinLatencyInterval.setUnits("seconds")


class _DocsIfMCmtsDepiSessionCinLatencyThrshld_Type(Unsigned32):
    """Custom type docsIfMCmtsDepiSessionCinLatencyThrshld based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 4294967295),
    )


_DocsIfMCmtsDepiSessionCinLatencyThrshld_Type.__name__ = "Unsigned32"
_DocsIfMCmtsDepiSessionCinLatencyThrshld_Object = MibScalar
docsIfMCmtsDepiSessionCinLatencyThrshld = _DocsIfMCmtsDepiSessionCinLatencyThrshld_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 6, 1, 4, 1, 5, 2),
    _DocsIfMCmtsDepiSessionCinLatencyThrshld_Type()
)
docsIfMCmtsDepiSessionCinLatencyThrshld.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsIfMCmtsDepiSessionCinLatencyThrshld.setStatus("current")
if mibBuilder.loadTexts:
    docsIfMCmtsDepiSessionCinLatencyThrshld.setUnits("MasterClockTicks")


class _DocsIfMCmtsDepiSessionCinEventLevel_Type(Integer32):
    """Custom type docsIfMCmtsDepiSessionCinEventLevel based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("alert", 2),
          ("critical", 3),
          ("debug", 8),
          ("emergency", 1),
          ("error", 4),
          ("information", 7),
          ("notice", 6),
          ("warning", 5))
    )


_DocsIfMCmtsDepiSessionCinEventLevel_Type.__name__ = "Integer32"
_DocsIfMCmtsDepiSessionCinEventLevel_Object = MibScalar
docsIfMCmtsDepiSessionCinEventLevel = _DocsIfMCmtsDepiSessionCinEventLevel_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 6, 1, 4, 1, 5, 3),
    _DocsIfMCmtsDepiSessionCinEventLevel_Type()
)
docsIfMCmtsDepiSessionCinEventLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsIfMCmtsDepiSessionCinEventLevel.setStatus("current")


class _DocsIfMCmtsDepiSessionCinLastValue_Type(Unsigned32):
    """Custom type docsIfMCmtsDepiSessionCinLastValue based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_DocsIfMCmtsDepiSessionCinLastValue_Type.__name__ = "Unsigned32"
_DocsIfMCmtsDepiSessionCinLastValue_Object = MibScalar
docsIfMCmtsDepiSessionCinLastValue = _DocsIfMCmtsDepiSessionCinLastValue_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 6, 1, 4, 1, 5, 4),
    _DocsIfMCmtsDepiSessionCinLastValue_Type()
)
docsIfMCmtsDepiSessionCinLastValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIfMCmtsDepiSessionCinLastValue.setStatus("current")
if mibBuilder.loadTexts:
    docsIfMCmtsDepiSessionCinLastValue.setUnits("MasterClockTicks")
_DocsIfMCmtsDepiSessionCinLastValueIfIndex_Type = InterfaceIndex
_DocsIfMCmtsDepiSessionCinLastValueIfIndex_Object = MibScalar
docsIfMCmtsDepiSessionCinLastValueIfIndex = _DocsIfMCmtsDepiSessionCinLastValueIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 6, 1, 4, 1, 5, 5),
    _DocsIfMCmtsDepiSessionCinLastValueIfIndex_Type()
)
docsIfMCmtsDepiSessionCinLastValueIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIfMCmtsDepiSessionCinLastValueIfIndex.setStatus("current")
_DocsIfMCmtsDepiSessionCinLatencyValueLastTime_Type = TimeTicks
_DocsIfMCmtsDepiSessionCinLatencyValueLastTime_Object = MibScalar
docsIfMCmtsDepiSessionCinLatencyValueLastTime = _DocsIfMCmtsDepiSessionCinLatencyValueLastTime_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 6, 1, 4, 1, 5, 6),
    _DocsIfMCmtsDepiSessionCinLatencyValueLastTime_Type()
)
docsIfMCmtsDepiSessionCinLatencyValueLastTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIfMCmtsDepiSessionCinLatencyValueLastTime.setStatus("current")
_DocsIfMCmtsDepiSessionCinLatencyPerfTable_Object = MibTable
docsIfMCmtsDepiSessionCinLatencyPerfTable = _DocsIfMCmtsDepiSessionCinLatencyPerfTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 6, 1, 4, 1, 6)
)
if mibBuilder.loadTexts:
    docsIfMCmtsDepiSessionCinLatencyPerfTable.setStatus("current")
_DocsIfMCmtsDepiSessionCinLatencyPerfEntry_Object = MibTableRow
docsIfMCmtsDepiSessionCinLatencyPerfEntry = _DocsIfMCmtsDepiSessionCinLatencyPerfEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 6, 1, 4, 1, 6, 1)
)
docsIfMCmtsDepiSessionCinLatencyPerfEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "DOCS-IF-M-CMTS-MIB", "docsIfMCmtsDepiSessionCinLatencyPerfIntervalSeq"),
)
if mibBuilder.loadTexts:
    docsIfMCmtsDepiSessionCinLatencyPerfEntry.setStatus("current")
_DocsIfMCmtsDepiSessionCinLatencyPerfIntervalSeq_Type = Unsigned32
_DocsIfMCmtsDepiSessionCinLatencyPerfIntervalSeq_Object = MibTableColumn
docsIfMCmtsDepiSessionCinLatencyPerfIntervalSeq = _DocsIfMCmtsDepiSessionCinLatencyPerfIntervalSeq_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 6, 1, 4, 1, 6, 1, 1),
    _DocsIfMCmtsDepiSessionCinLatencyPerfIntervalSeq_Type()
)
docsIfMCmtsDepiSessionCinLatencyPerfIntervalSeq.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    docsIfMCmtsDepiSessionCinLatencyPerfIntervalSeq.setStatus("current")


class _DocsIfMCmtsDepiSessionCinLatencyPerfValue_Type(Unsigned32):
    """Custom type docsIfMCmtsDepiSessionCinLatencyPerfValue based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_DocsIfMCmtsDepiSessionCinLatencyPerfValue_Type.__name__ = "Unsigned32"
_DocsIfMCmtsDepiSessionCinLatencyPerfValue_Object = MibTableColumn
docsIfMCmtsDepiSessionCinLatencyPerfValue = _DocsIfMCmtsDepiSessionCinLatencyPerfValue_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 6, 1, 4, 1, 6, 1, 2),
    _DocsIfMCmtsDepiSessionCinLatencyPerfValue_Type()
)
docsIfMCmtsDepiSessionCinLatencyPerfValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIfMCmtsDepiSessionCinLatencyPerfValue.setStatus("current")
if mibBuilder.loadTexts:
    docsIfMCmtsDepiSessionCinLatencyPerfValue.setUnits("MasterClockTicks")
_DocsIfMCmtsDepiSessionCinLatencyTime_Type = TimeTicks
_DocsIfMCmtsDepiSessionCinLatencyTime_Object = MibTableColumn
docsIfMCmtsDepiSessionCinLatencyTime = _DocsIfMCmtsDepiSessionCinLatencyTime_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 6, 1, 4, 1, 6, 1, 3),
    _DocsIfMCmtsDepiSessionCinLatencyTime_Type()
)
docsIfMCmtsDepiSessionCinLatencyTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIfMCmtsDepiSessionCinLatencyTime.setStatus("current")
_DocsIfMCmtsDepiQosObjects_ObjectIdentity = ObjectIdentity
docsIfMCmtsDepiQosObjects = _DocsIfMCmtsDepiQosObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 6, 1, 4, 2)
)
_DocsIfMCmtsDepiPhbPolicyTable_Object = MibTable
docsIfMCmtsDepiPhbPolicyTable = _DocsIfMCmtsDepiPhbPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 6, 1, 4, 2, 1)
)
if mibBuilder.loadTexts:
    docsIfMCmtsDepiPhbPolicyTable.setStatus("current")
_DocsIfMCmtsDepiPhbPolicyEntry_Object = MibTableRow
docsIfMCmtsDepiPhbPolicyEntry = _DocsIfMCmtsDepiPhbPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 6, 1, 4, 2, 1, 1)
)
docsIfMCmtsDepiPhbPolicyEntry.setIndexNames(
    (0, "DOCS-IF-M-CMTS-MIB", "docsIfMCmtsDepiPhbPolicyTag"),
)
if mibBuilder.loadTexts:
    docsIfMCmtsDepiPhbPolicyEntry.setStatus("current")


class _DocsIfMCmtsDepiPhbPolicyTag_Type(SnmpAdminString):
    """Custom type docsIfMCmtsDepiPhbPolicyTag based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_DocsIfMCmtsDepiPhbPolicyTag_Type.__name__ = "SnmpAdminString"
_DocsIfMCmtsDepiPhbPolicyTag_Object = MibTableColumn
docsIfMCmtsDepiPhbPolicyTag = _DocsIfMCmtsDepiPhbPolicyTag_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 6, 1, 4, 2, 1, 1, 1),
    _DocsIfMCmtsDepiPhbPolicyTag_Type()
)
docsIfMCmtsDepiPhbPolicyTag.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    docsIfMCmtsDepiPhbPolicyTag.setStatus("current")


class _DocsIfMCmtsDepiPhbPolicySCN_Type(SnmpAdminString):
    """Custom type docsIfMCmtsDepiPhbPolicySCN based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_DocsIfMCmtsDepiPhbPolicySCN_Type.__name__ = "SnmpAdminString"
_DocsIfMCmtsDepiPhbPolicySCN_Object = MibTableColumn
docsIfMCmtsDepiPhbPolicySCN = _DocsIfMCmtsDepiPhbPolicySCN_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 6, 1, 4, 2, 1, 1, 2),
    _DocsIfMCmtsDepiPhbPolicySCN_Type()
)
docsIfMCmtsDepiPhbPolicySCN.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsIfMCmtsDepiPhbPolicySCN.setStatus("current")


class _DocsIfMCmtsDepiPhbPolicyCinPhbId_Type(Unsigned32):
    """Custom type docsIfMCmtsDepiPhbPolicyCinPhbId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_DocsIfMCmtsDepiPhbPolicyCinPhbId_Type.__name__ = "Unsigned32"
_DocsIfMCmtsDepiPhbPolicyCinPhbId_Object = MibTableColumn
docsIfMCmtsDepiPhbPolicyCinPhbId = _DocsIfMCmtsDepiPhbPolicyCinPhbId_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 6, 1, 4, 2, 1, 1, 3),
    _DocsIfMCmtsDepiPhbPolicyCinPhbId_Type()
)
docsIfMCmtsDepiPhbPolicyCinPhbId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsIfMCmtsDepiPhbPolicyCinPhbId.setStatus("current")
_DocsIfMCmtsDepiPhbPolicyStorage_Type = StorageType
_DocsIfMCmtsDepiPhbPolicyStorage_Object = MibTableColumn
docsIfMCmtsDepiPhbPolicyStorage = _DocsIfMCmtsDepiPhbPolicyStorage_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 6, 1, 4, 2, 1, 1, 4),
    _DocsIfMCmtsDepiPhbPolicyStorage_Type()
)
docsIfMCmtsDepiPhbPolicyStorage.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsIfMCmtsDepiPhbPolicyStorage.setStatus("current")
_DocsIfMCmtsDepiPhbPolicyRowStatus_Type = RowStatus
_DocsIfMCmtsDepiPhbPolicyRowStatus_Object = MibTableColumn
docsIfMCmtsDepiPhbPolicyRowStatus = _DocsIfMCmtsDepiPhbPolicyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 6, 1, 4, 2, 1, 1, 5),
    _DocsIfMCmtsDepiPhbPolicyRowStatus_Type()
)
docsIfMCmtsDepiPhbPolicyRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsIfMCmtsDepiPhbPolicyRowStatus.setStatus("current")
_DocsIfMCmtsQosServiceFlowExtTable_Object = MibTable
docsIfMCmtsQosServiceFlowExtTable = _DocsIfMCmtsQosServiceFlowExtTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 6, 1, 4, 2, 2)
)
if mibBuilder.loadTexts:
    docsIfMCmtsQosServiceFlowExtTable.setStatus("current")
_DocsIfMCmtsQosServiceFlowExtEntry_Object = MibTableRow
docsIfMCmtsQosServiceFlowExtEntry = _DocsIfMCmtsQosServiceFlowExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 6, 1, 4, 2, 2, 1)
)
docsIfMCmtsQosServiceFlowExtEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "DOCS-QOS-MIB", "docsQosServiceFlowId"),
)
if mibBuilder.loadTexts:
    docsIfMCmtsQosServiceFlowExtEntry.setStatus("current")


class _DocsIfMCmtsQosServiceFlowExtDepiFlowId_Type(Unsigned32):
    """Custom type docsIfMCmtsQosServiceFlowExtDepiFlowId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 127),
    )


_DocsIfMCmtsQosServiceFlowExtDepiFlowId_Type.__name__ = "Unsigned32"
_DocsIfMCmtsQosServiceFlowExtDepiFlowId_Object = MibTableColumn
docsIfMCmtsQosServiceFlowExtDepiFlowId = _DocsIfMCmtsQosServiceFlowExtDepiFlowId_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 6, 1, 4, 2, 2, 1, 1),
    _DocsIfMCmtsQosServiceFlowExtDepiFlowId_Type()
)
docsIfMCmtsQosServiceFlowExtDepiFlowId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIfMCmtsQosServiceFlowExtDepiFlowId.setStatus("current")


class _DocsIfMCmtsQosServiceFlowExtCinPhbId_Type(Unsigned32):
    """Custom type docsIfMCmtsQosServiceFlowExtCinPhbId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_DocsIfMCmtsQosServiceFlowExtCinPhbId_Type.__name__ = "Unsigned32"
_DocsIfMCmtsQosServiceFlowExtCinPhbId_Object = MibTableColumn
docsIfMCmtsQosServiceFlowExtCinPhbId = _DocsIfMCmtsQosServiceFlowExtCinPhbId_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 6, 1, 4, 2, 2, 1, 2),
    _DocsIfMCmtsQosServiceFlowExtCinPhbId_Type()
)
docsIfMCmtsQosServiceFlowExtCinPhbId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIfMCmtsQosServiceFlowExtCinPhbId.setStatus("current")
_DocsIfMCmtsQosServiceFlowExtDepiIfIndex_Type = InterfaceIndexOrZero
_DocsIfMCmtsQosServiceFlowExtDepiIfIndex_Object = MibTableColumn
docsIfMCmtsQosServiceFlowExtDepiIfIndex = _DocsIfMCmtsQosServiceFlowExtDepiIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 6, 1, 4, 2, 2, 1, 3),
    _DocsIfMCmtsQosServiceFlowExtDepiIfIndex_Type()
)
docsIfMCmtsQosServiceFlowExtDepiIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIfMCmtsQosServiceFlowExtDepiIfIndex.setStatus("current")
_DocsIfMCmtsConformance_ObjectIdentity = ObjectIdentity
docsIfMCmtsConformance = _DocsIfMCmtsConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 6, 2)
)
_DocsIfMCmtsCompliances_ObjectIdentity = ObjectIdentity
docsIfMCmtsCompliances = _DocsIfMCmtsCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 6, 2, 1)
)
_DocsIfMCmtsGroups_ObjectIdentity = ObjectIdentity
docsIfMCmtsGroups = _DocsIfMCmtsGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 6, 2, 2)
)

# Managed Objects groups

docsIfMCmtsBaseGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 6, 2, 2, 1)
)
docsIfMCmtsBaseGroup.setObjects(
      *(("DOCS-IF-M-CMTS-MIB", "docsIfMCmtsDepiSessionConfigCableMacIfIndex"),
        ("DOCS-IF-M-CMTS-MIB", "docsIfMCmtsDepiSessionConfigCableMCmtsDownIfIndex"),
        ("DOCS-IF-M-CMTS-MIB", "docsIfMCmtsDepiSessionConfigAddrType"),
        ("DOCS-IF-M-CMTS-MIB", "docsIfMCmtsDepiSessionConfigLocalAddr"),
        ("DOCS-IF-M-CMTS-MIB", "docsIfMCmtsDepiSessionConfigRemoteAddr"),
        ("DOCS-IF-M-CMTS-MIB", "docsIfMCmtsDepiSessionConfigL2TPv3HeaderType"),
        ("DOCS-IF-M-CMTS-MIB", "docsIfMCmtsDepiSessionConfigMethod"),
        ("DOCS-IF-M-CMTS-MIB", "docsIfMCmtsDepiSessionConfigTSID"),
        ("DOCS-IF-M-CMTS-MIB", "docsIfMCmtsDepiSessionConfigDEPIMode"),
        ("DOCS-IF-M-CMTS-MIB", "docsIfMCmtsDepiSessionConfigRsrcAllocReq"),
        ("DOCS-IF-M-CMTS-MIB", "docsIfMCmtsDepiSessionConfigCinPhbIdPolicy"),
        ("DOCS-IF-M-CMTS-MIB", "docsIfMCmtsDepiSessionConfigSyncEnabled"),
        ("DOCS-IF-M-CMTS-MIB", "docsIfMCmtsDepiSessionConfigSyncInterval"),
        ("DOCS-IF-M-CMTS-MIB", "docsIfMCmtsDepiSessionConfigPhyParamsFlag"),
        ("DOCS-IF-M-CMTS-MIB", "docsIfMCmtsDepiSessionConfigChannelFrequency"),
        ("DOCS-IF-M-CMTS-MIB", "docsIfMCmtsDepiSessionConfigChannelModulation"),
        ("DOCS-IF-M-CMTS-MIB", "docsIfMCmtsDepiSessionConfigChannelInterleave"),
        ("DOCS-IF-M-CMTS-MIB", "docsIfMCmtsDepiSessionConfigChannelPower"),
        ("DOCS-IF-M-CMTS-MIB", "docsIfMCmtsDepiSessionConfigChannelAnnex"),
        ("DOCS-IF-M-CMTS-MIB", "docsIfMCmtsDepiSessionConfigChannelSymbolRateM"),
        ("DOCS-IF-M-CMTS-MIB", "docsIfMCmtsDepiSessionConfigChannelSymbolRateN"),
        ("DOCS-IF-M-CMTS-MIB", "docsIfMCmtsDepiSessionConfigChannelOutputRate"),
        ("DOCS-IF-M-CMTS-MIB", "docsIfMCmtsDepiSessionConfigChannelBurstSize"),
        ("DOCS-IF-M-CMTS-MIB", "docsIfMCmtsDepiSessionConfigStorage"),
        ("DOCS-IF-M-CMTS-MIB", "docsIfMCmtsDepiSessionConfigRowStatus"),
        ("DOCS-IF-M-CMTS-MIB", "docsIfMCmtsDepiSessionConfigChannelId"),
        ("DOCS-IF-M-CMTS-MIB", "docsIfMCmtsDepiSessionInfoCfgIndex"),
        ("DOCS-IF-M-CMTS-MIB", "docsIfMCmtsDepiSessionInfoUdpPort"),
        ("DOCS-IF-M-CMTS-MIB", "docsIfMCmtsDepiSessionInfoMaxPayload"),
        ("DOCS-IF-M-CMTS-MIB", "docsIfMCmtsDepiSessionInfoPathPayload"),
        ("DOCS-IF-M-CMTS-MIB", "docsIfMCmtsDepiSessionInfoIncludeDOCSISMsgs"),
        ("DOCS-IF-M-CMTS-MIB", "docsIfMCmtsDepiSessionInfoRsrcAllocResp"),
        ("DOCS-IF-M-CMTS-MIB", "docsIfMCmtsDepiSessionInfoConnCtrlID"),
        ("DOCS-IF-M-CMTS-MIB", "docsIfMCmtsDepiSessionInfoEQAMSessionID"),
        ("DOCS-IF-M-CMTS-MIB", "docsIfMCmtsDepiSessionInfoOwner"),
        ("DOCS-IF-M-CMTS-MIB", "docsIfMCmtsDepiSessionInfoState"),
        ("DOCS-IF-M-CMTS-MIB", "docsIfMCmtsDepiSessionInfoErrorCode"),
        ("DOCS-IF-M-CMTS-MIB", "docsIfMCmtsDepiSessionInfoCreationTime"),
        ("DOCS-IF-M-CMTS-MIB", "docsIfMCmtsDepiSessionInfoStorage"),
        ("DOCS-IF-M-CMTS-MIB", "docsIfMCmtsDepiRsrcAllocPhbId"),
        ("DOCS-IF-M-CMTS-MIB", "docsIfMCmtsDepiRsrcAllocFlowId"),
        ("DOCS-IF-M-CMTS-MIB", "docsIfMCmtsDepiRsrcAllocUdpPort"),
        ("DOCS-IF-M-CMTS-MIB", "docsIfMCmtsDepiRsrcAllocPolicyScnTags"),
        ("DOCS-IF-M-CMTS-MIB", "docsIfMCmtsDepiRsrcAllocStorage"),
        ("DOCS-IF-M-CMTS-MIB", "docsIfMCmtsDepiRsrcAllocRowStatus"),
        ("DOCS-IF-M-CMTS-MIB", "docsIfMCmtsDepiSessionInfoOutOfSequencePkts"),
        ("DOCS-IF-M-CMTS-MIB", "docsIfMCmtsDepiSessionCinLatencyInterval"),
        ("DOCS-IF-M-CMTS-MIB", "docsIfMCmtsDepiSessionCinLatencyThrshld"),
        ("DOCS-IF-M-CMTS-MIB", "docsIfMCmtsDepiSessionCinEventLevel"),
        ("DOCS-IF-M-CMTS-MIB", "docsIfMCmtsDepiSessionCinLastValue"),
        ("DOCS-IF-M-CMTS-MIB", "docsIfMCmtsDepiSessionCinLastValueIfIndex"),
        ("DOCS-IF-M-CMTS-MIB", "docsIfMCmtsDepiSessionCinLatencyValueLastTime"))
)
if mibBuilder.loadTexts:
    docsIfMCmtsBaseGroup.setStatus("current")

docsIfMCmtsCoreGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 6, 2, 2, 2)
)
docsIfMCmtsCoreGroup.setObjects(
      *(("DOCS-IF-M-CMTS-MIB", "docsIfMCmtsCoreDownstreamPhyDependencies"),
        ("DOCS-IF-M-CMTS-MIB", "docsIfMCmtsCoreDownstreamType"),
        ("DOCS-IF-M-CMTS-MIB", "docsIfMCmtsQosServiceFlowExtDepiFlowId"),
        ("DOCS-IF-M-CMTS-MIB", "docsIfMCmtsQosServiceFlowExtCinPhbId"),
        ("DOCS-IF-M-CMTS-MIB", "docsIfMCmtsQosServiceFlowExtDepiIfIndex"),
        ("DOCS-IF-M-CMTS-MIB", "docsIfMCmtsDepiSessionCinLatencyPerfValue"),
        ("DOCS-IF-M-CMTS-MIB", "docsIfMCmtsDepiSessionCinLatencyTime"),
        ("DOCS-IF-M-CMTS-MIB", "docsIfMCmtsDepiPhbPolicySCN"),
        ("DOCS-IF-M-CMTS-MIB", "docsIfMCmtsDepiPhbPolicyCinPhbId"),
        ("DOCS-IF-M-CMTS-MIB", "docsIfMCmtsDepiPhbPolicyStorage"),
        ("DOCS-IF-M-CMTS-MIB", "docsIfMCmtsDepiPhbPolicyRowStatus"))
)
if mibBuilder.loadTexts:
    docsIfMCmtsCoreGroup.setStatus("current")

docsIfMCmtsEqamDevGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 6, 2, 2, 3)
)
docsIfMCmtsEqamDevGroup.setObjects(
      *(("DOCS-IF-M-CMTS-MIB", "docsIfMCmtsEqamDownstreamTSID"),
        ("DOCS-IF-M-CMTS-MIB", "docsIfMCmtsEqamDownstreamPhyDependencies"),
        ("DOCS-IF-M-CMTS-MIB", "docsIfMCmtsEqamDownstreamDevicePhyParamLock"),
        ("DOCS-IF-M-CMTS-MIB", "docsIfMCmtsEqamDownstreamDeviceConfigPhyParamLock"),
        ("DOCS-IF-M-CMTS-MIB", "docsIfMCmtsEqamDownstreamAllocationType"),
        ("DOCS-IF-M-CMTS-MIB", "docsIfMCmtsEqamDownstreamAllocationStatus"),
        ("DOCS-IF-M-CMTS-MIB", "docsIfMCmtsEqamDownstreamAllocationTimeout"),
        ("DOCS-IF-M-CMTS-MIB", "docsIfMCmtsEqamDownstreamDRRPAdvertizing"),
        ("DOCS-IF-M-CMTS-MIB", "docsIfMCmtsEqamDownstreamUdpPortMapping"),
        ("DOCS-IF-M-CMTS-MIB", "docsIfMCmtsEqamDownstreamCapabFrequency"),
        ("DOCS-IF-M-CMTS-MIB", "docsIfMCmtsEqamDownstreamCapabBandwidth"),
        ("DOCS-IF-M-CMTS-MIB", "docsIfMCmtsEqamDownstreamCapabPower"),
        ("DOCS-IF-M-CMTS-MIB", "docsIfMCmtsEqamDownstreamCapabModulation"),
        ("DOCS-IF-M-CMTS-MIB", "docsIfMCmtsEqamDownstreamCapabInterleaver"),
        ("DOCS-IF-M-CMTS-MIB", "docsIfMCmtsEqamDownstreamCapabJ83Annex"),
        ("DOCS-IF-M-CMTS-MIB", "docsIfMCmtsEqamDownstreamCapabConcurrentServices"),
        ("DOCS-IF-M-CMTS-MIB", "docsIfMCmtsEqamDownstreamCapabServicesTransport"),
        ("DOCS-IF-M-CMTS-MIB", "docsIfMCmtsEqamDownstreamCapabMuting"),
        ("DOCS-IF-M-CMTS-MIB", "docsIfMCmtsEqamGroupDependencyGroupID"),
        ("DOCS-IF-M-CMTS-MIB", "docsIfMCmtsEqamGroupDependencyType"),
        ("DOCS-IF-M-CMTS-MIB", "docsIfMCmtsEqamGlobCfgDownPhysicalIndex"),
        ("DOCS-IF-M-CMTS-MIB", "docsIfMCmtsEqamGlobCfgDownBandwidth"),
        ("DOCS-IF-M-CMTS-MIB", "docsIfMCmtsEqamGlobCfgDownPower"),
        ("DOCS-IF-M-CMTS-MIB", "docsIfMCmtsEqamGlobCfgDownModulation"),
        ("DOCS-IF-M-CMTS-MIB", "docsIfMCmtsEqamGlobCfgDownInterleave"),
        ("DOCS-IF-M-CMTS-MIB", "docsIfMCmtsEqamGlogCfgDownAnnex"),
        ("DOCS-IF-M-CMTS-MIB", "docsIfMCmtsEqamGlobCfgDownSymbolRateM"),
        ("DOCS-IF-M-CMTS-MIB", "docsIfMCmtsEqamGlobCfgDownSymbolRateN"),
        ("DOCS-IF-M-CMTS-MIB", "docsIfMCmtsEqamGlobCfgDownLockParams"),
        ("DOCS-IF-M-CMTS-MIB", "docsIfMCmtsEqamGlobCfgDownExecutionCode"),
        ("DOCS-IF-M-CMTS-MIB", "docsIfMCmtsEqamGlobCfgDownErrorsCount"),
        ("DOCS-IF-M-CMTS-MIB", "docsIfMCmtsEqamGlobCfgDownRowStatus"),
        ("DOCS-IF-M-CMTS-MIB", "docsIfMCmtsChannelBlockNumberChannels"),
        ("DOCS-IF-M-CMTS-MIB", "docsIfMCmtsChannelBlockCfgNumberChannels"),
        ("DOCS-IF-M-CMTS-MIB", "docsIfMCmtsChannelBlockMute"),
        ("DOCS-IF-M-CMTS-MIB", "docsIfMCmtsChannelBlockTestType"),
        ("DOCS-IF-M-CMTS-MIB", "docsIfMCmtsChannelBlockTestIfIndex"))
)
if mibBuilder.loadTexts:
    docsIfMCmtsEqamDevGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

docsIfMCmtsCoreDeviceCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 6, 2, 1, 1)
)
if mibBuilder.loadTexts:
    docsIfMCmtsCoreDeviceCompliance.setStatus(
        "current"
    )

docsIfMCmtsEQAMCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 6, 2, 1, 2)
)
if mibBuilder.loadTexts:
    docsIfMCmtsEQAMCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DOCS-IF-M-CMTS-MIB",
    **{"docsIfMCmtsMib": docsIfMCmtsMib,
       "docsIfMCmtsNotifications": docsIfMCmtsNotifications,
       "docsIfMCmtsObjects": docsIfMCmtsObjects,
       "docsIfMCmtsBaseObjects": docsIfMCmtsBaseObjects,
       "docsIfMCmtsBaseAdmin": docsIfMCmtsBaseAdmin,
       "docsPHYParamFixValue": docsPHYParamFixValue,
       "docsPHYParamSameValue": docsPHYParamSameValue,
       "docsPHYParamAdjacentValues": docsPHYParamAdjacentValues,
       "docsPHYParamFrequencyRange": docsPHYParamFrequencyRange,
       "docsIfMCmtsCoreObjects": docsIfMCmtsCoreObjects,
       "docsIfMCmtsCoreDownstreamTable": docsIfMCmtsCoreDownstreamTable,
       "docsIfMCmtsCoreDownstreamEntry": docsIfMCmtsCoreDownstreamEntry,
       "docsIfMCmtsCoreDownstreamType": docsIfMCmtsCoreDownstreamType,
       "docsIfMCmtsCoreDownstreamPhyDependencies": docsIfMCmtsCoreDownstreamPhyDependencies,
       "docsIfMCmtsEqamObjects": docsIfMCmtsEqamObjects,
       "docsIfMCmtsEqamDownstreamTable": docsIfMCmtsEqamDownstreamTable,
       "docsIfMCmtsEqamDownstreamEntry": docsIfMCmtsEqamDownstreamEntry,
       "docsIfMCmtsEqamDownstreamTSID": docsIfMCmtsEqamDownstreamTSID,
       "docsIfMCmtsEqamDownstreamPhyDependencies": docsIfMCmtsEqamDownstreamPhyDependencies,
       "docsIfMCmtsEqamDownstreamDevicePhyParamLock": docsIfMCmtsEqamDownstreamDevicePhyParamLock,
       "docsIfMCmtsEqamDownstreamDeviceConfigPhyParamLock": docsIfMCmtsEqamDownstreamDeviceConfigPhyParamLock,
       "docsIfMCmtsEqamDownstreamAllocationType": docsIfMCmtsEqamDownstreamAllocationType,
       "docsIfMCmtsEqamDownstreamAllocationStatus": docsIfMCmtsEqamDownstreamAllocationStatus,
       "docsIfMCmtsEqamDownstreamAllocationTimeout": docsIfMCmtsEqamDownstreamAllocationTimeout,
       "docsIfMCmtsEqamDownstreamDRRPAdvertizing": docsIfMCmtsEqamDownstreamDRRPAdvertizing,
       "docsIfMCmtsEqamDownstreamUdpPortMapping": docsIfMCmtsEqamDownstreamUdpPortMapping,
       "docsIfMCmtsEqamDownstreamCapabilitiesTable": docsIfMCmtsEqamDownstreamCapabilitiesTable,
       "docsIfMCmtsEqamDownstreamCapabilitiesEntry": docsIfMCmtsEqamDownstreamCapabilitiesEntry,
       "docsIfMCmtsEqamDownstreamCapabFrequency": docsIfMCmtsEqamDownstreamCapabFrequency,
       "docsIfMCmtsEqamDownstreamCapabBandwidth": docsIfMCmtsEqamDownstreamCapabBandwidth,
       "docsIfMCmtsEqamDownstreamCapabPower": docsIfMCmtsEqamDownstreamCapabPower,
       "docsIfMCmtsEqamDownstreamCapabModulation": docsIfMCmtsEqamDownstreamCapabModulation,
       "docsIfMCmtsEqamDownstreamCapabInterleaver": docsIfMCmtsEqamDownstreamCapabInterleaver,
       "docsIfMCmtsEqamDownstreamCapabJ83Annex": docsIfMCmtsEqamDownstreamCapabJ83Annex,
       "docsIfMCmtsEqamDownstreamCapabConcurrentServices": docsIfMCmtsEqamDownstreamCapabConcurrentServices,
       "docsIfMCmtsEqamDownstreamCapabServicesTransport": docsIfMCmtsEqamDownstreamCapabServicesTransport,
       "docsIfMCmtsEqamDownstreamCapabMuting": docsIfMCmtsEqamDownstreamCapabMuting,
       "docsIfMCmtsEqamGroupDependencyTable": docsIfMCmtsEqamGroupDependencyTable,
       "docsIfMCmtsEqamGroupDependencyEntry": docsIfMCmtsEqamGroupDependencyEntry,
       "docsIfMCmtsEqamGroupDependencyPhyParam": docsIfMCmtsEqamGroupDependencyPhyParam,
       "docsIfMCmtsEqamGroupDependencyPhysicalIndex": docsIfMCmtsEqamGroupDependencyPhysicalIndex,
       "docsIfMCmtsEqamGroupDependencyGroupID": docsIfMCmtsEqamGroupDependencyGroupID,
       "docsIfMCmtsEqamGroupDependencyType": docsIfMCmtsEqamGroupDependencyType,
       "docsIfMCmtsEqamGlobCfgDownTable": docsIfMCmtsEqamGlobCfgDownTable,
       "docsIfMCmtsEqamGlobCfgDownEntry": docsIfMCmtsEqamGlobCfgDownEntry,
       "docsIfMCmtsEqamGlobCfgDownIndex": docsIfMCmtsEqamGlobCfgDownIndex,
       "docsIfMCmtsEqamGlobCfgDownPhysicalIndex": docsIfMCmtsEqamGlobCfgDownPhysicalIndex,
       "docsIfMCmtsEqamGlobCfgDownBandwidth": docsIfMCmtsEqamGlobCfgDownBandwidth,
       "docsIfMCmtsEqamGlobCfgDownPower": docsIfMCmtsEqamGlobCfgDownPower,
       "docsIfMCmtsEqamGlobCfgDownModulation": docsIfMCmtsEqamGlobCfgDownModulation,
       "docsIfMCmtsEqamGlobCfgDownInterleave": docsIfMCmtsEqamGlobCfgDownInterleave,
       "docsIfMCmtsEqamGlogCfgDownAnnex": docsIfMCmtsEqamGlogCfgDownAnnex,
       "docsIfMCmtsEqamGlobCfgDownSymbolRateM": docsIfMCmtsEqamGlobCfgDownSymbolRateM,
       "docsIfMCmtsEqamGlobCfgDownSymbolRateN": docsIfMCmtsEqamGlobCfgDownSymbolRateN,
       "docsIfMCmtsEqamGlobCfgDownLockParams": docsIfMCmtsEqamGlobCfgDownLockParams,
       "docsIfMCmtsEqamGlobCfgDownExecutionCode": docsIfMCmtsEqamGlobCfgDownExecutionCode,
       "docsIfMCmtsEqamGlobCfgDownErrorsCount": docsIfMCmtsEqamGlobCfgDownErrorsCount,
       "docsIfMCmtsEqamGlobCfgDownRowStatus": docsIfMCmtsEqamGlobCfgDownRowStatus,
       "docsIfMCmtsChannelBlockTable": docsIfMCmtsChannelBlockTable,
       "docsIfMCmtsChannelBlockEntry": docsIfMCmtsChannelBlockEntry,
       "docsIfMCmtsChannelBlockPhysicalIndex": docsIfMCmtsChannelBlockPhysicalIndex,
       "docsIfMCmtsChannelBlockNumberChannels": docsIfMCmtsChannelBlockNumberChannels,
       "docsIfMCmtsChannelBlockCfgNumberChannels": docsIfMCmtsChannelBlockCfgNumberChannels,
       "docsIfMCmtsChannelBlockMute": docsIfMCmtsChannelBlockMute,
       "docsIfMCmtsChannelBlockTestType": docsIfMCmtsChannelBlockTestType,
       "docsIfMCmtsChannelBlockTestIfIndex": docsIfMCmtsChannelBlockTestIfIndex,
       "docsIfMCmtsDepiObjects": docsIfMCmtsDepiObjects,
       "docsIfMCmtsDepiSessionObjects": docsIfMCmtsDepiSessionObjects,
       "docsIfMCmtsDepiSessionConfigTable": docsIfMCmtsDepiSessionConfigTable,
       "docsIfMCmtsDepiSessionConfigEntry": docsIfMCmtsDepiSessionConfigEntry,
       "docsIfMCmtsDepiSessionConfigIndex": docsIfMCmtsDepiSessionConfigIndex,
       "docsIfMCmtsDepiSessionConfigCableMacIfIndex": docsIfMCmtsDepiSessionConfigCableMacIfIndex,
       "docsIfMCmtsDepiSessionConfigCableMCmtsDownIfIndex": docsIfMCmtsDepiSessionConfigCableMCmtsDownIfIndex,
       "docsIfMCmtsDepiSessionConfigAddrType": docsIfMCmtsDepiSessionConfigAddrType,
       "docsIfMCmtsDepiSessionConfigLocalAddr": docsIfMCmtsDepiSessionConfigLocalAddr,
       "docsIfMCmtsDepiSessionConfigRemoteAddr": docsIfMCmtsDepiSessionConfigRemoteAddr,
       "docsIfMCmtsDepiSessionConfigL2TPv3HeaderType": docsIfMCmtsDepiSessionConfigL2TPv3HeaderType,
       "docsIfMCmtsDepiSessionConfigMethod": docsIfMCmtsDepiSessionConfigMethod,
       "docsIfMCmtsDepiSessionConfigTSID": docsIfMCmtsDepiSessionConfigTSID,
       "docsIfMCmtsDepiSessionConfigDEPIMode": docsIfMCmtsDepiSessionConfigDEPIMode,
       "docsIfMCmtsDepiSessionConfigRsrcAllocReq": docsIfMCmtsDepiSessionConfigRsrcAllocReq,
       "docsIfMCmtsDepiSessionConfigCinPhbIdPolicy": docsIfMCmtsDepiSessionConfigCinPhbIdPolicy,
       "docsIfMCmtsDepiSessionConfigSyncEnabled": docsIfMCmtsDepiSessionConfigSyncEnabled,
       "docsIfMCmtsDepiSessionConfigSyncInterval": docsIfMCmtsDepiSessionConfigSyncInterval,
       "docsIfMCmtsDepiSessionConfigPhyParamsFlag": docsIfMCmtsDepiSessionConfigPhyParamsFlag,
       "docsIfMCmtsDepiSessionConfigChannelFrequency": docsIfMCmtsDepiSessionConfigChannelFrequency,
       "docsIfMCmtsDepiSessionConfigChannelModulation": docsIfMCmtsDepiSessionConfigChannelModulation,
       "docsIfMCmtsDepiSessionConfigChannelInterleave": docsIfMCmtsDepiSessionConfigChannelInterleave,
       "docsIfMCmtsDepiSessionConfigChannelPower": docsIfMCmtsDepiSessionConfigChannelPower,
       "docsIfMCmtsDepiSessionConfigChannelAnnex": docsIfMCmtsDepiSessionConfigChannelAnnex,
       "docsIfMCmtsDepiSessionConfigChannelSymbolRateM": docsIfMCmtsDepiSessionConfigChannelSymbolRateM,
       "docsIfMCmtsDepiSessionConfigChannelSymbolRateN": docsIfMCmtsDepiSessionConfigChannelSymbolRateN,
       "docsIfMCmtsDepiSessionConfigChannelOutputRate": docsIfMCmtsDepiSessionConfigChannelOutputRate,
       "docsIfMCmtsDepiSessionConfigChannelBurstSize": docsIfMCmtsDepiSessionConfigChannelBurstSize,
       "docsIfMCmtsDepiSessionConfigStorage": docsIfMCmtsDepiSessionConfigStorage,
       "docsIfMCmtsDepiSessionConfigRowStatus": docsIfMCmtsDepiSessionConfigRowStatus,
       "docsIfMCmtsDepiSessionConfigChannelId": docsIfMCmtsDepiSessionConfigChannelId,
       "docsIfMCmtsDepiSessionInfoTable": docsIfMCmtsDepiSessionInfoTable,
       "docsIfMCmtsDepiSessionInfoEntry": docsIfMCmtsDepiSessionInfoEntry,
       "docsIfMCmtsDepiSessionInfoCfgIndex": docsIfMCmtsDepiSessionInfoCfgIndex,
       "docsIfMCmtsDepiSessionInfoUdpPort": docsIfMCmtsDepiSessionInfoUdpPort,
       "docsIfMCmtsDepiSessionInfoMaxPayload": docsIfMCmtsDepiSessionInfoMaxPayload,
       "docsIfMCmtsDepiSessionInfoPathPayload": docsIfMCmtsDepiSessionInfoPathPayload,
       "docsIfMCmtsDepiSessionInfoIncludeDOCSISMsgs": docsIfMCmtsDepiSessionInfoIncludeDOCSISMsgs,
       "docsIfMCmtsDepiSessionInfoRsrcAllocResp": docsIfMCmtsDepiSessionInfoRsrcAllocResp,
       "docsIfMCmtsDepiSessionInfoConnCtrlID": docsIfMCmtsDepiSessionInfoConnCtrlID,
       "docsIfMCmtsDepiSessionInfoEQAMSessionID": docsIfMCmtsDepiSessionInfoEQAMSessionID,
       "docsIfMCmtsDepiSessionInfoOwner": docsIfMCmtsDepiSessionInfoOwner,
       "docsIfMCmtsDepiSessionInfoState": docsIfMCmtsDepiSessionInfoState,
       "docsIfMCmtsDepiSessionInfoErrorCode": docsIfMCmtsDepiSessionInfoErrorCode,
       "docsIfMCmtsDepiSessionInfoCreationTime": docsIfMCmtsDepiSessionInfoCreationTime,
       "docsIfMCmtsDepiSessionInfoStorage": docsIfMCmtsDepiSessionInfoStorage,
       "docsIfMCmtsDepiRsrcAllocTable": docsIfMCmtsDepiRsrcAllocTable,
       "docsIfMCmtsDepiRsrcAllocEntry": docsIfMCmtsDepiRsrcAllocEntry,
       "docsIfMCmtsDepiRsrcAllocIndex": docsIfMCmtsDepiRsrcAllocIndex,
       "docsIfMCmtsDepiRsrcAllocSeq": docsIfMCmtsDepiRsrcAllocSeq,
       "docsIfMCmtsDepiRsrcAllocPhbId": docsIfMCmtsDepiRsrcAllocPhbId,
       "docsIfMCmtsDepiRsrcAllocFlowId": docsIfMCmtsDepiRsrcAllocFlowId,
       "docsIfMCmtsDepiRsrcAllocUdpPort": docsIfMCmtsDepiRsrcAllocUdpPort,
       "docsIfMCmtsDepiRsrcAllocPolicyScnTags": docsIfMCmtsDepiRsrcAllocPolicyScnTags,
       "docsIfMCmtsDepiRsrcAllocStorage": docsIfMCmtsDepiRsrcAllocStorage,
       "docsIfMCmtsDepiRsrcAllocRowStatus": docsIfMCmtsDepiRsrcAllocRowStatus,
       "docsIfMCmtsDepiSessionStatsTable": docsIfMCmtsDepiSessionStatsTable,
       "docsIfMCmtsDepiSessionStatsEntry": docsIfMCmtsDepiSessionStatsEntry,
       "docsIfMCmtsDepiSessionInfoOutOfSequencePkts": docsIfMCmtsDepiSessionInfoOutOfSequencePkts,
       "docsIfMCmtsDepiSessionCinLatency": docsIfMCmtsDepiSessionCinLatency,
       "docsIfMCmtsDepiSessionCinLatencyInterval": docsIfMCmtsDepiSessionCinLatencyInterval,
       "docsIfMCmtsDepiSessionCinLatencyThrshld": docsIfMCmtsDepiSessionCinLatencyThrshld,
       "docsIfMCmtsDepiSessionCinEventLevel": docsIfMCmtsDepiSessionCinEventLevel,
       "docsIfMCmtsDepiSessionCinLastValue": docsIfMCmtsDepiSessionCinLastValue,
       "docsIfMCmtsDepiSessionCinLastValueIfIndex": docsIfMCmtsDepiSessionCinLastValueIfIndex,
       "docsIfMCmtsDepiSessionCinLatencyValueLastTime": docsIfMCmtsDepiSessionCinLatencyValueLastTime,
       "docsIfMCmtsDepiSessionCinLatencyPerfTable": docsIfMCmtsDepiSessionCinLatencyPerfTable,
       "docsIfMCmtsDepiSessionCinLatencyPerfEntry": docsIfMCmtsDepiSessionCinLatencyPerfEntry,
       "docsIfMCmtsDepiSessionCinLatencyPerfIntervalSeq": docsIfMCmtsDepiSessionCinLatencyPerfIntervalSeq,
       "docsIfMCmtsDepiSessionCinLatencyPerfValue": docsIfMCmtsDepiSessionCinLatencyPerfValue,
       "docsIfMCmtsDepiSessionCinLatencyTime": docsIfMCmtsDepiSessionCinLatencyTime,
       "docsIfMCmtsDepiQosObjects": docsIfMCmtsDepiQosObjects,
       "docsIfMCmtsDepiPhbPolicyTable": docsIfMCmtsDepiPhbPolicyTable,
       "docsIfMCmtsDepiPhbPolicyEntry": docsIfMCmtsDepiPhbPolicyEntry,
       "docsIfMCmtsDepiPhbPolicyTag": docsIfMCmtsDepiPhbPolicyTag,
       "docsIfMCmtsDepiPhbPolicySCN": docsIfMCmtsDepiPhbPolicySCN,
       "docsIfMCmtsDepiPhbPolicyCinPhbId": docsIfMCmtsDepiPhbPolicyCinPhbId,
       "docsIfMCmtsDepiPhbPolicyStorage": docsIfMCmtsDepiPhbPolicyStorage,
       "docsIfMCmtsDepiPhbPolicyRowStatus": docsIfMCmtsDepiPhbPolicyRowStatus,
       "docsIfMCmtsQosServiceFlowExtTable": docsIfMCmtsQosServiceFlowExtTable,
       "docsIfMCmtsQosServiceFlowExtEntry": docsIfMCmtsQosServiceFlowExtEntry,
       "docsIfMCmtsQosServiceFlowExtDepiFlowId": docsIfMCmtsQosServiceFlowExtDepiFlowId,
       "docsIfMCmtsQosServiceFlowExtCinPhbId": docsIfMCmtsQosServiceFlowExtCinPhbId,
       "docsIfMCmtsQosServiceFlowExtDepiIfIndex": docsIfMCmtsQosServiceFlowExtDepiIfIndex,
       "docsIfMCmtsConformance": docsIfMCmtsConformance,
       "docsIfMCmtsCompliances": docsIfMCmtsCompliances,
       "docsIfMCmtsCoreDeviceCompliance": docsIfMCmtsCoreDeviceCompliance,
       "docsIfMCmtsEQAMCompliance": docsIfMCmtsEQAMCompliance,
       "docsIfMCmtsGroups": docsIfMCmtsGroups,
       "docsIfMCmtsBaseGroup": docsIfMCmtsBaseGroup,
       "docsIfMCmtsCoreGroup": docsIfMCmtsCoreGroup,
       "docsIfMCmtsEqamDevGroup": docsIfMCmtsEqamDevGroup}
)
