# SNMP MIB module (OLD-CISCO-NOVELL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/OLD-CISCO-NOVELL-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:34:04 2024
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

(temporary,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "temporary")

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



class IPXaddress(OctetString):
    """Custom type IPXaddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(10, 10),
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Tmpnovell_ObjectIdentity = ObjectIdentity
tmpnovell = _Tmpnovell_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 3, 4)
)
_NovellInput_Type = Integer32
_NovellInput_Object = MibScalar
novellInput = _NovellInput_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 4, 1),
    _NovellInput_Type()
)
novellInput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    novellInput.setStatus("mandatory")
_NovellBcastin_Type = Integer32
_NovellBcastin_Object = MibScalar
novellBcastin = _NovellBcastin_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 4, 2),
    _NovellBcastin_Type()
)
novellBcastin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    novellBcastin.setStatus("mandatory")
_NovellForward_Type = Integer32
_NovellForward_Object = MibScalar
novellForward = _NovellForward_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 4, 3),
    _NovellForward_Type()
)
novellForward.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    novellForward.setStatus("mandatory")
_NovellBcastout_Type = Integer32
_NovellBcastout_Object = MibScalar
novellBcastout = _NovellBcastout_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 4, 4),
    _NovellBcastout_Type()
)
novellBcastout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    novellBcastout.setStatus("mandatory")
_NovellFormerr_Type = Integer32
_NovellFormerr_Object = MibScalar
novellFormerr = _NovellFormerr_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 4, 5),
    _NovellFormerr_Type()
)
novellFormerr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    novellFormerr.setStatus("mandatory")
_NovellChksum_Type = Integer32
_NovellChksum_Object = MibScalar
novellChksum = _NovellChksum_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 4, 6),
    _NovellChksum_Type()
)
novellChksum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    novellChksum.setStatus("mandatory")
_NovellHopcnt_Type = Integer32
_NovellHopcnt_Object = MibScalar
novellHopcnt = _NovellHopcnt_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 4, 7),
    _NovellHopcnt_Type()
)
novellHopcnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    novellHopcnt.setStatus("mandatory")
_NovellNoroute_Type = Integer32
_NovellNoroute_Object = MibScalar
novellNoroute = _NovellNoroute_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 4, 8),
    _NovellNoroute_Type()
)
novellNoroute.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    novellNoroute.setStatus("mandatory")
_NovellNoencap_Type = Integer32
_NovellNoencap_Object = MibScalar
novellNoencap = _NovellNoencap_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 4, 9),
    _NovellNoencap_Type()
)
novellNoencap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    novellNoencap.setStatus("mandatory")
_NovellOutput_Type = Integer32
_NovellOutput_Object = MibScalar
novellOutput = _NovellOutput_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 4, 10),
    _NovellOutput_Type()
)
novellOutput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    novellOutput.setStatus("mandatory")
_NovellInmult_Type = Integer32
_NovellInmult_Object = MibScalar
novellInmult = _NovellInmult_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 4, 11),
    _NovellInmult_Type()
)
novellInmult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    novellInmult.setStatus("mandatory")
_NovellLocal_Type = Integer32
_NovellLocal_Object = MibScalar
novellLocal = _NovellLocal_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 4, 12),
    _NovellLocal_Type()
)
novellLocal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    novellLocal.setStatus("mandatory")
_NovellUnknown_Type = Integer32
_NovellUnknown_Object = MibScalar
novellUnknown = _NovellUnknown_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 4, 13),
    _NovellUnknown_Type()
)
novellUnknown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    novellUnknown.setStatus("mandatory")
_NovellSapreqin_Type = Integer32
_NovellSapreqin_Object = MibScalar
novellSapreqin = _NovellSapreqin_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 4, 14),
    _NovellSapreqin_Type()
)
novellSapreqin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    novellSapreqin.setStatus("mandatory")
_NovellSapresin_Type = Integer32
_NovellSapresin_Object = MibScalar
novellSapresin = _NovellSapresin_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 4, 15),
    _NovellSapresin_Type()
)
novellSapresin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    novellSapresin.setStatus("mandatory")
_NovellSapout_Type = Integer32
_NovellSapout_Object = MibScalar
novellSapout = _NovellSapout_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 4, 16),
    _NovellSapout_Type()
)
novellSapout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    novellSapout.setStatus("mandatory")
_NovellSapreply_Type = Integer32
_NovellSapreply_Object = MibScalar
novellSapreply = _NovellSapreply_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 4, 17),
    _NovellSapreply_Type()
)
novellSapreply.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    novellSapreply.setStatus("mandatory")
_IpxActThresh_Type = Integer32
_IpxActThresh_Object = MibScalar
ipxActThresh = _IpxActThresh_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 4, 18),
    _IpxActThresh_Type()
)
ipxActThresh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxActThresh.setStatus("mandatory")
_IpxActLostPkts_Type = Integer32
_IpxActLostPkts_Object = MibScalar
ipxActLostPkts = _IpxActLostPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 4, 19),
    _IpxActLostPkts_Type()
)
ipxActLostPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxActLostPkts.setStatus("mandatory")
_IpxActLostByts_Type = Integer32
_IpxActLostByts_Object = MibScalar
ipxActLostByts = _IpxActLostByts_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 4, 20),
    _IpxActLostByts_Type()
)
ipxActLostByts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxActLostByts.setStatus("mandatory")
_LipxAccountingTable_Object = MibTable
lipxAccountingTable = _LipxAccountingTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 4, 21)
)
if mibBuilder.loadTexts:
    lipxAccountingTable.setStatus("mandatory")
_LipxAccountingEntry_Object = MibTableRow
lipxAccountingEntry = _LipxAccountingEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 4, 21, 1)
)
lipxAccountingEntry.setIndexNames(
    (0, "OLD-CISCO-NOVELL-MIB", "ipxActSrc"),
    (0, "OLD-CISCO-NOVELL-MIB", "ipxActDst"),
)
if mibBuilder.loadTexts:
    lipxAccountingEntry.setStatus("mandatory")
_IpxActSrc_Type = IPXaddress
_IpxActSrc_Object = MibTableColumn
ipxActSrc = _IpxActSrc_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 4, 21, 1, 1),
    _IpxActSrc_Type()
)
ipxActSrc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxActSrc.setStatus("mandatory")
_IpxActDst_Type = IPXaddress
_IpxActDst_Object = MibTableColumn
ipxActDst = _IpxActDst_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 4, 21, 1, 2),
    _IpxActDst_Type()
)
ipxActDst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxActDst.setStatus("mandatory")
_IpxActPkts_Type = Integer32
_IpxActPkts_Object = MibTableColumn
ipxActPkts = _IpxActPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 4, 21, 1, 3),
    _IpxActPkts_Type()
)
ipxActPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxActPkts.setStatus("mandatory")
_IpxActByts_Type = Integer32
_IpxActByts_Object = MibTableColumn
ipxActByts = _IpxActByts_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 4, 21, 1, 4),
    _IpxActByts_Type()
)
ipxActByts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxActByts.setStatus("mandatory")
_IpxActAge_Type = TimeTicks
_IpxActAge_Object = MibScalar
ipxActAge = _IpxActAge_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 4, 22),
    _IpxActAge_Type()
)
ipxActAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxActAge.setStatus("mandatory")
_LipxCkAccountingTable_Object = MibTable
lipxCkAccountingTable = _LipxCkAccountingTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 4, 23)
)
if mibBuilder.loadTexts:
    lipxCkAccountingTable.setStatus("mandatory")
_LipxCkAccountingEntry_Object = MibTableRow
lipxCkAccountingEntry = _LipxCkAccountingEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 4, 23, 1)
)
lipxCkAccountingEntry.setIndexNames(
    (0, "OLD-CISCO-NOVELL-MIB", "ipxCkactSrc"),
    (0, "OLD-CISCO-NOVELL-MIB", "ipxCkactDst"),
)
if mibBuilder.loadTexts:
    lipxCkAccountingEntry.setStatus("mandatory")
_IpxCkactSrc_Type = IPXaddress
_IpxCkactSrc_Object = MibTableColumn
ipxCkactSrc = _IpxCkactSrc_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 4, 23, 1, 1),
    _IpxCkactSrc_Type()
)
ipxCkactSrc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxCkactSrc.setStatus("mandatory")
_IpxCkactDst_Type = IPXaddress
_IpxCkactDst_Object = MibTableColumn
ipxCkactDst = _IpxCkactDst_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 4, 23, 1, 2),
    _IpxCkactDst_Type()
)
ipxCkactDst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxCkactDst.setStatus("mandatory")
_IpxCkactPkts_Type = Integer32
_IpxCkactPkts_Object = MibTableColumn
ipxCkactPkts = _IpxCkactPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 4, 23, 1, 3),
    _IpxCkactPkts_Type()
)
ipxCkactPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxCkactPkts.setStatus("mandatory")
_IpxCkactByts_Type = Counter32
_IpxCkactByts_Object = MibTableColumn
ipxCkactByts = _IpxCkactByts_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 4, 23, 1, 4),
    _IpxCkactByts_Type()
)
ipxCkactByts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxCkactByts.setStatus("mandatory")
_IpxCkactAge_Type = TimeTicks
_IpxCkactAge_Object = MibScalar
ipxCkactAge = _IpxCkactAge_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 4, 24),
    _IpxCkactAge_Type()
)
ipxCkactAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxCkactAge.setStatus("mandatory")
_IpxActCheckPoint_Type = Integer32
_IpxActCheckPoint_Object = MibScalar
ipxActCheckPoint = _IpxActCheckPoint_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 4, 25),
    _IpxActCheckPoint_Type()
)
ipxActCheckPoint.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxActCheckPoint.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "OLD-CISCO-NOVELL-MIB",
    **{"IPXaddress": IPXaddress,
       "tmpnovell": tmpnovell,
       "novellInput": novellInput,
       "novellBcastin": novellBcastin,
       "novellForward": novellForward,
       "novellBcastout": novellBcastout,
       "novellFormerr": novellFormerr,
       "novellChksum": novellChksum,
       "novellHopcnt": novellHopcnt,
       "novellNoroute": novellNoroute,
       "novellNoencap": novellNoencap,
       "novellOutput": novellOutput,
       "novellInmult": novellInmult,
       "novellLocal": novellLocal,
       "novellUnknown": novellUnknown,
       "novellSapreqin": novellSapreqin,
       "novellSapresin": novellSapresin,
       "novellSapout": novellSapout,
       "novellSapreply": novellSapreply,
       "ipxActThresh": ipxActThresh,
       "ipxActLostPkts": ipxActLostPkts,
       "ipxActLostByts": ipxActLostByts,
       "lipxAccountingTable": lipxAccountingTable,
       "lipxAccountingEntry": lipxAccountingEntry,
       "ipxActSrc": ipxActSrc,
       "ipxActDst": ipxActDst,
       "ipxActPkts": ipxActPkts,
       "ipxActByts": ipxActByts,
       "ipxActAge": ipxActAge,
       "lipxCkAccountingTable": lipxCkAccountingTable,
       "lipxCkAccountingEntry": lipxCkAccountingEntry,
       "ipxCkactSrc": ipxCkactSrc,
       "ipxCkactDst": ipxCkactDst,
       "ipxCkactPkts": ipxCkactPkts,
       "ipxCkactByts": ipxCkactByts,
       "ipxCkactAge": ipxCkactAge,
       "ipxActCheckPoint": ipxActCheckPoint}
)
