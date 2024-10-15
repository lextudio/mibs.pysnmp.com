# SNMP MIB module (STEELHEAD-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/STEELHEAD-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:57:59 2024
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

(products,) = mibBuilder.importSymbols(
    "RBT-MIB",
    "products")

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

(DateAndTime,
 DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

steelhead = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 17163, 1, 1)
)
steelhead.setRevisions(
        ("2014-01-07 00:00",
         "2013-01-25 00:00",
         "2012-10-17 00:00",
         "2012-02-03 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_System_ObjectIdentity = ObjectIdentity
system = _System_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17163, 1, 1, 1)
)
_Model_Type = OctetString
_Model_Object = MibScalar
model = _Model_Object(
    (1, 3, 6, 1, 4, 1, 17163, 1, 1, 1, 1),
    _Model_Type()
)
model.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    model.setStatus("current")
_SerialNumber_Type = OctetString
_SerialNumber_Object = MibScalar
serialNumber = _SerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 17163, 1, 1, 1, 2),
    _SerialNumber_Type()
)
serialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serialNumber.setStatus("current")
_SystemVersion_Type = OctetString
_SystemVersion_Object = MibScalar
systemVersion = _SystemVersion_Object(
    (1, 3, 6, 1, 4, 1, 17163, 1, 1, 1, 3),
    _SystemVersion_Type()
)
systemVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemVersion.setStatus("current")
_Status_ObjectIdentity = ObjectIdentity
status = _Status_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17163, 1, 1, 2)
)
_SystemClock_Type = DateAndTime
_SystemClock_Object = MibScalar
systemClock = _SystemClock_Object(
    (1, 3, 6, 1, 4, 1, 17163, 1, 1, 2, 1),
    _SystemClock_Type()
)
systemClock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemClock.setStatus("current")
_Health_Type = OctetString
_Health_Object = MibScalar
health = _Health_Object(
    (1, 3, 6, 1, 4, 1, 17163, 1, 1, 2, 2),
    _Health_Type()
)
health.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    health.setStatus("current")
_ServiceStatus_Type = OctetString
_ServiceStatus_Object = MibScalar
serviceStatus = _ServiceStatus_Object(
    (1, 3, 6, 1, 4, 1, 17163, 1, 1, 2, 3),
    _ServiceStatus_Type()
)
serviceStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serviceStatus.setStatus("current")
_ServiceUptime_Type = TimeTicks
_ServiceUptime_Object = MibScalar
serviceUptime = _ServiceUptime_Object(
    (1, 3, 6, 1, 4, 1, 17163, 1, 1, 2, 4),
    _ServiceUptime_Type()
)
serviceUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serviceUptime.setStatus("current")
_ProcTable_Object = MibTable
procTable = _ProcTable_Object(
    (1, 3, 6, 1, 4, 1, 17163, 1, 1, 2, 5)
)
if mibBuilder.loadTexts:
    procTable.setStatus("current")
_ProcEntry_Object = MibTableRow
procEntry = _ProcEntry_Object(
    (1, 3, 6, 1, 4, 1, 17163, 1, 1, 2, 5, 1)
)
procEntry.setIndexNames(
    (0, "STEELHEAD-MIB", "procIndex"),
)
if mibBuilder.loadTexts:
    procEntry.setStatus("current")
_ProcIndex_Type = Unsigned32
_ProcIndex_Object = MibTableColumn
procIndex = _ProcIndex_Object(
    (1, 3, 6, 1, 4, 1, 17163, 1, 1, 2, 5, 1, 1),
    _ProcIndex_Type()
)
procIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    procIndex.setStatus("current")
_ProcName_Type = OctetString
_ProcName_Object = MibTableColumn
procName = _ProcName_Object(
    (1, 3, 6, 1, 4, 1, 17163, 1, 1, 2, 5, 1, 2),
    _ProcName_Type()
)
procName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    procName.setStatus("current")
_ProcStatus_Type = OctetString
_ProcStatus_Object = MibTableColumn
procStatus = _ProcStatus_Object(
    (1, 3, 6, 1, 4, 1, 17163, 1, 1, 2, 5, 1, 3),
    _ProcStatus_Type()
)
procStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    procStatus.setStatus("current")
_ProcNumFailures_Type = Unsigned32
_ProcNumFailures_Object = MibTableColumn
procNumFailures = _ProcNumFailures_Object(
    (1, 3, 6, 1, 4, 1, 17163, 1, 1, 2, 5, 1, 4),
    _ProcNumFailures_Type()
)
procNumFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    procNumFailures.setStatus("current")
_PeerStatus_ObjectIdentity = ObjectIdentity
peerStatus = _PeerStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17163, 1, 1, 2, 6)
)
_PeerTable_Object = MibTable
peerTable = _PeerTable_Object(
    (1, 3, 6, 1, 4, 1, 17163, 1, 1, 2, 6, 1)
)
if mibBuilder.loadTexts:
    peerTable.setStatus("current")
_PeerEntry_Object = MibTableRow
peerEntry = _PeerEntry_Object(
    (1, 3, 6, 1, 4, 1, 17163, 1, 1, 2, 6, 1, 1)
)
peerEntry.setIndexNames(
    (0, "STEELHEAD-MIB", "peerIndex"),
)
if mibBuilder.loadTexts:
    peerEntry.setStatus("current")
_PeerIndex_Type = Unsigned32
_PeerIndex_Object = MibTableColumn
peerIndex = _PeerIndex_Object(
    (1, 3, 6, 1, 4, 1, 17163, 1, 1, 2, 6, 1, 1, 1),
    _PeerIndex_Type()
)
peerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    peerIndex.setStatus("current")
_PeerHostname_Type = OctetString
_PeerHostname_Object = MibTableColumn
peerHostname = _PeerHostname_Object(
    (1, 3, 6, 1, 4, 1, 17163, 1, 1, 2, 6, 1, 1, 2),
    _PeerHostname_Type()
)
peerHostname.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    peerHostname.setStatus("current")
_PeerVersion_Type = OctetString
_PeerVersion_Object = MibTableColumn
peerVersion = _PeerVersion_Object(
    (1, 3, 6, 1, 4, 1, 17163, 1, 1, 2, 6, 1, 1, 3),
    _PeerVersion_Type()
)
peerVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    peerVersion.setStatus("current")
_PeerAddress_Type = IpAddress
_PeerAddress_Object = MibTableColumn
peerAddress = _PeerAddress_Object(
    (1, 3, 6, 1, 4, 1, 17163, 1, 1, 2, 6, 1, 1, 4),
    _PeerAddress_Type()
)
peerAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    peerAddress.setStatus("current")
_PeerModel_Type = OctetString
_PeerModel_Object = MibTableColumn
peerModel = _PeerModel_Object(
    (1, 3, 6, 1, 4, 1, 17163, 1, 1, 2, 6, 1, 1, 5),
    _PeerModel_Type()
)
peerModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    peerModel.setStatus("current")


class _SystemHealth_Type(Integer32):
    """Custom type systemHealth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(10000,
              30000,
              31000,
              50000)
        )
    )
    namedValues = NamedValues(
        *(("admissionControl", 31000),
          ("critical", 50000),
          ("degraded", 30000),
          ("healthy", 10000))
    )


_SystemHealth_Type.__name__ = "Integer32"
_SystemHealth_Object = MibScalar
systemHealth = _SystemHealth_Object(
    (1, 3, 6, 1, 4, 1, 17163, 1, 1, 2, 7),
    _SystemHealth_Type()
)
systemHealth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemHealth.setStatus("current")


class _OptServiceStatus_Type(Integer32):
    """Custom type optServiceStatus based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("pending", 7),
          ("running", 2),
          ("sentCom1", 3),
          ("sentTerm1", 4),
          ("sentTerm2", 5),
          ("sentTerm3", 6),
          ("stopped", 8),
          ("unmanaged", 1))
    )


_OptServiceStatus_Type.__name__ = "Integer32"
_OptServiceStatus_Object = MibScalar
optServiceStatus = _OptServiceStatus_Object(
    (1, 3, 6, 1, 4, 1, 17163, 1, 1, 2, 8),
    _OptServiceStatus_Type()
)
optServiceStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    optServiceStatus.setStatus("current")
_SystemTemperature_Type = Unsigned32
_SystemTemperature_Object = MibScalar
systemTemperature = _SystemTemperature_Object(
    (1, 3, 6, 1, 4, 1, 17163, 1, 1, 2, 9),
    _SystemTemperature_Type()
)
systemTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemTemperature.setStatus("current")
_HealthNotes_Type = OctetString
_HealthNotes_Object = MibScalar
healthNotes = _HealthNotes_Object(
    (1, 3, 6, 1, 4, 1, 17163, 1, 1, 2, 10),
    _HealthNotes_Type()
)
healthNotes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    healthNotes.setStatus("current")
_CrlStatus_ObjectIdentity = ObjectIdentity
crlStatus = _CrlStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17163, 1, 1, 2, 11)
)
_CrlTable_Object = MibTable
crlTable = _CrlTable_Object(
    (1, 3, 6, 1, 4, 1, 17163, 1, 1, 2, 11, 1)
)
if mibBuilder.loadTexts:
    crlTable.setStatus("current")
_CrlEntry_Object = MibTableRow
crlEntry = _CrlEntry_Object(
    (1, 3, 6, 1, 4, 1, 17163, 1, 1, 2, 11, 1, 1)
)
crlEntry.setIndexNames(
    (0, "STEELHEAD-MIB", "crlIndex"),
)
if mibBuilder.loadTexts:
    crlEntry.setStatus("current")
_CrlIndex_Type = Unsigned32
_CrlIndex_Object = MibTableColumn
crlIndex = _CrlIndex_Object(
    (1, 3, 6, 1, 4, 1, 17163, 1, 1, 2, 11, 1, 1, 1),
    _CrlIndex_Type()
)
crlIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    crlIndex.setStatus("current")
_CrlFeatureName_Type = OctetString
_CrlFeatureName_Object = MibTableColumn
crlFeatureName = _CrlFeatureName_Object(
    (1, 3, 6, 1, 4, 1, 17163, 1, 1, 2, 11, 1, 1, 2),
    _CrlFeatureName_Type()
)
crlFeatureName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crlFeatureName.setStatus("current")
_CrlNumCdpErr_Type = Unsigned32
_CrlNumCdpErr_Object = MibTableColumn
crlNumCdpErr = _CrlNumCdpErr_Object(
    (1, 3, 6, 1, 4, 1, 17163, 1, 1, 2, 11, 1, 1, 3),
    _CrlNumCdpErr_Type()
)
crlNumCdpErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crlNumCdpErr.setStatus("current")
_CrlErrMsg_Type = OctetString
_CrlErrMsg_Object = MibTableColumn
crlErrMsg = _CrlErrMsg_Object(
    (1, 3, 6, 1, 4, 1, 17163, 1, 1, 2, 11, 1, 1, 4),
    _CrlErrMsg_Type()
)
crlErrMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crlErrMsg.setStatus("current")
_NeighborStatus_ObjectIdentity = ObjectIdentity
neighborStatus = _NeighborStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17163, 1, 1, 2, 12)
)
_NeighborTable_Object = MibTable
neighborTable = _NeighborTable_Object(
    (1, 3, 6, 1, 4, 1, 17163, 1, 1, 2, 12, 1)
)
if mibBuilder.loadTexts:
    neighborTable.setStatus("current")
_NeighborEntry_Object = MibTableRow
neighborEntry = _NeighborEntry_Object(
    (1, 3, 6, 1, 4, 1, 17163, 1, 1, 2, 12, 1, 1)
)
neighborEntry.setIndexNames(
    (0, "STEELHEAD-MIB", "neighborIndex"),
)
if mibBuilder.loadTexts:
    neighborEntry.setStatus("current")
_NeighborIndex_Type = Unsigned32
_NeighborIndex_Object = MibTableColumn
neighborIndex = _NeighborIndex_Object(
    (1, 3, 6, 1, 4, 1, 17163, 1, 1, 2, 12, 1, 1, 1),
    _NeighborIndex_Type()
)
neighborIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    neighborIndex.setStatus("current")
_NeighborAddress_Type = IpAddress
_NeighborAddress_Object = MibTableColumn
neighborAddress = _NeighborAddress_Object(
    (1, 3, 6, 1, 4, 1, 17163, 1, 1, 2, 12, 1, 1, 2),
    _NeighborAddress_Type()
)
neighborAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    neighborAddress.setStatus("current")
_NeighborState_Type = Unsigned32
_NeighborState_Object = MibTableColumn
neighborState = _NeighborState_Object(
    (1, 3, 6, 1, 4, 1, 17163, 1, 1, 2, 12, 1, 1, 3),
    _NeighborState_Type()
)
neighborState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    neighborState.setStatus("current")
_NeighborNatReqSent_Type = Counter32
_NeighborNatReqSent_Object = MibTableColumn
neighborNatReqSent = _NeighborNatReqSent_Object(
    (1, 3, 6, 1, 4, 1, 17163, 1, 1, 2, 12, 1, 1, 4),
    _NeighborNatReqSent_Type()
)
neighborNatReqSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    neighborNatReqSent.setStatus("current")
_NeighborNatDelSent_Type = Counter32
_NeighborNatDelSent_Object = MibTableColumn
neighborNatDelSent = _NeighborNatDelSent_Object(
    (1, 3, 6, 1, 4, 1, 17163, 1, 1, 2, 12, 1, 1, 5),
    _NeighborNatDelSent_Type()
)
neighborNatDelSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    neighborNatDelSent.setStatus("current")
_NeighborNatAckRcvd_Type = Counter32
_NeighborNatAckRcvd_Object = MibTableColumn
neighborNatAckRcvd = _NeighborNatAckRcvd_Object(
    (1, 3, 6, 1, 4, 1, 17163, 1, 1, 2, 12, 1, 1, 6),
    _NeighborNatAckRcvd_Type()
)
neighborNatAckRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    neighborNatAckRcvd.setStatus("current")
_NeighborNatReqRcvd_Type = Counter32
_NeighborNatReqRcvd_Object = MibTableColumn
neighborNatReqRcvd = _NeighborNatReqRcvd_Object(
    (1, 3, 6, 1, 4, 1, 17163, 1, 1, 2, 12, 1, 1, 7),
    _NeighborNatReqRcvd_Type()
)
neighborNatReqRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    neighborNatReqRcvd.setStatus("current")
_NeighborNatDelRcvd_Type = Counter32
_NeighborNatDelRcvd_Object = MibTableColumn
neighborNatDelRcvd = _NeighborNatDelRcvd_Object(
    (1, 3, 6, 1, 4, 1, 17163, 1, 1, 2, 12, 1, 1, 8),
    _NeighborNatDelRcvd_Type()
)
neighborNatDelRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    neighborNatDelRcvd.setStatus("current")
_NeighborNatAckSent_Type = Counter32
_NeighborNatAckSent_Object = MibTableColumn
neighborNatAckSent = _NeighborNatAckSent_Object(
    (1, 3, 6, 1, 4, 1, 17163, 1, 1, 2, 12, 1, 1, 9),
    _NeighborNatAckSent_Type()
)
neighborNatAckSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    neighborNatAckSent.setStatus("current")
_NeighborDynReqSent_Type = Counter32
_NeighborDynReqSent_Object = MibTableColumn
neighborDynReqSent = _NeighborDynReqSent_Object(
    (1, 3, 6, 1, 4, 1, 17163, 1, 1, 2, 12, 1, 1, 10),
    _NeighborDynReqSent_Type()
)
neighborDynReqSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    neighborDynReqSent.setStatus("current")
_NeighborDynDelSent_Type = Counter32
_NeighborDynDelSent_Object = MibTableColumn
neighborDynDelSent = _NeighborDynDelSent_Object(
    (1, 3, 6, 1, 4, 1, 17163, 1, 1, 2, 12, 1, 1, 11),
    _NeighborDynDelSent_Type()
)
neighborDynDelSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    neighborDynDelSent.setStatus("current")
_NeighborDynAckRcvd_Type = Counter32
_NeighborDynAckRcvd_Object = MibTableColumn
neighborDynAckRcvd = _NeighborDynAckRcvd_Object(
    (1, 3, 6, 1, 4, 1, 17163, 1, 1, 2, 12, 1, 1, 12),
    _NeighborDynAckRcvd_Type()
)
neighborDynAckRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    neighborDynAckRcvd.setStatus("current")
_NeighborDynReqRcvd_Type = Counter32
_NeighborDynReqRcvd_Object = MibTableColumn
neighborDynReqRcvd = _NeighborDynReqRcvd_Object(
    (1, 3, 6, 1, 4, 1, 17163, 1, 1, 2, 12, 1, 1, 13),
    _NeighborDynReqRcvd_Type()
)
neighborDynReqRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    neighborDynReqRcvd.setStatus("current")
_NeighborDynDelRcvd_Type = Counter32
_NeighborDynDelRcvd_Object = MibTableColumn
neighborDynDelRcvd = _NeighborDynDelRcvd_Object(
    (1, 3, 6, 1, 4, 1, 17163, 1, 1, 2, 12, 1, 1, 14),
    _NeighborDynDelRcvd_Type()
)
neighborDynDelRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    neighborDynDelRcvd.setStatus("current")
_NeighborDynAckSent_Type = Counter32
_NeighborDynAckSent_Object = MibTableColumn
neighborDynAckSent = _NeighborDynAckSent_Object(
    (1, 3, 6, 1, 4, 1, 17163, 1, 1, 2, 12, 1, 1, 15),
    _NeighborDynAckSent_Type()
)
neighborDynAckSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    neighborDynAckSent.setStatus("current")
_NeighborRedirReqSent_Type = Counter32
_NeighborRedirReqSent_Object = MibTableColumn
neighborRedirReqSent = _NeighborRedirReqSent_Object(
    (1, 3, 6, 1, 4, 1, 17163, 1, 1, 2, 12, 1, 1, 16),
    _NeighborRedirReqSent_Type()
)
neighborRedirReqSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    neighborRedirReqSent.setStatus("current")
_NeighborRedirDelSent_Type = Counter32
_NeighborRedirDelSent_Object = MibTableColumn
neighborRedirDelSent = _NeighborRedirDelSent_Object(
    (1, 3, 6, 1, 4, 1, 17163, 1, 1, 2, 12, 1, 1, 17),
    _NeighborRedirDelSent_Type()
)
neighborRedirDelSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    neighborRedirDelSent.setStatus("current")
_NeighborRedirAckRcvd_Type = Counter32
_NeighborRedirAckRcvd_Object = MibTableColumn
neighborRedirAckRcvd = _NeighborRedirAckRcvd_Object(
    (1, 3, 6, 1, 4, 1, 17163, 1, 1, 2, 12, 1, 1, 18),
    _NeighborRedirAckRcvd_Type()
)
neighborRedirAckRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    neighborRedirAckRcvd.setStatus("current")
_NeighborRedirReqRcvd_Type = Counter32
_NeighborRedirReqRcvd_Object = MibTableColumn
neighborRedirReqRcvd = _NeighborRedirReqRcvd_Object(
    (1, 3, 6, 1, 4, 1, 17163, 1, 1, 2, 12, 1, 1, 19),
    _NeighborRedirReqRcvd_Type()
)
neighborRedirReqRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    neighborRedirReqRcvd.setStatus("current")
_NeighborRedirDelRcvd_Type = Counter32
_NeighborRedirDelRcvd_Object = MibTableColumn
neighborRedirDelRcvd = _NeighborRedirDelRcvd_Object(
    (1, 3, 6, 1, 4, 1, 17163, 1, 1, 2, 12, 1, 1, 20),
    _NeighborRedirDelRcvd_Type()
)
neighborRedirDelRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    neighborRedirDelRcvd.setStatus("current")
_NeighborRedirAckSent_Type = Counter32
_NeighborRedirAckSent_Object = MibTableColumn
neighborRedirAckSent = _NeighborRedirAckSent_Object(
    (1, 3, 6, 1, 4, 1, 17163, 1, 1, 2, 12, 1, 1, 21),
    _NeighborRedirAckSent_Type()
)
neighborRedirAckSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    neighborRedirAckSent.setStatus("current")
_NeighborConnFailures_Type = Counter32
_NeighborConnFailures_Object = MibTableColumn
neighborConnFailures = _NeighborConnFailures_Object(
    (1, 3, 6, 1, 4, 1, 17163, 1, 1, 2, 12, 1, 1, 22),
    _NeighborConnFailures_Type()
)
neighborConnFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    neighborConnFailures.setStatus("current")
_NeighborKeepaliveTimeouts_Type = Counter32
_NeighborKeepaliveTimeouts_Object = MibTableColumn
neighborKeepaliveTimeouts = _NeighborKeepaliveTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 17163, 1, 1, 2, 12, 1, 1, 23),
    _NeighborKeepaliveTimeouts_Type()
)
neighborKeepaliveTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    neighborKeepaliveTimeouts.setStatus("current")
_NeighborRequestTimeouts_Type = Counter32
_NeighborRequestTimeouts_Object = MibTableColumn
neighborRequestTimeouts = _NeighborRequestTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 17163, 1, 1, 2, 12, 1, 1, 24),
    _NeighborRequestTimeouts_Type()
)
neighborRequestTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    neighborRequestTimeouts.setStatus("current")
_NeighborMaxLatency_Type = Unsigned32
_NeighborMaxLatency_Object = MibTableColumn
neighborMaxLatency = _NeighborMaxLatency_Object(
    (1, 3, 6, 1, 4, 1, 17163, 1, 1, 2, 12, 1, 1, 25),
    _NeighborMaxLatency_Type()
)
neighborMaxLatency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    neighborMaxLatency.setStatus("current")
_NeighborAggregates_ObjectIdentity = ObjectIdentity
neighborAggregates = _NeighborAggregates_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17163, 1, 1, 2, 12, 2)
)
_NghAggrConfigured_Type = Unsigned32
_NghAggrConfigured_Object = MibScalar
nghAggrConfigured = _NghAggrConfigured_Object(
    (1, 3, 6, 1, 4, 1, 17163, 1, 1, 2, 12, 2, 1),
    _NghAggrConfigured_Type()
)
nghAggrConfigured.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nghAggrConfigured.setStatus("current")
_NghAggrConnected_Type = Unsigned32
_NghAggrConnected_Object = MibScalar
nghAggrConnected = _NghAggrConnected_Object(
    (1, 3, 6, 1, 4, 1, 17163, 1, 1, 2, 12, 2, 2),
    _NghAggrConnected_Type()
)
nghAggrConnected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nghAggrConnected.setStatus("current")
_NghAggrConnFailures_Type = Counter32
_NghAggrConnFailures_Object = MibScalar
nghAggrConnFailures = _NghAggrConnFailures_Object(
    (1, 3, 6, 1, 4, 1, 17163, 1, 1, 2, 12, 2, 3),
    _NghAggrConnFailures_Type()
)
nghAggrConnFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nghAggrConnFailures.setStatus("current")
_NghAggrKeepaliveTimouts_Type = Counter32
_NghAggrKeepaliveTimouts_Object = MibScalar
nghAggrKeepaliveTimouts = _NghAggrKeepaliveTimouts_Object(
    (1, 3, 6, 1, 4, 1, 17163, 1, 1, 2, 12, 2, 4),
    _NghAggrKeepaliveTimouts_Type()
)
nghAggrKeepaliveTimouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nghAggrKeepaliveTimouts.setStatus("current")
_NghAggrRequestTimeouts_Type = Counter32
_NghAggrRequestTimeouts_Object = MibScalar
nghAggrRequestTimeouts = _NghAggrRequestTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 17163, 1, 1, 2, 12, 2, 5),
    _NghAggrRequestTimeouts_Type()
)
nghAggrRequestTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nghAggrRequestTimeouts.setStatus("current")
_NghAggrMaxLatency_Type = Unsigned32
_NghAggrMaxLatency_Object = MibScalar
nghAggrMaxLatency = _NghAggrMaxLatency_Object(
    (1, 3, 6, 1, 4, 1, 17163, 1, 1, 2, 12, 2, 6),
    _NghAggrMaxLatency_Type()
)
nghAggrMaxLatency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nghAggrMaxLatency.setStatus("current")
_NghAggrNatReqSent_Type = Counter32
_NghAggrNatReqSent_Object = MibScalar
nghAggrNatReqSent = _NghAggrNatReqSent_Object(
    (1, 3, 6, 1, 4, 1, 17163, 1, 1, 2, 12, 2, 7),
    _NghAggrNatReqSent_Type()
)
nghAggrNatReqSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nghAggrNatReqSent.setStatus("current")
_NghAggrNatDelSent_Type = Counter32
_NghAggrNatDelSent_Object = MibScalar
nghAggrNatDelSent = _NghAggrNatDelSent_Object(
    (1, 3, 6, 1, 4, 1, 17163, 1, 1, 2, 12, 2, 8),
    _NghAggrNatDelSent_Type()
)
nghAggrNatDelSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nghAggrNatDelSent.setStatus("current")
_NghAggrNatAckRcvd_Type = Counter32
_NghAggrNatAckRcvd_Object = MibScalar
nghAggrNatAckRcvd = _NghAggrNatAckRcvd_Object(
    (1, 3, 6, 1, 4, 1, 17163, 1, 1, 2, 12, 2, 9),
    _NghAggrNatAckRcvd_Type()
)
nghAggrNatAckRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nghAggrNatAckRcvd.setStatus("current")
_NghAggrNatReqRcvd_Type = Counter32
_NghAggrNatReqRcvd_Object = MibScalar
nghAggrNatReqRcvd = _NghAggrNatReqRcvd_Object(
    (1, 3, 6, 1, 4, 1, 17163, 1, 1, 2, 12, 2, 10),
    _NghAggrNatReqRcvd_Type()
)
nghAggrNatReqRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nghAggrNatReqRcvd.setStatus("current")
_NghAggrNatDelRcvd_Type = Counter32
_NghAggrNatDelRcvd_Object = MibScalar
nghAggrNatDelRcvd = _NghAggrNatDelRcvd_Object(
    (1, 3, 6, 1, 4, 1, 17163, 1, 1, 2, 12, 2, 11),
    _NghAggrNatDelRcvd_Type()
)
nghAggrNatDelRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nghAggrNatDelRcvd.setStatus("current")
_NghAggrNatAckSent_Type = Counter32
_NghAggrNatAckSent_Object = MibScalar
nghAggrNatAckSent = _NghAggrNatAckSent_Object(
    (1, 3, 6, 1, 4, 1, 17163, 1, 1, 2, 12, 2, 12),
    _NghAggrNatAckSent_Type()
)
nghAggrNatAckSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nghAggrNatAckSent.setStatus("current")
_NghAggrDynReqSent_Type = Counter32
_NghAggrDynReqSent_Object = MibScalar
nghAggrDynReqSent = _NghAggrDynReqSent_Object(
    (1, 3, 6, 1, 4, 1, 17163, 1, 1, 2, 12, 2, 13),
    _NghAggrDynReqSent_Type()
)
nghAggrDynReqSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nghAggrDynReqSent.setStatus("current")
_NghAggrDynDelSent_Type = Counter32
_NghAggrDynDelSent_Object = MibScalar
nghAggrDynDelSent = _NghAggrDynDelSent_Object(
    (1, 3, 6, 1, 4, 1, 17163, 1, 1, 2, 12, 2, 14),
    _NghAggrDynDelSent_Type()
)
nghAggrDynDelSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nghAggrDynDelSent.setStatus("current")
_NghAggrDynAckRcvd_Type = Counter32
_NghAggrDynAckRcvd_Object = MibScalar
nghAggrDynAckRcvd = _NghAggrDynAckRcvd_Object(
    (1, 3, 6, 1, 4, 1, 17163, 1, 1, 2, 12, 2, 15),
    _NghAggrDynAckRcvd_Type()
)
nghAggrDynAckRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nghAggrDynAckRcvd.setStatus("current")
_NghAggrDynReqRcvd_Type = Counter32
_NghAggrDynReqRcvd_Object = MibScalar
nghAggrDynReqRcvd = _NghAggrDynReqRcvd_Object(
    (1, 3, 6, 1, 4, 1, 17163, 1, 1, 2, 12, 2, 16),
    _NghAggrDynReqRcvd_Type()
)
nghAggrDynReqRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nghAggrDynReqRcvd.setStatus("current")
_NghAggrDynDelRcvd_Type = Counter32
_NghAggrDynDelRcvd_Object = MibScalar
nghAggrDynDelRcvd = _NghAggrDynDelRcvd_Object(
    (1, 3, 6, 1, 4, 1, 17163, 1, 1, 2, 12, 2, 17),
    _NghAggrDynDelRcvd_Type()
)
nghAggrDynDelRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nghAggrDynDelRcvd.setStatus("current")
_NghAggrDynAckSent_Type = Counter32
_NghAggrDynAckSent_Object = MibScalar
nghAggrDynAckSent = _NghAggrDynAckSent_Object(
    (1, 3, 6, 1, 4, 1, 17163, 1, 1, 2, 12, 2, 18),
    _NghAggrDynAckSent_Type()
)
nghAggrDynAckSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nghAggrDynAckSent.setStatus("current")
_NghAggrRedirReqSent_Type = Counter32
_NghAggrRedirReqSent_Object = MibScalar
nghAggrRedirReqSent = _NghAggrRedirReqSent_Object(
    (1, 3, 6, 1, 4, 1, 17163, 1, 1, 2, 12, 2, 19),
    _NghAggrRedirReqSent_Type()
)
nghAggrRedirReqSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nghAggrRedirReqSent.setStatus("current")
_NghAggrRedirDelSent_Type = Counter32
_NghAggrRedirDelSent_Object = MibScalar
nghAggrRedirDelSent = _NghAggrRedirDelSent_Object(
    (1, 3, 6, 1, 4, 1, 17163, 1, 1, 2, 12, 2, 20),
    _NghAggrRedirDelSent_Type()
)
nghAggrRedirDelSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nghAggrRedirDelSent.setStatus("current")
_NghAggrRedirAckRcvd_Type = Counter32
_NghAggrRedirAckRcvd_Object = MibScalar
nghAggrRedirAckRcvd = _NghAggrRedirAckRcvd_Object(
    (1, 3, 6, 1, 4, 1, 17163, 1, 1, 2, 12, 2, 21),
    _NghAggrRedirAckRcvd_Type()
)
nghAggrRedirAckRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nghAggrRedirAckRcvd.setStatus("current")
_NghAggrRedirReqRcvd_Type = Counter32
_NghAggrRedirReqRcvd_Object = MibScalar
nghAggrRedirReqRcvd = _NghAggrRedirReqRcvd_Object(
    (1, 3, 6, 1, 4, 1, 17163, 1, 1, 2, 12, 2, 22),
    _NghAggrRedirReqRcvd_Type()
)
nghAggrRedirReqRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nghAggrRedirReqRcvd.setStatus("current")
_NghAggrRedirDelRcvd_Type = Counter32
_NghAggrRedirDelRcvd_Object = MibScalar
nghAggrRedirDelRcvd = _NghAggrRedirDelRcvd_Object(
    (1, 3, 6, 1, 4, 1, 17163, 1, 1, 2, 12, 2, 23),
    _NghAggrRedirDelRcvd_Type()
)
nghAggrRedirDelRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nghAggrRedirDelRcvd.setStatus("current")
_NghAggrRedirAckSent_Type = Counter32
_NghAggrRedirAckSent_Object = MibScalar
nghAggrRedirAckSent = _NghAggrRedirAckSent_Object(
    (1, 3, 6, 1, 4, 1, 17163, 1, 1, 2, 12, 2, 24),
    _NghAggrRedirAckSent_Type()
)
nghAggrRedirAckSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nghAggrRedirAckSent.setStatus("current")
_CapabilityStatus_ObjectIdentity = ObjectIdentity
capabilityStatus = _CapabilityStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17163, 1, 1, 2, 13)
)
_ShMaxConnections_Type = Unsigned32
_ShMaxConnections_Object = MibScalar
shMaxConnections = _ShMaxConnections_Object(
    (1, 3, 6, 1, 4, 1, 17163, 1, 1, 2, 13, 1),
    _ShMaxConnections_Type()
)
shMaxConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shMaxConnections.setStatus("current")
_ShMaxBandwidth_Type = Counter64
_ShMaxBandwidth_Object = MibScalar
shMaxBandwidth = _ShMaxBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 17163, 1, 1, 2, 13, 2),
    _ShMaxBandwidth_Type()
)
shMaxBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shMaxBandwidth.setStatus("current")
_AsymRouteCount_Type = Unsigned32
_AsymRouteCount_Object = MibScalar
asymRouteCount = _AsymRouteCount_Object(
    (1, 3, 6, 1, 4, 1, 17163, 1, 1, 2, 14),
    _AsymRouteCount_Type()
)
asymRouteCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asymRouteCount.setStatus("current")
_Config_ObjectIdentity = ObjectIdentity
config = _Config_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17163, 1, 1, 3)
)
_ActiveConfig_Type = OctetString
_ActiveConfig_Object = MibScalar
activeConfig = _ActiveConfig_Object(
    (1, 3, 6, 1, 4, 1, 17163, 1, 1, 3, 1),
    _ActiveConfig_Type()
)
activeConfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    activeConfig.setStatus("current")
_Inpath_ObjectIdentity = ObjectIdentity
inpath = _Inpath_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17163, 1, 1, 3, 2)
)
_InpathSupport_Type = Unsigned32
_InpathSupport_Object = MibScalar
inpathSupport = _InpathSupport_Object(
    (1, 3, 6, 1, 4, 1, 17163, 1, 1, 3, 2, 1),
    _InpathSupport_Type()
)
inpathSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inpathSupport.setStatus("current")
_Outofpath_ObjectIdentity = ObjectIdentity
outofpath = _Outofpath_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17163, 1, 1, 3, 3)
)
_OutofpathSupport_Type = Unsigned32
_OutofpathSupport_Object = MibScalar
outofpathSupport = _OutofpathSupport_Object(
    (1, 3, 6, 1, 4, 1, 17163, 1, 1, 3, 3, 1),
    _OutofpathSupport_Type()
)
outofpathSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outofpathSupport.setStatus("current")
_DatastoreSync_ObjectIdentity = ObjectIdentity
datastoreSync = _DatastoreSync_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17163, 1, 1, 3, 4)
)
_DatastoreSyncPort_Type = Unsigned32
_DatastoreSyncPort_Object = MibScalar
datastoreSyncPort = _DatastoreSyncPort_Object(
    (1, 3, 6, 1, 4, 1, 17163, 1, 1, 3, 4, 1),
    _DatastoreSyncPort_Type()
)
datastoreSyncPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    datastoreSyncPort.setStatus("current")
_DatastoreSyncAddr_Type = IpAddress
_DatastoreSyncAddr_Object = MibScalar
datastoreSyncAddr = _DatastoreSyncAddr_Object(
    (1, 3, 6, 1, 4, 1, 17163, 1, 1, 3, 4, 2),
    _DatastoreSyncAddr_Type()
)
datastoreSyncAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    datastoreSyncAddr.setStatus("current")
_Alarms_ObjectIdentity = ObjectIdentity
alarms = _Alarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17163, 1, 1, 4)
)
_AlarmsPrefix_ObjectIdentity = ObjectIdentity
alarmsPrefix = _AlarmsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17163, 1, 1, 4, 0)
)
_Statistics_ObjectIdentity = ObjectIdentity
statistics = _Statistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17163, 1, 1, 5)
)
_CpuLoad_ObjectIdentity = ObjectIdentity
cpuLoad = _CpuLoad_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17163, 1, 1, 5, 1)
)
_CpuLoad1_Type = Unsigned32
_CpuLoad1_Object = MibScalar
cpuLoad1 = _CpuLoad1_Object(
    (1, 3, 6, 1, 4, 1, 17163, 1, 1, 5, 1, 1),
    _CpuLoad1_Type()
)
cpuLoad1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuLoad1.setStatus("current")
_CpuLoad5_Type = Unsigned32
_CpuLoad5_Object = MibScalar
cpuLoad5 = _CpuLoad5_Object(
    (1, 3, 6, 1, 4, 1, 17163, 1, 1, 5, 1, 2),
    _CpuLoad5_Type()
)
cpuLoad5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuLoad5.setStatus("current")
_CpuLoad15_Type = Unsigned32
_CpuLoad15_Object = MibScalar
cpuLoad15 = _CpuLoad15_Object(
    (1, 3, 6, 1, 4, 1, 17163, 1, 1, 5, 1, 3),
    _CpuLoad15_Type()
)
cpuLoad15.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuLoad15.setStatus("current")
_CpuUtil1_Type = Unsigned32
_CpuUtil1_Object = MibScalar
cpuUtil1 = _CpuUtil1_Object(
    (1, 3, 6, 1, 4, 1, 17163, 1, 1, 5, 1, 4),
    _CpuUtil1_Type()
)
cpuUtil1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuUtil1.setStatus("current")
_CpuIndivUtilTable_Object = MibTable
cpuIndivUtilTable = _CpuIndivUtilTable_Object(
    (1, 3, 6, 1, 4, 1, 17163, 1, 1, 5, 1, 5)
)
if mibBuilder.loadTexts:
    cpuIndivUtilTable.setStatus("current")
_CpuIndivUtilEntry_Object = MibTableRow
cpuIndivUtilEntry = _CpuIndivUtilEntry_Object(
    (1, 3, 6, 1, 4, 1, 17163, 1, 1, 5, 1, 5, 1)
)
cpuIndivUtilEntry.setIndexNames(
    (0, "STEELHEAD-MIB", "cpuIndivIndex"),
)
if mibBuilder.loadTexts:
    cpuIndivUtilEntry.setStatus("current")
_CpuIndivIndex_Type = Unsigned32
_CpuIndivIndex_Object = MibTableColumn
cpuIndivIndex = _CpuIndivIndex_Object(
    (1, 3, 6, 1, 4, 1, 17163, 1, 1, 5, 1, 5, 1, 1),
    _CpuIndivIndex_Type()
)
cpuIndivIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cpuIndivIndex.setStatus("current")
_CpuIndivId_Type = Unsigned32
_CpuIndivId_Object = MibTableColumn
cpuIndivId = _CpuIndivId_Object(
    (1, 3, 6, 1, 4, 1, 17163, 1, 1, 5, 1, 5, 1, 2),
    _CpuIndivId_Type()
)
cpuIndivId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuIndivId.setStatus("current")
_CpuIndivIdleTime_Type = Unsigned32
_CpuIndivIdleTime_Object = MibTableColumn
cpuIndivIdleTime = _CpuIndivIdleTime_Object(
    (1, 3, 6, 1, 4, 1, 17163, 1, 1, 5, 1, 5, 1, 3),
    _CpuIndivIdleTime_Type()
)
cpuIndivIdleTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuIndivIdleTime.setStatus("current")
_CpuIndivSystemTime_Type = Unsigned32
_CpuIndivSystemTime_Object = MibTableColumn
cpuIndivSystemTime = _CpuIndivSystemTime_Object(
    (1, 3, 6, 1, 4, 1, 17163, 1, 1, 5, 1, 5, 1, 4),
    _CpuIndivSystemTime_Type()
)
cpuIndivSystemTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuIndivSystemTime.setStatus("current")
_CpuIndivUserTime_Type = Unsigned32
_CpuIndivUserTime_Object = MibTableColumn
cpuIndivUserTime = _CpuIndivUserTime_Object(
    (1, 3, 6, 1, 4, 1, 17163, 1, 1, 5, 1, 5, 1, 5),
    _CpuIndivUserTime_Type()
)
cpuIndivUserTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuIndivUserTime.setStatus("current")
_ConnectionCounts_ObjectIdentity = ObjectIdentity
connectionCounts = _ConnectionCounts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17163, 1, 1, 5, 2)
)
_OptimizedConnections_Type = Unsigned32
_OptimizedConnections_Object = MibScalar
optimizedConnections = _OptimizedConnections_Object(
    (1, 3, 6, 1, 4, 1, 17163, 1, 1, 5, 2, 1),
    _OptimizedConnections_Type()
)
optimizedConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    optimizedConnections.setStatus("current")
_PassthroughConnections_Type = Unsigned32
_PassthroughConnections_Object = MibScalar
passthroughConnections = _PassthroughConnections_Object(
    (1, 3, 6, 1, 4, 1, 17163, 1, 1, 5, 2, 2),
    _PassthroughConnections_Type()
)
passthroughConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    passthroughConnections.setStatus("current")
_HalfOpenedConnections_Type = Unsigned32
_HalfOpenedConnections_Object = MibScalar
halfOpenedConnections = _HalfOpenedConnections_Object(
    (1, 3, 6, 1, 4, 1, 17163, 1, 1, 5, 2, 3),
    _HalfOpenedConnections_Type()
)
halfOpenedConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    halfOpenedConnections.setStatus("current")
_HalfClosedConnections_Type = Unsigned32
_HalfClosedConnections_Object = MibScalar
halfClosedConnections = _HalfClosedConnections_Object(
    (1, 3, 6, 1, 4, 1, 17163, 1, 1, 5, 2, 4),
    _HalfClosedConnections_Type()
)
halfClosedConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    halfClosedConnections.setStatus("current")
_EstablishedConnections_Type = Unsigned32
_EstablishedConnections_Object = MibScalar
establishedConnections = _EstablishedConnections_Object(
    (1, 3, 6, 1, 4, 1, 17163, 1, 1, 5, 2, 5),
    _EstablishedConnections_Type()
)
establishedConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    establishedConnections.setStatus("current")
_ActiveConnections_Type = Unsigned32
_ActiveConnections_Object = MibScalar
activeConnections = _ActiveConnections_Object(
    (1, 3, 6, 1, 4, 1, 17163, 1, 1, 5, 2, 6),
    _ActiveConnections_Type()
)
activeConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    activeConnections.setStatus("current")
_TotalConnections_Type = Unsigned32
_TotalConnections_Object = MibScalar
totalConnections = _TotalConnections_Object(
    (1, 3, 6, 1, 4, 1, 17163, 1, 1, 5, 2, 7),
    _TotalConnections_Type()
)
totalConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    totalConnections.setStatus("current")
_Bandwidth_ObjectIdentity = ObjectIdentity
bandwidth = _Bandwidth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17163, 1, 1, 5, 3)
)
_BandwidthAggregate_ObjectIdentity = ObjectIdentity
bandwidthAggregate = _BandwidthAggregate_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17163, 1, 1, 5, 3, 1)
)
_BwAggInLan_Type = Counter32
_BwAggInLan_Object = MibScalar
bwAggInLan = _BwAggInLan_Object(
    (1, 3, 6, 1, 4, 1, 17163, 1, 1, 5, 3, 1, 1),
    _BwAggInLan_Type()
)
bwAggInLan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwAggInLan.setStatus("current")
_BwAggInWan_Type = Counter32
_BwAggInWan_Object = MibScalar
bwAggInWan = _BwAggInWan_Object(
    (1, 3, 6, 1, 4, 1, 17163, 1, 1, 5, 3, 1, 2),
    _BwAggInWan_Type()
)
bwAggInWan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwAggInWan.setStatus("current")
_BwAggOutLan_Type = Counter32
_BwAggOutLan_Object = MibScalar
bwAggOutLan = _BwAggOutLan_Object(
    (1, 3, 6, 1, 4, 1, 17163, 1, 1, 5, 3, 1, 3),
    _BwAggOutLan_Type()
)
bwAggOutLan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwAggOutLan.setStatus("current")
_BwAggOutWan_Type = Counter32
_BwAggOutWan_Object = MibScalar
bwAggOutWan = _BwAggOutWan_Object(
    (1, 3, 6, 1, 4, 1, 17163, 1, 1, 5, 3, 1, 4),
    _BwAggOutWan_Type()
)
bwAggOutWan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwAggOutWan.setStatus("current")
_BandwidthPerPort_ObjectIdentity = ObjectIdentity
bandwidthPerPort = _BandwidthPerPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17163, 1, 1, 5, 3, 2)
)
_BwPortTable_Object = MibTable
bwPortTable = _BwPortTable_Object(
    (1, 3, 6, 1, 4, 1, 17163, 1, 1, 5, 3, 2, 1)
)
if mibBuilder.loadTexts:
    bwPortTable.setStatus("current")
_BwPortEntry_Object = MibTableRow
bwPortEntry = _BwPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 17163, 1, 1, 5, 3, 2, 1, 1)
)
bwPortEntry.setIndexNames(
    (0, "STEELHEAD-MIB", "bwPortNumber"),
)
if mibBuilder.loadTexts:
    bwPortEntry.setStatus("current")
_BwPortNumber_Type = Unsigned32
_BwPortNumber_Object = MibTableColumn
bwPortNumber = _BwPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 17163, 1, 1, 5, 3, 2, 1, 1, 1),
    _BwPortNumber_Type()
)
bwPortNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bwPortNumber.setStatus("current")
_BwPortInLan_Type = Counter32
_BwPortInLan_Object = MibTableColumn
bwPortInLan = _BwPortInLan_Object(
    (1, 3, 6, 1, 4, 1, 17163, 1, 1, 5, 3, 2, 1, 1, 2),
    _BwPortInLan_Type()
)
bwPortInLan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwPortInLan.setStatus("current")
_BwPortInWan_Type = Counter32
_BwPortInWan_Object = MibTableColumn
bwPortInWan = _BwPortInWan_Object(
    (1, 3, 6, 1, 4, 1, 17163, 1, 1, 5, 3, 2, 1, 1, 3),
    _BwPortInWan_Type()
)
bwPortInWan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwPortInWan.setStatus("current")
_BwPortOutLan_Type = Counter32
_BwPortOutLan_Object = MibTableColumn
bwPortOutLan = _BwPortOutLan_Object(
    (1, 3, 6, 1, 4, 1, 17163, 1, 1, 5, 3, 2, 1, 1, 4),
    _BwPortOutLan_Type()
)
bwPortOutLan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwPortOutLan.setStatus("current")
_BwPortOutWan_Type = Counter32
_BwPortOutWan_Object = MibTableColumn
bwPortOutWan = _BwPortOutWan_Object(
    (1, 3, 6, 1, 4, 1, 17163, 1, 1, 5, 3, 2, 1, 1, 5),
    _BwPortOutWan_Type()
)
bwPortOutWan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwPortOutWan.setStatus("current")
_BandwidthPassThrough_ObjectIdentity = ObjectIdentity
bandwidthPassThrough = _BandwidthPassThrough_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17163, 1, 1, 5, 3, 3)
)
_BwPassThroughIn_Type = Counter64
_BwPassThroughIn_Object = MibScalar
bwPassThroughIn = _BwPassThroughIn_Object(
    (1, 3, 6, 1, 4, 1, 17163, 1, 1, 5, 3, 3, 1),
    _BwPassThroughIn_Type()
)
bwPassThroughIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwPassThroughIn.setStatus("current")
_BwPassThroughOut_Type = Counter64
_BwPassThroughOut_Object = MibScalar
bwPassThroughOut = _BwPassThroughOut_Object(
    (1, 3, 6, 1, 4, 1, 17163, 1, 1, 5, 3, 3, 2),
    _BwPassThroughOut_Type()
)
bwPassThroughOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwPassThroughOut.setStatus("current")
_BwPassThroughTotal_Type = Counter64
_BwPassThroughTotal_Object = MibScalar
bwPassThroughTotal = _BwPassThroughTotal_Object(
    (1, 3, 6, 1, 4, 1, 17163, 1, 1, 5, 3, 3, 3),
    _BwPassThroughTotal_Type()
)
bwPassThroughTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwPassThroughTotal.setStatus("current")
_Datastore_ObjectIdentity = ObjectIdentity
datastore = _Datastore_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17163, 1, 1, 5, 4)
)
_DsHitsTotal_Type = Counter64
_DsHitsTotal_Object = MibScalar
dsHitsTotal = _DsHitsTotal_Object(
    (1, 3, 6, 1, 4, 1, 17163, 1, 1, 5, 4, 1),
    _DsHitsTotal_Type()
)
dsHitsTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsHitsTotal.setStatus("current")
_DsMissTotal_Type = Counter64
_DsMissTotal_Object = MibScalar
dsMissTotal = _DsMissTotal_Object(
    (1, 3, 6, 1, 4, 1, 17163, 1, 1, 5, 4, 2),
    _DsMissTotal_Type()
)
dsMissTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsMissTotal.setStatus("current")
_DsCostPerSegment_Type = Unsigned32
_DsCostPerSegment_Object = MibScalar
dsCostPerSegment = _DsCostPerSegment_Object(
    (1, 3, 6, 1, 4, 1, 17163, 1, 1, 5, 4, 3),
    _DsCostPerSegment_Type()
)
dsCostPerSegment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsCostPerSegment.setStatus("deprecated")
_DsAveDiskUtilization_Type = Unsigned32
_DsAveDiskUtilization_Object = MibScalar
dsAveDiskUtilization = _DsAveDiskUtilization_Object(
    (1, 3, 6, 1, 4, 1, 17163, 1, 1, 5, 4, 4),
    _DsAveDiskUtilization_Type()
)
dsAveDiskUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsAveDiskUtilization.setStatus("current")
_TopTalkers_ObjectIdentity = ObjectIdentity
topTalkers = _TopTalkers_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17163, 1, 1, 5, 5)
)
_TtTalkersTable_Object = MibTable
ttTalkersTable = _TtTalkersTable_Object(
    (1, 3, 6, 1, 4, 1, 17163, 1, 1, 5, 5, 1)
)
if mibBuilder.loadTexts:
    ttTalkersTable.setStatus("current")
_TtTalkersEntry_Object = MibTableRow
ttTalkersEntry = _TtTalkersEntry_Object(
    (1, 3, 6, 1, 4, 1, 17163, 1, 1, 5, 5, 1, 1)
)
ttTalkersEntry.setIndexNames(
    (0, "STEELHEAD-MIB", "ttTalkerId"),
)
if mibBuilder.loadTexts:
    ttTalkersEntry.setStatus("current")
_TtTalkerId_Type = Unsigned32
_TtTalkerId_Object = MibTableColumn
ttTalkerId = _TtTalkerId_Object(
    (1, 3, 6, 1, 4, 1, 17163, 1, 1, 5, 5, 1, 1, 1),
    _TtTalkerId_Type()
)
ttTalkerId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ttTalkerId.setStatus("current")
_TtTalkerIp1_Type = IpAddress
_TtTalkerIp1_Object = MibTableColumn
ttTalkerIp1 = _TtTalkerIp1_Object(
    (1, 3, 6, 1, 4, 1, 17163, 1, 1, 5, 5, 1, 1, 2),
    _TtTalkerIp1_Type()
)
ttTalkerIp1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ttTalkerIp1.setStatus("current")
_TtTalkerPort1_Type = Unsigned32
_TtTalkerPort1_Object = MibTableColumn
ttTalkerPort1 = _TtTalkerPort1_Object(
    (1, 3, 6, 1, 4, 1, 17163, 1, 1, 5, 5, 1, 1, 3),
    _TtTalkerPort1_Type()
)
ttTalkerPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ttTalkerPort1.setStatus("current")
_TtTalkerIp2_Type = IpAddress
_TtTalkerIp2_Object = MibTableColumn
ttTalkerIp2 = _TtTalkerIp2_Object(
    (1, 3, 6, 1, 4, 1, 17163, 1, 1, 5, 5, 1, 1, 4),
    _TtTalkerIp2_Type()
)
ttTalkerIp2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ttTalkerIp2.setStatus("current")
_TtTalkerPort2_Type = Unsigned32
_TtTalkerPort2_Object = MibTableColumn
ttTalkerPort2 = _TtTalkerPort2_Object(
    (1, 3, 6, 1, 4, 1, 17163, 1, 1, 5, 5, 1, 1, 5),
    _TtTalkerPort2_Type()
)
ttTalkerPort2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ttTalkerPort2.setStatus("current")
_TtTalkerByteCount_Type = Counter64
_TtTalkerByteCount_Object = MibTableColumn
ttTalkerByteCount = _TtTalkerByteCount_Object(
    (1, 3, 6, 1, 4, 1, 17163, 1, 1, 5, 5, 1, 1, 6),
    _TtTalkerByteCount_Type()
)
ttTalkerByteCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ttTalkerByteCount.setStatus("current")
_TtSrcHostTable_Object = MibTable
ttSrcHostTable = _TtSrcHostTable_Object(
    (1, 3, 6, 1, 4, 1, 17163, 1, 1, 5, 5, 2)
)
if mibBuilder.loadTexts:
    ttSrcHostTable.setStatus("current")
_TtSrcHostEntry_Object = MibTableRow
ttSrcHostEntry = _TtSrcHostEntry_Object(
    (1, 3, 6, 1, 4, 1, 17163, 1, 1, 5, 5, 2, 1)
)
ttSrcHostEntry.setIndexNames(
    (0, "STEELHEAD-MIB", "ttSrcHostId"),
)
if mibBuilder.loadTexts:
    ttSrcHostEntry.setStatus("current")
_TtSrcHostId_Type = Unsigned32
_TtSrcHostId_Object = MibTableColumn
ttSrcHostId = _TtSrcHostId_Object(
    (1, 3, 6, 1, 4, 1, 17163, 1, 1, 5, 5, 2, 1, 1),
    _TtSrcHostId_Type()
)
ttSrcHostId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ttSrcHostId.setStatus("current")
_TtSrcHostIp_Type = IpAddress
_TtSrcHostIp_Object = MibTableColumn
ttSrcHostIp = _TtSrcHostIp_Object(
    (1, 3, 6, 1, 4, 1, 17163, 1, 1, 5, 5, 2, 1, 2),
    _TtSrcHostIp_Type()
)
ttSrcHostIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ttSrcHostIp.setStatus("current")
_TtSrcHostByteCount_Type = Counter64
_TtSrcHostByteCount_Object = MibTableColumn
ttSrcHostByteCount = _TtSrcHostByteCount_Object(
    (1, 3, 6, 1, 4, 1, 17163, 1, 1, 5, 5, 2, 1, 3),
    _TtSrcHostByteCount_Type()
)
ttSrcHostByteCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ttSrcHostByteCount.setStatus("current")
_TtDestHostTable_Object = MibTable
ttDestHostTable = _TtDestHostTable_Object(
    (1, 3, 6, 1, 4, 1, 17163, 1, 1, 5, 5, 3)
)
if mibBuilder.loadTexts:
    ttDestHostTable.setStatus("current")
_TtDestHostEntry_Object = MibTableRow
ttDestHostEntry = _TtDestHostEntry_Object(
    (1, 3, 6, 1, 4, 1, 17163, 1, 1, 5, 5, 3, 1)
)
ttDestHostEntry.setIndexNames(
    (0, "STEELHEAD-MIB", "ttDestHostId"),
)
if mibBuilder.loadTexts:
    ttDestHostEntry.setStatus("current")
_TtDestHostId_Type = Unsigned32
_TtDestHostId_Object = MibTableColumn
ttDestHostId = _TtDestHostId_Object(
    (1, 3, 6, 1, 4, 1, 17163, 1, 1, 5, 5, 3, 1, 1),
    _TtDestHostId_Type()
)
ttDestHostId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ttDestHostId.setStatus("current")
_TtDestHostIp_Type = IpAddress
_TtDestHostIp_Object = MibTableColumn
ttDestHostIp = _TtDestHostIp_Object(
    (1, 3, 6, 1, 4, 1, 17163, 1, 1, 5, 5, 3, 1, 2),
    _TtDestHostIp_Type()
)
ttDestHostIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ttDestHostIp.setStatus("current")
_TtDestHostByteCount_Type = Counter64
_TtDestHostByteCount_Object = MibTableColumn
ttDestHostByteCount = _TtDestHostByteCount_Object(
    (1, 3, 6, 1, 4, 1, 17163, 1, 1, 5, 5, 3, 1, 3),
    _TtDestHostByteCount_Type()
)
ttDestHostByteCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ttDestHostByteCount.setStatus("current")
_TtAppPortTable_Object = MibTable
ttAppPortTable = _TtAppPortTable_Object(
    (1, 3, 6, 1, 4, 1, 17163, 1, 1, 5, 5, 4)
)
if mibBuilder.loadTexts:
    ttAppPortTable.setStatus("current")
_TtAppPortEntry_Object = MibTableRow
ttAppPortEntry = _TtAppPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 17163, 1, 1, 5, 5, 4, 1)
)
ttAppPortEntry.setIndexNames(
    (0, "STEELHEAD-MIB", "ttAppPortId"),
)
if mibBuilder.loadTexts:
    ttAppPortEntry.setStatus("current")
_TtAppPortId_Type = Unsigned32
_TtAppPortId_Object = MibTableColumn
ttAppPortId = _TtAppPortId_Object(
    (1, 3, 6, 1, 4, 1, 17163, 1, 1, 5, 5, 4, 1, 1),
    _TtAppPortId_Type()
)
ttAppPortId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ttAppPortId.setStatus("current")
_TtAppPort_Type = Unsigned32
_TtAppPort_Object = MibTableColumn
ttAppPort = _TtAppPort_Object(
    (1, 3, 6, 1, 4, 1, 17163, 1, 1, 5, 5, 4, 1, 2),
    _TtAppPort_Type()
)
ttAppPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ttAppPort.setStatus("current")
_TtAppPortByteCount_Type = Counter64
_TtAppPortByteCount_Object = MibTableColumn
ttAppPortByteCount = _TtAppPortByteCount_Object(
    (1, 3, 6, 1, 4, 1, 17163, 1, 1, 5, 5, 4, 1, 3),
    _TtAppPortByteCount_Type()
)
ttAppPortByteCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ttAppPortByteCount.setStatus("current")
_BandwidthHC_ObjectIdentity = ObjectIdentity
bandwidthHC = _BandwidthHC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17163, 1, 1, 5, 6)
)
_BandwidthHCAggregate_ObjectIdentity = ObjectIdentity
bandwidthHCAggregate = _BandwidthHCAggregate_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17163, 1, 1, 5, 6, 1)
)
_BwHCAggInLan_Type = Counter64
_BwHCAggInLan_Object = MibScalar
bwHCAggInLan = _BwHCAggInLan_Object(
    (1, 3, 6, 1, 4, 1, 17163, 1, 1, 5, 6, 1, 1),
    _BwHCAggInLan_Type()
)
bwHCAggInLan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwHCAggInLan.setStatus("current")
_BwHCAggInWan_Type = Counter64
_BwHCAggInWan_Object = MibScalar
bwHCAggInWan = _BwHCAggInWan_Object(
    (1, 3, 6, 1, 4, 1, 17163, 1, 1, 5, 6, 1, 2),
    _BwHCAggInWan_Type()
)
bwHCAggInWan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwHCAggInWan.setStatus("current")
_BwHCAggOutLan_Type = Counter64
_BwHCAggOutLan_Object = MibScalar
bwHCAggOutLan = _BwHCAggOutLan_Object(
    (1, 3, 6, 1, 4, 1, 17163, 1, 1, 5, 6, 1, 3),
    _BwHCAggOutLan_Type()
)
bwHCAggOutLan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwHCAggOutLan.setStatus("current")
_BwAggHCOutWan_Type = Counter64
_BwAggHCOutWan_Object = MibScalar
bwAggHCOutWan = _BwAggHCOutWan_Object(
    (1, 3, 6, 1, 4, 1, 17163, 1, 1, 5, 6, 1, 4),
    _BwAggHCOutWan_Type()
)
bwAggHCOutWan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwAggHCOutWan.setStatus("current")
_BandwidthHCPerPort_ObjectIdentity = ObjectIdentity
bandwidthHCPerPort = _BandwidthHCPerPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17163, 1, 1, 5, 6, 2)
)
_BwHCPortTable_Object = MibTable
bwHCPortTable = _BwHCPortTable_Object(
    (1, 3, 6, 1, 4, 1, 17163, 1, 1, 5, 6, 2, 1)
)
if mibBuilder.loadTexts:
    bwHCPortTable.setStatus("current")
_BwHCPortEntry_Object = MibTableRow
bwHCPortEntry = _BwHCPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 17163, 1, 1, 5, 6, 2, 1, 1)
)
bwHCPortEntry.setIndexNames(
    (0, "STEELHEAD-MIB", "bwHCPortNumber"),
)
if mibBuilder.loadTexts:
    bwHCPortEntry.setStatus("current")
_BwHCPortNumber_Type = Unsigned32
_BwHCPortNumber_Object = MibTableColumn
bwHCPortNumber = _BwHCPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 17163, 1, 1, 5, 6, 2, 1, 1, 1),
    _BwHCPortNumber_Type()
)
bwHCPortNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bwHCPortNumber.setStatus("current")
_BwHCPortInLan_Type = Counter64
_BwHCPortInLan_Object = MibTableColumn
bwHCPortInLan = _BwHCPortInLan_Object(
    (1, 3, 6, 1, 4, 1, 17163, 1, 1, 5, 6, 2, 1, 1, 2),
    _BwHCPortInLan_Type()
)
bwHCPortInLan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwHCPortInLan.setStatus("current")
_BwHCPortInWan_Type = Counter64
_BwHCPortInWan_Object = MibTableColumn
bwHCPortInWan = _BwHCPortInWan_Object(
    (1, 3, 6, 1, 4, 1, 17163, 1, 1, 5, 6, 2, 1, 1, 3),
    _BwHCPortInWan_Type()
)
bwHCPortInWan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwHCPortInWan.setStatus("current")
_BwHCPortOutLan_Type = Counter64
_BwHCPortOutLan_Object = MibTableColumn
bwHCPortOutLan = _BwHCPortOutLan_Object(
    (1, 3, 6, 1, 4, 1, 17163, 1, 1, 5, 6, 2, 1, 1, 4),
    _BwHCPortOutLan_Type()
)
bwHCPortOutLan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwHCPortOutLan.setStatus("current")
_BwHCPortOutWan_Type = Counter64
_BwHCPortOutWan_Object = MibTableColumn
bwHCPortOutWan = _BwHCPortOutWan_Object(
    (1, 3, 6, 1, 4, 1, 17163, 1, 1, 5, 6, 2, 1, 1, 5),
    _BwHCPortOutWan_Type()
)
bwHCPortOutWan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwHCPortOutWan.setStatus("current")

# Managed Objects groups


# Notification objects

procCrash = NotificationType(
    (1, 3, 6, 1, 4, 1, 17163, 1, 1, 4, 0, 1)
)
procCrash.setObjects(
    ("STEELHEAD-MIB", "procName")
)
if mibBuilder.loadTexts:
    procCrash.setStatus(
        "current"
    )

procExit = NotificationType(
    (1, 3, 6, 1, 4, 1, 17163, 1, 1, 4, 0, 2)
)
procExit.setObjects(
    ("STEELHEAD-MIB", "procName")
)
if mibBuilder.loadTexts:
    procExit.setStatus(
        "current"
    )

cpuUtil = NotificationType(
    (1, 3, 6, 1, 4, 1, 17163, 1, 1, 4, 0, 3)
)
if mibBuilder.loadTexts:
    cpuUtil.setStatus(
        "current"
    )

pagingActivity = NotificationType(
    (1, 3, 6, 1, 4, 1, 17163, 1, 1, 4, 0, 4)
)
if mibBuilder.loadTexts:
    pagingActivity.setStatus(
        "current"
    )

smartError = NotificationType(
    (1, 3, 6, 1, 4, 1, 17163, 1, 1, 4, 0, 5)
)
if mibBuilder.loadTexts:
    smartError.setStatus(
        "current"
    )

peerVersionMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 17163, 1, 1, 4, 0, 6)
)
peerVersionMismatch.setObjects(
    ("STEELHEAD-MIB", "systemVersion")
)
if mibBuilder.loadTexts:
    peerVersionMismatch.setStatus(
        "current"
    )

bypassMode = NotificationType(
    (1, 3, 6, 1, 4, 1, 17163, 1, 1, 4, 0, 7)
)
if mibBuilder.loadTexts:
    bypassMode.setStatus(
        "current"
    )

raidError = NotificationType(
    (1, 3, 6, 1, 4, 1, 17163, 1, 1, 4, 0, 8)
)
if mibBuilder.loadTexts:
    raidError.setStatus(
        "current"
    )

storeCorruption = NotificationType(
    (1, 3, 6, 1, 4, 1, 17163, 1, 1, 4, 0, 9)
)
if mibBuilder.loadTexts:
    storeCorruption.setStatus(
        "current"
    )

admissionMemError = NotificationType(
    (1, 3, 6, 1, 4, 1, 17163, 1, 1, 4, 0, 10)
)
if mibBuilder.loadTexts:
    admissionMemError.setStatus(
        "current"
    )

admissionConnError = NotificationType(
    (1, 3, 6, 1, 4, 1, 17163, 1, 1, 4, 0, 11)
)
if mibBuilder.loadTexts:
    admissionConnError.setStatus(
        "current"
    )

haltError = NotificationType(
    (1, 3, 6, 1, 4, 1, 17163, 1, 1, 4, 0, 12)
)
if mibBuilder.loadTexts:
    haltError.setStatus(
        "current"
    )

serviceError = NotificationType(
    (1, 3, 6, 1, 4, 1, 17163, 1, 1, 4, 0, 13)
)
if mibBuilder.loadTexts:
    serviceError.setStatus(
        "current"
    )

scheduledJobError = NotificationType(
    (1, 3, 6, 1, 4, 1, 17163, 1, 1, 4, 0, 14)
)
if mibBuilder.loadTexts:
    scheduledJobError.setStatus(
        "current"
    )

confModeEnter = NotificationType(
    (1, 3, 6, 1, 4, 1, 17163, 1, 1, 4, 0, 15)
)
if mibBuilder.loadTexts:
    confModeEnter.setStatus(
        "current"
    )

confModeExit = NotificationType(
    (1, 3, 6, 1, 4, 1, 17163, 1, 1, 4, 0, 16)
)
if mibBuilder.loadTexts:
    confModeExit.setStatus(
        "current"
    )

linkError = NotificationType(
    (1, 3, 6, 1, 4, 1, 17163, 1, 1, 4, 0, 17)
)
if mibBuilder.loadTexts:
    linkError.setStatus(
        "current"
    )

nfsV2V4 = NotificationType(
    (1, 3, 6, 1, 4, 1, 17163, 1, 1, 4, 0, 18)
)
if mibBuilder.loadTexts:
    nfsV2V4.setStatus(
        "current"
    )

powerSupplyError = NotificationType(
    (1, 3, 6, 1, 4, 1, 17163, 1, 1, 4, 0, 19)
)
if mibBuilder.loadTexts:
    powerSupplyError.setStatus(
        "current"
    )

asymRouteError = NotificationType(
    (1, 3, 6, 1, 4, 1, 17163, 1, 1, 4, 0, 20)
)
asymRouteError.setObjects(
    ("STEELHEAD-MIB", "asymRouteCount")
)
if mibBuilder.loadTexts:
    asymRouteError.setStatus(
        "current"
    )

fanError = NotificationType(
    (1, 3, 6, 1, 4, 1, 17163, 1, 1, 4, 0, 21)
)
if mibBuilder.loadTexts:
    fanError.setStatus(
        "current"
    )

memoryError = NotificationType(
    (1, 3, 6, 1, 4, 1, 17163, 1, 1, 4, 0, 22)
)
if mibBuilder.loadTexts:
    memoryError.setStatus(
        "current"
    )

ipmi = NotificationType(
    (1, 3, 6, 1, 4, 1, 17163, 1, 1, 4, 0, 23)
)
if mibBuilder.loadTexts:
    ipmi.setStatus(
        "current"
    )

configChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 17163, 1, 1, 4, 0, 24)
)
if mibBuilder.loadTexts:
    configChange.setStatus(
        "current"
    )

datastoreWrapped = NotificationType(
    (1, 3, 6, 1, 4, 1, 17163, 1, 1, 4, 0, 25)
)
if mibBuilder.loadTexts:
    datastoreWrapped.setStatus(
        "current"
    )

temperatureWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 17163, 1, 1, 4, 0, 26)
)
if mibBuilder.loadTexts:
    temperatureWarning.setStatus(
        "current"
    )

temperatureCritical = NotificationType(
    (1, 3, 6, 1, 4, 1, 17163, 1, 1, 4, 0, 27)
)
if mibBuilder.loadTexts:
    temperatureCritical.setStatus(
        "current"
    )

cfConnFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 17163, 1, 1, 4, 0, 28)
)
cfConnFailure.setObjects(
    ("STEELHEAD-MIB", "neighborAddress")
)
if mibBuilder.loadTexts:
    cfConnFailure.setStatus(
        "current"
    )

cfConnLostEos = NotificationType(
    (1, 3, 6, 1, 4, 1, 17163, 1, 1, 4, 0, 29)
)
cfConnLostEos.setObjects(
    ("STEELHEAD-MIB", "neighborAddress")
)
if mibBuilder.loadTexts:
    cfConnLostEos.setStatus(
        "current"
    )

cfConnLostErr = NotificationType(
    (1, 3, 6, 1, 4, 1, 17163, 1, 1, 4, 0, 30)
)
cfConnLostErr.setObjects(
    ("STEELHEAD-MIB", "neighborAddress")
)
if mibBuilder.loadTexts:
    cfConnLostErr.setStatus(
        "current"
    )

cfKeepaliveTimeout = NotificationType(
    (1, 3, 6, 1, 4, 1, 17163, 1, 1, 4, 0, 31)
)
cfKeepaliveTimeout.setObjects(
    ("STEELHEAD-MIB", "neighborAddress")
)
if mibBuilder.loadTexts:
    cfKeepaliveTimeout.setStatus(
        "current"
    )

cfAckTimeout = NotificationType(
    (1, 3, 6, 1, 4, 1, 17163, 1, 1, 4, 0, 32)
)
cfAckTimeout.setObjects(
    ("STEELHEAD-MIB", "neighborAddress")
)
if mibBuilder.loadTexts:
    cfAckTimeout.setStatus(
        "current"
    )

cfReadInfoTimeout = NotificationType(
    (1, 3, 6, 1, 4, 1, 17163, 1, 1, 4, 0, 33)
)
cfReadInfoTimeout.setObjects(
    ("STEELHEAD-MIB", "neighborAddress")
)
if mibBuilder.loadTexts:
    cfReadInfoTimeout.setStatus(
        "current"
    )

cfLatencyExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 17163, 1, 1, 4, 0, 34)
)
cfLatencyExceeded.setObjects(
    ("STEELHEAD-MIB", "neighborAddress")
)
if mibBuilder.loadTexts:
    cfLatencyExceeded.setStatus(
        "current"
    )

sslPeeringSCEPAutoReenrollError = NotificationType(
    (1, 3, 6, 1, 4, 1, 17163, 1, 1, 4, 0, 35)
)
if mibBuilder.loadTexts:
    sslPeeringSCEPAutoReenrollError.setStatus(
        "current"
    )

crlError = NotificationType(
    (1, 3, 6, 1, 4, 1, 17163, 1, 1, 4, 0, 36)
)
crlError.setObjects(
      *(("STEELHEAD-MIB", "crlFeatureName"),
        ("STEELHEAD-MIB", "crlErrMsg"))
)
if mibBuilder.loadTexts:
    crlError.setStatus(
        "current"
    )

datastoreSyncFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 17163, 1, 1, 4, 0, 37)
)
if mibBuilder.loadTexts:
    datastoreSyncFailure.setStatus(
        "current"
    )

secureVaultNeedsUnlock = NotificationType(
    (1, 3, 6, 1, 4, 1, 17163, 1, 1, 4, 0, 38)
)
if mibBuilder.loadTexts:
    secureVaultNeedsUnlock.setStatus(
        "current"
    )

secureVaultNeedsRekey = NotificationType(
    (1, 3, 6, 1, 4, 1, 17163, 1, 1, 4, 0, 39)
)
if mibBuilder.loadTexts:
    secureVaultNeedsRekey.setStatus(
        "current"
    )

secureVaultInitError = NotificationType(
    (1, 3, 6, 1, 4, 1, 17163, 1, 1, 4, 0, 40)
)
if mibBuilder.loadTexts:
    secureVaultInitError.setStatus(
        "current"
    )

configSave = NotificationType(
    (1, 3, 6, 1, 4, 1, 17163, 1, 1, 4, 0, 41)
)
if mibBuilder.loadTexts:
    configSave.setStatus(
        "current"
    )

tcpDumpStarted = NotificationType(
    (1, 3, 6, 1, 4, 1, 17163, 1, 1, 4, 0, 42)
)
if mibBuilder.loadTexts:
    tcpDumpStarted.setStatus(
        "current"
    )

tcpDumpScheduled = NotificationType(
    (1, 3, 6, 1, 4, 1, 17163, 1, 1, 4, 0, 43)
)
if mibBuilder.loadTexts:
    tcpDumpScheduled.setStatus(
        "current"
    )

newUserCreated = NotificationType(
    (1, 3, 6, 1, 4, 1, 17163, 1, 1, 4, 0, 44)
)
if mibBuilder.loadTexts:
    newUserCreated.setStatus(
        "current"
    )

diskError = NotificationType(
    (1, 3, 6, 1, 4, 1, 17163, 1, 1, 4, 0, 45)
)
if mibBuilder.loadTexts:
    diskError.setStatus(
        "current"
    )

wearWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 17163, 1, 1, 4, 0, 46)
)
if mibBuilder.loadTexts:
    wearWarning.setStatus(
        "current"
    )

cliUserLogin = NotificationType(
    (1, 3, 6, 1, 4, 1, 17163, 1, 1, 4, 0, 47)
)
if mibBuilder.loadTexts:
    cliUserLogin.setStatus(
        "current"
    )

cliUserLogout = NotificationType(
    (1, 3, 6, 1, 4, 1, 17163, 1, 1, 4, 0, 48)
)
if mibBuilder.loadTexts:
    cliUserLogout.setStatus(
        "current"
    )

webUserLogin = NotificationType(
    (1, 3, 6, 1, 4, 1, 17163, 1, 1, 4, 0, 49)
)
if mibBuilder.loadTexts:
    webUserLogin.setStatus(
        "current"
    )

webUserLogout = NotificationType(
    (1, 3, 6, 1, 4, 1, 17163, 1, 1, 4, 0, 50)
)
if mibBuilder.loadTexts:
    webUserLogout.setStatus(
        "current"
    )

trapTest = NotificationType(
    (1, 3, 6, 1, 4, 1, 17163, 1, 1, 4, 0, 51)
)
if mibBuilder.loadTexts:
    trapTest.setStatus(
        "current"
    )

admissionCpuError = NotificationType(
    (1, 3, 6, 1, 4, 1, 17163, 1, 1, 4, 0, 52)
)
if mibBuilder.loadTexts:
    admissionCpuError.setStatus(
        "current"
    )

admissionTcpError = NotificationType(
    (1, 3, 6, 1, 4, 1, 17163, 1, 1, 4, 0, 53)
)
if mibBuilder.loadTexts:
    admissionTcpError.setStatus(
        "current"
    )

systemDiskFullError = NotificationType(
    (1, 3, 6, 1, 4, 1, 17163, 1, 1, 4, 0, 54)
)
if mibBuilder.loadTexts:
    systemDiskFullError.setStatus(
        "current"
    )

domainJoinError = NotificationType(
    (1, 3, 6, 1, 4, 1, 17163, 1, 1, 4, 0, 55)
)
if mibBuilder.loadTexts:
    domainJoinError.setStatus(
        "current"
    )

certsExpiringError = NotificationType(
    (1, 3, 6, 1, 4, 1, 17163, 1, 1, 4, 0, 56)
)
if mibBuilder.loadTexts:
    certsExpiringError.setStatus(
        "current"
    )

licenseError = NotificationType(
    (1, 3, 6, 1, 4, 1, 17163, 1, 1, 4, 0, 57)
)
if mibBuilder.loadTexts:
    licenseError.setStatus(
        "current"
    )

hardwareError = NotificationType(
    (1, 3, 6, 1, 4, 1, 17163, 1, 1, 4, 0, 58)
)
if mibBuilder.loadTexts:
    hardwareError.setStatus(
        "current"
    )

sysdetailError = NotificationType(
    (1, 3, 6, 1, 4, 1, 17163, 1, 1, 4, 0, 59)
)
if mibBuilder.loadTexts:
    sysdetailError.setStatus(
        "current"
    )

admissionMapiError = NotificationType(
    (1, 3, 6, 1, 4, 1, 17163, 1, 1, 4, 0, 60)
)
if mibBuilder.loadTexts:
    admissionMapiError.setStatus(
        "current"
    )

neighborIncompatibility = NotificationType(
    (1, 3, 6, 1, 4, 1, 17163, 1, 1, 4, 0, 61)
)
if mibBuilder.loadTexts:
    neighborIncompatibility.setStatus(
        "current"
    )

flashError = NotificationType(
    (1, 3, 6, 1, 4, 1, 17163, 1, 1, 4, 0, 62)
)
if mibBuilder.loadTexts:
    flashError.setStatus(
        "current"
    )

lanWanLoopError = NotificationType(
    (1, 3, 6, 1, 4, 1, 17163, 1, 1, 4, 0, 63)
)
if mibBuilder.loadTexts:
    lanWanLoopError.setStatus(
        "current"
    )

optimizationServiceStatusError = NotificationType(
    (1, 3, 6, 1, 4, 1, 17163, 1, 1, 4, 0, 64)
)
if mibBuilder.loadTexts:
    optimizationServiceStatusError.setStatus(
        "current"
    )

upgradeFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 17163, 1, 1, 4, 0, 65)
)
if mibBuilder.loadTexts:
    upgradeFailure.setStatus(
        "current"
    )

licenseExpiring = NotificationType(
    (1, 3, 6, 1, 4, 1, 17163, 1, 1, 4, 0, 66)
)
if mibBuilder.loadTexts:
    licenseExpiring.setStatus(
        "current"
    )

licenseExpired = NotificationType(
    (1, 3, 6, 1, 4, 1, 17163, 1, 1, 4, 0, 67)
)
if mibBuilder.loadTexts:
    licenseExpired.setStatus(
        "current"
    )

clusterDisconnectedSHAlertError = NotificationType(
    (1, 3, 6, 1, 4, 1, 17163, 1, 1, 4, 0, 68)
)
if mibBuilder.loadTexts:
    clusterDisconnectedSHAlertError.setStatus(
        "current"
    )

smbAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 17163, 1, 1, 4, 0, 69)
)
if mibBuilder.loadTexts:
    smbAlert.setStatus(
        "current"
    )

linkDuplex = NotificationType(
    (1, 3, 6, 1, 4, 1, 17163, 1, 1, 4, 0, 70)
)
if mibBuilder.loadTexts:
    linkDuplex.setStatus(
        "current"
    )

linkIoErrors = NotificationType(
    (1, 3, 6, 1, 4, 1, 17163, 1, 1, 4, 0, 71)
)
if mibBuilder.loadTexts:
    linkIoErrors.setStatus(
        "current"
    )

storageProfSwitchFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 17163, 1, 1, 4, 0, 73)
)
if mibBuilder.loadTexts:
    storageProfSwitchFailed.setStatus(
        "current"
    )

clusterIpv6IncompatiblePeerError = NotificationType(
    (1, 3, 6, 1, 4, 1, 17163, 1, 1, 4, 0, 74)
)
if mibBuilder.loadTexts:
    clusterIpv6IncompatiblePeerError.setStatus(
        "current"
    )

flashProtectionFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 17163, 1, 1, 4, 0, 75)
)
if mibBuilder.loadTexts:
    flashProtectionFailed.setStatus(
        "current"
    )

datastoreNeedClean = NotificationType(
    (1, 3, 6, 1, 4, 1, 17163, 1, 1, 4, 0, 76)
)
if mibBuilder.loadTexts:
    datastoreNeedClean.setStatus(
        "current"
    )

pathSelectionPathDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 17163, 1, 1, 4, 0, 77)
)
if mibBuilder.loadTexts:
    pathSelectionPathDown.setStatus(
        "current"
    )

clusterNeighborIncompatibleError = NotificationType(
    (1, 3, 6, 1, 4, 1, 17163, 1, 1, 4, 0, 80)
)
if mibBuilder.loadTexts:
    clusterNeighborIncompatibleError.setStatus(
        "current"
    )

pathSelectionPathProbingError = NotificationType(
    (1, 3, 6, 1, 4, 1, 17163, 1, 1, 4, 0, 81)
)
if mibBuilder.loadTexts:
    pathSelectionPathProbingError.setStatus(
        "current"
    )

cpuUtilClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 17163, 1, 1, 4, 0, 1003)
)
if mibBuilder.loadTexts:
    cpuUtilClear.setStatus(
        "current"
    )

pagingActivityClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 17163, 1, 1, 4, 0, 1004)
)
if mibBuilder.loadTexts:
    pagingActivityClear.setStatus(
        "current"
    )

peerVersionMismatchClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 17163, 1, 1, 4, 0, 1006)
)
peerVersionMismatchClear.setObjects(
    ("STEELHEAD-MIB", "systemVersion")
)
if mibBuilder.loadTexts:
    peerVersionMismatchClear.setStatus(
        "current"
    )

bypassModeClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 17163, 1, 1, 4, 0, 1007)
)
if mibBuilder.loadTexts:
    bypassModeClear.setStatus(
        "current"
    )

raidErrorClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 17163, 1, 1, 4, 0, 1008)
)
if mibBuilder.loadTexts:
    raidErrorClear.setStatus(
        "current"
    )

storeCorruptionClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 17163, 1, 1, 4, 0, 1009)
)
if mibBuilder.loadTexts:
    storeCorruptionClear.setStatus(
        "current"
    )

admissionMemErrorClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 17163, 1, 1, 4, 0, 1010)
)
if mibBuilder.loadTexts:
    admissionMemErrorClear.setStatus(
        "current"
    )

admissionConnErrorClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 17163, 1, 1, 4, 0, 1011)
)
if mibBuilder.loadTexts:
    admissionConnErrorClear.setStatus(
        "current"
    )

haltErrorClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 17163, 1, 1, 4, 0, 1012)
)
if mibBuilder.loadTexts:
    haltErrorClear.setStatus(
        "current"
    )

serviceErrorClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 17163, 1, 1, 4, 0, 1013)
)
if mibBuilder.loadTexts:
    serviceErrorClear.setStatus(
        "current"
    )

linkErrorClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 17163, 1, 1, 4, 0, 1017)
)
if mibBuilder.loadTexts:
    linkErrorClear.setStatus(
        "current"
    )

nfsV2V4Clear = NotificationType(
    (1, 3, 6, 1, 4, 1, 17163, 1, 1, 4, 0, 1018)
)
if mibBuilder.loadTexts:
    nfsV2V4Clear.setStatus(
        "current"
    )

powerSupplyErrorClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 17163, 1, 1, 4, 0, 1019)
)
if mibBuilder.loadTexts:
    powerSupplyErrorClear.setStatus(
        "current"
    )

asymRouteErrorClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 17163, 1, 1, 4, 0, 1020)
)
if mibBuilder.loadTexts:
    asymRouteErrorClear.setStatus(
        "current"
    )

fanErrorClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 17163, 1, 1, 4, 0, 1021)
)
if mibBuilder.loadTexts:
    fanErrorClear.setStatus(
        "current"
    )

memoryErrorClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 17163, 1, 1, 4, 0, 1022)
)
if mibBuilder.loadTexts:
    memoryErrorClear.setStatus(
        "current"
    )

ipmiClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 17163, 1, 1, 4, 0, 1023)
)
if mibBuilder.loadTexts:
    ipmiClear.setStatus(
        "current"
    )

temperatureNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 17163, 1, 1, 4, 0, 1026)
)
if mibBuilder.loadTexts:
    temperatureNormal.setStatus(
        "current"
    )

temperatureNonCritical = NotificationType(
    (1, 3, 6, 1, 4, 1, 17163, 1, 1, 4, 0, 1027)
)
if mibBuilder.loadTexts:
    temperatureNonCritical.setStatus(
        "current"
    )

cfConnRestored = NotificationType(
    (1, 3, 6, 1, 4, 1, 17163, 1, 1, 4, 0, 1028)
)
cfConnRestored.setObjects(
    ("STEELHEAD-MIB", "neighborAddress")
)
if mibBuilder.loadTexts:
    cfConnRestored.setStatus(
        "current"
    )

cfConnLostEosClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 17163, 1, 1, 4, 0, 1029)
)
cfConnLostEosClear.setObjects(
    ("STEELHEAD-MIB", "neighborAddress")
)
if mibBuilder.loadTexts:
    cfConnLostEosClear.setStatus(
        "current"
    )

cfConnLostErrClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 17163, 1, 1, 4, 0, 1030)
)
cfConnLostErrClear.setObjects(
    ("STEELHEAD-MIB", "neighborAddress")
)
if mibBuilder.loadTexts:
    cfConnLostErrClear.setStatus(
        "current"
    )

cfKeepaliveTimeoutClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 17163, 1, 1, 4, 0, 1031)
)
cfKeepaliveTimeoutClear.setObjects(
    ("STEELHEAD-MIB", "neighborAddress")
)
if mibBuilder.loadTexts:
    cfKeepaliveTimeoutClear.setStatus(
        "current"
    )

cfAckTimeoutClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 17163, 1, 1, 4, 0, 1032)
)
cfAckTimeoutClear.setObjects(
    ("STEELHEAD-MIB", "neighborAddress")
)
if mibBuilder.loadTexts:
    cfAckTimeoutClear.setStatus(
        "current"
    )

cfReadInfoTimeoutClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 17163, 1, 1, 4, 0, 1033)
)
cfReadInfoTimeoutClear.setObjects(
    ("STEELHEAD-MIB", "neighborAddress")
)
if mibBuilder.loadTexts:
    cfReadInfoTimeoutClear.setStatus(
        "current"
    )

cfLatencyExceededClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 17163, 1, 1, 4, 0, 1034)
)
cfLatencyExceededClear.setObjects(
    ("STEELHEAD-MIB", "neighborAddress")
)
if mibBuilder.loadTexts:
    cfLatencyExceededClear.setStatus(
        "current"
    )

sslPeeringSCEPAutoReenrollClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 17163, 1, 1, 4, 0, 1035)
)
if mibBuilder.loadTexts:
    sslPeeringSCEPAutoReenrollClear.setStatus(
        "current"
    )

crlClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 17163, 1, 1, 4, 0, 1036)
)
if mibBuilder.loadTexts:
    crlClear.setStatus(
        "current"
    )

datastoreSyncFailureClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 17163, 1, 1, 4, 0, 1037)
)
if mibBuilder.loadTexts:
    datastoreSyncFailureClear.setStatus(
        "current"
    )

secureVaultClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 17163, 1, 1, 4, 0, 1040)
)
if mibBuilder.loadTexts:
    secureVaultClear.setStatus(
        "current"
    )

diskErrorClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 17163, 1, 1, 4, 0, 1045)
)
if mibBuilder.loadTexts:
    diskErrorClear.setStatus(
        "current"
    )

admissionCpuErrorClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 17163, 1, 1, 4, 0, 1052)
)
if mibBuilder.loadTexts:
    admissionCpuErrorClear.setStatus(
        "current"
    )

admissionTcpErrorClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 17163, 1, 1, 4, 0, 1053)
)
if mibBuilder.loadTexts:
    admissionTcpErrorClear.setStatus(
        "current"
    )

systemDiskFullErrorClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 17163, 1, 1, 4, 0, 1054)
)
if mibBuilder.loadTexts:
    systemDiskFullErrorClear.setStatus(
        "current"
    )

domainJoinErrorClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 17163, 1, 1, 4, 0, 1055)
)
if mibBuilder.loadTexts:
    domainJoinErrorClear.setStatus(
        "current"
    )

certsExpiringErrorClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 17163, 1, 1, 4, 0, 1056)
)
if mibBuilder.loadTexts:
    certsExpiringErrorClear.setStatus(
        "current"
    )

licenseErrorClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 17163, 1, 1, 4, 0, 1057)
)
if mibBuilder.loadTexts:
    licenseErrorClear.setStatus(
        "current"
    )

hardwareErrorClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 17163, 1, 1, 4, 0, 1058)
)
if mibBuilder.loadTexts:
    hardwareErrorClear.setStatus(
        "current"
    )

sysdetailErrorClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 17163, 1, 1, 4, 0, 1059)
)
if mibBuilder.loadTexts:
    sysdetailErrorClear.setStatus(
        "current"
    )

admissionMapiErrorClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 17163, 1, 1, 4, 0, 1060)
)
if mibBuilder.loadTexts:
    admissionMapiErrorClear.setStatus(
        "current"
    )

neighborIncompatibilityClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 17163, 1, 1, 4, 0, 1061)
)
if mibBuilder.loadTexts:
    neighborIncompatibilityClear.setStatus(
        "current"
    )

flashErrorClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 17163, 1, 1, 4, 0, 1062)
)
if mibBuilder.loadTexts:
    flashErrorClear.setStatus(
        "current"
    )

lanWanLoopClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 17163, 1, 1, 4, 0, 1063)
)
if mibBuilder.loadTexts:
    lanWanLoopClear.setStatus(
        "current"
    )

optimizationServiceStatusClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 17163, 1, 1, 4, 0, 1064)
)
if mibBuilder.loadTexts:
    optimizationServiceStatusClear.setStatus(
        "current"
    )

upgradeFailureClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 17163, 1, 1, 4, 0, 1065)
)
if mibBuilder.loadTexts:
    upgradeFailureClear.setStatus(
        "current"
    )

clusterDisconnectedSHAlertClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 17163, 1, 1, 4, 0, 1068)
)
if mibBuilder.loadTexts:
    clusterDisconnectedSHAlertClear.setStatus(
        "current"
    )

smbAlertClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 17163, 1, 1, 4, 0, 1069)
)
if mibBuilder.loadTexts:
    smbAlertClear.setStatus(
        "current"
    )

linkDuplexClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 17163, 1, 1, 4, 0, 1070)
)
if mibBuilder.loadTexts:
    linkDuplexClear.setStatus(
        "current"
    )

linkIoErrorsClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 17163, 1, 1, 4, 0, 1071)
)
if mibBuilder.loadTexts:
    linkIoErrorsClear.setStatus(
        "current"
    )

clusterIpv6IncompatiblePeerClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 17163, 1, 1, 4, 0, 1074)
)
if mibBuilder.loadTexts:
    clusterIpv6IncompatiblePeerClear.setStatus(
        "current"
    )

pathSelectionPathDownClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 17163, 1, 1, 4, 0, 1077)
)
if mibBuilder.loadTexts:
    pathSelectionPathDownClear.setStatus(
        "current"
    )

clusterNeighborIncompatibleClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 17163, 1, 1, 4, 0, 1080)
)
if mibBuilder.loadTexts:
    clusterNeighborIncompatibleClear.setStatus(
        "current"
    )

pathSelectionPathProbingErrorClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 17163, 1, 1, 4, 0, 1081)
)
if mibBuilder.loadTexts:
    pathSelectionPathProbingErrorClear.setStatus(
        "current"
    )

rspGeneralError = NotificationType(
    (1, 3, 6, 1, 4, 1, 17163, 1, 1, 4, 0, 20001)
)
if mibBuilder.loadTexts:
    rspGeneralError.setStatus(
        "current"
    )

rspServiceError = NotificationType(
    (1, 3, 6, 1, 4, 1, 17163, 1, 1, 4, 0, 20002)
)
if mibBuilder.loadTexts:
    rspServiceError.setStatus(
        "current"
    )

rspGeneralClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 17163, 1, 1, 4, 0, 21001)
)
if mibBuilder.loadTexts:
    rspGeneralClear.setStatus(
        "current"
    )

rspServiceClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 17163, 1, 1, 4, 0, 21002)
)
if mibBuilder.loadTexts:
    rspServiceClear.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "STEELHEAD-MIB",
    **{"steelhead": steelhead,
       "system": system,
       "model": model,
       "serialNumber": serialNumber,
       "systemVersion": systemVersion,
       "status": status,
       "systemClock": systemClock,
       "health": health,
       "serviceStatus": serviceStatus,
       "serviceUptime": serviceUptime,
       "procTable": procTable,
       "procEntry": procEntry,
       "procIndex": procIndex,
       "procName": procName,
       "procStatus": procStatus,
       "procNumFailures": procNumFailures,
       "peerStatus": peerStatus,
       "peerTable": peerTable,
       "peerEntry": peerEntry,
       "peerIndex": peerIndex,
       "peerHostname": peerHostname,
       "peerVersion": peerVersion,
       "peerAddress": peerAddress,
       "peerModel": peerModel,
       "systemHealth": systemHealth,
       "optServiceStatus": optServiceStatus,
       "systemTemperature": systemTemperature,
       "healthNotes": healthNotes,
       "crlStatus": crlStatus,
       "crlTable": crlTable,
       "crlEntry": crlEntry,
       "crlIndex": crlIndex,
       "crlFeatureName": crlFeatureName,
       "crlNumCdpErr": crlNumCdpErr,
       "crlErrMsg": crlErrMsg,
       "neighborStatus": neighborStatus,
       "neighborTable": neighborTable,
       "neighborEntry": neighborEntry,
       "neighborIndex": neighborIndex,
       "neighborAddress": neighborAddress,
       "neighborState": neighborState,
       "neighborNatReqSent": neighborNatReqSent,
       "neighborNatDelSent": neighborNatDelSent,
       "neighborNatAckRcvd": neighborNatAckRcvd,
       "neighborNatReqRcvd": neighborNatReqRcvd,
       "neighborNatDelRcvd": neighborNatDelRcvd,
       "neighborNatAckSent": neighborNatAckSent,
       "neighborDynReqSent": neighborDynReqSent,
       "neighborDynDelSent": neighborDynDelSent,
       "neighborDynAckRcvd": neighborDynAckRcvd,
       "neighborDynReqRcvd": neighborDynReqRcvd,
       "neighborDynDelRcvd": neighborDynDelRcvd,
       "neighborDynAckSent": neighborDynAckSent,
       "neighborRedirReqSent": neighborRedirReqSent,
       "neighborRedirDelSent": neighborRedirDelSent,
       "neighborRedirAckRcvd": neighborRedirAckRcvd,
       "neighborRedirReqRcvd": neighborRedirReqRcvd,
       "neighborRedirDelRcvd": neighborRedirDelRcvd,
       "neighborRedirAckSent": neighborRedirAckSent,
       "neighborConnFailures": neighborConnFailures,
       "neighborKeepaliveTimeouts": neighborKeepaliveTimeouts,
       "neighborRequestTimeouts": neighborRequestTimeouts,
       "neighborMaxLatency": neighborMaxLatency,
       "neighborAggregates": neighborAggregates,
       "nghAggrConfigured": nghAggrConfigured,
       "nghAggrConnected": nghAggrConnected,
       "nghAggrConnFailures": nghAggrConnFailures,
       "nghAggrKeepaliveTimouts": nghAggrKeepaliveTimouts,
       "nghAggrRequestTimeouts": nghAggrRequestTimeouts,
       "nghAggrMaxLatency": nghAggrMaxLatency,
       "nghAggrNatReqSent": nghAggrNatReqSent,
       "nghAggrNatDelSent": nghAggrNatDelSent,
       "nghAggrNatAckRcvd": nghAggrNatAckRcvd,
       "nghAggrNatReqRcvd": nghAggrNatReqRcvd,
       "nghAggrNatDelRcvd": nghAggrNatDelRcvd,
       "nghAggrNatAckSent": nghAggrNatAckSent,
       "nghAggrDynReqSent": nghAggrDynReqSent,
       "nghAggrDynDelSent": nghAggrDynDelSent,
       "nghAggrDynAckRcvd": nghAggrDynAckRcvd,
       "nghAggrDynReqRcvd": nghAggrDynReqRcvd,
       "nghAggrDynDelRcvd": nghAggrDynDelRcvd,
       "nghAggrDynAckSent": nghAggrDynAckSent,
       "nghAggrRedirReqSent": nghAggrRedirReqSent,
       "nghAggrRedirDelSent": nghAggrRedirDelSent,
       "nghAggrRedirAckRcvd": nghAggrRedirAckRcvd,
       "nghAggrRedirReqRcvd": nghAggrRedirReqRcvd,
       "nghAggrRedirDelRcvd": nghAggrRedirDelRcvd,
       "nghAggrRedirAckSent": nghAggrRedirAckSent,
       "capabilityStatus": capabilityStatus,
       "shMaxConnections": shMaxConnections,
       "shMaxBandwidth": shMaxBandwidth,
       "asymRouteCount": asymRouteCount,
       "config": config,
       "activeConfig": activeConfig,
       "inpath": inpath,
       "inpathSupport": inpathSupport,
       "outofpath": outofpath,
       "outofpathSupport": outofpathSupport,
       "datastoreSync": datastoreSync,
       "datastoreSyncPort": datastoreSyncPort,
       "datastoreSyncAddr": datastoreSyncAddr,
       "alarms": alarms,
       "alarmsPrefix": alarmsPrefix,
       "procCrash": procCrash,
       "procExit": procExit,
       "cpuUtil": cpuUtil,
       "pagingActivity": pagingActivity,
       "smartError": smartError,
       "peerVersionMismatch": peerVersionMismatch,
       "bypassMode": bypassMode,
       "raidError": raidError,
       "storeCorruption": storeCorruption,
       "admissionMemError": admissionMemError,
       "admissionConnError": admissionConnError,
       "haltError": haltError,
       "serviceError": serviceError,
       "scheduledJobError": scheduledJobError,
       "confModeEnter": confModeEnter,
       "confModeExit": confModeExit,
       "linkError": linkError,
       "nfsV2V4": nfsV2V4,
       "powerSupplyError": powerSupplyError,
       "asymRouteError": asymRouteError,
       "fanError": fanError,
       "memoryError": memoryError,
       "ipmi": ipmi,
       "configChange": configChange,
       "datastoreWrapped": datastoreWrapped,
       "temperatureWarning": temperatureWarning,
       "temperatureCritical": temperatureCritical,
       "cfConnFailure": cfConnFailure,
       "cfConnLostEos": cfConnLostEos,
       "cfConnLostErr": cfConnLostErr,
       "cfKeepaliveTimeout": cfKeepaliveTimeout,
       "cfAckTimeout": cfAckTimeout,
       "cfReadInfoTimeout": cfReadInfoTimeout,
       "cfLatencyExceeded": cfLatencyExceeded,
       "sslPeeringSCEPAutoReenrollError": sslPeeringSCEPAutoReenrollError,
       "crlError": crlError,
       "datastoreSyncFailure": datastoreSyncFailure,
       "secureVaultNeedsUnlock": secureVaultNeedsUnlock,
       "secureVaultNeedsRekey": secureVaultNeedsRekey,
       "secureVaultInitError": secureVaultInitError,
       "configSave": configSave,
       "tcpDumpStarted": tcpDumpStarted,
       "tcpDumpScheduled": tcpDumpScheduled,
       "newUserCreated": newUserCreated,
       "diskError": diskError,
       "wearWarning": wearWarning,
       "cliUserLogin": cliUserLogin,
       "cliUserLogout": cliUserLogout,
       "webUserLogin": webUserLogin,
       "webUserLogout": webUserLogout,
       "trapTest": trapTest,
       "admissionCpuError": admissionCpuError,
       "admissionTcpError": admissionTcpError,
       "systemDiskFullError": systemDiskFullError,
       "domainJoinError": domainJoinError,
       "certsExpiringError": certsExpiringError,
       "licenseError": licenseError,
       "hardwareError": hardwareError,
       "sysdetailError": sysdetailError,
       "admissionMapiError": admissionMapiError,
       "neighborIncompatibility": neighborIncompatibility,
       "flashError": flashError,
       "lanWanLoopError": lanWanLoopError,
       "optimizationServiceStatusError": optimizationServiceStatusError,
       "upgradeFailure": upgradeFailure,
       "licenseExpiring": licenseExpiring,
       "licenseExpired": licenseExpired,
       "clusterDisconnectedSHAlertError": clusterDisconnectedSHAlertError,
       "smbAlert": smbAlert,
       "linkDuplex": linkDuplex,
       "linkIoErrors": linkIoErrors,
       "storageProfSwitchFailed": storageProfSwitchFailed,
       "clusterIpv6IncompatiblePeerError": clusterIpv6IncompatiblePeerError,
       "flashProtectionFailed": flashProtectionFailed,
       "datastoreNeedClean": datastoreNeedClean,
       "pathSelectionPathDown": pathSelectionPathDown,
       "clusterNeighborIncompatibleError": clusterNeighborIncompatibleError,
       "pathSelectionPathProbingError": pathSelectionPathProbingError,
       "cpuUtilClear": cpuUtilClear,
       "pagingActivityClear": pagingActivityClear,
       "peerVersionMismatchClear": peerVersionMismatchClear,
       "bypassModeClear": bypassModeClear,
       "raidErrorClear": raidErrorClear,
       "storeCorruptionClear": storeCorruptionClear,
       "admissionMemErrorClear": admissionMemErrorClear,
       "admissionConnErrorClear": admissionConnErrorClear,
       "haltErrorClear": haltErrorClear,
       "serviceErrorClear": serviceErrorClear,
       "linkErrorClear": linkErrorClear,
       "nfsV2V4Clear": nfsV2V4Clear,
       "powerSupplyErrorClear": powerSupplyErrorClear,
       "asymRouteErrorClear": asymRouteErrorClear,
       "fanErrorClear": fanErrorClear,
       "memoryErrorClear": memoryErrorClear,
       "ipmiClear": ipmiClear,
       "temperatureNormal": temperatureNormal,
       "temperatureNonCritical": temperatureNonCritical,
       "cfConnRestored": cfConnRestored,
       "cfConnLostEosClear": cfConnLostEosClear,
       "cfConnLostErrClear": cfConnLostErrClear,
       "cfKeepaliveTimeoutClear": cfKeepaliveTimeoutClear,
       "cfAckTimeoutClear": cfAckTimeoutClear,
       "cfReadInfoTimeoutClear": cfReadInfoTimeoutClear,
       "cfLatencyExceededClear": cfLatencyExceededClear,
       "sslPeeringSCEPAutoReenrollClear": sslPeeringSCEPAutoReenrollClear,
       "crlClear": crlClear,
       "datastoreSyncFailureClear": datastoreSyncFailureClear,
       "secureVaultClear": secureVaultClear,
       "diskErrorClear": diskErrorClear,
       "admissionCpuErrorClear": admissionCpuErrorClear,
       "admissionTcpErrorClear": admissionTcpErrorClear,
       "systemDiskFullErrorClear": systemDiskFullErrorClear,
       "domainJoinErrorClear": domainJoinErrorClear,
       "certsExpiringErrorClear": certsExpiringErrorClear,
       "licenseErrorClear": licenseErrorClear,
       "hardwareErrorClear": hardwareErrorClear,
       "sysdetailErrorClear": sysdetailErrorClear,
       "admissionMapiErrorClear": admissionMapiErrorClear,
       "neighborIncompatibilityClear": neighborIncompatibilityClear,
       "flashErrorClear": flashErrorClear,
       "lanWanLoopClear": lanWanLoopClear,
       "optimizationServiceStatusClear": optimizationServiceStatusClear,
       "upgradeFailureClear": upgradeFailureClear,
       "clusterDisconnectedSHAlertClear": clusterDisconnectedSHAlertClear,
       "smbAlertClear": smbAlertClear,
       "linkDuplexClear": linkDuplexClear,
       "linkIoErrorsClear": linkIoErrorsClear,
       "clusterIpv6IncompatiblePeerClear": clusterIpv6IncompatiblePeerClear,
       "pathSelectionPathDownClear": pathSelectionPathDownClear,
       "clusterNeighborIncompatibleClear": clusterNeighborIncompatibleClear,
       "pathSelectionPathProbingErrorClear": pathSelectionPathProbingErrorClear,
       "rspGeneralError": rspGeneralError,
       "rspServiceError": rspServiceError,
       "rspGeneralClear": rspGeneralClear,
       "rspServiceClear": rspServiceClear,
       "statistics": statistics,
       "cpuLoad": cpuLoad,
       "cpuLoad1": cpuLoad1,
       "cpuLoad5": cpuLoad5,
       "cpuLoad15": cpuLoad15,
       "cpuUtil1": cpuUtil1,
       "cpuIndivUtilTable": cpuIndivUtilTable,
       "cpuIndivUtilEntry": cpuIndivUtilEntry,
       "cpuIndivIndex": cpuIndivIndex,
       "cpuIndivId": cpuIndivId,
       "cpuIndivIdleTime": cpuIndivIdleTime,
       "cpuIndivSystemTime": cpuIndivSystemTime,
       "cpuIndivUserTime": cpuIndivUserTime,
       "connectionCounts": connectionCounts,
       "optimizedConnections": optimizedConnections,
       "passthroughConnections": passthroughConnections,
       "halfOpenedConnections": halfOpenedConnections,
       "halfClosedConnections": halfClosedConnections,
       "establishedConnections": establishedConnections,
       "activeConnections": activeConnections,
       "totalConnections": totalConnections,
       "bandwidth": bandwidth,
       "bandwidthAggregate": bandwidthAggregate,
       "bwAggInLan": bwAggInLan,
       "bwAggInWan": bwAggInWan,
       "bwAggOutLan": bwAggOutLan,
       "bwAggOutWan": bwAggOutWan,
       "bandwidthPerPort": bandwidthPerPort,
       "bwPortTable": bwPortTable,
       "bwPortEntry": bwPortEntry,
       "bwPortNumber": bwPortNumber,
       "bwPortInLan": bwPortInLan,
       "bwPortInWan": bwPortInWan,
       "bwPortOutLan": bwPortOutLan,
       "bwPortOutWan": bwPortOutWan,
       "bandwidthPassThrough": bandwidthPassThrough,
       "bwPassThroughIn": bwPassThroughIn,
       "bwPassThroughOut": bwPassThroughOut,
       "bwPassThroughTotal": bwPassThroughTotal,
       "datastore": datastore,
       "dsHitsTotal": dsHitsTotal,
       "dsMissTotal": dsMissTotal,
       "dsCostPerSegment": dsCostPerSegment,
       "dsAveDiskUtilization": dsAveDiskUtilization,
       "topTalkers": topTalkers,
       "ttTalkersTable": ttTalkersTable,
       "ttTalkersEntry": ttTalkersEntry,
       "ttTalkerId": ttTalkerId,
       "ttTalkerIp1": ttTalkerIp1,
       "ttTalkerPort1": ttTalkerPort1,
       "ttTalkerIp2": ttTalkerIp2,
       "ttTalkerPort2": ttTalkerPort2,
       "ttTalkerByteCount": ttTalkerByteCount,
       "ttSrcHostTable": ttSrcHostTable,
       "ttSrcHostEntry": ttSrcHostEntry,
       "ttSrcHostId": ttSrcHostId,
       "ttSrcHostIp": ttSrcHostIp,
       "ttSrcHostByteCount": ttSrcHostByteCount,
       "ttDestHostTable": ttDestHostTable,
       "ttDestHostEntry": ttDestHostEntry,
       "ttDestHostId": ttDestHostId,
       "ttDestHostIp": ttDestHostIp,
       "ttDestHostByteCount": ttDestHostByteCount,
       "ttAppPortTable": ttAppPortTable,
       "ttAppPortEntry": ttAppPortEntry,
       "ttAppPortId": ttAppPortId,
       "ttAppPort": ttAppPort,
       "ttAppPortByteCount": ttAppPortByteCount,
       "bandwidthHC": bandwidthHC,
       "bandwidthHCAggregate": bandwidthHCAggregate,
       "bwHCAggInLan": bwHCAggInLan,
       "bwHCAggInWan": bwHCAggInWan,
       "bwHCAggOutLan": bwHCAggOutLan,
       "bwAggHCOutWan": bwAggHCOutWan,
       "bandwidthHCPerPort": bandwidthHCPerPort,
       "bwHCPortTable": bwHCPortTable,
       "bwHCPortEntry": bwHCPortEntry,
       "bwHCPortNumber": bwHCPortNumber,
       "bwHCPortInLan": bwHCPortInLan,
       "bwHCPortInWan": bwHCPortInWan,
       "bwHCPortOutLan": bwHCPortOutLan,
       "bwHCPortOutWan": bwHCPortOutWan}
)
