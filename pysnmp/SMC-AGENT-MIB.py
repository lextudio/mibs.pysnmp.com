# SNMP MIB module (SMC-AGENT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/SMC-AGENT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:55:33 2024
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



class MacAddress(OctetString):
    """Custom type MacAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Smc_ObjectIdentity = ObjectIdentity
smc = _Smc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 202)
)
_SmcDosWs_ObjectIdentity = ObjectIdentity
smcDosWs = _SmcDosWs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 202, 2)
)
_SmcDosWsPcTyp_Type = DisplayString
_SmcDosWsPcTyp_Object = MibScalar
smcDosWsPcTyp = _SmcDosWsPcTyp_Object(
    (1, 3, 6, 1, 4, 1, 202, 2, 1),
    _SmcDosWsPcTyp_Type()
)
smcDosWsPcTyp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smcDosWsPcTyp.setStatus("mandatory")
_SmcDosWsPcProc_Type = DisplayString
_SmcDosWsPcProc_Object = MibScalar
smcDosWsPcProc = _SmcDosWsPcProc_Object(
    (1, 3, 6, 1, 4, 1, 202, 2, 2),
    _SmcDosWsPcProc_Type()
)
smcDosWsPcProc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smcDosWsPcProc.setStatus("mandatory")
_SmcDosWsPcBios_Type = DisplayString
_SmcDosWsPcBios_Object = MibScalar
smcDosWsPcBios = _SmcDosWsPcBios_Object(
    (1, 3, 6, 1, 4, 1, 202, 2, 3),
    _SmcDosWsPcBios_Type()
)
smcDosWsPcBios.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smcDosWsPcBios.setStatus("mandatory")
_SmcDosWsPcRam_Type = DisplayString
_SmcDosWsPcRam_Object = MibScalar
smcDosWsPcRam = _SmcDosWsPcRam_Object(
    (1, 3, 6, 1, 4, 1, 202, 2, 4),
    _SmcDosWsPcRam_Type()
)
smcDosWsPcRam.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smcDosWsPcRam.setStatus("mandatory")
_SmcDosWsPcDisk_Type = DisplayString
_SmcDosWsPcDisk_Object = MibScalar
smcDosWsPcDisk = _SmcDosWsPcDisk_Object(
    (1, 3, 6, 1, 4, 1, 202, 2, 5),
    _SmcDosWsPcDisk_Type()
)
smcDosWsPcDisk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smcDosWsPcDisk.setStatus("mandatory")
_SmcDosWsPcVideo_Type = DisplayString
_SmcDosWsPcVideo_Object = MibScalar
smcDosWsPcVideo = _SmcDosWsPcVideo_Object(
    (1, 3, 6, 1, 4, 1, 202, 2, 6),
    _SmcDosWsPcVideo_Type()
)
smcDosWsPcVideo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smcDosWsPcVideo.setStatus("mandatory")
_SmcDosWsPcIo_Type = DisplayString
_SmcDosWsPcIo_Object = MibScalar
smcDosWsPcIo = _SmcDosWsPcIo_Object(
    (1, 3, 6, 1, 4, 1, 202, 2, 7),
    _SmcDosWsPcIo_Type()
)
smcDosWsPcIo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smcDosWsPcIo.setStatus("mandatory")
_SmcDosWsDosVer_Type = DisplayString
_SmcDosWsDosVer_Object = MibScalar
smcDosWsDosVer = _SmcDosWsDosVer_Object(
    (1, 3, 6, 1, 4, 1, 202, 2, 8),
    _SmcDosWsDosVer_Type()
)
smcDosWsDosVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smcDosWsDosVer.setStatus("mandatory")
_SmcDosWsDrvId_Type = DisplayString
_SmcDosWsDrvId_Object = MibScalar
smcDosWsDrvId = _SmcDosWsDrvId_Object(
    (1, 3, 6, 1, 4, 1, 202, 2, 9),
    _SmcDosWsDrvId_Type()
)
smcDosWsDrvId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smcDosWsDrvId.setStatus("mandatory")
_SmcDosWsNicBasIo_Type = DisplayString
_SmcDosWsNicBasIo_Object = MibScalar
smcDosWsNicBasIo = _SmcDosWsNicBasIo_Object(
    (1, 3, 6, 1, 4, 1, 202, 2, 10),
    _SmcDosWsNicBasIo_Type()
)
smcDosWsNicBasIo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smcDosWsNicBasIo.setStatus("mandatory")
_SmcDosWsNicIrq_Type = DisplayString
_SmcDosWsNicIrq_Object = MibScalar
smcDosWsNicIrq = _SmcDosWsNicIrq_Object(
    (1, 3, 6, 1, 4, 1, 202, 2, 11),
    _SmcDosWsNicIrq_Type()
)
smcDosWsNicIrq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smcDosWsNicIrq.setStatus("mandatory")
_SmcDosWsNicRam_Type = DisplayString
_SmcDosWsNicRam_Object = MibScalar
smcDosWsNicRam = _SmcDosWsNicRam_Object(
    (1, 3, 6, 1, 4, 1, 202, 2, 12),
    _SmcDosWsNicRam_Type()
)
smcDosWsNicRam.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smcDosWsNicRam.setStatus("mandatory")
_SmcDosWsNodId_Type = MacAddress
_SmcDosWsNodId_Object = MibScalar
smcDosWsNodId = _SmcDosWsNodId_Object(
    (1, 3, 6, 1, 4, 1, 202, 2, 13),
    _SmcDosWsNodId_Type()
)
smcDosWsNodId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smcDosWsNodId.setStatus("mandatory")
_SmcDosWsIpAdr_Type = IpAddress
_SmcDosWsIpAdr_Object = MibScalar
smcDosWsIpAdr = _SmcDosWsIpAdr_Object(
    (1, 3, 6, 1, 4, 1, 202, 2, 14),
    _SmcDosWsIpAdr_Type()
)
smcDosWsIpAdr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smcDosWsIpAdr.setStatus("mandatory")
_SmcDosWsComment_Type = DisplayString
_SmcDosWsComment_Object = MibScalar
smcDosWsComment = _SmcDosWsComment_Object(
    (1, 3, 6, 1, 4, 1, 202, 2, 15),
    _SmcDosWsComment_Type()
)
smcDosWsComment.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smcDosWsComment.setStatus("mandatory")
_SmcDosWsPcDate_Type = DisplayString
_SmcDosWsPcDate_Object = MibScalar
smcDosWsPcDate = _SmcDosWsPcDate_Object(
    (1, 3, 6, 1, 4, 1, 202, 2, 16),
    _SmcDosWsPcDate_Type()
)
smcDosWsPcDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smcDosWsPcDate.setStatus("mandatory")
_SmcDosWsPcTime_Type = DisplayString
_SmcDosWsPcTime_Object = MibScalar
smcDosWsPcTime = _SmcDosWsPcTime_Object(
    (1, 3, 6, 1, 4, 1, 202, 2, 17),
    _SmcDosWsPcTime_Type()
)
smcDosWsPcTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smcDosWsPcTime.setStatus("mandatory")
_SmcDosWsRst_Type = Integer32
_SmcDosWsRst_Object = MibScalar
smcDosWsRst = _SmcDosWsRst_Object(
    (1, 3, 6, 1, 4, 1, 202, 2, 18),
    _SmcDosWsRst_Type()
)
smcDosWsRst.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smcDosWsRst.setStatus("mandatory")
_SmcDosWsProtoMix_Type = DisplayString
_SmcDosWsProtoMix_Object = MibScalar
smcDosWsProtoMix = _SmcDosWsProtoMix_Object(
    (1, 3, 6, 1, 4, 1, 202, 2, 19),
    _SmcDosWsProtoMix_Type()
)
smcDosWsProtoMix.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smcDosWsProtoMix.setStatus("mandatory")
_SmcDosWsRcvPkts_Type = Counter32
_SmcDosWsRcvPkts_Object = MibScalar
smcDosWsRcvPkts = _SmcDosWsRcvPkts_Object(
    (1, 3, 6, 1, 4, 1, 202, 2, 20),
    _SmcDosWsRcvPkts_Type()
)
smcDosWsRcvPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smcDosWsRcvPkts.setStatus("mandatory")
_SmcDosWsXmtPkts_Type = Counter32
_SmcDosWsXmtPkts_Object = MibScalar
smcDosWsXmtPkts = _SmcDosWsXmtPkts_Object(
    (1, 3, 6, 1, 4, 1, 202, 2, 21),
    _SmcDosWsXmtPkts_Type()
)
smcDosWsXmtPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smcDosWsXmtPkts.setStatus("mandatory")
_SmcDosWsDrvSpcTable_Object = MibTable
smcDosWsDrvSpcTable = _SmcDosWsDrvSpcTable_Object(
    (1, 3, 6, 1, 4, 1, 202, 2, 22)
)
if mibBuilder.loadTexts:
    smcDosWsDrvSpcTable.setStatus("mandatory")
_SmcDosWsDrvSpcEntry_Object = MibTableRow
smcDosWsDrvSpcEntry = _SmcDosWsDrvSpcEntry_Object(
    (1, 3, 6, 1, 4, 1, 202, 2, 22, 1)
)
smcDosWsDrvSpcEntry.setIndexNames(
    (0, "SMC-AGENT-MIB", "smcDosWsDrvSpcId"),
)
if mibBuilder.loadTexts:
    smcDosWsDrvSpcEntry.setStatus("mandatory")
_SmcDosWsDrvSpcId_Type = Integer32
_SmcDosWsDrvSpcId_Object = MibTableColumn
smcDosWsDrvSpcId = _SmcDosWsDrvSpcId_Object(
    (1, 3, 6, 1, 4, 1, 202, 2, 22, 1, 1),
    _SmcDosWsDrvSpcId_Type()
)
smcDosWsDrvSpcId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smcDosWsDrvSpcId.setStatus("mandatory")
_SmcDosWsDrvSpcTxt_Type = DisplayString
_SmcDosWsDrvSpcTxt_Object = MibTableColumn
smcDosWsDrvSpcTxt = _SmcDosWsDrvSpcTxt_Object(
    (1, 3, 6, 1, 4, 1, 202, 2, 22, 1, 2),
    _SmcDosWsDrvSpcTxt_Type()
)
smcDosWsDrvSpcTxt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smcDosWsDrvSpcTxt.setStatus("mandatory")
_SmcDosWsDrvSpcCnt_Type = Counter32
_SmcDosWsDrvSpcCnt_Object = MibTableColumn
smcDosWsDrvSpcCnt = _SmcDosWsDrvSpcCnt_Object(
    (1, 3, 6, 1, 4, 1, 202, 2, 22, 1, 3),
    _SmcDosWsDrvSpcCnt_Type()
)
smcDosWsDrvSpcCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smcDosWsDrvSpcCnt.setStatus("mandatory")
_SmcDosWsTrapDestTable_Object = MibTable
smcDosWsTrapDestTable = _SmcDosWsTrapDestTable_Object(
    (1, 3, 6, 1, 4, 1, 202, 2, 23)
)
if mibBuilder.loadTexts:
    smcDosWsTrapDestTable.setStatus("mandatory")
_SmcDosWsTrapDestEntry_Object = MibTableRow
smcDosWsTrapDestEntry = _SmcDosWsTrapDestEntry_Object(
    (1, 3, 6, 1, 4, 1, 202, 2, 23, 1)
)
smcDosWsTrapDestEntry.setIndexNames(
    (0, "SMC-AGENT-MIB", "smcDosWsTrapId"),
)
if mibBuilder.loadTexts:
    smcDosWsTrapDestEntry.setStatus("mandatory")


class _SmcDosWsTrapId_Type(Integer32):
    """Custom type smcDosWsTrapId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 127),
    )


_SmcDosWsTrapId_Type.__name__ = "Integer32"
_SmcDosWsTrapId_Object = MibTableColumn
smcDosWsTrapId = _SmcDosWsTrapId_Object(
    (1, 3, 6, 1, 4, 1, 202, 2, 23, 1, 1),
    _SmcDosWsTrapId_Type()
)
smcDosWsTrapId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smcDosWsTrapId.setStatus("mandatory")
_SmcDosWsTrapDstAdr_Type = IpAddress
_SmcDosWsTrapDstAdr_Object = MibTableColumn
smcDosWsTrapDstAdr = _SmcDosWsTrapDstAdr_Object(
    (1, 3, 6, 1, 4, 1, 202, 2, 23, 1, 2),
    _SmcDosWsTrapDstAdr_Type()
)
smcDosWsTrapDstAdr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smcDosWsTrapDstAdr.setStatus("mandatory")
_SmcDosWsTrapDstPro_Type = Integer32
_SmcDosWsTrapDstPro_Object = MibTableColumn
smcDosWsTrapDstPro = _SmcDosWsTrapDstPro_Object(
    (1, 3, 6, 1, 4, 1, 202, 2, 23, 1, 3),
    _SmcDosWsTrapDstPro_Type()
)
smcDosWsTrapDstPro.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smcDosWsTrapDstPro.setStatus("mandatory")
_SmcDosWsApiTrap_Type = DisplayString
_SmcDosWsApiTrap_Object = MibScalar
smcDosWsApiTrap = _SmcDosWsApiTrap_Object(
    (1, 3, 6, 1, 4, 1, 202, 2, 24),
    _SmcDosWsApiTrap_Type()
)
smcDosWsApiTrap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smcDosWsApiTrap.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SMC-AGENT-MIB",
    **{"MacAddress": MacAddress,
       "smc": smc,
       "smcDosWs": smcDosWs,
       "smcDosWsPcTyp": smcDosWsPcTyp,
       "smcDosWsPcProc": smcDosWsPcProc,
       "smcDosWsPcBios": smcDosWsPcBios,
       "smcDosWsPcRam": smcDosWsPcRam,
       "smcDosWsPcDisk": smcDosWsPcDisk,
       "smcDosWsPcVideo": smcDosWsPcVideo,
       "smcDosWsPcIo": smcDosWsPcIo,
       "smcDosWsDosVer": smcDosWsDosVer,
       "smcDosWsDrvId": smcDosWsDrvId,
       "smcDosWsNicBasIo": smcDosWsNicBasIo,
       "smcDosWsNicIrq": smcDosWsNicIrq,
       "smcDosWsNicRam": smcDosWsNicRam,
       "smcDosWsNodId": smcDosWsNodId,
       "smcDosWsIpAdr": smcDosWsIpAdr,
       "smcDosWsComment": smcDosWsComment,
       "smcDosWsPcDate": smcDosWsPcDate,
       "smcDosWsPcTime": smcDosWsPcTime,
       "smcDosWsRst": smcDosWsRst,
       "smcDosWsProtoMix": smcDosWsProtoMix,
       "smcDosWsRcvPkts": smcDosWsRcvPkts,
       "smcDosWsXmtPkts": smcDosWsXmtPkts,
       "smcDosWsDrvSpcTable": smcDosWsDrvSpcTable,
       "smcDosWsDrvSpcEntry": smcDosWsDrvSpcEntry,
       "smcDosWsDrvSpcId": smcDosWsDrvSpcId,
       "smcDosWsDrvSpcTxt": smcDosWsDrvSpcTxt,
       "smcDosWsDrvSpcCnt": smcDosWsDrvSpcCnt,
       "smcDosWsTrapDestTable": smcDosWsTrapDestTable,
       "smcDosWsTrapDestEntry": smcDosWsTrapDestEntry,
       "smcDosWsTrapId": smcDosWsTrapId,
       "smcDosWsTrapDstAdr": smcDosWsTrapDstAdr,
       "smcDosWsTrapDstPro": smcDosWsTrapDstPro,
       "smcDosWsApiTrap": smcDosWsApiTrap}
)
