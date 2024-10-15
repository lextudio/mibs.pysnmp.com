# SNMP MIB module (ACC-ENET) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ACC-ENET
# Produced by pysmi-1.5.4 at Mon Oct 14 20:32:10 2024
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

(DisplayString,
 accBRG) = mibBuilder.importSymbols(
    "ACC-MIB",
    "DisplayString",
    "accBRG")

(accTrapLogSeqNum,) = mibBuilder.importSymbols(
    "ACC-SYSTEM",
    "accTrapLogSeqNum")

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

_AccEnet_ObjectIdentity = ObjectIdentity
accEnet = _AccEnet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 8)
)
_AccEnetNum_Type = Integer32
_AccEnetNum_Object = MibScalar
accEnetNum = _AccEnetNum_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 8, 1),
    _AccEnetNum_Type()
)
accEnetNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accEnetNum.setStatus("mandatory")
_AccEnetParmTable_Object = MibTable
accEnetParmTable = _AccEnetParmTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 8, 2)
)
if mibBuilder.loadTexts:
    accEnetParmTable.setStatus("mandatory")
_AccEnetParmEntry_Object = MibTableRow
accEnetParmEntry = _AccEnetParmEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 8, 2, 1)
)
accEnetParmEntry.setIndexNames(
    (0, "ACC-ENET", "accEnetPortNo"),
)
if mibBuilder.loadTexts:
    accEnetParmEntry.setStatus("mandatory")
_AccEnetPortNo_Type = Integer32
_AccEnetPortNo_Object = MibTableColumn
accEnetPortNo = _AccEnetPortNo_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 8, 2, 1, 1),
    _AccEnetPortNo_Type()
)
accEnetPortNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accEnetPortNo.setStatus("mandatory")
_AccEnetMACaddr_Type = OctetString
_AccEnetMACaddr_Object = MibTableColumn
accEnetMACaddr = _AccEnetMACaddr_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 8, 2, 1, 2),
    _AccEnetMACaddr_Type()
)
accEnetMACaddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accEnetMACaddr.setStatus("mandatory")


class _AccEthSpeed_Type(Integer32):
    """Custom type accEthSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_AccEthSpeed_Type.__name__ = "Integer32"
_AccEthSpeed_Object = MibTableColumn
accEthSpeed = _AccEthSpeed_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 8, 2, 1, 3),
    _AccEthSpeed_Type()
)
accEthSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accEthSpeed.setStatus("mandatory")


class _AccEthDuplex_Type(Integer32):
    """Custom type accEthDuplex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_AccEthDuplex_Type.__name__ = "Integer32"
_AccEthDuplex_Object = MibTableColumn
accEthDuplex = _AccEthDuplex_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 8, 2, 1, 4),
    _AccEthDuplex_Type()
)
accEthDuplex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accEthDuplex.setStatus("mandatory")
_AccEnetStatTable_Object = MibTable
accEnetStatTable = _AccEnetStatTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 8, 3)
)
if mibBuilder.loadTexts:
    accEnetStatTable.setStatus("mandatory")
_AccEnetStatEntry_Object = MibTableRow
accEnetStatEntry = _AccEnetStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 8, 3, 1)
)
accEnetStatEntry.setIndexNames(
    (0, "ACC-ENET", "accEnetIndex"),
)
if mibBuilder.loadTexts:
    accEnetStatEntry.setStatus("mandatory")
_AccEnetIndex_Type = Integer32
_AccEnetIndex_Object = MibTableColumn
accEnetIndex = _AccEnetIndex_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 8, 3, 1, 1),
    _AccEnetIndex_Type()
)
accEnetIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accEnetIndex.setStatus("mandatory")
_AccEnetStatCRCErrs_Type = Counter32
_AccEnetStatCRCErrs_Object = MibTableColumn
accEnetStatCRCErrs = _AccEnetStatCRCErrs_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 8, 3, 1, 2),
    _AccEnetStatCRCErrs_Type()
)
accEnetStatCRCErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accEnetStatCRCErrs.setStatus("mandatory")
_AccEnetStatAlignErrs_Type = Counter32
_AccEnetStatAlignErrs_Object = MibTableColumn
accEnetStatAlignErrs = _AccEnetStatAlignErrs_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 8, 3, 1, 3),
    _AccEnetStatAlignErrs_Type()
)
accEnetStatAlignErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accEnetStatAlignErrs.setStatus("mandatory")
_AccEnetStatOutColls_Type = Counter32
_AccEnetStatOutColls_Object = MibTableColumn
accEnetStatOutColls = _AccEnetStatOutColls_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 8, 3, 1, 4),
    _AccEnetStatOutColls_Type()
)
accEnetStatOutColls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accEnetStatOutColls.setStatus("mandatory")
_AccEnetStatJabberConds_Type = Counter32
_AccEnetStatJabberConds_Object = MibTableColumn
accEnetStatJabberConds = _AccEnetStatJabberConds_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 8, 3, 1, 5),
    _AccEnetStatJabberConds_Type()
)
accEnetStatJabberConds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accEnetStatJabberConds.setStatus("mandatory")
_AccEnetStatCarrierLosts_Type = Counter32
_AccEnetStatCarrierLosts_Object = MibTableColumn
accEnetStatCarrierLosts = _AccEnetStatCarrierLosts_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 8, 3, 1, 6),
    _AccEnetStatCarrierLosts_Type()
)
accEnetStatCarrierLosts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accEnetStatCarrierLosts.setStatus("mandatory")
_AccEnetStatHeartbeatErrs_Type = Counter32
_AccEnetStatHeartbeatErrs_Object = MibTableColumn
accEnetStatHeartbeatErrs = _AccEnetStatHeartbeatErrs_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 8, 3, 1, 7),
    _AccEnetStatHeartbeatErrs_Type()
)
accEnetStatHeartbeatErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accEnetStatHeartbeatErrs.setStatus("mandatory")
_AccEnetStatGiants_Type = Counter32
_AccEnetStatGiants_Object = MibTableColumn
accEnetStatGiants = _AccEnetStatGiants_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 8, 3, 1, 8),
    _AccEnetStatGiants_Type()
)
accEnetStatGiants.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accEnetStatGiants.setStatus("mandatory")
_AccEnetStatOneRetrys_Type = Counter32
_AccEnetStatOneRetrys_Object = MibTableColumn
accEnetStatOneRetrys = _AccEnetStatOneRetrys_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 8, 3, 1, 9),
    _AccEnetStatOneRetrys_Type()
)
accEnetStatOneRetrys.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accEnetStatOneRetrys.setStatus("mandatory")
_AccEnetStatMultRetrys_Type = Counter32
_AccEnetStatMultRetrys_Object = MibTableColumn
accEnetStatMultRetrys = _AccEnetStatMultRetrys_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 8, 3, 1, 10),
    _AccEnetStatMultRetrys_Type()
)
accEnetStatMultRetrys.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accEnetStatMultRetrys.setStatus("mandatory")
_AccEnetStatLateColls_Type = Counter32
_AccEnetStatLateColls_Object = MibTableColumn
accEnetStatLateColls = _AccEnetStatLateColls_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 8, 3, 1, 11),
    _AccEnetStatLateColls_Type()
)
accEnetStatLateColls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accEnetStatLateColls.setStatus("mandatory")
_AccEnetChipCrashes_Type = Counter32
_AccEnetChipCrashes_Object = MibTableColumn
accEnetChipCrashes = _AccEnetChipCrashes_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 8, 3, 1, 12),
    _AccEnetChipCrashes_Type()
)
accEnetChipCrashes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accEnetChipCrashes.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ACC-ENET",
    **{"accEnet": accEnet,
       "accEnetNum": accEnetNum,
       "accEnetParmTable": accEnetParmTable,
       "accEnetParmEntry": accEnetParmEntry,
       "accEnetPortNo": accEnetPortNo,
       "accEnetMACaddr": accEnetMACaddr,
       "accEthSpeed": accEthSpeed,
       "accEthDuplex": accEthDuplex,
       "accEnetStatTable": accEnetStatTable,
       "accEnetStatEntry": accEnetStatEntry,
       "accEnetIndex": accEnetIndex,
       "accEnetStatCRCErrs": accEnetStatCRCErrs,
       "accEnetStatAlignErrs": accEnetStatAlignErrs,
       "accEnetStatOutColls": accEnetStatOutColls,
       "accEnetStatJabberConds": accEnetStatJabberConds,
       "accEnetStatCarrierLosts": accEnetStatCarrierLosts,
       "accEnetStatHeartbeatErrs": accEnetStatHeartbeatErrs,
       "accEnetStatGiants": accEnetStatGiants,
       "accEnetStatOneRetrys": accEnetStatOneRetrys,
       "accEnetStatMultRetrys": accEnetStatMultRetrys,
       "accEnetStatLateColls": accEnetStatLateColls,
       "accEnetChipCrashes": accEnetChipCrashes}
)
