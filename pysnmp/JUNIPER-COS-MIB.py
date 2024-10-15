# SNMP MIB module (JUNIPER-COS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/JUNIPER-COS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:12:48 2024
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

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

(jnxCosNotifications,
 jnxMibs) = mibBuilder.importSymbols(
    "JUNIPER-SMI",
    "jnxCosNotifications",
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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

jnxCos = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 15)
)
jnxCos.setRevisions(
        ("2014-11-07 00:00",
         "2013-05-20 00:00",
         "1970-01-01 00:00",
         "2009-10-29 00:00",
         "2007-12-31 00:00",
         "2006-10-31 00:00",
         "2003-06-13 00:00",
         "2002-09-09 00:00",
         "2002-01-10 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class JnxCosAdminString(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )



class JnxCosFcIdentifier(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )



class JnxCosIfstatFlags(Bits, TextualConvention):
    status = "current"


# MIB Managed Objects in the order of their OIDs

_JnxCosIfqStatsTable_Object = MibTable
jnxCosIfqStatsTable = _JnxCosIfqStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 15, 1)
)
if mibBuilder.loadTexts:
    jnxCosIfqStatsTable.setStatus("deprecated")
_JnxCosIfqStatsEntry_Object = MibTableRow
jnxCosIfqStatsEntry = _JnxCosIfqStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 15, 1, 1)
)
jnxCosIfqStatsEntry.setIndexNames(
    (0, "JUNIPER-COS-MIB", "jnxCosIfqIfIndex"),
    (0, "JUNIPER-COS-MIB", "jnxCosIfqFc"),
)
if mibBuilder.loadTexts:
    jnxCosIfqStatsEntry.setStatus("deprecated")
_JnxCosIfqIfIndex_Type = InterfaceIndex
_JnxCosIfqIfIndex_Object = MibTableColumn
jnxCosIfqIfIndex = _JnxCosIfqIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 15, 1, 1, 1),
    _JnxCosIfqIfIndex_Type()
)
jnxCosIfqIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxCosIfqIfIndex.setStatus("deprecated")
_JnxCosIfqFc_Type = JnxCosAdminString
_JnxCosIfqFc_Object = MibTableColumn
jnxCosIfqFc = _JnxCosIfqFc_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 15, 1, 1, 2),
    _JnxCosIfqFc_Type()
)
jnxCosIfqFc.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxCosIfqFc.setStatus("deprecated")
_JnxCosIfqQedPkts_Type = Counter64
_JnxCosIfqQedPkts_Object = MibTableColumn
jnxCosIfqQedPkts = _JnxCosIfqQedPkts_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 15, 1, 1, 3),
    _JnxCosIfqQedPkts_Type()
)
jnxCosIfqQedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxCosIfqQedPkts.setStatus("deprecated")
_JnxCosIfqQedPktRate_Type = CounterBasedGauge64
_JnxCosIfqQedPktRate_Object = MibTableColumn
jnxCosIfqQedPktRate = _JnxCosIfqQedPktRate_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 15, 1, 1, 4),
    _JnxCosIfqQedPktRate_Type()
)
jnxCosIfqQedPktRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxCosIfqQedPktRate.setStatus("deprecated")
_JnxCosIfqQedBytes_Type = Counter64
_JnxCosIfqQedBytes_Object = MibTableColumn
jnxCosIfqQedBytes = _JnxCosIfqQedBytes_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 15, 1, 1, 5),
    _JnxCosIfqQedBytes_Type()
)
jnxCosIfqQedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxCosIfqQedBytes.setStatus("deprecated")
_JnxCosIfqQedByteRate_Type = CounterBasedGauge64
_JnxCosIfqQedByteRate_Object = MibTableColumn
jnxCosIfqQedByteRate = _JnxCosIfqQedByteRate_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 15, 1, 1, 6),
    _JnxCosIfqQedByteRate_Type()
)
jnxCosIfqQedByteRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxCosIfqQedByteRate.setStatus("deprecated")
_JnxCosIfqTxedPkts_Type = Counter64
_JnxCosIfqTxedPkts_Object = MibTableColumn
jnxCosIfqTxedPkts = _JnxCosIfqTxedPkts_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 15, 1, 1, 7),
    _JnxCosIfqTxedPkts_Type()
)
jnxCosIfqTxedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxCosIfqTxedPkts.setStatus("deprecated")
_JnxCosIfqTxedPktRate_Type = CounterBasedGauge64
_JnxCosIfqTxedPktRate_Object = MibTableColumn
jnxCosIfqTxedPktRate = _JnxCosIfqTxedPktRate_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 15, 1, 1, 8),
    _JnxCosIfqTxedPktRate_Type()
)
jnxCosIfqTxedPktRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxCosIfqTxedPktRate.setStatus("deprecated")
_JnxCosIfqTxedBytes_Type = Counter64
_JnxCosIfqTxedBytes_Object = MibTableColumn
jnxCosIfqTxedBytes = _JnxCosIfqTxedBytes_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 15, 1, 1, 9),
    _JnxCosIfqTxedBytes_Type()
)
jnxCosIfqTxedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxCosIfqTxedBytes.setStatus("deprecated")
_JnxCosIfqTxedByteRate_Type = CounterBasedGauge64
_JnxCosIfqTxedByteRate_Object = MibTableColumn
jnxCosIfqTxedByteRate = _JnxCosIfqTxedByteRate_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 15, 1, 1, 10),
    _JnxCosIfqTxedByteRate_Type()
)
jnxCosIfqTxedByteRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxCosIfqTxedByteRate.setStatus("deprecated")
_JnxCosIfqTailDropPkts_Type = Counter64
_JnxCosIfqTailDropPkts_Object = MibTableColumn
jnxCosIfqTailDropPkts = _JnxCosIfqTailDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 15, 1, 1, 11),
    _JnxCosIfqTailDropPkts_Type()
)
jnxCosIfqTailDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxCosIfqTailDropPkts.setStatus("deprecated")
_JnxCosIfqTailDropPktRate_Type = CounterBasedGauge64
_JnxCosIfqTailDropPktRate_Object = MibTableColumn
jnxCosIfqTailDropPktRate = _JnxCosIfqTailDropPktRate_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 15, 1, 1, 12),
    _JnxCosIfqTailDropPktRate_Type()
)
jnxCosIfqTailDropPktRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxCosIfqTailDropPktRate.setStatus("deprecated")
_JnxCosIfqTotalRedDropPkts_Type = Counter64
_JnxCosIfqTotalRedDropPkts_Object = MibTableColumn
jnxCosIfqTotalRedDropPkts = _JnxCosIfqTotalRedDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 15, 1, 1, 13),
    _JnxCosIfqTotalRedDropPkts_Type()
)
jnxCosIfqTotalRedDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxCosIfqTotalRedDropPkts.setStatus("deprecated")
_JnxCosIfqTotalRedDropPktRate_Type = CounterBasedGauge64
_JnxCosIfqTotalRedDropPktRate_Object = MibTableColumn
jnxCosIfqTotalRedDropPktRate = _JnxCosIfqTotalRedDropPktRate_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 15, 1, 1, 14),
    _JnxCosIfqTotalRedDropPktRate_Type()
)
jnxCosIfqTotalRedDropPktRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxCosIfqTotalRedDropPktRate.setStatus("deprecated")
_JnxCosIfqLpNonTcpRedDropPkts_Type = Counter64
_JnxCosIfqLpNonTcpRedDropPkts_Object = MibTableColumn
jnxCosIfqLpNonTcpRedDropPkts = _JnxCosIfqLpNonTcpRedDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 15, 1, 1, 15),
    _JnxCosIfqLpNonTcpRedDropPkts_Type()
)
jnxCosIfqLpNonTcpRedDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxCosIfqLpNonTcpRedDropPkts.setStatus("deprecated")
_JnxCosIfqLpNonTcpRedDropPktRate_Type = CounterBasedGauge64
_JnxCosIfqLpNonTcpRedDropPktRate_Object = MibTableColumn
jnxCosIfqLpNonTcpRedDropPktRate = _JnxCosIfqLpNonTcpRedDropPktRate_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 15, 1, 1, 16),
    _JnxCosIfqLpNonTcpRedDropPktRate_Type()
)
jnxCosIfqLpNonTcpRedDropPktRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxCosIfqLpNonTcpRedDropPktRate.setStatus("deprecated")
_JnxCosIfqLpTcpRedDropPkts_Type = Counter64
_JnxCosIfqLpTcpRedDropPkts_Object = MibTableColumn
jnxCosIfqLpTcpRedDropPkts = _JnxCosIfqLpTcpRedDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 15, 1, 1, 17),
    _JnxCosIfqLpTcpRedDropPkts_Type()
)
jnxCosIfqLpTcpRedDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxCosIfqLpTcpRedDropPkts.setStatus("deprecated")
_JnxCosIfqLpTcpRedDropPktRate_Type = CounterBasedGauge64
_JnxCosIfqLpTcpRedDropPktRate_Object = MibTableColumn
jnxCosIfqLpTcpRedDropPktRate = _JnxCosIfqLpTcpRedDropPktRate_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 15, 1, 1, 18),
    _JnxCosIfqLpTcpRedDropPktRate_Type()
)
jnxCosIfqLpTcpRedDropPktRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxCosIfqLpTcpRedDropPktRate.setStatus("deprecated")
_JnxCosIfqHpNonTcpRedDropPkts_Type = Counter64
_JnxCosIfqHpNonTcpRedDropPkts_Object = MibTableColumn
jnxCosIfqHpNonTcpRedDropPkts = _JnxCosIfqHpNonTcpRedDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 15, 1, 1, 19),
    _JnxCosIfqHpNonTcpRedDropPkts_Type()
)
jnxCosIfqHpNonTcpRedDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxCosIfqHpNonTcpRedDropPkts.setStatus("deprecated")
_JnxCosIfqHpNonTcpRedDropPktRate_Type = CounterBasedGauge64
_JnxCosIfqHpNonTcpRedDropPktRate_Object = MibTableColumn
jnxCosIfqHpNonTcpRedDropPktRate = _JnxCosIfqHpNonTcpRedDropPktRate_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 15, 1, 1, 20),
    _JnxCosIfqHpNonTcpRedDropPktRate_Type()
)
jnxCosIfqHpNonTcpRedDropPktRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxCosIfqHpNonTcpRedDropPktRate.setStatus("deprecated")
_JnxCosIfqHpTcpRedDropPkts_Type = Counter64
_JnxCosIfqHpTcpRedDropPkts_Object = MibTableColumn
jnxCosIfqHpTcpRedDropPkts = _JnxCosIfqHpTcpRedDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 15, 1, 1, 21),
    _JnxCosIfqHpTcpRedDropPkts_Type()
)
jnxCosIfqHpTcpRedDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxCosIfqHpTcpRedDropPkts.setStatus("deprecated")
_JnxCosIfqHpTcpRedDropPktRate_Type = CounterBasedGauge64
_JnxCosIfqHpTcpRedDropPktRate_Object = MibTableColumn
jnxCosIfqHpTcpRedDropPktRate = _JnxCosIfqHpTcpRedDropPktRate_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 15, 1, 1, 22),
    _JnxCosIfqHpTcpRedDropPktRate_Type()
)
jnxCosIfqHpTcpRedDropPktRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxCosIfqHpTcpRedDropPktRate.setStatus("deprecated")
_JnxCosIfqTotalRedDropBytes_Type = Counter64
_JnxCosIfqTotalRedDropBytes_Object = MibTableColumn
jnxCosIfqTotalRedDropBytes = _JnxCosIfqTotalRedDropBytes_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 15, 1, 1, 23),
    _JnxCosIfqTotalRedDropBytes_Type()
)
jnxCosIfqTotalRedDropBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxCosIfqTotalRedDropBytes.setStatus("deprecated")
_JnxCosIfqTotalRedDropByteRate_Type = CounterBasedGauge64
_JnxCosIfqTotalRedDropByteRate_Object = MibTableColumn
jnxCosIfqTotalRedDropByteRate = _JnxCosIfqTotalRedDropByteRate_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 15, 1, 1, 24),
    _JnxCosIfqTotalRedDropByteRate_Type()
)
jnxCosIfqTotalRedDropByteRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxCosIfqTotalRedDropByteRate.setStatus("deprecated")
_JnxCosIfqLpNonTcpRedDropBytes_Type = Counter64
_JnxCosIfqLpNonTcpRedDropBytes_Object = MibTableColumn
jnxCosIfqLpNonTcpRedDropBytes = _JnxCosIfqLpNonTcpRedDropBytes_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 15, 1, 1, 25),
    _JnxCosIfqLpNonTcpRedDropBytes_Type()
)
jnxCosIfqLpNonTcpRedDropBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxCosIfqLpNonTcpRedDropBytes.setStatus("deprecated")
_JnxCosIfqLpNonTcpRedDropByteRate_Type = CounterBasedGauge64
_JnxCosIfqLpNonTcpRedDropByteRate_Object = MibTableColumn
jnxCosIfqLpNonTcpRedDropByteRate = _JnxCosIfqLpNonTcpRedDropByteRate_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 15, 1, 1, 26),
    _JnxCosIfqLpNonTcpRedDropByteRate_Type()
)
jnxCosIfqLpNonTcpRedDropByteRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxCosIfqLpNonTcpRedDropByteRate.setStatus("deprecated")
_JnxCosIfqLpTcpRedDropBytes_Type = Counter64
_JnxCosIfqLpTcpRedDropBytes_Object = MibTableColumn
jnxCosIfqLpTcpRedDropBytes = _JnxCosIfqLpTcpRedDropBytes_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 15, 1, 1, 27),
    _JnxCosIfqLpTcpRedDropBytes_Type()
)
jnxCosIfqLpTcpRedDropBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxCosIfqLpTcpRedDropBytes.setStatus("deprecated")
_JnxCosIfqLpTcpRedDropByteRate_Type = CounterBasedGauge64
_JnxCosIfqLpTcpRedDropByteRate_Object = MibTableColumn
jnxCosIfqLpTcpRedDropByteRate = _JnxCosIfqLpTcpRedDropByteRate_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 15, 1, 1, 28),
    _JnxCosIfqLpTcpRedDropByteRate_Type()
)
jnxCosIfqLpTcpRedDropByteRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxCosIfqLpTcpRedDropByteRate.setStatus("deprecated")
_JnxCosIfqHpNonTcpRedDropBytes_Type = Counter64
_JnxCosIfqHpNonTcpRedDropBytes_Object = MibTableColumn
jnxCosIfqHpNonTcpRedDropBytes = _JnxCosIfqHpNonTcpRedDropBytes_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 15, 1, 1, 29),
    _JnxCosIfqHpNonTcpRedDropBytes_Type()
)
jnxCosIfqHpNonTcpRedDropBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxCosIfqHpNonTcpRedDropBytes.setStatus("deprecated")
_JnxCosIfqHpNonTcpRedDropByteRate_Type = CounterBasedGauge64
_JnxCosIfqHpNonTcpRedDropByteRate_Object = MibTableColumn
jnxCosIfqHpNonTcpRedDropByteRate = _JnxCosIfqHpNonTcpRedDropByteRate_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 15, 1, 1, 30),
    _JnxCosIfqHpNonTcpRedDropByteRate_Type()
)
jnxCosIfqHpNonTcpRedDropByteRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxCosIfqHpNonTcpRedDropByteRate.setStatus("deprecated")
_JnxCosIfqHpTcpRedDropBytes_Type = Counter64
_JnxCosIfqHpTcpRedDropBytes_Object = MibTableColumn
jnxCosIfqHpTcpRedDropBytes = _JnxCosIfqHpTcpRedDropBytes_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 15, 1, 1, 31),
    _JnxCosIfqHpTcpRedDropBytes_Type()
)
jnxCosIfqHpTcpRedDropBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxCosIfqHpTcpRedDropBytes.setStatus("deprecated")
_JnxCosIfqHpTcpRedDropByteRate_Type = CounterBasedGauge64
_JnxCosIfqHpTcpRedDropByteRate_Object = MibTableColumn
jnxCosIfqHpTcpRedDropByteRate = _JnxCosIfqHpTcpRedDropByteRate_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 15, 1, 1, 32),
    _JnxCosIfqHpTcpRedDropByteRate_Type()
)
jnxCosIfqHpTcpRedDropByteRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxCosIfqHpTcpRedDropByteRate.setStatus("deprecated")
_JnxCosFcTable_Object = MibTable
jnxCosFcTable = _JnxCosFcTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 15, 2)
)
if mibBuilder.loadTexts:
    jnxCosFcTable.setStatus("current")
_JnxCosFcEntry_Object = MibTableRow
jnxCosFcEntry = _JnxCosFcEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 15, 2, 1)
)
jnxCosFcEntry.setIndexNames(
    (0, "JUNIPER-COS-MIB", "jnxCosFcName"),
)
if mibBuilder.loadTexts:
    jnxCosFcEntry.setStatus("current")
_JnxCosFcName_Type = JnxCosAdminString
_JnxCosFcName_Object = MibTableColumn
jnxCosFcName = _JnxCosFcName_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 15, 2, 1, 1),
    _JnxCosFcName_Type()
)
jnxCosFcName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxCosFcName.setStatus("current")


class _JnxCosFcQueueNr_Type(Integer32):
    """Custom type jnxCosFcQueueNr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_JnxCosFcQueueNr_Type.__name__ = "Integer32"
_JnxCosFcQueueNr_Object = MibTableColumn
jnxCosFcQueueNr = _JnxCosFcQueueNr_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 15, 2, 1, 2),
    _JnxCosFcQueueNr_Type()
)
jnxCosFcQueueNr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxCosFcQueueNr.setStatus("current")


class _JnxCosRestrictedQNr_Type(Integer32):
    """Custom type jnxCosRestrictedQNr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_JnxCosRestrictedQNr_Type.__name__ = "Integer32"
_JnxCosRestrictedQNr_Object = MibTableColumn
jnxCosRestrictedQNr = _JnxCosRestrictedQNr_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 15, 2, 1, 3),
    _JnxCosRestrictedQNr_Type()
)
jnxCosRestrictedQNr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxCosRestrictedQNr.setStatus("current")
_JnxCosFcIdTable_Object = MibTable
jnxCosFcIdTable = _JnxCosFcIdTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 15, 3)
)
if mibBuilder.loadTexts:
    jnxCosFcIdTable.setStatus("current")
_JnxCosFcIdEntry_Object = MibTableRow
jnxCosFcIdEntry = _JnxCosFcIdEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 15, 3, 1)
)
jnxCosFcIdEntry.setIndexNames(
    (0, "JUNIPER-COS-MIB", "jnxCosFcId"),
)
if mibBuilder.loadTexts:
    jnxCosFcIdEntry.setStatus("current")
_JnxCosFcId_Type = JnxCosFcIdentifier
_JnxCosFcId_Object = MibTableColumn
jnxCosFcId = _JnxCosFcId_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 15, 3, 1, 1),
    _JnxCosFcId_Type()
)
jnxCosFcId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxCosFcId.setStatus("current")
_JnxCosFcIdToFcName_Type = JnxCosAdminString
_JnxCosFcIdToFcName_Object = MibTableColumn
jnxCosFcIdToFcName = _JnxCosFcIdToFcName_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 15, 3, 1, 2),
    _JnxCosFcIdToFcName_Type()
)
jnxCosFcIdToFcName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxCosFcIdToFcName.setStatus("current")


class _JnxCosFcFabricPriority_Type(Integer32):
    """Custom type jnxCosFcFabricPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("high", 1),
          ("low", 0))
    )


_JnxCosFcFabricPriority_Type.__name__ = "Integer32"
_JnxCosFcFabricPriority_Object = MibTableColumn
jnxCosFcFabricPriority = _JnxCosFcFabricPriority_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 15, 3, 1, 3),
    _JnxCosFcFabricPriority_Type()
)
jnxCosFcFabricPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxCosFcFabricPriority.setStatus("current")
_JnxCosQstatTable_Object = MibTable
jnxCosQstatTable = _JnxCosQstatTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 15, 4)
)
if mibBuilder.loadTexts:
    jnxCosQstatTable.setStatus("current")
_JnxCosQstatEntry_Object = MibTableRow
jnxCosQstatEntry = _JnxCosQstatEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 15, 4, 1)
)
jnxCosQstatEntry.setIndexNames(
    (0, "JUNIPER-COS-MIB", "jnxCosQstatIfIndex"),
    (0, "JUNIPER-COS-MIB", "jnxCosQstatQueueNr"),
)
if mibBuilder.loadTexts:
    jnxCosQstatEntry.setStatus("current")
_JnxCosQstatIfIndex_Type = InterfaceIndex
_JnxCosQstatIfIndex_Object = MibTableColumn
jnxCosQstatIfIndex = _JnxCosQstatIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 15, 4, 1, 1),
    _JnxCosQstatIfIndex_Type()
)
jnxCosQstatIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxCosQstatIfIndex.setStatus("current")


class _JnxCosQstatQueueNr_Type(Integer32):
    """Custom type jnxCosQstatQueueNr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_JnxCosQstatQueueNr_Type.__name__ = "Integer32"
_JnxCosQstatQueueNr_Object = MibTableColumn
jnxCosQstatQueueNr = _JnxCosQstatQueueNr_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 15, 4, 1, 2),
    _JnxCosQstatQueueNr_Type()
)
jnxCosQstatQueueNr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxCosQstatQueueNr.setStatus("current")
_JnxCosQstatQedPkts_Type = Counter64
_JnxCosQstatQedPkts_Object = MibTableColumn
jnxCosQstatQedPkts = _JnxCosQstatQedPkts_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 15, 4, 1, 3),
    _JnxCosQstatQedPkts_Type()
)
jnxCosQstatQedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxCosQstatQedPkts.setStatus("current")
_JnxCosQstatQedPktRate_Type = CounterBasedGauge64
_JnxCosQstatQedPktRate_Object = MibTableColumn
jnxCosQstatQedPktRate = _JnxCosQstatQedPktRate_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 15, 4, 1, 4),
    _JnxCosQstatQedPktRate_Type()
)
jnxCosQstatQedPktRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxCosQstatQedPktRate.setStatus("current")
_JnxCosQstatQedBytes_Type = Counter64
_JnxCosQstatQedBytes_Object = MibTableColumn
jnxCosQstatQedBytes = _JnxCosQstatQedBytes_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 15, 4, 1, 5),
    _JnxCosQstatQedBytes_Type()
)
jnxCosQstatQedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxCosQstatQedBytes.setStatus("current")
_JnxCosQstatQedByteRate_Type = CounterBasedGauge64
_JnxCosQstatQedByteRate_Object = MibTableColumn
jnxCosQstatQedByteRate = _JnxCosQstatQedByteRate_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 15, 4, 1, 6),
    _JnxCosQstatQedByteRate_Type()
)
jnxCosQstatQedByteRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxCosQstatQedByteRate.setStatus("current")
_JnxCosQstatTxedPkts_Type = Counter64
_JnxCosQstatTxedPkts_Object = MibTableColumn
jnxCosQstatTxedPkts = _JnxCosQstatTxedPkts_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 15, 4, 1, 7),
    _JnxCosQstatTxedPkts_Type()
)
jnxCosQstatTxedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxCosQstatTxedPkts.setStatus("current")
_JnxCosQstatTxedPktRate_Type = CounterBasedGauge64
_JnxCosQstatTxedPktRate_Object = MibTableColumn
jnxCosQstatTxedPktRate = _JnxCosQstatTxedPktRate_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 15, 4, 1, 8),
    _JnxCosQstatTxedPktRate_Type()
)
jnxCosQstatTxedPktRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxCosQstatTxedPktRate.setStatus("current")
_JnxCosQstatTxedBytes_Type = Counter64
_JnxCosQstatTxedBytes_Object = MibTableColumn
jnxCosQstatTxedBytes = _JnxCosQstatTxedBytes_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 15, 4, 1, 9),
    _JnxCosQstatTxedBytes_Type()
)
jnxCosQstatTxedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxCosQstatTxedBytes.setStatus("current")
_JnxCosQstatTxedByteRate_Type = CounterBasedGauge64
_JnxCosQstatTxedByteRate_Object = MibTableColumn
jnxCosQstatTxedByteRate = _JnxCosQstatTxedByteRate_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 15, 4, 1, 10),
    _JnxCosQstatTxedByteRate_Type()
)
jnxCosQstatTxedByteRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxCosQstatTxedByteRate.setStatus("current")
_JnxCosQstatTailDropPkts_Type = Counter64
_JnxCosQstatTailDropPkts_Object = MibTableColumn
jnxCosQstatTailDropPkts = _JnxCosQstatTailDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 15, 4, 1, 11),
    _JnxCosQstatTailDropPkts_Type()
)
jnxCosQstatTailDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxCosQstatTailDropPkts.setStatus("current")
_JnxCosQstatTailDropPktRate_Type = CounterBasedGauge64
_JnxCosQstatTailDropPktRate_Object = MibTableColumn
jnxCosQstatTailDropPktRate = _JnxCosQstatTailDropPktRate_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 15, 4, 1, 12),
    _JnxCosQstatTailDropPktRate_Type()
)
jnxCosQstatTailDropPktRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxCosQstatTailDropPktRate.setStatus("current")
_JnxCosQstatTotalRedDropPkts_Type = Counter64
_JnxCosQstatTotalRedDropPkts_Object = MibTableColumn
jnxCosQstatTotalRedDropPkts = _JnxCosQstatTotalRedDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 15, 4, 1, 13),
    _JnxCosQstatTotalRedDropPkts_Type()
)
jnxCosQstatTotalRedDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxCosQstatTotalRedDropPkts.setStatus("current")
_JnxCosQstatTotalRedDropPktRate_Type = CounterBasedGauge64
_JnxCosQstatTotalRedDropPktRate_Object = MibTableColumn
jnxCosQstatTotalRedDropPktRate = _JnxCosQstatTotalRedDropPktRate_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 15, 4, 1, 14),
    _JnxCosQstatTotalRedDropPktRate_Type()
)
jnxCosQstatTotalRedDropPktRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxCosQstatTotalRedDropPktRate.setStatus("current")
_JnxCosQstatLpNonTcpRedDropPkts_Type = Counter64
_JnxCosQstatLpNonTcpRedDropPkts_Object = MibTableColumn
jnxCosQstatLpNonTcpRedDropPkts = _JnxCosQstatLpNonTcpRedDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 15, 4, 1, 15),
    _JnxCosQstatLpNonTcpRedDropPkts_Type()
)
jnxCosQstatLpNonTcpRedDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxCosQstatLpNonTcpRedDropPkts.setStatus("current")
_JnxCosQstatLpNonTcpRDropPktRate_Type = CounterBasedGauge64
_JnxCosQstatLpNonTcpRDropPktRate_Object = MibTableColumn
jnxCosQstatLpNonTcpRDropPktRate = _JnxCosQstatLpNonTcpRDropPktRate_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 15, 4, 1, 16),
    _JnxCosQstatLpNonTcpRDropPktRate_Type()
)
jnxCosQstatLpNonTcpRDropPktRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxCosQstatLpNonTcpRDropPktRate.setStatus("current")
_JnxCosQstatLpTcpRedDropPkts_Type = Counter64
_JnxCosQstatLpTcpRedDropPkts_Object = MibTableColumn
jnxCosQstatLpTcpRedDropPkts = _JnxCosQstatLpTcpRedDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 15, 4, 1, 17),
    _JnxCosQstatLpTcpRedDropPkts_Type()
)
jnxCosQstatLpTcpRedDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxCosQstatLpTcpRedDropPkts.setStatus("current")
_JnxCosQstatLpTcpRedDropPktRate_Type = CounterBasedGauge64
_JnxCosQstatLpTcpRedDropPktRate_Object = MibTableColumn
jnxCosQstatLpTcpRedDropPktRate = _JnxCosQstatLpTcpRedDropPktRate_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 15, 4, 1, 18),
    _JnxCosQstatLpTcpRedDropPktRate_Type()
)
jnxCosQstatLpTcpRedDropPktRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxCosQstatLpTcpRedDropPktRate.setStatus("current")
_JnxCosQstatHpNonTcpRedDropPkts_Type = Counter64
_JnxCosQstatHpNonTcpRedDropPkts_Object = MibTableColumn
jnxCosQstatHpNonTcpRedDropPkts = _JnxCosQstatHpNonTcpRedDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 15, 4, 1, 19),
    _JnxCosQstatHpNonTcpRedDropPkts_Type()
)
jnxCosQstatHpNonTcpRedDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxCosQstatHpNonTcpRedDropPkts.setStatus("current")
_JnxCosQstatHpNonTcpRDropPktRate_Type = CounterBasedGauge64
_JnxCosQstatHpNonTcpRDropPktRate_Object = MibTableColumn
jnxCosQstatHpNonTcpRDropPktRate = _JnxCosQstatHpNonTcpRDropPktRate_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 15, 4, 1, 20),
    _JnxCosQstatHpNonTcpRDropPktRate_Type()
)
jnxCosQstatHpNonTcpRDropPktRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxCosQstatHpNonTcpRDropPktRate.setStatus("current")
_JnxCosQstatHpTcpRedDropPkts_Type = Counter64
_JnxCosQstatHpTcpRedDropPkts_Object = MibTableColumn
jnxCosQstatHpTcpRedDropPkts = _JnxCosQstatHpTcpRedDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 15, 4, 1, 21),
    _JnxCosQstatHpTcpRedDropPkts_Type()
)
jnxCosQstatHpTcpRedDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxCosQstatHpTcpRedDropPkts.setStatus("current")
_JnxCosQstatHpTcpRedDropPktRate_Type = CounterBasedGauge64
_JnxCosQstatHpTcpRedDropPktRate_Object = MibTableColumn
jnxCosQstatHpTcpRedDropPktRate = _JnxCosQstatHpTcpRedDropPktRate_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 15, 4, 1, 22),
    _JnxCosQstatHpTcpRedDropPktRate_Type()
)
jnxCosQstatHpTcpRedDropPktRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxCosQstatHpTcpRedDropPktRate.setStatus("current")
_JnxCosQstatTotalRedDropBytes_Type = Counter64
_JnxCosQstatTotalRedDropBytes_Object = MibTableColumn
jnxCosQstatTotalRedDropBytes = _JnxCosQstatTotalRedDropBytes_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 15, 4, 1, 23),
    _JnxCosQstatTotalRedDropBytes_Type()
)
jnxCosQstatTotalRedDropBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxCosQstatTotalRedDropBytes.setStatus("current")
_JnxCosQstatTotalRedDropByteRate_Type = CounterBasedGauge64
_JnxCosQstatTotalRedDropByteRate_Object = MibTableColumn
jnxCosQstatTotalRedDropByteRate = _JnxCosQstatTotalRedDropByteRate_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 15, 4, 1, 24),
    _JnxCosQstatTotalRedDropByteRate_Type()
)
jnxCosQstatTotalRedDropByteRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxCosQstatTotalRedDropByteRate.setStatus("current")
_JnxCosQstatLpNonTcpRedDropBytes_Type = Counter64
_JnxCosQstatLpNonTcpRedDropBytes_Object = MibTableColumn
jnxCosQstatLpNonTcpRedDropBytes = _JnxCosQstatLpNonTcpRedDropBytes_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 15, 4, 1, 25),
    _JnxCosQstatLpNonTcpRedDropBytes_Type()
)
jnxCosQstatLpNonTcpRedDropBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxCosQstatLpNonTcpRedDropBytes.setStatus("current")
_JnxCosQstatLpNonTcpRDropByteRate_Type = CounterBasedGauge64
_JnxCosQstatLpNonTcpRDropByteRate_Object = MibTableColumn
jnxCosQstatLpNonTcpRDropByteRate = _JnxCosQstatLpNonTcpRDropByteRate_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 15, 4, 1, 26),
    _JnxCosQstatLpNonTcpRDropByteRate_Type()
)
jnxCosQstatLpNonTcpRDropByteRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxCosQstatLpNonTcpRDropByteRate.setStatus("current")
_JnxCosQstatLpTcpRedDropBytes_Type = Counter64
_JnxCosQstatLpTcpRedDropBytes_Object = MibTableColumn
jnxCosQstatLpTcpRedDropBytes = _JnxCosQstatLpTcpRedDropBytes_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 15, 4, 1, 27),
    _JnxCosQstatLpTcpRedDropBytes_Type()
)
jnxCosQstatLpTcpRedDropBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxCosQstatLpTcpRedDropBytes.setStatus("current")
_JnxCosQstatLpTcpRedDropByteRate_Type = CounterBasedGauge64
_JnxCosQstatLpTcpRedDropByteRate_Object = MibTableColumn
jnxCosQstatLpTcpRedDropByteRate = _JnxCosQstatLpTcpRedDropByteRate_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 15, 4, 1, 28),
    _JnxCosQstatLpTcpRedDropByteRate_Type()
)
jnxCosQstatLpTcpRedDropByteRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxCosQstatLpTcpRedDropByteRate.setStatus("current")
_JnxCosQstatHpNonTcpRedDropBytes_Type = Counter64
_JnxCosQstatHpNonTcpRedDropBytes_Object = MibTableColumn
jnxCosQstatHpNonTcpRedDropBytes = _JnxCosQstatHpNonTcpRedDropBytes_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 15, 4, 1, 29),
    _JnxCosQstatHpNonTcpRedDropBytes_Type()
)
jnxCosQstatHpNonTcpRedDropBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxCosQstatHpNonTcpRedDropBytes.setStatus("current")
_JnxCosQstatHpNonTcpRDropByteRate_Type = CounterBasedGauge64
_JnxCosQstatHpNonTcpRDropByteRate_Object = MibTableColumn
jnxCosQstatHpNonTcpRDropByteRate = _JnxCosQstatHpNonTcpRDropByteRate_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 15, 4, 1, 30),
    _JnxCosQstatHpNonTcpRDropByteRate_Type()
)
jnxCosQstatHpNonTcpRDropByteRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxCosQstatHpNonTcpRDropByteRate.setStatus("current")
_JnxCosQstatHpTcpRedDropBytes_Type = Counter64
_JnxCosQstatHpTcpRedDropBytes_Object = MibTableColumn
jnxCosQstatHpTcpRedDropBytes = _JnxCosQstatHpTcpRedDropBytes_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 15, 4, 1, 31),
    _JnxCosQstatHpTcpRedDropBytes_Type()
)
jnxCosQstatHpTcpRedDropBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxCosQstatHpTcpRedDropBytes.setStatus("current")
_JnxCosQstatHpTcpRedDropByteRate_Type = CounterBasedGauge64
_JnxCosQstatHpTcpRedDropByteRate_Object = MibTableColumn
jnxCosQstatHpTcpRedDropByteRate = _JnxCosQstatHpTcpRedDropByteRate_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 15, 4, 1, 32),
    _JnxCosQstatHpTcpRedDropByteRate_Type()
)
jnxCosQstatHpTcpRedDropByteRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxCosQstatHpTcpRedDropByteRate.setStatus("current")
_JnxCosQstatLpRedDropPkts_Type = Counter64
_JnxCosQstatLpRedDropPkts_Object = MibTableColumn
jnxCosQstatLpRedDropPkts = _JnxCosQstatLpRedDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 15, 4, 1, 33),
    _JnxCosQstatLpRedDropPkts_Type()
)
jnxCosQstatLpRedDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxCosQstatLpRedDropPkts.setStatus("current")
_JnxCosQstatLpRedDropPktRate_Type = CounterBasedGauge64
_JnxCosQstatLpRedDropPktRate_Object = MibTableColumn
jnxCosQstatLpRedDropPktRate = _JnxCosQstatLpRedDropPktRate_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 15, 4, 1, 34),
    _JnxCosQstatLpRedDropPktRate_Type()
)
jnxCosQstatLpRedDropPktRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxCosQstatLpRedDropPktRate.setStatus("current")
_JnxCosQstatMLpRedDropPkts_Type = Counter64
_JnxCosQstatMLpRedDropPkts_Object = MibTableColumn
jnxCosQstatMLpRedDropPkts = _JnxCosQstatMLpRedDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 15, 4, 1, 35),
    _JnxCosQstatMLpRedDropPkts_Type()
)
jnxCosQstatMLpRedDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxCosQstatMLpRedDropPkts.setStatus("current")
_JnxCosQstatMLpRedDropPktRate_Type = CounterBasedGauge64
_JnxCosQstatMLpRedDropPktRate_Object = MibTableColumn
jnxCosQstatMLpRedDropPktRate = _JnxCosQstatMLpRedDropPktRate_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 15, 4, 1, 36),
    _JnxCosQstatMLpRedDropPktRate_Type()
)
jnxCosQstatMLpRedDropPktRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxCosQstatMLpRedDropPktRate.setStatus("current")
_JnxCosQstatMHpRedDropPkts_Type = Counter64
_JnxCosQstatMHpRedDropPkts_Object = MibTableColumn
jnxCosQstatMHpRedDropPkts = _JnxCosQstatMHpRedDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 15, 4, 1, 37),
    _JnxCosQstatMHpRedDropPkts_Type()
)
jnxCosQstatMHpRedDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxCosQstatMHpRedDropPkts.setStatus("current")
_JnxCosQstatMHpRedDropPktRate_Type = CounterBasedGauge64
_JnxCosQstatMHpRedDropPktRate_Object = MibTableColumn
jnxCosQstatMHpRedDropPktRate = _JnxCosQstatMHpRedDropPktRate_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 15, 4, 1, 38),
    _JnxCosQstatMHpRedDropPktRate_Type()
)
jnxCosQstatMHpRedDropPktRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxCosQstatMHpRedDropPktRate.setStatus("current")
_JnxCosQstatHpRedDropPkts_Type = Counter64
_JnxCosQstatHpRedDropPkts_Object = MibTableColumn
jnxCosQstatHpRedDropPkts = _JnxCosQstatHpRedDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 15, 4, 1, 39),
    _JnxCosQstatHpRedDropPkts_Type()
)
jnxCosQstatHpRedDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxCosQstatHpRedDropPkts.setStatus("current")
_JnxCosQstatHpRedDropPktRate_Type = CounterBasedGauge64
_JnxCosQstatHpRedDropPktRate_Object = MibTableColumn
jnxCosQstatHpRedDropPktRate = _JnxCosQstatHpRedDropPktRate_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 15, 4, 1, 40),
    _JnxCosQstatHpRedDropPktRate_Type()
)
jnxCosQstatHpRedDropPktRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxCosQstatHpRedDropPktRate.setStatus("current")
_JnxCosQstatLpRedDropBytes_Type = Counter64
_JnxCosQstatLpRedDropBytes_Object = MibTableColumn
jnxCosQstatLpRedDropBytes = _JnxCosQstatLpRedDropBytes_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 15, 4, 1, 41),
    _JnxCosQstatLpRedDropBytes_Type()
)
jnxCosQstatLpRedDropBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxCosQstatLpRedDropBytes.setStatus("current")
_JnxCosQstatLpRedDropByteRate_Type = CounterBasedGauge64
_JnxCosQstatLpRedDropByteRate_Object = MibTableColumn
jnxCosQstatLpRedDropByteRate = _JnxCosQstatLpRedDropByteRate_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 15, 4, 1, 42),
    _JnxCosQstatLpRedDropByteRate_Type()
)
jnxCosQstatLpRedDropByteRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxCosQstatLpRedDropByteRate.setStatus("current")
_JnxCosQstatMLpRedDropBytes_Type = Counter64
_JnxCosQstatMLpRedDropBytes_Object = MibTableColumn
jnxCosQstatMLpRedDropBytes = _JnxCosQstatMLpRedDropBytes_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 15, 4, 1, 43),
    _JnxCosQstatMLpRedDropBytes_Type()
)
jnxCosQstatMLpRedDropBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxCosQstatMLpRedDropBytes.setStatus("current")
_JnxCosQstatMLpRedDropByteRate_Type = CounterBasedGauge64
_JnxCosQstatMLpRedDropByteRate_Object = MibTableColumn
jnxCosQstatMLpRedDropByteRate = _JnxCosQstatMLpRedDropByteRate_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 15, 4, 1, 44),
    _JnxCosQstatMLpRedDropByteRate_Type()
)
jnxCosQstatMLpRedDropByteRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxCosQstatMLpRedDropByteRate.setStatus("current")
_JnxCosQstatMHpRedDropBytes_Type = Counter64
_JnxCosQstatMHpRedDropBytes_Object = MibTableColumn
jnxCosQstatMHpRedDropBytes = _JnxCosQstatMHpRedDropBytes_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 15, 4, 1, 45),
    _JnxCosQstatMHpRedDropBytes_Type()
)
jnxCosQstatMHpRedDropBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxCosQstatMHpRedDropBytes.setStatus("current")
_JnxCosQstatMHpRedDropByteRate_Type = CounterBasedGauge64
_JnxCosQstatMHpRedDropByteRate_Object = MibTableColumn
jnxCosQstatMHpRedDropByteRate = _JnxCosQstatMHpRedDropByteRate_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 15, 4, 1, 46),
    _JnxCosQstatMHpRedDropByteRate_Type()
)
jnxCosQstatMHpRedDropByteRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxCosQstatMHpRedDropByteRate.setStatus("current")
_JnxCosQstatHpRedDropBytes_Type = Counter64
_JnxCosQstatHpRedDropBytes_Object = MibTableColumn
jnxCosQstatHpRedDropBytes = _JnxCosQstatHpRedDropBytes_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 15, 4, 1, 47),
    _JnxCosQstatHpRedDropBytes_Type()
)
jnxCosQstatHpRedDropBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxCosQstatHpRedDropBytes.setStatus("current")
_JnxCosQstatHpRedDropByteRate_Type = CounterBasedGauge64
_JnxCosQstatHpRedDropByteRate_Object = MibTableColumn
jnxCosQstatHpRedDropByteRate = _JnxCosQstatHpRedDropByteRate_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 15, 4, 1, 48),
    _JnxCosQstatHpRedDropByteRate_Type()
)
jnxCosQstatHpRedDropByteRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxCosQstatHpRedDropByteRate.setStatus("current")
_JnxCosQstatRateLimitDropPkts_Type = Counter64
_JnxCosQstatRateLimitDropPkts_Object = MibTableColumn
jnxCosQstatRateLimitDropPkts = _JnxCosQstatRateLimitDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 15, 4, 1, 49),
    _JnxCosQstatRateLimitDropPkts_Type()
)
jnxCosQstatRateLimitDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxCosQstatRateLimitDropPkts.setStatus("current")
_JnxCosQstatRateLimitDropPktRate_Type = CounterBasedGauge64
_JnxCosQstatRateLimitDropPktRate_Object = MibTableColumn
jnxCosQstatRateLimitDropPktRate = _JnxCosQstatRateLimitDropPktRate_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 15, 4, 1, 50),
    _JnxCosQstatRateLimitDropPktRate_Type()
)
jnxCosQstatRateLimitDropPktRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxCosQstatRateLimitDropPktRate.setStatus("current")
_JnxCosQstatRateLimitDropBytes_Type = Counter64
_JnxCosQstatRateLimitDropBytes_Object = MibTableColumn
jnxCosQstatRateLimitDropBytes = _JnxCosQstatRateLimitDropBytes_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 15, 4, 1, 51),
    _JnxCosQstatRateLimitDropBytes_Type()
)
jnxCosQstatRateLimitDropBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxCosQstatRateLimitDropBytes.setStatus("current")
_JnxCosQstatRateLimitDropByteRate_Type = CounterBasedGauge64
_JnxCosQstatRateLimitDropByteRate_Object = MibTableColumn
jnxCosQstatRateLimitDropByteRate = _JnxCosQstatRateLimitDropByteRate_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 15, 4, 1, 52),
    _JnxCosQstatRateLimitDropByteRate_Type()
)
jnxCosQstatRateLimitDropByteRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxCosQstatRateLimitDropByteRate.setStatus("current")
_JnxCosQstatTotalDropPkts_Type = Counter64
_JnxCosQstatTotalDropPkts_Object = MibTableColumn
jnxCosQstatTotalDropPkts = _JnxCosQstatTotalDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 15, 4, 1, 53),
    _JnxCosQstatTotalDropPkts_Type()
)
jnxCosQstatTotalDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxCosQstatTotalDropPkts.setStatus("current")
_JnxCosQstatTotalDropPktRate_Type = CounterBasedGauge64
_JnxCosQstatTotalDropPktRate_Object = MibTableColumn
jnxCosQstatTotalDropPktRate = _JnxCosQstatTotalDropPktRate_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 15, 4, 1, 54),
    _JnxCosQstatTotalDropPktRate_Type()
)
jnxCosQstatTotalDropPktRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxCosQstatTotalDropPktRate.setStatus("current")
_JnxCosQstatTotalDropBytes_Type = Counter64
_JnxCosQstatTotalDropBytes_Object = MibTableColumn
jnxCosQstatTotalDropBytes = _JnxCosQstatTotalDropBytes_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 15, 4, 1, 55),
    _JnxCosQstatTotalDropBytes_Type()
)
jnxCosQstatTotalDropBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxCosQstatTotalDropBytes.setStatus("current")
_JnxCosQstatTotalDropByteRate_Type = CounterBasedGauge64
_JnxCosQstatTotalDropByteRate_Object = MibTableColumn
jnxCosQstatTotalDropByteRate = _JnxCosQstatTotalDropByteRate_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 15, 4, 1, 56),
    _JnxCosQstatTotalDropByteRate_Type()
)
jnxCosQstatTotalDropByteRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxCosQstatTotalDropByteRate.setStatus("current")
_JnxCosQstatDepthAverage_Type = CounterBasedGauge64
_JnxCosQstatDepthAverage_Object = MibTableColumn
jnxCosQstatDepthAverage = _JnxCosQstatDepthAverage_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 15, 4, 1, 57),
    _JnxCosQstatDepthAverage_Type()
)
jnxCosQstatDepthAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxCosQstatDepthAverage.setStatus("current")
_JnxCosQstatDepthCurrent_Type = CounterBasedGauge64
_JnxCosQstatDepthCurrent_Object = MibTableColumn
jnxCosQstatDepthCurrent = _JnxCosQstatDepthCurrent_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 15, 4, 1, 58),
    _JnxCosQstatDepthCurrent_Type()
)
jnxCosQstatDepthCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxCosQstatDepthCurrent.setStatus("current")
_JnxCosQstatDepthPeak_Type = CounterBasedGauge64
_JnxCosQstatDepthPeak_Object = MibTableColumn
jnxCosQstatDepthPeak = _JnxCosQstatDepthPeak_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 15, 4, 1, 59),
    _JnxCosQstatDepthPeak_Type()
)
jnxCosQstatDepthPeak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxCosQstatDepthPeak.setStatus("current")
_JnxCosQstatDepthMax_Type = CounterBasedGauge64
_JnxCosQstatDepthMax_Object = MibTableColumn
jnxCosQstatDepthMax = _JnxCosQstatDepthMax_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 15, 4, 1, 60),
    _JnxCosQstatDepthMax_Type()
)
jnxCosQstatDepthMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxCosQstatDepthMax.setStatus("current")
_JnxCosIfstatFlagTable_Object = MibTable
jnxCosIfstatFlagTable = _JnxCosIfstatFlagTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 15, 5)
)
if mibBuilder.loadTexts:
    jnxCosIfstatFlagTable.setStatus("current")
_JnxCosIfstatFlagEntry_Object = MibTableRow
jnxCosIfstatFlagEntry = _JnxCosIfstatFlagEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 15, 5, 1)
)
jnxCosIfstatFlagEntry.setIndexNames(
    (0, "JUNIPER-COS-MIB", "jnxCosIfIndex"),
)
if mibBuilder.loadTexts:
    jnxCosIfstatFlagEntry.setStatus("current")
_JnxCosIfIndex_Type = InterfaceIndex
_JnxCosIfIndex_Object = MibTableColumn
jnxCosIfIndex = _JnxCosIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 15, 5, 1, 1),
    _JnxCosIfIndex_Type()
)
jnxCosIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxCosIfIndex.setStatus("current")
_JnxCosIfstatFlags_Type = JnxCosIfstatFlags
_JnxCosIfstatFlags_Object = MibTableColumn
jnxCosIfstatFlags = _JnxCosIfstatFlags_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 15, 5, 1, 2),
    _JnxCosIfstatFlags_Type()
)
jnxCosIfstatFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxCosIfstatFlags.setStatus("current")
_JnxCosInvQstatTable_Object = MibTable
jnxCosInvQstatTable = _JnxCosInvQstatTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 15, 6)
)
if mibBuilder.loadTexts:
    jnxCosInvQstatTable.setStatus("current")
_JnxCosInvQstatEntry_Object = MibTableRow
jnxCosInvQstatEntry = _JnxCosInvQstatEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 15, 6, 1)
)
jnxCosInvQstatEntry.setIndexNames(
    (0, "JUNIPER-COS-MIB", "jnxCosInvQstatQueueNr"),
    (0, "JUNIPER-COS-MIB", "jnxCosInvQstatIfIndex"),
)
if mibBuilder.loadTexts:
    jnxCosInvQstatEntry.setStatus("current")


class _JnxCosInvQstatQueueNr_Type(Integer32):
    """Custom type jnxCosInvQstatQueueNr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_JnxCosInvQstatQueueNr_Type.__name__ = "Integer32"
_JnxCosInvQstatQueueNr_Object = MibTableColumn
jnxCosInvQstatQueueNr = _JnxCosInvQstatQueueNr_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 15, 6, 1, 1),
    _JnxCosInvQstatQueueNr_Type()
)
jnxCosInvQstatQueueNr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxCosInvQstatQueueNr.setStatus("current")
_JnxCosInvQstatIfIndex_Type = InterfaceIndex
_JnxCosInvQstatIfIndex_Object = MibTableColumn
jnxCosInvQstatIfIndex = _JnxCosInvQstatIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 15, 6, 1, 2),
    _JnxCosInvQstatIfIndex_Type()
)
jnxCosInvQstatIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxCosInvQstatIfIndex.setStatus("current")
_JnxCosInvQstatQedPkts_Type = Counter64
_JnxCosInvQstatQedPkts_Object = MibTableColumn
jnxCosInvQstatQedPkts = _JnxCosInvQstatQedPkts_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 15, 6, 1, 3),
    _JnxCosInvQstatQedPkts_Type()
)
jnxCosInvQstatQedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxCosInvQstatQedPkts.setStatus("current")
_JnxCosInvQstatQedPktRate_Type = CounterBasedGauge64
_JnxCosInvQstatQedPktRate_Object = MibTableColumn
jnxCosInvQstatQedPktRate = _JnxCosInvQstatQedPktRate_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 15, 6, 1, 4),
    _JnxCosInvQstatQedPktRate_Type()
)
jnxCosInvQstatQedPktRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxCosInvQstatQedPktRate.setStatus("current")
_JnxCosInvQstatQedBytes_Type = Counter64
_JnxCosInvQstatQedBytes_Object = MibTableColumn
jnxCosInvQstatQedBytes = _JnxCosInvQstatQedBytes_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 15, 6, 1, 5),
    _JnxCosInvQstatQedBytes_Type()
)
jnxCosInvQstatQedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxCosInvQstatQedBytes.setStatus("current")
_JnxCosInvQstatQedByteRate_Type = CounterBasedGauge64
_JnxCosInvQstatQedByteRate_Object = MibTableColumn
jnxCosInvQstatQedByteRate = _JnxCosInvQstatQedByteRate_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 15, 6, 1, 6),
    _JnxCosInvQstatQedByteRate_Type()
)
jnxCosInvQstatQedByteRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxCosInvQstatQedByteRate.setStatus("current")
_JnxCosInvQstatTxedPkts_Type = Counter64
_JnxCosInvQstatTxedPkts_Object = MibTableColumn
jnxCosInvQstatTxedPkts = _JnxCosInvQstatTxedPkts_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 15, 6, 1, 7),
    _JnxCosInvQstatTxedPkts_Type()
)
jnxCosInvQstatTxedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxCosInvQstatTxedPkts.setStatus("current")
_JnxCosInvQstatTxedPktRate_Type = CounterBasedGauge64
_JnxCosInvQstatTxedPktRate_Object = MibTableColumn
jnxCosInvQstatTxedPktRate = _JnxCosInvQstatTxedPktRate_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 15, 6, 1, 8),
    _JnxCosInvQstatTxedPktRate_Type()
)
jnxCosInvQstatTxedPktRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxCosInvQstatTxedPktRate.setStatus("current")
_JnxCosInvQstatTxedBytes_Type = Counter64
_JnxCosInvQstatTxedBytes_Object = MibTableColumn
jnxCosInvQstatTxedBytes = _JnxCosInvQstatTxedBytes_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 15, 6, 1, 9),
    _JnxCosInvQstatTxedBytes_Type()
)
jnxCosInvQstatTxedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxCosInvQstatTxedBytes.setStatus("current")
_JnxCosInvQstatTxedByteRate_Type = CounterBasedGauge64
_JnxCosInvQstatTxedByteRate_Object = MibTableColumn
jnxCosInvQstatTxedByteRate = _JnxCosInvQstatTxedByteRate_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 15, 6, 1, 10),
    _JnxCosInvQstatTxedByteRate_Type()
)
jnxCosInvQstatTxedByteRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxCosInvQstatTxedByteRate.setStatus("current")
_JnxCosInvQstatTailDropPkts_Type = Counter64
_JnxCosInvQstatTailDropPkts_Object = MibTableColumn
jnxCosInvQstatTailDropPkts = _JnxCosInvQstatTailDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 15, 6, 1, 11),
    _JnxCosInvQstatTailDropPkts_Type()
)
jnxCosInvQstatTailDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxCosInvQstatTailDropPkts.setStatus("current")
_JnxCosInvQstatTailDropPktRate_Type = CounterBasedGauge64
_JnxCosInvQstatTailDropPktRate_Object = MibTableColumn
jnxCosInvQstatTailDropPktRate = _JnxCosInvQstatTailDropPktRate_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 15, 6, 1, 12),
    _JnxCosInvQstatTailDropPktRate_Type()
)
jnxCosInvQstatTailDropPktRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxCosInvQstatTailDropPktRate.setStatus("current")
_JnxCosInvQstatTotalRedDropPkts_Type = Counter64
_JnxCosInvQstatTotalRedDropPkts_Object = MibTableColumn
jnxCosInvQstatTotalRedDropPkts = _JnxCosInvQstatTotalRedDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 15, 6, 1, 13),
    _JnxCosInvQstatTotalRedDropPkts_Type()
)
jnxCosInvQstatTotalRedDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxCosInvQstatTotalRedDropPkts.setStatus("current")
_JnxCosInvQstatTotalRedDropPktRate_Type = CounterBasedGauge64
_JnxCosInvQstatTotalRedDropPktRate_Object = MibTableColumn
jnxCosInvQstatTotalRedDropPktRate = _JnxCosInvQstatTotalRedDropPktRate_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 15, 6, 1, 14),
    _JnxCosInvQstatTotalRedDropPktRate_Type()
)
jnxCosInvQstatTotalRedDropPktRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxCosInvQstatTotalRedDropPktRate.setStatus("current")
_JnxCosInvQstatLpNonTcpRedDropPkts_Type = Counter64
_JnxCosInvQstatLpNonTcpRedDropPkts_Object = MibTableColumn
jnxCosInvQstatLpNonTcpRedDropPkts = _JnxCosInvQstatLpNonTcpRedDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 15, 6, 1, 15),
    _JnxCosInvQstatLpNonTcpRedDropPkts_Type()
)
jnxCosInvQstatLpNonTcpRedDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxCosInvQstatLpNonTcpRedDropPkts.setStatus("current")
_JnxCosInvQstatLpNonTcpRDropPktRate_Type = CounterBasedGauge64
_JnxCosInvQstatLpNonTcpRDropPktRate_Object = MibTableColumn
jnxCosInvQstatLpNonTcpRDropPktRate = _JnxCosInvQstatLpNonTcpRDropPktRate_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 15, 6, 1, 16),
    _JnxCosInvQstatLpNonTcpRDropPktRate_Type()
)
jnxCosInvQstatLpNonTcpRDropPktRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxCosInvQstatLpNonTcpRDropPktRate.setStatus("current")
_JnxCosInvQstatLpTcpRedDropPkts_Type = Counter64
_JnxCosInvQstatLpTcpRedDropPkts_Object = MibTableColumn
jnxCosInvQstatLpTcpRedDropPkts = _JnxCosInvQstatLpTcpRedDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 15, 6, 1, 17),
    _JnxCosInvQstatLpTcpRedDropPkts_Type()
)
jnxCosInvQstatLpTcpRedDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxCosInvQstatLpTcpRedDropPkts.setStatus("current")
_JnxCosInvQstatLpTcpRedDropPktRate_Type = CounterBasedGauge64
_JnxCosInvQstatLpTcpRedDropPktRate_Object = MibTableColumn
jnxCosInvQstatLpTcpRedDropPktRate = _JnxCosInvQstatLpTcpRedDropPktRate_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 15, 6, 1, 18),
    _JnxCosInvQstatLpTcpRedDropPktRate_Type()
)
jnxCosInvQstatLpTcpRedDropPktRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxCosInvQstatLpTcpRedDropPktRate.setStatus("current")
_JnxCosInvQstatHpNonTcpRedDropPkts_Type = Counter64
_JnxCosInvQstatHpNonTcpRedDropPkts_Object = MibTableColumn
jnxCosInvQstatHpNonTcpRedDropPkts = _JnxCosInvQstatHpNonTcpRedDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 15, 6, 1, 19),
    _JnxCosInvQstatHpNonTcpRedDropPkts_Type()
)
jnxCosInvQstatHpNonTcpRedDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxCosInvQstatHpNonTcpRedDropPkts.setStatus("current")
_JnxCosInvQstatHpNonTcpRDropPktRate_Type = CounterBasedGauge64
_JnxCosInvQstatHpNonTcpRDropPktRate_Object = MibTableColumn
jnxCosInvQstatHpNonTcpRDropPktRate = _JnxCosInvQstatHpNonTcpRDropPktRate_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 15, 6, 1, 20),
    _JnxCosInvQstatHpNonTcpRDropPktRate_Type()
)
jnxCosInvQstatHpNonTcpRDropPktRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxCosInvQstatHpNonTcpRDropPktRate.setStatus("current")
_JnxCosInvQstatHpTcpRedDropPkts_Type = Counter64
_JnxCosInvQstatHpTcpRedDropPkts_Object = MibTableColumn
jnxCosInvQstatHpTcpRedDropPkts = _JnxCosInvQstatHpTcpRedDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 15, 6, 1, 21),
    _JnxCosInvQstatHpTcpRedDropPkts_Type()
)
jnxCosInvQstatHpTcpRedDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxCosInvQstatHpTcpRedDropPkts.setStatus("current")
_JnxCosInvQstatHpTcpRedDropPktRate_Type = CounterBasedGauge64
_JnxCosInvQstatHpTcpRedDropPktRate_Object = MibTableColumn
jnxCosInvQstatHpTcpRedDropPktRate = _JnxCosInvQstatHpTcpRedDropPktRate_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 15, 6, 1, 22),
    _JnxCosInvQstatHpTcpRedDropPktRate_Type()
)
jnxCosInvQstatHpTcpRedDropPktRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxCosInvQstatHpTcpRedDropPktRate.setStatus("current")
_JnxCosInvQstatTotalRedDropBytes_Type = Counter64
_JnxCosInvQstatTotalRedDropBytes_Object = MibTableColumn
jnxCosInvQstatTotalRedDropBytes = _JnxCosInvQstatTotalRedDropBytes_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 15, 6, 1, 23),
    _JnxCosInvQstatTotalRedDropBytes_Type()
)
jnxCosInvQstatTotalRedDropBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxCosInvQstatTotalRedDropBytes.setStatus("current")
_JnxCosInvQstatTotalRedDropByteRate_Type = CounterBasedGauge64
_JnxCosInvQstatTotalRedDropByteRate_Object = MibTableColumn
jnxCosInvQstatTotalRedDropByteRate = _JnxCosInvQstatTotalRedDropByteRate_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 15, 6, 1, 24),
    _JnxCosInvQstatTotalRedDropByteRate_Type()
)
jnxCosInvQstatTotalRedDropByteRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxCosInvQstatTotalRedDropByteRate.setStatus("current")
_JnxCosInvQstatLpNonTcpRedDropBytes_Type = Counter64
_JnxCosInvQstatLpNonTcpRedDropBytes_Object = MibTableColumn
jnxCosInvQstatLpNonTcpRedDropBytes = _JnxCosInvQstatLpNonTcpRedDropBytes_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 15, 6, 1, 25),
    _JnxCosInvQstatLpNonTcpRedDropBytes_Type()
)
jnxCosInvQstatLpNonTcpRedDropBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxCosInvQstatLpNonTcpRedDropBytes.setStatus("current")
_JnxCosInvQstatLpNonTcpRDropByteRate_Type = CounterBasedGauge64
_JnxCosInvQstatLpNonTcpRDropByteRate_Object = MibTableColumn
jnxCosInvQstatLpNonTcpRDropByteRate = _JnxCosInvQstatLpNonTcpRDropByteRate_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 15, 6, 1, 26),
    _JnxCosInvQstatLpNonTcpRDropByteRate_Type()
)
jnxCosInvQstatLpNonTcpRDropByteRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxCosInvQstatLpNonTcpRDropByteRate.setStatus("current")
_JnxCosInvQstatLpTcpRedDropBytes_Type = Counter64
_JnxCosInvQstatLpTcpRedDropBytes_Object = MibTableColumn
jnxCosInvQstatLpTcpRedDropBytes = _JnxCosInvQstatLpTcpRedDropBytes_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 15, 6, 1, 27),
    _JnxCosInvQstatLpTcpRedDropBytes_Type()
)
jnxCosInvQstatLpTcpRedDropBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxCosInvQstatLpTcpRedDropBytes.setStatus("current")
_JnxCosInvQstatLpTcpRedDropByteRate_Type = CounterBasedGauge64
_JnxCosInvQstatLpTcpRedDropByteRate_Object = MibTableColumn
jnxCosInvQstatLpTcpRedDropByteRate = _JnxCosInvQstatLpTcpRedDropByteRate_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 15, 6, 1, 28),
    _JnxCosInvQstatLpTcpRedDropByteRate_Type()
)
jnxCosInvQstatLpTcpRedDropByteRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxCosInvQstatLpTcpRedDropByteRate.setStatus("current")
_JnxCosInvQstatHpNonTcpRedDropBytes_Type = Counter64
_JnxCosInvQstatHpNonTcpRedDropBytes_Object = MibTableColumn
jnxCosInvQstatHpNonTcpRedDropBytes = _JnxCosInvQstatHpNonTcpRedDropBytes_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 15, 6, 1, 29),
    _JnxCosInvQstatHpNonTcpRedDropBytes_Type()
)
jnxCosInvQstatHpNonTcpRedDropBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxCosInvQstatHpNonTcpRedDropBytes.setStatus("current")
_JnxCosInvQstatHpNonTcpRDropByteRate_Type = CounterBasedGauge64
_JnxCosInvQstatHpNonTcpRDropByteRate_Object = MibTableColumn
jnxCosInvQstatHpNonTcpRDropByteRate = _JnxCosInvQstatHpNonTcpRDropByteRate_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 15, 6, 1, 30),
    _JnxCosInvQstatHpNonTcpRDropByteRate_Type()
)
jnxCosInvQstatHpNonTcpRDropByteRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxCosInvQstatHpNonTcpRDropByteRate.setStatus("current")
_JnxCosInvQstatHpTcpRedDropBytes_Type = Counter64
_JnxCosInvQstatHpTcpRedDropBytes_Object = MibTableColumn
jnxCosInvQstatHpTcpRedDropBytes = _JnxCosInvQstatHpTcpRedDropBytes_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 15, 6, 1, 31),
    _JnxCosInvQstatHpTcpRedDropBytes_Type()
)
jnxCosInvQstatHpTcpRedDropBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxCosInvQstatHpTcpRedDropBytes.setStatus("current")
_JnxCosInvQstatHpTcpRedDropByteRate_Type = CounterBasedGauge64
_JnxCosInvQstatHpTcpRedDropByteRate_Object = MibTableColumn
jnxCosInvQstatHpTcpRedDropByteRate = _JnxCosInvQstatHpTcpRedDropByteRate_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 15, 6, 1, 32),
    _JnxCosInvQstatHpTcpRedDropByteRate_Type()
)
jnxCosInvQstatHpTcpRedDropByteRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxCosInvQstatHpTcpRedDropByteRate.setStatus("current")
_JnxCosInvQstatLpRedDropPkts_Type = Counter64
_JnxCosInvQstatLpRedDropPkts_Object = MibTableColumn
jnxCosInvQstatLpRedDropPkts = _JnxCosInvQstatLpRedDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 15, 6, 1, 33),
    _JnxCosInvQstatLpRedDropPkts_Type()
)
jnxCosInvQstatLpRedDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxCosInvQstatLpRedDropPkts.setStatus("current")
_JnxCosInvQstatLpRedDropPktRate_Type = CounterBasedGauge64
_JnxCosInvQstatLpRedDropPktRate_Object = MibTableColumn
jnxCosInvQstatLpRedDropPktRate = _JnxCosInvQstatLpRedDropPktRate_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 15, 6, 1, 34),
    _JnxCosInvQstatLpRedDropPktRate_Type()
)
jnxCosInvQstatLpRedDropPktRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxCosInvQstatLpRedDropPktRate.setStatus("current")
_JnxCosInvQstatMLpRedDropPkts_Type = Counter64
_JnxCosInvQstatMLpRedDropPkts_Object = MibTableColumn
jnxCosInvQstatMLpRedDropPkts = _JnxCosInvQstatMLpRedDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 15, 6, 1, 35),
    _JnxCosInvQstatMLpRedDropPkts_Type()
)
jnxCosInvQstatMLpRedDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxCosInvQstatMLpRedDropPkts.setStatus("current")
_JnxCosInvQstatMLpRedDropPktRate_Type = CounterBasedGauge64
_JnxCosInvQstatMLpRedDropPktRate_Object = MibTableColumn
jnxCosInvQstatMLpRedDropPktRate = _JnxCosInvQstatMLpRedDropPktRate_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 15, 6, 1, 36),
    _JnxCosInvQstatMLpRedDropPktRate_Type()
)
jnxCosInvQstatMLpRedDropPktRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxCosInvQstatMLpRedDropPktRate.setStatus("current")
_JnxCosInvQstatMHpRedDropPkts_Type = Counter64
_JnxCosInvQstatMHpRedDropPkts_Object = MibTableColumn
jnxCosInvQstatMHpRedDropPkts = _JnxCosInvQstatMHpRedDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 15, 6, 1, 37),
    _JnxCosInvQstatMHpRedDropPkts_Type()
)
jnxCosInvQstatMHpRedDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxCosInvQstatMHpRedDropPkts.setStatus("current")
_JnxCosInvQstatMHpRedDropPktRate_Type = CounterBasedGauge64
_JnxCosInvQstatMHpRedDropPktRate_Object = MibTableColumn
jnxCosInvQstatMHpRedDropPktRate = _JnxCosInvQstatMHpRedDropPktRate_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 15, 6, 1, 38),
    _JnxCosInvQstatMHpRedDropPktRate_Type()
)
jnxCosInvQstatMHpRedDropPktRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxCosInvQstatMHpRedDropPktRate.setStatus("current")
_JnxCosInvQstatHpRedDropPkts_Type = Counter64
_JnxCosInvQstatHpRedDropPkts_Object = MibTableColumn
jnxCosInvQstatHpRedDropPkts = _JnxCosInvQstatHpRedDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 15, 6, 1, 39),
    _JnxCosInvQstatHpRedDropPkts_Type()
)
jnxCosInvQstatHpRedDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxCosInvQstatHpRedDropPkts.setStatus("current")
_JnxCosInvQstatHpRedDropPktRate_Type = CounterBasedGauge64
_JnxCosInvQstatHpRedDropPktRate_Object = MibTableColumn
jnxCosInvQstatHpRedDropPktRate = _JnxCosInvQstatHpRedDropPktRate_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 15, 6, 1, 40),
    _JnxCosInvQstatHpRedDropPktRate_Type()
)
jnxCosInvQstatHpRedDropPktRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxCosInvQstatHpRedDropPktRate.setStatus("current")
_JnxCosInvQstatLpRedDropBytes_Type = Counter64
_JnxCosInvQstatLpRedDropBytes_Object = MibTableColumn
jnxCosInvQstatLpRedDropBytes = _JnxCosInvQstatLpRedDropBytes_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 15, 6, 1, 41),
    _JnxCosInvQstatLpRedDropBytes_Type()
)
jnxCosInvQstatLpRedDropBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxCosInvQstatLpRedDropBytes.setStatus("current")
_JnxCosInvQstatLpRedDropByteRate_Type = CounterBasedGauge64
_JnxCosInvQstatLpRedDropByteRate_Object = MibTableColumn
jnxCosInvQstatLpRedDropByteRate = _JnxCosInvQstatLpRedDropByteRate_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 15, 6, 1, 42),
    _JnxCosInvQstatLpRedDropByteRate_Type()
)
jnxCosInvQstatLpRedDropByteRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxCosInvQstatLpRedDropByteRate.setStatus("current")
_JnxCosInvQstatMLpRedDropBytes_Type = Counter64
_JnxCosInvQstatMLpRedDropBytes_Object = MibTableColumn
jnxCosInvQstatMLpRedDropBytes = _JnxCosInvQstatMLpRedDropBytes_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 15, 6, 1, 43),
    _JnxCosInvQstatMLpRedDropBytes_Type()
)
jnxCosInvQstatMLpRedDropBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxCosInvQstatMLpRedDropBytes.setStatus("current")
_JnxCosInvQstatMLpRedDropByteRate_Type = CounterBasedGauge64
_JnxCosInvQstatMLpRedDropByteRate_Object = MibTableColumn
jnxCosInvQstatMLpRedDropByteRate = _JnxCosInvQstatMLpRedDropByteRate_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 15, 6, 1, 44),
    _JnxCosInvQstatMLpRedDropByteRate_Type()
)
jnxCosInvQstatMLpRedDropByteRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxCosInvQstatMLpRedDropByteRate.setStatus("current")
_JnxCosInvQstatMHpRedDropBytes_Type = Counter64
_JnxCosInvQstatMHpRedDropBytes_Object = MibTableColumn
jnxCosInvQstatMHpRedDropBytes = _JnxCosInvQstatMHpRedDropBytes_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 15, 6, 1, 45),
    _JnxCosInvQstatMHpRedDropBytes_Type()
)
jnxCosInvQstatMHpRedDropBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxCosInvQstatMHpRedDropBytes.setStatus("current")
_JnxCosInvQstatMHpRedDropByteRate_Type = CounterBasedGauge64
_JnxCosInvQstatMHpRedDropByteRate_Object = MibTableColumn
jnxCosInvQstatMHpRedDropByteRate = _JnxCosInvQstatMHpRedDropByteRate_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 15, 6, 1, 46),
    _JnxCosInvQstatMHpRedDropByteRate_Type()
)
jnxCosInvQstatMHpRedDropByteRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxCosInvQstatMHpRedDropByteRate.setStatus("current")
_JnxCosInvQstatHpRedDropBytes_Type = Counter64
_JnxCosInvQstatHpRedDropBytes_Object = MibTableColumn
jnxCosInvQstatHpRedDropBytes = _JnxCosInvQstatHpRedDropBytes_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 15, 6, 1, 47),
    _JnxCosInvQstatHpRedDropBytes_Type()
)
jnxCosInvQstatHpRedDropBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxCosInvQstatHpRedDropBytes.setStatus("current")
_JnxCosInvQstatHpRedDropByteRate_Type = CounterBasedGauge64
_JnxCosInvQstatHpRedDropByteRate_Object = MibTableColumn
jnxCosInvQstatHpRedDropByteRate = _JnxCosInvQstatHpRedDropByteRate_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 15, 6, 1, 48),
    _JnxCosInvQstatHpRedDropByteRate_Type()
)
jnxCosInvQstatHpRedDropByteRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxCosInvQstatHpRedDropByteRate.setStatus("current")
_JnxCosIngressQstatTable_Object = MibTable
jnxCosIngressQstatTable = _JnxCosIngressQstatTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 15, 7)
)
if mibBuilder.loadTexts:
    jnxCosIngressQstatTable.setStatus("current")
_JnxCosIngressQstatEntry_Object = MibTableRow
jnxCosIngressQstatEntry = _JnxCosIngressQstatEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 15, 7, 1)
)
jnxCosIngressQstatEntry.setIndexNames(
    (0, "JUNIPER-COS-MIB", "jnxCosIngressQstatIfIndex"),
    (0, "JUNIPER-COS-MIB", "jnxCosIngressQstatQueueNr"),
)
if mibBuilder.loadTexts:
    jnxCosIngressQstatEntry.setStatus("current")
_JnxCosIngressQstatIfIndex_Type = InterfaceIndex
_JnxCosIngressQstatIfIndex_Object = MibTableColumn
jnxCosIngressQstatIfIndex = _JnxCosIngressQstatIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 15, 7, 1, 1),
    _JnxCosIngressQstatIfIndex_Type()
)
jnxCosIngressQstatIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxCosIngressQstatIfIndex.setStatus("current")


class _JnxCosIngressQstatQueueNr_Type(Integer32):
    """Custom type jnxCosIngressQstatQueueNr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_JnxCosIngressQstatQueueNr_Type.__name__ = "Integer32"
_JnxCosIngressQstatQueueNr_Object = MibTableColumn
jnxCosIngressQstatQueueNr = _JnxCosIngressQstatQueueNr_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 15, 7, 1, 2),
    _JnxCosIngressQstatQueueNr_Type()
)
jnxCosIngressQstatQueueNr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxCosIngressQstatQueueNr.setStatus("current")
_JnxCosIngressQstatQedPkts_Type = Counter64
_JnxCosIngressQstatQedPkts_Object = MibTableColumn
jnxCosIngressQstatQedPkts = _JnxCosIngressQstatQedPkts_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 15, 7, 1, 3),
    _JnxCosIngressQstatQedPkts_Type()
)
jnxCosIngressQstatQedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxCosIngressQstatQedPkts.setStatus("current")
_JnxCosIngressQstatQedPktRate_Type = CounterBasedGauge64
_JnxCosIngressQstatQedPktRate_Object = MibTableColumn
jnxCosIngressQstatQedPktRate = _JnxCosIngressQstatQedPktRate_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 15, 7, 1, 4),
    _JnxCosIngressQstatQedPktRate_Type()
)
jnxCosIngressQstatQedPktRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxCosIngressQstatQedPktRate.setStatus("current")
_JnxCosIngressQstatQedBytes_Type = Counter64
_JnxCosIngressQstatQedBytes_Object = MibTableColumn
jnxCosIngressQstatQedBytes = _JnxCosIngressQstatQedBytes_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 15, 7, 1, 5),
    _JnxCosIngressQstatQedBytes_Type()
)
jnxCosIngressQstatQedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxCosIngressQstatQedBytes.setStatus("current")
_JnxCosIngressQstatQedByteRate_Type = CounterBasedGauge64
_JnxCosIngressQstatQedByteRate_Object = MibTableColumn
jnxCosIngressQstatQedByteRate = _JnxCosIngressQstatQedByteRate_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 15, 7, 1, 6),
    _JnxCosIngressQstatQedByteRate_Type()
)
jnxCosIngressQstatQedByteRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxCosIngressQstatQedByteRate.setStatus("current")
_JnxCosIngressQstatTxedPkts_Type = Counter64
_JnxCosIngressQstatTxedPkts_Object = MibTableColumn
jnxCosIngressQstatTxedPkts = _JnxCosIngressQstatTxedPkts_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 15, 7, 1, 7),
    _JnxCosIngressQstatTxedPkts_Type()
)
jnxCosIngressQstatTxedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxCosIngressQstatTxedPkts.setStatus("current")
_JnxCosIngressQstatTxedPktRate_Type = CounterBasedGauge64
_JnxCosIngressQstatTxedPktRate_Object = MibTableColumn
jnxCosIngressQstatTxedPktRate = _JnxCosIngressQstatTxedPktRate_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 15, 7, 1, 8),
    _JnxCosIngressQstatTxedPktRate_Type()
)
jnxCosIngressQstatTxedPktRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxCosIngressQstatTxedPktRate.setStatus("current")
_JnxCosIngressQstatTxedBytes_Type = Counter64
_JnxCosIngressQstatTxedBytes_Object = MibTableColumn
jnxCosIngressQstatTxedBytes = _JnxCosIngressQstatTxedBytes_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 15, 7, 1, 9),
    _JnxCosIngressQstatTxedBytes_Type()
)
jnxCosIngressQstatTxedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxCosIngressQstatTxedBytes.setStatus("current")
_JnxCosIngressQstatTxedByteRate_Type = CounterBasedGauge64
_JnxCosIngressQstatTxedByteRate_Object = MibTableColumn
jnxCosIngressQstatTxedByteRate = _JnxCosIngressQstatTxedByteRate_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 15, 7, 1, 10),
    _JnxCosIngressQstatTxedByteRate_Type()
)
jnxCosIngressQstatTxedByteRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxCosIngressQstatTxedByteRate.setStatus("current")
_JnxCosIngressQstatTailDropPkts_Type = Counter64
_JnxCosIngressQstatTailDropPkts_Object = MibTableColumn
jnxCosIngressQstatTailDropPkts = _JnxCosIngressQstatTailDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 15, 7, 1, 11),
    _JnxCosIngressQstatTailDropPkts_Type()
)
jnxCosIngressQstatTailDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxCosIngressQstatTailDropPkts.setStatus("current")
_JnxCosIngressQstatTailDropPktRate_Type = CounterBasedGauge64
_JnxCosIngressQstatTailDropPktRate_Object = MibTableColumn
jnxCosIngressQstatTailDropPktRate = _JnxCosIngressQstatTailDropPktRate_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 15, 7, 1, 12),
    _JnxCosIngressQstatTailDropPktRate_Type()
)
jnxCosIngressQstatTailDropPktRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxCosIngressQstatTailDropPktRate.setStatus("current")
_JnxCosIngressQstatTotalRedDropPkts_Type = Counter64
_JnxCosIngressQstatTotalRedDropPkts_Object = MibTableColumn
jnxCosIngressQstatTotalRedDropPkts = _JnxCosIngressQstatTotalRedDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 15, 7, 1, 13),
    _JnxCosIngressQstatTotalRedDropPkts_Type()
)
jnxCosIngressQstatTotalRedDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxCosIngressQstatTotalRedDropPkts.setStatus("current")
_JnxCosIngressQstatTotalRedDropPktRate_Type = CounterBasedGauge64
_JnxCosIngressQstatTotalRedDropPktRate_Object = MibTableColumn
jnxCosIngressQstatTotalRedDropPktRate = _JnxCosIngressQstatTotalRedDropPktRate_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 15, 7, 1, 14),
    _JnxCosIngressQstatTotalRedDropPktRate_Type()
)
jnxCosIngressQstatTotalRedDropPktRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxCosIngressQstatTotalRedDropPktRate.setStatus("current")
_JnxCosIngressQstatLpNonTcpRedDropPkts_Type = Counter64
_JnxCosIngressQstatLpNonTcpRedDropPkts_Object = MibTableColumn
jnxCosIngressQstatLpNonTcpRedDropPkts = _JnxCosIngressQstatLpNonTcpRedDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 15, 7, 1, 15),
    _JnxCosIngressQstatLpNonTcpRedDropPkts_Type()
)
jnxCosIngressQstatLpNonTcpRedDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxCosIngressQstatLpNonTcpRedDropPkts.setStatus("current")
_JnxCosIngressQstatLpNonTcpRDropPktRate_Type = CounterBasedGauge64
_JnxCosIngressQstatLpNonTcpRDropPktRate_Object = MibTableColumn
jnxCosIngressQstatLpNonTcpRDropPktRate = _JnxCosIngressQstatLpNonTcpRDropPktRate_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 15, 7, 1, 16),
    _JnxCosIngressQstatLpNonTcpRDropPktRate_Type()
)
jnxCosIngressQstatLpNonTcpRDropPktRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxCosIngressQstatLpNonTcpRDropPktRate.setStatus("current")
_JnxCosIngressQstatLpTcpRedDropPkts_Type = Counter64
_JnxCosIngressQstatLpTcpRedDropPkts_Object = MibTableColumn
jnxCosIngressQstatLpTcpRedDropPkts = _JnxCosIngressQstatLpTcpRedDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 15, 7, 1, 17),
    _JnxCosIngressQstatLpTcpRedDropPkts_Type()
)
jnxCosIngressQstatLpTcpRedDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxCosIngressQstatLpTcpRedDropPkts.setStatus("current")
_JnxCosIngressQstatLpTcpRedDropPktRate_Type = CounterBasedGauge64
_JnxCosIngressQstatLpTcpRedDropPktRate_Object = MibTableColumn
jnxCosIngressQstatLpTcpRedDropPktRate = _JnxCosIngressQstatLpTcpRedDropPktRate_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 15, 7, 1, 18),
    _JnxCosIngressQstatLpTcpRedDropPktRate_Type()
)
jnxCosIngressQstatLpTcpRedDropPktRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxCosIngressQstatLpTcpRedDropPktRate.setStatus("current")
_JnxCosIngressQstatHpNonTcpRedDropPkts_Type = Counter64
_JnxCosIngressQstatHpNonTcpRedDropPkts_Object = MibTableColumn
jnxCosIngressQstatHpNonTcpRedDropPkts = _JnxCosIngressQstatHpNonTcpRedDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 15, 7, 1, 19),
    _JnxCosIngressQstatHpNonTcpRedDropPkts_Type()
)
jnxCosIngressQstatHpNonTcpRedDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxCosIngressQstatHpNonTcpRedDropPkts.setStatus("current")
_JnxCosIngressQstatHpNonTcpRDropPktRate_Type = CounterBasedGauge64
_JnxCosIngressQstatHpNonTcpRDropPktRate_Object = MibTableColumn
jnxCosIngressQstatHpNonTcpRDropPktRate = _JnxCosIngressQstatHpNonTcpRDropPktRate_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 15, 7, 1, 20),
    _JnxCosIngressQstatHpNonTcpRDropPktRate_Type()
)
jnxCosIngressQstatHpNonTcpRDropPktRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxCosIngressQstatHpNonTcpRDropPktRate.setStatus("current")
_JnxCosIngressQstatHpTcpRedDropPkts_Type = Counter64
_JnxCosIngressQstatHpTcpRedDropPkts_Object = MibTableColumn
jnxCosIngressQstatHpTcpRedDropPkts = _JnxCosIngressQstatHpTcpRedDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 15, 7, 1, 21),
    _JnxCosIngressQstatHpTcpRedDropPkts_Type()
)
jnxCosIngressQstatHpTcpRedDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxCosIngressQstatHpTcpRedDropPkts.setStatus("current")
_JnxCosIngressQstatHpTcpRedDropPktRate_Type = CounterBasedGauge64
_JnxCosIngressQstatHpTcpRedDropPktRate_Object = MibTableColumn
jnxCosIngressQstatHpTcpRedDropPktRate = _JnxCosIngressQstatHpTcpRedDropPktRate_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 15, 7, 1, 22),
    _JnxCosIngressQstatHpTcpRedDropPktRate_Type()
)
jnxCosIngressQstatHpTcpRedDropPktRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxCosIngressQstatHpTcpRedDropPktRate.setStatus("current")
_JnxCosIngressQstatTotalRedDropBytes_Type = Counter64
_JnxCosIngressQstatTotalRedDropBytes_Object = MibTableColumn
jnxCosIngressQstatTotalRedDropBytes = _JnxCosIngressQstatTotalRedDropBytes_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 15, 7, 1, 23),
    _JnxCosIngressQstatTotalRedDropBytes_Type()
)
jnxCosIngressQstatTotalRedDropBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxCosIngressQstatTotalRedDropBytes.setStatus("current")
_JnxCosIngressQstatTotalRedDropByteRate_Type = CounterBasedGauge64
_JnxCosIngressQstatTotalRedDropByteRate_Object = MibTableColumn
jnxCosIngressQstatTotalRedDropByteRate = _JnxCosIngressQstatTotalRedDropByteRate_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 15, 7, 1, 24),
    _JnxCosIngressQstatTotalRedDropByteRate_Type()
)
jnxCosIngressQstatTotalRedDropByteRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxCosIngressQstatTotalRedDropByteRate.setStatus("current")
_JnxCosIngressQstatLpNonTcpRedDropBytes_Type = Counter64
_JnxCosIngressQstatLpNonTcpRedDropBytes_Object = MibTableColumn
jnxCosIngressQstatLpNonTcpRedDropBytes = _JnxCosIngressQstatLpNonTcpRedDropBytes_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 15, 7, 1, 25),
    _JnxCosIngressQstatLpNonTcpRedDropBytes_Type()
)
jnxCosIngressQstatLpNonTcpRedDropBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxCosIngressQstatLpNonTcpRedDropBytes.setStatus("current")
_JnxCosIngressQstatLpNonTcpRDropByteRate_Type = CounterBasedGauge64
_JnxCosIngressQstatLpNonTcpRDropByteRate_Object = MibTableColumn
jnxCosIngressQstatLpNonTcpRDropByteRate = _JnxCosIngressQstatLpNonTcpRDropByteRate_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 15, 7, 1, 26),
    _JnxCosIngressQstatLpNonTcpRDropByteRate_Type()
)
jnxCosIngressQstatLpNonTcpRDropByteRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxCosIngressQstatLpNonTcpRDropByteRate.setStatus("current")
_JnxCosIngressQstatLpTcpRedDropBytes_Type = Counter64
_JnxCosIngressQstatLpTcpRedDropBytes_Object = MibTableColumn
jnxCosIngressQstatLpTcpRedDropBytes = _JnxCosIngressQstatLpTcpRedDropBytes_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 15, 7, 1, 27),
    _JnxCosIngressQstatLpTcpRedDropBytes_Type()
)
jnxCosIngressQstatLpTcpRedDropBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxCosIngressQstatLpTcpRedDropBytes.setStatus("current")
_JnxCosIngressQstatLpTcpRedDropByteRate_Type = CounterBasedGauge64
_JnxCosIngressQstatLpTcpRedDropByteRate_Object = MibTableColumn
jnxCosIngressQstatLpTcpRedDropByteRate = _JnxCosIngressQstatLpTcpRedDropByteRate_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 15, 7, 1, 28),
    _JnxCosIngressQstatLpTcpRedDropByteRate_Type()
)
jnxCosIngressQstatLpTcpRedDropByteRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxCosIngressQstatLpTcpRedDropByteRate.setStatus("current")
_JnxCosIngressQstatHpNonTcpRedDropBytes_Type = Counter64
_JnxCosIngressQstatHpNonTcpRedDropBytes_Object = MibTableColumn
jnxCosIngressQstatHpNonTcpRedDropBytes = _JnxCosIngressQstatHpNonTcpRedDropBytes_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 15, 7, 1, 29),
    _JnxCosIngressQstatHpNonTcpRedDropBytes_Type()
)
jnxCosIngressQstatHpNonTcpRedDropBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxCosIngressQstatHpNonTcpRedDropBytes.setStatus("current")
_JnxCosIngressQstatHpNonTcpRDropByteRate_Type = CounterBasedGauge64
_JnxCosIngressQstatHpNonTcpRDropByteRate_Object = MibTableColumn
jnxCosIngressQstatHpNonTcpRDropByteRate = _JnxCosIngressQstatHpNonTcpRDropByteRate_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 15, 7, 1, 30),
    _JnxCosIngressQstatHpNonTcpRDropByteRate_Type()
)
jnxCosIngressQstatHpNonTcpRDropByteRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxCosIngressQstatHpNonTcpRDropByteRate.setStatus("current")
_JnxCosIngressQstatHpTcpRedDropBytes_Type = Counter64
_JnxCosIngressQstatHpTcpRedDropBytes_Object = MibTableColumn
jnxCosIngressQstatHpTcpRedDropBytes = _JnxCosIngressQstatHpTcpRedDropBytes_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 15, 7, 1, 31),
    _JnxCosIngressQstatHpTcpRedDropBytes_Type()
)
jnxCosIngressQstatHpTcpRedDropBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxCosIngressQstatHpTcpRedDropBytes.setStatus("current")
_JnxCosIngressQstatHpTcpRedDropByteRate_Type = CounterBasedGauge64
_JnxCosIngressQstatHpTcpRedDropByteRate_Object = MibTableColumn
jnxCosIngressQstatHpTcpRedDropByteRate = _JnxCosIngressQstatHpTcpRedDropByteRate_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 15, 7, 1, 32),
    _JnxCosIngressQstatHpTcpRedDropByteRate_Type()
)
jnxCosIngressQstatHpTcpRedDropByteRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxCosIngressQstatHpTcpRedDropByteRate.setStatus("current")
_JnxCosIngressQstatLpRedDropPkts_Type = Counter64
_JnxCosIngressQstatLpRedDropPkts_Object = MibTableColumn
jnxCosIngressQstatLpRedDropPkts = _JnxCosIngressQstatLpRedDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 15, 7, 1, 33),
    _JnxCosIngressQstatLpRedDropPkts_Type()
)
jnxCosIngressQstatLpRedDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxCosIngressQstatLpRedDropPkts.setStatus("current")
_JnxCosIngressQstatLpRedDropPktRate_Type = CounterBasedGauge64
_JnxCosIngressQstatLpRedDropPktRate_Object = MibTableColumn
jnxCosIngressQstatLpRedDropPktRate = _JnxCosIngressQstatLpRedDropPktRate_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 15, 7, 1, 34),
    _JnxCosIngressQstatLpRedDropPktRate_Type()
)
jnxCosIngressQstatLpRedDropPktRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxCosIngressQstatLpRedDropPktRate.setStatus("current")
_JnxCosIngressQstatMLpRedDropPkts_Type = Counter64
_JnxCosIngressQstatMLpRedDropPkts_Object = MibTableColumn
jnxCosIngressQstatMLpRedDropPkts = _JnxCosIngressQstatMLpRedDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 15, 7, 1, 35),
    _JnxCosIngressQstatMLpRedDropPkts_Type()
)
jnxCosIngressQstatMLpRedDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxCosIngressQstatMLpRedDropPkts.setStatus("current")
_JnxCosIngressQstatMLpRedDropPktRate_Type = CounterBasedGauge64
_JnxCosIngressQstatMLpRedDropPktRate_Object = MibTableColumn
jnxCosIngressQstatMLpRedDropPktRate = _JnxCosIngressQstatMLpRedDropPktRate_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 15, 7, 1, 36),
    _JnxCosIngressQstatMLpRedDropPktRate_Type()
)
jnxCosIngressQstatMLpRedDropPktRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxCosIngressQstatMLpRedDropPktRate.setStatus("current")
_JnxCosIngressQstatMHpRedDropPkts_Type = Counter64
_JnxCosIngressQstatMHpRedDropPkts_Object = MibTableColumn
jnxCosIngressQstatMHpRedDropPkts = _JnxCosIngressQstatMHpRedDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 15, 7, 1, 37),
    _JnxCosIngressQstatMHpRedDropPkts_Type()
)
jnxCosIngressQstatMHpRedDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxCosIngressQstatMHpRedDropPkts.setStatus("current")
_JnxCosIngressQstatMHpRedDropPktRate_Type = CounterBasedGauge64
_JnxCosIngressQstatMHpRedDropPktRate_Object = MibTableColumn
jnxCosIngressQstatMHpRedDropPktRate = _JnxCosIngressQstatMHpRedDropPktRate_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 15, 7, 1, 38),
    _JnxCosIngressQstatMHpRedDropPktRate_Type()
)
jnxCosIngressQstatMHpRedDropPktRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxCosIngressQstatMHpRedDropPktRate.setStatus("current")
_JnxCosIngressQstatHpRedDropPkts_Type = Counter64
_JnxCosIngressQstatHpRedDropPkts_Object = MibTableColumn
jnxCosIngressQstatHpRedDropPkts = _JnxCosIngressQstatHpRedDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 15, 7, 1, 39),
    _JnxCosIngressQstatHpRedDropPkts_Type()
)
jnxCosIngressQstatHpRedDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxCosIngressQstatHpRedDropPkts.setStatus("current")
_JnxCosIngressQstatHpRedDropPktRate_Type = CounterBasedGauge64
_JnxCosIngressQstatHpRedDropPktRate_Object = MibTableColumn
jnxCosIngressQstatHpRedDropPktRate = _JnxCosIngressQstatHpRedDropPktRate_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 15, 7, 1, 40),
    _JnxCosIngressQstatHpRedDropPktRate_Type()
)
jnxCosIngressQstatHpRedDropPktRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxCosIngressQstatHpRedDropPktRate.setStatus("current")
_JnxCosIngressQstatLpRedDropBytes_Type = Counter64
_JnxCosIngressQstatLpRedDropBytes_Object = MibTableColumn
jnxCosIngressQstatLpRedDropBytes = _JnxCosIngressQstatLpRedDropBytes_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 15, 7, 1, 41),
    _JnxCosIngressQstatLpRedDropBytes_Type()
)
jnxCosIngressQstatLpRedDropBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxCosIngressQstatLpRedDropBytes.setStatus("current")
_JnxCosIngressQstatLpRedDropByteRate_Type = CounterBasedGauge64
_JnxCosIngressQstatLpRedDropByteRate_Object = MibTableColumn
jnxCosIngressQstatLpRedDropByteRate = _JnxCosIngressQstatLpRedDropByteRate_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 15, 7, 1, 42),
    _JnxCosIngressQstatLpRedDropByteRate_Type()
)
jnxCosIngressQstatLpRedDropByteRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxCosIngressQstatLpRedDropByteRate.setStatus("current")
_JnxCosIngressQstatMLpRedDropBytes_Type = Counter64
_JnxCosIngressQstatMLpRedDropBytes_Object = MibTableColumn
jnxCosIngressQstatMLpRedDropBytes = _JnxCosIngressQstatMLpRedDropBytes_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 15, 7, 1, 43),
    _JnxCosIngressQstatMLpRedDropBytes_Type()
)
jnxCosIngressQstatMLpRedDropBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxCosIngressQstatMLpRedDropBytes.setStatus("current")
_JnxCosIngressQstatMLpRedDropByteRate_Type = CounterBasedGauge64
_JnxCosIngressQstatMLpRedDropByteRate_Object = MibTableColumn
jnxCosIngressQstatMLpRedDropByteRate = _JnxCosIngressQstatMLpRedDropByteRate_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 15, 7, 1, 44),
    _JnxCosIngressQstatMLpRedDropByteRate_Type()
)
jnxCosIngressQstatMLpRedDropByteRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxCosIngressQstatMLpRedDropByteRate.setStatus("current")
_JnxCosIngressQstatMHpRedDropBytes_Type = Counter64
_JnxCosIngressQstatMHpRedDropBytes_Object = MibTableColumn
jnxCosIngressQstatMHpRedDropBytes = _JnxCosIngressQstatMHpRedDropBytes_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 15, 7, 1, 45),
    _JnxCosIngressQstatMHpRedDropBytes_Type()
)
jnxCosIngressQstatMHpRedDropBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxCosIngressQstatMHpRedDropBytes.setStatus("current")
_JnxCosIngressQstatMHpRedDropByteRate_Type = CounterBasedGauge64
_JnxCosIngressQstatMHpRedDropByteRate_Object = MibTableColumn
jnxCosIngressQstatMHpRedDropByteRate = _JnxCosIngressQstatMHpRedDropByteRate_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 15, 7, 1, 46),
    _JnxCosIngressQstatMHpRedDropByteRate_Type()
)
jnxCosIngressQstatMHpRedDropByteRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxCosIngressQstatMHpRedDropByteRate.setStatus("current")
_JnxCosIngressQstatHpRedDropBytes_Type = Counter64
_JnxCosIngressQstatHpRedDropBytes_Object = MibTableColumn
jnxCosIngressQstatHpRedDropBytes = _JnxCosIngressQstatHpRedDropBytes_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 15, 7, 1, 47),
    _JnxCosIngressQstatHpRedDropBytes_Type()
)
jnxCosIngressQstatHpRedDropBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxCosIngressQstatHpRedDropBytes.setStatus("current")
_JnxCosIngressQstatHpRedDropByteRate_Type = CounterBasedGauge64
_JnxCosIngressQstatHpRedDropByteRate_Object = MibTableColumn
jnxCosIngressQstatHpRedDropByteRate = _JnxCosIngressQstatHpRedDropByteRate_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 15, 7, 1, 48),
    _JnxCosIngressQstatHpRedDropByteRate_Type()
)
jnxCosIngressQstatHpRedDropByteRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxCosIngressQstatHpRedDropByteRate.setStatus("current")
_JnxCosIngressQstatDepthAverage_Type = CounterBasedGauge64
_JnxCosIngressQstatDepthAverage_Object = MibTableColumn
jnxCosIngressQstatDepthAverage = _JnxCosIngressQstatDepthAverage_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 15, 7, 1, 49),
    _JnxCosIngressQstatDepthAverage_Type()
)
jnxCosIngressQstatDepthAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxCosIngressQstatDepthAverage.setStatus("current")
_JnxCosIngressQstatDepthCurrent_Type = CounterBasedGauge64
_JnxCosIngressQstatDepthCurrent_Object = MibTableColumn
jnxCosIngressQstatDepthCurrent = _JnxCosIngressQstatDepthCurrent_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 15, 7, 1, 50),
    _JnxCosIngressQstatDepthCurrent_Type()
)
jnxCosIngressQstatDepthCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxCosIngressQstatDepthCurrent.setStatus("current")
_JnxCosIngressQstatDepthPeak_Type = CounterBasedGauge64
_JnxCosIngressQstatDepthPeak_Object = MibTableColumn
jnxCosIngressQstatDepthPeak = _JnxCosIngressQstatDepthPeak_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 15, 7, 1, 51),
    _JnxCosIngressQstatDepthPeak_Type()
)
jnxCosIngressQstatDepthPeak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxCosIngressQstatDepthPeak.setStatus("current")
_JnxCosIngressQstatDepthMax_Type = CounterBasedGauge64
_JnxCosIngressQstatDepthMax_Object = MibTableColumn
jnxCosIngressQstatDepthMax = _JnxCosIngressQstatDepthMax_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 15, 7, 1, 52),
    _JnxCosIngressQstatDepthMax_Type()
)
jnxCosIngressQstatDepthMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxCosIngressQstatDepthMax.setStatus("current")
_JnxCosNotifyVars_ObjectIdentity = ObjectIdentity
jnxCosNotifyVars = _JnxCosNotifyVars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 15, 8)
)
if mibBuilder.loadTexts:
    jnxCosNotifyVars.setStatus("current")
_JnxCosInterfaceName_Type = DisplayString
_JnxCosInterfaceName_Object = MibScalar
jnxCosInterfaceName = _JnxCosInterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 15, 8, 1),
    _JnxCosInterfaceName_Type()
)
jnxCosInterfaceName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxCosInterfaceName.setStatus("current")


class _JnxCosFpcIndex_Type(Integer32):
    """Custom type jnxCosFpcIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_JnxCosFpcIndex_Type.__name__ = "Integer32"
_JnxCosFpcIndex_Object = MibScalar
jnxCosFpcIndex = _JnxCosFpcIndex_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 15, 8, 2),
    _JnxCosFpcIndex_Type()
)
jnxCosFpcIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxCosFpcIndex.setStatus("current")


class _JnxCosPfeIndex_Type(Integer32):
    """Custom type jnxCosPfeIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_JnxCosPfeIndex_Type.__name__ = "Integer32"
_JnxCosPfeIndex_Object = MibScalar
jnxCosPfeIndex = _JnxCosPfeIndex_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 15, 8, 3),
    _JnxCosPfeIndex_Type()
)
jnxCosPfeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxCosPfeIndex.setStatus("current")


class _JnxCosQueueIndex_Type(Integer32):
    """Custom type jnxCosQueueIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_JnxCosQueueIndex_Type.__name__ = "Integer32"
_JnxCosQueueIndex_Object = MibScalar
jnxCosQueueIndex = _JnxCosQueueIndex_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 15, 8, 4),
    _JnxCosQueueIndex_Type()
)
jnxCosQueueIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxCosQueueIndex.setStatus("current")
_JnxCosIfTable_Object = MibTable
jnxCosIfTable = _JnxCosIfTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 15, 9)
)
if mibBuilder.loadTexts:
    jnxCosIfTable.setStatus("current")
_JnxCosIfEntry_Object = MibTableRow
jnxCosIfEntry = _JnxCosIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 15, 9, 1)
)
jnxCosIfEntry.setIndexNames(
    (0, "JUNIPER-COS-MIB", "jnxCosIfIdx"),
)
if mibBuilder.loadTexts:
    jnxCosIfEntry.setStatus("current")
_JnxCosIfIdx_Type = InterfaceIndex
_JnxCosIfIdx_Object = MibTableColumn
jnxCosIfIdx = _JnxCosIfIdx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 15, 9, 1, 1),
    _JnxCosIfIdx_Type()
)
jnxCosIfIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxCosIfIdx.setStatus("current")


class _JnxCosIfsetDescr_Type(DisplayString):
    """Custom type jnxCosIfsetDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_JnxCosIfsetDescr_Type.__name__ = "DisplayString"
_JnxCosIfsetDescr_Object = MibTableColumn
jnxCosIfsetDescr = _JnxCosIfsetDescr_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 15, 9, 1, 2),
    _JnxCosIfsetDescr_Type()
)
jnxCosIfsetDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxCosIfsetDescr.setStatus("current")
_JnxCosIfsetQstatTable_Object = MibTable
jnxCosIfsetQstatTable = _JnxCosIfsetQstatTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 15, 10)
)
if mibBuilder.loadTexts:
    jnxCosIfsetQstatTable.setStatus("current")
_JnxCosIfsetQstatEntry_Object = MibTableRow
jnxCosIfsetQstatEntry = _JnxCosIfsetQstatEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 15, 10, 1)
)
jnxCosIfsetQstatEntry.setIndexNames(
    (0, "JUNIPER-COS-MIB", "jnxCosIfsetQstatChildIfIndex"),
    (0, "JUNIPER-COS-MIB", "jnxCosIfsetQstatQueueNr"),
)
if mibBuilder.loadTexts:
    jnxCosIfsetQstatEntry.setStatus("current")
_JnxCosIfsetQstatChildIfIndex_Type = InterfaceIndex
_JnxCosIfsetQstatChildIfIndex_Object = MibTableColumn
jnxCosIfsetQstatChildIfIndex = _JnxCosIfsetQstatChildIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 15, 10, 1, 1),
    _JnxCosIfsetQstatChildIfIndex_Type()
)
jnxCosIfsetQstatChildIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxCosIfsetQstatChildIfIndex.setStatus("current")


class _JnxCosIfsetQstatQueueNr_Type(Integer32):
    """Custom type jnxCosIfsetQstatQueueNr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_JnxCosIfsetQstatQueueNr_Type.__name__ = "Integer32"
_JnxCosIfsetQstatQueueNr_Object = MibTableColumn
jnxCosIfsetQstatQueueNr = _JnxCosIfsetQstatQueueNr_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 15, 10, 1, 2),
    _JnxCosIfsetQstatQueueNr_Type()
)
jnxCosIfsetQstatQueueNr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxCosIfsetQstatQueueNr.setStatus("current")
_JnxCosIfsetQstatQedPkts_Type = Counter64
_JnxCosIfsetQstatQedPkts_Object = MibTableColumn
jnxCosIfsetQstatQedPkts = _JnxCosIfsetQstatQedPkts_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 15, 10, 1, 3),
    _JnxCosIfsetQstatQedPkts_Type()
)
jnxCosIfsetQstatQedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxCosIfsetQstatQedPkts.setStatus("current")
_JnxCosIfsetQstatQedPktRate_Type = CounterBasedGauge64
_JnxCosIfsetQstatQedPktRate_Object = MibTableColumn
jnxCosIfsetQstatQedPktRate = _JnxCosIfsetQstatQedPktRate_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 15, 10, 1, 4),
    _JnxCosIfsetQstatQedPktRate_Type()
)
jnxCosIfsetQstatQedPktRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxCosIfsetQstatQedPktRate.setStatus("current")
_JnxCosIfsetQstatQedBytes_Type = Counter64
_JnxCosIfsetQstatQedBytes_Object = MibTableColumn
jnxCosIfsetQstatQedBytes = _JnxCosIfsetQstatQedBytes_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 15, 10, 1, 5),
    _JnxCosIfsetQstatQedBytes_Type()
)
jnxCosIfsetQstatQedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxCosIfsetQstatQedBytes.setStatus("current")
_JnxCosIfsetQstatQedByteRate_Type = CounterBasedGauge64
_JnxCosIfsetQstatQedByteRate_Object = MibTableColumn
jnxCosIfsetQstatQedByteRate = _JnxCosIfsetQstatQedByteRate_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 15, 10, 1, 6),
    _JnxCosIfsetQstatQedByteRate_Type()
)
jnxCosIfsetQstatQedByteRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxCosIfsetQstatQedByteRate.setStatus("current")
_JnxCosIfsetQstatTxedPkts_Type = Counter64
_JnxCosIfsetQstatTxedPkts_Object = MibTableColumn
jnxCosIfsetQstatTxedPkts = _JnxCosIfsetQstatTxedPkts_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 15, 10, 1, 7),
    _JnxCosIfsetQstatTxedPkts_Type()
)
jnxCosIfsetQstatTxedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxCosIfsetQstatTxedPkts.setStatus("current")
_JnxCosIfsetQstatTxedPktRate_Type = CounterBasedGauge64
_JnxCosIfsetQstatTxedPktRate_Object = MibTableColumn
jnxCosIfsetQstatTxedPktRate = _JnxCosIfsetQstatTxedPktRate_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 15, 10, 1, 8),
    _JnxCosIfsetQstatTxedPktRate_Type()
)
jnxCosIfsetQstatTxedPktRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxCosIfsetQstatTxedPktRate.setStatus("current")
_JnxCosIfsetQstatTxedBytes_Type = Counter64
_JnxCosIfsetQstatTxedBytes_Object = MibTableColumn
jnxCosIfsetQstatTxedBytes = _JnxCosIfsetQstatTxedBytes_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 15, 10, 1, 9),
    _JnxCosIfsetQstatTxedBytes_Type()
)
jnxCosIfsetQstatTxedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxCosIfsetQstatTxedBytes.setStatus("current")
_JnxCosIfsetQstatTxedByteRate_Type = CounterBasedGauge64
_JnxCosIfsetQstatTxedByteRate_Object = MibTableColumn
jnxCosIfsetQstatTxedByteRate = _JnxCosIfsetQstatTxedByteRate_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 15, 10, 1, 10),
    _JnxCosIfsetQstatTxedByteRate_Type()
)
jnxCosIfsetQstatTxedByteRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxCosIfsetQstatTxedByteRate.setStatus("current")
_JnxCosIfsetQstatTailDropPkts_Type = Counter64
_JnxCosIfsetQstatTailDropPkts_Object = MibTableColumn
jnxCosIfsetQstatTailDropPkts = _JnxCosIfsetQstatTailDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 15, 10, 1, 11),
    _JnxCosIfsetQstatTailDropPkts_Type()
)
jnxCosIfsetQstatTailDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxCosIfsetQstatTailDropPkts.setStatus("current")
_JnxCosIfsetQstatTailDropPktRate_Type = CounterBasedGauge64
_JnxCosIfsetQstatTailDropPktRate_Object = MibTableColumn
jnxCosIfsetQstatTailDropPktRate = _JnxCosIfsetQstatTailDropPktRate_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 15, 10, 1, 12),
    _JnxCosIfsetQstatTailDropPktRate_Type()
)
jnxCosIfsetQstatTailDropPktRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxCosIfsetQstatTailDropPktRate.setStatus("current")
_JnxCosIfsetQstatTotalRedDropPkts_Type = Counter64
_JnxCosIfsetQstatTotalRedDropPkts_Object = MibTableColumn
jnxCosIfsetQstatTotalRedDropPkts = _JnxCosIfsetQstatTotalRedDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 15, 10, 1, 13),
    _JnxCosIfsetQstatTotalRedDropPkts_Type()
)
jnxCosIfsetQstatTotalRedDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxCosIfsetQstatTotalRedDropPkts.setStatus("current")
_JnxCosIfsetQstatTotalRedDropPktRate_Type = CounterBasedGauge64
_JnxCosIfsetQstatTotalRedDropPktRate_Object = MibTableColumn
jnxCosIfsetQstatTotalRedDropPktRate = _JnxCosIfsetQstatTotalRedDropPktRate_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 15, 10, 1, 14),
    _JnxCosIfsetQstatTotalRedDropPktRate_Type()
)
jnxCosIfsetQstatTotalRedDropPktRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxCosIfsetQstatTotalRedDropPktRate.setStatus("current")
_JnxCosIfsetQstatLpNonTcpRedDropPkts_Type = Counter64
_JnxCosIfsetQstatLpNonTcpRedDropPkts_Object = MibTableColumn
jnxCosIfsetQstatLpNonTcpRedDropPkts = _JnxCosIfsetQstatLpNonTcpRedDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 15, 10, 1, 15),
    _JnxCosIfsetQstatLpNonTcpRedDropPkts_Type()
)
jnxCosIfsetQstatLpNonTcpRedDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxCosIfsetQstatLpNonTcpRedDropPkts.setStatus("current")
_JnxCosIfsetQstatLpNonTcpRDropPktRate_Type = CounterBasedGauge64
_JnxCosIfsetQstatLpNonTcpRDropPktRate_Object = MibTableColumn
jnxCosIfsetQstatLpNonTcpRDropPktRate = _JnxCosIfsetQstatLpNonTcpRDropPktRate_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 15, 10, 1, 16),
    _JnxCosIfsetQstatLpNonTcpRDropPktRate_Type()
)
jnxCosIfsetQstatLpNonTcpRDropPktRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxCosIfsetQstatLpNonTcpRDropPktRate.setStatus("current")
_JnxCosIfsetQstatLpTcpRedDropPkts_Type = Counter64
_JnxCosIfsetQstatLpTcpRedDropPkts_Object = MibTableColumn
jnxCosIfsetQstatLpTcpRedDropPkts = _JnxCosIfsetQstatLpTcpRedDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 15, 10, 1, 17),
    _JnxCosIfsetQstatLpTcpRedDropPkts_Type()
)
jnxCosIfsetQstatLpTcpRedDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxCosIfsetQstatLpTcpRedDropPkts.setStatus("current")
_JnxCosIfsetQstatLpTcpRedDropPktRate_Type = CounterBasedGauge64
_JnxCosIfsetQstatLpTcpRedDropPktRate_Object = MibTableColumn
jnxCosIfsetQstatLpTcpRedDropPktRate = _JnxCosIfsetQstatLpTcpRedDropPktRate_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 15, 10, 1, 18),
    _JnxCosIfsetQstatLpTcpRedDropPktRate_Type()
)
jnxCosIfsetQstatLpTcpRedDropPktRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxCosIfsetQstatLpTcpRedDropPktRate.setStatus("current")
_JnxCosIfsetQstatHpNonTcpRedDropPkts_Type = Counter64
_JnxCosIfsetQstatHpNonTcpRedDropPkts_Object = MibTableColumn
jnxCosIfsetQstatHpNonTcpRedDropPkts = _JnxCosIfsetQstatHpNonTcpRedDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 15, 10, 1, 19),
    _JnxCosIfsetQstatHpNonTcpRedDropPkts_Type()
)
jnxCosIfsetQstatHpNonTcpRedDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxCosIfsetQstatHpNonTcpRedDropPkts.setStatus("current")
_JnxCosIfsetQstatHpNonTcpRDropPktRate_Type = CounterBasedGauge64
_JnxCosIfsetQstatHpNonTcpRDropPktRate_Object = MibTableColumn
jnxCosIfsetQstatHpNonTcpRDropPktRate = _JnxCosIfsetQstatHpNonTcpRDropPktRate_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 15, 10, 1, 20),
    _JnxCosIfsetQstatHpNonTcpRDropPktRate_Type()
)
jnxCosIfsetQstatHpNonTcpRDropPktRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxCosIfsetQstatHpNonTcpRDropPktRate.setStatus("current")
_JnxCosIfsetQstatHpTcpRedDropPkts_Type = Counter64
_JnxCosIfsetQstatHpTcpRedDropPkts_Object = MibTableColumn
jnxCosIfsetQstatHpTcpRedDropPkts = _JnxCosIfsetQstatHpTcpRedDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 15, 10, 1, 21),
    _JnxCosIfsetQstatHpTcpRedDropPkts_Type()
)
jnxCosIfsetQstatHpTcpRedDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxCosIfsetQstatHpTcpRedDropPkts.setStatus("current")
_JnxCosIfsetQstatHpTcpRedDropPktRate_Type = CounterBasedGauge64
_JnxCosIfsetQstatHpTcpRedDropPktRate_Object = MibTableColumn
jnxCosIfsetQstatHpTcpRedDropPktRate = _JnxCosIfsetQstatHpTcpRedDropPktRate_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 15, 10, 1, 22),
    _JnxCosIfsetQstatHpTcpRedDropPktRate_Type()
)
jnxCosIfsetQstatHpTcpRedDropPktRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxCosIfsetQstatHpTcpRedDropPktRate.setStatus("current")
_JnxCosIfsetQstatTotalRedDropBytes_Type = Counter64
_JnxCosIfsetQstatTotalRedDropBytes_Object = MibTableColumn
jnxCosIfsetQstatTotalRedDropBytes = _JnxCosIfsetQstatTotalRedDropBytes_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 15, 10, 1, 23),
    _JnxCosIfsetQstatTotalRedDropBytes_Type()
)
jnxCosIfsetQstatTotalRedDropBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxCosIfsetQstatTotalRedDropBytes.setStatus("current")
_JnxCosIfsetQstatTotalRedDropByteRate_Type = CounterBasedGauge64
_JnxCosIfsetQstatTotalRedDropByteRate_Object = MibTableColumn
jnxCosIfsetQstatTotalRedDropByteRate = _JnxCosIfsetQstatTotalRedDropByteRate_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 15, 10, 1, 24),
    _JnxCosIfsetQstatTotalRedDropByteRate_Type()
)
jnxCosIfsetQstatTotalRedDropByteRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxCosIfsetQstatTotalRedDropByteRate.setStatus("current")
_JnxCosIfsetQstatLpNonTcpRedDropBytes_Type = Counter64
_JnxCosIfsetQstatLpNonTcpRedDropBytes_Object = MibTableColumn
jnxCosIfsetQstatLpNonTcpRedDropBytes = _JnxCosIfsetQstatLpNonTcpRedDropBytes_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 15, 10, 1, 25),
    _JnxCosIfsetQstatLpNonTcpRedDropBytes_Type()
)
jnxCosIfsetQstatLpNonTcpRedDropBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxCosIfsetQstatLpNonTcpRedDropBytes.setStatus("current")
_JnxCosIfsetQstatLpNonTcpRDropByteRate_Type = CounterBasedGauge64
_JnxCosIfsetQstatLpNonTcpRDropByteRate_Object = MibTableColumn
jnxCosIfsetQstatLpNonTcpRDropByteRate = _JnxCosIfsetQstatLpNonTcpRDropByteRate_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 15, 10, 1, 26),
    _JnxCosIfsetQstatLpNonTcpRDropByteRate_Type()
)
jnxCosIfsetQstatLpNonTcpRDropByteRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxCosIfsetQstatLpNonTcpRDropByteRate.setStatus("current")
_JnxCosIfsetQstatLpTcpRedDropBytes_Type = Counter64
_JnxCosIfsetQstatLpTcpRedDropBytes_Object = MibTableColumn
jnxCosIfsetQstatLpTcpRedDropBytes = _JnxCosIfsetQstatLpTcpRedDropBytes_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 15, 10, 1, 27),
    _JnxCosIfsetQstatLpTcpRedDropBytes_Type()
)
jnxCosIfsetQstatLpTcpRedDropBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxCosIfsetQstatLpTcpRedDropBytes.setStatus("current")
_JnxCosIfsetQstatLpTcpRedDropByteRate_Type = CounterBasedGauge64
_JnxCosIfsetQstatLpTcpRedDropByteRate_Object = MibTableColumn
jnxCosIfsetQstatLpTcpRedDropByteRate = _JnxCosIfsetQstatLpTcpRedDropByteRate_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 15, 10, 1, 28),
    _JnxCosIfsetQstatLpTcpRedDropByteRate_Type()
)
jnxCosIfsetQstatLpTcpRedDropByteRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxCosIfsetQstatLpTcpRedDropByteRate.setStatus("current")
_JnxCosIfsetQstatHpNonTcpRedDropBytes_Type = Counter64
_JnxCosIfsetQstatHpNonTcpRedDropBytes_Object = MibTableColumn
jnxCosIfsetQstatHpNonTcpRedDropBytes = _JnxCosIfsetQstatHpNonTcpRedDropBytes_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 15, 10, 1, 29),
    _JnxCosIfsetQstatHpNonTcpRedDropBytes_Type()
)
jnxCosIfsetQstatHpNonTcpRedDropBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxCosIfsetQstatHpNonTcpRedDropBytes.setStatus("current")
_JnxCosIfsetQstatHpNonTcpRDropByteRate_Type = CounterBasedGauge64
_JnxCosIfsetQstatHpNonTcpRDropByteRate_Object = MibTableColumn
jnxCosIfsetQstatHpNonTcpRDropByteRate = _JnxCosIfsetQstatHpNonTcpRDropByteRate_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 15, 10, 1, 30),
    _JnxCosIfsetQstatHpNonTcpRDropByteRate_Type()
)
jnxCosIfsetQstatHpNonTcpRDropByteRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxCosIfsetQstatHpNonTcpRDropByteRate.setStatus("current")
_JnxCosIfsetQstatHpTcpRedDropBytes_Type = Counter64
_JnxCosIfsetQstatHpTcpRedDropBytes_Object = MibTableColumn
jnxCosIfsetQstatHpTcpRedDropBytes = _JnxCosIfsetQstatHpTcpRedDropBytes_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 15, 10, 1, 31),
    _JnxCosIfsetQstatHpTcpRedDropBytes_Type()
)
jnxCosIfsetQstatHpTcpRedDropBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxCosIfsetQstatHpTcpRedDropBytes.setStatus("current")
_JnxCosIfsetQstatHpTcpRedDropByteRate_Type = CounterBasedGauge64
_JnxCosIfsetQstatHpTcpRedDropByteRate_Object = MibTableColumn
jnxCosIfsetQstatHpTcpRedDropByteRate = _JnxCosIfsetQstatHpTcpRedDropByteRate_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 15, 10, 1, 32),
    _JnxCosIfsetQstatHpTcpRedDropByteRate_Type()
)
jnxCosIfsetQstatHpTcpRedDropByteRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxCosIfsetQstatHpTcpRedDropByteRate.setStatus("current")
_JnxCosIfsetQstatLpRedDropPkts_Type = Counter64
_JnxCosIfsetQstatLpRedDropPkts_Object = MibTableColumn
jnxCosIfsetQstatLpRedDropPkts = _JnxCosIfsetQstatLpRedDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 15, 10, 1, 33),
    _JnxCosIfsetQstatLpRedDropPkts_Type()
)
jnxCosIfsetQstatLpRedDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxCosIfsetQstatLpRedDropPkts.setStatus("current")
_JnxCosIfsetQstatLpRedDropPktRate_Type = CounterBasedGauge64
_JnxCosIfsetQstatLpRedDropPktRate_Object = MibTableColumn
jnxCosIfsetQstatLpRedDropPktRate = _JnxCosIfsetQstatLpRedDropPktRate_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 15, 10, 1, 34),
    _JnxCosIfsetQstatLpRedDropPktRate_Type()
)
jnxCosIfsetQstatLpRedDropPktRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxCosIfsetQstatLpRedDropPktRate.setStatus("current")
_JnxCosIfsetQstatMLpRedDropPkts_Type = Counter64
_JnxCosIfsetQstatMLpRedDropPkts_Object = MibTableColumn
jnxCosIfsetQstatMLpRedDropPkts = _JnxCosIfsetQstatMLpRedDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 15, 10, 1, 35),
    _JnxCosIfsetQstatMLpRedDropPkts_Type()
)
jnxCosIfsetQstatMLpRedDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxCosIfsetQstatMLpRedDropPkts.setStatus("current")
_JnxCosIfsetQstatMLpRedDropPktRate_Type = CounterBasedGauge64
_JnxCosIfsetQstatMLpRedDropPktRate_Object = MibTableColumn
jnxCosIfsetQstatMLpRedDropPktRate = _JnxCosIfsetQstatMLpRedDropPktRate_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 15, 10, 1, 36),
    _JnxCosIfsetQstatMLpRedDropPktRate_Type()
)
jnxCosIfsetQstatMLpRedDropPktRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxCosIfsetQstatMLpRedDropPktRate.setStatus("current")
_JnxCosIfsetQstatMHpRedDropPkts_Type = Counter64
_JnxCosIfsetQstatMHpRedDropPkts_Object = MibTableColumn
jnxCosIfsetQstatMHpRedDropPkts = _JnxCosIfsetQstatMHpRedDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 15, 10, 1, 37),
    _JnxCosIfsetQstatMHpRedDropPkts_Type()
)
jnxCosIfsetQstatMHpRedDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxCosIfsetQstatMHpRedDropPkts.setStatus("current")
_JnxCosIfsetQstatMHpRedDropPktRate_Type = CounterBasedGauge64
_JnxCosIfsetQstatMHpRedDropPktRate_Object = MibTableColumn
jnxCosIfsetQstatMHpRedDropPktRate = _JnxCosIfsetQstatMHpRedDropPktRate_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 15, 10, 1, 38),
    _JnxCosIfsetQstatMHpRedDropPktRate_Type()
)
jnxCosIfsetQstatMHpRedDropPktRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxCosIfsetQstatMHpRedDropPktRate.setStatus("current")
_JnxCosIfsetQstatHpRedDropPkts_Type = Counter64
_JnxCosIfsetQstatHpRedDropPkts_Object = MibTableColumn
jnxCosIfsetQstatHpRedDropPkts = _JnxCosIfsetQstatHpRedDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 15, 10, 1, 39),
    _JnxCosIfsetQstatHpRedDropPkts_Type()
)
jnxCosIfsetQstatHpRedDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxCosIfsetQstatHpRedDropPkts.setStatus("current")
_JnxCosIfsetQstatHpRedDropPktRate_Type = CounterBasedGauge64
_JnxCosIfsetQstatHpRedDropPktRate_Object = MibTableColumn
jnxCosIfsetQstatHpRedDropPktRate = _JnxCosIfsetQstatHpRedDropPktRate_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 15, 10, 1, 40),
    _JnxCosIfsetQstatHpRedDropPktRate_Type()
)
jnxCosIfsetQstatHpRedDropPktRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxCosIfsetQstatHpRedDropPktRate.setStatus("current")
_JnxCosIfsetQstatLpRedDropBytes_Type = Counter64
_JnxCosIfsetQstatLpRedDropBytes_Object = MibTableColumn
jnxCosIfsetQstatLpRedDropBytes = _JnxCosIfsetQstatLpRedDropBytes_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 15, 10, 1, 41),
    _JnxCosIfsetQstatLpRedDropBytes_Type()
)
jnxCosIfsetQstatLpRedDropBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxCosIfsetQstatLpRedDropBytes.setStatus("current")
_JnxCosIfsetQstatLpRedDropByteRate_Type = CounterBasedGauge64
_JnxCosIfsetQstatLpRedDropByteRate_Object = MibTableColumn
jnxCosIfsetQstatLpRedDropByteRate = _JnxCosIfsetQstatLpRedDropByteRate_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 15, 10, 1, 42),
    _JnxCosIfsetQstatLpRedDropByteRate_Type()
)
jnxCosIfsetQstatLpRedDropByteRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxCosIfsetQstatLpRedDropByteRate.setStatus("current")
_JnxCosIfsetQstatMLpRedDropBytes_Type = Counter64
_JnxCosIfsetQstatMLpRedDropBytes_Object = MibTableColumn
jnxCosIfsetQstatMLpRedDropBytes = _JnxCosIfsetQstatMLpRedDropBytes_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 15, 10, 1, 43),
    _JnxCosIfsetQstatMLpRedDropBytes_Type()
)
jnxCosIfsetQstatMLpRedDropBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxCosIfsetQstatMLpRedDropBytes.setStatus("current")
_JnxCosIfsetQstatMLpRedDropByteRate_Type = CounterBasedGauge64
_JnxCosIfsetQstatMLpRedDropByteRate_Object = MibTableColumn
jnxCosIfsetQstatMLpRedDropByteRate = _JnxCosIfsetQstatMLpRedDropByteRate_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 15, 10, 1, 44),
    _JnxCosIfsetQstatMLpRedDropByteRate_Type()
)
jnxCosIfsetQstatMLpRedDropByteRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxCosIfsetQstatMLpRedDropByteRate.setStatus("current")
_JnxCosIfsetQstatMHpRedDropBytes_Type = Counter64
_JnxCosIfsetQstatMHpRedDropBytes_Object = MibTableColumn
jnxCosIfsetQstatMHpRedDropBytes = _JnxCosIfsetQstatMHpRedDropBytes_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 15, 10, 1, 45),
    _JnxCosIfsetQstatMHpRedDropBytes_Type()
)
jnxCosIfsetQstatMHpRedDropBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxCosIfsetQstatMHpRedDropBytes.setStatus("current")
_JnxCosIfsetQstatMHpRedDropByteRate_Type = CounterBasedGauge64
_JnxCosIfsetQstatMHpRedDropByteRate_Object = MibTableColumn
jnxCosIfsetQstatMHpRedDropByteRate = _JnxCosIfsetQstatMHpRedDropByteRate_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 15, 10, 1, 46),
    _JnxCosIfsetQstatMHpRedDropByteRate_Type()
)
jnxCosIfsetQstatMHpRedDropByteRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxCosIfsetQstatMHpRedDropByteRate.setStatus("current")
_JnxCosIfsetQstatHpRedDropBytes_Type = Counter64
_JnxCosIfsetQstatHpRedDropBytes_Object = MibTableColumn
jnxCosIfsetQstatHpRedDropBytes = _JnxCosIfsetQstatHpRedDropBytes_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 15, 10, 1, 47),
    _JnxCosIfsetQstatHpRedDropBytes_Type()
)
jnxCosIfsetQstatHpRedDropBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxCosIfsetQstatHpRedDropBytes.setStatus("current")
_JnxCosIfsetQstatHpRedDropByteRate_Type = CounterBasedGauge64
_JnxCosIfsetQstatHpRedDropByteRate_Object = MibTableColumn
jnxCosIfsetQstatHpRedDropByteRate = _JnxCosIfsetQstatHpRedDropByteRate_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 15, 10, 1, 48),
    _JnxCosIfsetQstatHpRedDropByteRate_Type()
)
jnxCosIfsetQstatHpRedDropByteRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxCosIfsetQstatHpRedDropByteRate.setStatus("current")
_JnxCosIfsetQstatRateLimitDropPkts_Type = Counter64
_JnxCosIfsetQstatRateLimitDropPkts_Object = MibTableColumn
jnxCosIfsetQstatRateLimitDropPkts = _JnxCosIfsetQstatRateLimitDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 15, 10, 1, 49),
    _JnxCosIfsetQstatRateLimitDropPkts_Type()
)
jnxCosIfsetQstatRateLimitDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxCosIfsetQstatRateLimitDropPkts.setStatus("current")
_JnxCosIfsetQstatRateLimitDropPktRate_Type = CounterBasedGauge64
_JnxCosIfsetQstatRateLimitDropPktRate_Object = MibTableColumn
jnxCosIfsetQstatRateLimitDropPktRate = _JnxCosIfsetQstatRateLimitDropPktRate_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 15, 10, 1, 50),
    _JnxCosIfsetQstatRateLimitDropPktRate_Type()
)
jnxCosIfsetQstatRateLimitDropPktRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxCosIfsetQstatRateLimitDropPktRate.setStatus("current")
_JnxCosIfsetQstatRateLimitDropBytes_Type = Counter64
_JnxCosIfsetQstatRateLimitDropBytes_Object = MibTableColumn
jnxCosIfsetQstatRateLimitDropBytes = _JnxCosIfsetQstatRateLimitDropBytes_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 15, 10, 1, 51),
    _JnxCosIfsetQstatRateLimitDropBytes_Type()
)
jnxCosIfsetQstatRateLimitDropBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxCosIfsetQstatRateLimitDropBytes.setStatus("current")
_JnxCosIfsetQstatRateLimitDropByteRate_Type = CounterBasedGauge64
_JnxCosIfsetQstatRateLimitDropByteRate_Object = MibTableColumn
jnxCosIfsetQstatRateLimitDropByteRate = _JnxCosIfsetQstatRateLimitDropByteRate_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 15, 10, 1, 52),
    _JnxCosIfsetQstatRateLimitDropByteRate_Type()
)
jnxCosIfsetQstatRateLimitDropByteRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxCosIfsetQstatRateLimitDropByteRate.setStatus("current")
_JnxCosNotificationsPrefix_ObjectIdentity = ObjectIdentity
jnxCosNotificationsPrefix = _JnxCosNotificationsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 4, 17, 0)
)
if mibBuilder.loadTexts:
    jnxCosNotificationsPrefix.setStatus("current")

# Managed Objects groups


# Notification objects

jnxCosOutOfDedicatedQueues = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 4, 17, 0, 1)
)
jnxCosOutOfDedicatedQueues.setObjects(
    ("JUNIPER-COS-MIB", "jnxCosInterfaceName")
)
if mibBuilder.loadTexts:
    jnxCosOutOfDedicatedQueues.setStatus(
        "current"
    )

jnxCosAlmostOutOfDedicatedQueues = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 4, 17, 0, 2)
)
jnxCosAlmostOutOfDedicatedQueues.setObjects(
    ("JUNIPER-COS-MIB", "jnxCosInterfaceName")
)
if mibBuilder.loadTexts:
    jnxCosAlmostOutOfDedicatedQueues.setStatus(
        "current"
    )

jnxCosFabricQueueOverflow = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 4, 17, 0, 3)
)
jnxCosFabricQueueOverflow.setObjects(
      *(("JUNIPER-COS-MIB", "jnxCosFpcIndex"),
        ("JUNIPER-COS-MIB", "jnxCosPfeIndex"),
        ("JUNIPER-COS-MIB", "jnxCosQueueIndex"))
)
if mibBuilder.loadTexts:
    jnxCosFabricQueueOverflow.setStatus(
        "current"
    )

jnxCosWanQueueOverflow = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 4, 17, 0, 4)
)
jnxCosWanQueueOverflow.setObjects(
      *(("JUNIPER-COS-MIB", "jnxCosFpcIndex"),
        ("JUNIPER-COS-MIB", "jnxCosInterfaceName"),
        ("JUNIPER-COS-MIB", "jnxCosQueueIndex"))
)
if mibBuilder.loadTexts:
    jnxCosWanQueueOverflow.setStatus(
        "current"
    )

jnxCosFabricQueueOverflowCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 4, 17, 0, 5)
)
jnxCosFabricQueueOverflowCleared.setObjects(
      *(("JUNIPER-COS-MIB", "jnxCosFpcIndex"),
        ("JUNIPER-COS-MIB", "jnxCosPfeIndex"),
        ("JUNIPER-COS-MIB", "jnxCosQueueIndex"))
)
if mibBuilder.loadTexts:
    jnxCosFabricQueueOverflowCleared.setStatus(
        "current"
    )

jnxCosWanQueueOverflowCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 4, 17, 0, 6)
)
jnxCosWanQueueOverflowCleared.setObjects(
      *(("JUNIPER-COS-MIB", "jnxCosFpcIndex"),
        ("JUNIPER-COS-MIB", "jnxCosInterfaceName"),
        ("JUNIPER-COS-MIB", "jnxCosQueueIndex"))
)
if mibBuilder.loadTexts:
    jnxCosWanQueueOverflowCleared.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "JUNIPER-COS-MIB",
    **{"JnxCosAdminString": JnxCosAdminString,
       "JnxCosFcIdentifier": JnxCosFcIdentifier,
       "JnxCosIfstatFlags": JnxCosIfstatFlags,
       "jnxCos": jnxCos,
       "jnxCosIfqStatsTable": jnxCosIfqStatsTable,
       "jnxCosIfqStatsEntry": jnxCosIfqStatsEntry,
       "jnxCosIfqIfIndex": jnxCosIfqIfIndex,
       "jnxCosIfqFc": jnxCosIfqFc,
       "jnxCosIfqQedPkts": jnxCosIfqQedPkts,
       "jnxCosIfqQedPktRate": jnxCosIfqQedPktRate,
       "jnxCosIfqQedBytes": jnxCosIfqQedBytes,
       "jnxCosIfqQedByteRate": jnxCosIfqQedByteRate,
       "jnxCosIfqTxedPkts": jnxCosIfqTxedPkts,
       "jnxCosIfqTxedPktRate": jnxCosIfqTxedPktRate,
       "jnxCosIfqTxedBytes": jnxCosIfqTxedBytes,
       "jnxCosIfqTxedByteRate": jnxCosIfqTxedByteRate,
       "jnxCosIfqTailDropPkts": jnxCosIfqTailDropPkts,
       "jnxCosIfqTailDropPktRate": jnxCosIfqTailDropPktRate,
       "jnxCosIfqTotalRedDropPkts": jnxCosIfqTotalRedDropPkts,
       "jnxCosIfqTotalRedDropPktRate": jnxCosIfqTotalRedDropPktRate,
       "jnxCosIfqLpNonTcpRedDropPkts": jnxCosIfqLpNonTcpRedDropPkts,
       "jnxCosIfqLpNonTcpRedDropPktRate": jnxCosIfqLpNonTcpRedDropPktRate,
       "jnxCosIfqLpTcpRedDropPkts": jnxCosIfqLpTcpRedDropPkts,
       "jnxCosIfqLpTcpRedDropPktRate": jnxCosIfqLpTcpRedDropPktRate,
       "jnxCosIfqHpNonTcpRedDropPkts": jnxCosIfqHpNonTcpRedDropPkts,
       "jnxCosIfqHpNonTcpRedDropPktRate": jnxCosIfqHpNonTcpRedDropPktRate,
       "jnxCosIfqHpTcpRedDropPkts": jnxCosIfqHpTcpRedDropPkts,
       "jnxCosIfqHpTcpRedDropPktRate": jnxCosIfqHpTcpRedDropPktRate,
       "jnxCosIfqTotalRedDropBytes": jnxCosIfqTotalRedDropBytes,
       "jnxCosIfqTotalRedDropByteRate": jnxCosIfqTotalRedDropByteRate,
       "jnxCosIfqLpNonTcpRedDropBytes": jnxCosIfqLpNonTcpRedDropBytes,
       "jnxCosIfqLpNonTcpRedDropByteRate": jnxCosIfqLpNonTcpRedDropByteRate,
       "jnxCosIfqLpTcpRedDropBytes": jnxCosIfqLpTcpRedDropBytes,
       "jnxCosIfqLpTcpRedDropByteRate": jnxCosIfqLpTcpRedDropByteRate,
       "jnxCosIfqHpNonTcpRedDropBytes": jnxCosIfqHpNonTcpRedDropBytes,
       "jnxCosIfqHpNonTcpRedDropByteRate": jnxCosIfqHpNonTcpRedDropByteRate,
       "jnxCosIfqHpTcpRedDropBytes": jnxCosIfqHpTcpRedDropBytes,
       "jnxCosIfqHpTcpRedDropByteRate": jnxCosIfqHpTcpRedDropByteRate,
       "jnxCosFcTable": jnxCosFcTable,
       "jnxCosFcEntry": jnxCosFcEntry,
       "jnxCosFcName": jnxCosFcName,
       "jnxCosFcQueueNr": jnxCosFcQueueNr,
       "jnxCosRestrictedQNr": jnxCosRestrictedQNr,
       "jnxCosFcIdTable": jnxCosFcIdTable,
       "jnxCosFcIdEntry": jnxCosFcIdEntry,
       "jnxCosFcId": jnxCosFcId,
       "jnxCosFcIdToFcName": jnxCosFcIdToFcName,
       "jnxCosFcFabricPriority": jnxCosFcFabricPriority,
       "jnxCosQstatTable": jnxCosQstatTable,
       "jnxCosQstatEntry": jnxCosQstatEntry,
       "jnxCosQstatIfIndex": jnxCosQstatIfIndex,
       "jnxCosQstatQueueNr": jnxCosQstatQueueNr,
       "jnxCosQstatQedPkts": jnxCosQstatQedPkts,
       "jnxCosQstatQedPktRate": jnxCosQstatQedPktRate,
       "jnxCosQstatQedBytes": jnxCosQstatQedBytes,
       "jnxCosQstatQedByteRate": jnxCosQstatQedByteRate,
       "jnxCosQstatTxedPkts": jnxCosQstatTxedPkts,
       "jnxCosQstatTxedPktRate": jnxCosQstatTxedPktRate,
       "jnxCosQstatTxedBytes": jnxCosQstatTxedBytes,
       "jnxCosQstatTxedByteRate": jnxCosQstatTxedByteRate,
       "jnxCosQstatTailDropPkts": jnxCosQstatTailDropPkts,
       "jnxCosQstatTailDropPktRate": jnxCosQstatTailDropPktRate,
       "jnxCosQstatTotalRedDropPkts": jnxCosQstatTotalRedDropPkts,
       "jnxCosQstatTotalRedDropPktRate": jnxCosQstatTotalRedDropPktRate,
       "jnxCosQstatLpNonTcpRedDropPkts": jnxCosQstatLpNonTcpRedDropPkts,
       "jnxCosQstatLpNonTcpRDropPktRate": jnxCosQstatLpNonTcpRDropPktRate,
       "jnxCosQstatLpTcpRedDropPkts": jnxCosQstatLpTcpRedDropPkts,
       "jnxCosQstatLpTcpRedDropPktRate": jnxCosQstatLpTcpRedDropPktRate,
       "jnxCosQstatHpNonTcpRedDropPkts": jnxCosQstatHpNonTcpRedDropPkts,
       "jnxCosQstatHpNonTcpRDropPktRate": jnxCosQstatHpNonTcpRDropPktRate,
       "jnxCosQstatHpTcpRedDropPkts": jnxCosQstatHpTcpRedDropPkts,
       "jnxCosQstatHpTcpRedDropPktRate": jnxCosQstatHpTcpRedDropPktRate,
       "jnxCosQstatTotalRedDropBytes": jnxCosQstatTotalRedDropBytes,
       "jnxCosQstatTotalRedDropByteRate": jnxCosQstatTotalRedDropByteRate,
       "jnxCosQstatLpNonTcpRedDropBytes": jnxCosQstatLpNonTcpRedDropBytes,
       "jnxCosQstatLpNonTcpRDropByteRate": jnxCosQstatLpNonTcpRDropByteRate,
       "jnxCosQstatLpTcpRedDropBytes": jnxCosQstatLpTcpRedDropBytes,
       "jnxCosQstatLpTcpRedDropByteRate": jnxCosQstatLpTcpRedDropByteRate,
       "jnxCosQstatHpNonTcpRedDropBytes": jnxCosQstatHpNonTcpRedDropBytes,
       "jnxCosQstatHpNonTcpRDropByteRate": jnxCosQstatHpNonTcpRDropByteRate,
       "jnxCosQstatHpTcpRedDropBytes": jnxCosQstatHpTcpRedDropBytes,
       "jnxCosQstatHpTcpRedDropByteRate": jnxCosQstatHpTcpRedDropByteRate,
       "jnxCosQstatLpRedDropPkts": jnxCosQstatLpRedDropPkts,
       "jnxCosQstatLpRedDropPktRate": jnxCosQstatLpRedDropPktRate,
       "jnxCosQstatMLpRedDropPkts": jnxCosQstatMLpRedDropPkts,
       "jnxCosQstatMLpRedDropPktRate": jnxCosQstatMLpRedDropPktRate,
       "jnxCosQstatMHpRedDropPkts": jnxCosQstatMHpRedDropPkts,
       "jnxCosQstatMHpRedDropPktRate": jnxCosQstatMHpRedDropPktRate,
       "jnxCosQstatHpRedDropPkts": jnxCosQstatHpRedDropPkts,
       "jnxCosQstatHpRedDropPktRate": jnxCosQstatHpRedDropPktRate,
       "jnxCosQstatLpRedDropBytes": jnxCosQstatLpRedDropBytes,
       "jnxCosQstatLpRedDropByteRate": jnxCosQstatLpRedDropByteRate,
       "jnxCosQstatMLpRedDropBytes": jnxCosQstatMLpRedDropBytes,
       "jnxCosQstatMLpRedDropByteRate": jnxCosQstatMLpRedDropByteRate,
       "jnxCosQstatMHpRedDropBytes": jnxCosQstatMHpRedDropBytes,
       "jnxCosQstatMHpRedDropByteRate": jnxCosQstatMHpRedDropByteRate,
       "jnxCosQstatHpRedDropBytes": jnxCosQstatHpRedDropBytes,
       "jnxCosQstatHpRedDropByteRate": jnxCosQstatHpRedDropByteRate,
       "jnxCosQstatRateLimitDropPkts": jnxCosQstatRateLimitDropPkts,
       "jnxCosQstatRateLimitDropPktRate": jnxCosQstatRateLimitDropPktRate,
       "jnxCosQstatRateLimitDropBytes": jnxCosQstatRateLimitDropBytes,
       "jnxCosQstatRateLimitDropByteRate": jnxCosQstatRateLimitDropByteRate,
       "jnxCosQstatTotalDropPkts": jnxCosQstatTotalDropPkts,
       "jnxCosQstatTotalDropPktRate": jnxCosQstatTotalDropPktRate,
       "jnxCosQstatTotalDropBytes": jnxCosQstatTotalDropBytes,
       "jnxCosQstatTotalDropByteRate": jnxCosQstatTotalDropByteRate,
       "jnxCosQstatDepthAverage": jnxCosQstatDepthAverage,
       "jnxCosQstatDepthCurrent": jnxCosQstatDepthCurrent,
       "jnxCosQstatDepthPeak": jnxCosQstatDepthPeak,
       "jnxCosQstatDepthMax": jnxCosQstatDepthMax,
       "jnxCosIfstatFlagTable": jnxCosIfstatFlagTable,
       "jnxCosIfstatFlagEntry": jnxCosIfstatFlagEntry,
       "jnxCosIfIndex": jnxCosIfIndex,
       "jnxCosIfstatFlags": jnxCosIfstatFlags,
       "jnxCosInvQstatTable": jnxCosInvQstatTable,
       "jnxCosInvQstatEntry": jnxCosInvQstatEntry,
       "jnxCosInvQstatQueueNr": jnxCosInvQstatQueueNr,
       "jnxCosInvQstatIfIndex": jnxCosInvQstatIfIndex,
       "jnxCosInvQstatQedPkts": jnxCosInvQstatQedPkts,
       "jnxCosInvQstatQedPktRate": jnxCosInvQstatQedPktRate,
       "jnxCosInvQstatQedBytes": jnxCosInvQstatQedBytes,
       "jnxCosInvQstatQedByteRate": jnxCosInvQstatQedByteRate,
       "jnxCosInvQstatTxedPkts": jnxCosInvQstatTxedPkts,
       "jnxCosInvQstatTxedPktRate": jnxCosInvQstatTxedPktRate,
       "jnxCosInvQstatTxedBytes": jnxCosInvQstatTxedBytes,
       "jnxCosInvQstatTxedByteRate": jnxCosInvQstatTxedByteRate,
       "jnxCosInvQstatTailDropPkts": jnxCosInvQstatTailDropPkts,
       "jnxCosInvQstatTailDropPktRate": jnxCosInvQstatTailDropPktRate,
       "jnxCosInvQstatTotalRedDropPkts": jnxCosInvQstatTotalRedDropPkts,
       "jnxCosInvQstatTotalRedDropPktRate": jnxCosInvQstatTotalRedDropPktRate,
       "jnxCosInvQstatLpNonTcpRedDropPkts": jnxCosInvQstatLpNonTcpRedDropPkts,
       "jnxCosInvQstatLpNonTcpRDropPktRate": jnxCosInvQstatLpNonTcpRDropPktRate,
       "jnxCosInvQstatLpTcpRedDropPkts": jnxCosInvQstatLpTcpRedDropPkts,
       "jnxCosInvQstatLpTcpRedDropPktRate": jnxCosInvQstatLpTcpRedDropPktRate,
       "jnxCosInvQstatHpNonTcpRedDropPkts": jnxCosInvQstatHpNonTcpRedDropPkts,
       "jnxCosInvQstatHpNonTcpRDropPktRate": jnxCosInvQstatHpNonTcpRDropPktRate,
       "jnxCosInvQstatHpTcpRedDropPkts": jnxCosInvQstatHpTcpRedDropPkts,
       "jnxCosInvQstatHpTcpRedDropPktRate": jnxCosInvQstatHpTcpRedDropPktRate,
       "jnxCosInvQstatTotalRedDropBytes": jnxCosInvQstatTotalRedDropBytes,
       "jnxCosInvQstatTotalRedDropByteRate": jnxCosInvQstatTotalRedDropByteRate,
       "jnxCosInvQstatLpNonTcpRedDropBytes": jnxCosInvQstatLpNonTcpRedDropBytes,
       "jnxCosInvQstatLpNonTcpRDropByteRate": jnxCosInvQstatLpNonTcpRDropByteRate,
       "jnxCosInvQstatLpTcpRedDropBytes": jnxCosInvQstatLpTcpRedDropBytes,
       "jnxCosInvQstatLpTcpRedDropByteRate": jnxCosInvQstatLpTcpRedDropByteRate,
       "jnxCosInvQstatHpNonTcpRedDropBytes": jnxCosInvQstatHpNonTcpRedDropBytes,
       "jnxCosInvQstatHpNonTcpRDropByteRate": jnxCosInvQstatHpNonTcpRDropByteRate,
       "jnxCosInvQstatHpTcpRedDropBytes": jnxCosInvQstatHpTcpRedDropBytes,
       "jnxCosInvQstatHpTcpRedDropByteRate": jnxCosInvQstatHpTcpRedDropByteRate,
       "jnxCosInvQstatLpRedDropPkts": jnxCosInvQstatLpRedDropPkts,
       "jnxCosInvQstatLpRedDropPktRate": jnxCosInvQstatLpRedDropPktRate,
       "jnxCosInvQstatMLpRedDropPkts": jnxCosInvQstatMLpRedDropPkts,
       "jnxCosInvQstatMLpRedDropPktRate": jnxCosInvQstatMLpRedDropPktRate,
       "jnxCosInvQstatMHpRedDropPkts": jnxCosInvQstatMHpRedDropPkts,
       "jnxCosInvQstatMHpRedDropPktRate": jnxCosInvQstatMHpRedDropPktRate,
       "jnxCosInvQstatHpRedDropPkts": jnxCosInvQstatHpRedDropPkts,
       "jnxCosInvQstatHpRedDropPktRate": jnxCosInvQstatHpRedDropPktRate,
       "jnxCosInvQstatLpRedDropBytes": jnxCosInvQstatLpRedDropBytes,
       "jnxCosInvQstatLpRedDropByteRate": jnxCosInvQstatLpRedDropByteRate,
       "jnxCosInvQstatMLpRedDropBytes": jnxCosInvQstatMLpRedDropBytes,
       "jnxCosInvQstatMLpRedDropByteRate": jnxCosInvQstatMLpRedDropByteRate,
       "jnxCosInvQstatMHpRedDropBytes": jnxCosInvQstatMHpRedDropBytes,
       "jnxCosInvQstatMHpRedDropByteRate": jnxCosInvQstatMHpRedDropByteRate,
       "jnxCosInvQstatHpRedDropBytes": jnxCosInvQstatHpRedDropBytes,
       "jnxCosInvQstatHpRedDropByteRate": jnxCosInvQstatHpRedDropByteRate,
       "jnxCosIngressQstatTable": jnxCosIngressQstatTable,
       "jnxCosIngressQstatEntry": jnxCosIngressQstatEntry,
       "jnxCosIngressQstatIfIndex": jnxCosIngressQstatIfIndex,
       "jnxCosIngressQstatQueueNr": jnxCosIngressQstatQueueNr,
       "jnxCosIngressQstatQedPkts": jnxCosIngressQstatQedPkts,
       "jnxCosIngressQstatQedPktRate": jnxCosIngressQstatQedPktRate,
       "jnxCosIngressQstatQedBytes": jnxCosIngressQstatQedBytes,
       "jnxCosIngressQstatQedByteRate": jnxCosIngressQstatQedByteRate,
       "jnxCosIngressQstatTxedPkts": jnxCosIngressQstatTxedPkts,
       "jnxCosIngressQstatTxedPktRate": jnxCosIngressQstatTxedPktRate,
       "jnxCosIngressQstatTxedBytes": jnxCosIngressQstatTxedBytes,
       "jnxCosIngressQstatTxedByteRate": jnxCosIngressQstatTxedByteRate,
       "jnxCosIngressQstatTailDropPkts": jnxCosIngressQstatTailDropPkts,
       "jnxCosIngressQstatTailDropPktRate": jnxCosIngressQstatTailDropPktRate,
       "jnxCosIngressQstatTotalRedDropPkts": jnxCosIngressQstatTotalRedDropPkts,
       "jnxCosIngressQstatTotalRedDropPktRate": jnxCosIngressQstatTotalRedDropPktRate,
       "jnxCosIngressQstatLpNonTcpRedDropPkts": jnxCosIngressQstatLpNonTcpRedDropPkts,
       "jnxCosIngressQstatLpNonTcpRDropPktRate": jnxCosIngressQstatLpNonTcpRDropPktRate,
       "jnxCosIngressQstatLpTcpRedDropPkts": jnxCosIngressQstatLpTcpRedDropPkts,
       "jnxCosIngressQstatLpTcpRedDropPktRate": jnxCosIngressQstatLpTcpRedDropPktRate,
       "jnxCosIngressQstatHpNonTcpRedDropPkts": jnxCosIngressQstatHpNonTcpRedDropPkts,
       "jnxCosIngressQstatHpNonTcpRDropPktRate": jnxCosIngressQstatHpNonTcpRDropPktRate,
       "jnxCosIngressQstatHpTcpRedDropPkts": jnxCosIngressQstatHpTcpRedDropPkts,
       "jnxCosIngressQstatHpTcpRedDropPktRate": jnxCosIngressQstatHpTcpRedDropPktRate,
       "jnxCosIngressQstatTotalRedDropBytes": jnxCosIngressQstatTotalRedDropBytes,
       "jnxCosIngressQstatTotalRedDropByteRate": jnxCosIngressQstatTotalRedDropByteRate,
       "jnxCosIngressQstatLpNonTcpRedDropBytes": jnxCosIngressQstatLpNonTcpRedDropBytes,
       "jnxCosIngressQstatLpNonTcpRDropByteRate": jnxCosIngressQstatLpNonTcpRDropByteRate,
       "jnxCosIngressQstatLpTcpRedDropBytes": jnxCosIngressQstatLpTcpRedDropBytes,
       "jnxCosIngressQstatLpTcpRedDropByteRate": jnxCosIngressQstatLpTcpRedDropByteRate,
       "jnxCosIngressQstatHpNonTcpRedDropBytes": jnxCosIngressQstatHpNonTcpRedDropBytes,
       "jnxCosIngressQstatHpNonTcpRDropByteRate": jnxCosIngressQstatHpNonTcpRDropByteRate,
       "jnxCosIngressQstatHpTcpRedDropBytes": jnxCosIngressQstatHpTcpRedDropBytes,
       "jnxCosIngressQstatHpTcpRedDropByteRate": jnxCosIngressQstatHpTcpRedDropByteRate,
       "jnxCosIngressQstatLpRedDropPkts": jnxCosIngressQstatLpRedDropPkts,
       "jnxCosIngressQstatLpRedDropPktRate": jnxCosIngressQstatLpRedDropPktRate,
       "jnxCosIngressQstatMLpRedDropPkts": jnxCosIngressQstatMLpRedDropPkts,
       "jnxCosIngressQstatMLpRedDropPktRate": jnxCosIngressQstatMLpRedDropPktRate,
       "jnxCosIngressQstatMHpRedDropPkts": jnxCosIngressQstatMHpRedDropPkts,
       "jnxCosIngressQstatMHpRedDropPktRate": jnxCosIngressQstatMHpRedDropPktRate,
       "jnxCosIngressQstatHpRedDropPkts": jnxCosIngressQstatHpRedDropPkts,
       "jnxCosIngressQstatHpRedDropPktRate": jnxCosIngressQstatHpRedDropPktRate,
       "jnxCosIngressQstatLpRedDropBytes": jnxCosIngressQstatLpRedDropBytes,
       "jnxCosIngressQstatLpRedDropByteRate": jnxCosIngressQstatLpRedDropByteRate,
       "jnxCosIngressQstatMLpRedDropBytes": jnxCosIngressQstatMLpRedDropBytes,
       "jnxCosIngressQstatMLpRedDropByteRate": jnxCosIngressQstatMLpRedDropByteRate,
       "jnxCosIngressQstatMHpRedDropBytes": jnxCosIngressQstatMHpRedDropBytes,
       "jnxCosIngressQstatMHpRedDropByteRate": jnxCosIngressQstatMHpRedDropByteRate,
       "jnxCosIngressQstatHpRedDropBytes": jnxCosIngressQstatHpRedDropBytes,
       "jnxCosIngressQstatHpRedDropByteRate": jnxCosIngressQstatHpRedDropByteRate,
       "jnxCosIngressQstatDepthAverage": jnxCosIngressQstatDepthAverage,
       "jnxCosIngressQstatDepthCurrent": jnxCosIngressQstatDepthCurrent,
       "jnxCosIngressQstatDepthPeak": jnxCosIngressQstatDepthPeak,
       "jnxCosIngressQstatDepthMax": jnxCosIngressQstatDepthMax,
       "jnxCosNotifyVars": jnxCosNotifyVars,
       "jnxCosInterfaceName": jnxCosInterfaceName,
       "jnxCosFpcIndex": jnxCosFpcIndex,
       "jnxCosPfeIndex": jnxCosPfeIndex,
       "jnxCosQueueIndex": jnxCosQueueIndex,
       "jnxCosIfTable": jnxCosIfTable,
       "jnxCosIfEntry": jnxCosIfEntry,
       "jnxCosIfIdx": jnxCosIfIdx,
       "jnxCosIfsetDescr": jnxCosIfsetDescr,
       "jnxCosIfsetQstatTable": jnxCosIfsetQstatTable,
       "jnxCosIfsetQstatEntry": jnxCosIfsetQstatEntry,
       "jnxCosIfsetQstatChildIfIndex": jnxCosIfsetQstatChildIfIndex,
       "jnxCosIfsetQstatQueueNr": jnxCosIfsetQstatQueueNr,
       "jnxCosIfsetQstatQedPkts": jnxCosIfsetQstatQedPkts,
       "jnxCosIfsetQstatQedPktRate": jnxCosIfsetQstatQedPktRate,
       "jnxCosIfsetQstatQedBytes": jnxCosIfsetQstatQedBytes,
       "jnxCosIfsetQstatQedByteRate": jnxCosIfsetQstatQedByteRate,
       "jnxCosIfsetQstatTxedPkts": jnxCosIfsetQstatTxedPkts,
       "jnxCosIfsetQstatTxedPktRate": jnxCosIfsetQstatTxedPktRate,
       "jnxCosIfsetQstatTxedBytes": jnxCosIfsetQstatTxedBytes,
       "jnxCosIfsetQstatTxedByteRate": jnxCosIfsetQstatTxedByteRate,
       "jnxCosIfsetQstatTailDropPkts": jnxCosIfsetQstatTailDropPkts,
       "jnxCosIfsetQstatTailDropPktRate": jnxCosIfsetQstatTailDropPktRate,
       "jnxCosIfsetQstatTotalRedDropPkts": jnxCosIfsetQstatTotalRedDropPkts,
       "jnxCosIfsetQstatTotalRedDropPktRate": jnxCosIfsetQstatTotalRedDropPktRate,
       "jnxCosIfsetQstatLpNonTcpRedDropPkts": jnxCosIfsetQstatLpNonTcpRedDropPkts,
       "jnxCosIfsetQstatLpNonTcpRDropPktRate": jnxCosIfsetQstatLpNonTcpRDropPktRate,
       "jnxCosIfsetQstatLpTcpRedDropPkts": jnxCosIfsetQstatLpTcpRedDropPkts,
       "jnxCosIfsetQstatLpTcpRedDropPktRate": jnxCosIfsetQstatLpTcpRedDropPktRate,
       "jnxCosIfsetQstatHpNonTcpRedDropPkts": jnxCosIfsetQstatHpNonTcpRedDropPkts,
       "jnxCosIfsetQstatHpNonTcpRDropPktRate": jnxCosIfsetQstatHpNonTcpRDropPktRate,
       "jnxCosIfsetQstatHpTcpRedDropPkts": jnxCosIfsetQstatHpTcpRedDropPkts,
       "jnxCosIfsetQstatHpTcpRedDropPktRate": jnxCosIfsetQstatHpTcpRedDropPktRate,
       "jnxCosIfsetQstatTotalRedDropBytes": jnxCosIfsetQstatTotalRedDropBytes,
       "jnxCosIfsetQstatTotalRedDropByteRate": jnxCosIfsetQstatTotalRedDropByteRate,
       "jnxCosIfsetQstatLpNonTcpRedDropBytes": jnxCosIfsetQstatLpNonTcpRedDropBytes,
       "jnxCosIfsetQstatLpNonTcpRDropByteRate": jnxCosIfsetQstatLpNonTcpRDropByteRate,
       "jnxCosIfsetQstatLpTcpRedDropBytes": jnxCosIfsetQstatLpTcpRedDropBytes,
       "jnxCosIfsetQstatLpTcpRedDropByteRate": jnxCosIfsetQstatLpTcpRedDropByteRate,
       "jnxCosIfsetQstatHpNonTcpRedDropBytes": jnxCosIfsetQstatHpNonTcpRedDropBytes,
       "jnxCosIfsetQstatHpNonTcpRDropByteRate": jnxCosIfsetQstatHpNonTcpRDropByteRate,
       "jnxCosIfsetQstatHpTcpRedDropBytes": jnxCosIfsetQstatHpTcpRedDropBytes,
       "jnxCosIfsetQstatHpTcpRedDropByteRate": jnxCosIfsetQstatHpTcpRedDropByteRate,
       "jnxCosIfsetQstatLpRedDropPkts": jnxCosIfsetQstatLpRedDropPkts,
       "jnxCosIfsetQstatLpRedDropPktRate": jnxCosIfsetQstatLpRedDropPktRate,
       "jnxCosIfsetQstatMLpRedDropPkts": jnxCosIfsetQstatMLpRedDropPkts,
       "jnxCosIfsetQstatMLpRedDropPktRate": jnxCosIfsetQstatMLpRedDropPktRate,
       "jnxCosIfsetQstatMHpRedDropPkts": jnxCosIfsetQstatMHpRedDropPkts,
       "jnxCosIfsetQstatMHpRedDropPktRate": jnxCosIfsetQstatMHpRedDropPktRate,
       "jnxCosIfsetQstatHpRedDropPkts": jnxCosIfsetQstatHpRedDropPkts,
       "jnxCosIfsetQstatHpRedDropPktRate": jnxCosIfsetQstatHpRedDropPktRate,
       "jnxCosIfsetQstatLpRedDropBytes": jnxCosIfsetQstatLpRedDropBytes,
       "jnxCosIfsetQstatLpRedDropByteRate": jnxCosIfsetQstatLpRedDropByteRate,
       "jnxCosIfsetQstatMLpRedDropBytes": jnxCosIfsetQstatMLpRedDropBytes,
       "jnxCosIfsetQstatMLpRedDropByteRate": jnxCosIfsetQstatMLpRedDropByteRate,
       "jnxCosIfsetQstatMHpRedDropBytes": jnxCosIfsetQstatMHpRedDropBytes,
       "jnxCosIfsetQstatMHpRedDropByteRate": jnxCosIfsetQstatMHpRedDropByteRate,
       "jnxCosIfsetQstatHpRedDropBytes": jnxCosIfsetQstatHpRedDropBytes,
       "jnxCosIfsetQstatHpRedDropByteRate": jnxCosIfsetQstatHpRedDropByteRate,
       "jnxCosIfsetQstatRateLimitDropPkts": jnxCosIfsetQstatRateLimitDropPkts,
       "jnxCosIfsetQstatRateLimitDropPktRate": jnxCosIfsetQstatRateLimitDropPktRate,
       "jnxCosIfsetQstatRateLimitDropBytes": jnxCosIfsetQstatRateLimitDropBytes,
       "jnxCosIfsetQstatRateLimitDropByteRate": jnxCosIfsetQstatRateLimitDropByteRate,
       "jnxCosNotificationsPrefix": jnxCosNotificationsPrefix,
       "jnxCosOutOfDedicatedQueues": jnxCosOutOfDedicatedQueues,
       "jnxCosAlmostOutOfDedicatedQueues": jnxCosAlmostOutOfDedicatedQueues,
       "jnxCosFabricQueueOverflow": jnxCosFabricQueueOverflow,
       "jnxCosWanQueueOverflow": jnxCosWanQueueOverflow,
       "jnxCosFabricQueueOverflowCleared": jnxCosFabricQueueOverflowCleared,
       "jnxCosWanQueueOverflowCleared": jnxCosWanQueueOverflowCleared}
)
