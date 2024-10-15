# SNMP MIB module (ZHONE-COM-IP-ICMP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ZHONE-COM-IP-ICMP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:20:15 2024
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

(rdEntry,) = mibBuilder.importSymbols(
    "ZHONE-COM-IP-RD-MIB",
    "rdEntry")

(zhoneIp,
 zhoneModules) = mibBuilder.importSymbols(
    "Zhone",
    "zhoneIp",
    "zhoneModules")


# MODULE-IDENTITY

comIpIcmp = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 6, 55)
)
comIpIcmp.setRevisions(
        ("2000-09-11 16:25",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Icmp_ObjectIdentity = ObjectIdentity
icmp = _Icmp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 5)
)
if mibBuilder.loadTexts:
    icmp.setStatus("current")
_ZhoneIcmpTable_Object = MibTable
zhoneIcmpTable = _ZhoneIcmpTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 5, 1)
)
if mibBuilder.loadTexts:
    zhoneIcmpTable.setStatus("current")
_ZhoneIcmpEntry_Object = MibTableRow
zhoneIcmpEntry = _ZhoneIcmpEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 5, 1, 1)
)
if mibBuilder.loadTexts:
    zhoneIcmpEntry.setStatus("current")
_ZhIcmpInMsgs_Type = Counter32
_ZhIcmpInMsgs_Object = MibTableColumn
zhIcmpInMsgs = _ZhIcmpInMsgs_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 5, 1, 1, 1),
    _ZhIcmpInMsgs_Type()
)
zhIcmpInMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhIcmpInMsgs.setStatus("current")
_ZhIcmpInErrors_Type = Counter32
_ZhIcmpInErrors_Object = MibTableColumn
zhIcmpInErrors = _ZhIcmpInErrors_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 5, 1, 1, 2),
    _ZhIcmpInErrors_Type()
)
zhIcmpInErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhIcmpInErrors.setStatus("current")
_ZhIcmpInDestUnreachs_Type = Counter32
_ZhIcmpInDestUnreachs_Object = MibTableColumn
zhIcmpInDestUnreachs = _ZhIcmpInDestUnreachs_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 5, 1, 1, 3),
    _ZhIcmpInDestUnreachs_Type()
)
zhIcmpInDestUnreachs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhIcmpInDestUnreachs.setStatus("current")
_ZhIcmpInTimeExcds_Type = Counter32
_ZhIcmpInTimeExcds_Object = MibTableColumn
zhIcmpInTimeExcds = _ZhIcmpInTimeExcds_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 5, 1, 1, 4),
    _ZhIcmpInTimeExcds_Type()
)
zhIcmpInTimeExcds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhIcmpInTimeExcds.setStatus("current")
_ZhIcmpInParmProbs_Type = Counter32
_ZhIcmpInParmProbs_Object = MibTableColumn
zhIcmpInParmProbs = _ZhIcmpInParmProbs_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 5, 1, 1, 5),
    _ZhIcmpInParmProbs_Type()
)
zhIcmpInParmProbs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhIcmpInParmProbs.setStatus("current")
_ZhIcmpInSrcQuenchs_Type = Counter32
_ZhIcmpInSrcQuenchs_Object = MibTableColumn
zhIcmpInSrcQuenchs = _ZhIcmpInSrcQuenchs_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 5, 1, 1, 6),
    _ZhIcmpInSrcQuenchs_Type()
)
zhIcmpInSrcQuenchs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhIcmpInSrcQuenchs.setStatus("current")
_ZhIcmpInRedirects_Type = Counter32
_ZhIcmpInRedirects_Object = MibTableColumn
zhIcmpInRedirects = _ZhIcmpInRedirects_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 5, 1, 1, 7),
    _ZhIcmpInRedirects_Type()
)
zhIcmpInRedirects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhIcmpInRedirects.setStatus("current")
_ZhIcmpInEchos_Type = Counter32
_ZhIcmpInEchos_Object = MibTableColumn
zhIcmpInEchos = _ZhIcmpInEchos_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 5, 1, 1, 8),
    _ZhIcmpInEchos_Type()
)
zhIcmpInEchos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhIcmpInEchos.setStatus("current")
_ZhIcmpInEchoReps_Type = Counter32
_ZhIcmpInEchoReps_Object = MibTableColumn
zhIcmpInEchoReps = _ZhIcmpInEchoReps_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 5, 1, 1, 9),
    _ZhIcmpInEchoReps_Type()
)
zhIcmpInEchoReps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhIcmpInEchoReps.setStatus("current")
_ZhIcmpInTimestamps_Type = Counter32
_ZhIcmpInTimestamps_Object = MibTableColumn
zhIcmpInTimestamps = _ZhIcmpInTimestamps_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 5, 1, 1, 10),
    _ZhIcmpInTimestamps_Type()
)
zhIcmpInTimestamps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhIcmpInTimestamps.setStatus("current")
_ZhIcmpInTimestampReps_Type = Counter32
_ZhIcmpInTimestampReps_Object = MibTableColumn
zhIcmpInTimestampReps = _ZhIcmpInTimestampReps_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 5, 1, 1, 11),
    _ZhIcmpInTimestampReps_Type()
)
zhIcmpInTimestampReps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhIcmpInTimestampReps.setStatus("current")
_ZhIcmpInAddrMasks_Type = Counter32
_ZhIcmpInAddrMasks_Object = MibTableColumn
zhIcmpInAddrMasks = _ZhIcmpInAddrMasks_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 5, 1, 1, 12),
    _ZhIcmpInAddrMasks_Type()
)
zhIcmpInAddrMasks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhIcmpInAddrMasks.setStatus("current")
_ZhIcmpInAddrMaskReps_Type = Counter32
_ZhIcmpInAddrMaskReps_Object = MibTableColumn
zhIcmpInAddrMaskReps = _ZhIcmpInAddrMaskReps_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 5, 1, 1, 13),
    _ZhIcmpInAddrMaskReps_Type()
)
zhIcmpInAddrMaskReps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhIcmpInAddrMaskReps.setStatus("current")
_ZhIcmpOutMsgs_Type = Counter32
_ZhIcmpOutMsgs_Object = MibTableColumn
zhIcmpOutMsgs = _ZhIcmpOutMsgs_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 5, 1, 1, 14),
    _ZhIcmpOutMsgs_Type()
)
zhIcmpOutMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhIcmpOutMsgs.setStatus("current")
_ZhIcmpOutErrors_Type = Counter32
_ZhIcmpOutErrors_Object = MibTableColumn
zhIcmpOutErrors = _ZhIcmpOutErrors_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 5, 1, 1, 15),
    _ZhIcmpOutErrors_Type()
)
zhIcmpOutErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhIcmpOutErrors.setStatus("current")
_ZhIcmpOutDestUnreachs_Type = Counter32
_ZhIcmpOutDestUnreachs_Object = MibTableColumn
zhIcmpOutDestUnreachs = _ZhIcmpOutDestUnreachs_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 5, 1, 1, 16),
    _ZhIcmpOutDestUnreachs_Type()
)
zhIcmpOutDestUnreachs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhIcmpOutDestUnreachs.setStatus("current")
_ZhIcmpOutTimeExcds_Type = Counter32
_ZhIcmpOutTimeExcds_Object = MibTableColumn
zhIcmpOutTimeExcds = _ZhIcmpOutTimeExcds_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 5, 1, 1, 17),
    _ZhIcmpOutTimeExcds_Type()
)
zhIcmpOutTimeExcds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhIcmpOutTimeExcds.setStatus("current")
_ZhIcmpOutParmProbs_Type = Counter32
_ZhIcmpOutParmProbs_Object = MibTableColumn
zhIcmpOutParmProbs = _ZhIcmpOutParmProbs_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 5, 1, 1, 18),
    _ZhIcmpOutParmProbs_Type()
)
zhIcmpOutParmProbs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhIcmpOutParmProbs.setStatus("current")
_ZhIcmpOutSrcQuenchs_Type = Counter32
_ZhIcmpOutSrcQuenchs_Object = MibTableColumn
zhIcmpOutSrcQuenchs = _ZhIcmpOutSrcQuenchs_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 5, 1, 1, 19),
    _ZhIcmpOutSrcQuenchs_Type()
)
zhIcmpOutSrcQuenchs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhIcmpOutSrcQuenchs.setStatus("current")
_ZhIcmpOutRedirects_Type = Counter32
_ZhIcmpOutRedirects_Object = MibTableColumn
zhIcmpOutRedirects = _ZhIcmpOutRedirects_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 5, 1, 1, 20),
    _ZhIcmpOutRedirects_Type()
)
zhIcmpOutRedirects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhIcmpOutRedirects.setStatus("current")
_ZhIcmpOutEchos_Type = Counter32
_ZhIcmpOutEchos_Object = MibTableColumn
zhIcmpOutEchos = _ZhIcmpOutEchos_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 5, 1, 1, 21),
    _ZhIcmpOutEchos_Type()
)
zhIcmpOutEchos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhIcmpOutEchos.setStatus("current")
_ZhIcmpOutEchoReps_Type = Counter32
_ZhIcmpOutEchoReps_Object = MibTableColumn
zhIcmpOutEchoReps = _ZhIcmpOutEchoReps_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 5, 1, 1, 22),
    _ZhIcmpOutEchoReps_Type()
)
zhIcmpOutEchoReps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhIcmpOutEchoReps.setStatus("current")
_ZhIcmpOutTimestamps_Type = Counter32
_ZhIcmpOutTimestamps_Object = MibTableColumn
zhIcmpOutTimestamps = _ZhIcmpOutTimestamps_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 5, 1, 1, 23),
    _ZhIcmpOutTimestamps_Type()
)
zhIcmpOutTimestamps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhIcmpOutTimestamps.setStatus("current")
_ZhIcmpOutTimestampReps_Type = Counter32
_ZhIcmpOutTimestampReps_Object = MibTableColumn
zhIcmpOutTimestampReps = _ZhIcmpOutTimestampReps_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 5, 1, 1, 24),
    _ZhIcmpOutTimestampReps_Type()
)
zhIcmpOutTimestampReps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhIcmpOutTimestampReps.setStatus("current")
_ZhIcmpOutAddrMasks_Type = Counter32
_ZhIcmpOutAddrMasks_Object = MibTableColumn
zhIcmpOutAddrMasks = _ZhIcmpOutAddrMasks_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 5, 1, 1, 25),
    _ZhIcmpOutAddrMasks_Type()
)
zhIcmpOutAddrMasks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhIcmpOutAddrMasks.setStatus("current")
_ZhIcmpOutAddrMaskReps_Type = Counter32
_ZhIcmpOutAddrMaskReps_Object = MibTableColumn
zhIcmpOutAddrMaskReps = _ZhIcmpOutAddrMaskReps_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 5, 1, 1, 26),
    _ZhIcmpOutAddrMaskReps_Type()
)
zhIcmpOutAddrMaskReps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhIcmpOutAddrMaskReps.setStatus("current")
rdEntry.registerAugmentions(
    ("ZHONE-COM-IP-ICMP-MIB",
     "zhoneIcmpEntry")
)
zhoneIcmpEntry.setIndexNames(*rdEntry.getIndexNames())

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZHONE-COM-IP-ICMP-MIB",
    **{"icmp": icmp,
       "zhoneIcmpTable": zhoneIcmpTable,
       "zhoneIcmpEntry": zhoneIcmpEntry,
       "zhIcmpInMsgs": zhIcmpInMsgs,
       "zhIcmpInErrors": zhIcmpInErrors,
       "zhIcmpInDestUnreachs": zhIcmpInDestUnreachs,
       "zhIcmpInTimeExcds": zhIcmpInTimeExcds,
       "zhIcmpInParmProbs": zhIcmpInParmProbs,
       "zhIcmpInSrcQuenchs": zhIcmpInSrcQuenchs,
       "zhIcmpInRedirects": zhIcmpInRedirects,
       "zhIcmpInEchos": zhIcmpInEchos,
       "zhIcmpInEchoReps": zhIcmpInEchoReps,
       "zhIcmpInTimestamps": zhIcmpInTimestamps,
       "zhIcmpInTimestampReps": zhIcmpInTimestampReps,
       "zhIcmpInAddrMasks": zhIcmpInAddrMasks,
       "zhIcmpInAddrMaskReps": zhIcmpInAddrMaskReps,
       "zhIcmpOutMsgs": zhIcmpOutMsgs,
       "zhIcmpOutErrors": zhIcmpOutErrors,
       "zhIcmpOutDestUnreachs": zhIcmpOutDestUnreachs,
       "zhIcmpOutTimeExcds": zhIcmpOutTimeExcds,
       "zhIcmpOutParmProbs": zhIcmpOutParmProbs,
       "zhIcmpOutSrcQuenchs": zhIcmpOutSrcQuenchs,
       "zhIcmpOutRedirects": zhIcmpOutRedirects,
       "zhIcmpOutEchos": zhIcmpOutEchos,
       "zhIcmpOutEchoReps": zhIcmpOutEchoReps,
       "zhIcmpOutTimestamps": zhIcmpOutTimestamps,
       "zhIcmpOutTimestampReps": zhIcmpOutTimestampReps,
       "zhIcmpOutAddrMasks": zhIcmpOutAddrMasks,
       "zhIcmpOutAddrMaskReps": zhIcmpOutAddrMaskReps,
       "comIpIcmp": comIpIcmp}
)
