# SNMP MIB module (BIANCA-BRICK-OSPF-STAT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/BIANCA-BRICK-OSPF-ERR-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:47:35 2024
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
 enterprises,
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
    "enterprises",
    "iso")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Bintec_ObjectIdentity = ObjectIdentity
bintec = _Bintec_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 272)
)
_Bibo_ObjectIdentity = ObjectIdentity
bibo = _Bibo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 272, 4)
)
_Biboip_ObjectIdentity = ObjectIdentity
biboip = _Biboip_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 272, 4, 5)
)
_OspfStat_ObjectIdentity = ObjectIdentity
ospfStat = _OspfStat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 10)
)
_OspfStatHelloRecv_Type = Counter32
_OspfStatHelloRecv_Object = MibScalar
ospfStatHelloRecv = _OspfStatHelloRecv_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 10, 1),
    _OspfStatHelloRecv_Type()
)
ospfStatHelloRecv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfStatHelloRecv.setStatus("mandatory")
_OspfStatHelloSent_Type = Counter32
_OspfStatHelloSent_Object = MibScalar
ospfStatHelloSent = _OspfStatHelloSent_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 10, 2),
    _OspfStatHelloSent_Type()
)
ospfStatHelloSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfStatHelloSent.setStatus("mandatory")
_OspfStatDdRecv_Type = Counter32
_OspfStatDdRecv_Object = MibScalar
ospfStatDdRecv = _OspfStatDdRecv_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 10, 3),
    _OspfStatDdRecv_Type()
)
ospfStatDdRecv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfStatDdRecv.setStatus("mandatory")
_OspfStatDdSent_Type = Counter32
_OspfStatDdSent_Object = MibScalar
ospfStatDdSent = _OspfStatDdSent_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 10, 4),
    _OspfStatDdSent_Type()
)
ospfStatDdSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfStatDdSent.setStatus("mandatory")
_OspfStatLsackRecv_Type = Counter32
_OspfStatLsackRecv_Object = MibScalar
ospfStatLsackRecv = _OspfStatLsackRecv_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 10, 5),
    _OspfStatLsackRecv_Type()
)
ospfStatLsackRecv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfStatLsackRecv.setStatus("mandatory")
_OspfStatLsackSent_Type = Counter32
_OspfStatLsackSent_Object = MibScalar
ospfStatLsackSent = _OspfStatLsackSent_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 10, 6),
    _OspfStatLsackSent_Type()
)
ospfStatLsackSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfStatLsackSent.setStatus("mandatory")
_OspfStatLsreqRecv_Type = Counter32
_OspfStatLsreqRecv_Object = MibScalar
ospfStatLsreqRecv = _OspfStatLsreqRecv_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 10, 7),
    _OspfStatLsreqRecv_Type()
)
ospfStatLsreqRecv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfStatLsreqRecv.setStatus("mandatory")
_OspfStatLsreqSent_Type = Counter32
_OspfStatLsreqSent_Object = MibScalar
ospfStatLsreqSent = _OspfStatLsreqSent_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 10, 8),
    _OspfStatLsreqSent_Type()
)
ospfStatLsreqSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfStatLsreqSent.setStatus("mandatory")
_OspfStatLsupdRecv_Type = Counter32
_OspfStatLsupdRecv_Object = MibScalar
ospfStatLsupdRecv = _OspfStatLsupdRecv_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 10, 9),
    _OspfStatLsupdRecv_Type()
)
ospfStatLsupdRecv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfStatLsupdRecv.setStatus("mandatory")
_OspfStatLsupdSent_Type = Counter32
_OspfStatLsupdSent_Object = MibScalar
ospfStatLsupdSent = _OspfStatLsupdSent_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 10, 10),
    _OspfStatLsupdSent_Type()
)
ospfStatLsupdSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfStatLsupdSent.setStatus("mandatory")
_OspfStatSummaryIncUpd_Type = Counter32
_OspfStatSummaryIncUpd_Object = MibScalar
ospfStatSummaryIncUpd = _OspfStatSummaryIncUpd_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 10, 11),
    _OspfStatSummaryIncUpd_Type()
)
ospfStatSummaryIncUpd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfStatSummaryIncUpd.setStatus("mandatory")
_OspfStatExternalIncUpd_Type = Counter32
_OspfStatExternalIncUpd_Object = MibScalar
ospfStatExternalIncUpd = _OspfStatExternalIncUpd_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 10, 12),
    _OspfStatExternalIncUpd_Type()
)
ospfStatExternalIncUpd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfStatExternalIncUpd.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BIANCA-BRICK-OSPF-STAT-MIB",
    **{"bintec": bintec,
       "bibo": bibo,
       "biboip": biboip,
       "ospfStat": ospfStat,
       "ospfStatHelloRecv": ospfStatHelloRecv,
       "ospfStatHelloSent": ospfStatHelloSent,
       "ospfStatDdRecv": ospfStatDdRecv,
       "ospfStatDdSent": ospfStatDdSent,
       "ospfStatLsackRecv": ospfStatLsackRecv,
       "ospfStatLsackSent": ospfStatLsackSent,
       "ospfStatLsreqRecv": ospfStatLsreqRecv,
       "ospfStatLsreqSent": ospfStatLsreqSent,
       "ospfStatLsupdRecv": ospfStatLsupdRecv,
       "ospfStatLsupdSent": ospfStatLsupdSent,
       "ospfStatSummaryIncUpd": ospfStatSummaryIncUpd,
       "ospfStatExternalIncUpd": ospfStatExternalIncUpd}
)
