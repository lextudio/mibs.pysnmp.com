# SNMP MIB module (SCSPATMARP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/SCSPATMARP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:50:05 2024
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

(AtmAddr,
 AtmConnKind) = mibBuilder.importSymbols(
    "ATM-TC-MIB",
    "AtmAddr",
    "AtmConnKind")

(SCSPVCIInteger,
 SCSPVPIInteger,
 ScspHFSMStateType,
 scspDCSID,
 scspLSID,
 scspServerGroupID,
 scspServerGroupPID) = mibBuilder.importSymbols(
    "SCSP-MIB",
    "SCSPVCIInteger",
    "SCSPVPIInteger",
    "ScspHFSMStateType",
    "scspDCSID",
    "scspLSID",
    "scspServerGroupID",
    "scspServerGroupPID")

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
 experimental,
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
    "experimental",
    "iso")

(DisplayString,
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

scspAtmarpMIB = ModuleIdentity(
    (1, 3, 6, 1, 3, 2002)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ScspAtmarpObjects_ObjectIdentity = ObjectIdentity
scspAtmarpObjects = _ScspAtmarpObjects_ObjectIdentity(
    (1, 3, 6, 1, 3, 2002, 1)
)
_ScspAtmarpServerGroupTable_Object = MibTable
scspAtmarpServerGroupTable = _ScspAtmarpServerGroupTable_Object(
    (1, 3, 6, 1, 3, 2002, 1, 1)
)
if mibBuilder.loadTexts:
    scspAtmarpServerGroupTable.setStatus("current")
_ScspAtmarpServerGroupEntry_Object = MibTableRow
scspAtmarpServerGroupEntry = _ScspAtmarpServerGroupEntry_Object(
    (1, 3, 6, 1, 3, 2002, 1, 1, 1)
)
scspAtmarpServerGroupEntry.setIndexNames(
    (0, "SCSP-MIB", "scspServerGroupID"),
    (0, "SCSP-MIB", "scspServerGroupPID"),
)
if mibBuilder.loadTexts:
    scspAtmarpServerGroupEntry.setStatus("current")
_ScspAtmarpServerGroupNetMask_Type = IpAddress
_ScspAtmarpServerGroupNetMask_Object = MibTableColumn
scspAtmarpServerGroupNetMask = _ScspAtmarpServerGroupNetMask_Object(
    (1, 3, 6, 1, 3, 2002, 1, 1, 1, 1),
    _ScspAtmarpServerGroupNetMask_Type()
)
scspAtmarpServerGroupNetMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scspAtmarpServerGroupNetMask.setStatus("current")
_ScspAtmarpServerGroupSubnetAddr_Type = IpAddress
_ScspAtmarpServerGroupSubnetAddr_Object = MibTableColumn
scspAtmarpServerGroupSubnetAddr = _ScspAtmarpServerGroupSubnetAddr_Object(
    (1, 3, 6, 1, 3, 2002, 1, 1, 1, 2),
    _ScspAtmarpServerGroupSubnetAddr_Type()
)
scspAtmarpServerGroupSubnetAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scspAtmarpServerGroupSubnetAddr.setStatus("current")
_ScspAtmarpServerGroupRowStatus_Type = RowStatus
_ScspAtmarpServerGroupRowStatus_Object = MibTableColumn
scspAtmarpServerGroupRowStatus = _ScspAtmarpServerGroupRowStatus_Object(
    (1, 3, 6, 1, 3, 2002, 1, 1, 1, 3),
    _ScspAtmarpServerGroupRowStatus_Type()
)
scspAtmarpServerGroupRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    scspAtmarpServerGroupRowStatus.setStatus("current")
_ScspAtmarpLSTable_Object = MibTable
scspAtmarpLSTable = _ScspAtmarpLSTable_Object(
    (1, 3, 6, 1, 3, 2002, 1, 2)
)
if mibBuilder.loadTexts:
    scspAtmarpLSTable.setStatus("current")
_ScspAtmarpLSEntry_Object = MibTableRow
scspAtmarpLSEntry = _ScspAtmarpLSEntry_Object(
    (1, 3, 6, 1, 3, 2002, 1, 2, 1)
)
scspAtmarpLSEntry.setIndexNames(
    (0, "SCSP-MIB", "scspServerGroupID"),
    (0, "SCSP-MIB", "scspServerGroupPID"),
    (0, "SCSP-MIB", "scspLSID"),
)
if mibBuilder.loadTexts:
    scspAtmarpLSEntry.setStatus("current")
_ScspAtmarpLSLSIPAddr_Type = IpAddress
_ScspAtmarpLSLSIPAddr_Object = MibTableColumn
scspAtmarpLSLSIPAddr = _ScspAtmarpLSLSIPAddr_Object(
    (1, 3, 6, 1, 3, 2002, 1, 2, 1, 1),
    _ScspAtmarpLSLSIPAddr_Type()
)
scspAtmarpLSLSIPAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scspAtmarpLSLSIPAddr.setStatus("current")
_ScspAtmarpLSLSAtmAddr_Type = AtmAddr
_ScspAtmarpLSLSAtmAddr_Object = MibTableColumn
scspAtmarpLSLSAtmAddr = _ScspAtmarpLSLSAtmAddr_Object(
    (1, 3, 6, 1, 3, 2002, 1, 2, 1, 2),
    _ScspAtmarpLSLSAtmAddr_Type()
)
scspAtmarpLSLSAtmAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scspAtmarpLSLSAtmAddr.setStatus("current")
_ScspAtmarpLSRowStatus_Type = RowStatus
_ScspAtmarpLSRowStatus_Object = MibTableColumn
scspAtmarpLSRowStatus = _ScspAtmarpLSRowStatus_Object(
    (1, 3, 6, 1, 3, 2002, 1, 2, 1, 3),
    _ScspAtmarpLSRowStatus_Type()
)
scspAtmarpLSRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    scspAtmarpLSRowStatus.setStatus("current")
_ScspAtmarpPeerTable_Object = MibTable
scspAtmarpPeerTable = _ScspAtmarpPeerTable_Object(
    (1, 3, 6, 1, 3, 2002, 1, 3)
)
if mibBuilder.loadTexts:
    scspAtmarpPeerTable.setStatus("current")
_ScspAtmarpPeerEntry_Object = MibTableRow
scspAtmarpPeerEntry = _ScspAtmarpPeerEntry_Object(
    (1, 3, 6, 1, 3, 2002, 1, 3, 1)
)
scspAtmarpPeerEntry.setIndexNames(
    (0, "SCSP-MIB", "scspServerGroupID"),
    (0, "SCSP-MIB", "scspServerGroupPID"),
    (0, "SCSPATMARP-MIB", "scspAtmarpPeerIndex"),
)
if mibBuilder.loadTexts:
    scspAtmarpPeerEntry.setStatus("current")
_ScspAtmarpPeerIndex_Type = Integer32
_ScspAtmarpPeerIndex_Object = MibTableColumn
scspAtmarpPeerIndex = _ScspAtmarpPeerIndex_Object(
    (1, 3, 6, 1, 3, 2002, 1, 3, 1, 1),
    _ScspAtmarpPeerIndex_Type()
)
scspAtmarpPeerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scspAtmarpPeerIndex.setStatus("current")
_ScspAtmarpPeerIPAddr_Type = IpAddress
_ScspAtmarpPeerIPAddr_Object = MibTableColumn
scspAtmarpPeerIPAddr = _ScspAtmarpPeerIPAddr_Object(
    (1, 3, 6, 1, 3, 2002, 1, 3, 1, 2),
    _ScspAtmarpPeerIPAddr_Type()
)
scspAtmarpPeerIPAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scspAtmarpPeerIPAddr.setStatus("current")
_ScspAtmarpPeerAtmAddr_Type = AtmAddr
_ScspAtmarpPeerAtmAddr_Object = MibTableColumn
scspAtmarpPeerAtmAddr = _ScspAtmarpPeerAtmAddr_Object(
    (1, 3, 6, 1, 3, 2002, 1, 3, 1, 3),
    _ScspAtmarpPeerAtmAddr_Type()
)
scspAtmarpPeerAtmAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scspAtmarpPeerAtmAddr.setStatus("current")
_ScspAtmarpPeerVCType_Type = AtmConnKind
_ScspAtmarpPeerVCType_Object = MibTableColumn
scspAtmarpPeerVCType = _ScspAtmarpPeerVCType_Object(
    (1, 3, 6, 1, 3, 2002, 1, 3, 1, 4),
    _ScspAtmarpPeerVCType_Type()
)
scspAtmarpPeerVCType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scspAtmarpPeerVCType.setStatus("current")
_ScspAtmarpPeerVPI_Type = SCSPVPIInteger
_ScspAtmarpPeerVPI_Object = MibTableColumn
scspAtmarpPeerVPI = _ScspAtmarpPeerVPI_Object(
    (1, 3, 6, 1, 3, 2002, 1, 3, 1, 5),
    _ScspAtmarpPeerVPI_Type()
)
scspAtmarpPeerVPI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scspAtmarpPeerVPI.setStatus("current")
_ScspAtmarpPeerVCI_Type = SCSPVCIInteger
_ScspAtmarpPeerVCI_Object = MibTableColumn
scspAtmarpPeerVCI = _ScspAtmarpPeerVCI_Object(
    (1, 3, 6, 1, 3, 2002, 1, 3, 1, 6),
    _ScspAtmarpPeerVCI_Type()
)
scspAtmarpPeerVCI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scspAtmarpPeerVCI.setStatus("current")


class _ScspAtmarpPeerDCSID_Type(OctetString):
    """Custom type scspAtmarpPeerDCSID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_ScspAtmarpPeerDCSID_Type.__name__ = "OctetString"
_ScspAtmarpPeerDCSID_Object = MibTableColumn
scspAtmarpPeerDCSID = _ScspAtmarpPeerDCSID_Object(
    (1, 3, 6, 1, 3, 2002, 1, 3, 1, 7),
    _ScspAtmarpPeerDCSID_Type()
)
scspAtmarpPeerDCSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scspAtmarpPeerDCSID.setStatus("current")
_ScspAtmarpPeerRowStatus_Type = RowStatus
_ScspAtmarpPeerRowStatus_Object = MibTableColumn
scspAtmarpPeerRowStatus = _ScspAtmarpPeerRowStatus_Object(
    (1, 3, 6, 1, 3, 2002, 1, 3, 1, 8),
    _ScspAtmarpPeerRowStatus_Type()
)
scspAtmarpPeerRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    scspAtmarpPeerRowStatus.setStatus("current")
_ScspAtmarpHFSMTable_Object = MibTable
scspAtmarpHFSMTable = _ScspAtmarpHFSMTable_Object(
    (1, 3, 6, 1, 3, 2002, 1, 4)
)
if mibBuilder.loadTexts:
    scspAtmarpHFSMTable.setStatus("current")
_ScspAtmarpHFSMEntry_Object = MibTableRow
scspAtmarpHFSMEntry = _ScspAtmarpHFSMEntry_Object(
    (1, 3, 6, 1, 3, 2002, 1, 4, 1)
)
scspAtmarpHFSMEntry.setIndexNames(
    (0, "SCSP-MIB", "scspServerGroupID"),
    (0, "SCSP-MIB", "scspServerGroupPID"),
    (0, "SCSPATMARP-MIB", "scspAtmarpPeerIndex"),
)
if mibBuilder.loadTexts:
    scspAtmarpHFSMEntry.setStatus("current")
_ScspHFSMHFSMState_Type = ScspHFSMStateType
_ScspHFSMHFSMState_Object = MibTableColumn
scspHFSMHFSMState = _ScspHFSMHFSMState_Object(
    (1, 3, 6, 1, 3, 2002, 1, 4, 1, 1),
    _ScspHFSMHFSMState_Type()
)
scspHFSMHFSMState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scspHFSMHFSMState.setStatus("current")
_ScspHFSMHelloIn_Type = Counter32
_ScspHFSMHelloIn_Object = MibTableColumn
scspHFSMHelloIn = _ScspHFSMHelloIn_Object(
    (1, 3, 6, 1, 3, 2002, 1, 4, 1, 2),
    _ScspHFSMHelloIn_Type()
)
scspHFSMHelloIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scspHFSMHelloIn.setStatus("current")
_ScspHFSMHelloOut_Type = Counter32
_ScspHFSMHelloOut_Object = MibTableColumn
scspHFSMHelloOut = _ScspHFSMHelloOut_Object(
    (1, 3, 6, 1, 3, 2002, 1, 4, 1, 3),
    _ScspHFSMHelloOut_Type()
)
scspHFSMHelloOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scspHFSMHelloOut.setStatus("current")
_ScspHFSMHelloInvalidIn_Type = Counter32
_ScspHFSMHelloInvalidIn_Object = MibTableColumn
scspHFSMHelloInvalidIn = _ScspHFSMHelloInvalidIn_Object(
    (1, 3, 6, 1, 3, 2002, 1, 4, 1, 4),
    _ScspHFSMHelloInvalidIn_Type()
)
scspHFSMHelloInvalidIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scspHFSMHelloInvalidIn.setStatus("current")


class _ScspHFSMHelloInterval_Type(Integer32):
    """Custom type scspHFSMHelloInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ScspHFSMHelloInterval_Type.__name__ = "Integer32"
_ScspHFSMHelloInterval_Object = MibTableColumn
scspHFSMHelloInterval = _ScspHFSMHelloInterval_Object(
    (1, 3, 6, 1, 3, 2002, 1, 4, 1, 5),
    _ScspHFSMHelloInterval_Type()
)
scspHFSMHelloInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    scspHFSMHelloInterval.setStatus("current")


class _ScspHFSMDeadFactor_Type(Integer32):
    """Custom type scspHFSMDeadFactor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ScspHFSMDeadFactor_Type.__name__ = "Integer32"
_ScspHFSMDeadFactor_Object = MibTableColumn
scspHFSMDeadFactor = _ScspHFSMDeadFactor_Object(
    (1, 3, 6, 1, 3, 2002, 1, 4, 1, 6),
    _ScspHFSMDeadFactor_Type()
)
scspHFSMDeadFactor.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    scspHFSMDeadFactor.setStatus("current")


class _ScspHFSMFamilyID_Type(Integer32):
    """Custom type scspHFSMFamilyID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ScspHFSMFamilyID_Type.__name__ = "Integer32"
_ScspHFSMFamilyID_Object = MibTableColumn
scspHFSMFamilyID = _ScspHFSMFamilyID_Object(
    (1, 3, 6, 1, 3, 2002, 1, 4, 1, 7),
    _ScspHFSMFamilyID_Type()
)
scspHFSMFamilyID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scspHFSMFamilyID.setStatus("current")
_ScspAtmarpHFSMRowStatus_Type = RowStatus
_ScspAtmarpHFSMRowStatus_Object = MibTableColumn
scspAtmarpHFSMRowStatus = _ScspAtmarpHFSMRowStatus_Object(
    (1, 3, 6, 1, 3, 2002, 1, 4, 1, 8),
    _ScspAtmarpHFSMRowStatus_Type()
)
scspAtmarpHFSMRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    scspAtmarpHFSMRowStatus.setStatus("current")
_ScspAtmarpNotifications_ObjectIdentity = ObjectIdentity
scspAtmarpNotifications = _ScspAtmarpNotifications_ObjectIdentity(
    (1, 3, 6, 1, 3, 2002, 2)
)
_ScspAtmarpConformance_ObjectIdentity = ObjectIdentity
scspAtmarpConformance = _ScspAtmarpConformance_ObjectIdentity(
    (1, 3, 6, 1, 3, 2002, 3)
)
_ScspAtmarpCompliances_ObjectIdentity = ObjectIdentity
scspAtmarpCompliances = _ScspAtmarpCompliances_ObjectIdentity(
    (1, 3, 6, 1, 3, 2002, 3, 1)
)
_ScspAtmarpGroups_ObjectIdentity = ObjectIdentity
scspAtmarpGroups = _ScspAtmarpGroups_ObjectIdentity(
    (1, 3, 6, 1, 3, 2002, 3, 2)
)

# Managed Objects groups

scspAtmarpGroup = ObjectGroup(
    (1, 3, 6, 1, 3, 2002, 3, 2, 1)
)
scspAtmarpGroup.setObjects(
      *(("SCSPATMARP-MIB", "scspAtmarpServerGroupNetMask"),
        ("SCSPATMARP-MIB", "scspAtmarpServerGroupSubnetAddr"),
        ("SCSPATMARP-MIB", "scspAtmarpLSLSIPAddr"),
        ("SCSPATMARP-MIB", "scspAtmarpLSLSAtmAddr"),
        ("SCSPATMARP-MIB", "scspAtmarpPeerIndex"),
        ("SCSPATMARP-MIB", "scspAtmarpPeerAtmAddr"),
        ("SCSPATMARP-MIB", "scspAtmarpPeerVCType"),
        ("SCSPATMARP-MIB", "scspAtmarpPeerVPI"),
        ("SCSPATMARP-MIB", "scspAtmarpPeerVCI"),
        ("SCSPATMARP-MIB", "scspAtmarpPeerDCSID"),
        ("SCSPATMARP-MIB", "scspHFSMHFSMState"),
        ("SCSPATMARP-MIB", "scspHFSMHelloIn"),
        ("SCSPATMARP-MIB", "scspHFSMHelloOut"),
        ("SCSPATMARP-MIB", "scspHFSMHelloInvalidIn"),
        ("SCSPATMARP-MIB", "scspHFSMHelloInterval"),
        ("SCSPATMARP-MIB", "scspHFSMDeadFactor"),
        ("SCSPATMARP-MIB", "scspHFSMFamilyID"))
)
if mibBuilder.loadTexts:
    scspAtmarpGroup.setStatus("current")


# Notification objects

scspHFSMDown = NotificationType(
    (1, 3, 6, 1, 3, 2002, 2, 1)
)
scspHFSMDown.setObjects(
      *(("SCSP-MIB", "scspServerGroupID"),
        ("SCSP-MIB", "scspServerGroupPID"),
        ("SCSPATMARP-MIB", "scspAtmarpPeerIndex"))
)
if mibBuilder.loadTexts:
    scspHFSMDown.setStatus(
        "current"
    )

scspHFSMWaiting = NotificationType(
    (1, 3, 6, 1, 3, 2002, 2, 2)
)
scspHFSMWaiting.setObjects(
      *(("SCSP-MIB", "scspServerGroupID"),
        ("SCSP-MIB", "scspServerGroupPID"),
        ("SCSPATMARP-MIB", "scspAtmarpPeerIndex"))
)
if mibBuilder.loadTexts:
    scspHFSMWaiting.setStatus(
        "current"
    )

scspHFSMBiConn = NotificationType(
    (1, 3, 6, 1, 3, 2002, 2, 3)
)
scspHFSMBiConn.setObjects(
      *(("SCSP-MIB", "scspServerGroupID"),
        ("SCSP-MIB", "scspServerGroupPID"),
        ("SCSPATMARP-MIB", "scspAtmarpPeerIndex"))
)
if mibBuilder.loadTexts:
    scspHFSMBiConn.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance

scspAtmarpCompliance = ModuleCompliance(
    (1, 3, 6, 1, 3, 2002, 3, 1, 1)
)
if mibBuilder.loadTexts:
    scspAtmarpCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SCSPATMARP-MIB",
    **{"scspAtmarpMIB": scspAtmarpMIB,
       "scspAtmarpObjects": scspAtmarpObjects,
       "scspAtmarpServerGroupTable": scspAtmarpServerGroupTable,
       "scspAtmarpServerGroupEntry": scspAtmarpServerGroupEntry,
       "scspAtmarpServerGroupNetMask": scspAtmarpServerGroupNetMask,
       "scspAtmarpServerGroupSubnetAddr": scspAtmarpServerGroupSubnetAddr,
       "scspAtmarpServerGroupRowStatus": scspAtmarpServerGroupRowStatus,
       "scspAtmarpLSTable": scspAtmarpLSTable,
       "scspAtmarpLSEntry": scspAtmarpLSEntry,
       "scspAtmarpLSLSIPAddr": scspAtmarpLSLSIPAddr,
       "scspAtmarpLSLSAtmAddr": scspAtmarpLSLSAtmAddr,
       "scspAtmarpLSRowStatus": scspAtmarpLSRowStatus,
       "scspAtmarpPeerTable": scspAtmarpPeerTable,
       "scspAtmarpPeerEntry": scspAtmarpPeerEntry,
       "scspAtmarpPeerIndex": scspAtmarpPeerIndex,
       "scspAtmarpPeerIPAddr": scspAtmarpPeerIPAddr,
       "scspAtmarpPeerAtmAddr": scspAtmarpPeerAtmAddr,
       "scspAtmarpPeerVCType": scspAtmarpPeerVCType,
       "scspAtmarpPeerVPI": scspAtmarpPeerVPI,
       "scspAtmarpPeerVCI": scspAtmarpPeerVCI,
       "scspAtmarpPeerDCSID": scspAtmarpPeerDCSID,
       "scspAtmarpPeerRowStatus": scspAtmarpPeerRowStatus,
       "scspAtmarpHFSMTable": scspAtmarpHFSMTable,
       "scspAtmarpHFSMEntry": scspAtmarpHFSMEntry,
       "scspHFSMHFSMState": scspHFSMHFSMState,
       "scspHFSMHelloIn": scspHFSMHelloIn,
       "scspHFSMHelloOut": scspHFSMHelloOut,
       "scspHFSMHelloInvalidIn": scspHFSMHelloInvalidIn,
       "scspHFSMHelloInterval": scspHFSMHelloInterval,
       "scspHFSMDeadFactor": scspHFSMDeadFactor,
       "scspHFSMFamilyID": scspHFSMFamilyID,
       "scspAtmarpHFSMRowStatus": scspAtmarpHFSMRowStatus,
       "scspAtmarpNotifications": scspAtmarpNotifications,
       "scspHFSMDown": scspHFSMDown,
       "scspHFSMWaiting": scspHFSMWaiting,
       "scspHFSMBiConn": scspHFSMBiConn,
       "scspAtmarpConformance": scspAtmarpConformance,
       "scspAtmarpCompliances": scspAtmarpCompliances,
       "scspAtmarpCompliance": scspAtmarpCompliance,
       "scspAtmarpGroups": scspAtmarpGroups,
       "scspAtmarpGroup": scspAtmarpGroup}
)
