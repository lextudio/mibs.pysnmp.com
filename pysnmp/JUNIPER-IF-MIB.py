# SNMP MIB module (JUNIPER-IF-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/JUNIPER-IF-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:13:06 2024
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

(CounterBasedGauge64,) = mibBuilder.importSymbols(
    "HCNUM-TC",
    "CounterBasedGauge64")

(ifEntry,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifEntry",
    "ifIndex")

(jnxMibs,) = mibBuilder.importSymbols(
    "JUNIPER-SMI",
    "jnxMibs")

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

ifJnx = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 3)
)
ifJnx.setRevisions(
        ("2011-05-10 00:00",
         "2011-09-22 00:00",
         "2007-06-05 00:00",
         "2002-10-31 00:00",
         "2001-06-21 00:00",
         "2001-03-15 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_IfJnxTable_Object = MibTable
ifJnxTable = _IfJnxTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 3, 1)
)
if mibBuilder.loadTexts:
    ifJnxTable.setStatus("current")
_IfJnxEntry_Object = MibTableRow
ifJnxEntry = _IfJnxEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 3, 1, 1)
)
if mibBuilder.loadTexts:
    ifJnxEntry.setStatus("current")
_IfIn1SecRate_Type = Gauge32
_IfIn1SecRate_Object = MibTableColumn
ifIn1SecRate = _IfIn1SecRate_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 3, 1, 1, 1),
    _IfIn1SecRate_Type()
)
ifIn1SecRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifIn1SecRate.setStatus("current")
_IfIn1SecOctets_Type = Gauge32
_IfIn1SecOctets_Object = MibTableColumn
ifIn1SecOctets = _IfIn1SecOctets_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 3, 1, 1, 2),
    _IfIn1SecOctets_Type()
)
ifIn1SecOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifIn1SecOctets.setStatus("current")
_IfIn1SecPkts_Type = Gauge32
_IfIn1SecPkts_Object = MibTableColumn
ifIn1SecPkts = _IfIn1SecPkts_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 3, 1, 1, 3),
    _IfIn1SecPkts_Type()
)
ifIn1SecPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifIn1SecPkts.setStatus("current")
_IfOut1SecRate_Type = Gauge32
_IfOut1SecRate_Object = MibTableColumn
ifOut1SecRate = _IfOut1SecRate_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 3, 1, 1, 4),
    _IfOut1SecRate_Type()
)
ifOut1SecRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifOut1SecRate.setStatus("current")
_IfOut1SecOctets_Type = Gauge32
_IfOut1SecOctets_Object = MibTableColumn
ifOut1SecOctets = _IfOut1SecOctets_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 3, 1, 1, 5),
    _IfOut1SecOctets_Type()
)
ifOut1SecOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifOut1SecOctets.setStatus("current")
_IfOut1SecPkts_Type = Gauge32
_IfOut1SecPkts_Object = MibTableColumn
ifOut1SecPkts = _IfOut1SecPkts_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 3, 1, 1, 6),
    _IfOut1SecPkts_Type()
)
ifOut1SecPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifOut1SecPkts.setStatus("current")
_IfHCIn1SecRate_Type = CounterBasedGauge64
_IfHCIn1SecRate_Object = MibTableColumn
ifHCIn1SecRate = _IfHCIn1SecRate_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 3, 1, 1, 7),
    _IfHCIn1SecRate_Type()
)
ifHCIn1SecRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifHCIn1SecRate.setStatus("current")
_IfHCOut1SecRate_Type = CounterBasedGauge64
_IfHCOut1SecRate_Object = MibTableColumn
ifHCOut1SecRate = _IfHCOut1SecRate_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 3, 1, 1, 8),
    _IfHCOut1SecRate_Type()
)
ifHCOut1SecRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifHCOut1SecRate.setStatus("current")
_IfJnxInErrors_Type = Counter64
_IfJnxInErrors_Object = MibTableColumn
ifJnxInErrors = _IfJnxInErrors_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 3, 1, 1, 9),
    _IfJnxInErrors_Type()
)
ifJnxInErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifJnxInErrors.setStatus("current")
_IfJnxInFrameErrors_Type = Counter64
_IfJnxInFrameErrors_Object = MibTableColumn
ifJnxInFrameErrors = _IfJnxInFrameErrors_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 3, 1, 1, 10),
    _IfJnxInFrameErrors_Type()
)
ifJnxInFrameErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifJnxInFrameErrors.setStatus("current")
_IfJnxInQDrops_Type = Counter64
_IfJnxInQDrops_Object = MibTableColumn
ifJnxInQDrops = _IfJnxInQDrops_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 3, 1, 1, 11),
    _IfJnxInQDrops_Type()
)
ifJnxInQDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifJnxInQDrops.setStatus("current")
_IfJnxInRunts_Type = Counter64
_IfJnxInRunts_Object = MibTableColumn
ifJnxInRunts = _IfJnxInRunts_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 3, 1, 1, 12),
    _IfJnxInRunts_Type()
)
ifJnxInRunts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifJnxInRunts.setStatus("current")
_IfJnxInGiants_Type = Counter64
_IfJnxInGiants_Object = MibTableColumn
ifJnxInGiants = _IfJnxInGiants_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 3, 1, 1, 13),
    _IfJnxInGiants_Type()
)
ifJnxInGiants.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifJnxInGiants.setStatus("current")
_IfJnxInDiscards_Type = Counter64
_IfJnxInDiscards_Object = MibTableColumn
ifJnxInDiscards = _IfJnxInDiscards_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 3, 1, 1, 14),
    _IfJnxInDiscards_Type()
)
ifJnxInDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifJnxInDiscards.setStatus("current")
_IfJnxInHslCrcErrors_Type = Counter64
_IfJnxInHslCrcErrors_Object = MibTableColumn
ifJnxInHslCrcErrors = _IfJnxInHslCrcErrors_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 3, 1, 1, 15),
    _IfJnxInHslCrcErrors_Type()
)
ifJnxInHslCrcErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifJnxInHslCrcErrors.setStatus("current")
_IfJnxInHslFifoOverFlows_Type = Counter64
_IfJnxInHslFifoOverFlows_Object = MibTableColumn
ifJnxInHslFifoOverFlows = _IfJnxInHslFifoOverFlows_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 3, 1, 1, 16),
    _IfJnxInHslFifoOverFlows_Type()
)
ifJnxInHslFifoOverFlows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifJnxInHslFifoOverFlows.setStatus("current")
_IfJnxInL3Incompletes_Type = Counter64
_IfJnxInL3Incompletes_Object = MibTableColumn
ifJnxInL3Incompletes = _IfJnxInL3Incompletes_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 3, 1, 1, 17),
    _IfJnxInL3Incompletes_Type()
)
ifJnxInL3Incompletes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifJnxInL3Incompletes.setStatus("current")
_IfJnxInL2ChanErrors_Type = Counter64
_IfJnxInL2ChanErrors_Object = MibTableColumn
ifJnxInL2ChanErrors = _IfJnxInL2ChanErrors_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 3, 1, 1, 18),
    _IfJnxInL2ChanErrors_Type()
)
ifJnxInL2ChanErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifJnxInL2ChanErrors.setStatus("current")
_IfJnxInL2MismatchTimeouts_Type = Counter64
_IfJnxInL2MismatchTimeouts_Object = MibTableColumn
ifJnxInL2MismatchTimeouts = _IfJnxInL2MismatchTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 3, 1, 1, 19),
    _IfJnxInL2MismatchTimeouts_Type()
)
ifJnxInL2MismatchTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifJnxInL2MismatchTimeouts.setStatus("current")
_IfJnxInInvalidVCs_Type = Counter64
_IfJnxInInvalidVCs_Object = MibTableColumn
ifJnxInInvalidVCs = _IfJnxInInvalidVCs_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 3, 1, 1, 20),
    _IfJnxInInvalidVCs_Type()
)
ifJnxInInvalidVCs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifJnxInInvalidVCs.setStatus("current")
_IfJnxInFifoErrors_Type = Counter32
_IfJnxInFifoErrors_Object = MibTableColumn
ifJnxInFifoErrors = _IfJnxInFifoErrors_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 3, 1, 1, 21),
    _IfJnxInFifoErrors_Type()
)
ifJnxInFifoErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifJnxInFifoErrors.setStatus("current")
_IfJnxBucketDrops_Type = Counter64
_IfJnxBucketDrops_Object = MibTableColumn
ifJnxBucketDrops = _IfJnxBucketDrops_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 3, 1, 1, 22),
    _IfJnxBucketDrops_Type()
)
ifJnxBucketDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifJnxBucketDrops.setStatus("current")
_IfJnxSramErrors_Type = Counter32
_IfJnxSramErrors_Object = MibTableColumn
ifJnxSramErrors = _IfJnxSramErrors_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 3, 1, 1, 23),
    _IfJnxSramErrors_Type()
)
ifJnxSramErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifJnxSramErrors.setStatus("current")
_IfJnxOutErrors_Type = Counter64
_IfJnxOutErrors_Object = MibTableColumn
ifJnxOutErrors = _IfJnxOutErrors_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 3, 1, 1, 24),
    _IfJnxOutErrors_Type()
)
ifJnxOutErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifJnxOutErrors.setStatus("current")
_IfJnxCollisions_Type = Counter64
_IfJnxCollisions_Object = MibTableColumn
ifJnxCollisions = _IfJnxCollisions_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 3, 1, 1, 25),
    _IfJnxCollisions_Type()
)
ifJnxCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifJnxCollisions.setStatus("current")
_IfJnxCarrierTrans_Type = Counter64
_IfJnxCarrierTrans_Object = MibTableColumn
ifJnxCarrierTrans = _IfJnxCarrierTrans_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 3, 1, 1, 26),
    _IfJnxCarrierTrans_Type()
)
ifJnxCarrierTrans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifJnxCarrierTrans.setStatus("current")
_IfJnxOutQDrops_Type = Counter64
_IfJnxOutQDrops_Object = MibTableColumn
ifJnxOutQDrops = _IfJnxOutQDrops_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 3, 1, 1, 27),
    _IfJnxOutQDrops_Type()
)
ifJnxOutQDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifJnxOutQDrops.setStatus("current")
_IfJnxOutAgedErrors_Type = Counter64
_IfJnxOutAgedErrors_Object = MibTableColumn
ifJnxOutAgedErrors = _IfJnxOutAgedErrors_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 3, 1, 1, 28),
    _IfJnxOutAgedErrors_Type()
)
ifJnxOutAgedErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifJnxOutAgedErrors.setStatus("current")
_IfJnxOutFifoErrors_Type = Counter32
_IfJnxOutFifoErrors_Object = MibTableColumn
ifJnxOutFifoErrors = _IfJnxOutFifoErrors_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 3, 1, 1, 29),
    _IfJnxOutFifoErrors_Type()
)
ifJnxOutFifoErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifJnxOutFifoErrors.setStatus("current")
_IfJnxOutHslFifoUnderFlows_Type = Counter64
_IfJnxOutHslFifoUnderFlows_Object = MibTableColumn
ifJnxOutHslFifoUnderFlows = _IfJnxOutHslFifoUnderFlows_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 3, 1, 1, 30),
    _IfJnxOutHslFifoUnderFlows_Type()
)
ifJnxOutHslFifoUnderFlows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifJnxOutHslFifoUnderFlows.setStatus("current")
_IfJnxOutHslCrcErrors_Type = Counter32
_IfJnxOutHslCrcErrors_Object = MibTableColumn
ifJnxOutHslCrcErrors = _IfJnxOutHslCrcErrors_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 3, 1, 1, 31),
    _IfJnxOutHslCrcErrors_Type()
)
ifJnxOutHslCrcErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifJnxOutHslCrcErrors.setStatus("current")
_IfJnxCrcErrors_Type = Counter64
_IfJnxCrcErrors_Object = MibTableColumn
ifJnxCrcErrors = _IfJnxCrcErrors_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 3, 1, 1, 32),
    _IfJnxCrcErrors_Type()
)
ifJnxCrcErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifJnxCrcErrors.setStatus("current")
_IfJnxFcsErrors_Type = Counter64
_IfJnxFcsErrors_Object = MibTableColumn
ifJnxFcsErrors = _IfJnxFcsErrors_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 3, 1, 1, 33),
    _IfJnxFcsErrors_Type()
)
ifJnxFcsErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifJnxFcsErrors.setStatus("current")
_IfChassisTable_Object = MibTable
ifChassisTable = _IfChassisTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 3, 2)
)
if mibBuilder.loadTexts:
    ifChassisTable.setStatus("current")
_IfChassisEntry_Object = MibTableRow
ifChassisEntry = _IfChassisEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 3, 2, 1)
)
if mibBuilder.loadTexts:
    ifChassisEntry.setStatus("current")
_IfChassisFpc_Type = Integer32
_IfChassisFpc_Object = MibTableColumn
ifChassisFpc = _IfChassisFpc_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 3, 2, 1, 1),
    _IfChassisFpc_Type()
)
ifChassisFpc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifChassisFpc.setStatus("current")
_IfChassisPic_Type = Integer32
_IfChassisPic_Object = MibTableColumn
ifChassisPic = _IfChassisPic_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 3, 2, 1, 2),
    _IfChassisPic_Type()
)
ifChassisPic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifChassisPic.setStatus("current")
_IfChassisPort_Type = Integer32
_IfChassisPort_Object = MibTableColumn
ifChassisPort = _IfChassisPort_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 3, 2, 1, 3),
    _IfChassisPort_Type()
)
ifChassisPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifChassisPort.setStatus("current")
_IfChassisChannel_Type = Integer32
_IfChassisChannel_Object = MibTableColumn
ifChassisChannel = _IfChassisChannel_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 3, 2, 1, 4),
    _IfChassisChannel_Type()
)
ifChassisChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifChassisChannel.setStatus("current")
_IfChassisLogicalUnit_Type = Integer32
_IfChassisLogicalUnit_Object = MibTableColumn
ifChassisLogicalUnit = _IfChassisLogicalUnit_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 3, 2, 1, 5),
    _IfChassisLogicalUnit_Type()
)
ifChassisLogicalUnit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifChassisLogicalUnit.setStatus("current")
_IfChassisPicIndex_Type = OctetString
_IfChassisPicIndex_Object = MibTableColumn
ifChassisPicIndex = _IfChassisPicIndex_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 3, 2, 1, 6),
    _IfChassisPicIndex_Type()
)
ifChassisPicIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifChassisPicIndex.setStatus("current")
_IfJnxNotification_ObjectIdentity = ObjectIdentity
ifJnxNotification = _IfJnxNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 3, 3)
)
_IfJnxNotificationPrefix_ObjectIdentity = ObjectIdentity
ifJnxNotificationPrefix = _IfJnxNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 3, 3, 0)
)
_IfJnxPolTable_Object = MibTable
ifJnxPolTable = _IfJnxPolTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 3, 4)
)
if mibBuilder.loadTexts:
    ifJnxPolTable.setStatus("current")
_IfJnxPolEntry_Object = MibTableRow
ifJnxPolEntry = _IfJnxPolEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 3, 4, 1)
)
ifJnxPolEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    ifJnxPolEntry.setStatus("current")
_IfJnxInPolLowOctets_Type = Counter64
_IfJnxInPolLowOctets_Object = MibTableColumn
ifJnxInPolLowOctets = _IfJnxInPolLowOctets_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 3, 4, 1, 1),
    _IfJnxInPolLowOctets_Type()
)
ifJnxInPolLowOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifJnxInPolLowOctets.setStatus("current")
_IfJnxInPolLowPkts_Type = Counter64
_IfJnxInPolLowPkts_Object = MibTableColumn
ifJnxInPolLowPkts = _IfJnxInPolLowPkts_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 3, 4, 1, 2),
    _IfJnxInPolLowPkts_Type()
)
ifJnxInPolLowPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifJnxInPolLowPkts.setStatus("current")
_IfJnxInPolLow1SecRate_Type = Counter64
_IfJnxInPolLow1SecRate_Object = MibTableColumn
ifJnxInPolLow1SecRate = _IfJnxInPolLow1SecRate_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 3, 4, 1, 3),
    _IfJnxInPolLow1SecRate_Type()
)
ifJnxInPolLow1SecRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifJnxInPolLow1SecRate.setStatus("current")
_IfJnxInPolMLowOctets_Type = Counter64
_IfJnxInPolMLowOctets_Object = MibTableColumn
ifJnxInPolMLowOctets = _IfJnxInPolMLowOctets_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 3, 4, 1, 4),
    _IfJnxInPolMLowOctets_Type()
)
ifJnxInPolMLowOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifJnxInPolMLowOctets.setStatus("current")
_IfJnxInPolMLowPkts_Type = Counter64
_IfJnxInPolMLowPkts_Object = MibTableColumn
ifJnxInPolMLowPkts = _IfJnxInPolMLowPkts_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 3, 4, 1, 5),
    _IfJnxInPolMLowPkts_Type()
)
ifJnxInPolMLowPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifJnxInPolMLowPkts.setStatus("current")
_IfJnxInPolMLow1SecRate_Type = Counter64
_IfJnxInPolMLow1SecRate_Object = MibTableColumn
ifJnxInPolMLow1SecRate = _IfJnxInPolMLow1SecRate_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 3, 4, 1, 6),
    _IfJnxInPolMLow1SecRate_Type()
)
ifJnxInPolMLow1SecRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifJnxInPolMLow1SecRate.setStatus("current")
_IfJnxInPolMHighOctets_Type = Counter64
_IfJnxInPolMHighOctets_Object = MibTableColumn
ifJnxInPolMHighOctets = _IfJnxInPolMHighOctets_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 3, 4, 1, 7),
    _IfJnxInPolMHighOctets_Type()
)
ifJnxInPolMHighOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifJnxInPolMHighOctets.setStatus("current")
_IfJnxInPolMHighPkts_Type = Counter64
_IfJnxInPolMHighPkts_Object = MibTableColumn
ifJnxInPolMHighPkts = _IfJnxInPolMHighPkts_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 3, 4, 1, 8),
    _IfJnxInPolMHighPkts_Type()
)
ifJnxInPolMHighPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifJnxInPolMHighPkts.setStatus("current")
_IfJnxInPolMHigh1SecRate_Type = Counter64
_IfJnxInPolMHigh1SecRate_Object = MibTableColumn
ifJnxInPolMHigh1SecRate = _IfJnxInPolMHigh1SecRate_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 3, 4, 1, 9),
    _IfJnxInPolMHigh1SecRate_Type()
)
ifJnxInPolMHigh1SecRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifJnxInPolMHigh1SecRate.setStatus("current")
_IfJnxInPolHighOctets_Type = Counter64
_IfJnxInPolHighOctets_Object = MibTableColumn
ifJnxInPolHighOctets = _IfJnxInPolHighOctets_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 3, 4, 1, 10),
    _IfJnxInPolHighOctets_Type()
)
ifJnxInPolHighOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifJnxInPolHighOctets.setStatus("current")
_IfJnxInPolHighPkts_Type = Counter64
_IfJnxInPolHighPkts_Object = MibTableColumn
ifJnxInPolHighPkts = _IfJnxInPolHighPkts_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 3, 4, 1, 11),
    _IfJnxInPolHighPkts_Type()
)
ifJnxInPolHighPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifJnxInPolHighPkts.setStatus("current")
_IfJnxInPolHigh1SecRate_Type = Counter64
_IfJnxInPolHigh1SecRate_Object = MibTableColumn
ifJnxInPolHigh1SecRate = _IfJnxInPolHigh1SecRate_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 3, 4, 1, 12),
    _IfJnxInPolHigh1SecRate_Type()
)
ifJnxInPolHigh1SecRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifJnxInPolHigh1SecRate.setStatus("current")
_IfJnxInPolDropOctets_Type = Counter64
_IfJnxInPolDropOctets_Object = MibTableColumn
ifJnxInPolDropOctets = _IfJnxInPolDropOctets_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 3, 4, 1, 13),
    _IfJnxInPolDropOctets_Type()
)
ifJnxInPolDropOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifJnxInPolDropOctets.setStatus("current")
_IfJnxInPolDropPkts_Type = Counter64
_IfJnxInPolDropPkts_Object = MibTableColumn
ifJnxInPolDropPkts = _IfJnxInPolDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 3, 4, 1, 14),
    _IfJnxInPolDropPkts_Type()
)
ifJnxInPolDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifJnxInPolDropPkts.setStatus("current")
_IfJnxInPolDrop1SecRate_Type = Counter64
_IfJnxInPolDrop1SecRate_Object = MibTableColumn
ifJnxInPolDrop1SecRate = _IfJnxInPolDrop1SecRate_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 3, 4, 1, 15),
    _IfJnxInPolDrop1SecRate_Type()
)
ifJnxInPolDrop1SecRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifJnxInPolDrop1SecRate.setStatus("current")
_IfJnxOutPolLowOctets_Type = Counter64
_IfJnxOutPolLowOctets_Object = MibTableColumn
ifJnxOutPolLowOctets = _IfJnxOutPolLowOctets_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 3, 4, 1, 16),
    _IfJnxOutPolLowOctets_Type()
)
ifJnxOutPolLowOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifJnxOutPolLowOctets.setStatus("current")
_IfJnxOutPolLowPkts_Type = Counter64
_IfJnxOutPolLowPkts_Object = MibTableColumn
ifJnxOutPolLowPkts = _IfJnxOutPolLowPkts_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 3, 4, 1, 17),
    _IfJnxOutPolLowPkts_Type()
)
ifJnxOutPolLowPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifJnxOutPolLowPkts.setStatus("current")
_IfJnxOutPolLow1SecRate_Type = Counter64
_IfJnxOutPolLow1SecRate_Object = MibTableColumn
ifJnxOutPolLow1SecRate = _IfJnxOutPolLow1SecRate_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 3, 4, 1, 18),
    _IfJnxOutPolLow1SecRate_Type()
)
ifJnxOutPolLow1SecRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifJnxOutPolLow1SecRate.setStatus("current")
_IfJnxOutPolMLowOctets_Type = Counter64
_IfJnxOutPolMLowOctets_Object = MibTableColumn
ifJnxOutPolMLowOctets = _IfJnxOutPolMLowOctets_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 3, 4, 1, 19),
    _IfJnxOutPolMLowOctets_Type()
)
ifJnxOutPolMLowOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifJnxOutPolMLowOctets.setStatus("current")
_IfJnxOutPolMLowPkts_Type = Counter64
_IfJnxOutPolMLowPkts_Object = MibTableColumn
ifJnxOutPolMLowPkts = _IfJnxOutPolMLowPkts_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 3, 4, 1, 20),
    _IfJnxOutPolMLowPkts_Type()
)
ifJnxOutPolMLowPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifJnxOutPolMLowPkts.setStatus("current")
_IfJnxOutPolMLow1SecRate_Type = Counter64
_IfJnxOutPolMLow1SecRate_Object = MibTableColumn
ifJnxOutPolMLow1SecRate = _IfJnxOutPolMLow1SecRate_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 3, 4, 1, 21),
    _IfJnxOutPolMLow1SecRate_Type()
)
ifJnxOutPolMLow1SecRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifJnxOutPolMLow1SecRate.setStatus("current")
_IfJnxOutPolMHighOctets_Type = Counter64
_IfJnxOutPolMHighOctets_Object = MibTableColumn
ifJnxOutPolMHighOctets = _IfJnxOutPolMHighOctets_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 3, 4, 1, 22),
    _IfJnxOutPolMHighOctets_Type()
)
ifJnxOutPolMHighOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifJnxOutPolMHighOctets.setStatus("current")
_IfJnxOutPolMHighPkts_Type = Counter64
_IfJnxOutPolMHighPkts_Object = MibTableColumn
ifJnxOutPolMHighPkts = _IfJnxOutPolMHighPkts_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 3, 4, 1, 23),
    _IfJnxOutPolMHighPkts_Type()
)
ifJnxOutPolMHighPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifJnxOutPolMHighPkts.setStatus("current")
_IfJnxOutPolMHigh1SecRate_Type = Counter64
_IfJnxOutPolMHigh1SecRate_Object = MibTableColumn
ifJnxOutPolMHigh1SecRate = _IfJnxOutPolMHigh1SecRate_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 3, 4, 1, 24),
    _IfJnxOutPolMHigh1SecRate_Type()
)
ifJnxOutPolMHigh1SecRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifJnxOutPolMHigh1SecRate.setStatus("current")
_IfJnxOutPolHighOctets_Type = Counter64
_IfJnxOutPolHighOctets_Object = MibTableColumn
ifJnxOutPolHighOctets = _IfJnxOutPolHighOctets_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 3, 4, 1, 25),
    _IfJnxOutPolHighOctets_Type()
)
ifJnxOutPolHighOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifJnxOutPolHighOctets.setStatus("current")
_IfJnxOutPolHighPkts_Type = Counter64
_IfJnxOutPolHighPkts_Object = MibTableColumn
ifJnxOutPolHighPkts = _IfJnxOutPolHighPkts_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 3, 4, 1, 26),
    _IfJnxOutPolHighPkts_Type()
)
ifJnxOutPolHighPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifJnxOutPolHighPkts.setStatus("current")
_IfJnxOutPolHigh1SecRate_Type = Counter64
_IfJnxOutPolHigh1SecRate_Object = MibTableColumn
ifJnxOutPolHigh1SecRate = _IfJnxOutPolHigh1SecRate_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 3, 4, 1, 27),
    _IfJnxOutPolHigh1SecRate_Type()
)
ifJnxOutPolHigh1SecRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifJnxOutPolHigh1SecRate.setStatus("current")
_IfJnxOutPolDropOctets_Type = Counter64
_IfJnxOutPolDropOctets_Object = MibTableColumn
ifJnxOutPolDropOctets = _IfJnxOutPolDropOctets_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 3, 4, 1, 28),
    _IfJnxOutPolDropOctets_Type()
)
ifJnxOutPolDropOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifJnxOutPolDropOctets.setStatus("current")
_IfJnxOutPolDropPkts_Type = Counter64
_IfJnxOutPolDropPkts_Object = MibTableColumn
ifJnxOutPolDropPkts = _IfJnxOutPolDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 3, 4, 1, 29),
    _IfJnxOutPolDropPkts_Type()
)
ifJnxOutPolDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifJnxOutPolDropPkts.setStatus("current")
_IfJnxOutPolDrop1SecRate_Type = Counter64
_IfJnxOutPolDrop1SecRate_Object = MibTableColumn
ifJnxOutPolDrop1SecRate = _IfJnxOutPolDrop1SecRate_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 3, 4, 1, 30),
    _IfJnxOutPolDrop1SecRate_Type()
)
ifJnxOutPolDrop1SecRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifJnxOutPolDrop1SecRate.setStatus("current")
ifEntry.registerAugmentions(
    ("JUNIPER-IF-MIB",
     "ifJnxEntry")
)
ifJnxEntry.setIndexNames(*ifEntry.getIndexNames())
ifEntry.registerAugmentions(
    ("JUNIPER-IF-MIB",
     "ifChassisEntry")
)
ifChassisEntry.setIndexNames(*ifEntry.getIndexNames())

# Managed Objects groups


# Notification objects

ifJnxErrors = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 3, 3, 0, 1)
)
ifJnxErrors.setObjects(
      *(("JUNIPER-IF-MIB", "ifJnxCrcErrors"),
        ("JUNIPER-IF-MIB", "ifJnxFcsErrors"))
)
if mibBuilder.loadTexts:
    ifJnxErrors.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "JUNIPER-IF-MIB",
    **{"ifJnx": ifJnx,
       "ifJnxTable": ifJnxTable,
       "ifJnxEntry": ifJnxEntry,
       "ifIn1SecRate": ifIn1SecRate,
       "ifIn1SecOctets": ifIn1SecOctets,
       "ifIn1SecPkts": ifIn1SecPkts,
       "ifOut1SecRate": ifOut1SecRate,
       "ifOut1SecOctets": ifOut1SecOctets,
       "ifOut1SecPkts": ifOut1SecPkts,
       "ifHCIn1SecRate": ifHCIn1SecRate,
       "ifHCOut1SecRate": ifHCOut1SecRate,
       "ifJnxInErrors": ifJnxInErrors,
       "ifJnxInFrameErrors": ifJnxInFrameErrors,
       "ifJnxInQDrops": ifJnxInQDrops,
       "ifJnxInRunts": ifJnxInRunts,
       "ifJnxInGiants": ifJnxInGiants,
       "ifJnxInDiscards": ifJnxInDiscards,
       "ifJnxInHslCrcErrors": ifJnxInHslCrcErrors,
       "ifJnxInHslFifoOverFlows": ifJnxInHslFifoOverFlows,
       "ifJnxInL3Incompletes": ifJnxInL3Incompletes,
       "ifJnxInL2ChanErrors": ifJnxInL2ChanErrors,
       "ifJnxInL2MismatchTimeouts": ifJnxInL2MismatchTimeouts,
       "ifJnxInInvalidVCs": ifJnxInInvalidVCs,
       "ifJnxInFifoErrors": ifJnxInFifoErrors,
       "ifJnxBucketDrops": ifJnxBucketDrops,
       "ifJnxSramErrors": ifJnxSramErrors,
       "ifJnxOutErrors": ifJnxOutErrors,
       "ifJnxCollisions": ifJnxCollisions,
       "ifJnxCarrierTrans": ifJnxCarrierTrans,
       "ifJnxOutQDrops": ifJnxOutQDrops,
       "ifJnxOutAgedErrors": ifJnxOutAgedErrors,
       "ifJnxOutFifoErrors": ifJnxOutFifoErrors,
       "ifJnxOutHslFifoUnderFlows": ifJnxOutHslFifoUnderFlows,
       "ifJnxOutHslCrcErrors": ifJnxOutHslCrcErrors,
       "ifJnxCrcErrors": ifJnxCrcErrors,
       "ifJnxFcsErrors": ifJnxFcsErrors,
       "ifChassisTable": ifChassisTable,
       "ifChassisEntry": ifChassisEntry,
       "ifChassisFpc": ifChassisFpc,
       "ifChassisPic": ifChassisPic,
       "ifChassisPort": ifChassisPort,
       "ifChassisChannel": ifChassisChannel,
       "ifChassisLogicalUnit": ifChassisLogicalUnit,
       "ifChassisPicIndex": ifChassisPicIndex,
       "ifJnxNotification": ifJnxNotification,
       "ifJnxNotificationPrefix": ifJnxNotificationPrefix,
       "ifJnxErrors": ifJnxErrors,
       "ifJnxPolTable": ifJnxPolTable,
       "ifJnxPolEntry": ifJnxPolEntry,
       "ifJnxInPolLowOctets": ifJnxInPolLowOctets,
       "ifJnxInPolLowPkts": ifJnxInPolLowPkts,
       "ifJnxInPolLow1SecRate": ifJnxInPolLow1SecRate,
       "ifJnxInPolMLowOctets": ifJnxInPolMLowOctets,
       "ifJnxInPolMLowPkts": ifJnxInPolMLowPkts,
       "ifJnxInPolMLow1SecRate": ifJnxInPolMLow1SecRate,
       "ifJnxInPolMHighOctets": ifJnxInPolMHighOctets,
       "ifJnxInPolMHighPkts": ifJnxInPolMHighPkts,
       "ifJnxInPolMHigh1SecRate": ifJnxInPolMHigh1SecRate,
       "ifJnxInPolHighOctets": ifJnxInPolHighOctets,
       "ifJnxInPolHighPkts": ifJnxInPolHighPkts,
       "ifJnxInPolHigh1SecRate": ifJnxInPolHigh1SecRate,
       "ifJnxInPolDropOctets": ifJnxInPolDropOctets,
       "ifJnxInPolDropPkts": ifJnxInPolDropPkts,
       "ifJnxInPolDrop1SecRate": ifJnxInPolDrop1SecRate,
       "ifJnxOutPolLowOctets": ifJnxOutPolLowOctets,
       "ifJnxOutPolLowPkts": ifJnxOutPolLowPkts,
       "ifJnxOutPolLow1SecRate": ifJnxOutPolLow1SecRate,
       "ifJnxOutPolMLowOctets": ifJnxOutPolMLowOctets,
       "ifJnxOutPolMLowPkts": ifJnxOutPolMLowPkts,
       "ifJnxOutPolMLow1SecRate": ifJnxOutPolMLow1SecRate,
       "ifJnxOutPolMHighOctets": ifJnxOutPolMHighOctets,
       "ifJnxOutPolMHighPkts": ifJnxOutPolMHighPkts,
       "ifJnxOutPolMHigh1SecRate": ifJnxOutPolMHigh1SecRate,
       "ifJnxOutPolHighOctets": ifJnxOutPolHighOctets,
       "ifJnxOutPolHighPkts": ifJnxOutPolHighPkts,
       "ifJnxOutPolHigh1SecRate": ifJnxOutPolHigh1SecRate,
       "ifJnxOutPolDropOctets": ifJnxOutPolDropOctets,
       "ifJnxOutPolDropPkts": ifJnxOutPolDropPkts,
       "ifJnxOutPolDrop1SecRate": ifJnxOutPolDrop1SecRate}
)
