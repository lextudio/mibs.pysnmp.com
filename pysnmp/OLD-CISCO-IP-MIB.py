# SNMP MIB module (OLD-CISCO-IP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/OLD-CISCO-IP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:34:02 2024
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

(local,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "local")

(ipAdEntAddr,) = mibBuilder.importSymbols(
    "IP-MIB",
    "ipAdEntAddr")

(ipRouteDest,) = mibBuilder.importSymbols(
    "RFC1213-MIB",
    "ipRouteDest")

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


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Lip_ObjectIdentity = ObjectIdentity
lip = _Lip_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 2, 4)
)
_LipAddrTable_Object = MibTable
lipAddrTable = _LipAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 4, 1)
)
if mibBuilder.loadTexts:
    lipAddrTable.setStatus("mandatory")
_LipAddrEntry_Object = MibTableRow
lipAddrEntry = _LipAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 4, 1, 1)
)
lipAddrEntry.setIndexNames(
    (0, "IP-MIB", "ipAdEntAddr"),
)
if mibBuilder.loadTexts:
    lipAddrEntry.setStatus("mandatory")
_LocIPHow_Type = DisplayString
_LocIPHow_Object = MibTableColumn
locIPHow = _LocIPHow_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 4, 1, 1, 1),
    _LocIPHow_Type()
)
locIPHow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    locIPHow.setStatus("mandatory")
_LocIPWho_Type = IpAddress
_LocIPWho_Object = MibTableColumn
locIPWho = _LocIPWho_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 4, 1, 1, 2),
    _LocIPWho_Type()
)
locIPWho.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    locIPWho.setStatus("mandatory")
_LocIPHelper_Type = IpAddress
_LocIPHelper_Object = MibTableColumn
locIPHelper = _LocIPHelper_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 4, 1, 1, 3),
    _LocIPHelper_Type()
)
locIPHelper.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    locIPHelper.setStatus("mandatory")
_LocIPSecurity_Type = Integer32
_LocIPSecurity_Object = MibTableColumn
locIPSecurity = _LocIPSecurity_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 4, 1, 1, 4),
    _LocIPSecurity_Type()
)
locIPSecurity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    locIPSecurity.setStatus("mandatory")
_LocIPRedirects_Type = Integer32
_LocIPRedirects_Object = MibTableColumn
locIPRedirects = _LocIPRedirects_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 4, 1, 1, 5),
    _LocIPRedirects_Type()
)
locIPRedirects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    locIPRedirects.setStatus("mandatory")
_LocIPUnreach_Type = Integer32
_LocIPUnreach_Object = MibTableColumn
locIPUnreach = _LocIPUnreach_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 4, 1, 1, 6),
    _LocIPUnreach_Type()
)
locIPUnreach.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    locIPUnreach.setStatus("mandatory")
_LipRouteTable_Object = MibTable
lipRouteTable = _LipRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 4, 2)
)
if mibBuilder.loadTexts:
    lipRouteTable.setStatus("mandatory")
_LipRouteEntry_Object = MibTableRow
lipRouteEntry = _LipRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 4, 2, 1)
)
lipRouteEntry.setIndexNames(
    (0, "RFC1213-MIB", "ipRouteDest"),
)
if mibBuilder.loadTexts:
    lipRouteEntry.setStatus("mandatory")
_LocRtMask_Type = IpAddress
_LocRtMask_Object = MibTableColumn
locRtMask = _LocRtMask_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 4, 2, 1, 1),
    _LocRtMask_Type()
)
locRtMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    locRtMask.setStatus("mandatory")
_LocRtCount_Type = Integer32
_LocRtCount_Object = MibTableColumn
locRtCount = _LocRtCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 4, 2, 1, 2),
    _LocRtCount_Type()
)
locRtCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    locRtCount.setStatus("mandatory")
_LocRtUses_Type = Integer32
_LocRtUses_Object = MibTableColumn
locRtUses = _LocRtUses_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 4, 2, 1, 3),
    _LocRtUses_Type()
)
locRtUses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    locRtUses.setStatus("mandatory")
_ActThresh_Type = Integer32
_ActThresh_Object = MibScalar
actThresh = _ActThresh_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 4, 4),
    _ActThresh_Type()
)
actThresh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    actThresh.setStatus("mandatory")
_ActLostPkts_Type = Integer32
_ActLostPkts_Object = MibScalar
actLostPkts = _ActLostPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 4, 5),
    _ActLostPkts_Type()
)
actLostPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    actLostPkts.setStatus("mandatory")
_ActLostByts_Type = Integer32
_ActLostByts_Object = MibScalar
actLostByts = _ActLostByts_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 4, 6),
    _ActLostByts_Type()
)
actLostByts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    actLostByts.setStatus("mandatory")
_LipAccountingTable_Object = MibTable
lipAccountingTable = _LipAccountingTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 4, 7)
)
if mibBuilder.loadTexts:
    lipAccountingTable.setStatus("mandatory")
_LipAccountEntry_Object = MibTableRow
lipAccountEntry = _LipAccountEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 4, 7, 1)
)
lipAccountEntry.setIndexNames(
    (0, "OLD-CISCO-IP-MIB", "actSrc"),
    (0, "OLD-CISCO-IP-MIB", "actDst"),
)
if mibBuilder.loadTexts:
    lipAccountEntry.setStatus("mandatory")
_ActSrc_Type = IpAddress
_ActSrc_Object = MibTableColumn
actSrc = _ActSrc_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 4, 7, 1, 1),
    _ActSrc_Type()
)
actSrc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    actSrc.setStatus("mandatory")
_ActDst_Type = IpAddress
_ActDst_Object = MibTableColumn
actDst = _ActDst_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 4, 7, 1, 2),
    _ActDst_Type()
)
actDst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    actDst.setStatus("mandatory")
_ActPkts_Type = Integer32
_ActPkts_Object = MibTableColumn
actPkts = _ActPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 4, 7, 1, 3),
    _ActPkts_Type()
)
actPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    actPkts.setStatus("mandatory")
_ActByts_Type = Integer32
_ActByts_Object = MibTableColumn
actByts = _ActByts_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 4, 7, 1, 4),
    _ActByts_Type()
)
actByts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    actByts.setStatus("mandatory")
_ActViolation_Type = Integer32
_ActViolation_Object = MibTableColumn
actViolation = _ActViolation_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 4, 7, 1, 5),
    _ActViolation_Type()
)
actViolation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    actViolation.setStatus("mandatory")
_ActAge_Type = TimeTicks
_ActAge_Object = MibScalar
actAge = _ActAge_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 4, 8),
    _ActAge_Type()
)
actAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    actAge.setStatus("mandatory")
_LipCkAccountingTable_Object = MibTable
lipCkAccountingTable = _LipCkAccountingTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 4, 9)
)
if mibBuilder.loadTexts:
    lipCkAccountingTable.setStatus("mandatory")
_LipCkAccountEntry_Object = MibTableRow
lipCkAccountEntry = _LipCkAccountEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 4, 9, 1)
)
lipCkAccountEntry.setIndexNames(
    (0, "OLD-CISCO-IP-MIB", "ckactSrc"),
    (0, "OLD-CISCO-IP-MIB", "ckactDst"),
)
if mibBuilder.loadTexts:
    lipCkAccountEntry.setStatus("mandatory")
_CkactSrc_Type = IpAddress
_CkactSrc_Object = MibTableColumn
ckactSrc = _CkactSrc_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 4, 9, 1, 1),
    _CkactSrc_Type()
)
ckactSrc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ckactSrc.setStatus("mandatory")
_CkactDst_Type = IpAddress
_CkactDst_Object = MibTableColumn
ckactDst = _CkactDst_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 4, 9, 1, 2),
    _CkactDst_Type()
)
ckactDst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ckactDst.setStatus("mandatory")
_CkactPkts_Type = Integer32
_CkactPkts_Object = MibTableColumn
ckactPkts = _CkactPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 4, 9, 1, 3),
    _CkactPkts_Type()
)
ckactPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ckactPkts.setStatus("mandatory")
_CkactByts_Type = Integer32
_CkactByts_Object = MibTableColumn
ckactByts = _CkactByts_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 4, 9, 1, 4),
    _CkactByts_Type()
)
ckactByts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ckactByts.setStatus("mandatory")
_CkactViolation_Type = Integer32
_CkactViolation_Object = MibTableColumn
ckactViolation = _CkactViolation_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 4, 9, 1, 5),
    _CkactViolation_Type()
)
ckactViolation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ckactViolation.setStatus("mandatory")
_CkactAge_Type = TimeTicks
_CkactAge_Object = MibScalar
ckactAge = _CkactAge_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 4, 10),
    _CkactAge_Type()
)
ckactAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ckactAge.setStatus("mandatory")
_ActCheckPoint_Type = Integer32
_ActCheckPoint_Object = MibScalar
actCheckPoint = _ActCheckPoint_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 4, 11),
    _ActCheckPoint_Type()
)
actCheckPoint.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    actCheckPoint.setStatus("mandatory")
_IpNoaccess_Type = Counter32
_IpNoaccess_Object = MibScalar
ipNoaccess = _IpNoaccess_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 4, 12),
    _IpNoaccess_Type()
)
ipNoaccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipNoaccess.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "OLD-CISCO-IP-MIB",
    **{"lip": lip,
       "lipAddrTable": lipAddrTable,
       "lipAddrEntry": lipAddrEntry,
       "locIPHow": locIPHow,
       "locIPWho": locIPWho,
       "locIPHelper": locIPHelper,
       "locIPSecurity": locIPSecurity,
       "locIPRedirects": locIPRedirects,
       "locIPUnreach": locIPUnreach,
       "lipRouteTable": lipRouteTable,
       "lipRouteEntry": lipRouteEntry,
       "locRtMask": locRtMask,
       "locRtCount": locRtCount,
       "locRtUses": locRtUses,
       "actThresh": actThresh,
       "actLostPkts": actLostPkts,
       "actLostByts": actLostByts,
       "lipAccountingTable": lipAccountingTable,
       "lipAccountEntry": lipAccountEntry,
       "actSrc": actSrc,
       "actDst": actDst,
       "actPkts": actPkts,
       "actByts": actByts,
       "actViolation": actViolation,
       "actAge": actAge,
       "lipCkAccountingTable": lipCkAccountingTable,
       "lipCkAccountEntry": lipCkAccountEntry,
       "ckactSrc": ckactSrc,
       "ckactDst": ckactDst,
       "ckactPkts": ckactPkts,
       "ckactByts": ckactByts,
       "ckactViolation": ckactViolation,
       "ckactAge": ckactAge,
       "actCheckPoint": actCheckPoint,
       "ipNoaccess": ipNoaccess}
)
