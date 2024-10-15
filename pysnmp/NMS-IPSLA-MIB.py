# SNMP MIB module (NMS-IPSLA-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/NMS-IPSLA-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:27:59 2024
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

(nmsMgmt,) = mibBuilder.importSymbols(
    "NMS-SMI",
    "nmsMgmt")

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
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

nmsIpslaMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11606, 10, 9, 102)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_NmsIpslaJitterObjects_ObjectIdentity = ObjectIdentity
nmsIpslaJitterObjects = _NmsIpslaJitterObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11606, 10, 9, 102, 1)
)
_IpslaJitterTable_Object = MibTable
ipslaJitterTable = _IpslaJitterTable_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 9, 102, 1, 1)
)
if mibBuilder.loadTexts:
    ipslaJitterTable.setStatus("mandatory")
_NmsIpslaJitterEntry_Object = MibTableRow
nmsIpslaJitterEntry = _NmsIpslaJitterEntry_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 9, 102, 1, 1, 1)
)
nmsIpslaJitterEntry.setIndexNames(
    (0, "NMS-IPSLA-MIB", "nmsIpslaJobEntryIndex"),
)
if mibBuilder.loadTexts:
    nmsIpslaJitterEntry.setStatus("mandatory")
_NmsIpslaJobEntryIndex_Type = Integer32
_NmsIpslaJobEntryIndex_Object = MibTableColumn
nmsIpslaJobEntryIndex = _NmsIpslaJobEntryIndex_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 9, 102, 1, 1, 1, 1),
    _NmsIpslaJobEntryIndex_Type()
)
nmsIpslaJobEntryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmsIpslaJobEntryIndex.setStatus("mandatory")
_NmsIpslaJobSuccesses_Type = Integer32
_NmsIpslaJobSuccesses_Object = MibTableColumn
nmsIpslaJobSuccesses = _NmsIpslaJobSuccesses_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 9, 102, 1, 1, 1, 2),
    _NmsIpslaJobSuccesses_Type()
)
nmsIpslaJobSuccesses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmsIpslaJobSuccesses.setStatus("current")
_NmsIpslaJobFailures_Type = Integer32
_NmsIpslaJobFailures_Object = MibTableColumn
nmsIpslaJobFailures = _NmsIpslaJobFailures_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 9, 102, 1, 1, 1, 3),
    _NmsIpslaJobFailures_Type()
)
nmsIpslaJobFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmsIpslaJobFailures.setStatus("current")
_NmsIpslaJitterSamples_Type = Integer32
_NmsIpslaJitterSamples_Object = MibTableColumn
nmsIpslaJitterSamples = _NmsIpslaJitterSamples_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 9, 102, 1, 1, 1, 4),
    _NmsIpslaJitterSamples_Type()
)
nmsIpslaJitterSamples.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmsIpslaJitterSamples.setStatus("current")
_NmsIpslaJitterSrc2DstMin_Type = Integer32
_NmsIpslaJitterSrc2DstMin_Object = MibTableColumn
nmsIpslaJitterSrc2DstMin = _NmsIpslaJitterSrc2DstMin_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 9, 102, 1, 1, 1, 5),
    _NmsIpslaJitterSrc2DstMin_Type()
)
nmsIpslaJitterSrc2DstMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmsIpslaJitterSrc2DstMin.setStatus("current")
_NmsIpslaJitterSrc2DstMax_Type = Integer32
_NmsIpslaJitterSrc2DstMax_Object = MibTableColumn
nmsIpslaJitterSrc2DstMax = _NmsIpslaJitterSrc2DstMax_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 9, 102, 1, 1, 1, 6),
    _NmsIpslaJitterSrc2DstMax_Type()
)
nmsIpslaJitterSrc2DstMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmsIpslaJitterSrc2DstMax.setStatus("current")
_NmsIpslaJitterSrc2DstAvg_Type = Integer32
_NmsIpslaJitterSrc2DstAvg_Object = MibTableColumn
nmsIpslaJitterSrc2DstAvg = _NmsIpslaJitterSrc2DstAvg_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 9, 102, 1, 1, 1, 7),
    _NmsIpslaJitterSrc2DstAvg_Type()
)
nmsIpslaJitterSrc2DstAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmsIpslaJitterSrc2DstAvg.setStatus("current")
_NmsIpslaJitterDst2SrcMin_Type = Integer32
_NmsIpslaJitterDst2SrcMin_Object = MibTableColumn
nmsIpslaJitterDst2SrcMin = _NmsIpslaJitterDst2SrcMin_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 9, 102, 1, 1, 1, 8),
    _NmsIpslaJitterDst2SrcMin_Type()
)
nmsIpslaJitterDst2SrcMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmsIpslaJitterDst2SrcMin.setStatus("current")
_NmsIpslaJitterDst2SrcMax_Type = Integer32
_NmsIpslaJitterDst2SrcMax_Object = MibTableColumn
nmsIpslaJitterDst2SrcMax = _NmsIpslaJitterDst2SrcMax_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 9, 102, 1, 1, 1, 9),
    _NmsIpslaJitterDst2SrcMax_Type()
)
nmsIpslaJitterDst2SrcMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmsIpslaJitterDst2SrcMax.setStatus("current")
_NmsIpslaJitterDst2SrcAvg_Type = Integer32
_NmsIpslaJitterDst2SrcAvg_Object = MibTableColumn
nmsIpslaJitterDst2SrcAvg = _NmsIpslaJitterDst2SrcAvg_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 9, 102, 1, 1, 1, 10),
    _NmsIpslaJitterDst2SrcAvg_Type()
)
nmsIpslaJitterDst2SrcAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmsIpslaJitterDst2SrcAvg.setStatus("current")
_NmsIpslaJitterRttMin_Type = Integer32
_NmsIpslaJitterRttMin_Object = MibTableColumn
nmsIpslaJitterRttMin = _NmsIpslaJitterRttMin_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 9, 102, 1, 1, 1, 11),
    _NmsIpslaJitterRttMin_Type()
)
nmsIpslaJitterRttMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmsIpslaJitterRttMin.setStatus("current")
_NmsIpslaJitterRttMax_Type = Integer32
_NmsIpslaJitterRttMax_Object = MibTableColumn
nmsIpslaJitterRttMax = _NmsIpslaJitterRttMax_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 9, 102, 1, 1, 1, 12),
    _NmsIpslaJitterRttMax_Type()
)
nmsIpslaJitterRttMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmsIpslaJitterRttMax.setStatus("current")
_NmsIpslaJitterRttAvg_Type = Integer32
_NmsIpslaJitterRttAvg_Object = MibTableColumn
nmsIpslaJitterRttAvg = _NmsIpslaJitterRttAvg_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 9, 102, 1, 1, 1, 13),
    _NmsIpslaJitterRttAvg_Type()
)
nmsIpslaJitterRttAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmsIpslaJitterRttAvg.setStatus("current")
_NmsIpslaEchoObjects_ObjectIdentity = ObjectIdentity
nmsIpslaEchoObjects = _NmsIpslaEchoObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11606, 10, 9, 102, 2)
)
_IpslaEchoTable_Object = MibTable
ipslaEchoTable = _IpslaEchoTable_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 9, 102, 2, 1)
)
if mibBuilder.loadTexts:
    ipslaEchoTable.setStatus("mandatory")
_NmsIpslaEchoEntry_Object = MibTableRow
nmsIpslaEchoEntry = _NmsIpslaEchoEntry_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 9, 102, 2, 1, 1)
)
nmsIpslaEchoEntry.setIndexNames(
    (0, "NMS-IPSLA-MIB", "nmsIpslaEchoTargetPort"),
)
if mibBuilder.loadTexts:
    nmsIpslaEchoEntry.setStatus("mandatory")
_NmsIpslaEchoTargetPort_Type = Integer32
_NmsIpslaEchoTargetPort_Object = MibTableColumn
nmsIpslaEchoTargetPort = _NmsIpslaEchoTargetPort_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 9, 102, 2, 1, 1, 1),
    _NmsIpslaEchoTargetPort_Type()
)
nmsIpslaEchoTargetPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmsIpslaEchoTargetPort.setStatus("mandatory")
_NmsIpslaEchoSourcePort_Type = Integer32
_NmsIpslaEchoSourcePort_Object = MibTableColumn
nmsIpslaEchoSourcePort = _NmsIpslaEchoSourcePort_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 9, 102, 2, 1, 1, 2),
    _NmsIpslaEchoSourcePort_Type()
)
nmsIpslaEchoSourcePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmsIpslaEchoSourcePort.setStatus("current")
_NmsIpslaEchoRtt_Type = Integer32
_NmsIpslaEchoRtt_Object = MibTableColumn
nmsIpslaEchoRtt = _NmsIpslaEchoRtt_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 9, 102, 2, 1, 1, 3),
    _NmsIpslaEchoRtt_Type()
)
nmsIpslaEchoRtt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmsIpslaEchoRtt.setStatus("current")
_NmsIpslaEchoProbeSent_Type = Integer32
_NmsIpslaEchoProbeSent_Object = MibTableColumn
nmsIpslaEchoProbeSent = _NmsIpslaEchoProbeSent_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 9, 102, 2, 1, 1, 4),
    _NmsIpslaEchoProbeSent_Type()
)
nmsIpslaEchoProbeSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmsIpslaEchoProbeSent.setStatus("current")
_NmsIpslaEchoProbeCompletion_Type = Integer32
_NmsIpslaEchoProbeCompletion_Object = MibTableColumn
nmsIpslaEchoProbeCompletion = _NmsIpslaEchoProbeCompletion_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 9, 102, 2, 1, 1, 5),
    _NmsIpslaEchoProbeCompletion_Type()
)
nmsIpslaEchoProbeCompletion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmsIpslaEchoProbeCompletion.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NMS-IPSLA-MIB",
    **{"nmsIpslaMIB": nmsIpslaMIB,
       "nmsIpslaJitterObjects": nmsIpslaJitterObjects,
       "ipslaJitterTable": ipslaJitterTable,
       "nmsIpslaJitterEntry": nmsIpslaJitterEntry,
       "nmsIpslaJobEntryIndex": nmsIpslaJobEntryIndex,
       "nmsIpslaJobSuccesses": nmsIpslaJobSuccesses,
       "nmsIpslaJobFailures": nmsIpslaJobFailures,
       "nmsIpslaJitterSamples": nmsIpslaJitterSamples,
       "nmsIpslaJitterSrc2DstMin": nmsIpslaJitterSrc2DstMin,
       "nmsIpslaJitterSrc2DstMax": nmsIpslaJitterSrc2DstMax,
       "nmsIpslaJitterSrc2DstAvg": nmsIpslaJitterSrc2DstAvg,
       "nmsIpslaJitterDst2SrcMin": nmsIpslaJitterDst2SrcMin,
       "nmsIpslaJitterDst2SrcMax": nmsIpslaJitterDst2SrcMax,
       "nmsIpslaJitterDst2SrcAvg": nmsIpslaJitterDst2SrcAvg,
       "nmsIpslaJitterRttMin": nmsIpslaJitterRttMin,
       "nmsIpslaJitterRttMax": nmsIpslaJitterRttMax,
       "nmsIpslaJitterRttAvg": nmsIpslaJitterRttAvg,
       "nmsIpslaEchoObjects": nmsIpslaEchoObjects,
       "ipslaEchoTable": ipslaEchoTable,
       "nmsIpslaEchoEntry": nmsIpslaEchoEntry,
       "nmsIpslaEchoTargetPort": nmsIpslaEchoTargetPort,
       "nmsIpslaEchoSourcePort": nmsIpslaEchoSourcePort,
       "nmsIpslaEchoRtt": nmsIpslaEchoRtt,
       "nmsIpslaEchoProbeSent": nmsIpslaEchoProbeSent,
       "nmsIpslaEchoProbeCompletion": nmsIpslaEchoProbeCompletion}
)
