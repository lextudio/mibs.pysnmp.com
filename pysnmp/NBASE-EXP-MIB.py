# SNMP MIB module (NBASE-EXP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/NBASE-EXP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:24:42 2024
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

_Nbase_ObjectIdentity = ObjectIdentity
nbase = _Nbase_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629)
)
_NbSwitchG1_ObjectIdentity = ObjectIdentity
nbSwitchG1 = _NbSwitchG1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 1)
)
_NbsMegaMibs_ObjectIdentity = ObjectIdentity
nbsMegaMibs = _NbsMegaMibs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 1, 16)
)
_NbsExpansionPortMIB_ObjectIdentity = ObjectIdentity
nbsExpansionPortMIB = _NbsExpansionPortMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 1, 16, 1)
)
_NbsExpPortMaxNum_Type = Integer32
_NbsExpPortMaxNum_Object = MibScalar
nbsExpPortMaxNum = _NbsExpPortMaxNum_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 16, 1, 1),
    _NbsExpPortMaxNum_Type()
)
nbsExpPortMaxNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsExpPortMaxNum.setStatus("mandatory")
_NbsExpPortTable_Object = MibTable
nbsExpPortTable = _NbsExpPortTable_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 16, 1, 2)
)
if mibBuilder.loadTexts:
    nbsExpPortTable.setStatus("mandatory")
_NbsExpPortEntry_Object = MibTableRow
nbsExpPortEntry = _NbsExpPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 16, 1, 2, 1)
)
nbsExpPortEntry.setIndexNames(
    (0, "NBASE-EXP-MIB", "nbsExpPortTblPortNumber"),
)
if mibBuilder.loadTexts:
    nbsExpPortEntry.setStatus("mandatory")
_NbsExpPortTblPortNumber_Type = Integer32
_NbsExpPortTblPortNumber_Object = MibTableColumn
nbsExpPortTblPortNumber = _NbsExpPortTblPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 16, 1, 2, 1, 1),
    _NbsExpPortTblPortNumber_Type()
)
nbsExpPortTblPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsExpPortTblPortNumber.setStatus("mandatory")


class _NbsExpPortTblHwType_Type(Integer32):
    """Custom type nbsExpPortTblHwType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("cpu-card", 2),
          ("other", 1))
    )


_NbsExpPortTblHwType_Type.__name__ = "Integer32"
_NbsExpPortTblHwType_Object = MibTableColumn
nbsExpPortTblHwType = _NbsExpPortTblHwType_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 16, 1, 2, 1, 2),
    _NbsExpPortTblHwType_Type()
)
nbsExpPortTblHwType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsExpPortTblHwType.setStatus("mandatory")


class _NbsExpPortTblSwType_Type(Integer32):
    """Custom type nbsExpPortTblSwType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("atm-lec", 2),
          ("atm-mpoa", 3),
          ("fddi", 4),
          ("other", 1),
          ("wan-router", 5))
    )


_NbsExpPortTblSwType_Type.__name__ = "Integer32"
_NbsExpPortTblSwType_Object = MibTableColumn
nbsExpPortTblSwType = _NbsExpPortTblSwType_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 16, 1, 2, 1, 3),
    _NbsExpPortTblSwType_Type()
)
nbsExpPortTblSwType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsExpPortTblSwType.setStatus("mandatory")
_NbsExpPortTblSquall_Type = DisplayString
_NbsExpPortTblSquall_Object = MibTableColumn
nbsExpPortTblSquall = _NbsExpPortTblSquall_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 16, 1, 2, 1, 4),
    _NbsExpPortTblSquall_Type()
)
nbsExpPortTblSquall.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsExpPortTblSquall.setStatus("mandatory")
_NbsExpPortTblHwVersion_Type = DisplayString
_NbsExpPortTblHwVersion_Object = MibTableColumn
nbsExpPortTblHwVersion = _NbsExpPortTblHwVersion_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 16, 1, 2, 1, 5),
    _NbsExpPortTblHwVersion_Type()
)
nbsExpPortTblHwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsExpPortTblHwVersion.setStatus("mandatory")
_NbsExpPortTblMCodeVrsn_Type = DisplayString
_NbsExpPortTblMCodeVrsn_Object = MibTableColumn
nbsExpPortTblMCodeVrsn = _NbsExpPortTblMCodeVrsn_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 16, 1, 2, 1, 6),
    _NbsExpPortTblMCodeVrsn_Type()
)
nbsExpPortTblMCodeVrsn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsExpPortTblMCodeVrsn.setStatus("mandatory")
_NbsExpPortTblSwVersion_Type = DisplayString
_NbsExpPortTblSwVersion_Object = MibTableColumn
nbsExpPortTblSwVersion = _NbsExpPortTblSwVersion_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 16, 1, 2, 1, 7),
    _NbsExpPortTblSwVersion_Type()
)
nbsExpPortTblSwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsExpPortTblSwVersion.setStatus("mandatory")


class _NbsExpPortTblStatus_Type(Integer32):
    """Custom type nbsExpPortTblStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("error", 3),
          ("ok", 2),
          ("other", 1))
    )


_NbsExpPortTblStatus_Type.__name__ = "Integer32"
_NbsExpPortTblStatus_Object = MibTableColumn
nbsExpPortTblStatus = _NbsExpPortTblStatus_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 16, 1, 2, 1, 8),
    _NbsExpPortTblStatus_Type()
)
nbsExpPortTblStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsExpPortTblStatus.setStatus("mandatory")
_NbsExpPortTftpSwFileName_Type = DisplayString
_NbsExpPortTftpSwFileName_Object = MibTableColumn
nbsExpPortTftpSwFileName = _NbsExpPortTftpSwFileName_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 16, 1, 2, 1, 9),
    _NbsExpPortTftpSwFileName_Type()
)
nbsExpPortTftpSwFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsExpPortTftpSwFileName.setStatus("mandatory")


class _NbsExpPortInitDownload_Type(Integer32):
    """Custom type nbsExpPortInitDownload based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 2))
    )


_NbsExpPortInitDownload_Type.__name__ = "Integer32"
_NbsExpPortInitDownload_Object = MibTableColumn
nbsExpPortInitDownload = _NbsExpPortInitDownload_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 16, 1, 2, 1, 10),
    _NbsExpPortInitDownload_Type()
)
nbsExpPortInitDownload.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsExpPortInitDownload.setStatus("mandatory")
_NbsAtmLanePortMIB_ObjectIdentity = ObjectIdentity
nbsAtmLanePortMIB = _NbsAtmLanePortMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 1, 16, 2)
)
_NbsAtmLanePortMaxNum_Type = Integer32
_NbsAtmLanePortMaxNum_Object = MibScalar
nbsAtmLanePortMaxNum = _NbsAtmLanePortMaxNum_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 16, 2, 1),
    _NbsAtmLanePortMaxNum_Type()
)
nbsAtmLanePortMaxNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsAtmLanePortMaxNum.setStatus("mandatory")
_NbsAtmLanePortTable_Object = MibTable
nbsAtmLanePortTable = _NbsAtmLanePortTable_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 16, 2, 2)
)
if mibBuilder.loadTexts:
    nbsAtmLanePortTable.setStatus("mandatory")
_NbsAtmLanePortEntry_Object = MibTableRow
nbsAtmLanePortEntry = _NbsAtmLanePortEntry_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 16, 2, 2, 1)
)
nbsAtmLanePortEntry.setIndexNames(
    (0, "NBASE-EXP-MIB", "nbsAtmLanePortNumber"),
)
if mibBuilder.loadTexts:
    nbsAtmLanePortEntry.setStatus("mandatory")
_NbsAtmLanePortNumber_Type = Integer32
_NbsAtmLanePortNumber_Object = MibTableColumn
nbsAtmLanePortNumber = _NbsAtmLanePortNumber_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 16, 2, 2, 1, 1),
    _NbsAtmLanePortNumber_Type()
)
nbsAtmLanePortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsAtmLanePortNumber.setStatus("mandatory")


class _LaneLecsAddress_Type(OctetString):
    """Custom type laneLecsAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(20, 20),
    )


_LaneLecsAddress_Type.__name__ = "OctetString"
_LaneLecsAddress_Object = MibTableColumn
laneLecsAddress = _LaneLecsAddress_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 16, 2, 2, 1, 2),
    _LaneLecsAddress_Type()
)
laneLecsAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    laneLecsAddress.setStatus("mandatory")
_SonetCircuitId_Type = DisplayString
_SonetCircuitId_Object = MibTableColumn
sonetCircuitId = _SonetCircuitId_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 16, 2, 2, 1, 3),
    _SonetCircuitId_Type()
)
sonetCircuitId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonetCircuitId.setStatus("mandatory")


class _SignalingStatus_Type(Integer32):
    """Custom type signalingStatus based on Integer32"""
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


_SignalingStatus_Type.__name__ = "Integer32"
_SignalingStatus_Object = MibTableColumn
signalingStatus = _SignalingStatus_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 16, 2, 2, 1, 4),
    _SignalingStatus_Type()
)
signalingStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    signalingStatus.setStatus("mandatory")
_NbsFddiPortMIB_ObjectIdentity = ObjectIdentity
nbsFddiPortMIB = _NbsFddiPortMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 1, 16, 3)
)
_NbsFddiPortMaxNum_Type = Integer32
_NbsFddiPortMaxNum_Object = MibScalar
nbsFddiPortMaxNum = _NbsFddiPortMaxNum_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 16, 3, 1),
    _NbsFddiPortMaxNum_Type()
)
nbsFddiPortMaxNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsFddiPortMaxNum.setStatus("mandatory")
_NbsFddiPortTable_Object = MibTable
nbsFddiPortTable = _NbsFddiPortTable_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 16, 3, 2)
)
if mibBuilder.loadTexts:
    nbsFddiPortTable.setStatus("mandatory")
_NbsFddiPortEntry_Object = MibTableRow
nbsFddiPortEntry = _NbsFddiPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 16, 3, 2, 1)
)
nbsFddiPortEntry.setIndexNames(
    (0, "NBASE-EXP-MIB", "nbsFddiPortNumber"),
)
if mibBuilder.loadTexts:
    nbsFddiPortEntry.setStatus("mandatory")
_NbsFddiPortNumber_Type = Integer32
_NbsFddiPortNumber_Object = MibTableColumn
nbsFddiPortNumber = _NbsFddiPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 16, 3, 2, 1, 1),
    _NbsFddiPortNumber_Type()
)
nbsFddiPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsFddiPortNumber.setStatus("mandatory")
_NbsFddiSmtIndex_Type = Integer32
_NbsFddiSmtIndex_Object = MibTableColumn
nbsFddiSmtIndex = _NbsFddiSmtIndex_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 16, 3, 2, 1, 2),
    _NbsFddiSmtIndex_Type()
)
nbsFddiSmtIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsFddiSmtIndex.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NBASE-EXP-MIB",
    **{"nbase": nbase,
       "nbSwitchG1": nbSwitchG1,
       "nbsMegaMibs": nbsMegaMibs,
       "nbsExpansionPortMIB": nbsExpansionPortMIB,
       "nbsExpPortMaxNum": nbsExpPortMaxNum,
       "nbsExpPortTable": nbsExpPortTable,
       "nbsExpPortEntry": nbsExpPortEntry,
       "nbsExpPortTblPortNumber": nbsExpPortTblPortNumber,
       "nbsExpPortTblHwType": nbsExpPortTblHwType,
       "nbsExpPortTblSwType": nbsExpPortTblSwType,
       "nbsExpPortTblSquall": nbsExpPortTblSquall,
       "nbsExpPortTblHwVersion": nbsExpPortTblHwVersion,
       "nbsExpPortTblMCodeVrsn": nbsExpPortTblMCodeVrsn,
       "nbsExpPortTblSwVersion": nbsExpPortTblSwVersion,
       "nbsExpPortTblStatus": nbsExpPortTblStatus,
       "nbsExpPortTftpSwFileName": nbsExpPortTftpSwFileName,
       "nbsExpPortInitDownload": nbsExpPortInitDownload,
       "nbsAtmLanePortMIB": nbsAtmLanePortMIB,
       "nbsAtmLanePortMaxNum": nbsAtmLanePortMaxNum,
       "nbsAtmLanePortTable": nbsAtmLanePortTable,
       "nbsAtmLanePortEntry": nbsAtmLanePortEntry,
       "nbsAtmLanePortNumber": nbsAtmLanePortNumber,
       "laneLecsAddress": laneLecsAddress,
       "sonetCircuitId": sonetCircuitId,
       "signalingStatus": signalingStatus,
       "nbsFddiPortMIB": nbsFddiPortMIB,
       "nbsFddiPortMaxNum": nbsFddiPortMaxNum,
       "nbsFddiPortTable": nbsFddiPortTable,
       "nbsFddiPortEntry": nbsFddiPortEntry,
       "nbsFddiPortNumber": nbsFddiPortNumber,
       "nbsFddiSmtIndex": nbsFddiSmtIndex}
)
