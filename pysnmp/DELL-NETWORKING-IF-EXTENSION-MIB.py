# SNMP MIB module (DELL-NETWORKING-IF-EXTENSION-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/DELL-NETWORKING-IF-EXTENSION-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:23:55 2024
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

(dellNetMgmt,) = mibBuilder.importSymbols(
    "DELL-NETWORKING-SMI",
    "dellNetMgmt")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

dellNetIfExtensionMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 3, 11)
)
dellNetIfExtensionMib.setRevisions(
        ("2014-08-12 12:00",
         "2012-03-06 12:00",
         "2010-08-11 12:00",
         "2010-08-10 12:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_DellNetIfExtensionMibObject_ObjectIdentity = ObjectIdentity
dellNetIfExtensionMibObject = _DellNetIfExtensionMibObject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 3, 11, 1)
)
_DellNetIfExtensionParams_ObjectIdentity = ObjectIdentity
dellNetIfExtensionParams = _DellNetIfExtensionParams_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 3, 11, 1, 1)
)
_DellNetIfTable_Object = MibTable
dellNetIfTable = _DellNetIfTable_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 11, 1, 1, 1)
)
if mibBuilder.loadTexts:
    dellNetIfTable.setStatus("current")
_DellNetIfEntry_Object = MibTableRow
dellNetIfEntry = _DellNetIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 11, 1, 1, 1, 1)
)
dellNetIfEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    dellNetIfEntry.setStatus("current")


class _DellNetIfIpMtu_Type(Unsigned32):
    """Custom type dellNetIfIpMtu based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(594, 9252),
    )


_DellNetIfIpMtu_Type.__name__ = "Unsigned32"
_DellNetIfIpMtu_Object = MibTableColumn
dellNetIfIpMtu = _DellNetIfIpMtu_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 11, 1, 1, 1, 1, 1),
    _DellNetIfIpMtu_Type()
)
dellNetIfIpMtu.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dellNetIfIpMtu.setStatus("current")


class _DellNetIfDuplexMode_Type(Integer32):
    """Custom type dellNetIfDuplexMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("auto", 3),
          ("full", 2),
          ("half", 1))
    )


_DellNetIfDuplexMode_Type.__name__ = "Integer32"
_DellNetIfDuplexMode_Object = MibTableColumn
dellNetIfDuplexMode = _DellNetIfDuplexMode_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 11, 1, 1, 1, 1, 2),
    _DellNetIfDuplexMode_Type()
)
dellNetIfDuplexMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dellNetIfDuplexMode.setStatus("current")


class _DellNetIfQueueingStrategy_Type(DisplayString):
    """Custom type dellNetIfQueueingStrategy based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_DellNetIfQueueingStrategy_Type.__name__ = "DisplayString"
_DellNetIfQueueingStrategy_Object = MibTableColumn
dellNetIfQueueingStrategy = _DellNetIfQueueingStrategy_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 11, 1, 1, 1, 1, 3),
    _DellNetIfQueueingStrategy_Type()
)
dellNetIfQueueingStrategy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetIfQueueingStrategy.setStatus("current")
_DellNetIfRxFlowCtrl_Type = TruthValue
_DellNetIfRxFlowCtrl_Object = MibTableColumn
dellNetIfRxFlowCtrl = _DellNetIfRxFlowCtrl_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 11, 1, 1, 1, 1, 4),
    _DellNetIfRxFlowCtrl_Type()
)
dellNetIfRxFlowCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dellNetIfRxFlowCtrl.setStatus("current")
_DellNetIfTxFlowCtrl_Type = TruthValue
_DellNetIfTxFlowCtrl_Object = MibTableColumn
dellNetIfTxFlowCtrl = _DellNetIfTxFlowCtrl_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 11, 1, 1, 1, 1, 5),
    _DellNetIfTxFlowCtrl_Type()
)
dellNetIfTxFlowCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dellNetIfTxFlowCtrl.setStatus("current")


class _DellNetIfDescr_Type(OctetString):
    """Custom type dellNetIfDescr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 241),
    )


_DellNetIfDescr_Type.__name__ = "OctetString"
_DellNetIfDescr_Object = MibTableColumn
dellNetIfDescr = _DellNetIfDescr_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 11, 1, 1, 1, 1, 6),
    _DellNetIfDescr_Type()
)
dellNetIfDescr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dellNetIfDescr.setStatus("current")


class _DellNetIfAdminStatus_Type(Integer32):
    """Custom type dellNetIfAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_DellNetIfAdminStatus_Type.__name__ = "Integer32"
_DellNetIfAdminStatus_Object = MibTableColumn
dellNetIfAdminStatus = _DellNetIfAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 11, 1, 1, 1, 1, 7),
    _DellNetIfAdminStatus_Type()
)
dellNetIfAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dellNetIfAdminStatus.setStatus("current")


class _DellNetIfRateInterval_Type(Unsigned32):
    """Custom type dellNetIfRateInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30, 299),
    )


_DellNetIfRateInterval_Type.__name__ = "Unsigned32"
_DellNetIfRateInterval_Object = MibTableColumn
dellNetIfRateInterval = _DellNetIfRateInterval_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 11, 1, 1, 1, 1, 8),
    _DellNetIfRateInterval_Type()
)
dellNetIfRateInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dellNetIfRateInterval.setStatus("current")


class _DellNetIfSpeed_Type(Integer32):
    """Custom type dellNetIfSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              10,
              100,
              1000)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("hundredMbps", 100),
          ("tenMbps", 10),
          ("thousandMbps", 1000))
    )


_DellNetIfSpeed_Type.__name__ = "Integer32"
_DellNetIfSpeed_Object = MibTableColumn
dellNetIfSpeed = _DellNetIfSpeed_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 11, 1, 1, 1, 1, 9),
    _DellNetIfSpeed_Type()
)
dellNetIfSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dellNetIfSpeed.setStatus("current")
_DellNetIfPortListBitPos_Type = Integer32
_DellNetIfPortListBitPos_Object = MibTableColumn
dellNetIfPortListBitPos = _DellNetIfPortListBitPos_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 11, 1, 1, 1, 1, 10),
    _DellNetIfPortListBitPos_Type()
)
dellNetIfPortListBitPos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetIfPortListBitPos.setStatus("current")
_DellNetIfExtensionStats_ObjectIdentity = ObjectIdentity
dellNetIfExtensionStats = _DellNetIfExtensionStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 3, 11, 1, 2)
)
_DellNetIfStaticsTable_Object = MibTable
dellNetIfStaticsTable = _DellNetIfStaticsTable_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 11, 1, 2, 1)
)
if mibBuilder.loadTexts:
    dellNetIfStaticsTable.setStatus("current")
_DellNetIfStaticsEntry_Object = MibTableRow
dellNetIfStaticsEntry = _DellNetIfStaticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 11, 1, 2, 1, 1)
)
dellNetIfStaticsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    dellNetIfStaticsEntry.setStatus("current")
_DellNetIfInVlanPkts_Type = Counter64
_DellNetIfInVlanPkts_Object = MibTableColumn
dellNetIfInVlanPkts = _DellNetIfInVlanPkts_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 11, 1, 2, 1, 1, 1),
    _DellNetIfInVlanPkts_Type()
)
dellNetIfInVlanPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetIfInVlanPkts.setStatus("current")
_DellNetIfIn64BytePkts_Type = Counter64
_DellNetIfIn64BytePkts_Object = MibTableColumn
dellNetIfIn64BytePkts = _DellNetIfIn64BytePkts_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 11, 1, 2, 1, 1, 2),
    _DellNetIfIn64BytePkts_Type()
)
dellNetIfIn64BytePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetIfIn64BytePkts.setStatus("current")
_DellNetifIn65To127BytePkts_Type = Counter64
_DellNetifIn65To127BytePkts_Object = MibTableColumn
dellNetifIn65To127BytePkts = _DellNetifIn65To127BytePkts_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 11, 1, 2, 1, 1, 3),
    _DellNetifIn65To127BytePkts_Type()
)
dellNetifIn65To127BytePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetifIn65To127BytePkts.setStatus("current")
_DellNetIfIn128To255BytePkts_Type = Counter64
_DellNetIfIn128To255BytePkts_Object = MibTableColumn
dellNetIfIn128To255BytePkts = _DellNetIfIn128To255BytePkts_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 11, 1, 2, 1, 1, 4),
    _DellNetIfIn128To255BytePkts_Type()
)
dellNetIfIn128To255BytePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetIfIn128To255BytePkts.setStatus("current")
_DellNetIfIn256To511BytePkts_Type = Counter64
_DellNetIfIn256To511BytePkts_Object = MibTableColumn
dellNetIfIn256To511BytePkts = _DellNetIfIn256To511BytePkts_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 11, 1, 2, 1, 1, 5),
    _DellNetIfIn256To511BytePkts_Type()
)
dellNetIfIn256To511BytePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetIfIn256To511BytePkts.setStatus("current")
_DellNetIfIn512To1023BytePkts_Type = Counter64
_DellNetIfIn512To1023BytePkts_Object = MibTableColumn
dellNetIfIn512To1023BytePkts = _DellNetIfIn512To1023BytePkts_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 11, 1, 2, 1, 1, 6),
    _DellNetIfIn512To1023BytePkts_Type()
)
dellNetIfIn512To1023BytePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetIfIn512To1023BytePkts.setStatus("current")
_DellNetIfInOver1023BytePkts_Type = Counter64
_DellNetIfInOver1023BytePkts_Object = MibTableColumn
dellNetIfInOver1023BytePkts = _DellNetIfInOver1023BytePkts_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 11, 1, 2, 1, 1, 7),
    _DellNetIfInOver1023BytePkts_Type()
)
dellNetIfInOver1023BytePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetIfInOver1023BytePkts.setStatus("current")
_DellNetIfInThrottles_Type = Counter64
_DellNetIfInThrottles_Object = MibTableColumn
dellNetIfInThrottles = _DellNetIfInThrottles_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 11, 1, 2, 1, 1, 8),
    _DellNetIfInThrottles_Type()
)
dellNetIfInThrottles.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetIfInThrottles.setStatus("current")
_DellNetIfInRunts_Type = Counter64
_DellNetIfInRunts_Object = MibTableColumn
dellNetIfInRunts = _DellNetIfInRunts_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 11, 1, 2, 1, 1, 9),
    _DellNetIfInRunts_Type()
)
dellNetIfInRunts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetIfInRunts.setStatus("current")
_DellNetIfInGiants_Type = Counter64
_DellNetIfInGiants_Object = MibTableColumn
dellNetIfInGiants = _DellNetIfInGiants_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 11, 1, 2, 1, 1, 10),
    _DellNetIfInGiants_Type()
)
dellNetIfInGiants.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetIfInGiants.setStatus("current")
_DellNetIfInCRC_Type = Counter64
_DellNetIfInCRC_Object = MibTableColumn
dellNetIfInCRC = _DellNetIfInCRC_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 11, 1, 2, 1, 1, 11),
    _DellNetIfInCRC_Type()
)
dellNetIfInCRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetIfInCRC.setStatus("current")
_DellNetIfInOverruns_Type = Counter64
_DellNetIfInOverruns_Object = MibTableColumn
dellNetIfInOverruns = _DellNetIfInOverruns_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 11, 1, 2, 1, 1, 12),
    _DellNetIfInOverruns_Type()
)
dellNetIfInOverruns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetIfInOverruns.setStatus("current")
_DellNetIfOutVlanPkts_Type = Counter64
_DellNetIfOutVlanPkts_Object = MibTableColumn
dellNetIfOutVlanPkts = _DellNetIfOutVlanPkts_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 11, 1, 2, 1, 1, 13),
    _DellNetIfOutVlanPkts_Type()
)
dellNetIfOutVlanPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetIfOutVlanPkts.setStatus("current")
_DellNetIfOutUnderruns_Type = Counter64
_DellNetIfOutUnderruns_Object = MibTableColumn
dellNetIfOutUnderruns = _DellNetIfOutUnderruns_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 11, 1, 2, 1, 1, 14),
    _DellNetIfOutUnderruns_Type()
)
dellNetIfOutUnderruns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetIfOutUnderruns.setStatus("current")
_DellNetIfOutUnicasts_Type = Counter64
_DellNetIfOutUnicasts_Object = MibTableColumn
dellNetIfOutUnicasts = _DellNetIfOutUnicasts_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 11, 1, 2, 1, 1, 15),
    _DellNetIfOutUnicasts_Type()
)
dellNetIfOutUnicasts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetIfOutUnicasts.setStatus("current")
_DellNetIfOutCollisions_Type = Counter64
_DellNetIfOutCollisions_Object = MibTableColumn
dellNetIfOutCollisions = _DellNetIfOutCollisions_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 11, 1, 2, 1, 1, 16),
    _DellNetIfOutCollisions_Type()
)
dellNetIfOutCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetIfOutCollisions.setStatus("current")
_DellNetIfOutWredDrops_Type = Counter64
_DellNetIfOutWredDrops_Object = MibTableColumn
dellNetIfOutWredDrops = _DellNetIfOutWredDrops_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 11, 1, 2, 1, 1, 17),
    _DellNetIfOutWredDrops_Type()
)
dellNetIfOutWredDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetIfOutWredDrops.setStatus("current")
_DellNetIfOut64BytePkts_Type = Counter64
_DellNetIfOut64BytePkts_Object = MibTableColumn
dellNetIfOut64BytePkts = _DellNetIfOut64BytePkts_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 11, 1, 2, 1, 1, 18),
    _DellNetIfOut64BytePkts_Type()
)
dellNetIfOut64BytePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetIfOut64BytePkts.setStatus("current")
_DellNetIfOut65To127BytePkts_Type = Counter64
_DellNetIfOut65To127BytePkts_Object = MibTableColumn
dellNetIfOut65To127BytePkts = _DellNetIfOut65To127BytePkts_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 11, 1, 2, 1, 1, 19),
    _DellNetIfOut65To127BytePkts_Type()
)
dellNetIfOut65To127BytePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetIfOut65To127BytePkts.setStatus("current")
_DellNetIfOut128To255BytePkts_Type = Counter64
_DellNetIfOut128To255BytePkts_Object = MibTableColumn
dellNetIfOut128To255BytePkts = _DellNetIfOut128To255BytePkts_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 11, 1, 2, 1, 1, 20),
    _DellNetIfOut128To255BytePkts_Type()
)
dellNetIfOut128To255BytePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetIfOut128To255BytePkts.setStatus("current")
_DellNetIfOut256To511BytePkts_Type = Counter64
_DellNetIfOut256To511BytePkts_Object = MibTableColumn
dellNetIfOut256To511BytePkts = _DellNetIfOut256To511BytePkts_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 11, 1, 2, 1, 1, 21),
    _DellNetIfOut256To511BytePkts_Type()
)
dellNetIfOut256To511BytePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetIfOut256To511BytePkts.setStatus("current")
_DellNetIfOut512To1023BytePkts_Type = Counter64
_DellNetIfOut512To1023BytePkts_Object = MibTableColumn
dellNetIfOut512To1023BytePkts = _DellNetIfOut512To1023BytePkts_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 11, 1, 2, 1, 1, 22),
    _DellNetIfOut512To1023BytePkts_Type()
)
dellNetIfOut512To1023BytePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetIfOut512To1023BytePkts.setStatus("current")
_DellNetIfOutOver1023BytePkts_Type = Counter64
_DellNetIfOutOver1023BytePkts_Object = MibTableColumn
dellNetIfOutOver1023BytePkts = _DellNetIfOutOver1023BytePkts_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 11, 1, 2, 1, 1, 23),
    _DellNetIfOutOver1023BytePkts_Type()
)
dellNetIfOutOver1023BytePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetIfOutOver1023BytePkts.setStatus("current")
_DellNetIfOutThrottles_Type = Counter64
_DellNetIfOutThrottles_Object = MibTableColumn
dellNetIfOutThrottles = _DellNetIfOutThrottles_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 11, 1, 2, 1, 1, 24),
    _DellNetIfOutThrottles_Type()
)
dellNetIfOutThrottles.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetIfOutThrottles.setStatus("current")
_DellNetIfLastDiscontinuityTime_Type = TimeStamp
_DellNetIfLastDiscontinuityTime_Object = MibTableColumn
dellNetIfLastDiscontinuityTime = _DellNetIfLastDiscontinuityTime_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 11, 1, 2, 1, 1, 25),
    _DellNetIfLastDiscontinuityTime_Type()
)
dellNetIfLastDiscontinuityTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetIfLastDiscontinuityTime.setStatus("current")


class _DellNetIfInCentRate_Type(Integer32):
    """Custom type dellNetIfInCentRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_DellNetIfInCentRate_Type.__name__ = "Integer32"
_DellNetIfInCentRate_Object = MibTableColumn
dellNetIfInCentRate = _DellNetIfInCentRate_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 11, 1, 2, 1, 1, 26),
    _DellNetIfInCentRate_Type()
)
dellNetIfInCentRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetIfInCentRate.setStatus("current")


class _DellNetIfOutCentRate_Type(Integer32):
    """Custom type dellNetIfOutCentRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_DellNetIfOutCentRate_Type.__name__ = "Integer32"
_DellNetIfOutCentRate_Object = MibTableColumn
dellNetIfOutCentRate = _DellNetIfOutCentRate_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 11, 1, 2, 1, 1, 27),
    _DellNetIfOutCentRate_Type()
)
dellNetIfOutCentRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetIfOutCentRate.setStatus("current")
_DellNetIfExtensionMibConformance_ObjectIdentity = ObjectIdentity
dellNetIfExtensionMibConformance = _DellNetIfExtensionMibConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 3, 11, 2)
)
_DellNetIfExtensionMibCompliances_ObjectIdentity = ObjectIdentity
dellNetIfExtensionMibCompliances = _DellNetIfExtensionMibCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 3, 11, 2, 1)
)
_DellNetIfExtensionMibGroups_ObjectIdentity = ObjectIdentity
dellNetIfExtensionMibGroups = _DellNetIfExtensionMibGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 3, 11, 2, 2)
)

# Managed Objects groups

dellNetIfParamsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6027, 3, 11, 2, 2, 1)
)
dellNetIfParamsGroup.setObjects(
      *(("DELL-NETWORKING-IF-EXTENSION-MIB", "dellNetIfIpMtu"),
        ("DELL-NETWORKING-IF-EXTENSION-MIB", "dellNetIfDuplexMode"),
        ("DELL-NETWORKING-IF-EXTENSION-MIB", "dellNetIfQueueingStrategy"),
        ("DELL-NETWORKING-IF-EXTENSION-MIB", "dellNetIfRxFlowCtrl"),
        ("DELL-NETWORKING-IF-EXTENSION-MIB", "dellNetIfTxFlowCtrl"),
        ("DELL-NETWORKING-IF-EXTENSION-MIB", "dellNetIfDescr"),
        ("DELL-NETWORKING-IF-EXTENSION-MIB", "dellNetIfAdminStatus"),
        ("DELL-NETWORKING-IF-EXTENSION-MIB", "dellNetIfRateInterval"),
        ("DELL-NETWORKING-IF-EXTENSION-MIB", "dellNetIfSpeed"),
        ("DELL-NETWORKING-IF-EXTENSION-MIB", "dellNetIfPortListBitPos"))
)
if mibBuilder.loadTexts:
    dellNetIfParamsGroup.setStatus("current")

dellNetIfStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6027, 3, 11, 2, 2, 2)
)
dellNetIfStatsGroup.setObjects(
      *(("DELL-NETWORKING-IF-EXTENSION-MIB", "dellNetIfInVlanPkts"),
        ("DELL-NETWORKING-IF-EXTENSION-MIB", "dellNetIfIn64BytePkts"),
        ("DELL-NETWORKING-IF-EXTENSION-MIB", "dellNetifIn65To127BytePkts"),
        ("DELL-NETWORKING-IF-EXTENSION-MIB", "dellNetIfIn128To255BytePkts"),
        ("DELL-NETWORKING-IF-EXTENSION-MIB", "dellNetIfIn256To511BytePkts"),
        ("DELL-NETWORKING-IF-EXTENSION-MIB", "dellNetIfIn512To1023BytePkts"),
        ("DELL-NETWORKING-IF-EXTENSION-MIB", "dellNetIfInOver1023BytePkts"),
        ("DELL-NETWORKING-IF-EXTENSION-MIB", "dellNetIfInThrottles"),
        ("DELL-NETWORKING-IF-EXTENSION-MIB", "dellNetIfInRunts"),
        ("DELL-NETWORKING-IF-EXTENSION-MIB", "dellNetIfInGiants"),
        ("DELL-NETWORKING-IF-EXTENSION-MIB", "dellNetIfInCRC"),
        ("DELL-NETWORKING-IF-EXTENSION-MIB", "dellNetIfInOverruns"),
        ("DELL-NETWORKING-IF-EXTENSION-MIB", "dellNetIfOutVlanPkts"),
        ("DELL-NETWORKING-IF-EXTENSION-MIB", "dellNetIfOutUnderruns"),
        ("DELL-NETWORKING-IF-EXTENSION-MIB", "dellNetIfOutUnicasts"),
        ("DELL-NETWORKING-IF-EXTENSION-MIB", "dellNetIfOutCollisions"),
        ("DELL-NETWORKING-IF-EXTENSION-MIB", "dellNetIfOutWredDrops"),
        ("DELL-NETWORKING-IF-EXTENSION-MIB", "dellNetIfOut64BytePkts"),
        ("DELL-NETWORKING-IF-EXTENSION-MIB", "dellNetIfOut65To127BytePkts"),
        ("DELL-NETWORKING-IF-EXTENSION-MIB", "dellNetIfOut128To255BytePkts"),
        ("DELL-NETWORKING-IF-EXTENSION-MIB", "dellNetIfOut256To511BytePkts"),
        ("DELL-NETWORKING-IF-EXTENSION-MIB", "dellNetIfOut512To1023BytePkts"),
        ("DELL-NETWORKING-IF-EXTENSION-MIB", "dellNetIfOutOver1023BytePkts"),
        ("DELL-NETWORKING-IF-EXTENSION-MIB", "dellNetIfOutThrottles"),
        ("DELL-NETWORKING-IF-EXTENSION-MIB", "dellNetIfLastDiscontinuityTime"),
        ("DELL-NETWORKING-IF-EXTENSION-MIB", "dellNetIfInCentRate"),
        ("DELL-NETWORKING-IF-EXTENSION-MIB", "dellNetIfOutCentRate"))
)
if mibBuilder.loadTexts:
    dellNetIfStatsGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

dellNetIfExtensionMibCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6027, 3, 11, 2, 1, 1)
)
if mibBuilder.loadTexts:
    dellNetIfExtensionMibCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DELL-NETWORKING-IF-EXTENSION-MIB",
    **{"dellNetIfExtensionMib": dellNetIfExtensionMib,
       "dellNetIfExtensionMibObject": dellNetIfExtensionMibObject,
       "dellNetIfExtensionParams": dellNetIfExtensionParams,
       "dellNetIfTable": dellNetIfTable,
       "dellNetIfEntry": dellNetIfEntry,
       "dellNetIfIpMtu": dellNetIfIpMtu,
       "dellNetIfDuplexMode": dellNetIfDuplexMode,
       "dellNetIfQueueingStrategy": dellNetIfQueueingStrategy,
       "dellNetIfRxFlowCtrl": dellNetIfRxFlowCtrl,
       "dellNetIfTxFlowCtrl": dellNetIfTxFlowCtrl,
       "dellNetIfDescr": dellNetIfDescr,
       "dellNetIfAdminStatus": dellNetIfAdminStatus,
       "dellNetIfRateInterval": dellNetIfRateInterval,
       "dellNetIfSpeed": dellNetIfSpeed,
       "dellNetIfPortListBitPos": dellNetIfPortListBitPos,
       "dellNetIfExtensionStats": dellNetIfExtensionStats,
       "dellNetIfStaticsTable": dellNetIfStaticsTable,
       "dellNetIfStaticsEntry": dellNetIfStaticsEntry,
       "dellNetIfInVlanPkts": dellNetIfInVlanPkts,
       "dellNetIfIn64BytePkts": dellNetIfIn64BytePkts,
       "dellNetifIn65To127BytePkts": dellNetifIn65To127BytePkts,
       "dellNetIfIn128To255BytePkts": dellNetIfIn128To255BytePkts,
       "dellNetIfIn256To511BytePkts": dellNetIfIn256To511BytePkts,
       "dellNetIfIn512To1023BytePkts": dellNetIfIn512To1023BytePkts,
       "dellNetIfInOver1023BytePkts": dellNetIfInOver1023BytePkts,
       "dellNetIfInThrottles": dellNetIfInThrottles,
       "dellNetIfInRunts": dellNetIfInRunts,
       "dellNetIfInGiants": dellNetIfInGiants,
       "dellNetIfInCRC": dellNetIfInCRC,
       "dellNetIfInOverruns": dellNetIfInOverruns,
       "dellNetIfOutVlanPkts": dellNetIfOutVlanPkts,
       "dellNetIfOutUnderruns": dellNetIfOutUnderruns,
       "dellNetIfOutUnicasts": dellNetIfOutUnicasts,
       "dellNetIfOutCollisions": dellNetIfOutCollisions,
       "dellNetIfOutWredDrops": dellNetIfOutWredDrops,
       "dellNetIfOut64BytePkts": dellNetIfOut64BytePkts,
       "dellNetIfOut65To127BytePkts": dellNetIfOut65To127BytePkts,
       "dellNetIfOut128To255BytePkts": dellNetIfOut128To255BytePkts,
       "dellNetIfOut256To511BytePkts": dellNetIfOut256To511BytePkts,
       "dellNetIfOut512To1023BytePkts": dellNetIfOut512To1023BytePkts,
       "dellNetIfOutOver1023BytePkts": dellNetIfOutOver1023BytePkts,
       "dellNetIfOutThrottles": dellNetIfOutThrottles,
       "dellNetIfLastDiscontinuityTime": dellNetIfLastDiscontinuityTime,
       "dellNetIfInCentRate": dellNetIfInCentRate,
       "dellNetIfOutCentRate": dellNetIfOutCentRate,
       "dellNetIfExtensionMibConformance": dellNetIfExtensionMibConformance,
       "dellNetIfExtensionMibCompliances": dellNetIfExtensionMibCompliances,
       "dellNetIfExtensionMibCompliance": dellNetIfExtensionMibCompliance,
       "dellNetIfExtensionMibGroups": dellNetIfExtensionMibGroups,
       "dellNetIfParamsGroup": dellNetIfParamsGroup,
       "dellNetIfStatsGroup": dellNetIfStatsGroup}
)
