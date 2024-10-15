# SNMP MIB module (LIGHTSTREAM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/LIGHTSTREAM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:18:08 2024
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

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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
 NotificationType,
 TimeTicks,
 Unsigned32,
 enterprises,
 iso,
 mib_2) = mibBuilder.importSymbols(
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
    "NotificationType",
    "TimeTicks",
    "Unsigned32",
    "enterprises",
    "iso",
    "mib-2")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions



class LightStreamStatus(Integer32):
    """Custom type LightStreamStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )





class LightStreamValidation(Integer32):
    """Custom type LightStreamValidation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 2),
          ("valid", 1))
    )





class LightStreamFilterAction(Integer32):
    """Custom type LightStreamFilterAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("block", 2),
          ("forward", 1))
    )





class LightStreamUpToMaxAge(Integer32):
    """Custom type LightStreamUpToMaxAge based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3600),
    )





class LightStreamDLCI(Integer32):
    """Custom type LightStreamDLCI based on Integer32"""




class VCI(Integer32):
    """Custom type VCI based on Integer32"""



# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_LightStream_ObjectIdentity = ObjectIdentity
lightStream = _LightStream_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 711)
)
_LightStreamOIDs_ObjectIdentity = ObjectIdentity
lightStreamOIDs = _LightStreamOIDs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 711, 1)
)
_LightStreamATM_ObjectIdentity = ObjectIdentity
lightStreamATM = _LightStreamATM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 711, 1, 1)
)
_LsOther_ObjectIdentity = ObjectIdentity
lsOther = _LsOther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 711, 1, 2)
)
_LsTrapNumber_ObjectIdentity = ObjectIdentity
lsTrapNumber = _LsTrapNumber_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 711, 1, 2, 1)
)
_LsTrapText_ObjectIdentity = ObjectIdentity
lsTrapText = _LsTrapText_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 711, 1, 2, 2)
)
_LsTrapName_ObjectIdentity = ObjectIdentity
lsTrapName = _LsTrapName_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 711, 1, 2, 3)
)
_LsConfig_ObjectIdentity = ObjectIdentity
lsConfig = _LsConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 711, 1, 3)
)
_LightStreamProducts_ObjectIdentity = ObjectIdentity
lightStreamProducts = _LightStreamProducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 711, 2)
)
_AtmSwitch_ObjectIdentity = ObjectIdentity
atmSwitch = _AtmSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 711, 2, 1)
)
_ChassisInfo_ObjectIdentity = ObjectIdentity
chassisInfo = _ChassisInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 1)
)
_ChassisId_Type = Integer32
_ChassisId_Object = MibScalar
chassisId = _ChassisId_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 1, 2),
    _ChassisId_Type()
)
chassisId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisId.setStatus("mandatory")
_ChassisActiveIpAddr_Type = IpAddress
_ChassisActiveIpAddr_Object = MibScalar
chassisActiveIpAddr = _ChassisActiveIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 1, 3),
    _ChassisActiveIpAddr_Type()
)
chassisActiveIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chassisActiveIpAddr.setStatus("mandatory")
_ChassisSecondaryIpAddr_Type = IpAddress
_ChassisSecondaryIpAddr_Object = MibScalar
chassisSecondaryIpAddr = _ChassisSecondaryIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 1, 4),
    _ChassisSecondaryIpAddr_Type()
)
chassisSecondaryIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chassisSecondaryIpAddr.setStatus("mandatory")
_ChassisNetworkMask_Type = IpAddress
_ChassisNetworkMask_Object = MibScalar
chassisNetworkMask = _ChassisNetworkMask_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 1, 5),
    _ChassisNetworkMask_Type()
)
chassisNetworkMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chassisNetworkMask.setStatus("mandatory")
_ChassisEthernetIpAddr_Type = IpAddress
_ChassisEthernetIpAddr_Object = MibScalar
chassisEthernetIpAddr = _ChassisEthernetIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 1, 6),
    _ChassisEthernetIpAddr_Type()
)
chassisEthernetIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chassisEthernetIpAddr.setStatus("mandatory")
_ChassisEthernetIpMask_Type = IpAddress
_ChassisEthernetIpMask_Object = MibScalar
chassisEthernetIpMask = _ChassisEthernetIpMask_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 1, 7),
    _ChassisEthernetIpMask_Type()
)
chassisEthernetIpMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chassisEthernetIpMask.setStatus("mandatory")
_ChassisDefaultIpRouter_Type = IpAddress
_ChassisDefaultIpRouter_Object = MibScalar
chassisDefaultIpRouter = _ChassisDefaultIpRouter_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 1, 8),
    _ChassisDefaultIpRouter_Type()
)
chassisDefaultIpRouter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chassisDefaultIpRouter.setStatus("mandatory")
_ChassisStatusWord_Type = Integer32
_ChassisStatusWord_Object = MibScalar
chassisStatusWord = _ChassisStatusWord_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 1, 9),
    _ChassisStatusWord_Type()
)
chassisStatusWord.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisStatusWord.setStatus("mandatory")


class _ChassisConsoleTrapLevel_Type(Integer32):
    """Custom type chassisConsoleTrapLevel based on Integer32"""
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
        *(("debug", 4),
          ("informational", 2),
          ("off", 5),
          ("operational", 1),
          ("trace", 3))
    )


_ChassisConsoleTrapLevel_Type.__name__ = "Integer32"
_ChassisConsoleTrapLevel_Object = MibScalar
chassisConsoleTrapLevel = _ChassisConsoleTrapLevel_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 1, 10),
    _ChassisConsoleTrapLevel_Type()
)
chassisConsoleTrapLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisConsoleTrapLevel.setStatus("mandatory")
_CardInfo_ObjectIdentity = ObjectIdentity
cardInfo = _CardInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 2)
)
_CardTable_Object = MibTable
cardTable = _CardTable_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 2, 1)
)
if mibBuilder.loadTexts:
    cardTable.setStatus("mandatory")
_CardEntry_Object = MibTableRow
cardEntry = _CardEntry_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 2, 1, 1)
)
cardEntry.setIndexNames(
    (0, "LIGHTSTREAM-MIB", "cardIndex"),
)
if mibBuilder.loadTexts:
    cardEntry.setStatus("mandatory")
_CardIndex_Type = Integer32
_CardIndex_Object = MibTableColumn
cardIndex = _CardIndex_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 2, 1, 1, 1),
    _CardIndex_Type()
)
cardIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cardIndex.setStatus("mandatory")


class _CardName_Type(DisplayString):
    """Custom type cardName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CardName_Type.__name__ = "DisplayString"
_CardName_Object = MibTableColumn
cardName = _CardName_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 2, 1, 1, 2),
    _CardName_Type()
)
cardName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cardName.setStatus("mandatory")


class _CardBoardType_Type(DisplayString):
    """Custom type cardBoardType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CardBoardType_Type.__name__ = "DisplayString"
_CardBoardType_Object = MibTableColumn
cardBoardType = _CardBoardType_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 2, 1, 1, 3),
    _CardBoardType_Type()
)
cardBoardType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cardBoardType.setStatus("mandatory")


class _CardLcSoftwareVersion_Type(DisplayString):
    """Custom type cardLcSoftwareVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CardLcSoftwareVersion_Type.__name__ = "DisplayString"
_CardLcSoftwareVersion_Object = MibTableColumn
cardLcSoftwareVersion = _CardLcSoftwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 2, 1, 1, 4),
    _CardLcSoftwareVersion_Type()
)
cardLcSoftwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cardLcSoftwareVersion.setStatus("mandatory")


class _CardLccSoftwareVersion_Type(DisplayString):
    """Custom type cardLccSoftwareVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CardLccSoftwareVersion_Type.__name__ = "DisplayString"
_CardLccSoftwareVersion_Object = MibTableColumn
cardLccSoftwareVersion = _CardLccSoftwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 2, 1, 1, 5),
    _CardLccSoftwareVersion_Type()
)
cardLccSoftwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cardLccSoftwareVersion.setStatus("mandatory")
_CardPID_Type = Integer32
_CardPID_Object = MibTableColumn
cardPID = _CardPID_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 2, 1, 1, 6),
    _CardPID_Type()
)
cardPID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cardPID.setStatus("mandatory")


class _CardMaxVCs_Type(Integer32):
    """Custom type cardMaxVCs based on Integer32"""
    defaultValue = 800


_CardMaxVCs_Object = MibTableColumn
cardMaxVCs = _CardMaxVCs_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 2, 1, 1, 7),
    _CardMaxVCs_Type()
)
cardMaxVCs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cardMaxVCs.setStatus("mandatory")


class _CardOperStatus_Type(Integer32):
    """Custom type cardOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("empty", 4),
          ("testing", 3),
          ("up", 1))
    )


_CardOperStatus_Type.__name__ = "Integer32"
_CardOperStatus_Object = MibTableColumn
cardOperStatus = _CardOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 2, 1, 1, 8),
    _CardOperStatus_Type()
)
cardOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cardOperStatus.setStatus("mandatory")


class _CardAdminStatus_Type(Integer32):
    """Custom type cardAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("testing", 3),
          ("up", 1))
    )


_CardAdminStatus_Type.__name__ = "Integer32"
_CardAdminStatus_Object = MibTableColumn
cardAdminStatus = _CardAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 2, 1, 1, 9),
    _CardAdminStatus_Type()
)
cardAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cardAdminStatus.setStatus("mandatory")
_CardStatusWord_Type = Integer32
_CardStatusWord_Object = MibTableColumn
cardStatusWord = _CardStatusWord_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 2, 1, 1, 10),
    _CardStatusWord_Type()
)
cardStatusWord.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cardStatusWord.setStatus("mandatory")


class _CardConfigRegister_Type(Integer32):
    """Custom type cardConfigRegister based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("empty", 4),
          ("testing", 3),
          ("up", 1))
    )


_CardConfigRegister_Type.__name__ = "Integer32"
_CardConfigRegister_Object = MibTableColumn
cardConfigRegister = _CardConfigRegister_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 2, 1, 1, 11),
    _CardConfigRegister_Type()
)
cardConfigRegister.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cardConfigRegister.setStatus("mandatory")
_PortInfo_ObjectIdentity = ObjectIdentity
portInfo = _PortInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 3)
)
_PortInfoTable_Object = MibTable
portInfoTable = _PortInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 3, 1)
)
if mibBuilder.loadTexts:
    portInfoTable.setStatus("mandatory")
_PortInfoEntry_Object = MibTableRow
portInfoEntry = _PortInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 3, 1, 1)
)
portInfoEntry.setIndexNames(
    (0, "LIGHTSTREAM-MIB", "portInfoIndex"),
)
if mibBuilder.loadTexts:
    portInfoEntry.setStatus("mandatory")
_PortInfoIndex_Type = Integer32
_PortInfoIndex_Object = MibTableColumn
portInfoIndex = _PortInfoIndex_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 3, 1, 1, 1),
    _PortInfoIndex_Type()
)
portInfoIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portInfoIndex.setStatus("mandatory")


class _PortInfoType_Type(Integer32):
    """Custom type portInfoType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              10,
              11,
              12,
              13,
              14,
              15,
              30,
              31,
              32,
              33,
              34,
              35,
              36,
              37)
        )
    )
    namedValues = NamedValues(
        *(("clc12oc3ac1Edge", 31),
          ("clc12oc3ac1Trunk", 32),
          ("clc12taxiac1Edge", 35),
          ("clc12taxiac1Trunk", 36),
          ("clc18t1e1cbrac1", 37),
          ("clc18t3ac1Edge", 33),
          ("clc18t3ac1Trunk", 34),
          ("clc1Gen", 30),
          ("empty", 1),
          ("error", 2),
          ("lsEdge", 6),
          ("lsTrunk", 7),
          ("msEdge", 10),
          ("msTrunk", 8),
          ("np", 5),
          ("plc12fac1", 11),
          ("plc18eac1", 12),
          ("plc18sac1Edge", 14),
          ("plc18sac1Trunk", 15),
          ("plc1Lstoken", 13),
          ("switch", 4),
          ("unknown", 3))
    )


_PortInfoType_Type.__name__ = "Integer32"
_PortInfoType_Object = MibTableColumn
portInfoType = _PortInfoType_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 3, 1, 1, 2),
    _PortInfoType_Type()
)
portInfoType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portInfoType.setStatus("mandatory")
_PortInfoSpecific_Type = ObjectIdentifier
_PortInfoSpecific_Object = MibTableColumn
portInfoSpecific = _PortInfoSpecific_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 3, 1, 1, 3),
    _PortInfoSpecific_Type()
)
portInfoSpecific.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portInfoSpecific.setStatus("mandatory")
_PortInfoName_Type = DisplayString
_PortInfoName_Object = MibTableColumn
portInfoName = _PortInfoName_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 3, 1, 1, 4),
    _PortInfoName_Type()
)
portInfoName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portInfoName.setStatus("mandatory")
_PortInfoErrorLimit_Type = Integer32
_PortInfoErrorLimit_Object = MibTableColumn
portInfoErrorLimit = _PortInfoErrorLimit_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 3, 1, 1, 5),
    _PortInfoErrorLimit_Type()
)
portInfoErrorLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portInfoErrorLimit.setStatus("mandatory")
_PortTransmission_ObjectIdentity = ObjectIdentity
portTransmission = _PortTransmission_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 4)
)
_Ls1InfoTable_Object = MibTable
ls1InfoTable = _Ls1InfoTable_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 4, 1)
)
if mibBuilder.loadTexts:
    ls1InfoTable.setStatus("mandatory")
_Ls1InfoEntry_Object = MibTableRow
ls1InfoEntry = _Ls1InfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 4, 1, 1)
)
ls1InfoEntry.setIndexNames(
    (0, "LIGHTSTREAM-MIB", "ls1InfoIfIndex"),
)
if mibBuilder.loadTexts:
    ls1InfoEntry.setStatus("mandatory")
_Ls1InfoIfIndex_Type = Integer32
_Ls1InfoIfIndex_Object = MibTableColumn
ls1InfoIfIndex = _Ls1InfoIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 4, 1, 1, 1),
    _Ls1InfoIfIndex_Type()
)
ls1InfoIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ls1InfoIfIndex.setStatus("mandatory")


class _Ls1InfoType_Type(Integer32):
    """Custom type ls1InfoType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              99)
        )
    )
    namedValues = NamedValues(
        *(("rs422", 2),
          ("rs530", 3),
          ("t1", 4),
          ("unknown", 99),
          ("v35", 1))
    )


_Ls1InfoType_Type.__name__ = "Integer32"
_Ls1InfoType_Object = MibTableColumn
ls1InfoType = _Ls1InfoType_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 4, 1, 1, 2),
    _Ls1InfoType_Type()
)
ls1InfoType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ls1InfoType.setStatus("mandatory")


class _Ls1InfoOperCsuType_Type(Integer32):
    """Custom type ls1InfoOperCsuType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("larse", 2),
          ("none", 1))
    )


_Ls1InfoOperCsuType_Type.__name__ = "Integer32"
_Ls1InfoOperCsuType_Object = MibTableColumn
ls1InfoOperCsuType = _Ls1InfoOperCsuType_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 4, 1, 1, 3),
    _Ls1InfoOperCsuType_Type()
)
ls1InfoOperCsuType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ls1InfoOperCsuType.setStatus("mandatory")


class _Ls1InfoAdminCsuType_Type(Integer32):
    """Custom type ls1InfoAdminCsuType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("larse", 2),
          ("none", 1))
    )


_Ls1InfoAdminCsuType_Type.__name__ = "Integer32"
_Ls1InfoAdminCsuType_Object = MibTableColumn
ls1InfoAdminCsuType = _Ls1InfoAdminCsuType_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 4, 1, 1, 4),
    _Ls1InfoAdminCsuType_Type()
)
ls1InfoAdminCsuType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ls1InfoAdminCsuType.setStatus("mandatory")
_Ls1InfoOperRcvBaudRate_Type = Integer32
_Ls1InfoOperRcvBaudRate_Object = MibTableColumn
ls1InfoOperRcvBaudRate = _Ls1InfoOperRcvBaudRate_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 4, 1, 1, 5),
    _Ls1InfoOperRcvBaudRate_Type()
)
ls1InfoOperRcvBaudRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ls1InfoOperRcvBaudRate.setStatus("mandatory")
_Ls1InfoAdminRcvBaudRate_Type = Integer32
_Ls1InfoAdminRcvBaudRate_Object = MibTableColumn
ls1InfoAdminRcvBaudRate = _Ls1InfoAdminRcvBaudRate_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 4, 1, 1, 6),
    _Ls1InfoAdminRcvBaudRate_Type()
)
ls1InfoAdminRcvBaudRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ls1InfoAdminRcvBaudRate.setStatus("mandatory")
_Ls1InfoOperXmitBaudRate_Type = Integer32
_Ls1InfoOperXmitBaudRate_Object = MibTableColumn
ls1InfoOperXmitBaudRate = _Ls1InfoOperXmitBaudRate_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 4, 1, 1, 7),
    _Ls1InfoOperXmitBaudRate_Type()
)
ls1InfoOperXmitBaudRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ls1InfoOperXmitBaudRate.setStatus("mandatory")
_Ls1InfoAdminXmitBaudRate_Type = Integer32
_Ls1InfoAdminXmitBaudRate_Object = MibTableColumn
ls1InfoAdminXmitBaudRate = _Ls1InfoAdminXmitBaudRate_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 4, 1, 1, 8),
    _Ls1InfoAdminXmitBaudRate_Type()
)
ls1InfoAdminXmitBaudRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ls1InfoAdminXmitBaudRate.setStatus("mandatory")


class _Ls1InfoOperNetIntType_Type(Integer32):
    """Custom type ls1InfoOperNetIntType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dce", 1),
          ("dceTTloop", 3),
          ("dte", 2))
    )


_Ls1InfoOperNetIntType_Type.__name__ = "Integer32"
_Ls1InfoOperNetIntType_Object = MibTableColumn
ls1InfoOperNetIntType = _Ls1InfoOperNetIntType_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 4, 1, 1, 9),
    _Ls1InfoOperNetIntType_Type()
)
ls1InfoOperNetIntType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ls1InfoOperNetIntType.setStatus("mandatory")


class _Ls1InfoAdminNetIntType_Type(Integer32):
    """Custom type ls1InfoAdminNetIntType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dce", 1),
          ("dceTTloop", 3),
          ("dte", 2))
    )


_Ls1InfoAdminNetIntType_Type.__name__ = "Integer32"
_Ls1InfoAdminNetIntType_Object = MibTableColumn
ls1InfoAdminNetIntType = _Ls1InfoAdminNetIntType_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 4, 1, 1, 10),
    _Ls1InfoAdminNetIntType_Type()
)
ls1InfoAdminNetIntType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ls1InfoAdminNetIntType.setStatus("mandatory")
_Ls1InfoOperModemState_Type = Integer32
_Ls1InfoOperModemState_Object = MibTableColumn
ls1InfoOperModemState = _Ls1InfoOperModemState_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 4, 1, 1, 13),
    _Ls1InfoOperModemState_Type()
)
ls1InfoOperModemState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ls1InfoOperModemState.setStatus("mandatory")


class _Ls1InfoOperProtocol_Type(Integer32):
    """Custom type ls1InfoOperProtocol based on Integer32"""
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
        *(("frameForwarding", 3),
          ("frameRelay", 2),
          ("ppp", 4),
          ("trunk", 1),
          ("unknown", 5))
    )


_Ls1InfoOperProtocol_Type.__name__ = "Integer32"
_Ls1InfoOperProtocol_Object = MibTableColumn
ls1InfoOperProtocol = _Ls1InfoOperProtocol_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 4, 1, 1, 15),
    _Ls1InfoOperProtocol_Type()
)
ls1InfoOperProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ls1InfoOperProtocol.setStatus("mandatory")


class _Ls1InfoAdminProtocol_Type(Integer32):
    """Custom type ls1InfoAdminProtocol based on Integer32"""
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
        *(("frameForwarding", 3),
          ("frameRelay", 2),
          ("ppp", 4),
          ("trunk", 1),
          ("unknown", 5))
    )


_Ls1InfoAdminProtocol_Type.__name__ = "Integer32"
_Ls1InfoAdminProtocol_Object = MibTableColumn
ls1InfoAdminProtocol = _Ls1InfoAdminProtocol_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 4, 1, 1, 16),
    _Ls1InfoAdminProtocol_Type()
)
ls1InfoAdminProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ls1InfoAdminProtocol.setStatus("mandatory")
_Ls1InfoOperControlBandwidthSize_Type = Integer32
_Ls1InfoOperControlBandwidthSize_Object = MibTableColumn
ls1InfoOperControlBandwidthSize = _Ls1InfoOperControlBandwidthSize_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 4, 1, 1, 21),
    _Ls1InfoOperControlBandwidthSize_Type()
)
ls1InfoOperControlBandwidthSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ls1InfoOperControlBandwidthSize.setStatus("mandatory")
_Ls1InfoAdminControlBandwidthSize_Type = Integer32
_Ls1InfoAdminControlBandwidthSize_Object = MibTableColumn
ls1InfoAdminControlBandwidthSize = _Ls1InfoAdminControlBandwidthSize_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 4, 1, 1, 22),
    _Ls1InfoAdminControlBandwidthSize_Type()
)
ls1InfoAdminControlBandwidthSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ls1InfoAdminControlBandwidthSize.setStatus("mandatory")
_Ls1InfoOperDataBandwidthSize_Type = Integer32
_Ls1InfoOperDataBandwidthSize_Object = MibTableColumn
ls1InfoOperDataBandwidthSize = _Ls1InfoOperDataBandwidthSize_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 4, 1, 1, 23),
    _Ls1InfoOperDataBandwidthSize_Type()
)
ls1InfoOperDataBandwidthSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ls1InfoOperDataBandwidthSize.setStatus("mandatory")
_Ls1InfoAdminDataBandwidthSize_Type = Integer32
_Ls1InfoAdminDataBandwidthSize_Object = MibTableColumn
ls1InfoAdminDataBandwidthSize = _Ls1InfoAdminDataBandwidthSize_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 4, 1, 1, 24),
    _Ls1InfoAdminDataBandwidthSize_Type()
)
ls1InfoAdminDataBandwidthSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ls1InfoAdminDataBandwidthSize.setStatus("mandatory")


class _Ls1InfoOperLoopMode_Type(Integer32):
    """Custom type ls1InfoOperLoopMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("external", 3),
          ("internal", 2),
          ("none", 1),
          ("remote", 4))
    )


_Ls1InfoOperLoopMode_Type.__name__ = "Integer32"
_Ls1InfoOperLoopMode_Object = MibTableColumn
ls1InfoOperLoopMode = _Ls1InfoOperLoopMode_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 4, 1, 1, 25),
    _Ls1InfoOperLoopMode_Type()
)
ls1InfoOperLoopMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ls1InfoOperLoopMode.setStatus("mandatory")


class _Ls1InfoAdminLoopMode_Type(Integer32):
    """Custom type ls1InfoAdminLoopMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("external", 3),
          ("internal", 2),
          ("none", 1),
          ("remote", 4))
    )


_Ls1InfoAdminLoopMode_Type.__name__ = "Integer32"
_Ls1InfoAdminLoopMode_Object = MibTableColumn
ls1InfoAdminLoopMode = _Ls1InfoAdminLoopMode_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 4, 1, 1, 26),
    _Ls1InfoAdminLoopMode_Type()
)
ls1InfoAdminLoopMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ls1InfoAdminLoopMode.setStatus("mandatory")


class _Ls1InfoLcAutoEnable_Type(Integer32):
    """Custom type ls1InfoLcAutoEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_Ls1InfoLcAutoEnable_Type.__name__ = "Integer32"
_Ls1InfoLcAutoEnable_Object = MibTableColumn
ls1InfoLcAutoEnable = _Ls1InfoLcAutoEnable_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 4, 1, 1, 27),
    _Ls1InfoLcAutoEnable_Type()
)
ls1InfoLcAutoEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ls1InfoLcAutoEnable.setStatus("mandatory")
_Ls1InfoLcDebugLevel_Type = Integer32
_Ls1InfoLcDebugLevel_Object = MibTableColumn
ls1InfoLcDebugLevel = _Ls1InfoLcDebugLevel_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 4, 1, 1, 28),
    _Ls1InfoLcDebugLevel_Type()
)
ls1InfoLcDebugLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ls1InfoLcDebugLevel.setStatus("mandatory")
_Ls1InfoDataCellCapacity_Type = Integer32
_Ls1InfoDataCellCapacity_Object = MibTableColumn
ls1InfoDataCellCapacity = _Ls1InfoDataCellCapacity_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 4, 1, 1, 29),
    _Ls1InfoDataCellCapacity_Type()
)
ls1InfoDataCellCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ls1InfoDataCellCapacity.setStatus("mandatory")
_Ls1InfoDataCellAvailable_Type = Integer32
_Ls1InfoDataCellAvailable_Object = MibTableColumn
ls1InfoDataCellAvailable = _Ls1InfoDataCellAvailable_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 4, 1, 1, 30),
    _Ls1InfoDataCellAvailable_Type()
)
ls1InfoDataCellAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ls1InfoDataCellAvailable.setStatus("mandatory")
_Ls1InfoMeasuredBaudRate_Type = Integer32
_Ls1InfoMeasuredBaudRate_Object = MibTableColumn
ls1InfoMeasuredBaudRate = _Ls1InfoMeasuredBaudRate_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 4, 1, 1, 31),
    _Ls1InfoMeasuredBaudRate_Type()
)
ls1InfoMeasuredBaudRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ls1InfoMeasuredBaudRate.setStatus("mandatory")
_Ls1InfoLinkUtilization_Type = Integer32
_Ls1InfoLinkUtilization_Object = MibTableColumn
ls1InfoLinkUtilization = _Ls1InfoLinkUtilization_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 4, 1, 1, 32),
    _Ls1InfoLinkUtilization_Type()
)
ls1InfoLinkUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ls1InfoLinkUtilization.setStatus("mandatory")


class _Ls1InfoAdminOperTrigger_Type(Integer32):
    """Custom type ls1InfoAdminOperTrigger based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              99)
        )
    )
    namedValues = NamedValues(
        *(("other", 99),
          ("trigger", 1))
    )


_Ls1InfoAdminOperTrigger_Type.__name__ = "Integer32"
_Ls1InfoAdminOperTrigger_Object = MibTableColumn
ls1InfoAdminOperTrigger = _Ls1InfoAdminOperTrigger_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 4, 1, 1, 99),
    _Ls1InfoAdminOperTrigger_Type()
)
ls1InfoAdminOperTrigger.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ls1InfoAdminOperTrigger.setStatus("mandatory")
_Ms1InfoTable_Object = MibTable
ms1InfoTable = _Ms1InfoTable_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 4, 2)
)
if mibBuilder.loadTexts:
    ms1InfoTable.setStatus("mandatory")
_Ms1InfoEntry_Object = MibTableRow
ms1InfoEntry = _Ms1InfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 4, 2, 1)
)
ms1InfoEntry.setIndexNames(
    (0, "LIGHTSTREAM-MIB", "ms1InfoIfIndex"),
)
if mibBuilder.loadTexts:
    ms1InfoEntry.setStatus("mandatory")
_Ms1InfoIfIndex_Type = Integer32
_Ms1InfoIfIndex_Object = MibTableColumn
ms1InfoIfIndex = _Ms1InfoIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 4, 2, 1, 1),
    _Ms1InfoIfIndex_Type()
)
ms1InfoIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ms1InfoIfIndex.setStatus("mandatory")


class _Ms1InfoOperCableLength_Type(Integer32):
    """Custom type ms1InfoOperCableLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("e3CableLength1", 3),
          ("e3CableLength2", 4),
          ("e3CableLength3", 5),
          ("e3CableLength4", 6),
          ("t3CableLength1", 1),
          ("t3CableLength2", 2))
    )


_Ms1InfoOperCableLength_Type.__name__ = "Integer32"
_Ms1InfoOperCableLength_Object = MibTableColumn
ms1InfoOperCableLength = _Ms1InfoOperCableLength_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 4, 2, 1, 2),
    _Ms1InfoOperCableLength_Type()
)
ms1InfoOperCableLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ms1InfoOperCableLength.setStatus("mandatory")


class _Ms1InfoAdminCableLength_Type(Integer32):
    """Custom type ms1InfoAdminCableLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("e3CableLength1", 3),
          ("e3CableLength2", 4),
          ("e3CableLength3", 5),
          ("e3CableLength4", 6),
          ("t3CableLength1", 1),
          ("t3CableLength2", 2))
    )


_Ms1InfoAdminCableLength_Type.__name__ = "Integer32"
_Ms1InfoAdminCableLength_Object = MibTableColumn
ms1InfoAdminCableLength = _Ms1InfoAdminCableLength_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 4, 2, 1, 3),
    _Ms1InfoAdminCableLength_Type()
)
ms1InfoAdminCableLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ms1InfoAdminCableLength.setStatus("mandatory")


class _Ms1InfoOperProtocol_Type(Integer32):
    """Custom type ms1InfoOperProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("atmUni", 2),
          ("trunk", 1),
          ("unknown", 3))
    )


_Ms1InfoOperProtocol_Type.__name__ = "Integer32"
_Ms1InfoOperProtocol_Object = MibTableColumn
ms1InfoOperProtocol = _Ms1InfoOperProtocol_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 4, 2, 1, 4),
    _Ms1InfoOperProtocol_Type()
)
ms1InfoOperProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ms1InfoOperProtocol.setStatus("mandatory")


class _Ms1InfoAdminProtocol_Type(Integer32):
    """Custom type ms1InfoAdminProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("atmUni", 2),
          ("trunk", 1),
          ("unknown", 3))
    )


_Ms1InfoAdminProtocol_Type.__name__ = "Integer32"
_Ms1InfoAdminProtocol_Object = MibTableColumn
ms1InfoAdminProtocol = _Ms1InfoAdminProtocol_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 4, 2, 1, 5),
    _Ms1InfoAdminProtocol_Type()
)
ms1InfoAdminProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ms1InfoAdminProtocol.setStatus("mandatory")
_Ms1InfoOperControlBandwidthSize_Type = Integer32
_Ms1InfoOperControlBandwidthSize_Object = MibTableColumn
ms1InfoOperControlBandwidthSize = _Ms1InfoOperControlBandwidthSize_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 4, 2, 1, 10),
    _Ms1InfoOperControlBandwidthSize_Type()
)
ms1InfoOperControlBandwidthSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ms1InfoOperControlBandwidthSize.setStatus("mandatory")
_Ms1InfoAdminControlBandwidthSize_Type = Integer32
_Ms1InfoAdminControlBandwidthSize_Object = MibTableColumn
ms1InfoAdminControlBandwidthSize = _Ms1InfoAdminControlBandwidthSize_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 4, 2, 1, 11),
    _Ms1InfoAdminControlBandwidthSize_Type()
)
ms1InfoAdminControlBandwidthSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ms1InfoAdminControlBandwidthSize.setStatus("mandatory")
_Ms1InfoOperDataBandwidthSize_Type = Integer32
_Ms1InfoOperDataBandwidthSize_Object = MibTableColumn
ms1InfoOperDataBandwidthSize = _Ms1InfoOperDataBandwidthSize_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 4, 2, 1, 12),
    _Ms1InfoOperDataBandwidthSize_Type()
)
ms1InfoOperDataBandwidthSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ms1InfoOperDataBandwidthSize.setStatus("mandatory")
_Ms1InfoAdminDataBandwidthSize_Type = Integer32
_Ms1InfoAdminDataBandwidthSize_Object = MibTableColumn
ms1InfoAdminDataBandwidthSize = _Ms1InfoAdminDataBandwidthSize_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 4, 2, 1, 13),
    _Ms1InfoAdminDataBandwidthSize_Type()
)
ms1InfoAdminDataBandwidthSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ms1InfoAdminDataBandwidthSize.setStatus("mandatory")


class _Ms1InfoLcAutoEnable_Type(Integer32):
    """Custom type ms1InfoLcAutoEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_Ms1InfoLcAutoEnable_Type.__name__ = "Integer32"
_Ms1InfoLcAutoEnable_Object = MibTableColumn
ms1InfoLcAutoEnable = _Ms1InfoLcAutoEnable_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 4, 2, 1, 14),
    _Ms1InfoLcAutoEnable_Type()
)
ms1InfoLcAutoEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ms1InfoLcAutoEnable.setStatus("mandatory")
_Ms1InfoLcDebugLevel_Type = Integer32
_Ms1InfoLcDebugLevel_Object = MibTableColumn
ms1InfoLcDebugLevel = _Ms1InfoLcDebugLevel_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 4, 2, 1, 15),
    _Ms1InfoLcDebugLevel_Type()
)
ms1InfoLcDebugLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ms1InfoLcDebugLevel.setStatus("mandatory")


class _Ms1InfoOperScramble_Type(Integer32):
    """Custom type ms1InfoOperScramble based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("t3ScrambleDisable", 2),
          ("t3ScrambleEnable", 1))
    )


_Ms1InfoOperScramble_Type.__name__ = "Integer32"
_Ms1InfoOperScramble_Object = MibTableColumn
ms1InfoOperScramble = _Ms1InfoOperScramble_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 4, 2, 1, 16),
    _Ms1InfoOperScramble_Type()
)
ms1InfoOperScramble.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ms1InfoOperScramble.setStatus("mandatory")


class _Ms1InfoAdminScramble_Type(Integer32):
    """Custom type ms1InfoAdminScramble based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("t3ScrambleDisable", 2),
          ("t3ScrambleEnable", 1))
    )


_Ms1InfoAdminScramble_Type.__name__ = "Integer32"
_Ms1InfoAdminScramble_Object = MibTableColumn
ms1InfoAdminScramble = _Ms1InfoAdminScramble_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 4, 2, 1, 17),
    _Ms1InfoAdminScramble_Type()
)
ms1InfoAdminScramble.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ms1InfoAdminScramble.setStatus("mandatory")
_Ms1InfoDataCellCapacity_Type = Integer32
_Ms1InfoDataCellCapacity_Object = MibTableColumn
ms1InfoDataCellCapacity = _Ms1InfoDataCellCapacity_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 4, 2, 1, 18),
    _Ms1InfoDataCellCapacity_Type()
)
ms1InfoDataCellCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ms1InfoDataCellCapacity.setStatus("mandatory")
_Ms1InfoDataCellAvailable_Type = Integer32
_Ms1InfoDataCellAvailable_Object = MibTableColumn
ms1InfoDataCellAvailable = _Ms1InfoDataCellAvailable_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 4, 2, 1, 19),
    _Ms1InfoDataCellAvailable_Type()
)
ms1InfoDataCellAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ms1InfoDataCellAvailable.setStatus("mandatory")
_Ms1InfoLinkUtilization_Type = Integer32
_Ms1InfoLinkUtilization_Object = MibTableColumn
ms1InfoLinkUtilization = _Ms1InfoLinkUtilization_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 4, 2, 1, 20),
    _Ms1InfoLinkUtilization_Type()
)
ms1InfoLinkUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ms1InfoLinkUtilization.setStatus("mandatory")


class _Ms1InfoOperFraming_Type(Integer32):
    """Custom type ms1InfoOperFraming based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("g-804", 3),
          ("plcp", 1),
          ("t3-Hec", 2))
    )


_Ms1InfoOperFraming_Type.__name__ = "Integer32"
_Ms1InfoOperFraming_Object = MibTableColumn
ms1InfoOperFraming = _Ms1InfoOperFraming_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 4, 2, 1, 21),
    _Ms1InfoOperFraming_Type()
)
ms1InfoOperFraming.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ms1InfoOperFraming.setStatus("mandatory")


class _Ms1InfoAdminOperTrigger_Type(Integer32):
    """Custom type ms1InfoAdminOperTrigger based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              99)
        )
    )
    namedValues = NamedValues(
        *(("other", 99),
          ("trigger", 1))
    )


_Ms1InfoAdminOperTrigger_Type.__name__ = "Integer32"
_Ms1InfoAdminOperTrigger_Object = MibTableColumn
ms1InfoAdminOperTrigger = _Ms1InfoAdminOperTrigger_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 4, 2, 1, 99),
    _Ms1InfoAdminOperTrigger_Type()
)
ms1InfoAdminOperTrigger.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ms1InfoAdminOperTrigger.setStatus("mandatory")
_NpInfoTable_Object = MibTable
npInfoTable = _NpInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 4, 3)
)
if mibBuilder.loadTexts:
    npInfoTable.setStatus("mandatory")
_NpInfoEntry_Object = MibTableRow
npInfoEntry = _NpInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 4, 3, 1)
)
npInfoEntry.setIndexNames(
    (0, "LIGHTSTREAM-MIB", "npInfoIfIndex"),
)
if mibBuilder.loadTexts:
    npInfoEntry.setStatus("mandatory")
_NpInfoIfIndex_Type = Integer32
_NpInfoIfIndex_Object = MibTableColumn
npInfoIfIndex = _NpInfoIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 4, 3, 1, 1),
    _NpInfoIfIndex_Type()
)
npInfoIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npInfoIfIndex.setStatus("mandatory")
_NpInfoIPCommittedRate_Type = Integer32
_NpInfoIPCommittedRate_Object = MibTableColumn
npInfoIPCommittedRate = _NpInfoIPCommittedRate_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 4, 3, 1, 5),
    _NpInfoIPCommittedRate_Type()
)
npInfoIPCommittedRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    npInfoIPCommittedRate.setStatus("mandatory")
_NpInfoIPCommittedBurst_Type = Integer32
_NpInfoIPCommittedBurst_Object = MibTableColumn
npInfoIPCommittedBurst = _NpInfoIPCommittedBurst_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 4, 3, 1, 6),
    _NpInfoIPCommittedBurst_Type()
)
npInfoIPCommittedBurst.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    npInfoIPCommittedBurst.setStatus("mandatory")
_NpInfoIPExcessRate_Type = Integer32
_NpInfoIPExcessRate_Object = MibTableColumn
npInfoIPExcessRate = _NpInfoIPExcessRate_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 4, 3, 1, 7),
    _NpInfoIPExcessRate_Type()
)
npInfoIPExcessRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    npInfoIPExcessRate.setStatus("mandatory")
_NpInfoIPExcessBurst_Type = Integer32
_NpInfoIPExcessBurst_Object = MibTableColumn
npInfoIPExcessBurst = _NpInfoIPExcessBurst_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 4, 3, 1, 8),
    _NpInfoIPExcessBurst_Type()
)
npInfoIPExcessBurst.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    npInfoIPExcessBurst.setStatus("mandatory")
_NpInfoIPNCircuits_Type = Integer32
_NpInfoIPNCircuits_Object = MibTableColumn
npInfoIPNCircuits = _NpInfoIPNCircuits_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 4, 3, 1, 9),
    _NpInfoIPNCircuits_Type()
)
npInfoIPNCircuits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    npInfoIPNCircuits.setStatus("mandatory")


class _NpInfoAdminOperTrigger_Type(Integer32):
    """Custom type npInfoAdminOperTrigger based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              99)
        )
    )
    namedValues = NamedValues(
        *(("other", 99),
          ("trigger", 1))
    )


_NpInfoAdminOperTrigger_Type.__name__ = "Integer32"
_NpInfoAdminOperTrigger_Object = MibTableColumn
npInfoAdminOperTrigger = _NpInfoAdminOperTrigger_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 4, 3, 1, 99),
    _NpInfoAdminOperTrigger_Type()
)
npInfoAdminOperTrigger.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    npInfoAdminOperTrigger.setStatus("mandatory")
_Clc1InfoTable_Object = MibTable
clc1InfoTable = _Clc1InfoTable_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 4, 4)
)
if mibBuilder.loadTexts:
    clc1InfoTable.setStatus("mandatory")
_Clc1InfoEntry_Object = MibTableRow
clc1InfoEntry = _Clc1InfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 4, 4, 1)
)
clc1InfoEntry.setIndexNames(
    (0, "LIGHTSTREAM-MIB", "clc1InfoIfIndex"),
)
if mibBuilder.loadTexts:
    clc1InfoEntry.setStatus("mandatory")
_Clc1InfoIfIndex_Type = Integer32
_Clc1InfoIfIndex_Object = MibTableColumn
clc1InfoIfIndex = _Clc1InfoIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 4, 4, 1, 1),
    _Clc1InfoIfIndex_Type()
)
clc1InfoIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clc1InfoIfIndex.setStatus("mandatory")


class _Clc1InfoOperProtocol_Type(Integer32):
    """Custom type clc1InfoOperProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("atmUni", 2),
          ("trunk", 1),
          ("unknown", 3))
    )


_Clc1InfoOperProtocol_Type.__name__ = "Integer32"
_Clc1InfoOperProtocol_Object = MibTableColumn
clc1InfoOperProtocol = _Clc1InfoOperProtocol_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 4, 4, 1, 4),
    _Clc1InfoOperProtocol_Type()
)
clc1InfoOperProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clc1InfoOperProtocol.setStatus("mandatory")


class _Clc1InfoAdminProtocol_Type(Integer32):
    """Custom type clc1InfoAdminProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("atmUni", 2),
          ("trunk", 1),
          ("unknown", 3))
    )


_Clc1InfoAdminProtocol_Type.__name__ = "Integer32"
_Clc1InfoAdminProtocol_Object = MibTableColumn
clc1InfoAdminProtocol = _Clc1InfoAdminProtocol_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 4, 4, 1, 5),
    _Clc1InfoAdminProtocol_Type()
)
clc1InfoAdminProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clc1InfoAdminProtocol.setStatus("mandatory")


class _Clc1InfoOperLoopMode_Type(Integer32):
    """Custom type clc1InfoOperLoopMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("external", 3),
          ("internal", 2),
          ("none", 1))
    )


_Clc1InfoOperLoopMode_Type.__name__ = "Integer32"
_Clc1InfoOperLoopMode_Object = MibTableColumn
clc1InfoOperLoopMode = _Clc1InfoOperLoopMode_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 4, 4, 1, 6),
    _Clc1InfoOperLoopMode_Type()
)
clc1InfoOperLoopMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clc1InfoOperLoopMode.setStatus("mandatory")


class _Clc1InfoAdminLoopMode_Type(Integer32):
    """Custom type clc1InfoAdminLoopMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("external", 3),
          ("internal", 2),
          ("none", 1))
    )


_Clc1InfoAdminLoopMode_Type.__name__ = "Integer32"
_Clc1InfoAdminLoopMode_Object = MibTableColumn
clc1InfoAdminLoopMode = _Clc1InfoAdminLoopMode_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 4, 4, 1, 7),
    _Clc1InfoAdminLoopMode_Type()
)
clc1InfoAdminLoopMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clc1InfoAdminLoopMode.setStatus("mandatory")
_Clc1InfoOperControlBandwidthSize_Type = Integer32
_Clc1InfoOperControlBandwidthSize_Object = MibTableColumn
clc1InfoOperControlBandwidthSize = _Clc1InfoOperControlBandwidthSize_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 4, 4, 1, 10),
    _Clc1InfoOperControlBandwidthSize_Type()
)
clc1InfoOperControlBandwidthSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clc1InfoOperControlBandwidthSize.setStatus("mandatory")
_Clc1InfoAdminControlBandwidthSize_Type = Integer32
_Clc1InfoAdminControlBandwidthSize_Object = MibTableColumn
clc1InfoAdminControlBandwidthSize = _Clc1InfoAdminControlBandwidthSize_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 4, 4, 1, 11),
    _Clc1InfoAdminControlBandwidthSize_Type()
)
clc1InfoAdminControlBandwidthSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clc1InfoAdminControlBandwidthSize.setStatus("mandatory")
_Clc1InfoOperDataBandwidthSize_Type = Integer32
_Clc1InfoOperDataBandwidthSize_Object = MibTableColumn
clc1InfoOperDataBandwidthSize = _Clc1InfoOperDataBandwidthSize_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 4, 4, 1, 12),
    _Clc1InfoOperDataBandwidthSize_Type()
)
clc1InfoOperDataBandwidthSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clc1InfoOperDataBandwidthSize.setStatus("mandatory")
_Clc1InfoAdminDataBandwidthSize_Type = Integer32
_Clc1InfoAdminDataBandwidthSize_Object = MibTableColumn
clc1InfoAdminDataBandwidthSize = _Clc1InfoAdminDataBandwidthSize_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 4, 4, 1, 13),
    _Clc1InfoAdminDataBandwidthSize_Type()
)
clc1InfoAdminDataBandwidthSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clc1InfoAdminDataBandwidthSize.setStatus("mandatory")


class _Clc1InfoLcAutoEnable_Type(Integer32):
    """Custom type clc1InfoLcAutoEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_Clc1InfoLcAutoEnable_Type.__name__ = "Integer32"
_Clc1InfoLcAutoEnable_Object = MibTableColumn
clc1InfoLcAutoEnable = _Clc1InfoLcAutoEnable_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 4, 4, 1, 14),
    _Clc1InfoLcAutoEnable_Type()
)
clc1InfoLcAutoEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clc1InfoLcAutoEnable.setStatus("mandatory")
_Clc1InfoLcDebugLevel_Type = Integer32
_Clc1InfoLcDebugLevel_Object = MibTableColumn
clc1InfoLcDebugLevel = _Clc1InfoLcDebugLevel_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 4, 4, 1, 15),
    _Clc1InfoLcDebugLevel_Type()
)
clc1InfoLcDebugLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clc1InfoLcDebugLevel.setStatus("mandatory")


class _Clc1InfoOperScramble_Type(Integer32):
    """Custom type clc1InfoOperScramble based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("scrambleDisable", 2),
          ("scrambleEnable", 1))
    )


_Clc1InfoOperScramble_Type.__name__ = "Integer32"
_Clc1InfoOperScramble_Object = MibTableColumn
clc1InfoOperScramble = _Clc1InfoOperScramble_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 4, 4, 1, 16),
    _Clc1InfoOperScramble_Type()
)
clc1InfoOperScramble.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clc1InfoOperScramble.setStatus("mandatory")


class _Clc1InfoAdminScramble_Type(Integer32):
    """Custom type clc1InfoAdminScramble based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("scrambleDisable", 2),
          ("scrambleEnable", 1))
    )


_Clc1InfoAdminScramble_Type.__name__ = "Integer32"
_Clc1InfoAdminScramble_Object = MibTableColumn
clc1InfoAdminScramble = _Clc1InfoAdminScramble_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 4, 4, 1, 17),
    _Clc1InfoAdminScramble_Type()
)
clc1InfoAdminScramble.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clc1InfoAdminScramble.setStatus("mandatory")
_Clc1InfoDataCellCapacity_Type = Integer32
_Clc1InfoDataCellCapacity_Object = MibTableColumn
clc1InfoDataCellCapacity = _Clc1InfoDataCellCapacity_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 4, 4, 1, 18),
    _Clc1InfoDataCellCapacity_Type()
)
clc1InfoDataCellCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clc1InfoDataCellCapacity.setStatus("mandatory")
_Clc1InfoDataCellAvailable_Type = Integer32
_Clc1InfoDataCellAvailable_Object = MibTableColumn
clc1InfoDataCellAvailable = _Clc1InfoDataCellAvailable_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 4, 4, 1, 19),
    _Clc1InfoDataCellAvailable_Type()
)
clc1InfoDataCellAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clc1InfoDataCellAvailable.setStatus("mandatory")
_Clc1InfoLinkUtilization_Type = Integer32
_Clc1InfoLinkUtilization_Object = MibTableColumn
clc1InfoLinkUtilization = _Clc1InfoLinkUtilization_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 4, 4, 1, 20),
    _Clc1InfoLinkUtilization_Type()
)
clc1InfoLinkUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clc1InfoLinkUtilization.setStatus("mandatory")


class _Clc1InfoOperClock_Type(Integer32):
    """Custom type clc1InfoOperClock based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("externalClock", 2),
          ("internalClock", 1))
    )


_Clc1InfoOperClock_Type.__name__ = "Integer32"
_Clc1InfoOperClock_Object = MibTableColumn
clc1InfoOperClock = _Clc1InfoOperClock_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 4, 4, 1, 21),
    _Clc1InfoOperClock_Type()
)
clc1InfoOperClock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clc1InfoOperClock.setStatus("mandatory")


class _Clc1InfoAdminClock_Type(Integer32):
    """Custom type clc1InfoAdminClock based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("externalClock", 2),
          ("internalClock", 1))
    )


_Clc1InfoAdminClock_Type.__name__ = "Integer32"
_Clc1InfoAdminClock_Object = MibTableColumn
clc1InfoAdminClock = _Clc1InfoAdminClock_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 4, 4, 1, 22),
    _Clc1InfoAdminClock_Type()
)
clc1InfoAdminClock.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clc1InfoAdminClock.setStatus("mandatory")


class _Clc1InfoAdminOperTrigger_Type(Integer32):
    """Custom type clc1InfoAdminOperTrigger based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              99)
        )
    )
    namedValues = NamedValues(
        *(("other", 99),
          ("trigger", 1))
    )


_Clc1InfoAdminOperTrigger_Type.__name__ = "Integer32"
_Clc1InfoAdminOperTrigger_Object = MibTableColumn
clc1InfoAdminOperTrigger = _Clc1InfoAdminOperTrigger_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 4, 4, 1, 99),
    _Clc1InfoAdminOperTrigger_Type()
)
clc1InfoAdminOperTrigger.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clc1InfoAdminOperTrigger.setStatus("mandatory")
_Oc3InfoTable_Object = MibTable
oc3InfoTable = _Oc3InfoTable_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 4, 5)
)
if mibBuilder.loadTexts:
    oc3InfoTable.setStatus("mandatory")
_Oc3InfoEntry_Object = MibTableRow
oc3InfoEntry = _Oc3InfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 4, 5, 1)
)
oc3InfoEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    oc3InfoEntry.setStatus("mandatory")


class _Oc3InfoReceiveSignalDetect_Type(Integer32):
    """Custom type oc3InfoReceiveSignalDetect based on Integer32"""
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


_Oc3InfoReceiveSignalDetect_Type.__name__ = "Integer32"
_Oc3InfoReceiveSignalDetect_Object = MibTableColumn
oc3InfoReceiveSignalDetect = _Oc3InfoReceiveSignalDetect_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 4, 5, 1, 1),
    _Oc3InfoReceiveSignalDetect_Type()
)
oc3InfoReceiveSignalDetect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oc3InfoReceiveSignalDetect.setStatus("mandatory")


class _Oc3InfoTransmitSafetySwitch_Type(Integer32):
    """Custom type oc3InfoTransmitSafetySwitch based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_Oc3InfoTransmitSafetySwitch_Type.__name__ = "Integer32"
_Oc3InfoTransmitSafetySwitch_Object = MibTableColumn
oc3InfoTransmitSafetySwitch = _Oc3InfoTransmitSafetySwitch_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 4, 5, 1, 2),
    _Oc3InfoTransmitSafetySwitch_Type()
)
oc3InfoTransmitSafetySwitch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oc3InfoTransmitSafetySwitch.setStatus("mandatory")


class _Oc3InfoMediumType_Type(Integer32):
    """Custom type oc3InfoMediumType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("sdh", 2),
          ("sonet", 1))
    )


_Oc3InfoMediumType_Type.__name__ = "Integer32"
_Oc3InfoMediumType_Object = MibTableColumn
oc3InfoMediumType = _Oc3InfoMediumType_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 4, 5, 1, 3),
    _Oc3InfoMediumType_Type()
)
oc3InfoMediumType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oc3InfoMediumType.setStatus("mandatory")
_CongestionAvoidance_ObjectIdentity = ObjectIdentity
congestionAvoidance = _CongestionAvoidance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 5)
)
_CaMaxIntervalPermitLimit_Type = Integer32
_CaMaxIntervalPermitLimit_Object = MibScalar
caMaxIntervalPermitLimit = _CaMaxIntervalPermitLimit_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 5, 1),
    _CaMaxIntervalPermitLimit_Type()
)
caMaxIntervalPermitLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    caMaxIntervalPermitLimit.setStatus("mandatory")
_CaMinIntervalPermitLimit_Type = Integer32
_CaMinIntervalPermitLimit_Object = MibScalar
caMinIntervalPermitLimit = _CaMinIntervalPermitLimit_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 5, 2),
    _CaMinIntervalPermitLimit_Type()
)
caMinIntervalPermitLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    caMinIntervalPermitLimit.setStatus("mandatory")
_CaMinIntervalCaInfo_Type = Integer32
_CaMinIntervalCaInfo_Object = MibScalar
caMinIntervalCaInfo = _CaMinIntervalCaInfo_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 5, 3),
    _CaMinIntervalCaInfo_Type()
)
caMinIntervalCaInfo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    caMinIntervalCaInfo.setStatus("mandatory")
_MmaInfo_ObjectIdentity = ObjectIdentity
mmaInfo = _MmaInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 6)
)


class _MmaDbActive_Type(Integer32):
    """Custom type mmaDbActive based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("inactive", 1),
          ("newDBactive", 2))
    )


_MmaDbActive_Type.__name__ = "Integer32"
_MmaDbActive_Object = MibScalar
mmaDbActive = _MmaDbActive_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 6, 1),
    _MmaDbActive_Type()
)
mmaDbActive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mmaDbActive.setStatus("mandatory")


class _MmaTrapFilter_Type(Integer32):
    """Custom type mmaTrapFilter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("debug", 4),
          ("informational", 2),
          ("operational", 1),
          ("trace", 3))
    )


_MmaTrapFilter_Type.__name__ = "Integer32"
_MmaTrapFilter_Object = MibScalar
mmaTrapFilter = _MmaTrapFilter_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 6, 2),
    _MmaTrapFilter_Type()
)
mmaTrapFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mmaTrapFilter.setStatus("mandatory")


class _MmaTrapLanguage_Type(Integer32):
    """Custom type mmaTrapLanguage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("english", 1)
    )


_MmaTrapLanguage_Type.__name__ = "Integer32"
_MmaTrapLanguage_Object = MibScalar
mmaTrapLanguage = _MmaTrapLanguage_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 6, 3),
    _MmaTrapLanguage_Type()
)
mmaTrapLanguage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mmaTrapLanguage.setStatus("mandatory")
_MmaCollectionSpace_Type = Integer32
_MmaCollectionSpace_Object = MibScalar
mmaCollectionSpace = _MmaCollectionSpace_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 6, 4),
    _MmaCollectionSpace_Type()
)
mmaCollectionSpace.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mmaCollectionSpace.setStatus("mandatory")


class _MmaConfigHost_Type(OctetString):
    """Custom type mmaConfigHost based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_MmaConfigHost_Type.__name__ = "OctetString"
_MmaConfigHost_Object = MibScalar
mmaConfigHost = _MmaConfigHost_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 6, 5),
    _MmaConfigHost_Type()
)
mmaConfigHost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mmaConfigHost.setStatus("mandatory")


class _MmaConfigAuthor_Type(OctetString):
    """Custom type mmaConfigAuthor based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_MmaConfigAuthor_Type.__name__ = "OctetString"
_MmaConfigAuthor_Object = MibScalar
mmaConfigAuthor = _MmaConfigAuthor_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 6, 6),
    _MmaConfigAuthor_Type()
)
mmaConfigAuthor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mmaConfigAuthor.setStatus("mandatory")
_MmaConfigID_Type = Integer32
_MmaConfigID_Object = MibScalar
mmaConfigID = _MmaConfigID_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 6, 7),
    _MmaConfigID_Type()
)
mmaConfigID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mmaConfigID.setStatus("mandatory")


class _MmaSetLock_Type(Integer32):
    """Custom type mmaSetLock based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("lockPermanent", 3),
          ("lockVolatile", 2),
          ("unlock", 1))
    )


_MmaSetLock_Type.__name__ = "Integer32"
_MmaSetLock_Object = MibScalar
mmaSetLock = _MmaSetLock_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 6, 8),
    _MmaSetLock_Type()
)
mmaSetLock.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mmaSetLock.setStatus("mandatory")
_MmaPID_Type = Integer32
_MmaPID_Object = MibScalar
mmaPID = _MmaPID_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 6, 9),
    _MmaPID_Type()
)
mmaPID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mmaPID.setStatus("mandatory")


class _MmaTrapLog_Type(Integer32):
    """Custom type mmaTrapLog based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_MmaTrapLog_Type.__name__ = "Integer32"
_MmaTrapLog_Object = MibScalar
mmaTrapLog = _MmaTrapLog_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 6, 10),
    _MmaTrapLog_Type()
)
mmaTrapLog.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mmaTrapLog.setStatus("mandatory")
_MmaTrapNumber_Type = Integer32
_MmaTrapNumber_Object = MibScalar
mmaTrapNumber = _MmaTrapNumber_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 6, 13),
    _MmaTrapNumber_Type()
)
mmaTrapNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mmaTrapNumber.setStatus("mandatory")


class _MmaTrapOnOffState_Type(Integer32):
    """Custom type mmaTrapOnOffState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("trapDisable", 4),
          ("trapEnable", 3),
          ("trapOff", 2),
          ("trapOn", 1))
    )


_MmaTrapOnOffState_Type.__name__ = "Integer32"
_MmaTrapOnOffState_Object = MibScalar
mmaTrapOnOffState = _MmaTrapOnOffState_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 6, 14),
    _MmaTrapOnOffState_Type()
)
mmaTrapOnOffState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mmaTrapOnOffState.setStatus("mandatory")
_MmaNumNameTable_Object = MibTable
mmaNumNameTable = _MmaNumNameTable_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 6, 16)
)
if mibBuilder.loadTexts:
    mmaNumNameTable.setStatus("mandatory")
_MmaNumNameEntry_Object = MibTableRow
mmaNumNameEntry = _MmaNumNameEntry_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 6, 16, 1)
)
mmaNumNameEntry.setIndexNames(
    (0, "LIGHTSTREAM-MIB", "mmaNumNameNumber"),
)
if mibBuilder.loadTexts:
    mmaNumNameEntry.setStatus("mandatory")
_MmaNumNameNumber_Type = Integer32
_MmaNumNameNumber_Object = MibTableColumn
mmaNumNameNumber = _MmaNumNameNumber_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 6, 16, 1, 1),
    _MmaNumNameNumber_Type()
)
mmaNumNameNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mmaNumNameNumber.setStatus("mandatory")
_MmaNumName_Type = DisplayString
_MmaNumName_Object = MibTableColumn
mmaNumName = _MmaNumName_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 6, 16, 1, 2),
    _MmaNumName_Type()
)
mmaNumName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mmaNumName.setStatus("mandatory")
_MmaLwmpTimeouts_Type = Counter32
_MmaLwmpTimeouts_Object = MibScalar
mmaLwmpTimeouts = _MmaLwmpTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 6, 20),
    _MmaLwmpTimeouts_Type()
)
mmaLwmpTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mmaLwmpTimeouts.setStatus("mandatory")
_CollectInfo_ObjectIdentity = ObjectIdentity
collectInfo = _CollectInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 7)
)
_CollectTable_Object = MibTable
collectTable = _CollectTable_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 7, 1)
)
if mibBuilder.loadTexts:
    collectTable.setStatus("mandatory")
_CollectEntry_Object = MibTableRow
collectEntry = _CollectEntry_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 7, 1, 1)
)
collectEntry.setIndexNames(
    (0, "LIGHTSTREAM-MIB", "collectIndex"),
)
if mibBuilder.loadTexts:
    collectEntry.setStatus("mandatory")
_CollectIndex_Type = Integer32
_CollectIndex_Object = MibTableColumn
collectIndex = _CollectIndex_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 7, 1, 1, 1),
    _CollectIndex_Type()
)
collectIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    collectIndex.setStatus("mandatory")


class _CollectStatus_Type(Integer32):
    """Custom type collectStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("createRequest", 2),
          ("invalid", 4),
          ("underCreation", 3),
          ("valid", 1))
    )


_CollectStatus_Type.__name__ = "Integer32"
_CollectStatus_Object = MibTableColumn
collectStatus = _CollectStatus_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 7, 1, 1, 2),
    _CollectStatus_Type()
)
collectStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    collectStatus.setStatus("mandatory")
_CollectStart_Type = Integer32
_CollectStart_Object = MibTableColumn
collectStart = _CollectStart_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 7, 1, 1, 3),
    _CollectStart_Type()
)
collectStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    collectStart.setStatus("mandatory")
_CollectFinish_Type = Integer32
_CollectFinish_Object = MibTableColumn
collectFinish = _CollectFinish_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 7, 1, 1, 4),
    _CollectFinish_Type()
)
collectFinish.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    collectFinish.setStatus("mandatory")
_CollectInterval_Type = Integer32
_CollectInterval_Object = MibTableColumn
collectInterval = _CollectInterval_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 7, 1, 1, 5),
    _CollectInterval_Type()
)
collectInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    collectInterval.setStatus("mandatory")


class _CollectFileName_Type(DisplayString):
    """Custom type collectFileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CollectFileName_Type.__name__ = "DisplayString"
_CollectFileName_Object = MibTableColumn
collectFileName = _CollectFileName_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 7, 1, 1, 6),
    _CollectFileName_Type()
)
collectFileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    collectFileName.setStatus("mandatory")
_CollectFileSize_Type = Integer32
_CollectFileSize_Object = MibTableColumn
collectFileSize = _CollectFileSize_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 7, 1, 1, 7),
    _CollectFileSize_Type()
)
collectFileSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    collectFileSize.setStatus("mandatory")


class _CollectOperStatus_Type(Integer32):
    """Custom type collectOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("running", 2),
          ("underCreation", 3),
          ("waiting", 1))
    )


_CollectOperStatus_Type.__name__ = "Integer32"
_CollectOperStatus_Object = MibTableColumn
collectOperStatus = _CollectOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 7, 1, 1, 8),
    _CollectOperStatus_Type()
)
collectOperStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    collectOperStatus.setStatus("mandatory")
_CollectDataBase_Object = MibTable
collectDataBase = _CollectDataBase_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 7, 2)
)
if mibBuilder.loadTexts:
    collectDataBase.setStatus("mandatory")
_CollectDbEntry_Object = MibTableRow
collectDbEntry = _CollectDbEntry_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 7, 2, 1)
)
collectDbEntry.setIndexNames(
    (0, "LIGHTSTREAM-MIB", "collectDBIndex"),
    (0, "LIGHTSTREAM-MIB", "collectDBInstance"),
)
if mibBuilder.loadTexts:
    collectDbEntry.setStatus("mandatory")
_CollectDBIndex_Type = Integer32
_CollectDBIndex_Object = MibTableColumn
collectDBIndex = _CollectDBIndex_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 7, 2, 1, 1),
    _CollectDBIndex_Type()
)
collectDBIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    collectDBIndex.setStatus("mandatory")
_CollectDBInstance_Type = Integer32
_CollectDBInstance_Object = MibTableColumn
collectDBInstance = _CollectDBInstance_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 7, 2, 1, 2),
    _CollectDBInstance_Type()
)
collectDBInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    collectDBInstance.setStatus("mandatory")
_CollectDBObjectID_Type = ObjectIdentifier
_CollectDBObjectID_Object = MibTableColumn
collectDBObjectID = _CollectDBObjectID_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 7, 2, 1, 3),
    _CollectDBObjectID_Type()
)
collectDBObjectID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    collectDBObjectID.setStatus("mandatory")


class _CollectDBStatus_Type(Integer32):
    """Custom type collectDBStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("createRequest", 2),
          ("invalid", 4),
          ("underCreation", 3),
          ("valid", 1))
    )


_CollectDBStatus_Type.__name__ = "Integer32"
_CollectDBStatus_Object = MibTableColumn
collectDBStatus = _CollectDBStatus_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 7, 2, 1, 4),
    _CollectDBStatus_Type()
)
collectDBStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    collectDBStatus.setStatus("mandatory")


class _CollectCommunityName_Type(DisplayString):
    """Custom type collectCommunityName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CollectCommunityName_Type.__name__ = "DisplayString"
_CollectCommunityName_Object = MibScalar
collectCommunityName = _CollectCommunityName_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 7, 3),
    _CollectCommunityName_Type()
)
collectCommunityName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    collectCommunityName.setStatus("mandatory")


class _RmonCommunityName_Type(DisplayString):
    """Custom type rmonCommunityName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_RmonCommunityName_Type.__name__ = "DisplayString"
_RmonCommunityName_Object = MibScalar
rmonCommunityName = _RmonCommunityName_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 7, 4),
    _RmonCommunityName_Type()
)
rmonCommunityName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmonCommunityName.setStatus("mandatory")
_LsPortProtocols_ObjectIdentity = ObjectIdentity
lsPortProtocols = _LsPortProtocols_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 8)
)
_EdgePort_ObjectIdentity = ObjectIdentity
edgePort = _EdgePort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 8, 1)
)
_EdgePortTable_Object = MibTable
edgePortTable = _EdgePortTable_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 8, 1, 1)
)
if mibBuilder.loadTexts:
    edgePortTable.setStatus("mandatory")
_EdgePortEntry_Object = MibTableRow
edgePortEntry = _EdgePortEntry_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 8, 1, 1, 1)
)
edgePortEntry.setIndexNames(
    (0, "LIGHTSTREAM-MIB", "edgeIfIndex"),
)
if mibBuilder.loadTexts:
    edgePortEntry.setStatus("mandatory")
_EdgeIfIndex_Type = Integer32
_EdgeIfIndex_Object = MibTableColumn
edgeIfIndex = _EdgeIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 8, 1, 1, 1, 1),
    _EdgeIfIndex_Type()
)
edgeIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edgeIfIndex.setStatus("mandatory")


class _EdgeUpcType_Type(Integer32):
    """Custom type edgeUpcType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("ansiCompliant", 1)
    )


_EdgeUpcType_Type.__name__ = "Integer32"
_EdgeUpcType_Object = MibTableColumn
edgeUpcType = _EdgeUpcType_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 8, 1, 1, 1, 2),
    _EdgeUpcType_Type()
)
edgeUpcType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    edgeUpcType.setStatus("mandatory")


class _EdgeUserDataPerCell_Type(Integer32):
    """Custom type edgeUserDataPerCell based on Integer32"""
    defaultValue = 341

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 384),
    )


_EdgeUserDataPerCell_Type.__name__ = "Integer32"
_EdgeUserDataPerCell_Object = MibTableColumn
edgeUserDataPerCell = _EdgeUserDataPerCell_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 8, 1, 1, 1, 3),
    _EdgeUserDataPerCell_Type()
)
edgeUserDataPerCell.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    edgeUserDataPerCell.setStatus("mandatory")
_EdgeCellDelayVariance_Type = Integer32
_EdgeCellDelayVariance_Object = MibTableColumn
edgeCellDelayVariance = _EdgeCellDelayVariance_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 8, 1, 1, 1, 4),
    _EdgeCellDelayVariance_Type()
)
edgeCellDelayVariance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    edgeCellDelayVariance.setStatus("mandatory")


class _EdgePrincipalScale_Type(Integer32):
    """Custom type edgePrincipalScale based on Integer32"""
    defaultValue = 100


_EdgePrincipalScale_Object = MibTableColumn
edgePrincipalScale = _EdgePrincipalScale_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 8, 1, 1, 1, 5),
    _EdgePrincipalScale_Type()
)
edgePrincipalScale.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    edgePrincipalScale.setStatus("mandatory")


class _EdgeSecondaryScale_Type(Integer32):
    """Custom type edgeSecondaryScale based on Integer32"""
    defaultValue = 2


_EdgeSecondaryScale_Object = MibTableColumn
edgeSecondaryScale = _EdgeSecondaryScale_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 8, 1, 1, 1, 6),
    _EdgeSecondaryScale_Type()
)
edgeSecondaryScale.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    edgeSecondaryScale.setStatus("mandatory")


class _EdgeMeteringFactor_Type(Integer32):
    """Custom type edgeMeteringFactor based on Integer32"""
    defaultValue = 64


_EdgeMeteringFactor_Object = MibTableColumn
edgeMeteringFactor = _EdgeMeteringFactor_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 8, 1, 1, 1, 7),
    _EdgeMeteringFactor_Type()
)
edgeMeteringFactor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    edgeMeteringFactor.setStatus("mandatory")


class _EdgeMeteringBurstSize_Type(Integer32):
    """Custom type edgeMeteringBurstSize based on Integer32"""
    defaultValue = 5


_EdgeMeteringBurstSize_Object = MibTableColumn
edgeMeteringBurstSize = _EdgeMeteringBurstSize_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 8, 1, 1, 1, 8),
    _EdgeMeteringBurstSize_Type()
)
edgeMeteringBurstSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    edgeMeteringBurstSize.setStatus("mandatory")


class _EdgeCallSetupRetry_Type(Integer32):
    """Custom type edgeCallSetupRetry based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3600),
    )


_EdgeCallSetupRetry_Type.__name__ = "Integer32"
_EdgeCallSetupRetry_Object = MibTableColumn
edgeCallSetupRetry = _EdgeCallSetupRetry_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 8, 1, 1, 1, 9),
    _EdgeCallSetupRetry_Type()
)
edgeCallSetupRetry.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    edgeCallSetupRetry.setStatus("mandatory")


class _EdgeCallSetupBackoff_Type(Integer32):
    """Custom type edgeCallSetupBackoff based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_EdgeCallSetupBackoff_Type.__name__ = "Integer32"
_EdgeCallSetupBackoff_Object = MibTableColumn
edgeCallSetupBackoff = _EdgeCallSetupBackoff_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 8, 1, 1, 1, 10),
    _EdgeCallSetupBackoff_Type()
)
edgeCallSetupBackoff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    edgeCallSetupBackoff.setStatus("mandatory")


class _EdgeMaxFrameSize_Type(Integer32):
    """Custom type edgeMaxFrameSize based on Integer32"""
    defaultValue = 1516

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(48, 8152),
    )


_EdgeMaxFrameSize_Type.__name__ = "Integer32"
_EdgeMaxFrameSize_Object = MibTableColumn
edgeMaxFrameSize = _EdgeMaxFrameSize_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 8, 1, 1, 1, 11),
    _EdgeMaxFrameSize_Type()
)
edgeMaxFrameSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    edgeMaxFrameSize.setStatus("mandatory")
_FrDceInfo_ObjectIdentity = ObjectIdentity
frDceInfo = _FrDceInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 8, 2)
)
_FrProvMiTable_Object = MibTable
frProvMiTable = _FrProvMiTable_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 8, 2, 1)
)
if mibBuilder.loadTexts:
    frProvMiTable.setStatus("mandatory")
_FrProvMiEntry_Object = MibTableRow
frProvMiEntry = _FrProvMiEntry_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 8, 2, 1, 1)
)
frProvMiEntry.setIndexNames(
    (0, "LIGHTSTREAM-MIB", "frProvMiIfIndex"),
)
if mibBuilder.loadTexts:
    frProvMiEntry.setStatus("mandatory")
_FrProvMiIfIndex_Type = Integer32
_FrProvMiIfIndex_Object = MibTableColumn
frProvMiIfIndex = _FrProvMiIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 8, 2, 1, 1, 1),
    _FrProvMiIfIndex_Type()
)
frProvMiIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frProvMiIfIndex.setStatus("mandatory")


class _FrProvMiState_Type(Integer32):
    """Custom type frProvMiState based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("ansiT1-617-D", 3),
          ("ccittQ-933-A", 4),
          ("lmiFRIF", 2),
          ("noLmiConfigured", 1))
    )


_FrProvMiState_Type.__name__ = "Integer32"
_FrProvMiState_Object = MibTableColumn
frProvMiState = _FrProvMiState_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 8, 2, 1, 1, 2),
    _FrProvMiState_Type()
)
frProvMiState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frProvMiState.setStatus("mandatory")


class _FrProvMiAddressLen_Type(Integer32):
    """Custom type frProvMiAddressLen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            2
        )
    )
    namedValues = NamedValues(
        ("two-octets", 2)
    )


_FrProvMiAddressLen_Type.__name__ = "Integer32"
_FrProvMiAddressLen_Object = MibTableColumn
frProvMiAddressLen = _FrProvMiAddressLen_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 8, 2, 1, 1, 3),
    _FrProvMiAddressLen_Type()
)
frProvMiAddressLen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frProvMiAddressLen.setStatus("mandatory")


class _FrProvMiNetRequestInterval_Type(Integer32):
    """Custom type frProvMiNetRequestInterval based on Integer32"""
    defaultValue = 15

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 30),
    )


_FrProvMiNetRequestInterval_Type.__name__ = "Integer32"
_FrProvMiNetRequestInterval_Object = MibTableColumn
frProvMiNetRequestInterval = _FrProvMiNetRequestInterval_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 8, 2, 1, 1, 4),
    _FrProvMiNetRequestInterval_Type()
)
frProvMiNetRequestInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frProvMiNetRequestInterval.setStatus("mandatory")


class _FrProvMiNetErrorThreshold_Type(Integer32):
    """Custom type frProvMiNetErrorThreshold based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_FrProvMiNetErrorThreshold_Type.__name__ = "Integer32"
_FrProvMiNetErrorThreshold_Object = MibTableColumn
frProvMiNetErrorThreshold = _FrProvMiNetErrorThreshold_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 8, 2, 1, 1, 5),
    _FrProvMiNetErrorThreshold_Type()
)
frProvMiNetErrorThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frProvMiNetErrorThreshold.setStatus("mandatory")


class _FrProvMiNetMonitoredEvents_Type(Integer32):
    """Custom type frProvMiNetMonitoredEvents based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_FrProvMiNetMonitoredEvents_Type.__name__ = "Integer32"
_FrProvMiNetMonitoredEvents_Object = MibTableColumn
frProvMiNetMonitoredEvents = _FrProvMiNetMonitoredEvents_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 8, 2, 1, 1, 6),
    _FrProvMiNetMonitoredEvents_Type()
)
frProvMiNetMonitoredEvents.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frProvMiNetMonitoredEvents.setStatus("mandatory")
_FrProvMiMaxSupportedVCs_Type = Integer32
_FrProvMiMaxSupportedVCs_Object = MibTableColumn
frProvMiMaxSupportedVCs = _FrProvMiMaxSupportedVCs_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 8, 2, 1, 1, 7),
    _FrProvMiMaxSupportedVCs_Type()
)
frProvMiMaxSupportedVCs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frProvMiMaxSupportedVCs.setStatus("mandatory")


class _FrProvMiMulticast_Type(Integer32):
    """Custom type frProvMiMulticast based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("nonBroadcast", 1)
    )


_FrProvMiMulticast_Type.__name__ = "Integer32"
_FrProvMiMulticast_Object = MibTableColumn
frProvMiMulticast = _FrProvMiMulticast_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 8, 2, 1, 1, 8),
    _FrProvMiMulticast_Type()
)
frProvMiMulticast.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frProvMiMulticast.setStatus("mandatory")


class _FrProvMiUserPollingInterval_Type(Integer32):
    """Custom type frProvMiUserPollingInterval based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 30),
    )


_FrProvMiUserPollingInterval_Type.__name__ = "Integer32"
_FrProvMiUserPollingInterval_Object = MibTableColumn
frProvMiUserPollingInterval = _FrProvMiUserPollingInterval_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 8, 2, 1, 1, 9),
    _FrProvMiUserPollingInterval_Type()
)
frProvMiUserPollingInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frProvMiUserPollingInterval.setStatus("mandatory")


class _FrProvMiUserFullEnquiryInterval_Type(Integer32):
    """Custom type frProvMiUserFullEnquiryInterval based on Integer32"""
    defaultValue = 6

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_FrProvMiUserFullEnquiryInterval_Type.__name__ = "Integer32"
_FrProvMiUserFullEnquiryInterval_Object = MibTableColumn
frProvMiUserFullEnquiryInterval = _FrProvMiUserFullEnquiryInterval_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 8, 2, 1, 1, 10),
    _FrProvMiUserFullEnquiryInterval_Type()
)
frProvMiUserFullEnquiryInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frProvMiUserFullEnquiryInterval.setStatus("mandatory")


class _FrProvMiUserErrorThreshold_Type(Integer32):
    """Custom type frProvMiUserErrorThreshold based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_FrProvMiUserErrorThreshold_Type.__name__ = "Integer32"
_FrProvMiUserErrorThreshold_Object = MibTableColumn
frProvMiUserErrorThreshold = _FrProvMiUserErrorThreshold_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 8, 2, 1, 1, 11),
    _FrProvMiUserErrorThreshold_Type()
)
frProvMiUserErrorThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frProvMiUserErrorThreshold.setStatus("mandatory")


class _FrProvMiUserMonitoredEvents_Type(Integer32):
    """Custom type frProvMiUserMonitoredEvents based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_FrProvMiUserMonitoredEvents_Type.__name__ = "Integer32"
_FrProvMiUserMonitoredEvents_Object = MibTableColumn
frProvMiUserMonitoredEvents = _FrProvMiUserMonitoredEvents_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 8, 2, 1, 1, 12),
    _FrProvMiUserMonitoredEvents_Type()
)
frProvMiUserMonitoredEvents.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frProvMiUserMonitoredEvents.setStatus("mandatory")


class _FrProvMiNetInterfaceType_Type(Integer32):
    """Custom type frProvMiNetInterfaceType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("niNNI", 2),
          ("niUNI", 1))
    )


_FrProvMiNetInterfaceType_Type.__name__ = "Integer32"
_FrProvMiNetInterfaceType_Object = MibTableColumn
frProvMiNetInterfaceType = _FrProvMiNetInterfaceType_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 8, 2, 1, 1, 13),
    _FrProvMiNetInterfaceType_Type()
)
frProvMiNetInterfaceType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frProvMiNetInterfaceType.setStatus("mandatory")
_FrCktInfo_ObjectIdentity = ObjectIdentity
frCktInfo = _FrCktInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 8, 3)
)
_FrCktCfgTable_Object = MibTable
frCktCfgTable = _FrCktCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 8, 3, 1)
)
if mibBuilder.loadTexts:
    frCktCfgTable.setStatus("mandatory")
_FrCktEntry_Object = MibTableRow
frCktEntry = _FrCktEntry_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 8, 3, 1, 1)
)
frCktEntry.setIndexNames(
    (0, "LIGHTSTREAM-MIB", "frCktSrcIfIndex"),
    (0, "LIGHTSTREAM-MIB", "frCktSrcDlci"),
)
if mibBuilder.loadTexts:
    frCktEntry.setStatus("mandatory")
_FrCktSrcNode_Type = Integer32
_FrCktSrcNode_Object = MibTableColumn
frCktSrcNode = _FrCktSrcNode_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 8, 3, 1, 1, 1),
    _FrCktSrcNode_Type()
)
frCktSrcNode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frCktSrcNode.setStatus("mandatory")
_FrCktSrcIfIndex_Type = Integer32
_FrCktSrcIfIndex_Object = MibTableColumn
frCktSrcIfIndex = _FrCktSrcIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 8, 3, 1, 1, 2),
    _FrCktSrcIfIndex_Type()
)
frCktSrcIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frCktSrcIfIndex.setStatus("mandatory")
_FrCktSrcDlci_Type = LightStreamDLCI
_FrCktSrcDlci_Object = MibTableColumn
frCktSrcDlci = _FrCktSrcDlci_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 8, 3, 1, 1, 3),
    _FrCktSrcDlci_Type()
)
frCktSrcDlci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frCktSrcDlci.setStatus("mandatory")
_FrCktAdminDestNode_Type = Integer32
_FrCktAdminDestNode_Object = MibTableColumn
frCktAdminDestNode = _FrCktAdminDestNode_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 8, 3, 1, 1, 10),
    _FrCktAdminDestNode_Type()
)
frCktAdminDestNode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frCktAdminDestNode.setStatus("mandatory")
_FrCktOperDestNode_Type = Integer32
_FrCktOperDestNode_Object = MibTableColumn
frCktOperDestNode = _FrCktOperDestNode_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 8, 3, 1, 1, 11),
    _FrCktOperDestNode_Type()
)
frCktOperDestNode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frCktOperDestNode.setStatus("mandatory")
_FrCktAdminDestIfIndex_Type = Integer32
_FrCktAdminDestIfIndex_Object = MibTableColumn
frCktAdminDestIfIndex = _FrCktAdminDestIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 8, 3, 1, 1, 12),
    _FrCktAdminDestIfIndex_Type()
)
frCktAdminDestIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frCktAdminDestIfIndex.setStatus("mandatory")
_FrCktOperDestIfIndex_Type = Integer32
_FrCktOperDestIfIndex_Object = MibTableColumn
frCktOperDestIfIndex = _FrCktOperDestIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 8, 3, 1, 1, 13),
    _FrCktOperDestIfIndex_Type()
)
frCktOperDestIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frCktOperDestIfIndex.setStatus("mandatory")
_FrCktAdminDestDlci_Type = LightStreamDLCI
_FrCktAdminDestDlci_Object = MibTableColumn
frCktAdminDestDlci = _FrCktAdminDestDlci_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 8, 3, 1, 1, 14),
    _FrCktAdminDestDlci_Type()
)
frCktAdminDestDlci.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frCktAdminDestDlci.setStatus("mandatory")
_FrCktOperDestDlci_Type = LightStreamDLCI
_FrCktOperDestDlci_Object = MibTableColumn
frCktOperDestDlci = _FrCktOperDestDlci_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 8, 3, 1, 1, 15),
    _FrCktOperDestDlci_Type()
)
frCktOperDestDlci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frCktOperDestDlci.setStatus("mandatory")


class _FrCktAdminSrcInsuredRate_Type(Integer32):
    """Custom type frCktAdminSrcInsuredRate based on Integer32"""
    defaultValue = 0


_FrCktAdminSrcInsuredRate_Object = MibTableColumn
frCktAdminSrcInsuredRate = _FrCktAdminSrcInsuredRate_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 8, 3, 1, 1, 25),
    _FrCktAdminSrcInsuredRate_Type()
)
frCktAdminSrcInsuredRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frCktAdminSrcInsuredRate.setStatus("mandatory")


class _FrCktOperSrcInsuredRate_Type(Integer32):
    """Custom type frCktOperSrcInsuredRate based on Integer32"""
    defaultValue = 0


_FrCktOperSrcInsuredRate_Object = MibTableColumn
frCktOperSrcInsuredRate = _FrCktOperSrcInsuredRate_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 8, 3, 1, 1, 26),
    _FrCktOperSrcInsuredRate_Type()
)
frCktOperSrcInsuredRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frCktOperSrcInsuredRate.setStatus("mandatory")


class _FrCktAdminSrcInsuredBurst_Type(Integer32):
    """Custom type frCktAdminSrcInsuredBurst based on Integer32"""
    defaultValue = 0


_FrCktAdminSrcInsuredBurst_Object = MibTableColumn
frCktAdminSrcInsuredBurst = _FrCktAdminSrcInsuredBurst_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 8, 3, 1, 1, 27),
    _FrCktAdminSrcInsuredBurst_Type()
)
frCktAdminSrcInsuredBurst.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frCktAdminSrcInsuredBurst.setStatus("mandatory")


class _FrCktOperSrcInsuredBurst_Type(Integer32):
    """Custom type frCktOperSrcInsuredBurst based on Integer32"""
    defaultValue = 0


_FrCktOperSrcInsuredBurst_Object = MibTableColumn
frCktOperSrcInsuredBurst = _FrCktOperSrcInsuredBurst_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 8, 3, 1, 1, 28),
    _FrCktOperSrcInsuredBurst_Type()
)
frCktOperSrcInsuredBurst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frCktOperSrcInsuredBurst.setStatus("mandatory")


class _FrCktAdminSrcMaxRate_Type(Integer32):
    """Custom type frCktAdminSrcMaxRate based on Integer32"""
    defaultValue = 0


_FrCktAdminSrcMaxRate_Object = MibTableColumn
frCktAdminSrcMaxRate = _FrCktAdminSrcMaxRate_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 8, 3, 1, 1, 29),
    _FrCktAdminSrcMaxRate_Type()
)
frCktAdminSrcMaxRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frCktAdminSrcMaxRate.setStatus("mandatory")


class _FrCktOperSrcMaxRate_Type(Integer32):
    """Custom type frCktOperSrcMaxRate based on Integer32"""
    defaultValue = 0


_FrCktOperSrcMaxRate_Object = MibTableColumn
frCktOperSrcMaxRate = _FrCktOperSrcMaxRate_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 8, 3, 1, 1, 30),
    _FrCktOperSrcMaxRate_Type()
)
frCktOperSrcMaxRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frCktOperSrcMaxRate.setStatus("mandatory")


class _FrCktAdminSrcMaxBurst_Type(Integer32):
    """Custom type frCktAdminSrcMaxBurst based on Integer32"""
    defaultValue = 0


_FrCktAdminSrcMaxBurst_Object = MibTableColumn
frCktAdminSrcMaxBurst = _FrCktAdminSrcMaxBurst_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 8, 3, 1, 1, 31),
    _FrCktAdminSrcMaxBurst_Type()
)
frCktAdminSrcMaxBurst.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frCktAdminSrcMaxBurst.setStatus("mandatory")


class _FrCktOperSrcMaxBurst_Type(Integer32):
    """Custom type frCktOperSrcMaxBurst based on Integer32"""
    defaultValue = 0


_FrCktOperSrcMaxBurst_Object = MibTableColumn
frCktOperSrcMaxBurst = _FrCktOperSrcMaxBurst_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 8, 3, 1, 1, 32),
    _FrCktOperSrcMaxBurst_Type()
)
frCktOperSrcMaxBurst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frCktOperSrcMaxBurst.setStatus("mandatory")


class _FrCktAdminDestInsuredRate_Type(Integer32):
    """Custom type frCktAdminDestInsuredRate based on Integer32"""
    defaultValue = 0


_FrCktAdminDestInsuredRate_Object = MibTableColumn
frCktAdminDestInsuredRate = _FrCktAdminDestInsuredRate_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 8, 3, 1, 1, 33),
    _FrCktAdminDestInsuredRate_Type()
)
frCktAdminDestInsuredRate.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    frCktAdminDestInsuredRate.setStatus("mandatory")


class _FrCktOperDestInsuredRate_Type(Integer32):
    """Custom type frCktOperDestInsuredRate based on Integer32"""
    defaultValue = 0


_FrCktOperDestInsuredRate_Object = MibTableColumn
frCktOperDestInsuredRate = _FrCktOperDestInsuredRate_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 8, 3, 1, 1, 34),
    _FrCktOperDestInsuredRate_Type()
)
frCktOperDestInsuredRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frCktOperDestInsuredRate.setStatus("mandatory")


class _FrCktAdminDestInsuredBurst_Type(Integer32):
    """Custom type frCktAdminDestInsuredBurst based on Integer32"""
    defaultValue = 0


_FrCktAdminDestInsuredBurst_Object = MibTableColumn
frCktAdminDestInsuredBurst = _FrCktAdminDestInsuredBurst_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 8, 3, 1, 1, 35),
    _FrCktAdminDestInsuredBurst_Type()
)
frCktAdminDestInsuredBurst.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    frCktAdminDestInsuredBurst.setStatus("mandatory")


class _FrCktOperDestInsuredBurst_Type(Integer32):
    """Custom type frCktOperDestInsuredBurst based on Integer32"""
    defaultValue = 0


_FrCktOperDestInsuredBurst_Object = MibTableColumn
frCktOperDestInsuredBurst = _FrCktOperDestInsuredBurst_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 8, 3, 1, 1, 36),
    _FrCktOperDestInsuredBurst_Type()
)
frCktOperDestInsuredBurst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frCktOperDestInsuredBurst.setStatus("mandatory")


class _FrCktAdminDestMaxRate_Type(Integer32):
    """Custom type frCktAdminDestMaxRate based on Integer32"""
    defaultValue = 0


_FrCktAdminDestMaxRate_Object = MibTableColumn
frCktAdminDestMaxRate = _FrCktAdminDestMaxRate_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 8, 3, 1, 1, 37),
    _FrCktAdminDestMaxRate_Type()
)
frCktAdminDestMaxRate.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    frCktAdminDestMaxRate.setStatus("mandatory")


class _FrCktOperDestMaxRate_Type(Integer32):
    """Custom type frCktOperDestMaxRate based on Integer32"""
    defaultValue = 0


_FrCktOperDestMaxRate_Object = MibTableColumn
frCktOperDestMaxRate = _FrCktOperDestMaxRate_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 8, 3, 1, 1, 38),
    _FrCktOperDestMaxRate_Type()
)
frCktOperDestMaxRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frCktOperDestMaxRate.setStatus("mandatory")


class _FrCktAdminDestMaxBurst_Type(Integer32):
    """Custom type frCktAdminDestMaxBurst based on Integer32"""
    defaultValue = 0


_FrCktAdminDestMaxBurst_Object = MibTableColumn
frCktAdminDestMaxBurst = _FrCktAdminDestMaxBurst_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 8, 3, 1, 1, 39),
    _FrCktAdminDestMaxBurst_Type()
)
frCktAdminDestMaxBurst.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    frCktAdminDestMaxBurst.setStatus("mandatory")


class _FrCktOperDestMaxBurst_Type(Integer32):
    """Custom type frCktOperDestMaxBurst based on Integer32"""
    defaultValue = 0


_FrCktOperDestMaxBurst_Object = MibTableColumn
frCktOperDestMaxBurst = _FrCktOperDestMaxBurst_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 8, 3, 1, 1, 40),
    _FrCktOperDestMaxBurst_Type()
)
frCktOperDestMaxBurst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frCktOperDestMaxBurst.setStatus("mandatory")


class _FrCktOperSecondaryScale_Type(Integer32):
    """Custom type frCktOperSecondaryScale based on Integer32"""
    defaultValue = 255


_FrCktOperSecondaryScale_Object = MibTableColumn
frCktOperSecondaryScale = _FrCktOperSecondaryScale_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 8, 3, 1, 1, 41),
    _FrCktOperSecondaryScale_Type()
)
frCktOperSecondaryScale.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frCktOperSecondaryScale.setStatus("mandatory")


class _FrCktAdminSecondaryScale_Type(Integer32):
    """Custom type frCktAdminSecondaryScale based on Integer32"""
    defaultValue = 255


_FrCktAdminSecondaryScale_Object = MibTableColumn
frCktAdminSecondaryScale = _FrCktAdminSecondaryScale_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 8, 3, 1, 1, 42),
    _FrCktAdminSecondaryScale_Type()
)
frCktAdminSecondaryScale.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frCktAdminSecondaryScale.setStatus("mandatory")


class _FrCktOperPrinBwType_Type(Integer32):
    """Custom type frCktOperPrinBwType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("guaranteed", 1),
          ("insured", 2))
    )


_FrCktOperPrinBwType_Type.__name__ = "Integer32"
_FrCktOperPrinBwType_Object = MibTableColumn
frCktOperPrinBwType = _FrCktOperPrinBwType_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 8, 3, 1, 1, 43),
    _FrCktOperPrinBwType_Type()
)
frCktOperPrinBwType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frCktOperPrinBwType.setStatus("mandatory")


class _FrCktAdminPrinBwType_Type(Integer32):
    """Custom type frCktAdminPrinBwType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("guaranteed", 1),
          ("insured", 2))
    )


_FrCktAdminPrinBwType_Type.__name__ = "Integer32"
_FrCktAdminPrinBwType_Object = MibTableColumn
frCktAdminPrinBwType = _FrCktAdminPrinBwType_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 8, 3, 1, 1, 44),
    _FrCktAdminPrinBwType_Type()
)
frCktAdminPrinBwType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frCktAdminPrinBwType.setStatus("mandatory")


class _FrCktOperTransPri_Type(Integer32):
    """Custom type frCktOperTransPri based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_FrCktOperTransPri_Type.__name__ = "Integer32"
_FrCktOperTransPri_Object = MibTableColumn
frCktOperTransPri = _FrCktOperTransPri_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 8, 3, 1, 1, 45),
    _FrCktOperTransPri_Type()
)
frCktOperTransPri.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frCktOperTransPri.setStatus("mandatory")


class _FrCktAdminTransPri_Type(Integer32):
    """Custom type frCktAdminTransPri based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_FrCktAdminTransPri_Type.__name__ = "Integer32"
_FrCktAdminTransPri_Object = MibTableColumn
frCktAdminTransPri = _FrCktAdminTransPri_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 8, 3, 1, 1, 46),
    _FrCktAdminTransPri_Type()
)
frCktAdminTransPri.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frCktAdminTransPri.setStatus("mandatory")


class _FrCktOperUserDataPerCell_Type(Integer32):
    """Custom type frCktOperUserDataPerCell based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 384),
    )


_FrCktOperUserDataPerCell_Type.__name__ = "Integer32"
_FrCktOperUserDataPerCell_Object = MibTableColumn
frCktOperUserDataPerCell = _FrCktOperUserDataPerCell_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 8, 3, 1, 1, 47),
    _FrCktOperUserDataPerCell_Type()
)
frCktOperUserDataPerCell.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frCktOperUserDataPerCell.setStatus("mandatory")


class _FrCktAdminUserDataPerCell_Type(Integer32):
    """Custom type frCktAdminUserDataPerCell based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 384),
    )


_FrCktAdminUserDataPerCell_Type.__name__ = "Integer32"
_FrCktAdminUserDataPerCell_Object = MibTableColumn
frCktAdminUserDataPerCell = _FrCktAdminUserDataPerCell_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 8, 3, 1, 1, 48),
    _FrCktAdminUserDataPerCell_Type()
)
frCktAdminUserDataPerCell.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frCktAdminUserDataPerCell.setStatus("mandatory")


class _FrCktStatus_Type(Integer32):
    """Custom type frCktStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("delete", 3),
          ("disabled", 2),
          ("enabled", 1))
    )


_FrCktStatus_Type.__name__ = "Integer32"
_FrCktStatus_Object = MibTableColumn
frCktStatus = _FrCktStatus_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 8, 3, 1, 1, 99),
    _FrCktStatus_Type()
)
frCktStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frCktStatus.setStatus("mandatory")
_FrCktInfoTable_Object = MibTable
frCktInfoTable = _FrCktInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 8, 3, 2)
)
if mibBuilder.loadTexts:
    frCktInfoTable.setStatus("mandatory")
_FrCktInfoEntry_Object = MibTableRow
frCktInfoEntry = _FrCktInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 8, 3, 2, 1)
)
frCktInfoEntry.setIndexNames(
    (0, "LIGHTSTREAM-MIB", "frCktInfoIfIndex"),
    (0, "LIGHTSTREAM-MIB", "frCktInfoDlci"),
)
if mibBuilder.loadTexts:
    frCktInfoEntry.setStatus("mandatory")
_FrCktInfoIfIndex_Type = Integer32
_FrCktInfoIfIndex_Object = MibTableColumn
frCktInfoIfIndex = _FrCktInfoIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 8, 3, 2, 1, 1),
    _FrCktInfoIfIndex_Type()
)
frCktInfoIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frCktInfoIfIndex.setStatus("mandatory")
_FrCktInfoDlci_Type = LightStreamDLCI
_FrCktInfoDlci_Object = MibTableColumn
frCktInfoDlci = _FrCktInfoDlci_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 8, 3, 2, 1, 2),
    _FrCktInfoDlci_Type()
)
frCktInfoDlci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frCktInfoDlci.setStatus("mandatory")


class _FrCktInfoLclLMI_Type(Integer32):
    """Custom type frCktInfoLclLMI based on Integer32"""
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


_FrCktInfoLclLMI_Type.__name__ = "Integer32"
_FrCktInfoLclLMI_Object = MibTableColumn
frCktInfoLclLMI = _FrCktInfoLclLMI_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 8, 3, 2, 1, 3),
    _FrCktInfoLclLMI_Type()
)
frCktInfoLclLMI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frCktInfoLclLMI.setStatus("mandatory")


class _FrCktInfoRmtLMI_Type(Integer32):
    """Custom type frCktInfoRmtLMI based on Integer32"""
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


_FrCktInfoRmtLMI_Type.__name__ = "Integer32"
_FrCktInfoRmtLMI_Object = MibTableColumn
frCktInfoRmtLMI = _FrCktInfoRmtLMI_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 8, 3, 2, 1, 4),
    _FrCktInfoRmtLMI_Type()
)
frCktInfoRmtLMI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frCktInfoRmtLMI.setStatus("mandatory")
_FrCktInfoCallIDIncoming_Type = Integer32
_FrCktInfoCallIDIncoming_Object = MibTableColumn
frCktInfoCallIDIncoming = _FrCktInfoCallIDIncoming_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 8, 3, 2, 1, 5),
    _FrCktInfoCallIDIncoming_Type()
)
frCktInfoCallIDIncoming.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frCktInfoCallIDIncoming.setStatus("mandatory")
_FrCktInfoCallIDOutgoing_Type = Integer32
_FrCktInfoCallIDOutgoing_Object = MibTableColumn
frCktInfoCallIDOutgoing = _FrCktInfoCallIDOutgoing_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 8, 3, 2, 1, 6),
    _FrCktInfoCallIDOutgoing_Type()
)
frCktInfoCallIDOutgoing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frCktInfoCallIDOutgoing.setStatus("mandatory")


class _FrCktInfoDownstreamState_Type(Integer32):
    """Custom type frCktInfoDownstreamState based on Integer32"""
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


_FrCktInfoDownstreamState_Type.__name__ = "Integer32"
_FrCktInfoDownstreamState_Object = MibTableColumn
frCktInfoDownstreamState = _FrCktInfoDownstreamState_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 8, 3, 2, 1, 7),
    _FrCktInfoDownstreamState_Type()
)
frCktInfoDownstreamState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frCktInfoDownstreamState.setStatus("mandatory")


class _FrCktInfoUpstreamState_Type(Integer32):
    """Custom type frCktInfoUpstreamState based on Integer32"""
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


_FrCktInfoUpstreamState_Type.__name__ = "Integer32"
_FrCktInfoUpstreamState_Object = MibTableColumn
frCktInfoUpstreamState = _FrCktInfoUpstreamState_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 8, 3, 2, 1, 8),
    _FrCktInfoUpstreamState_Type()
)
frCktInfoUpstreamState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frCktInfoUpstreamState.setStatus("mandatory")
_FrCktInfoLastAtmErr_Type = OctetString
_FrCktInfoLastAtmErr_Object = MibTableColumn
frCktInfoLastAtmErr = _FrCktInfoLastAtmErr_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 8, 3, 2, 1, 9),
    _FrCktInfoLastAtmErr_Type()
)
frCktInfoLastAtmErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frCktInfoLastAtmErr.setStatus("mandatory")
_FrCktInfoDataCellsRequired_Type = Integer32
_FrCktInfoDataCellsRequired_Object = MibTableColumn
frCktInfoDataCellsRequired = _FrCktInfoDataCellsRequired_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 8, 3, 2, 1, 10),
    _FrCktInfoDataCellsRequired_Type()
)
frCktInfoDataCellsRequired.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frCktInfoDataCellsRequired.setStatus("mandatory")


class _FrCktInfoLastAtmLocation_Type(DisplayString):
    """Custom type frCktInfoLastAtmLocation based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_FrCktInfoLastAtmLocation_Type.__name__ = "DisplayString"
_FrCktInfoLastAtmLocation_Object = MibTableColumn
frCktInfoLastAtmLocation = _FrCktInfoLastAtmLocation_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 8, 3, 2, 1, 11),
    _FrCktInfoLastAtmLocation_Type()
)
frCktInfoLastAtmLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frCktInfoLastAtmLocation.setStatus("mandatory")
_FfCktInfo_ObjectIdentity = ObjectIdentity
ffCktInfo = _FfCktInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 8, 4)
)
_FfCktCfgTable_Object = MibTable
ffCktCfgTable = _FfCktCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 8, 4, 1)
)
if mibBuilder.loadTexts:
    ffCktCfgTable.setStatus("mandatory")
_FfCktEntry_Object = MibTableRow
ffCktEntry = _FfCktEntry_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 8, 4, 1, 1)
)
ffCktEntry.setIndexNames(
    (0, "LIGHTSTREAM-MIB", "ffCktSrcIfIndex"),
)
if mibBuilder.loadTexts:
    ffCktEntry.setStatus("mandatory")
_FfCktSrcNode_Type = Integer32
_FfCktSrcNode_Object = MibTableColumn
ffCktSrcNode = _FfCktSrcNode_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 8, 4, 1, 1, 1),
    _FfCktSrcNode_Type()
)
ffCktSrcNode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ffCktSrcNode.setStatus("mandatory")
_FfCktSrcIfIndex_Type = Integer32
_FfCktSrcIfIndex_Object = MibTableColumn
ffCktSrcIfIndex = _FfCktSrcIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 8, 4, 1, 1, 2),
    _FfCktSrcIfIndex_Type()
)
ffCktSrcIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ffCktSrcIfIndex.setStatus("mandatory")
_FfCktAdminDestNode_Type = Integer32
_FfCktAdminDestNode_Object = MibTableColumn
ffCktAdminDestNode = _FfCktAdminDestNode_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 8, 4, 1, 1, 9),
    _FfCktAdminDestNode_Type()
)
ffCktAdminDestNode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ffCktAdminDestNode.setStatus("mandatory")
_FfCktOperDestNode_Type = Integer32
_FfCktOperDestNode_Object = MibTableColumn
ffCktOperDestNode = _FfCktOperDestNode_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 8, 4, 1, 1, 10),
    _FfCktOperDestNode_Type()
)
ffCktOperDestNode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ffCktOperDestNode.setStatus("mandatory")
_FfCktAdminDestIfIndex_Type = Integer32
_FfCktAdminDestIfIndex_Object = MibTableColumn
ffCktAdminDestIfIndex = _FfCktAdminDestIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 8, 4, 1, 1, 11),
    _FfCktAdminDestIfIndex_Type()
)
ffCktAdminDestIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ffCktAdminDestIfIndex.setStatus("mandatory")
_FfCktOperDestIfIndex_Type = Integer32
_FfCktOperDestIfIndex_Object = MibTableColumn
ffCktOperDestIfIndex = _FfCktOperDestIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 8, 4, 1, 1, 12),
    _FfCktOperDestIfIndex_Type()
)
ffCktOperDestIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ffCktOperDestIfIndex.setStatus("mandatory")


class _FfCktAdminSrcInsuredRate_Type(Integer32):
    """Custom type ffCktAdminSrcInsuredRate based on Integer32"""
    defaultValue = 0


_FfCktAdminSrcInsuredRate_Object = MibTableColumn
ffCktAdminSrcInsuredRate = _FfCktAdminSrcInsuredRate_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 8, 4, 1, 1, 21),
    _FfCktAdminSrcInsuredRate_Type()
)
ffCktAdminSrcInsuredRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ffCktAdminSrcInsuredRate.setStatus("mandatory")


class _FfCktOperSrcInsuredRate_Type(Integer32):
    """Custom type ffCktOperSrcInsuredRate based on Integer32"""
    defaultValue = -11


_FfCktOperSrcInsuredRate_Object = MibTableColumn
ffCktOperSrcInsuredRate = _FfCktOperSrcInsuredRate_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 8, 4, 1, 1, 22),
    _FfCktOperSrcInsuredRate_Type()
)
ffCktOperSrcInsuredRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ffCktOperSrcInsuredRate.setStatus("mandatory")


class _FfCktAdminSrcInsuredBurst_Type(Integer32):
    """Custom type ffCktAdminSrcInsuredBurst based on Integer32"""
    defaultValue = -1


_FfCktAdminSrcInsuredBurst_Object = MibTableColumn
ffCktAdminSrcInsuredBurst = _FfCktAdminSrcInsuredBurst_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 8, 4, 1, 1, 23),
    _FfCktAdminSrcInsuredBurst_Type()
)
ffCktAdminSrcInsuredBurst.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ffCktAdminSrcInsuredBurst.setStatus("mandatory")


class _FfCktOperSrcInsuredBurst_Type(Integer32):
    """Custom type ffCktOperSrcInsuredBurst based on Integer32"""
    defaultValue = -1


_FfCktOperSrcInsuredBurst_Object = MibTableColumn
ffCktOperSrcInsuredBurst = _FfCktOperSrcInsuredBurst_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 8, 4, 1, 1, 24),
    _FfCktOperSrcInsuredBurst_Type()
)
ffCktOperSrcInsuredBurst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ffCktOperSrcInsuredBurst.setStatus("mandatory")


class _FfCktAdminSrcMaxRate_Type(Integer32):
    """Custom type ffCktAdminSrcMaxRate based on Integer32"""
    defaultValue = -1


_FfCktAdminSrcMaxRate_Object = MibTableColumn
ffCktAdminSrcMaxRate = _FfCktAdminSrcMaxRate_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 8, 4, 1, 1, 25),
    _FfCktAdminSrcMaxRate_Type()
)
ffCktAdminSrcMaxRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ffCktAdminSrcMaxRate.setStatus("mandatory")


class _FfCktOperSrcMaxRate_Type(Integer32):
    """Custom type ffCktOperSrcMaxRate based on Integer32"""
    defaultValue = -1


_FfCktOperSrcMaxRate_Object = MibTableColumn
ffCktOperSrcMaxRate = _FfCktOperSrcMaxRate_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 8, 4, 1, 1, 26),
    _FfCktOperSrcMaxRate_Type()
)
ffCktOperSrcMaxRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ffCktOperSrcMaxRate.setStatus("mandatory")


class _FfCktAdminSrcMaxBurst_Type(Integer32):
    """Custom type ffCktAdminSrcMaxBurst based on Integer32"""
    defaultValue = -1


_FfCktAdminSrcMaxBurst_Object = MibTableColumn
ffCktAdminSrcMaxBurst = _FfCktAdminSrcMaxBurst_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 8, 4, 1, 1, 27),
    _FfCktAdminSrcMaxBurst_Type()
)
ffCktAdminSrcMaxBurst.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ffCktAdminSrcMaxBurst.setStatus("mandatory")


class _FfCktOperSrcMaxBurst_Type(Integer32):
    """Custom type ffCktOperSrcMaxBurst based on Integer32"""
    defaultValue = -1


_FfCktOperSrcMaxBurst_Object = MibTableColumn
ffCktOperSrcMaxBurst = _FfCktOperSrcMaxBurst_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 8, 4, 1, 1, 28),
    _FfCktOperSrcMaxBurst_Type()
)
ffCktOperSrcMaxBurst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ffCktOperSrcMaxBurst.setStatus("mandatory")


class _FfCktAdminDestInsuredRate_Type(Integer32):
    """Custom type ffCktAdminDestInsuredRate based on Integer32"""
    defaultValue = -1


_FfCktAdminDestInsuredRate_Object = MibTableColumn
ffCktAdminDestInsuredRate = _FfCktAdminDestInsuredRate_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 8, 4, 1, 1, 29),
    _FfCktAdminDestInsuredRate_Type()
)
ffCktAdminDestInsuredRate.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ffCktAdminDestInsuredRate.setStatus("mandatory")


class _FfCktOperDestInsuredRate_Type(Integer32):
    """Custom type ffCktOperDestInsuredRate based on Integer32"""
    defaultValue = -1


_FfCktOperDestInsuredRate_Object = MibTableColumn
ffCktOperDestInsuredRate = _FfCktOperDestInsuredRate_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 8, 4, 1, 1, 30),
    _FfCktOperDestInsuredRate_Type()
)
ffCktOperDestInsuredRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ffCktOperDestInsuredRate.setStatus("mandatory")


class _FfCktAdminDestInsuredBurst_Type(Integer32):
    """Custom type ffCktAdminDestInsuredBurst based on Integer32"""
    defaultValue = -1


_FfCktAdminDestInsuredBurst_Object = MibTableColumn
ffCktAdminDestInsuredBurst = _FfCktAdminDestInsuredBurst_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 8, 4, 1, 1, 31),
    _FfCktAdminDestInsuredBurst_Type()
)
ffCktAdminDestInsuredBurst.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ffCktAdminDestInsuredBurst.setStatus("mandatory")


class _FfCktOperDestInsuredBurst_Type(Integer32):
    """Custom type ffCktOperDestInsuredBurst based on Integer32"""
    defaultValue = -1


_FfCktOperDestInsuredBurst_Object = MibTableColumn
ffCktOperDestInsuredBurst = _FfCktOperDestInsuredBurst_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 8, 4, 1, 1, 32),
    _FfCktOperDestInsuredBurst_Type()
)
ffCktOperDestInsuredBurst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ffCktOperDestInsuredBurst.setStatus("mandatory")


class _FfCktAdminDestMaxRate_Type(Integer32):
    """Custom type ffCktAdminDestMaxRate based on Integer32"""
    defaultValue = -1


_FfCktAdminDestMaxRate_Object = MibTableColumn
ffCktAdminDestMaxRate = _FfCktAdminDestMaxRate_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 8, 4, 1, 1, 33),
    _FfCktAdminDestMaxRate_Type()
)
ffCktAdminDestMaxRate.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ffCktAdminDestMaxRate.setStatus("mandatory")


class _FfCktOperDestMaxRate_Type(Integer32):
    """Custom type ffCktOperDestMaxRate based on Integer32"""
    defaultValue = -1


_FfCktOperDestMaxRate_Object = MibTableColumn
ffCktOperDestMaxRate = _FfCktOperDestMaxRate_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 8, 4, 1, 1, 34),
    _FfCktOperDestMaxRate_Type()
)
ffCktOperDestMaxRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ffCktOperDestMaxRate.setStatus("mandatory")


class _FfCktAdminDestMaxBurst_Type(Integer32):
    """Custom type ffCktAdminDestMaxBurst based on Integer32"""
    defaultValue = -1


_FfCktAdminDestMaxBurst_Object = MibTableColumn
ffCktAdminDestMaxBurst = _FfCktAdminDestMaxBurst_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 8, 4, 1, 1, 35),
    _FfCktAdminDestMaxBurst_Type()
)
ffCktAdminDestMaxBurst.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ffCktAdminDestMaxBurst.setStatus("mandatory")


class _FfCktOperDestMaxBurst_Type(Integer32):
    """Custom type ffCktOperDestMaxBurst based on Integer32"""
    defaultValue = -1


_FfCktOperDestMaxBurst_Object = MibTableColumn
ffCktOperDestMaxBurst = _FfCktOperDestMaxBurst_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 8, 4, 1, 1, 36),
    _FfCktOperDestMaxBurst_Type()
)
ffCktOperDestMaxBurst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ffCktOperDestMaxBurst.setStatus("mandatory")


class _FfCktOperPrinBwType_Type(Integer32):
    """Custom type ffCktOperPrinBwType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("guaranteed", 1),
          ("insured", 2))
    )


_FfCktOperPrinBwType_Type.__name__ = "Integer32"
_FfCktOperPrinBwType_Object = MibTableColumn
ffCktOperPrinBwType = _FfCktOperPrinBwType_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 8, 4, 1, 1, 37),
    _FfCktOperPrinBwType_Type()
)
ffCktOperPrinBwType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ffCktOperPrinBwType.setStatus("mandatory")


class _FfCktAdminPrinBwType_Type(Integer32):
    """Custom type ffCktAdminPrinBwType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("guaranteed", 1),
          ("insured", 2))
    )


_FfCktAdminPrinBwType_Type.__name__ = "Integer32"
_FfCktAdminPrinBwType_Object = MibTableColumn
ffCktAdminPrinBwType = _FfCktAdminPrinBwType_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 8, 4, 1, 1, 38),
    _FfCktAdminPrinBwType_Type()
)
ffCktAdminPrinBwType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ffCktAdminPrinBwType.setStatus("mandatory")


class _FfCktOperTransPri_Type(Integer32):
    """Custom type ffCktOperTransPri based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_FfCktOperTransPri_Type.__name__ = "Integer32"
_FfCktOperTransPri_Object = MibTableColumn
ffCktOperTransPri = _FfCktOperTransPri_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 8, 4, 1, 1, 39),
    _FfCktOperTransPri_Type()
)
ffCktOperTransPri.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ffCktOperTransPri.setStatus("mandatory")


class _FfCktAdminTransPri_Type(Integer32):
    """Custom type ffCktAdminTransPri based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_FfCktAdminTransPri_Type.__name__ = "Integer32"
_FfCktAdminTransPri_Object = MibTableColumn
ffCktAdminTransPri = _FfCktAdminTransPri_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 8, 4, 1, 1, 40),
    _FfCktAdminTransPri_Type()
)
ffCktAdminTransPri.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ffCktAdminTransPri.setStatus("mandatory")


class _FfCktStatus_Type(Integer32):
    """Custom type ffCktStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("delete", 3),
          ("disabled", 2),
          ("enabled", 1))
    )


_FfCktStatus_Type.__name__ = "Integer32"
_FfCktStatus_Object = MibTableColumn
ffCktStatus = _FfCktStatus_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 8, 4, 1, 1, 99),
    _FfCktStatus_Type()
)
ffCktStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ffCktStatus.setStatus("mandatory")
_FfCktInfoTable_Object = MibTable
ffCktInfoTable = _FfCktInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 8, 4, 2)
)
if mibBuilder.loadTexts:
    ffCktInfoTable.setStatus("mandatory")
_FfCktInfoEntry_Object = MibTableRow
ffCktInfoEntry = _FfCktInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 8, 4, 2, 1)
)
ffCktInfoEntry.setIndexNames(
    (0, "LIGHTSTREAM-MIB", "ffCktInfoIfIndex"),
)
if mibBuilder.loadTexts:
    ffCktInfoEntry.setStatus("mandatory")
_FfCktInfoIfIndex_Type = Integer32
_FfCktInfoIfIndex_Object = MibTableColumn
ffCktInfoIfIndex = _FfCktInfoIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 8, 4, 2, 1, 1),
    _FfCktInfoIfIndex_Type()
)
ffCktInfoIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ffCktInfoIfIndex.setStatus("mandatory")


class _FfCktInfoDownstreamState_Type(Integer32):
    """Custom type ffCktInfoDownstreamState based on Integer32"""
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


_FfCktInfoDownstreamState_Type.__name__ = "Integer32"
_FfCktInfoDownstreamState_Object = MibTableColumn
ffCktInfoDownstreamState = _FfCktInfoDownstreamState_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 8, 4, 2, 1, 2),
    _FfCktInfoDownstreamState_Type()
)
ffCktInfoDownstreamState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ffCktInfoDownstreamState.setStatus("mandatory")


class _FfCktInfoUpstreamState_Type(Integer32):
    """Custom type ffCktInfoUpstreamState based on Integer32"""
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


_FfCktInfoUpstreamState_Type.__name__ = "Integer32"
_FfCktInfoUpstreamState_Object = MibTableColumn
ffCktInfoUpstreamState = _FfCktInfoUpstreamState_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 8, 4, 2, 1, 3),
    _FfCktInfoUpstreamState_Type()
)
ffCktInfoUpstreamState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ffCktInfoUpstreamState.setStatus("mandatory")
_FfCktInfoCallIDIncoming_Type = Integer32
_FfCktInfoCallIDIncoming_Object = MibTableColumn
ffCktInfoCallIDIncoming = _FfCktInfoCallIDIncoming_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 8, 4, 2, 1, 4),
    _FfCktInfoCallIDIncoming_Type()
)
ffCktInfoCallIDIncoming.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ffCktInfoCallIDIncoming.setStatus("mandatory")
_FfCktInfoCallIDOutgoing_Type = Integer32
_FfCktInfoCallIDOutgoing_Object = MibTableColumn
ffCktInfoCallIDOutgoing = _FfCktInfoCallIDOutgoing_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 8, 4, 2, 1, 5),
    _FfCktInfoCallIDOutgoing_Type()
)
ffCktInfoCallIDOutgoing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ffCktInfoCallIDOutgoing.setStatus("mandatory")
_FfCktInfoLastAtmErr_Type = OctetString
_FfCktInfoLastAtmErr_Object = MibTableColumn
ffCktInfoLastAtmErr = _FfCktInfoLastAtmErr_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 8, 4, 2, 1, 6),
    _FfCktInfoLastAtmErr_Type()
)
ffCktInfoLastAtmErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ffCktInfoLastAtmErr.setStatus("mandatory")
_FfCktInfoDataCellsRequired_Type = Integer32
_FfCktInfoDataCellsRequired_Object = MibTableColumn
ffCktInfoDataCellsRequired = _FfCktInfoDataCellsRequired_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 8, 4, 2, 1, 7),
    _FfCktInfoDataCellsRequired_Type()
)
ffCktInfoDataCellsRequired.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ffCktInfoDataCellsRequired.setStatus("mandatory")


class _FfCktInfoLastAtmLocation_Type(DisplayString):
    """Custom type ffCktInfoLastAtmLocation based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_FfCktInfoLastAtmLocation_Type.__name__ = "DisplayString"
_FfCktInfoLastAtmLocation_Object = MibTableColumn
ffCktInfoLastAtmLocation = _FfCktInfoLastAtmLocation_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 8, 4, 2, 1, 8),
    _FfCktInfoLastAtmLocation_Type()
)
ffCktInfoLastAtmLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ffCktInfoLastAtmLocation.setStatus("mandatory")
_SUniCktInfo_ObjectIdentity = ObjectIdentity
sUniCktInfo = _SUniCktInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 8, 5)
)
_SUniCktCfgTable_Object = MibTable
sUniCktCfgTable = _SUniCktCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 8, 5, 1)
)
if mibBuilder.loadTexts:
    sUniCktCfgTable.setStatus("mandatory")
_SUniCktEntry_Object = MibTableRow
sUniCktEntry = _SUniCktEntry_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 8, 5, 1, 1)
)
sUniCktEntry.setIndexNames(
    (0, "LIGHTSTREAM-MIB", "sUniCktSrcIfIndex"),
    (0, "LIGHTSTREAM-MIB", "sUniCktSrcVCI"),
)
if mibBuilder.loadTexts:
    sUniCktEntry.setStatus("mandatory")
_SUniCktSrcNode_Type = Integer32
_SUniCktSrcNode_Object = MibTableColumn
sUniCktSrcNode = _SUniCktSrcNode_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 8, 5, 1, 1, 1),
    _SUniCktSrcNode_Type()
)
sUniCktSrcNode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sUniCktSrcNode.setStatus("mandatory")
_SUniCktSrcIfIndex_Type = Integer32
_SUniCktSrcIfIndex_Object = MibTableColumn
sUniCktSrcIfIndex = _SUniCktSrcIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 8, 5, 1, 1, 2),
    _SUniCktSrcIfIndex_Type()
)
sUniCktSrcIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sUniCktSrcIfIndex.setStatus("mandatory")
_SUniCktSrcVCI_Type = VCI
_SUniCktSrcVCI_Object = MibTableColumn
sUniCktSrcVCI = _SUniCktSrcVCI_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 8, 5, 1, 1, 3),
    _SUniCktSrcVCI_Type()
)
sUniCktSrcVCI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sUniCktSrcVCI.setStatus("mandatory")
_SUniCktAdminDestNode_Type = Integer32
_SUniCktAdminDestNode_Object = MibTableColumn
sUniCktAdminDestNode = _SUniCktAdminDestNode_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 8, 5, 1, 1, 10),
    _SUniCktAdminDestNode_Type()
)
sUniCktAdminDestNode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sUniCktAdminDestNode.setStatus("mandatory")
_SUniCktOperDestNode_Type = Integer32
_SUniCktOperDestNode_Object = MibTableColumn
sUniCktOperDestNode = _SUniCktOperDestNode_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 8, 5, 1, 1, 11),
    _SUniCktOperDestNode_Type()
)
sUniCktOperDestNode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sUniCktOperDestNode.setStatus("mandatory")
_SUniCktAdminDestIfIndex_Type = Integer32
_SUniCktAdminDestIfIndex_Object = MibTableColumn
sUniCktAdminDestIfIndex = _SUniCktAdminDestIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 8, 5, 1, 1, 12),
    _SUniCktAdminDestIfIndex_Type()
)
sUniCktAdminDestIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sUniCktAdminDestIfIndex.setStatus("mandatory")
_SUniCktOperDestIfIndex_Type = Integer32
_SUniCktOperDestIfIndex_Object = MibTableColumn
sUniCktOperDestIfIndex = _SUniCktOperDestIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 8, 5, 1, 1, 13),
    _SUniCktOperDestIfIndex_Type()
)
sUniCktOperDestIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sUniCktOperDestIfIndex.setStatus("mandatory")
_SUniCktAdminDestVCI_Type = VCI
_SUniCktAdminDestVCI_Object = MibTableColumn
sUniCktAdminDestVCI = _SUniCktAdminDestVCI_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 8, 5, 1, 1, 14),
    _SUniCktAdminDestVCI_Type()
)
sUniCktAdminDestVCI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sUniCktAdminDestVCI.setStatus("mandatory")
_SUniCktOperDestVCI_Type = VCI
_SUniCktOperDestVCI_Object = MibTableColumn
sUniCktOperDestVCI = _SUniCktOperDestVCI_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 8, 5, 1, 1, 15),
    _SUniCktOperDestVCI_Type()
)
sUniCktOperDestVCI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sUniCktOperDestVCI.setStatus("mandatory")


class _SUniCktOperPrinBwType_Type(Integer32):
    """Custom type sUniCktOperPrinBwType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("guaranteed", 1),
          ("insured", 2))
    )


_SUniCktOperPrinBwType_Type.__name__ = "Integer32"
_SUniCktOperPrinBwType_Object = MibTableColumn
sUniCktOperPrinBwType = _SUniCktOperPrinBwType_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 8, 5, 1, 1, 22),
    _SUniCktOperPrinBwType_Type()
)
sUniCktOperPrinBwType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sUniCktOperPrinBwType.setStatus("mandatory")


class _SUniCktAdminPrinBwType_Type(Integer32):
    """Custom type sUniCktAdminPrinBwType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("guaranteed", 1),
          ("insured", 2))
    )


_SUniCktAdminPrinBwType_Type.__name__ = "Integer32"
_SUniCktAdminPrinBwType_Object = MibTableColumn
sUniCktAdminPrinBwType = _SUniCktAdminPrinBwType_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 8, 5, 1, 1, 23),
    _SUniCktAdminPrinBwType_Type()
)
sUniCktAdminPrinBwType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sUniCktAdminPrinBwType.setStatus("mandatory")


class _SUniCktOperTransPri_Type(Integer32):
    """Custom type sUniCktOperTransPri based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_SUniCktOperTransPri_Type.__name__ = "Integer32"
_SUniCktOperTransPri_Object = MibTableColumn
sUniCktOperTransPri = _SUniCktOperTransPri_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 8, 5, 1, 1, 24),
    _SUniCktOperTransPri_Type()
)
sUniCktOperTransPri.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sUniCktOperTransPri.setStatus("mandatory")


class _SUniCktAdminTransPri_Type(Integer32):
    """Custom type sUniCktAdminTransPri based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_SUniCktAdminTransPri_Type.__name__ = "Integer32"
_SUniCktAdminTransPri_Object = MibTableColumn
sUniCktAdminTransPri = _SUniCktAdminTransPri_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 8, 5, 1, 1, 25),
    _SUniCktAdminTransPri_Type()
)
sUniCktAdminTransPri.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sUniCktAdminTransPri.setStatus("mandatory")


class _SUniCktAdminSrcInsuredRate_Type(Integer32):
    """Custom type sUniCktAdminSrcInsuredRate based on Integer32"""
    defaultValue = 0


_SUniCktAdminSrcInsuredRate_Object = MibTableColumn
sUniCktAdminSrcInsuredRate = _SUniCktAdminSrcInsuredRate_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 8, 5, 1, 1, 26),
    _SUniCktAdminSrcInsuredRate_Type()
)
sUniCktAdminSrcInsuredRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sUniCktAdminSrcInsuredRate.setStatus("mandatory")


class _SUniCktOperSrcInsuredRate_Type(Integer32):
    """Custom type sUniCktOperSrcInsuredRate based on Integer32"""
    defaultValue = 0


_SUniCktOperSrcInsuredRate_Object = MibTableColumn
sUniCktOperSrcInsuredRate = _SUniCktOperSrcInsuredRate_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 8, 5, 1, 1, 27),
    _SUniCktOperSrcInsuredRate_Type()
)
sUniCktOperSrcInsuredRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sUniCktOperSrcInsuredRate.setStatus("mandatory")


class _SUniCktAdminSrcInsuredBurst_Type(Integer32):
    """Custom type sUniCktAdminSrcInsuredBurst based on Integer32"""
    defaultValue = 0


_SUniCktAdminSrcInsuredBurst_Object = MibTableColumn
sUniCktAdminSrcInsuredBurst = _SUniCktAdminSrcInsuredBurst_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 8, 5, 1, 1, 28),
    _SUniCktAdminSrcInsuredBurst_Type()
)
sUniCktAdminSrcInsuredBurst.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sUniCktAdminSrcInsuredBurst.setStatus("mandatory")


class _SUniCktOperSrcInsuredBurst_Type(Integer32):
    """Custom type sUniCktOperSrcInsuredBurst based on Integer32"""
    defaultValue = 0


_SUniCktOperSrcInsuredBurst_Object = MibTableColumn
sUniCktOperSrcInsuredBurst = _SUniCktOperSrcInsuredBurst_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 8, 5, 1, 1, 29),
    _SUniCktOperSrcInsuredBurst_Type()
)
sUniCktOperSrcInsuredBurst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sUniCktOperSrcInsuredBurst.setStatus("mandatory")


class _SUniCktAdminSrcMaxRate_Type(Integer32):
    """Custom type sUniCktAdminSrcMaxRate based on Integer32"""
    defaultValue = 0


_SUniCktAdminSrcMaxRate_Object = MibTableColumn
sUniCktAdminSrcMaxRate = _SUniCktAdminSrcMaxRate_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 8, 5, 1, 1, 30),
    _SUniCktAdminSrcMaxRate_Type()
)
sUniCktAdminSrcMaxRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sUniCktAdminSrcMaxRate.setStatus("mandatory")


class _SUniCktOperSrcMaxRate_Type(Integer32):
    """Custom type sUniCktOperSrcMaxRate based on Integer32"""
    defaultValue = 0


_SUniCktOperSrcMaxRate_Object = MibTableColumn
sUniCktOperSrcMaxRate = _SUniCktOperSrcMaxRate_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 8, 5, 1, 1, 31),
    _SUniCktOperSrcMaxRate_Type()
)
sUniCktOperSrcMaxRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sUniCktOperSrcMaxRate.setStatus("mandatory")


class _SUniCktAdminSrcMaxBurst_Type(Integer32):
    """Custom type sUniCktAdminSrcMaxBurst based on Integer32"""
    defaultValue = 0


_SUniCktAdminSrcMaxBurst_Object = MibTableColumn
sUniCktAdminSrcMaxBurst = _SUniCktAdminSrcMaxBurst_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 8, 5, 1, 1, 32),
    _SUniCktAdminSrcMaxBurst_Type()
)
sUniCktAdminSrcMaxBurst.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sUniCktAdminSrcMaxBurst.setStatus("mandatory")


class _SUniCktOperSrcMaxBurst_Type(Integer32):
    """Custom type sUniCktOperSrcMaxBurst based on Integer32"""
    defaultValue = 0


_SUniCktOperSrcMaxBurst_Object = MibTableColumn
sUniCktOperSrcMaxBurst = _SUniCktOperSrcMaxBurst_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 8, 5, 1, 1, 33),
    _SUniCktOperSrcMaxBurst_Type()
)
sUniCktOperSrcMaxBurst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sUniCktOperSrcMaxBurst.setStatus("mandatory")


class _SUniCktAdminDestInsuredRate_Type(Integer32):
    """Custom type sUniCktAdminDestInsuredRate based on Integer32"""
    defaultValue = 0


_SUniCktAdminDestInsuredRate_Object = MibTableColumn
sUniCktAdminDestInsuredRate = _SUniCktAdminDestInsuredRate_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 8, 5, 1, 1, 34),
    _SUniCktAdminDestInsuredRate_Type()
)
sUniCktAdminDestInsuredRate.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sUniCktAdminDestInsuredRate.setStatus("mandatory")


class _SUniCktOperDestInsuredRate_Type(Integer32):
    """Custom type sUniCktOperDestInsuredRate based on Integer32"""
    defaultValue = 0


_SUniCktOperDestInsuredRate_Object = MibTableColumn
sUniCktOperDestInsuredRate = _SUniCktOperDestInsuredRate_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 8, 5, 1, 1, 35),
    _SUniCktOperDestInsuredRate_Type()
)
sUniCktOperDestInsuredRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sUniCktOperDestInsuredRate.setStatus("mandatory")


class _SUniCktAdminDestInsuredBurst_Type(Integer32):
    """Custom type sUniCktAdminDestInsuredBurst based on Integer32"""
    defaultValue = 0


_SUniCktAdminDestInsuredBurst_Object = MibTableColumn
sUniCktAdminDestInsuredBurst = _SUniCktAdminDestInsuredBurst_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 8, 5, 1, 1, 36),
    _SUniCktAdminDestInsuredBurst_Type()
)
sUniCktAdminDestInsuredBurst.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sUniCktAdminDestInsuredBurst.setStatus("mandatory")


class _SUniCktOperDestInsuredBurst_Type(Integer32):
    """Custom type sUniCktOperDestInsuredBurst based on Integer32"""
    defaultValue = 0


_SUniCktOperDestInsuredBurst_Object = MibTableColumn
sUniCktOperDestInsuredBurst = _SUniCktOperDestInsuredBurst_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 8, 5, 1, 1, 37),
    _SUniCktOperDestInsuredBurst_Type()
)
sUniCktOperDestInsuredBurst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sUniCktOperDestInsuredBurst.setStatus("mandatory")


class _SUniCktAdminDestMaxRate_Type(Integer32):
    """Custom type sUniCktAdminDestMaxRate based on Integer32"""
    defaultValue = 0


_SUniCktAdminDestMaxRate_Object = MibTableColumn
sUniCktAdminDestMaxRate = _SUniCktAdminDestMaxRate_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 8, 5, 1, 1, 38),
    _SUniCktAdminDestMaxRate_Type()
)
sUniCktAdminDestMaxRate.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sUniCktAdminDestMaxRate.setStatus("mandatory")


class _SUniCktOperDestMaxRate_Type(Integer32):
    """Custom type sUniCktOperDestMaxRate based on Integer32"""
    defaultValue = 0


_SUniCktOperDestMaxRate_Object = MibTableColumn
sUniCktOperDestMaxRate = _SUniCktOperDestMaxRate_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 8, 5, 1, 1, 39),
    _SUniCktOperDestMaxRate_Type()
)
sUniCktOperDestMaxRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sUniCktOperDestMaxRate.setStatus("mandatory")


class _SUniCktAdminDestMaxBurst_Type(Integer32):
    """Custom type sUniCktAdminDestMaxBurst based on Integer32"""
    defaultValue = 0


_SUniCktAdminDestMaxBurst_Object = MibTableColumn
sUniCktAdminDestMaxBurst = _SUniCktAdminDestMaxBurst_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 8, 5, 1, 1, 40),
    _SUniCktAdminDestMaxBurst_Type()
)
sUniCktAdminDestMaxBurst.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sUniCktAdminDestMaxBurst.setStatus("mandatory")


class _SUniCktOperDestMaxBurst_Type(Integer32):
    """Custom type sUniCktOperDestMaxBurst based on Integer32"""
    defaultValue = 0


_SUniCktOperDestMaxBurst_Object = MibTableColumn
sUniCktOperDestMaxBurst = _SUniCktOperDestMaxBurst_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 8, 5, 1, 1, 41),
    _SUniCktOperDestMaxBurst_Type()
)
sUniCktOperDestMaxBurst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sUniCktOperDestMaxBurst.setStatus("mandatory")


class _SUniCktAdminSecondaryScale_Type(Integer32):
    """Custom type sUniCktAdminSecondaryScale based on Integer32"""
    defaultValue = 255


_SUniCktAdminSecondaryScale_Object = MibTableColumn
sUniCktAdminSecondaryScale = _SUniCktAdminSecondaryScale_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 8, 5, 1, 1, 42),
    _SUniCktAdminSecondaryScale_Type()
)
sUniCktAdminSecondaryScale.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sUniCktAdminSecondaryScale.setStatus("mandatory")


class _SUniCktOperSecondaryScale_Type(Integer32):
    """Custom type sUniCktOperSecondaryScale based on Integer32"""
    defaultValue = 255


_SUniCktOperSecondaryScale_Object = MibTableColumn
sUniCktOperSecondaryScale = _SUniCktOperSecondaryScale_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 8, 5, 1, 1, 43),
    _SUniCktOperSecondaryScale_Type()
)
sUniCktOperSecondaryScale.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sUniCktOperSecondaryScale.setStatus("mandatory")


class _SUniCktSts_Type(Integer32):
    """Custom type sUniCktSts based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("delete", 3),
          ("disabled", 2),
          ("enabled", 1))
    )


_SUniCktSts_Type.__name__ = "Integer32"
_SUniCktSts_Object = MibTableColumn
sUniCktSts = _SUniCktSts_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 8, 5, 1, 1, 99),
    _SUniCktSts_Type()
)
sUniCktSts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sUniCktSts.setStatus("mandatory")
_SUniCktInfoTable_Object = MibTable
sUniCktInfoTable = _SUniCktInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 8, 5, 2)
)
if mibBuilder.loadTexts:
    sUniCktInfoTable.setStatus("mandatory")
_SUniCktInfoEntry_Object = MibTableRow
sUniCktInfoEntry = _SUniCktInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 8, 5, 2, 1)
)
sUniCktInfoEntry.setIndexNames(
    (0, "LIGHTSTREAM-MIB", "sUniCktInfoIfIndex"),
    (0, "LIGHTSTREAM-MIB", "sUniCktInfoVCI"),
)
if mibBuilder.loadTexts:
    sUniCktInfoEntry.setStatus("mandatory")
_SUniCktInfoIfIndex_Type = Integer32
_SUniCktInfoIfIndex_Object = MibTableColumn
sUniCktInfoIfIndex = _SUniCktInfoIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 8, 5, 2, 1, 1),
    _SUniCktInfoIfIndex_Type()
)
sUniCktInfoIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sUniCktInfoIfIndex.setStatus("mandatory")
_SUniCktInfoVCI_Type = VCI
_SUniCktInfoVCI_Object = MibTableColumn
sUniCktInfoVCI = _SUniCktInfoVCI_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 8, 5, 2, 1, 2),
    _SUniCktInfoVCI_Type()
)
sUniCktInfoVCI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sUniCktInfoVCI.setStatus("mandatory")
_SUniCktInfoUniToNetCallID_Type = Integer32
_SUniCktInfoUniToNetCallID_Object = MibTableColumn
sUniCktInfoUniToNetCallID = _SUniCktInfoUniToNetCallID_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 8, 5, 2, 1, 3),
    _SUniCktInfoUniToNetCallID_Type()
)
sUniCktInfoUniToNetCallID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sUniCktInfoUniToNetCallID.setStatus("mandatory")
_SUniCktInfoNetToUniCallID_Type = Integer32
_SUniCktInfoNetToUniCallID_Object = MibTableColumn
sUniCktInfoNetToUniCallID = _SUniCktInfoNetToUniCallID_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 8, 5, 2, 1, 4),
    _SUniCktInfoNetToUniCallID_Type()
)
sUniCktInfoNetToUniCallID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sUniCktInfoNetToUniCallID.setStatus("mandatory")


class _SUniCktInfoUniToNetState_Type(Integer32):
    """Custom type sUniCktInfoUniToNetState based on Integer32"""
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


_SUniCktInfoUniToNetState_Type.__name__ = "Integer32"
_SUniCktInfoUniToNetState_Object = MibTableColumn
sUniCktInfoUniToNetState = _SUniCktInfoUniToNetState_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 8, 5, 2, 1, 5),
    _SUniCktInfoUniToNetState_Type()
)
sUniCktInfoUniToNetState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sUniCktInfoUniToNetState.setStatus("mandatory")


class _SUniCktInfoNetToUniState_Type(Integer32):
    """Custom type sUniCktInfoNetToUniState based on Integer32"""
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


_SUniCktInfoNetToUniState_Type.__name__ = "Integer32"
_SUniCktInfoNetToUniState_Object = MibTableColumn
sUniCktInfoNetToUniState = _SUniCktInfoNetToUniState_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 8, 5, 2, 1, 6),
    _SUniCktInfoNetToUniState_Type()
)
sUniCktInfoNetToUniState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sUniCktInfoNetToUniState.setStatus("mandatory")
_SUniCktInfoLastAtmErr_Type = OctetString
_SUniCktInfoLastAtmErr_Object = MibTableColumn
sUniCktInfoLastAtmErr = _SUniCktInfoLastAtmErr_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 8, 5, 2, 1, 7),
    _SUniCktInfoLastAtmErr_Type()
)
sUniCktInfoLastAtmErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sUniCktInfoLastAtmErr.setStatus("mandatory")
_SUniCktInfoDataCellsRequired_Type = Integer32
_SUniCktInfoDataCellsRequired_Object = MibTableColumn
sUniCktInfoDataCellsRequired = _SUniCktInfoDataCellsRequired_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 8, 5, 2, 1, 8),
    _SUniCktInfoDataCellsRequired_Type()
)
sUniCktInfoDataCellsRequired.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sUniCktInfoDataCellsRequired.setStatus("mandatory")


class _SUniCktInfoLastAtmLocation_Type(DisplayString):
    """Custom type sUniCktInfoLastAtmLocation based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_SUniCktInfoLastAtmLocation_Type.__name__ = "DisplayString"
_SUniCktInfoLastAtmLocation_Object = MibTableColumn
sUniCktInfoLastAtmLocation = _SUniCktInfoLastAtmLocation_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 8, 5, 2, 1, 9),
    _SUniCktInfoLastAtmLocation_Type()
)
sUniCktInfoLastAtmLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sUniCktInfoLastAtmLocation.setStatus("mandatory")
_PvcInfo_ObjectIdentity = ObjectIdentity
pvcInfo = _PvcInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 8, 6)
)
_PvcCfgTable_Object = MibTable
pvcCfgTable = _PvcCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 8, 6, 1)
)
if mibBuilder.loadTexts:
    pvcCfgTable.setStatus("mandatory")
_PvcEntry_Object = MibTableRow
pvcEntry = _PvcEntry_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 8, 6, 1, 1)
)
pvcEntry.setIndexNames(
    (0, "LIGHTSTREAM-MIB", "pvcSrcIfIndex"),
    (0, "LIGHTSTREAM-MIB", "pvcSrcPvcId"),
)
if mibBuilder.loadTexts:
    pvcEntry.setStatus("mandatory")
_PvcSrcIfIndex_Type = Integer32
_PvcSrcIfIndex_Object = MibTableColumn
pvcSrcIfIndex = _PvcSrcIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 8, 6, 1, 1, 1),
    _PvcSrcIfIndex_Type()
)
pvcSrcIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvcSrcIfIndex.setStatus("mandatory")
_PvcSrcPvcId_Type = Integer32
_PvcSrcPvcId_Object = MibTableColumn
pvcSrcPvcId = _PvcSrcPvcId_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 8, 6, 1, 1, 2),
    _PvcSrcPvcId_Type()
)
pvcSrcPvcId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvcSrcPvcId.setStatus("mandatory")
_PvcSrcNode_Type = Integer32
_PvcSrcNode_Object = MibTableColumn
pvcSrcNode = _PvcSrcNode_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 8, 6, 1, 1, 3),
    _PvcSrcNode_Type()
)
pvcSrcNode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvcSrcNode.setStatus("mandatory")


class _PvcSrcInsuredRate_Type(Integer32):
    """Custom type pvcSrcInsuredRate based on Integer32"""
    defaultValue = 0


_PvcSrcInsuredRate_Object = MibTableColumn
pvcSrcInsuredRate = _PvcSrcInsuredRate_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 8, 6, 1, 1, 4),
    _PvcSrcInsuredRate_Type()
)
pvcSrcInsuredRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pvcSrcInsuredRate.setStatus("mandatory")


class _PvcSrcInsuredBurst_Type(Integer32):
    """Custom type pvcSrcInsuredBurst based on Integer32"""
    defaultValue = 0


_PvcSrcInsuredBurst_Object = MibTableColumn
pvcSrcInsuredBurst = _PvcSrcInsuredBurst_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 8, 6, 1, 1, 5),
    _PvcSrcInsuredBurst_Type()
)
pvcSrcInsuredBurst.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pvcSrcInsuredBurst.setStatus("mandatory")


class _PvcSrcMaxRate_Type(Integer32):
    """Custom type pvcSrcMaxRate based on Integer32"""
    defaultValue = 0


_PvcSrcMaxRate_Object = MibTableColumn
pvcSrcMaxRate = _PvcSrcMaxRate_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 8, 6, 1, 1, 6),
    _PvcSrcMaxRate_Type()
)
pvcSrcMaxRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pvcSrcMaxRate.setStatus("mandatory")


class _PvcSrcMaxBurst_Type(Integer32):
    """Custom type pvcSrcMaxBurst based on Integer32"""
    defaultValue = 0


_PvcSrcMaxBurst_Object = MibTableColumn
pvcSrcMaxBurst = _PvcSrcMaxBurst_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 8, 6, 1, 1, 7),
    _PvcSrcMaxBurst_Type()
)
pvcSrcMaxBurst.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pvcSrcMaxBurst.setStatus("mandatory")


class _PvcSecondaryScale_Type(Integer32):
    """Custom type pvcSecondaryScale based on Integer32"""
    defaultValue = 255


_PvcSecondaryScale_Object = MibTableColumn
pvcSecondaryScale = _PvcSecondaryScale_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 8, 6, 1, 1, 8),
    _PvcSecondaryScale_Type()
)
pvcSecondaryScale.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pvcSecondaryScale.setStatus("mandatory")


class _PvcPrinBwType_Type(Integer32):
    """Custom type pvcPrinBwType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("guaranteed", 1),
          ("insured", 2))
    )


_PvcPrinBwType_Type.__name__ = "Integer32"
_PvcPrinBwType_Object = MibTableColumn
pvcPrinBwType = _PvcPrinBwType_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 8, 6, 1, 1, 9),
    _PvcPrinBwType_Type()
)
pvcPrinBwType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pvcPrinBwType.setStatus("mandatory")


class _PvcTransPri_Type(Integer32):
    """Custom type pvcTransPri based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_PvcTransPri_Type.__name__ = "Integer32"
_PvcTransPri_Object = MibTableColumn
pvcTransPri = _PvcTransPri_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 8, 6, 1, 1, 10),
    _PvcTransPri_Type()
)
pvcTransPri.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pvcTransPri.setStatus("mandatory")


class _PvcUserDataPerCell_Type(Integer32):
    """Custom type pvcUserDataPerCell based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 384),
    )


_PvcUserDataPerCell_Type.__name__ = "Integer32"
_PvcUserDataPerCell_Object = MibTableColumn
pvcUserDataPerCell = _PvcUserDataPerCell_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 8, 6, 1, 1, 11),
    _PvcUserDataPerCell_Type()
)
pvcUserDataPerCell.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pvcUserDataPerCell.setStatus("mandatory")


class _PvcStatus_Type(Integer32):
    """Custom type pvcStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("delete", 3),
          ("disabled", 2),
          ("enabled", 1))
    )


_PvcStatus_Type.__name__ = "Integer32"
_PvcStatus_Object = MibTableColumn
pvcStatus = _PvcStatus_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 8, 6, 1, 1, 99),
    _PvcStatus_Type()
)
pvcStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pvcStatus.setStatus("mandatory")
_McEndptInfo_ObjectIdentity = ObjectIdentity
mcEndptInfo = _McEndptInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 8, 7)
)
_McEndptCfgTable_Object = MibTable
mcEndptCfgTable = _McEndptCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 8, 7, 1)
)
if mibBuilder.loadTexts:
    mcEndptCfgTable.setStatus("mandatory")
_McEndptEntry_Object = MibTableRow
mcEndptEntry = _McEndptEntry_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 8, 7, 1, 1)
)
mcEndptEntry.setIndexNames(
    (0, "LIGHTSTREAM-MIB", "mcEndptLclIfIndex"),
    (0, "LIGHTSTREAM-MIB", "mcEndptLclCktid"),
    (0, "LIGHTSTREAM-MIB", "mcEndptLclInstance"),
)
if mibBuilder.loadTexts:
    mcEndptEntry.setStatus("mandatory")
_McEndptLclIfIndex_Type = Integer32
_McEndptLclIfIndex_Object = MibTableColumn
mcEndptLclIfIndex = _McEndptLclIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 8, 7, 1, 1, 1),
    _McEndptLclIfIndex_Type()
)
mcEndptLclIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcEndptLclIfIndex.setStatus("mandatory")
_McEndptLclCktid_Type = Integer32
_McEndptLclCktid_Object = MibTableColumn
mcEndptLclCktid = _McEndptLclCktid_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 8, 7, 1, 1, 2),
    _McEndptLclCktid_Type()
)
mcEndptLclCktid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcEndptLclCktid.setStatus("mandatory")
_McEndptLclInstance_Type = Integer32
_McEndptLclInstance_Object = MibTableColumn
mcEndptLclInstance = _McEndptLclInstance_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 8, 7, 1, 1, 3),
    _McEndptLclInstance_Type()
)
mcEndptLclInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcEndptLclInstance.setStatus("mandatory")


class _McEndptDest_Type(DisplayString):
    """Custom type mcEndptDest based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_McEndptDest_Type.__name__ = "DisplayString"
_McEndptDest_Object = MibTableColumn
mcEndptDest = _McEndptDest_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 8, 7, 1, 1, 4),
    _McEndptDest_Type()
)
mcEndptDest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcEndptDest.setStatus("mandatory")
_McEndptServiceType_Type = Integer32
_McEndptServiceType_Object = MibTableColumn
mcEndptServiceType = _McEndptServiceType_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 8, 7, 1, 1, 5),
    _McEndptServiceType_Type()
)
mcEndptServiceType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcEndptServiceType.setStatus("mandatory")


class _McEndptRmtVCstatus_Type(Integer32):
    """Custom type mcEndptRmtVCstatus based on Integer32"""
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


_McEndptRmtVCstatus_Type.__name__ = "Integer32"
_McEndptRmtVCstatus_Object = MibTableColumn
mcEndptRmtVCstatus = _McEndptRmtVCstatus_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 8, 7, 1, 1, 6),
    _McEndptRmtVCstatus_Type()
)
mcEndptRmtVCstatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcEndptRmtVCstatus.setStatus("mandatory")
_McEndptCallIDIncoming_Type = Integer32
_McEndptCallIDIncoming_Object = MibTableColumn
mcEndptCallIDIncoming = _McEndptCallIDIncoming_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 8, 7, 1, 1, 7),
    _McEndptCallIDIncoming_Type()
)
mcEndptCallIDIncoming.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcEndptCallIDIncoming.setStatus("mandatory")


class _McEndptDownstreamState_Type(Integer32):
    """Custom type mcEndptDownstreamState based on Integer32"""
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


_McEndptDownstreamState_Type.__name__ = "Integer32"
_McEndptDownstreamState_Object = MibTableColumn
mcEndptDownstreamState = _McEndptDownstreamState_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 8, 7, 1, 1, 8),
    _McEndptDownstreamState_Type()
)
mcEndptDownstreamState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcEndptDownstreamState.setStatus("mandatory")


class _McEndptUpstreamState_Type(Integer32):
    """Custom type mcEndptUpstreamState based on Integer32"""
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


_McEndptUpstreamState_Type.__name__ = "Integer32"
_McEndptUpstreamState_Object = MibTableColumn
mcEndptUpstreamState = _McEndptUpstreamState_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 8, 7, 1, 1, 9),
    _McEndptUpstreamState_Type()
)
mcEndptUpstreamState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcEndptUpstreamState.setStatus("mandatory")
_McEndptLastAtmErr_Type = OctetString
_McEndptLastAtmErr_Object = MibTableColumn
mcEndptLastAtmErr = _McEndptLastAtmErr_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 8, 7, 1, 1, 10),
    _McEndptLastAtmErr_Type()
)
mcEndptLastAtmErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcEndptLastAtmErr.setStatus("mandatory")


class _McEndptLastAtmLocation_Type(DisplayString):
    """Custom type mcEndptLastAtmLocation based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_McEndptLastAtmLocation_Type.__name__ = "DisplayString"
_McEndptLastAtmLocation_Object = MibTableColumn
mcEndptLastAtmLocation = _McEndptLastAtmLocation_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 8, 7, 1, 1, 11),
    _McEndptLastAtmLocation_Type()
)
mcEndptLastAtmLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcEndptLastAtmLocation.setStatus("mandatory")


class _McEndptStatus_Type(Integer32):
    """Custom type mcEndptStatus based on Integer32"""
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
        *(("createRequest", 4),
          ("delete", 3),
          ("disabled", 2),
          ("enabled", 1),
          ("underCreation", 5))
    )


_McEndptStatus_Type.__name__ = "Integer32"
_McEndptStatus_Object = MibTableColumn
mcEndptStatus = _McEndptStatus_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 8, 7, 1, 1, 99),
    _McEndptStatus_Type()
)
mcEndptStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcEndptStatus.setStatus("mandatory")
_LsPrivate_ObjectIdentity = ObjectIdentity
lsPrivate = _LsPrivate_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 10)
)
_LsExperimental_ObjectIdentity = ObjectIdentity
lsExperimental = _LsExperimental_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 11)
)
_LsExperimentalStatistics_ObjectIdentity = ObjectIdentity
lsExperimentalStatistics = _LsExperimentalStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 11, 1)
)
_LsEdgeStatistics_ObjectIdentity = ObjectIdentity
lsEdgeStatistics = _LsEdgeStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 11, 1, 1)
)
_LsEdgeStatTable_Object = MibTable
lsEdgeStatTable = _LsEdgeStatTable_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 11, 1, 1, 1)
)
if mibBuilder.loadTexts:
    lsEdgeStatTable.setStatus("mandatory")
_LsEdgeStatEntry_Object = MibTableRow
lsEdgeStatEntry = _LsEdgeStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 11, 1, 1, 1, 1)
)
lsEdgeStatEntry.setIndexNames(
    (0, "LIGHTSTREAM-MIB", "edgeStatIndex"),
)
if mibBuilder.loadTexts:
    lsEdgeStatEntry.setStatus("mandatory")
_EdgeStatIndex_Type = Integer32
_EdgeStatIndex_Object = MibTableColumn
edgeStatIndex = _EdgeStatIndex_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 11, 1, 1, 1, 1, 1),
    _EdgeStatIndex_Type()
)
edgeStatIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edgeStatIndex.setStatus("mandatory")
_EdgeStatFsuRATOs_Type = Counter32
_EdgeStatFsuRATOs_Object = MibTableColumn
edgeStatFsuRATOs = _EdgeStatFsuRATOs_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 11, 1, 1, 1, 1, 2),
    _EdgeStatFsuRATOs_Type()
)
edgeStatFsuRATOs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edgeStatFsuRATOs.setStatus("mandatory")
_EdgeStatFsuRATOLastInfo_Type = Integer32
_EdgeStatFsuRATOLastInfo_Object = MibTableColumn
edgeStatFsuRATOLastInfo = _EdgeStatFsuRATOLastInfo_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 11, 1, 1, 1, 1, 3),
    _EdgeStatFsuRATOLastInfo_Type()
)
edgeStatFsuRATOLastInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edgeStatFsuRATOLastInfo.setStatus("mandatory")
_EdgeStatTsuHoldQCells_Type = Gauge32
_EdgeStatTsuHoldQCells_Object = MibTableColumn
edgeStatTsuHoldQCells = _EdgeStatTsuHoldQCells_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 11, 1, 1, 1, 1, 4),
    _EdgeStatTsuHoldQCells_Type()
)
edgeStatTsuHoldQCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edgeStatTsuHoldQCells.setStatus("mandatory")
_EdgeStatTsuHoldQs_Type = Gauge32
_EdgeStatTsuHoldQs_Object = MibTableColumn
edgeStatTsuHoldQs = _EdgeStatTsuHoldQs_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 11, 1, 1, 1, 1, 5),
    _EdgeStatTsuHoldQs_Type()
)
edgeStatTsuHoldQs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edgeStatTsuHoldQs.setStatus("mandatory")
_TluAAL5XsumErrs_Type = Counter32
_TluAAL5XsumErrs_Object = MibTableColumn
tluAAL5XsumErrs = _TluAAL5XsumErrs_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 11, 1, 1, 1, 1, 6),
    _TluAAL5XsumErrs_Type()
)
tluAAL5XsumErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tluAAL5XsumErrs.setStatus("mandatory")
_TluAAL5AbortErrs_Type = Counter32
_TluAAL5AbortErrs_Object = MibTableColumn
tluAAL5AbortErrs = _TluAAL5AbortErrs_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 11, 1, 1, 1, 1, 7),
    _TluAAL5AbortErrs_Type()
)
tluAAL5AbortErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tluAAL5AbortErrs.setStatus("mandatory")
_TluAAL5ErrLastVci_Type = Integer32
_TluAAL5ErrLastVci_Object = MibTableColumn
tluAAL5ErrLastVci = _TluAAL5ErrLastVci_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 11, 1, 1, 1, 1, 8),
    _TluAAL5ErrLastVci_Type()
)
tluAAL5ErrLastVci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tluAAL5ErrLastVci.setStatus("mandatory")
_LsEdgePortStatTable_Object = MibTable
lsEdgePortStatTable = _LsEdgePortStatTable_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 11, 1, 1, 2)
)
if mibBuilder.loadTexts:
    lsEdgePortStatTable.setStatus("mandatory")
_LsEdgePortStatEntry_Object = MibTableRow
lsEdgePortStatEntry = _LsEdgePortStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 11, 1, 1, 2, 1)
)
lsEdgePortStatEntry.setIndexNames(
    (0, "LIGHTSTREAM-MIB", "edgePortStatIndex"),
)
if mibBuilder.loadTexts:
    lsEdgePortStatEntry.setStatus("mandatory")
_EdgePortStatIndex_Type = Integer32
_EdgePortStatIndex_Object = MibTableColumn
edgePortStatIndex = _EdgePortStatIndex_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 11, 1, 1, 2, 1, 1),
    _EdgePortStatIndex_Type()
)
edgePortStatIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edgePortStatIndex.setStatus("mandatory")
_EdgePortRcvOctets_Type = Counter32
_EdgePortRcvOctets_Object = MibTableColumn
edgePortRcvOctets = _EdgePortRcvOctets_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 11, 1, 1, 2, 1, 2),
    _EdgePortRcvOctets_Type()
)
edgePortRcvOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edgePortRcvOctets.setStatus("mandatory")
_EdgePortXmtOctets_Type = Counter32
_EdgePortXmtOctets_Object = MibTableColumn
edgePortXmtOctets = _EdgePortXmtOctets_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 11, 1, 1, 2, 1, 3),
    _EdgePortXmtOctets_Type()
)
edgePortXmtOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edgePortXmtOctets.setStatus("mandatory")
_EdgePortFsuCksmErrMsgs_Type = Counter32
_EdgePortFsuCksmErrMsgs_Object = MibTableColumn
edgePortFsuCksmErrMsgs = _EdgePortFsuCksmErrMsgs_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 11, 1, 1, 2, 1, 4),
    _EdgePortFsuCksmErrMsgs_Type()
)
edgePortFsuCksmErrMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edgePortFsuCksmErrMsgs.setStatus("mandatory")
_EdgePortCksmErrLastVci_Type = Integer32
_EdgePortCksmErrLastVci_Object = MibTableColumn
edgePortCksmErrLastVci = _EdgePortCksmErrLastVci_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 11, 1, 1, 2, 1, 5),
    _EdgePortCksmErrLastVci_Type()
)
edgePortCksmErrLastVci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edgePortCksmErrLastVci.setStatus("mandatory")
_EdgePortDownXmtFrames_Type = Counter32
_EdgePortDownXmtFrames_Object = MibTableColumn
edgePortDownXmtFrames = _EdgePortDownXmtFrames_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 11, 1, 1, 2, 1, 6),
    _EdgePortDownXmtFrames_Type()
)
edgePortDownXmtFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edgePortDownXmtFrames.setStatus("mandatory")
_EdgePortRcvUcastPkts_Type = Counter32
_EdgePortRcvUcastPkts_Object = MibTableColumn
edgePortRcvUcastPkts = _EdgePortRcvUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 11, 1, 1, 2, 1, 7),
    _EdgePortRcvUcastPkts_Type()
)
edgePortRcvUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edgePortRcvUcastPkts.setStatus("mandatory")
_EdgePortRcvNUcastPkts_Type = Counter32
_EdgePortRcvNUcastPkts_Object = MibTableColumn
edgePortRcvNUcastPkts = _EdgePortRcvNUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 11, 1, 1, 2, 1, 8),
    _EdgePortRcvNUcastPkts_Type()
)
edgePortRcvNUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edgePortRcvNUcastPkts.setStatus("mandatory")
_EdgePortXmtUcastPkts_Type = Counter32
_EdgePortXmtUcastPkts_Object = MibTableColumn
edgePortXmtUcastPkts = _EdgePortXmtUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 11, 1, 1, 2, 1, 9),
    _EdgePortXmtUcastPkts_Type()
)
edgePortXmtUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edgePortXmtUcastPkts.setStatus("mandatory")
_EdgePortXmtNUcastPkts_Type = Counter32
_EdgePortXmtNUcastPkts_Object = MibTableColumn
edgePortXmtNUcastPkts = _EdgePortXmtNUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 11, 1, 1, 2, 1, 10),
    _EdgePortXmtNUcastPkts_Type()
)
edgePortXmtNUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edgePortXmtNUcastPkts.setStatus("mandatory")
_EdgePortRcvSmplPktSize_Type = Gauge32
_EdgePortRcvSmplPktSize_Object = MibTableColumn
edgePortRcvSmplPktSize = _EdgePortRcvSmplPktSize_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 11, 1, 1, 2, 1, 11),
    _EdgePortRcvSmplPktSize_Type()
)
edgePortRcvSmplPktSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edgePortRcvSmplPktSize.setStatus("mandatory")
_EdgePortXmtSmplPktSize_Type = Gauge32
_EdgePortXmtSmplPktSize_Object = MibTableColumn
edgePortXmtSmplPktSize = _EdgePortXmtSmplPktSize_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 11, 1, 1, 2, 1, 12),
    _EdgePortXmtSmplPktSize_Type()
)
edgePortXmtSmplPktSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edgePortXmtSmplPktSize.setStatus("mandatory")
_EdgePortRcvL3XsumErrs_Type = Counter32
_EdgePortRcvL3XsumErrs_Object = MibTableColumn
edgePortRcvL3XsumErrs = _EdgePortRcvL3XsumErrs_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 11, 1, 1, 2, 1, 13),
    _EdgePortRcvL3XsumErrs_Type()
)
edgePortRcvL3XsumErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edgePortRcvL3XsumErrs.setStatus("mandatory")
_EdgePortRcvL3XsumErrLastVci_Type = Integer32
_EdgePortRcvL3XsumErrLastVci_Object = MibTableColumn
edgePortRcvL3XsumErrLastVci = _EdgePortRcvL3XsumErrLastVci_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 11, 1, 1, 2, 1, 14),
    _EdgePortRcvL3XsumErrLastVci_Type()
)
edgePortRcvL3XsumErrLastVci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edgePortRcvL3XsumErrLastVci.setStatus("mandatory")
_EdgePortRcvCRCErrors_Type = Counter32
_EdgePortRcvCRCErrors_Object = MibTableColumn
edgePortRcvCRCErrors = _EdgePortRcvCRCErrors_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 11, 1, 1, 2, 1, 15),
    _EdgePortRcvCRCErrors_Type()
)
edgePortRcvCRCErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edgePortRcvCRCErrors.setStatus("mandatory")
_EdgePortRcvAborts_Type = Counter32
_EdgePortRcvAborts_Object = MibTableColumn
edgePortRcvAborts = _EdgePortRcvAborts_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 11, 1, 1, 2, 1, 16),
    _EdgePortRcvAborts_Type()
)
edgePortRcvAborts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edgePortRcvAborts.setStatus("mandatory")
_EdgePortXmtUnderflows_Type = Counter32
_EdgePortXmtUnderflows_Object = MibTableColumn
edgePortXmtUnderflows = _EdgePortXmtUnderflows_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 11, 1, 1, 2, 1, 17),
    _EdgePortXmtUnderflows_Type()
)
edgePortXmtUnderflows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edgePortXmtUnderflows.setStatus("mandatory")
_EdgePortRcvShortFrames_Type = Counter32
_EdgePortRcvShortFrames_Object = MibTableColumn
edgePortRcvShortFrames = _EdgePortRcvShortFrames_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 11, 1, 1, 2, 1, 18),
    _EdgePortRcvShortFrames_Type()
)
edgePortRcvShortFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edgePortRcvShortFrames.setStatus("mandatory")
_LsFrameRelayDlciStatTable_Object = MibTable
lsFrameRelayDlciStatTable = _LsFrameRelayDlciStatTable_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 11, 1, 1, 3)
)
if mibBuilder.loadTexts:
    lsFrameRelayDlciStatTable.setStatus("mandatory")
_LsFrameRelayDlciStatEntry_Object = MibTableRow
lsFrameRelayDlciStatEntry = _LsFrameRelayDlciStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 11, 1, 1, 3, 1)
)
lsFrameRelayDlciStatEntry.setIndexNames(
    (0, "LIGHTSTREAM-MIB", "frameRelayDlciStatPortIndex"),
    (0, "LIGHTSTREAM-MIB", "frameRelayDlciStatDlciIndex"),
)
if mibBuilder.loadTexts:
    lsFrameRelayDlciStatEntry.setStatus("mandatory")
_FrameRelayDlciStatPortIndex_Type = Integer32
_FrameRelayDlciStatPortIndex_Object = MibTableColumn
frameRelayDlciStatPortIndex = _FrameRelayDlciStatPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 11, 1, 1, 3, 1, 1),
    _FrameRelayDlciStatPortIndex_Type()
)
frameRelayDlciStatPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frameRelayDlciStatPortIndex.setStatus("mandatory")
_FrameRelayDlciStatDlciIndex_Type = Integer32
_FrameRelayDlciStatDlciIndex_Object = MibTableColumn
frameRelayDlciStatDlciIndex = _FrameRelayDlciStatDlciIndex_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 11, 1, 1, 3, 1, 2),
    _FrameRelayDlciStatDlciIndex_Type()
)
frameRelayDlciStatDlciIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frameRelayDlciStatDlciIndex.setStatus("mandatory")
_FrameRelayDlciToSwCLP0Frames_Type = Counter32
_FrameRelayDlciToSwCLP0Frames_Object = MibTableColumn
frameRelayDlciToSwCLP0Frames = _FrameRelayDlciToSwCLP0Frames_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 11, 1, 1, 3, 1, 3),
    _FrameRelayDlciToSwCLP0Frames_Type()
)
frameRelayDlciToSwCLP0Frames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frameRelayDlciToSwCLP0Frames.setStatus("mandatory")
_FrameRelayDlciToSwCLP0Cells_Type = Counter32
_FrameRelayDlciToSwCLP0Cells_Object = MibTableColumn
frameRelayDlciToSwCLP0Cells = _FrameRelayDlciToSwCLP0Cells_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 11, 1, 1, 3, 1, 4),
    _FrameRelayDlciToSwCLP0Cells_Type()
)
frameRelayDlciToSwCLP0Cells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frameRelayDlciToSwCLP0Cells.setStatus("mandatory")
_FrameRelayDlciToSwCLP1Frames_Type = Counter32
_FrameRelayDlciToSwCLP1Frames_Object = MibTableColumn
frameRelayDlciToSwCLP1Frames = _FrameRelayDlciToSwCLP1Frames_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 11, 1, 1, 3, 1, 5),
    _FrameRelayDlciToSwCLP1Frames_Type()
)
frameRelayDlciToSwCLP1Frames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frameRelayDlciToSwCLP1Frames.setStatus("mandatory")
_FrameRelayDlciToSwCLP1Cells_Type = Counter32
_FrameRelayDlciToSwCLP1Cells_Object = MibTableColumn
frameRelayDlciToSwCLP1Cells = _FrameRelayDlciToSwCLP1Cells_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 11, 1, 1, 3, 1, 6),
    _FrameRelayDlciToSwCLP1Cells_Type()
)
frameRelayDlciToSwCLP1Cells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frameRelayDlciToSwCLP1Cells.setStatus("mandatory")
_FrameRelayDlciToSwDiscardFrames_Type = Counter32
_FrameRelayDlciToSwDiscardFrames_Object = MibTableColumn
frameRelayDlciToSwDiscardFrames = _FrameRelayDlciToSwDiscardFrames_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 11, 1, 1, 3, 1, 7),
    _FrameRelayDlciToSwDiscardFrames_Type()
)
frameRelayDlciToSwDiscardFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frameRelayDlciToSwDiscardFrames.setStatus("mandatory")
_FrameRelayDlciToSwDiscardCells_Type = Counter32
_FrameRelayDlciToSwDiscardCells_Object = MibTableColumn
frameRelayDlciToSwDiscardCells = _FrameRelayDlciToSwDiscardCells_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 11, 1, 1, 3, 1, 8),
    _FrameRelayDlciToSwDiscardCells_Type()
)
frameRelayDlciToSwDiscardCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frameRelayDlciToSwDiscardCells.setStatus("mandatory")
_FrameRelayDlciFrSwCLP0Frames_Type = Counter32
_FrameRelayDlciFrSwCLP0Frames_Object = MibTableColumn
frameRelayDlciFrSwCLP0Frames = _FrameRelayDlciFrSwCLP0Frames_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 11, 1, 1, 3, 1, 9),
    _FrameRelayDlciFrSwCLP0Frames_Type()
)
frameRelayDlciFrSwCLP0Frames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frameRelayDlciFrSwCLP0Frames.setStatus("mandatory")
_FrameRelayDlciFrSwCLP0Cells_Type = Counter32
_FrameRelayDlciFrSwCLP0Cells_Object = MibTableColumn
frameRelayDlciFrSwCLP0Cells = _FrameRelayDlciFrSwCLP0Cells_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 11, 1, 1, 3, 1, 10),
    _FrameRelayDlciFrSwCLP0Cells_Type()
)
frameRelayDlciFrSwCLP0Cells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frameRelayDlciFrSwCLP0Cells.setStatus("mandatory")
_FrameRelayDlciFrSwCLP1Frames_Type = Counter32
_FrameRelayDlciFrSwCLP1Frames_Object = MibTableColumn
frameRelayDlciFrSwCLP1Frames = _FrameRelayDlciFrSwCLP1Frames_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 11, 1, 1, 3, 1, 11),
    _FrameRelayDlciFrSwCLP1Frames_Type()
)
frameRelayDlciFrSwCLP1Frames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frameRelayDlciFrSwCLP1Frames.setStatus("mandatory")
_FrameRelayDlciFrSwCLP1Cells_Type = Counter32
_FrameRelayDlciFrSwCLP1Cells_Object = MibTableColumn
frameRelayDlciFrSwCLP1Cells = _FrameRelayDlciFrSwCLP1Cells_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 11, 1, 1, 3, 1, 12),
    _FrameRelayDlciFrSwCLP1Cells_Type()
)
frameRelayDlciFrSwCLP1Cells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frameRelayDlciFrSwCLP1Cells.setStatus("mandatory")
_LsEdgePortToSwMsgLenTable_Object = MibTable
lsEdgePortToSwMsgLenTable = _LsEdgePortToSwMsgLenTable_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 11, 1, 1, 4)
)
if mibBuilder.loadTexts:
    lsEdgePortToSwMsgLenTable.setStatus("mandatory")
_LsEdgePortToSwMsgLenEntry_Object = MibTableRow
lsEdgePortToSwMsgLenEntry = _LsEdgePortToSwMsgLenEntry_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 11, 1, 1, 4, 1)
)
lsEdgePortToSwMsgLenEntry.setIndexNames(
    (0, "LIGHTSTREAM-MIB", "edgeToSwMsgLenPortIndex"),
    (0, "LIGHTSTREAM-MIB", "edgeToSwMsgLenBinIndex"),
)
if mibBuilder.loadTexts:
    lsEdgePortToSwMsgLenEntry.setStatus("mandatory")
_EdgeToSwMsgLenPortIndex_Type = Integer32
_EdgeToSwMsgLenPortIndex_Object = MibTableColumn
edgeToSwMsgLenPortIndex = _EdgeToSwMsgLenPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 11, 1, 1, 4, 1, 1),
    _EdgeToSwMsgLenPortIndex_Type()
)
edgeToSwMsgLenPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edgeToSwMsgLenPortIndex.setStatus("mandatory")
_EdgeToSwMsgLenBinIndex_Type = Integer32
_EdgeToSwMsgLenBinIndex_Object = MibTableColumn
edgeToSwMsgLenBinIndex = _EdgeToSwMsgLenBinIndex_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 11, 1, 1, 4, 1, 2),
    _EdgeToSwMsgLenBinIndex_Type()
)
edgeToSwMsgLenBinIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edgeToSwMsgLenBinIndex.setStatus("mandatory")
_EdgeToSwMsgLenMsgs_Type = Counter32
_EdgeToSwMsgLenMsgs_Object = MibTableColumn
edgeToSwMsgLenMsgs = _EdgeToSwMsgLenMsgs_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 11, 1, 1, 4, 1, 3),
    _EdgeToSwMsgLenMsgs_Type()
)
edgeToSwMsgLenMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edgeToSwMsgLenMsgs.setStatus("mandatory")
_LsEdgeSwToPortMsgLenTable_Object = MibTable
lsEdgeSwToPortMsgLenTable = _LsEdgeSwToPortMsgLenTable_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 11, 1, 1, 5)
)
if mibBuilder.loadTexts:
    lsEdgeSwToPortMsgLenTable.setStatus("mandatory")
_LsEdgeSwToPortMsgLenEntry_Object = MibTableRow
lsEdgeSwToPortMsgLenEntry = _LsEdgeSwToPortMsgLenEntry_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 11, 1, 1, 5, 1)
)
lsEdgeSwToPortMsgLenEntry.setIndexNames(
    (0, "LIGHTSTREAM-MIB", "edgeToPortMsgLenPortIndex"),
    (0, "LIGHTSTREAM-MIB", "edgeToPortMsgLenBinIndex"),
)
if mibBuilder.loadTexts:
    lsEdgeSwToPortMsgLenEntry.setStatus("mandatory")
_EdgeToPortMsgLenPortIndex_Type = Integer32
_EdgeToPortMsgLenPortIndex_Object = MibTableColumn
edgeToPortMsgLenPortIndex = _EdgeToPortMsgLenPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 11, 1, 1, 5, 1, 1),
    _EdgeToPortMsgLenPortIndex_Type()
)
edgeToPortMsgLenPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edgeToPortMsgLenPortIndex.setStatus("mandatory")
_EdgeToPortMsgLenBinIndex_Type = Integer32
_EdgeToPortMsgLenBinIndex_Object = MibTableColumn
edgeToPortMsgLenBinIndex = _EdgeToPortMsgLenBinIndex_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 11, 1, 1, 5, 1, 2),
    _EdgeToPortMsgLenBinIndex_Type()
)
edgeToPortMsgLenBinIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edgeToPortMsgLenBinIndex.setStatus("mandatory")
_EdgeToPortMsgLenMsgs_Type = Counter32
_EdgeToPortMsgLenMsgs_Object = MibTableColumn
edgeToPortMsgLenMsgs = _EdgeToPortMsgLenMsgs_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 11, 1, 1, 5, 1, 3),
    _EdgeToPortMsgLenMsgs_Type()
)
edgeToPortMsgLenMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edgeToPortMsgLenMsgs.setStatus("mandatory")
_LsEdgeCpuWorkloadTable_Object = MibTable
lsEdgeCpuWorkloadTable = _LsEdgeCpuWorkloadTable_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 11, 1, 1, 6)
)
if mibBuilder.loadTexts:
    lsEdgeCpuWorkloadTable.setStatus("mandatory")
_LsEdgeCpuWorkloadEntry_Object = MibTableRow
lsEdgeCpuWorkloadEntry = _LsEdgeCpuWorkloadEntry_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 11, 1, 1, 6, 1)
)
lsEdgeCpuWorkloadEntry.setIndexNames(
    (0, "LIGHTSTREAM-MIB", "lsEdgeWorkloadCardIndex"),
    (0, "LIGHTSTREAM-MIB", "lsEdgeWorkloadTypeIndex"),
)
if mibBuilder.loadTexts:
    lsEdgeCpuWorkloadEntry.setStatus("mandatory")
_LsEdgeWorkloadCardIndex_Type = Integer32
_LsEdgeWorkloadCardIndex_Object = MibTableColumn
lsEdgeWorkloadCardIndex = _LsEdgeWorkloadCardIndex_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 11, 1, 1, 6, 1, 1),
    _LsEdgeWorkloadCardIndex_Type()
)
lsEdgeWorkloadCardIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lsEdgeWorkloadCardIndex.setStatus("mandatory")
_LsEdgeWorkloadTypeIndex_Type = Integer32
_LsEdgeWorkloadTypeIndex_Object = MibTableColumn
lsEdgeWorkloadTypeIndex = _LsEdgeWorkloadTypeIndex_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 11, 1, 1, 6, 1, 2),
    _LsEdgeWorkloadTypeIndex_Type()
)
lsEdgeWorkloadTypeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lsEdgeWorkloadTypeIndex.setStatus("mandatory")
_LsEdgeWorkloadEvents_Type = Counter32
_LsEdgeWorkloadEvents_Object = MibTableColumn
lsEdgeWorkloadEvents = _LsEdgeWorkloadEvents_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 11, 1, 1, 6, 1, 3),
    _LsEdgeWorkloadEvents_Type()
)
lsEdgeWorkloadEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lsEdgeWorkloadEvents.setStatus("mandatory")
_LsFrameForwardStatTable_Object = MibTable
lsFrameForwardStatTable = _LsFrameForwardStatTable_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 11, 1, 1, 7)
)
if mibBuilder.loadTexts:
    lsFrameForwardStatTable.setStatus("mandatory")
_LsFrameForwardStatEntry_Object = MibTableRow
lsFrameForwardStatEntry = _LsFrameForwardStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 11, 1, 1, 7, 1)
)
lsFrameForwardStatEntry.setIndexNames(
    (0, "LIGHTSTREAM-MIB", "frameForwardStatPortIndex"),
)
if mibBuilder.loadTexts:
    lsFrameForwardStatEntry.setStatus("mandatory")
_FrameForwardStatPortIndex_Type = Integer32
_FrameForwardStatPortIndex_Object = MibTableColumn
frameForwardStatPortIndex = _FrameForwardStatPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 11, 1, 1, 7, 1, 1),
    _FrameForwardStatPortIndex_Type()
)
frameForwardStatPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frameForwardStatPortIndex.setStatus("mandatory")
_FrameForwardToSwCLP0Frames_Type = Counter32
_FrameForwardToSwCLP0Frames_Object = MibTableColumn
frameForwardToSwCLP0Frames = _FrameForwardToSwCLP0Frames_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 11, 1, 1, 7, 1, 2),
    _FrameForwardToSwCLP0Frames_Type()
)
frameForwardToSwCLP0Frames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frameForwardToSwCLP0Frames.setStatus("mandatory")
_FrameForwardToSwCLP0Cells_Type = Counter32
_FrameForwardToSwCLP0Cells_Object = MibTableColumn
frameForwardToSwCLP0Cells = _FrameForwardToSwCLP0Cells_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 11, 1, 1, 7, 1, 3),
    _FrameForwardToSwCLP0Cells_Type()
)
frameForwardToSwCLP0Cells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frameForwardToSwCLP0Cells.setStatus("mandatory")
_FrameForwardToSwCLP1Frames_Type = Counter32
_FrameForwardToSwCLP1Frames_Object = MibTableColumn
frameForwardToSwCLP1Frames = _FrameForwardToSwCLP1Frames_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 11, 1, 1, 7, 1, 4),
    _FrameForwardToSwCLP1Frames_Type()
)
frameForwardToSwCLP1Frames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frameForwardToSwCLP1Frames.setStatus("mandatory")
_FrameForwardToSwCLP1Cells_Type = Counter32
_FrameForwardToSwCLP1Cells_Object = MibTableColumn
frameForwardToSwCLP1Cells = _FrameForwardToSwCLP1Cells_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 11, 1, 1, 7, 1, 5),
    _FrameForwardToSwCLP1Cells_Type()
)
frameForwardToSwCLP1Cells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frameForwardToSwCLP1Cells.setStatus("mandatory")
_FrameForwardToSwDiscardFrames_Type = Counter32
_FrameForwardToSwDiscardFrames_Object = MibTableColumn
frameForwardToSwDiscardFrames = _FrameForwardToSwDiscardFrames_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 11, 1, 1, 7, 1, 6),
    _FrameForwardToSwDiscardFrames_Type()
)
frameForwardToSwDiscardFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frameForwardToSwDiscardFrames.setStatus("mandatory")
_FrameForwardToSwDiscardCells_Type = Counter32
_FrameForwardToSwDiscardCells_Object = MibTableColumn
frameForwardToSwDiscardCells = _FrameForwardToSwDiscardCells_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 11, 1, 1, 7, 1, 7),
    _FrameForwardToSwDiscardCells_Type()
)
frameForwardToSwDiscardCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frameForwardToSwDiscardCells.setStatus("mandatory")
_FrameForwardFrSwCLP0Frames_Type = Counter32
_FrameForwardFrSwCLP0Frames_Object = MibTableColumn
frameForwardFrSwCLP0Frames = _FrameForwardFrSwCLP0Frames_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 11, 1, 1, 7, 1, 8),
    _FrameForwardFrSwCLP0Frames_Type()
)
frameForwardFrSwCLP0Frames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frameForwardFrSwCLP0Frames.setStatus("mandatory")
_FrameForwardFrSwCLP0Cells_Type = Counter32
_FrameForwardFrSwCLP0Cells_Object = MibTableColumn
frameForwardFrSwCLP0Cells = _FrameForwardFrSwCLP0Cells_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 11, 1, 1, 7, 1, 9),
    _FrameForwardFrSwCLP0Cells_Type()
)
frameForwardFrSwCLP0Cells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frameForwardFrSwCLP0Cells.setStatus("mandatory")
_FrameForwardFrSwCLP1Frames_Type = Counter32
_FrameForwardFrSwCLP1Frames_Object = MibTableColumn
frameForwardFrSwCLP1Frames = _FrameForwardFrSwCLP1Frames_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 11, 1, 1, 7, 1, 10),
    _FrameForwardFrSwCLP1Frames_Type()
)
frameForwardFrSwCLP1Frames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frameForwardFrSwCLP1Frames.setStatus("mandatory")
_FrameForwardFrSwCLP1Cells_Type = Counter32
_FrameForwardFrSwCLP1Cells_Object = MibTableColumn
frameForwardFrSwCLP1Cells = _FrameForwardFrSwCLP1Cells_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 11, 1, 1, 7, 1, 11),
    _FrameForwardFrSwCLP1Cells_Type()
)
frameForwardFrSwCLP1Cells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frameForwardFrSwCLP1Cells.setStatus("mandatory")
_LsTrunkStatistics_ObjectIdentity = ObjectIdentity
lsTrunkStatistics = _LsTrunkStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 11, 1, 2)
)
_LsTrunkPortStatTable_Object = MibTable
lsTrunkPortStatTable = _LsTrunkPortStatTable_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 11, 1, 2, 1)
)
if mibBuilder.loadTexts:
    lsTrunkPortStatTable.setStatus("mandatory")
_LsTrunkPortStatEntry_Object = MibTableRow
lsTrunkPortStatEntry = _LsTrunkPortStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 11, 1, 2, 1, 1)
)
lsTrunkPortStatEntry.setIndexNames(
    (0, "LIGHTSTREAM-MIB", "trunkPortStatIndex"),
)
if mibBuilder.loadTexts:
    lsTrunkPortStatEntry.setStatus("mandatory")
_TrunkPortStatIndex_Type = Integer32
_TrunkPortStatIndex_Object = MibTableColumn
trunkPortStatIndex = _TrunkPortStatIndex_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 11, 1, 2, 1, 1, 1),
    _TrunkPortStatIndex_Type()
)
trunkPortStatIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trunkPortStatIndex.setStatus("mandatory")
_TrunkPortRcvCells_Type = Counter32
_TrunkPortRcvCells_Object = MibTableColumn
trunkPortRcvCells = _TrunkPortRcvCells_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 11, 1, 2, 1, 1, 2),
    _TrunkPortRcvCells_Type()
)
trunkPortRcvCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trunkPortRcvCells.setStatus("mandatory")
_TrunkPortXmtCells_Type = Counter32
_TrunkPortXmtCells_Object = MibTableColumn
trunkPortXmtCells = _TrunkPortXmtCells_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 11, 1, 2, 1, 1, 3),
    _TrunkPortXmtCells_Type()
)
trunkPortXmtCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trunkPortXmtCells.setStatus("mandatory")
_TrunkPortRcvRuns_Type = Counter32
_TrunkPortRcvRuns_Object = MibTableColumn
trunkPortRcvRuns = _TrunkPortRcvRuns_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 11, 1, 2, 1, 1, 4),
    _TrunkPortRcvRuns_Type()
)
trunkPortRcvRuns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trunkPortRcvRuns.setStatus("mandatory")
_TrunkPortDownXmtCells_Type = Counter32
_TrunkPortDownXmtCells_Object = MibTableColumn
trunkPortDownXmtCells = _TrunkPortDownXmtCells_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 11, 1, 2, 1, 1, 5),
    _TrunkPortDownXmtCells_Type()
)
trunkPortDownXmtCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trunkPortDownXmtCells.setStatus("mandatory")
_TrunkPortRcvCRCErrors_Type = Counter32
_TrunkPortRcvCRCErrors_Object = MibTableColumn
trunkPortRcvCRCErrors = _TrunkPortRcvCRCErrors_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 11, 1, 2, 1, 1, 6),
    _TrunkPortRcvCRCErrors_Type()
)
trunkPortRcvCRCErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trunkPortRcvCRCErrors.setStatus("mandatory")
_TrunkPortRcvAborts_Type = Counter32
_TrunkPortRcvAborts_Object = MibTableColumn
trunkPortRcvAborts = _TrunkPortRcvAborts_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 11, 1, 2, 1, 1, 7),
    _TrunkPortRcvAborts_Type()
)
trunkPortRcvAborts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trunkPortRcvAborts.setStatus("mandatory")
_TrunkPortXmtUnderflows_Type = Counter32
_TrunkPortXmtUnderflows_Object = MibTableColumn
trunkPortXmtUnderflows = _TrunkPortXmtUnderflows_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 11, 1, 2, 1, 1, 8),
    _TrunkPortXmtUnderflows_Type()
)
trunkPortXmtUnderflows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trunkPortXmtUnderflows.setStatus("mandatory")
_TrunkPortRcvShortFrames_Type = Counter32
_TrunkPortRcvShortFrames_Object = MibTableColumn
trunkPortRcvShortFrames = _TrunkPortRcvShortFrames_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 11, 1, 2, 1, 1, 9),
    _TrunkPortRcvShortFrames_Type()
)
trunkPortRcvShortFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trunkPortRcvShortFrames.setStatus("mandatory")
_LsTrunkCpuWorkloadTable_Object = MibTable
lsTrunkCpuWorkloadTable = _LsTrunkCpuWorkloadTable_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 11, 1, 2, 2)
)
if mibBuilder.loadTexts:
    lsTrunkCpuWorkloadTable.setStatus("mandatory")
_LsTrunkCpuWorkloadEntry_Object = MibTableRow
lsTrunkCpuWorkloadEntry = _LsTrunkCpuWorkloadEntry_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 11, 1, 2, 2, 1)
)
lsTrunkCpuWorkloadEntry.setIndexNames(
    (0, "LIGHTSTREAM-MIB", "lsTrunkWorkloadCardIndex"),
    (0, "LIGHTSTREAM-MIB", "lsTrunkWorkloadTypeIndex"),
)
if mibBuilder.loadTexts:
    lsTrunkCpuWorkloadEntry.setStatus("mandatory")
_LsTrunkWorkloadCardIndex_Type = Integer32
_LsTrunkWorkloadCardIndex_Object = MibTableColumn
lsTrunkWorkloadCardIndex = _LsTrunkWorkloadCardIndex_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 11, 1, 2, 2, 1, 1),
    _LsTrunkWorkloadCardIndex_Type()
)
lsTrunkWorkloadCardIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lsTrunkWorkloadCardIndex.setStatus("mandatory")


class _LsTrunkWorkloadTypeIndex_Type(Integer32):
    """Custom type lsTrunkWorkloadTypeIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("average", 1)
    )


_LsTrunkWorkloadTypeIndex_Type.__name__ = "Integer32"
_LsTrunkWorkloadTypeIndex_Object = MibTableColumn
lsTrunkWorkloadTypeIndex = _LsTrunkWorkloadTypeIndex_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 11, 1, 2, 2, 1, 2),
    _LsTrunkWorkloadTypeIndex_Type()
)
lsTrunkWorkloadTypeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lsTrunkWorkloadTypeIndex.setStatus("mandatory")
_LsTrunkWorkloadEvents_Type = Counter32
_LsTrunkWorkloadEvents_Object = MibTableColumn
lsTrunkWorkloadEvents = _LsTrunkWorkloadEvents_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 11, 1, 2, 2, 1, 3),
    _LsTrunkWorkloadEvents_Type()
)
lsTrunkWorkloadEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lsTrunkWorkloadEvents.setStatus("mandatory")
_LsLcStatistics_ObjectIdentity = ObjectIdentity
lsLcStatistics = _LsLcStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 11, 1, 3)
)
_LcStatTable_Object = MibTable
lcStatTable = _LcStatTable_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 11, 1, 3, 1)
)
if mibBuilder.loadTexts:
    lcStatTable.setStatus("mandatory")
_LcStatEntry_Object = MibTableRow
lcStatEntry = _LcStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 11, 1, 3, 1, 1)
)
lcStatEntry.setIndexNames(
    (0, "LIGHTSTREAM-MIB", "lcStatCardIndex"),
)
if mibBuilder.loadTexts:
    lcStatEntry.setStatus("mandatory")
_LcStatCardIndex_Type = Integer32
_LcStatCardIndex_Object = MibTableColumn
lcStatCardIndex = _LcStatCardIndex_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 11, 1, 3, 1, 1, 1),
    _LcStatCardIndex_Type()
)
lcStatCardIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcStatCardIndex.setStatus("mandatory")
_TsuFreeCells_Type = Gauge32
_TsuFreeCells_Object = MibTableColumn
tsuFreeCells = _TsuFreeCells_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 11, 1, 3, 1, 1, 2),
    _TsuFreeCells_Type()
)
tsuFreeCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsuFreeCells.setStatus("mandatory")
_FsuSharedFreeCells_Type = Integer32
_FsuSharedFreeCells_Object = MibTableColumn
fsuSharedFreeCells = _FsuSharedFreeCells_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 11, 1, 3, 1, 1, 3),
    _FsuSharedFreeCells_Type()
)
fsuSharedFreeCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsuSharedFreeCells.setStatus("mandatory")
_TsuCellDropLastVci_Type = Integer32
_TsuCellDropLastVci_Object = MibTableColumn
tsuCellDropLastVci = _TsuCellDropLastVci_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 11, 1, 3, 1, 1, 4),
    _TsuCellDropLastVci_Type()
)
tsuCellDropLastVci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsuCellDropLastVci.setStatus("mandatory")
_SwitchCellDgRejectEvents_Type = Counter32
_SwitchCellDgRejectEvents_Object = MibTableColumn
switchCellDgRejectEvents = _SwitchCellDgRejectEvents_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 11, 1, 3, 1, 1, 5),
    _SwitchCellDgRejectEvents_Type()
)
switchCellDgRejectEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchCellDgRejectEvents.setStatus("mandatory")
_SwitchCellSchedRejectEvents_Type = Counter32
_SwitchCellSchedRejectEvents_Object = MibTableColumn
switchCellSchedRejectEvents = _SwitchCellSchedRejectEvents_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 11, 1, 3, 1, 1, 6),
    _SwitchCellSchedRejectEvents_Type()
)
switchCellSchedRejectEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchCellSchedRejectEvents.setStatus("mandatory")
_TsuErrFutQCellDrops_Type = Counter32
_TsuErrFutQCellDrops_Object = MibTableColumn
tsuErrFutQCellDrops = _TsuErrFutQCellDrops_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 11, 1, 3, 1, 1, 7),
    _TsuErrFutQCellDrops_Type()
)
tsuErrFutQCellDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsuErrFutQCellDrops.setStatus("mandatory")
_TsuErrFutQMsgDropLastVci_Type = Integer32
_TsuErrFutQMsgDropLastVci_Object = MibTableColumn
tsuErrFutQMsgDropLastVci = _TsuErrFutQMsgDropLastVci_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 11, 1, 3, 1, 1, 8),
    _TsuErrFutQMsgDropLastVci_Type()
)
tsuErrFutQMsgDropLastVci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsuErrFutQMsgDropLastVci.setStatus("mandatory")
_FsuHdrLrcErrs_Type = Counter32
_FsuHdrLrcErrs_Object = MibTableColumn
fsuHdrLrcErrs = _FsuHdrLrcErrs_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 11, 1, 3, 1, 1, 9),
    _FsuHdrLrcErrs_Type()
)
fsuHdrLrcErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsuHdrLrcErrs.setStatus("mandatory")
_FsuPayloadLrcErrs_Type = Counter32
_FsuPayloadLrcErrs_Object = MibTableColumn
fsuPayloadLrcErrs = _FsuPayloadLrcErrs_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 11, 1, 3, 1, 1, 10),
    _FsuPayloadLrcErrs_Type()
)
fsuPayloadLrcErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsuPayloadLrcErrs.setStatus("mandatory")
_LcPortStatTable_Object = MibTable
lcPortStatTable = _LcPortStatTable_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 11, 1, 3, 2)
)
if mibBuilder.loadTexts:
    lcPortStatTable.setStatus("mandatory")
_LcPortStatEntry_Object = MibTableRow
lcPortStatEntry = _LcPortStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 11, 1, 3, 2, 1)
)
lcPortStatEntry.setIndexNames(
    (0, "LIGHTSTREAM-MIB", "lcStatPortIndex"),
)
if mibBuilder.loadTexts:
    lcPortStatEntry.setStatus("mandatory")
_LcStatPortIndex_Type = Integer32
_LcStatPortIndex_Object = MibTableColumn
lcStatPortIndex = _LcStatPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 11, 1, 3, 2, 1, 1),
    _LcStatPortIndex_Type()
)
lcStatPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcStatPortIndex.setStatus("mandatory")
_FsuPortFreeCells_Type = Gauge32
_FsuPortFreeCells_Object = MibTableColumn
fsuPortFreeCells = _FsuPortFreeCells_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 11, 1, 3, 2, 1, 2),
    _FsuPortFreeCells_Type()
)
fsuPortFreeCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsuPortFreeCells.setStatus("mandatory")
_FsuCellDropLastCellHdr_Type = Integer32
_FsuCellDropLastCellHdr_Object = MibTableColumn
fsuCellDropLastCellHdr = _FsuCellDropLastCellHdr_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 11, 1, 3, 2, 1, 3),
    _FsuCellDropLastCellHdr_Type()
)
fsuCellDropLastCellHdr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsuCellDropLastCellHdr.setStatus("mandatory")
_TsuPortErrL1UnconfigVcis_Type = Counter32
_TsuPortErrL1UnconfigVcis_Object = MibTableColumn
tsuPortErrL1UnconfigVcis = _TsuPortErrL1UnconfigVcis_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 11, 1, 3, 2, 1, 4),
    _TsuPortErrL1UnconfigVcis_Type()
)
tsuPortErrL1UnconfigVcis.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsuPortErrL1UnconfigVcis.setStatus("mandatory")
_TsuPortErrL2UnconfigVcis_Type = Counter32
_TsuPortErrL2UnconfigVcis_Object = MibTableColumn
tsuPortErrL2UnconfigVcis = _TsuPortErrL2UnconfigVcis_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 11, 1, 3, 2, 1, 5),
    _TsuPortErrL2UnconfigVcis_Type()
)
tsuPortErrL2UnconfigVcis.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsuPortErrL2UnconfigVcis.setStatus("mandatory")
_TsuPortErrL1UnconfigLastVci_Type = Integer32
_TsuPortErrL1UnconfigLastVci_Object = MibTableColumn
tsuPortErrL1UnconfigLastVci = _TsuPortErrL1UnconfigLastVci_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 11, 1, 3, 2, 1, 6),
    _TsuPortErrL1UnconfigLastVci_Type()
)
tsuPortErrL1UnconfigLastVci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsuPortErrL1UnconfigLastVci.setStatus("mandatory")
_TsuPortErrL2UnconfigLastVci_Type = Integer32
_TsuPortErrL2UnconfigLastVci_Object = MibTableColumn
tsuPortErrL2UnconfigLastVci = _TsuPortErrL2UnconfigLastVci_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 11, 1, 3, 2, 1, 7),
    _TsuPortErrL2UnconfigLastVci_Type()
)
tsuPortErrL2UnconfigLastVci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsuPortErrL2UnconfigLastVci.setStatus("mandatory")
_TsuPortErrNonZeroGfc_Type = Counter32
_TsuPortErrNonZeroGfc_Object = MibTableColumn
tsuPortErrNonZeroGfc = _TsuPortErrNonZeroGfc_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 11, 1, 3, 2, 1, 8),
    _TsuPortErrNonZeroGfc_Type()
)
tsuPortErrNonZeroGfc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsuPortErrNonZeroGfc.setStatus("mandatory")
_FsuPortXmtCellsTable_Object = MibTable
fsuPortXmtCellsTable = _FsuPortXmtCellsTable_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 11, 1, 3, 3)
)
if mibBuilder.loadTexts:
    fsuPortXmtCellsTable.setStatus("mandatory")
_FsuPortXmtCellsEntry_Object = MibTableRow
fsuPortXmtCellsEntry = _FsuPortXmtCellsEntry_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 11, 1, 3, 3, 1)
)
fsuPortXmtCellsEntry.setIndexNames(
    (0, "LIGHTSTREAM-MIB", "fsuXmtCellsPortIndex"),
    (0, "LIGHTSTREAM-MIB", "fsuXmtCellsPriorityIndex"),
)
if mibBuilder.loadTexts:
    fsuPortXmtCellsEntry.setStatus("mandatory")
_FsuXmtCellsPortIndex_Type = Integer32
_FsuXmtCellsPortIndex_Object = MibTableColumn
fsuXmtCellsPortIndex = _FsuXmtCellsPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 11, 1, 3, 3, 1, 1),
    _FsuXmtCellsPortIndex_Type()
)
fsuXmtCellsPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsuXmtCellsPortIndex.setStatus("mandatory")


class _FsuXmtCellsPriorityIndex_Type(Integer32):
    """Custom type fsuXmtCellsPriorityIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_FsuXmtCellsPriorityIndex_Type.__name__ = "Integer32"
_FsuXmtCellsPriorityIndex_Object = MibTableColumn
fsuXmtCellsPriorityIndex = _FsuXmtCellsPriorityIndex_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 11, 1, 3, 3, 1, 2),
    _FsuXmtCellsPriorityIndex_Type()
)
fsuXmtCellsPriorityIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsuXmtCellsPriorityIndex.setStatus("mandatory")
_FsuXmtCellEvents_Type = Counter32
_FsuXmtCellEvents_Object = MibTableColumn
fsuXmtCellEvents = _FsuXmtCellEvents_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 11, 1, 3, 3, 1, 3),
    _FsuXmtCellEvents_Type()
)
fsuXmtCellEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsuXmtCellEvents.setStatus("mandatory")
_FsuQueueCellLengthTable_Object = MibTable
fsuQueueCellLengthTable = _FsuQueueCellLengthTable_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 11, 1, 3, 4)
)
if mibBuilder.loadTexts:
    fsuQueueCellLengthTable.setStatus("mandatory")
_FsuQueueCellLenEntry_Object = MibTableRow
fsuQueueCellLenEntry = _FsuQueueCellLenEntry_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 11, 1, 3, 4, 1)
)
fsuQueueCellLenEntry.setIndexNames(
    (0, "LIGHTSTREAM-MIB", "fsuQueueCellLenPortIndex"),
    (0, "LIGHTSTREAM-MIB", "fsuQueueCellLenSubQIndex"),
)
if mibBuilder.loadTexts:
    fsuQueueCellLenEntry.setStatus("mandatory")
_FsuQueueCellLenPortIndex_Type = Integer32
_FsuQueueCellLenPortIndex_Object = MibTableColumn
fsuQueueCellLenPortIndex = _FsuQueueCellLenPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 11, 1, 3, 4, 1, 1),
    _FsuQueueCellLenPortIndex_Type()
)
fsuQueueCellLenPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsuQueueCellLenPortIndex.setStatus("mandatory")


class _FsuQueueCellLenSubQIndex_Type(Integer32):
    """Custom type fsuQueueCellLenSubQIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_FsuQueueCellLenSubQIndex_Type.__name__ = "Integer32"
_FsuQueueCellLenSubQIndex_Object = MibTableColumn
fsuQueueCellLenSubQIndex = _FsuQueueCellLenSubQIndex_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 11, 1, 3, 4, 1, 2),
    _FsuQueueCellLenSubQIndex_Type()
)
fsuQueueCellLenSubQIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsuQueueCellLenSubQIndex.setStatus("mandatory")
_FsuQueueCellLength_Type = Gauge32
_FsuQueueCellLength_Object = MibTableColumn
fsuQueueCellLength = _FsuQueueCellLength_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 11, 1, 3, 4, 1, 3),
    _FsuQueueCellLength_Type()
)
fsuQueueCellLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsuQueueCellLength.setStatus("mandatory")
_FsuDropEventTable_Object = MibTable
fsuDropEventTable = _FsuDropEventTable_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 11, 1, 3, 5)
)
if mibBuilder.loadTexts:
    fsuDropEventTable.setStatus("mandatory")
_FsuDropEventEntry_Object = MibTableRow
fsuDropEventEntry = _FsuDropEventEntry_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 11, 1, 3, 5, 1)
)
fsuDropEventEntry.setIndexNames(
    (0, "LIGHTSTREAM-MIB", "fsuDropEventPortIndex"),
    (0, "LIGHTSTREAM-MIB", "fsuDropEventWatermarkIndex"),
)
if mibBuilder.loadTexts:
    fsuDropEventEntry.setStatus("mandatory")
_FsuDropEventPortIndex_Type = Integer32
_FsuDropEventPortIndex_Object = MibTableColumn
fsuDropEventPortIndex = _FsuDropEventPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 11, 1, 3, 5, 1, 1),
    _FsuDropEventPortIndex_Type()
)
fsuDropEventPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsuDropEventPortIndex.setStatus("mandatory")
_FsuDropEventWatermarkIndex_Type = Integer32
_FsuDropEventWatermarkIndex_Object = MibTableColumn
fsuDropEventWatermarkIndex = _FsuDropEventWatermarkIndex_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 11, 1, 3, 5, 1, 2),
    _FsuDropEventWatermarkIndex_Type()
)
fsuDropEventWatermarkIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsuDropEventWatermarkIndex.setStatus("mandatory")
_FsuDropEvents_Type = Counter32
_FsuDropEvents_Object = MibTableColumn
fsuDropEvents = _FsuDropEvents_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 11, 1, 3, 5, 1, 3),
    _FsuDropEvents_Type()
)
fsuDropEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsuDropEvents.setStatus("mandatory")
_LsFsuFastDropTable_Object = MibTable
lsFsuFastDropTable = _LsFsuFastDropTable_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 11, 1, 3, 6)
)
if mibBuilder.loadTexts:
    lsFsuFastDropTable.setStatus("mandatory")
_LsFsuFastDropEntry_Object = MibTableRow
lsFsuFastDropEntry = _LsFsuFastDropEntry_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 11, 1, 3, 6, 1)
)
lsFsuFastDropEntry.setIndexNames(
    (0, "LIGHTSTREAM-MIB", "lsFsuFastDropWatermarkIndex"),
)
if mibBuilder.loadTexts:
    lsFsuFastDropEntry.setStatus("mandatory")


class _LsFsuFastDropWatermarkIndex_Type(Integer32):
    """Custom type lsFsuFastDropWatermarkIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("clp0HiOther", 3),
          ("clp0HiPriority", 2),
          ("clp1", 1))
    )


_LsFsuFastDropWatermarkIndex_Type.__name__ = "Integer32"
_LsFsuFastDropWatermarkIndex_Object = MibTableColumn
lsFsuFastDropWatermarkIndex = _LsFsuFastDropWatermarkIndex_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 11, 1, 3, 6, 1, 1),
    _LsFsuFastDropWatermarkIndex_Type()
)
lsFsuFastDropWatermarkIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lsFsuFastDropWatermarkIndex.setStatus("mandatory")
_LsFsuFastCellDropEvents_Type = Counter32
_LsFsuFastCellDropEvents_Object = MibTableColumn
lsFsuFastCellDropEvents = _LsFsuFastCellDropEvents_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 11, 1, 3, 6, 1, 2),
    _LsFsuFastCellDropEvents_Type()
)
lsFsuFastCellDropEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lsFsuFastCellDropEvents.setStatus("mandatory")
_TsuDropEventTable_Object = MibTable
tsuDropEventTable = _TsuDropEventTable_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 11, 1, 3, 7)
)
if mibBuilder.loadTexts:
    tsuDropEventTable.setStatus("mandatory")
_TsuDropEventEntry_Object = MibTableRow
tsuDropEventEntry = _TsuDropEventEntry_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 11, 1, 3, 7, 1)
)
tsuDropEventEntry.setIndexNames(
    (0, "LIGHTSTREAM-MIB", "tsuDropEventPortIndex"),
    (0, "LIGHTSTREAM-MIB", "tsuDropEventWatermarkIndex"),
)
if mibBuilder.loadTexts:
    tsuDropEventEntry.setStatus("mandatory")
_TsuDropEventPortIndex_Type = Integer32
_TsuDropEventPortIndex_Object = MibTableColumn
tsuDropEventPortIndex = _TsuDropEventPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 11, 1, 3, 7, 1, 1),
    _TsuDropEventPortIndex_Type()
)
tsuDropEventPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsuDropEventPortIndex.setStatus("mandatory")


class _TsuDropEventWatermarkIndex_Type(Integer32):
    """Custom type tsuDropEventWatermarkIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("control", 2),
          ("scheduled", 3),
          ("user", 1))
    )


_TsuDropEventWatermarkIndex_Type.__name__ = "Integer32"
_TsuDropEventWatermarkIndex_Object = MibTableColumn
tsuDropEventWatermarkIndex = _TsuDropEventWatermarkIndex_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 11, 1, 3, 7, 1, 2),
    _TsuDropEventWatermarkIndex_Type()
)
tsuDropEventWatermarkIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsuDropEventWatermarkIndex.setStatus("mandatory")
_TsuDropEvents_Type = Counter32
_TsuDropEvents_Object = MibTableColumn
tsuDropEvents = _TsuDropEvents_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 11, 1, 3, 7, 1, 3),
    _TsuDropEvents_Type()
)
tsuDropEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsuDropEvents.setStatus("mandatory")
_LsUtStatistics_ObjectIdentity = ObjectIdentity
lsUtStatistics = _LsUtStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 11, 1, 4)
)
_LsLcFsuIntervalTable_Object = MibTable
lsLcFsuIntervalTable = _LsLcFsuIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 11, 1, 4, 1)
)
if mibBuilder.loadTexts:
    lsLcFsuIntervalTable.setStatus("mandatory")
_LsLcFsuIntervalEntry_Object = MibTableRow
lsLcFsuIntervalEntry = _LsLcFsuIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 11, 1, 4, 1, 1)
)
lsLcFsuIntervalEntry.setIndexNames(
    (0, "LIGHTSTREAM-MIB", "lsLcIntervalPortIndex"),
    (0, "LIGHTSTREAM-MIB", "lsLcIntervalNumber"),
)
if mibBuilder.loadTexts:
    lsLcFsuIntervalEntry.setStatus("mandatory")
_LsLcIntervalPortIndex_Type = Integer32
_LsLcIntervalPortIndex_Object = MibTableColumn
lsLcIntervalPortIndex = _LsLcIntervalPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 11, 1, 4, 1, 1, 1),
    _LsLcIntervalPortIndex_Type()
)
lsLcIntervalPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lsLcIntervalPortIndex.setStatus("mandatory")


class _LsLcIntervalNumber_Type(Integer32):
    """Custom type lsLcIntervalNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_LsLcIntervalNumber_Type.__name__ = "Integer32"
_LsLcIntervalNumber_Object = MibTableColumn
lsLcIntervalNumber = _LsLcIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 11, 1, 4, 1, 1, 2),
    _LsLcIntervalNumber_Type()
)
lsLcIntervalNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lsLcIntervalNumber.setStatus("mandatory")
_LsLcIntervalPSDepth_Type = Integer32
_LsLcIntervalPSDepth_Object = MibTableColumn
lsLcIntervalPSDepth = _LsLcIntervalPSDepth_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 11, 1, 4, 1, 1, 3),
    _LsLcIntervalPSDepth_Type()
)
lsLcIntervalPSDepth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lsLcIntervalPSDepth.setStatus("mandatory")
_LsLcIntervalASDepth_Type = Integer32
_LsLcIntervalASDepth_Object = MibTableColumn
lsLcIntervalASDepth = _LsLcIntervalASDepth_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 11, 1, 4, 1, 1, 4),
    _LsLcIntervalASDepth_Type()
)
lsLcIntervalASDepth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lsLcIntervalASDepth.setStatus("mandatory")
_LsLcIntervalDropEvents_Type = Integer32
_LsLcIntervalDropEvents_Object = MibTableColumn
lsLcIntervalDropEvents = _LsLcIntervalDropEvents_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 11, 1, 4, 1, 1, 5),
    _LsLcIntervalDropEvents_Type()
)
lsLcIntervalDropEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lsLcIntervalDropEvents.setStatus("mandatory")
_LsLcIntervalAvgCells_Type = Integer32
_LsLcIntervalAvgCells_Object = MibTableColumn
lsLcIntervalAvgCells = _LsLcIntervalAvgCells_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 11, 1, 4, 1, 1, 6),
    _LsLcIntervalAvgCells_Type()
)
lsLcIntervalAvgCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lsLcIntervalAvgCells.setStatus("mandatory")
_LsLcIntervalPeakCells_Type = Integer32
_LsLcIntervalPeakCells_Object = MibTableColumn
lsLcIntervalPeakCells = _LsLcIntervalPeakCells_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 11, 1, 4, 1, 1, 7),
    _LsLcIntervalPeakCells_Type()
)
lsLcIntervalPeakCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lsLcIntervalPeakCells.setStatus("mandatory")
_LsLcIntervalMinPermits_Type = Integer32
_LsLcIntervalMinPermits_Object = MibTableColumn
lsLcIntervalMinPermits = _LsLcIntervalMinPermits_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 11, 1, 4, 1, 1, 8),
    _LsLcIntervalMinPermits_Type()
)
lsLcIntervalMinPermits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lsLcIntervalMinPermits.setStatus("mandatory")
_LsLcIntervalAvgPermits_Type = Integer32
_LsLcIntervalAvgPermits_Object = MibTableColumn
lsLcIntervalAvgPermits = _LsLcIntervalAvgPermits_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 11, 1, 4, 1, 1, 9),
    _LsLcIntervalAvgPermits_Type()
)
lsLcIntervalAvgPermits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lsLcIntervalAvgPermits.setStatus("mandatory")
_LsLcIntervalMaxPermits_Type = Integer32
_LsLcIntervalMaxPermits_Object = MibTableColumn
lsLcIntervalMaxPermits = _LsLcIntervalMaxPermits_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 11, 1, 4, 1, 1, 10),
    _LsLcIntervalMaxPermits_Type()
)
lsLcIntervalMaxPermits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lsLcIntervalMaxPermits.setStatus("mandatory")
_LsLcIntervalDecrPermits_Type = Integer32
_LsLcIntervalDecrPermits_Object = MibTableColumn
lsLcIntervalDecrPermits = _LsLcIntervalDecrPermits_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 11, 1, 4, 1, 1, 11),
    _LsLcIntervalDecrPermits_Type()
)
lsLcIntervalDecrPermits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lsLcIntervalDecrPermits.setStatus("mandatory")
_LsLcIntervalIncrPermits_Type = Integer32
_LsLcIntervalIncrPermits_Object = MibTableColumn
lsLcIntervalIncrPermits = _LsLcIntervalIncrPermits_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 11, 1, 4, 1, 1, 12),
    _LsLcIntervalIncrPermits_Type()
)
lsLcIntervalIncrPermits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lsLcIntervalIncrPermits.setStatus("mandatory")
_LsLcIntervalMinBwAlloc_Type = Integer32
_LsLcIntervalMinBwAlloc_Object = MibTableColumn
lsLcIntervalMinBwAlloc = _LsLcIntervalMinBwAlloc_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 11, 1, 4, 1, 1, 13),
    _LsLcIntervalMinBwAlloc_Type()
)
lsLcIntervalMinBwAlloc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lsLcIntervalMinBwAlloc.setStatus("mandatory")
_LsLcIntervalAvgBwAlloc_Type = Integer32
_LsLcIntervalAvgBwAlloc_Object = MibTableColumn
lsLcIntervalAvgBwAlloc = _LsLcIntervalAvgBwAlloc_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 11, 1, 4, 1, 1, 14),
    _LsLcIntervalAvgBwAlloc_Type()
)
lsLcIntervalAvgBwAlloc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lsLcIntervalAvgBwAlloc.setStatus("mandatory")
_LsLcIntervalMaxBwAlloc_Type = Integer32
_LsLcIntervalMaxBwAlloc_Object = MibTableColumn
lsLcIntervalMaxBwAlloc = _LsLcIntervalMaxBwAlloc_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 11, 1, 4, 1, 1, 15),
    _LsLcIntervalMaxBwAlloc_Type()
)
lsLcIntervalMaxBwAlloc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lsLcIntervalMaxBwAlloc.setStatus("mandatory")
_LsNpStatistics_ObjectIdentity = ObjectIdentity
lsNpStatistics = _LsNpStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 11, 1, 5)
)
_LsNpCpuWorkloadTable_Object = MibTable
lsNpCpuWorkloadTable = _LsNpCpuWorkloadTable_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 11, 1, 5, 1)
)
if mibBuilder.loadTexts:
    lsNpCpuWorkloadTable.setStatus("mandatory")
_LsNpCpuWorkloadEntry_Object = MibTableRow
lsNpCpuWorkloadEntry = _LsNpCpuWorkloadEntry_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 11, 1, 5, 1, 1)
)
lsNpCpuWorkloadEntry.setIndexNames(
    (0, "LIGHTSTREAM-MIB", "lsNpCpuWorkloadIndex"),
)
if mibBuilder.loadTexts:
    lsNpCpuWorkloadEntry.setStatus("mandatory")
_LsNpCpuWorkloadIndex_Type = Integer32
_LsNpCpuWorkloadIndex_Object = MibTableColumn
lsNpCpuWorkloadIndex = _LsNpCpuWorkloadIndex_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 11, 1, 5, 1, 1, 1),
    _LsNpCpuWorkloadIndex_Type()
)
lsNpCpuWorkloadIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lsNpCpuWorkloadIndex.setStatus("mandatory")
_LsNpCpuWorkloadEvents_Type = Counter32
_LsNpCpuWorkloadEvents_Object = MibTableColumn
lsNpCpuWorkloadEvents = _LsNpCpuWorkloadEvents_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 11, 1, 5, 1, 1, 2),
    _LsNpCpuWorkloadEvents_Type()
)
lsNpCpuWorkloadEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lsNpCpuWorkloadEvents.setStatus("mandatory")
_LsCellStatistics_ObjectIdentity = ObjectIdentity
lsCellStatistics = _LsCellStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 11, 1, 6)
)
_LsCellVciStatTable_Object = MibTable
lsCellVciStatTable = _LsCellVciStatTable_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 11, 1, 6, 1)
)
if mibBuilder.loadTexts:
    lsCellVciStatTable.setStatus("mandatory")
_LsCellVciStatEntry_Object = MibTableRow
lsCellVciStatEntry = _LsCellVciStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 11, 1, 6, 1, 1)
)
lsCellVciStatEntry.setIndexNames(
    (0, "LIGHTSTREAM-MIB", "cellVciStatPortIndex"),
    (0, "LIGHTSTREAM-MIB", "cellVciStatVciIndex"),
)
if mibBuilder.loadTexts:
    lsCellVciStatEntry.setStatus("mandatory")
_CellVciStatPortIndex_Type = Integer32
_CellVciStatPortIndex_Object = MibTableColumn
cellVciStatPortIndex = _CellVciStatPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 11, 1, 6, 1, 1, 1),
    _CellVciStatPortIndex_Type()
)
cellVciStatPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cellVciStatPortIndex.setStatus("mandatory")
_CellVciStatVciIndex_Type = Integer32
_CellVciStatVciIndex_Object = MibTableColumn
cellVciStatVciIndex = _CellVciStatVciIndex_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 11, 1, 6, 1, 1, 2),
    _CellVciStatVciIndex_Type()
)
cellVciStatVciIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cellVciStatVciIndex.setStatus("mandatory")
_CellVciToSwCLP0Cells_Type = Counter32
_CellVciToSwCLP0Cells_Object = MibTableColumn
cellVciToSwCLP0Cells = _CellVciToSwCLP0Cells_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 11, 1, 6, 1, 1, 3),
    _CellVciToSwCLP0Cells_Type()
)
cellVciToSwCLP0Cells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cellVciToSwCLP0Cells.setStatus("mandatory")
_CellVciToSwCLP01Cells_Type = Counter32
_CellVciToSwCLP01Cells_Object = MibTableColumn
cellVciToSwCLP01Cells = _CellVciToSwCLP01Cells_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 11, 1, 6, 1, 1, 4),
    _CellVciToSwCLP01Cells_Type()
)
cellVciToSwCLP01Cells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cellVciToSwCLP01Cells.setStatus("mandatory")
_CellVciToSwCLP1Cells_Type = Counter32
_CellVciToSwCLP1Cells_Object = MibTableColumn
cellVciToSwCLP1Cells = _CellVciToSwCLP1Cells_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 11, 1, 6, 1, 1, 5),
    _CellVciToSwCLP1Cells_Type()
)
cellVciToSwCLP1Cells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cellVciToSwCLP1Cells.setStatus("mandatory")
_CellVciToSwDiscardCells_Type = Counter32
_CellVciToSwDiscardCells_Object = MibTableColumn
cellVciToSwDiscardCells = _CellVciToSwDiscardCells_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 11, 1, 6, 1, 1, 6),
    _CellVciToSwDiscardCells_Type()
)
cellVciToSwDiscardCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cellVciToSwDiscardCells.setStatus("mandatory")
_LsIR_ObjectIdentity = ObjectIdentity
lsIR = _LsIR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 12)
)
_IrRoutingGroup_ObjectIdentity = ObjectIdentity
irRoutingGroup = _IrRoutingGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 12, 1)
)
_IrRoutingPathsGenerated_Type = Counter32
_IrRoutingPathsGenerated_Object = MibScalar
irRoutingPathsGenerated = _IrRoutingPathsGenerated_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 12, 1, 1),
    _IrRoutingPathsGenerated_Type()
)
irRoutingPathsGenerated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    irRoutingPathsGenerated.setStatus("mandatory")
_IrRoutingPathGenSuccess_Type = Counter32
_IrRoutingPathGenSuccess_Object = MibScalar
irRoutingPathGenSuccess = _IrRoutingPathGenSuccess_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 12, 1, 2),
    _IrRoutingPathGenSuccess_Type()
)
irRoutingPathGenSuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    irRoutingPathGenSuccess.setStatus("mandatory")
_IrRoutingPathGenFailedNoResources_Type = Counter32
_IrRoutingPathGenFailedNoResources_Object = MibScalar
irRoutingPathGenFailedNoResources = _IrRoutingPathGenFailedNoResources_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 12, 1, 3),
    _IrRoutingPathGenFailedNoResources_Type()
)
irRoutingPathGenFailedNoResources.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    irRoutingPathGenFailedNoResources.setStatus("mandatory")
_IrRoutingPathGenFailedUnknown_Type = Counter32
_IrRoutingPathGenFailedUnknown_Object = MibScalar
irRoutingPathGenFailedUnknown = _IrRoutingPathGenFailedUnknown_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 12, 1, 4),
    _IrRoutingPathGenFailedUnknown_Type()
)
irRoutingPathGenFailedUnknown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    irRoutingPathGenFailedUnknown.setStatus("mandatory")
_IrRoutingPathGenFailedOther_Type = Counter32
_IrRoutingPathGenFailedOther_Object = MibScalar
irRoutingPathGenFailedOther = _IrRoutingPathGenFailedOther_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 12, 1, 5),
    _IrRoutingPathGenFailedOther_Type()
)
irRoutingPathGenFailedOther.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    irRoutingPathGenFailedOther.setStatus("mandatory")
_IrRoutingAveragePathLength_Type = Counter32
_IrRoutingAveragePathLength_Object = MibScalar
irRoutingAveragePathLength = _IrRoutingAveragePathLength_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 12, 1, 6),
    _IrRoutingAveragePathLength_Type()
)
irRoutingAveragePathLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    irRoutingAveragePathLength.setStatus("mandatory")
_LsStatistics_ObjectIdentity = ObjectIdentity
lsStatistics = _LsStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 13)
)
_TcsInfo_ObjectIdentity = ObjectIdentity
tcsInfo = _TcsInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 14)
)
_TcsTable_Object = MibTable
tcsTable = _TcsTable_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 14, 1)
)
if mibBuilder.loadTexts:
    tcsTable.setStatus("mandatory")
_TcsEntry_Object = MibTableRow
tcsEntry = _TcsEntry_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 14, 1, 1)
)
tcsEntry.setIndexNames(
    (0, "LIGHTSTREAM-MIB", "tcsIndex"),
)
if mibBuilder.loadTexts:
    tcsEntry.setStatus("mandatory")
_TcsIndex_Type = Integer32
_TcsIndex_Object = MibTableColumn
tcsIndex = _TcsIndex_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 14, 1, 1, 1),
    _TcsIndex_Type()
)
tcsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcsIndex.setStatus("mandatory")
_TcsTemp1_Type = Integer32
_TcsTemp1_Object = MibTableColumn
tcsTemp1 = _TcsTemp1_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 14, 1, 1, 2),
    _TcsTemp1_Type()
)
tcsTemp1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcsTemp1.setStatus("mandatory")
_TcsTemp2_Type = Integer32
_TcsTemp2_Object = MibTableColumn
tcsTemp2 = _TcsTemp2_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 14, 1, 1, 3),
    _TcsTemp2_Type()
)
tcsTemp2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcsTemp2.setStatus("mandatory")
_TcsTcsVoltage_Type = Integer32
_TcsTcsVoltage_Object = MibTableColumn
tcsTcsVoltage = _TcsTcsVoltage_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 14, 1, 1, 4),
    _TcsTcsVoltage_Type()
)
tcsTcsVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcsTcsVoltage.setStatus("mandatory")
_TcsVccVoltage_Type = Integer32
_TcsVccVoltage_Object = MibTableColumn
tcsVccVoltage = _TcsVccVoltage_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 14, 1, 1, 5),
    _TcsVccVoltage_Type()
)
tcsVccVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcsVccVoltage.setStatus("mandatory")
_TcsScsiVoltage_Type = Integer32
_TcsScsiVoltage_Object = MibTableColumn
tcsScsiVoltage = _TcsScsiVoltage_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 14, 1, 1, 7),
    _TcsScsiVoltage_Type()
)
tcsScsiVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcsScsiVoltage.setStatus("mandatory")


class _TcsPostResult_Type(OctetString):
    """Custom type tcsPostResult based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_TcsPostResult_Type.__name__ = "OctetString"
_TcsPostResult_Object = MibTableColumn
tcsPostResult = _TcsPostResult_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 14, 1, 1, 8),
    _TcsPostResult_Type()
)
tcsPostResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcsPostResult.setStatus("mandatory")


class _TcsCardType_Type(Integer32):
    """Custom type tcsCardType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              10,
              11,
              12,
              13,
              14,
              15,
              30,
              31,
              32,
              33,
              34,
              35,
              36,
              37,
              70)
        )
    )
    namedValues = NamedValues(
        *(("clc12oc3ac1Edge", 31),
          ("clc12oc3ac1Trunk", 32),
          ("clc12taxiac1Edge", 35),
          ("clc12taxiac1Trunk", 36),
          ("clc18t1e1cbrac1", 37),
          ("clc18t3ac1Edge", 33),
          ("clc18t3ac1Trunk", 34),
          ("clc1Gen", 30),
          ("empty", 1),
          ("error", 2),
          ("lsEdge", 6),
          ("lsTrunk", 7),
          ("msEdge", 10),
          ("msTrunk", 8),
          ("np", 5),
          ("plc12fac1", 11),
          ("plc18eac1", 12),
          ("plc18sac1Edge", 14),
          ("plc18sac1Trunk", 15),
          ("plc1Lstoken", 13),
          ("switch", 4),
          ("switch2", 70),
          ("unknown", 3))
    )


_TcsCardType_Type.__name__ = "Integer32"
_TcsCardType_Object = MibTableColumn
tcsCardType = _TcsCardType_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 14, 1, 1, 9),
    _TcsCardType_Type()
)
tcsCardType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcsCardType.setStatus("mandatory")
_TcsPaddleTemp1_Type = Integer32
_TcsPaddleTemp1_Object = MibTableColumn
tcsPaddleTemp1 = _TcsPaddleTemp1_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 14, 1, 1, 10),
    _TcsPaddleTemp1_Type()
)
tcsPaddleTemp1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcsPaddleTemp1.setStatus("mandatory")
_TcsPaddleTemp2_Type = Integer32
_TcsPaddleTemp2_Object = MibTableColumn
tcsPaddleTemp2 = _TcsPaddleTemp2_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 14, 1, 1, 11),
    _TcsPaddleTemp2_Type()
)
tcsPaddleTemp2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcsPaddleTemp2.setStatus("mandatory")
_TcsPaddleWarnTemp1_Type = Integer32
_TcsPaddleWarnTemp1_Object = MibTableColumn
tcsPaddleWarnTemp1 = _TcsPaddleWarnTemp1_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 14, 1, 1, 12),
    _TcsPaddleWarnTemp1_Type()
)
tcsPaddleWarnTemp1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcsPaddleWarnTemp1.setStatus("mandatory")
_TcsPaddleWarnTemp2_Type = Integer32
_TcsPaddleWarnTemp2_Object = MibTableColumn
tcsPaddleWarnTemp2 = _TcsPaddleWarnTemp2_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 14, 1, 1, 13),
    _TcsPaddleWarnTemp2_Type()
)
tcsPaddleWarnTemp2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcsPaddleWarnTemp2.setStatus("mandatory")
_TcsPaddleShutdownTemp1_Type = Integer32
_TcsPaddleShutdownTemp1_Object = MibTableColumn
tcsPaddleShutdownTemp1 = _TcsPaddleShutdownTemp1_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 14, 1, 1, 14),
    _TcsPaddleShutdownTemp1_Type()
)
tcsPaddleShutdownTemp1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcsPaddleShutdownTemp1.setStatus("mandatory")
_TcsPaddleShutdownTemp2_Type = Integer32
_TcsPaddleShutdownTemp2_Object = MibTableColumn
tcsPaddleShutdownTemp2 = _TcsPaddleShutdownTemp2_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 14, 1, 1, 15),
    _TcsPaddleShutdownTemp2_Type()
)
tcsPaddleShutdownTemp2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcsPaddleShutdownTemp2.setStatus("mandatory")
_TcsWarnTemp1_Type = Integer32
_TcsWarnTemp1_Object = MibTableColumn
tcsWarnTemp1 = _TcsWarnTemp1_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 14, 1, 1, 16),
    _TcsWarnTemp1_Type()
)
tcsWarnTemp1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcsWarnTemp1.setStatus("mandatory")
_TcsWarnTemp2_Type = Integer32
_TcsWarnTemp2_Object = MibTableColumn
tcsWarnTemp2 = _TcsWarnTemp2_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 14, 1, 1, 17),
    _TcsWarnTemp2_Type()
)
tcsWarnTemp2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcsWarnTemp2.setStatus("mandatory")
_TcsShutdownTemp1_Type = Integer32
_TcsShutdownTemp1_Object = MibTableColumn
tcsShutdownTemp1 = _TcsShutdownTemp1_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 14, 1, 1, 18),
    _TcsShutdownTemp1_Type()
)
tcsShutdownTemp1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcsShutdownTemp1.setStatus("mandatory")
_TcsShutdownTemp2_Type = Integer32
_TcsShutdownTemp2_Object = MibTableColumn
tcsShutdownTemp2 = _TcsShutdownTemp2_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 14, 1, 1, 19),
    _TcsShutdownTemp2_Type()
)
tcsShutdownTemp2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcsShutdownTemp2.setStatus("mandatory")


class _TcsFaultLight_Type(Integer32):
    """Custom type tcsFaultLight based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_TcsFaultLight_Type.__name__ = "Integer32"
_TcsFaultLight_Object = MibTableColumn
tcsFaultLight = _TcsFaultLight_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 14, 1, 1, 20),
    _TcsFaultLight_Type()
)
tcsFaultLight.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcsFaultLight.setStatus("mandatory")


class _TcsReadyLight_Type(Integer32):
    """Custom type tcsReadyLight based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_TcsReadyLight_Type.__name__ = "Integer32"
_TcsReadyLight_Object = MibTableColumn
tcsReadyLight = _TcsReadyLight_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 14, 1, 1, 21),
    _TcsReadyLight_Type()
)
tcsReadyLight.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcsReadyLight.setStatus("mandatory")
_TcsSwitchConnectivityMask_Type = Integer32
_TcsSwitchConnectivityMask_Object = MibTableColumn
tcsSwitchConnectivityMask = _TcsSwitchConnectivityMask_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 14, 1, 1, 22),
    _TcsSwitchConnectivityMask_Type()
)
tcsSwitchConnectivityMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcsSwitchConnectivityMask.setStatus("mandatory")


class _TcsPrimarySwitch_Type(Integer32):
    """Custom type tcsPrimarySwitch based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("switchA", 1),
          ("switchB", 2))
    )


_TcsPrimarySwitch_Type.__name__ = "Integer32"
_TcsPrimarySwitch_Object = MibScalar
tcsPrimarySwitch = _TcsPrimarySwitch_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 14, 2),
    _TcsPrimarySwitch_Type()
)
tcsPrimarySwitch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tcsPrimarySwitch.setStatus("mandatory")


class _TcsPowerSupplyA_Type(Integer32):
    """Custom type tcsPowerSupplyA based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("empty", 1),
          ("failed", 2),
          ("good", 3))
    )


_TcsPowerSupplyA_Type.__name__ = "Integer32"
_TcsPowerSupplyA_Object = MibScalar
tcsPowerSupplyA = _TcsPowerSupplyA_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 14, 3),
    _TcsPowerSupplyA_Type()
)
tcsPowerSupplyA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcsPowerSupplyA.setStatus("mandatory")


class _TcsPowerSupplyB_Type(Integer32):
    """Custom type tcsPowerSupplyB based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("empty", 1),
          ("failed", 2),
          ("good", 3))
    )


_TcsPowerSupplyB_Type.__name__ = "Integer32"
_TcsPowerSupplyB_Object = MibScalar
tcsPowerSupplyB = _TcsPowerSupplyB_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 14, 4),
    _TcsPowerSupplyB_Type()
)
tcsPowerSupplyB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcsPowerSupplyB.setStatus("mandatory")


class _TcsPowerSupplyTypeA_Type(Integer32):
    """Custom type tcsPowerSupplyTypeA based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("dcPowerTray", 2),
          ("empty", 1),
          ("toddPS", 3),
          ("unknown", 4))
    )


_TcsPowerSupplyTypeA_Type.__name__ = "Integer32"
_TcsPowerSupplyTypeA_Object = MibScalar
tcsPowerSupplyTypeA = _TcsPowerSupplyTypeA_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 14, 5),
    _TcsPowerSupplyTypeA_Type()
)
tcsPowerSupplyTypeA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcsPowerSupplyTypeA.setStatus("mandatory")


class _TcsPowerSupplyTypeB_Type(Integer32):
    """Custom type tcsPowerSupplyTypeB based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("dcPowerTray", 2),
          ("empty", 1),
          ("toddPS", 3),
          ("unknown", 4))
    )


_TcsPowerSupplyTypeB_Type.__name__ = "Integer32"
_TcsPowerSupplyTypeB_Object = MibScalar
tcsPowerSupplyTypeB = _TcsPowerSupplyTypeB_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 14, 6),
    _TcsPowerSupplyTypeB_Type()
)
tcsPowerSupplyTypeB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcsPowerSupplyTypeB.setStatus("mandatory")
_TcsSwitchFaultMaskA_Type = Integer32
_TcsSwitchFaultMaskA_Object = MibScalar
tcsSwitchFaultMaskA = _TcsSwitchFaultMaskA_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 14, 7),
    _TcsSwitchFaultMaskA_Type()
)
tcsSwitchFaultMaskA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcsSwitchFaultMaskA.setStatus("mandatory")
_TcsSwitchFaultMaskB_Type = Integer32
_TcsSwitchFaultMaskB_Object = MibScalar
tcsSwitchFaultMaskB = _TcsSwitchFaultMaskB_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 14, 8),
    _TcsSwitchFaultMaskB_Type()
)
tcsSwitchFaultMaskB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcsSwitchFaultMaskB.setStatus("mandatory")


class _TcsSwitchCutoverSupport_Type(Integer32):
    """Custom type tcsSwitchCutoverSupport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("cantDoLossLess", 3),
          ("willDoLossLess", 1),
          ("wontDoLossLess", 2))
    )


_TcsSwitchCutoverSupport_Type.__name__ = "Integer32"
_TcsSwitchCutoverSupport_Object = MibScalar
tcsSwitchCutoverSupport = _TcsSwitchCutoverSupport_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 14, 9),
    _TcsSwitchCutoverSupport_Type()
)
tcsSwitchCutoverSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcsSwitchCutoverSupport.setStatus("mandatory")
_TcsFCPrimarySwitchA_Type = Integer32
_TcsFCPrimarySwitchA_Object = MibScalar
tcsFCPrimarySwitchA = _TcsFCPrimarySwitchA_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 14, 10),
    _TcsFCPrimarySwitchA_Type()
)
tcsFCPrimarySwitchA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcsFCPrimarySwitchA.setStatus("mandatory")
_TcsFCPrimarySwitchB_Type = Integer32
_TcsFCPrimarySwitchB_Object = MibScalar
tcsFCPrimarySwitchB = _TcsFCPrimarySwitchB_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 14, 11),
    _TcsFCPrimarySwitchB_Type()
)
tcsFCPrimarySwitchB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcsFCPrimarySwitchB.setStatus("mandatory")
_LsGID_ObjectIdentity = ObjectIdentity
lsGID = _LsGID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 15)
)
_GidGeneralGroup_ObjectIdentity = ObjectIdentity
gidGeneralGroup = _GidGeneralGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 15, 1)
)
_GidSoftwareVersionNumber_Type = DisplayString
_GidSoftwareVersionNumber_Object = MibScalar
gidSoftwareVersionNumber = _GidSoftwareVersionNumber_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 15, 1, 1),
    _GidSoftwareVersionNumber_Type()
)
gidSoftwareVersionNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gidSoftwareVersionNumber.setStatus("mandatory")
_GidProcessID_Type = Integer32
_GidProcessID_Object = MibScalar
gidProcessID = _GidProcessID_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 15, 1, 2),
    _GidProcessID_Type()
)
gidProcessID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gidProcessID.setStatus("mandatory")
_GidUpTime_Type = Integer32
_GidUpTime_Object = MibScalar
gidUpTime = _GidUpTime_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 15, 1, 3),
    _GidUpTime_Type()
)
gidUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gidUpTime.setStatus("mandatory")
_GidMemoryUse_Type = Counter32
_GidMemoryUse_Object = MibScalar
gidMemoryUse = _GidMemoryUse_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 15, 1, 4),
    _GidMemoryUse_Type()
)
gidMemoryUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gidMemoryUse.setStatus("mandatory")
_GidTimersProcessed_Type = Counter32
_GidTimersProcessed_Object = MibScalar
gidTimersProcessed = _GidTimersProcessed_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 15, 1, 5),
    _GidTimersProcessed_Type()
)
gidTimersProcessed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gidTimersProcessed.setStatus("mandatory")
_GidMallocFailures_Type = Counter32
_GidMallocFailures_Object = MibScalar
gidMallocFailures = _GidMallocFailures_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 15, 1, 6),
    _GidMallocFailures_Type()
)
gidMallocFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gidMallocFailures.setStatus("mandatory")
_GidDebugFlag_Type = Integer32
_GidDebugFlag_Object = MibScalar
gidDebugFlag = _GidDebugFlag_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 15, 1, 7),
    _GidDebugFlag_Type()
)
gidDebugFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gidDebugFlag.setStatus("mandatory")
_GidDebugLevel_Type = Integer32
_GidDebugLevel_Object = MibScalar
gidDebugLevel = _GidDebugLevel_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 15, 1, 8),
    _GidDebugLevel_Type()
)
gidDebugLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gidDebugLevel.setStatus("mandatory")
_GidAcceptedBcastRateIn_Type = Integer32
_GidAcceptedBcastRateIn_Object = MibScalar
gidAcceptedBcastRateIn = _GidAcceptedBcastRateIn_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 15, 1, 9),
    _GidAcceptedBcastRateIn_Type()
)
gidAcceptedBcastRateIn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gidAcceptedBcastRateIn.setStatus("mandatory")
_GidNbrGroup_ObjectIdentity = ObjectIdentity
gidNbrGroup = _GidNbrGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 15, 2)
)
_GidNbrCount_Type = Counter32
_GidNbrCount_Object = MibScalar
gidNbrCount = _GidNbrCount_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 15, 2, 1),
    _GidNbrCount_Type()
)
gidNbrCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gidNbrCount.setStatus("mandatory")
_GidNbrTable_Object = MibTable
gidNbrTable = _GidNbrTable_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 15, 2, 2)
)
if mibBuilder.loadTexts:
    gidNbrTable.setStatus("mandatory")
_GidNbrEntry_Object = MibTableRow
gidNbrEntry = _GidNbrEntry_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 15, 2, 2, 1)
)
gidNbrEntry.setIndexNames(
    (0, "LIGHTSTREAM-MIB", "gidNbrEIA"),
)
if mibBuilder.loadTexts:
    gidNbrEntry.setStatus("mandatory")
_GidNbrEIA_Type = Integer32
_GidNbrEIA_Object = MibTableColumn
gidNbrEIA = _GidNbrEIA_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 15, 2, 2, 1, 1),
    _GidNbrEIA_Type()
)
gidNbrEIA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gidNbrEIA.setStatus("mandatory")
_GidNbrVCI_Type = Integer32
_GidNbrVCI_Object = MibTableColumn
gidNbrVCI = _GidNbrVCI_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 15, 2, 2, 1, 2),
    _GidNbrVCI_Type()
)
gidNbrVCI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gidNbrVCI.setStatus("mandatory")


class _GidNbrState_Type(Integer32):
    """Custom type gidNbrState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("exchange", 4),
          ("existent", 2),
          ("exstart", 3),
          ("full", 6),
          ("loading", 5),
          ("unknown", 1))
    )


_GidNbrState_Type.__name__ = "Integer32"
_GidNbrState_Object = MibTableColumn
gidNbrState = _GidNbrState_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 15, 2, 2, 1, 3),
    _GidNbrState_Type()
)
gidNbrState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gidNbrState.setStatus("mandatory")
_GidNbrSyncEvents_Type = Counter32
_GidNbrSyncEvents_Object = MibTableColumn
gidNbrSyncEvents = _GidNbrSyncEvents_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 15, 2, 2, 1, 4),
    _GidNbrSyncEvents_Type()
)
gidNbrSyncEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gidNbrSyncEvents.setStatus("mandatory")
_GidNbrDBReqListLength_Type = Counter32
_GidNbrDBReqListLength_Object = MibTableColumn
gidNbrDBReqListLength = _GidNbrDBReqListLength_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 15, 2, 2, 1, 5),
    _GidNbrDBReqListLength_Type()
)
gidNbrDBReqListLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gidNbrDBReqListLength.setStatus("mandatory")
_GidNbrDBSumListLength_Type = Counter32
_GidNbrDBSumListLength_Object = MibTableColumn
gidNbrDBSumListLength = _GidNbrDBSumListLength_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 15, 2, 2, 1, 6),
    _GidNbrDBSumListLength_Type()
)
gidNbrDBSumListLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gidNbrDBSumListLength.setStatus("mandatory")
_GidNbrHellosRx_Type = Counter32
_GidNbrHellosRx_Object = MibTableColumn
gidNbrHellosRx = _GidNbrHellosRx_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 15, 2, 2, 1, 7),
    _GidNbrHellosRx_Type()
)
gidNbrHellosRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gidNbrHellosRx.setStatus("mandatory")
_GidNbrLinkAnnouncementsRx_Type = Counter32
_GidNbrLinkAnnouncementsRx_Object = MibTableColumn
gidNbrLinkAnnouncementsRx = _GidNbrLinkAnnouncementsRx_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 15, 2, 2, 1, 8),
    _GidNbrLinkAnnouncementsRx_Type()
)
gidNbrLinkAnnouncementsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gidNbrLinkAnnouncementsRx.setStatus("mandatory")
_GidNbrNewLinkAnnouncementsRx_Type = Counter32
_GidNbrNewLinkAnnouncementsRx_Object = MibTableColumn
gidNbrNewLinkAnnouncementsRx = _GidNbrNewLinkAnnouncementsRx_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 15, 2, 2, 1, 9),
    _GidNbrNewLinkAnnouncementsRx_Type()
)
gidNbrNewLinkAnnouncementsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gidNbrNewLinkAnnouncementsRx.setStatus("mandatory")
_GidNbrIPAnnouncementsRx_Type = Counter32
_GidNbrIPAnnouncementsRx_Object = MibTableColumn
gidNbrIPAnnouncementsRx = _GidNbrIPAnnouncementsRx_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 15, 2, 2, 1, 10),
    _GidNbrIPAnnouncementsRx_Type()
)
gidNbrIPAnnouncementsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gidNbrIPAnnouncementsRx.setStatus("mandatory")
_GidNbrNewIPAnnouncementsRx_Type = Counter32
_GidNbrNewIPAnnouncementsRx_Object = MibTableColumn
gidNbrNewIPAnnouncementsRx = _GidNbrNewIPAnnouncementsRx_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 15, 2, 2, 1, 11),
    _GidNbrNewIPAnnouncementsRx_Type()
)
gidNbrNewIPAnnouncementsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gidNbrNewIPAnnouncementsRx.setStatus("mandatory")
_GidNbrGenericAnnouncementsRx_Type = Counter32
_GidNbrGenericAnnouncementsRx_Object = MibTableColumn
gidNbrGenericAnnouncementsRx = _GidNbrGenericAnnouncementsRx_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 15, 2, 2, 1, 12),
    _GidNbrGenericAnnouncementsRx_Type()
)
gidNbrGenericAnnouncementsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gidNbrGenericAnnouncementsRx.setStatus("mandatory")
_GidNbrNewGenericAnnouncementsRx_Type = Counter32
_GidNbrNewGenericAnnouncementsRx_Object = MibTableColumn
gidNbrNewGenericAnnouncementsRx = _GidNbrNewGenericAnnouncementsRx_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 15, 2, 2, 1, 13),
    _GidNbrNewGenericAnnouncementsRx_Type()
)
gidNbrNewGenericAnnouncementsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gidNbrNewGenericAnnouncementsRx.setStatus("mandatory")
_GidClientGroup_ObjectIdentity = ObjectIdentity
gidClientGroup = _GidClientGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 15, 3)
)
_GidClientCount_Type = Counter32
_GidClientCount_Object = MibScalar
gidClientCount = _GidClientCount_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 15, 3, 1),
    _GidClientCount_Type()
)
gidClientCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gidClientCount.setStatus("mandatory")
_GidClientTable_Object = MibTable
gidClientTable = _GidClientTable_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 15, 3, 2)
)
if mibBuilder.loadTexts:
    gidClientTable.setStatus("mandatory")
_GidClientEntry_Object = MibTableRow
gidClientEntry = _GidClientEntry_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 15, 3, 2, 1)
)
gidClientEntry.setIndexNames(
    (0, "LIGHTSTREAM-MIB", "gidClientID"),
)
if mibBuilder.loadTexts:
    gidClientEntry.setStatus("mandatory")
_GidClientID_Type = Integer32
_GidClientID_Object = MibTableColumn
gidClientID = _GidClientID_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 15, 3, 2, 1, 1),
    _GidClientID_Type()
)
gidClientID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gidClientID.setStatus("mandatory")
_GidClientEIA_Type = Integer32
_GidClientEIA_Object = MibTableColumn
gidClientEIA = _GidClientEIA_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 15, 3, 2, 1, 2),
    _GidClientEIA_Type()
)
gidClientEIA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gidClientEIA.setStatus("mandatory")
_GidClientAnnouncementsRx_Type = Counter32
_GidClientAnnouncementsRx_Object = MibTableColumn
gidClientAnnouncementsRx = _GidClientAnnouncementsRx_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 15, 3, 2, 1, 3),
    _GidClientAnnouncementsRx_Type()
)
gidClientAnnouncementsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gidClientAnnouncementsRx.setStatus("mandatory")
_GidClientLinkAnnouncementsRx_Type = Counter32
_GidClientLinkAnnouncementsRx_Object = MibTableColumn
gidClientLinkAnnouncementsRx = _GidClientLinkAnnouncementsRx_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 15, 3, 2, 1, 4),
    _GidClientLinkAnnouncementsRx_Type()
)
gidClientLinkAnnouncementsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gidClientLinkAnnouncementsRx.setStatus("mandatory")
_GidClientIPAnnouncementsRx_Type = Counter32
_GidClientIPAnnouncementsRx_Object = MibTableColumn
gidClientIPAnnouncementsRx = _GidClientIPAnnouncementsRx_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 15, 3, 2, 1, 5),
    _GidClientIPAnnouncementsRx_Type()
)
gidClientIPAnnouncementsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gidClientIPAnnouncementsRx.setStatus("mandatory")
_GidClientGenericAnnouncementsRx_Type = Counter32
_GidClientGenericAnnouncementsRx_Object = MibTableColumn
gidClientGenericAnnouncementsRx = _GidClientGenericAnnouncementsRx_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 15, 3, 2, 1, 6),
    _GidClientGenericAnnouncementsRx_Type()
)
gidClientGenericAnnouncementsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gidClientGenericAnnouncementsRx.setStatus("mandatory")
_GidClientEventsTx_Type = Counter32
_GidClientEventsTx_Object = MibTableColumn
gidClientEventsTx = _GidClientEventsTx_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 15, 3, 2, 1, 7),
    _GidClientEventsTx_Type()
)
gidClientEventsTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gidClientEventsTx.setStatus("mandatory")
_GidClientPathsGenerated_Type = Counter32
_GidClientPathsGenerated_Object = MibTableColumn
gidClientPathsGenerated = _GidClientPathsGenerated_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 15, 3, 2, 1, 8),
    _GidClientPathsGenerated_Type()
)
gidClientPathsGenerated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gidClientPathsGenerated.setStatus("mandatory")
_GidIOGroup_ObjectIdentity = ObjectIdentity
gidIOGroup = _GidIOGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 15, 4)
)
_GidIONbrMsgBuffersFree_Type = Counter32
_GidIONbrMsgBuffersFree_Object = MibScalar
gidIONbrMsgBuffersFree = _GidIONbrMsgBuffersFree_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 15, 4, 1),
    _GidIONbrMsgBuffersFree_Type()
)
gidIONbrMsgBuffersFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gidIONbrMsgBuffersFree.setStatus("mandatory")
_GidIONbrMsgBuffersActive_Type = Counter32
_GidIONbrMsgBuffersActive_Object = MibScalar
gidIONbrMsgBuffersActive = _GidIONbrMsgBuffersActive_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 15, 4, 2),
    _GidIONbrMsgBuffersActive_Type()
)
gidIONbrMsgBuffersActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gidIONbrMsgBuffersActive.setStatus("mandatory")
_GidIOClientMsgBuffersFree_Type = Counter32
_GidIOClientMsgBuffersFree_Object = MibScalar
gidIOClientMsgBuffersFree = _GidIOClientMsgBuffersFree_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 15, 4, 3),
    _GidIOClientMsgBuffersFree_Type()
)
gidIOClientMsgBuffersFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gidIOClientMsgBuffersFree.setStatus("mandatory")
_GidIOClientMsgBuffersActive_Type = Counter32
_GidIOClientMsgBuffersActive_Object = MibScalar
gidIOClientMsgBuffersActive = _GidIOClientMsgBuffersActive_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 15, 4, 4),
    _GidIOClientMsgBuffersActive_Type()
)
gidIOClientMsgBuffersActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gidIOClientMsgBuffersActive.setStatus("mandatory")
_GidSyncGroup_ObjectIdentity = ObjectIdentity
gidSyncGroup = _GidSyncGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 15, 6)
)
_GidSyncNbrsExistent_Type = Counter32
_GidSyncNbrsExistent_Object = MibScalar
gidSyncNbrsExistent = _GidSyncNbrsExistent_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 15, 6, 1),
    _GidSyncNbrsExistent_Type()
)
gidSyncNbrsExistent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gidSyncNbrsExistent.setStatus("mandatory")
_GidSyncNbrsExStart_Type = Counter32
_GidSyncNbrsExStart_Object = MibScalar
gidSyncNbrsExStart = _GidSyncNbrsExStart_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 15, 6, 2),
    _GidSyncNbrsExStart_Type()
)
gidSyncNbrsExStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gidSyncNbrsExStart.setStatus("mandatory")
_GidSyncNbrsExchange_Type = Counter32
_GidSyncNbrsExchange_Object = MibScalar
gidSyncNbrsExchange = _GidSyncNbrsExchange_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 15, 6, 3),
    _GidSyncNbrsExchange_Type()
)
gidSyncNbrsExchange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gidSyncNbrsExchange.setStatus("mandatory")
_GidSyncNbrsLoading_Type = Counter32
_GidSyncNbrsLoading_Object = MibScalar
gidSyncNbrsLoading = _GidSyncNbrsLoading_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 15, 6, 4),
    _GidSyncNbrsLoading_Type()
)
gidSyncNbrsLoading.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gidSyncNbrsLoading.setStatus("mandatory")
_GidSyncNbrsFull_Type = Counter32
_GidSyncNbrsFull_Object = MibScalar
gidSyncNbrsFull = _GidSyncNbrsFull_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 15, 6, 5),
    _GidSyncNbrsFull_Type()
)
gidSyncNbrsFull.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gidSyncNbrsFull.setStatus("mandatory")
_GidLinkGroup_ObjectIdentity = ObjectIdentity
gidLinkGroup = _GidLinkGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 15, 7)
)
_GidLinkDatabaseSize_Type = Integer32
_GidLinkDatabaseSize_Object = MibScalar
gidLinkDatabaseSize = _GidLinkDatabaseSize_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 15, 7, 1),
    _GidLinkDatabaseSize_Type()
)
gidLinkDatabaseSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gidLinkDatabaseSize.setStatus("mandatory")
_GidLineCardTable_Object = MibTable
gidLineCardTable = _GidLineCardTable_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 15, 7, 2)
)
if mibBuilder.loadTexts:
    gidLineCardTable.setStatus("mandatory")
_GidLineCardEntry_Object = MibTableRow
gidLineCardEntry = _GidLineCardEntry_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 15, 7, 2, 1)
)
gidLineCardEntry.setIndexNames(
    (0, "LIGHTSTREAM-MIB", "gidLineCardChassis"),
    (0, "LIGHTSTREAM-MIB", "gidLineCardSlot"),
)
if mibBuilder.loadTexts:
    gidLineCardEntry.setStatus("mandatory")
_GidLineCardChassis_Type = Integer32
_GidLineCardChassis_Object = MibTableColumn
gidLineCardChassis = _GidLineCardChassis_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 15, 7, 2, 1, 1),
    _GidLineCardChassis_Type()
)
gidLineCardChassis.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gidLineCardChassis.setStatus("mandatory")
_GidLineCardSlot_Type = Integer32
_GidLineCardSlot_Object = MibTableColumn
gidLineCardSlot = _GidLineCardSlot_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 15, 7, 2, 1, 2),
    _GidLineCardSlot_Type()
)
gidLineCardSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gidLineCardSlot.setStatus("mandatory")
_GidLineCardEntryAge_Type = LightStreamUpToMaxAge
_GidLineCardEntryAge_Object = MibTableColumn
gidLineCardEntryAge = _GidLineCardEntryAge_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 15, 7, 2, 1, 3),
    _GidLineCardEntryAge_Type()
)
gidLineCardEntryAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gidLineCardEntryAge.setStatus("mandatory")
_GidLineCardEntrySeqno_Type = Integer32
_GidLineCardEntrySeqno_Object = MibTableColumn
gidLineCardEntrySeqno = _GidLineCardEntrySeqno_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 15, 7, 2, 1, 4),
    _GidLineCardEntrySeqno_Type()
)
gidLineCardEntrySeqno.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gidLineCardEntrySeqno.setStatus("mandatory")
_GidLineCardEntryAdvNP_Type = Integer32
_GidLineCardEntryAdvNP_Object = MibTableColumn
gidLineCardEntryAdvNP = _GidLineCardEntryAdvNP_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 15, 7, 2, 1, 5),
    _GidLineCardEntryAdvNP_Type()
)
gidLineCardEntryAdvNP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gidLineCardEntryAdvNP.setStatus("mandatory")
_GidLineCardPorts_Type = Integer32
_GidLineCardPorts_Object = MibTableColumn
gidLineCardPorts = _GidLineCardPorts_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 15, 7, 2, 1, 6),
    _GidLineCardPorts_Type()
)
gidLineCardPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gidLineCardPorts.setStatus("mandatory")
_GidPortTable_Object = MibTable
gidPortTable = _GidPortTable_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 15, 7, 3)
)
if mibBuilder.loadTexts:
    gidPortTable.setStatus("mandatory")
_GidPortEntry_Object = MibTableRow
gidPortEntry = _GidPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 15, 7, 3, 1)
)
gidPortEntry.setIndexNames(
    (0, "LIGHTSTREAM-MIB", "gidPortChassis"),
    (0, "LIGHTSTREAM-MIB", "gidPortID"),
)
if mibBuilder.loadTexts:
    gidPortEntry.setStatus("mandatory")
_GidPortChassis_Type = Integer32
_GidPortChassis_Object = MibTableColumn
gidPortChassis = _GidPortChassis_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 15, 7, 3, 1, 1),
    _GidPortChassis_Type()
)
gidPortChassis.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gidPortChassis.setStatus("mandatory")
_GidPortID_Type = Integer32
_GidPortID_Object = MibTableColumn
gidPortID = _GidPortID_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 15, 7, 3, 1, 2),
    _GidPortID_Type()
)
gidPortID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gidPortID.setStatus("mandatory")


class _GidPortService_Type(Integer32):
    """Custom type gidPortService based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("edge", 2),
          ("trunk", 1))
    )


_GidPortService_Type.__name__ = "Integer32"
_GidPortService_Object = MibTableColumn
gidPortService = _GidPortService_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 15, 7, 3, 1, 3),
    _GidPortService_Type()
)
gidPortService.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gidPortService.setStatus("mandatory")


class _GidPortUpDown_Type(Integer32):
    """Custom type gidPortUpDown based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 1),
          ("up", 2))
    )


_GidPortUpDown_Type.__name__ = "Integer32"
_GidPortUpDown_Object = MibTableColumn
gidPortUpDown = _GidPortUpDown_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 15, 7, 3, 1, 4),
    _GidPortUpDown_Type()
)
gidPortUpDown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gidPortUpDown.setStatus("mandatory")
_GidPortBW0_Type = Integer32
_GidPortBW0_Object = MibTableColumn
gidPortBW0 = _GidPortBW0_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 15, 7, 3, 1, 5),
    _GidPortBW0_Type()
)
gidPortBW0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gidPortBW0.setStatus("mandatory")
_GidPortBW1_Type = Integer32
_GidPortBW1_Object = MibTableColumn
gidPortBW1 = _GidPortBW1_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 15, 7, 3, 1, 6),
    _GidPortBW1_Type()
)
gidPortBW1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gidPortBW1.setStatus("mandatory")
_GidPortBW2_Type = Integer32
_GidPortBW2_Object = MibTableColumn
gidPortBW2 = _GidPortBW2_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 15, 7, 3, 1, 7),
    _GidPortBW2_Type()
)
gidPortBW2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gidPortBW2.setStatus("mandatory")
_GidPortRemoteChassis_Type = Integer32
_GidPortRemoteChassis_Object = MibTableColumn
gidPortRemoteChassis = _GidPortRemoteChassis_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 15, 7, 3, 1, 8),
    _GidPortRemoteChassis_Type()
)
gidPortRemoteChassis.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gidPortRemoteChassis.setStatus("mandatory")
_GidPortRemotePort_Type = Integer32
_GidPortRemotePort_Object = MibTableColumn
gidPortRemotePort = _GidPortRemotePort_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 15, 7, 3, 1, 9),
    _GidPortRemotePort_Type()
)
gidPortRemotePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gidPortRemotePort.setStatus("mandatory")
_GidIpAddressGroup_ObjectIdentity = ObjectIdentity
gidIpAddressGroup = _GidIpAddressGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 15, 8)
)
_GidIpAddressDatabaseSize_Type = Integer32
_GidIpAddressDatabaseSize_Object = MibScalar
gidIpAddressDatabaseSize = _GidIpAddressDatabaseSize_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 15, 8, 1),
    _GidIpAddressDatabaseSize_Type()
)
gidIpAddressDatabaseSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gidIpAddressDatabaseSize.setStatus("mandatory")
_GidIpAddressTable_Object = MibTable
gidIpAddressTable = _GidIpAddressTable_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 15, 8, 2)
)
if mibBuilder.loadTexts:
    gidIpAddressTable.setStatus("mandatory")
_GidIpAddressEntry_Object = MibTableRow
gidIpAddressEntry = _GidIpAddressEntry_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 15, 8, 2, 1)
)
gidIpAddressEntry.setIndexNames(
    (0, "LIGHTSTREAM-MIB", "gidInternalIpAddress"),
)
if mibBuilder.loadTexts:
    gidIpAddressEntry.setStatus("mandatory")
_GidInternalIpAddress_Type = IpAddress
_GidInternalIpAddress_Object = MibTableColumn
gidInternalIpAddress = _GidInternalIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 15, 8, 2, 1, 1),
    _GidInternalIpAddress_Type()
)
gidInternalIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gidInternalIpAddress.setStatus("mandatory")
_GidIpEntryAge_Type = LightStreamUpToMaxAge
_GidIpEntryAge_Object = MibTableColumn
gidIpEntryAge = _GidIpEntryAge_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 15, 8, 2, 1, 2),
    _GidIpEntryAge_Type()
)
gidIpEntryAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gidIpEntryAge.setStatus("mandatory")
_GidIpEntrySeqno_Type = Integer32
_GidIpEntrySeqno_Object = MibTableColumn
gidIpEntrySeqno = _GidIpEntrySeqno_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 15, 8, 2, 1, 3),
    _GidIpEntrySeqno_Type()
)
gidIpEntrySeqno.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gidIpEntrySeqno.setStatus("mandatory")
_GidIpEntryAdvNP_Type = Integer32
_GidIpEntryAdvNP_Object = MibTableColumn
gidIpEntryAdvNP = _GidIpEntryAdvNP_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 15, 8, 2, 1, 4),
    _GidIpEntryAdvNP_Type()
)
gidIpEntryAdvNP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gidIpEntryAdvNP.setStatus("mandatory")
_GidIpEntryNetMask_Type = Integer32
_GidIpEntryNetMask_Object = MibTableColumn
gidIpEntryNetMask = _GidIpEntryNetMask_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 15, 8, 2, 1, 5),
    _GidIpEntryNetMask_Type()
)
gidIpEntryNetMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gidIpEntryNetMask.setStatus("mandatory")


class _GidIpEntryEIA_Type(OctetString):
    """Custom type gidIpEntryEIA based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_GidIpEntryEIA_Type.__name__ = "OctetString"
_GidIpEntryEIA_Object = MibTableColumn
gidIpEntryEIA = _GidIpEntryEIA_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 15, 8, 2, 1, 6),
    _GidIpEntryEIA_Type()
)
gidIpEntryEIA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gidIpEntryEIA.setStatus("mandatory")
_GidEventGroup_ObjectIdentity = ObjectIdentity
gidEventGroup = _GidEventGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 15, 9)
)
_GidEventLinkEventsDelivered_Type = Counter32
_GidEventLinkEventsDelivered_Object = MibScalar
gidEventLinkEventsDelivered = _GidEventLinkEventsDelivered_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 15, 9, 1),
    _GidEventLinkEventsDelivered_Type()
)
gidEventLinkEventsDelivered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gidEventLinkEventsDelivered.setStatus("mandatory")
_GidEventIpEventsDelivered_Type = Counter32
_GidEventIpEventsDelivered_Object = MibScalar
gidEventIpEventsDelivered = _GidEventIpEventsDelivered_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 15, 9, 2),
    _GidEventIpEventsDelivered_Type()
)
gidEventIpEventsDelivered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gidEventIpEventsDelivered.setStatus("mandatory")
_GidEventGenericGinfoEventsDelivered_Type = Counter32
_GidEventGenericGinfoEventsDelivered_Object = MibScalar
gidEventGenericGinfoEventsDelivered = _GidEventGenericGinfoEventsDelivered_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 15, 9, 3),
    _GidEventGenericGinfoEventsDelivered_Type()
)
gidEventGenericGinfoEventsDelivered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gidEventGenericGinfoEventsDelivered.setStatus("mandatory")
_GidEventGenericGinfoEventTable_Object = MibTable
gidEventGenericGinfoEventTable = _GidEventGenericGinfoEventTable_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 15, 9, 4)
)
if mibBuilder.loadTexts:
    gidEventGenericGinfoEventTable.setStatus("mandatory")
_GidEventGenericGinfoEventCount_Object = MibTableRow
gidEventGenericGinfoEventCount = _GidEventGenericGinfoEventCount_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 15, 9, 4, 1)
)
gidEventGenericGinfoEventCount.setIndexNames(
    (0, "LIGHTSTREAM-MIB", "gidEventDistributionGroup"),
)
if mibBuilder.loadTexts:
    gidEventGenericGinfoEventCount.setStatus("mandatory")
_GidEventDistributionGroup_Type = Integer32
_GidEventDistributionGroup_Object = MibTableColumn
gidEventDistributionGroup = _GidEventDistributionGroup_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 15, 9, 4, 1, 1),
    _GidEventDistributionGroup_Type()
)
gidEventDistributionGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gidEventDistributionGroup.setStatus("mandatory")
_GidEventGenericGinfoEvents_Type = Counter32
_GidEventGenericGinfoEvents_Object = MibTableColumn
gidEventGenericGinfoEvents = _GidEventGenericGinfoEvents_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 15, 9, 4, 1, 2),
    _GidEventGenericGinfoEvents_Type()
)
gidEventGenericGinfoEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gidEventGenericGinfoEvents.setStatus("mandatory")
_LsPID_ObjectIdentity = ObjectIdentity
lsPID = _LsPID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 16)
)
_PidTable_Object = MibTable
pidTable = _PidTable_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 16, 1)
)
if mibBuilder.loadTexts:
    pidTable.setStatus("mandatory")
_PidEntry_Object = MibTableRow
pidEntry = _PidEntry_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 16, 1, 1)
)
pidEntry.setIndexNames(
    (0, "LIGHTSTREAM-MIB", "pidIndex"),
)
if mibBuilder.loadTexts:
    pidEntry.setStatus("mandatory")
_PidIndex_Type = Integer32
_PidIndex_Object = MibTableColumn
pidIndex = _PidIndex_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 16, 1, 1, 1),
    _PidIndex_Type()
)
pidIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pidIndex.setStatus("mandatory")
_PidName_Type = DisplayString
_PidName_Object = MibTableColumn
pidName = _PidName_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 16, 1, 1, 2),
    _PidName_Type()
)
pidName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pidName.setStatus("mandatory")
_PidCreationTime_Type = Integer32
_PidCreationTime_Object = MibTableColumn
pidCreationTime = _PidCreationTime_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 16, 1, 1, 3),
    _PidCreationTime_Type()
)
pidCreationTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pidCreationTime.setStatus("mandatory")


class _PidOperStatus_Type(Integer32):
    """Custom type pidOperStatus based on Integer32"""
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


_PidOperStatus_Type.__name__ = "Integer32"
_PidOperStatus_Object = MibTableColumn
pidOperStatus = _PidOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 16, 1, 1, 4),
    _PidOperStatus_Type()
)
pidOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pidOperStatus.setStatus("mandatory")


class _PidAdminStatus_Type(Integer32):
    """Custom type pidAdminStatus based on Integer32"""
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


_PidAdminStatus_Type.__name__ = "Integer32"
_PidAdminStatus_Object = MibTableColumn
pidAdminStatus = _PidAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 16, 1, 1, 5),
    _PidAdminStatus_Type()
)
pidAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pidAdminStatus.setStatus("mandatory")
_LsND_ObjectIdentity = ObjectIdentity
lsND = _LsND_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 17)
)
_NdGeneralGroup_ObjectIdentity = ObjectIdentity
ndGeneralGroup = _NdGeneralGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 17, 1)
)
_NdSoftwareVersionNumber_Type = DisplayString
_NdSoftwareVersionNumber_Object = MibScalar
ndSoftwareVersionNumber = _NdSoftwareVersionNumber_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 17, 1, 1),
    _NdSoftwareVersionNumber_Type()
)
ndSoftwareVersionNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ndSoftwareVersionNumber.setStatus("mandatory")
_NdProcessID_Type = Integer32
_NdProcessID_Object = MibScalar
ndProcessID = _NdProcessID_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 17, 1, 2),
    _NdProcessID_Type()
)
ndProcessID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ndProcessID.setStatus("mandatory")
_NdMemoryUse_Type = Counter32
_NdMemoryUse_Object = MibScalar
ndMemoryUse = _NdMemoryUse_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 17, 1, 4),
    _NdMemoryUse_Type()
)
ndMemoryUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ndMemoryUse.setStatus("mandatory")
_NdTimersProcessed_Type = Counter32
_NdTimersProcessed_Object = MibScalar
ndTimersProcessed = _NdTimersProcessed_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 17, 1, 5),
    _NdTimersProcessed_Type()
)
ndTimersProcessed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ndTimersProcessed.setStatus("mandatory")
_NdLCGroup_ObjectIdentity = ObjectIdentity
ndLCGroup = _NdLCGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 17, 2)
)
_NdLCCount_Type = Counter32
_NdLCCount_Object = MibScalar
ndLCCount = _NdLCCount_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 17, 2, 1),
    _NdLCCount_Type()
)
ndLCCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ndLCCount.setStatus("mandatory")
_NdLCTable_Object = MibTable
ndLCTable = _NdLCTable_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 17, 2, 2)
)
if mibBuilder.loadTexts:
    ndLCTable.setStatus("mandatory")
_NdLCEntry_Object = MibTableRow
ndLCEntry = _NdLCEntry_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 17, 2, 2, 1)
)
ndLCEntry.setIndexNames(
    (0, "LIGHTSTREAM-MIB", "ndLCEIA"),
)
if mibBuilder.loadTexts:
    ndLCEntry.setStatus("mandatory")
_NdLCEIA_Type = Integer32
_NdLCEIA_Object = MibTableColumn
ndLCEIA = _NdLCEIA_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 17, 2, 2, 1, 1),
    _NdLCEIA_Type()
)
ndLCEIA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ndLCEIA.setStatus("mandatory")
_NdLCChannel_Type = Integer32
_NdLCChannel_Object = MibTableColumn
ndLCChannel = _NdLCChannel_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 17, 2, 2, 1, 2),
    _NdLCChannel_Type()
)
ndLCChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ndLCChannel.setStatus("mandatory")


class _NdLCState_Type(Integer32):
    """Custom type ndLCState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("comingdown", 4),
          ("existent", 2),
          ("unknown", 1),
          ("up", 3))
    )


_NdLCState_Type.__name__ = "Integer32"
_NdLCState_Object = MibTableColumn
ndLCState = _NdLCState_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 17, 2, 2, 1, 3),
    _NdLCState_Type()
)
ndLCState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ndLCState.setStatus("mandatory")
_NdNbrGroup_ObjectIdentity = ObjectIdentity
ndNbrGroup = _NdNbrGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 17, 3)
)
_NdNbrCount_Type = Counter32
_NdNbrCount_Object = MibScalar
ndNbrCount = _NdNbrCount_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 17, 3, 1),
    _NdNbrCount_Type()
)
ndNbrCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ndNbrCount.setStatus("mandatory")
_NdNbrTable_Object = MibTable
ndNbrTable = _NdNbrTable_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 17, 3, 2)
)
if mibBuilder.loadTexts:
    ndNbrTable.setStatus("mandatory")
_NdNbrEntry_Object = MibTableRow
ndNbrEntry = _NdNbrEntry_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 17, 3, 2, 1)
)
ndNbrEntry.setIndexNames(
    (0, "LIGHTSTREAM-MIB", "ndNbrEIA"),
)
if mibBuilder.loadTexts:
    ndNbrEntry.setStatus("mandatory")
_NdNbrEIA_Type = Integer32
_NdNbrEIA_Object = MibTableColumn
ndNbrEIA = _NdNbrEIA_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 17, 3, 2, 1, 1),
    _NdNbrEIA_Type()
)
ndNbrEIA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ndNbrEIA.setStatus("mandatory")
_NdNbrChannel_Type = Integer32
_NdNbrChannel_Object = MibTableColumn
ndNbrChannel = _NdNbrChannel_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 17, 3, 2, 1, 2),
    _NdNbrChannel_Type()
)
ndNbrChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ndNbrChannel.setStatus("mandatory")


class _NdNbrState_Type(Integer32):
    """Custom type ndNbrState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("comingdown", 4),
          ("existent", 2),
          ("unknown", 1),
          ("up", 3))
    )


_NdNbrState_Type.__name__ = "Integer32"
_NdNbrState_Object = MibTableColumn
ndNbrState = _NdNbrState_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 17, 3, 2, 1, 3),
    _NdNbrState_Type()
)
ndNbrState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ndNbrState.setStatus("mandatory")
_NdSwudGroup_ObjectIdentity = ObjectIdentity
ndSwudGroup = _NdSwudGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 17, 4)
)
_NdSwudTable_Object = MibTable
ndSwudTable = _NdSwudTable_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 17, 4, 1)
)
if mibBuilder.loadTexts:
    ndSwudTable.setStatus("mandatory")
_NdSwudEntry_Object = MibTableRow
ndSwudEntry = _NdSwudEntry_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 17, 4, 1, 1)
)
ndSwudEntry.setIndexNames(
    (0, "LIGHTSTREAM-MIB", "ndSwudIndex"),
)
if mibBuilder.loadTexts:
    ndSwudEntry.setStatus("mandatory")
_NdSwudIndex_Type = Integer32
_NdSwudIndex_Object = MibTableColumn
ndSwudIndex = _NdSwudIndex_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 17, 4, 1, 1, 1),
    _NdSwudIndex_Type()
)
ndSwudIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ndSwudIndex.setStatus("mandatory")
_NdOperIntvl_Type = Integer32
_NdOperIntvl_Object = MibTableColumn
ndOperIntvl = _NdOperIntvl_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 17, 4, 1, 1, 2),
    _NdOperIntvl_Type()
)
ndOperIntvl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ndOperIntvl.setStatus("mandatory")
_NdOperJ_Type = Integer32
_NdOperJ_Object = MibTableColumn
ndOperJ = _NdOperJ_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 17, 4, 1, 1, 3),
    _NdOperJ_Type()
)
ndOperJ.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ndOperJ.setStatus("mandatory")
_NdOperK_Type = Integer32
_NdOperK_Object = MibTableColumn
ndOperK = _NdOperK_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 17, 4, 1, 1, 4),
    _NdOperK_Type()
)
ndOperK.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ndOperK.setStatus("mandatory")
_NdOperM_Type = Integer32
_NdOperM_Object = MibTableColumn
ndOperM = _NdOperM_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 17, 4, 1, 1, 5),
    _NdOperM_Type()
)
ndOperM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ndOperM.setStatus("mandatory")
_NdOperN_Type = Integer32
_NdOperN_Object = MibTableColumn
ndOperN = _NdOperN_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 17, 4, 1, 1, 6),
    _NdOperN_Type()
)
ndOperN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ndOperN.setStatus("mandatory")


class _NdAdminIntvl_Type(Integer32):
    """Custom type ndAdminIntvl based on Integer32"""
    defaultValue = 3


_NdAdminIntvl_Object = MibTableColumn
ndAdminIntvl = _NdAdminIntvl_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 17, 4, 1, 1, 7),
    _NdAdminIntvl_Type()
)
ndAdminIntvl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ndAdminIntvl.setStatus("mandatory")


class _NdAdminJ_Type(Integer32):
    """Custom type ndAdminJ based on Integer32"""
    defaultValue = 1


_NdAdminJ_Object = MibTableColumn
ndAdminJ = _NdAdminJ_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 17, 4, 1, 1, 8),
    _NdAdminJ_Type()
)
ndAdminJ.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ndAdminJ.setStatus("mandatory")


class _NdAdminK_Type(Integer32):
    """Custom type ndAdminK based on Integer32"""
    defaultValue = 1


_NdAdminK_Object = MibTableColumn
ndAdminK = _NdAdminK_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 17, 4, 1, 1, 9),
    _NdAdminK_Type()
)
ndAdminK.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ndAdminK.setStatus("mandatory")


class _NdAdminM_Type(Integer32):
    """Custom type ndAdminM based on Integer32"""
    defaultValue = 1


_NdAdminM_Object = MibTableColumn
ndAdminM = _NdAdminM_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 17, 4, 1, 1, 10),
    _NdAdminM_Type()
)
ndAdminM.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ndAdminM.setStatus("mandatory")


class _NdAdminN_Type(Integer32):
    """Custom type ndAdminN based on Integer32"""
    defaultValue = 1


_NdAdminN_Object = MibTableColumn
ndAdminN = _NdAdminN_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 17, 4, 1, 1, 11),
    _NdAdminN_Type()
)
ndAdminN.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ndAdminN.setStatus("mandatory")
_NdTrigger_Type = Integer32
_NdTrigger_Object = MibTableColumn
ndTrigger = _NdTrigger_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 17, 4, 1, 1, 12),
    _NdTrigger_Type()
)
ndTrigger.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ndTrigger.setStatus("mandatory")
_NdSwudStatsInputErrors_Type = Counter32
_NdSwudStatsInputErrors_Object = MibScalar
ndSwudStatsInputErrors = _NdSwudStatsInputErrors_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 17, 4, 2),
    _NdSwudStatsInputErrors_Type()
)
ndSwudStatsInputErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ndSwudStatsInputErrors.setStatus("mandatory")
_NdSwudStatsTable_Object = MibTable
ndSwudStatsTable = _NdSwudStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 17, 4, 3)
)
if mibBuilder.loadTexts:
    ndSwudStatsTable.setStatus("mandatory")
_NdSwudStatsEntry_Object = MibTableRow
ndSwudStatsEntry = _NdSwudStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 17, 4, 3, 1)
)
ndSwudStatsEntry.setIndexNames(
    (0, "LIGHTSTREAM-MIB", "ndSwudStatsIndex"),
)
if mibBuilder.loadTexts:
    ndSwudStatsEntry.setStatus("mandatory")
_NdSwudStatsIndex_Type = Integer32
_NdSwudStatsIndex_Object = MibTableColumn
ndSwudStatsIndex = _NdSwudStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 17, 4, 3, 1, 1),
    _NdSwudStatsIndex_Type()
)
ndSwudStatsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ndSwudStatsIndex.setStatus("mandatory")
_NdInputCells_Type = Counter32
_NdInputCells_Object = MibTableColumn
ndInputCells = _NdInputCells_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 17, 4, 3, 1, 2),
    _NdInputCells_Type()
)
ndInputCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ndInputCells.setStatus("mandatory")
_NdInputErrs_Type = Counter32
_NdInputErrs_Object = MibTableColumn
ndInputErrs = _NdInputErrs_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 17, 4, 3, 1, 3),
    _NdInputErrs_Type()
)
ndInputErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ndInputErrs.setStatus("mandatory")
_NdOutputCells_Type = Counter32
_NdOutputCells_Object = MibTableColumn
ndOutputCells = _NdOutputCells_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 17, 4, 3, 1, 4),
    _NdOutputCells_Type()
)
ndOutputCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ndOutputCells.setStatus("mandatory")
_NdOutputErrs_Type = Counter32
_NdOutputErrs_Object = MibTableColumn
ndOutputErrs = _NdOutputErrs_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 17, 4, 3, 1, 5),
    _NdOutputErrs_Type()
)
ndOutputErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ndOutputErrs.setStatus("mandatory")
_NdClientGroup_ObjectIdentity = ObjectIdentity
ndClientGroup = _NdClientGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 17, 5)
)
_NdClientCount_Type = Counter32
_NdClientCount_Object = MibScalar
ndClientCount = _NdClientCount_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 17, 5, 1),
    _NdClientCount_Type()
)
ndClientCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ndClientCount.setStatus("mandatory")
_NdClientTable_Object = MibTable
ndClientTable = _NdClientTable_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 17, 5, 2)
)
if mibBuilder.loadTexts:
    ndClientTable.setStatus("mandatory")
_NdClientEntry_Object = MibTableRow
ndClientEntry = _NdClientEntry_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 17, 5, 2, 1)
)
ndClientEntry.setIndexNames(
    (0, "LIGHTSTREAM-MIB", "ndClientID"),
)
if mibBuilder.loadTexts:
    ndClientEntry.setStatus("mandatory")
_NdClientID_Type = Integer32
_NdClientID_Object = MibTableColumn
ndClientID = _NdClientID_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 17, 5, 2, 1, 1),
    _NdClientID_Type()
)
ndClientID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ndClientID.setStatus("mandatory")


class _NdClientType_Type(Integer32):
    """Custom type ndClientType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("ca", 6),
          ("gid", 4),
          ("lcc", 5),
          ("nd", 3),
          ("sys", 7))
    )


_NdClientType_Type.__name__ = "Integer32"
_NdClientType_Object = MibTableColumn
ndClientType = _NdClientType_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 17, 5, 2, 1, 2),
    _NdClientType_Type()
)
ndClientType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ndClientType.setStatus("mandatory")
_NdClientSubType_Type = Integer32
_NdClientSubType_Object = MibTableColumn
ndClientSubType = _NdClientSubType_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 17, 5, 2, 1, 3),
    _NdClientSubType_Type()
)
ndClientSubType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ndClientSubType.setStatus("mandatory")
_NdClientEIA_Type = Integer32
_NdClientEIA_Object = MibTableColumn
ndClientEIA = _NdClientEIA_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 17, 5, 2, 1, 4),
    _NdClientEIA_Type()
)
ndClientEIA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ndClientEIA.setStatus("mandatory")
_NdClientRegistration_Type = Integer32
_NdClientRegistration_Object = MibTableColumn
ndClientRegistration = _NdClientRegistration_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 17, 5, 2, 1, 5),
    _NdClientRegistration_Type()
)
ndClientRegistration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ndClientRegistration.setStatus("mandatory")
_NdInternalGroup_ObjectIdentity = ObjectIdentity
ndInternalGroup = _NdInternalGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 17, 6)
)


class _NdInternalDebugLevel_Type(Integer32):
    """Custom type ndInternalDebugLevel based on Integer32"""
    defaultValue = 0


_NdInternalDebugLevel_Object = MibScalar
ndInternalDebugLevel = _NdInternalDebugLevel_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 17, 6, 1),
    _NdInternalDebugLevel_Type()
)
ndInternalDebugLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ndInternalDebugLevel.setStatus("mandatory")


class _NdInternalDebugFlags_Type(Integer32):
    """Custom type ndInternalDebugFlags based on Integer32"""
    defaultValue = 0


_NdInternalDebugFlags_Object = MibScalar
ndInternalDebugFlags = _NdInternalDebugFlags_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 17, 6, 2),
    _NdInternalDebugFlags_Type()
)
ndInternalDebugFlags.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ndInternalDebugFlags.setStatus("mandatory")
_NdRedundancyGroup_ObjectIdentity = ObjectIdentity
ndRedundancyGroup = _NdRedundancyGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 17, 7)
)


class _NdPrimaryNP_Type(Integer32):
    """Custom type ndPrimaryNP based on Integer32"""
    defaultValue = 0


_NdPrimaryNP_Object = MibScalar
ndPrimaryNP = _NdPrimaryNP_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 17, 7, 1),
    _NdPrimaryNP_Type()
)
ndPrimaryNP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ndPrimaryNP.setStatus("mandatory")
_NdThisNP_Type = Integer32
_NdThisNP_Object = MibScalar
ndThisNP = _NdThisNP_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 17, 7, 2),
    _NdThisNP_Type()
)
ndThisNP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ndThisNP.setStatus("mandatory")
_NdForceToBackup_Type = Integer32
_NdForceToBackup_Object = MibScalar
ndForceToBackup = _NdForceToBackup_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 17, 7, 3),
    _NdForceToBackup_Type()
)
ndForceToBackup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ndForceToBackup.setStatus("mandatory")
_LwmaInfo_ObjectIdentity = ObjectIdentity
lwmaInfo = _LwmaInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 18)
)
_LwmaTable_Object = MibTable
lwmaTable = _LwmaTable_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 18, 1)
)
if mibBuilder.loadTexts:
    lwmaTable.setStatus("mandatory")
_LwmaEntry_Object = MibTableRow
lwmaEntry = _LwmaEntry_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 18, 1, 1)
)
lwmaEntry.setIndexNames(
    (0, "LIGHTSTREAM-MIB", "lwmaIndex"),
)
if mibBuilder.loadTexts:
    lwmaEntry.setStatus("mandatory")
_LwmaIndex_Type = Integer32
_LwmaIndex_Object = MibTableColumn
lwmaIndex = _LwmaIndex_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 18, 1, 1, 1),
    _LwmaIndex_Type()
)
lwmaIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lwmaIndex.setStatus("mandatory")
_LwmaCreationTime_Type = Integer32
_LwmaCreationTime_Object = MibTableColumn
lwmaCreationTime = _LwmaCreationTime_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 18, 1, 1, 2),
    _LwmaCreationTime_Type()
)
lwmaCreationTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lwmaCreationTime.setStatus("mandatory")
_LwmaTableNotification_Type = ObjectIdentifier
_LwmaTableNotification_Object = MibTableColumn
lwmaTableNotification = _LwmaTableNotification_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 18, 1, 1, 3),
    _LwmaTableNotification_Type()
)
lwmaTableNotification.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lwmaTableNotification.setStatus("mandatory")


class _LwmaTrapLevel_Type(Integer32):
    """Custom type lwmaTrapLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("debug", 4),
          ("informational", 2),
          ("operational", 1),
          ("trace", 3))
    )


_LwmaTrapLevel_Type.__name__ = "Integer32"
_LwmaTrapLevel_Object = MibTableColumn
lwmaTrapLevel = _LwmaTrapLevel_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 18, 1, 1, 4),
    _LwmaTrapLevel_Type()
)
lwmaTrapLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lwmaTrapLevel.setStatus("mandatory")
_LwmaTrapNumber_Type = Integer32
_LwmaTrapNumber_Object = MibTableColumn
lwmaTrapNumber = _LwmaTrapNumber_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 18, 1, 1, 5),
    _LwmaTrapNumber_Type()
)
lwmaTrapNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lwmaTrapNumber.setStatus("mandatory")


class _LwmaTrapOnOffState_Type(Integer32):
    """Custom type lwmaTrapOnOffState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("trapOff", 2),
          ("trapOn", 1))
    )


_LwmaTrapOnOffState_Type.__name__ = "Integer32"
_LwmaTrapOnOffState_Object = MibTableColumn
lwmaTrapOnOffState = _LwmaTrapOnOffState_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 18, 1, 1, 6),
    _LwmaTrapOnOffState_Type()
)
lwmaTrapOnOffState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lwmaTrapOnOffState.setStatus("mandatory")


class _LwmaTrapCliAlias_Type(OctetString):
    """Custom type lwmaTrapCliAlias based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(32, 32),
    )


_LwmaTrapCliAlias_Type.__name__ = "OctetString"
_LwmaTrapCliAlias_Object = MibTableColumn
lwmaTrapCliAlias = _LwmaTrapCliAlias_Object(
    (1, 3, 6, 1, 4, 1, 711, 2, 1, 18, 1, 1, 7),
    _LwmaTrapCliAlias_Type()
)
lwmaTrapCliAlias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lwmaTrapCliAlias.setStatus("mandatory")
_LightStreamInternet_ObjectIdentity = ObjectIdentity
lightStreamInternet = _LightStreamInternet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 711, 3)
)
_LightStreamBridge_ObjectIdentity = ObjectIdentity
lightStreamBridge = _LightStreamBridge_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 711, 3, 1)
)
_LightStreamBridgePortTable_Object = MibTable
lightStreamBridgePortTable = _LightStreamBridgePortTable_Object(
    (1, 3, 6, 1, 4, 1, 711, 3, 1, 1)
)
if mibBuilder.loadTexts:
    lightStreamBridgePortTable.setStatus("mandatory")
_LightStreamBridgePortEntry_Object = MibTableRow
lightStreamBridgePortEntry = _LightStreamBridgePortEntry_Object(
    (1, 3, 6, 1, 4, 1, 711, 3, 1, 1, 1)
)
lightStreamBridgePortEntry.setIndexNames(
    (0, "LIGHTSTREAM-MIB", "lightStreamBrPortPort"),
)
if mibBuilder.loadTexts:
    lightStreamBridgePortEntry.setStatus("mandatory")
_LightStreamBrPortPort_Type = Integer32
_LightStreamBrPortPort_Object = MibTableColumn
lightStreamBrPortPort = _LightStreamBrPortPort_Object(
    (1, 3, 6, 1, 4, 1, 711, 3, 1, 1, 1, 1),
    _LightStreamBrPortPort_Type()
)
lightStreamBrPortPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lightStreamBrPortPort.setStatus("mandatory")


class _LightStreamBrPortDefaultAction_Type(LightStreamFilterAction):
    """Custom type lightStreamBrPortDefaultAction based on LightStreamFilterAction"""


_LightStreamBrPortDefaultAction_Object = MibTableColumn
lightStreamBrPortDefaultAction = _LightStreamBrPortDefaultAction_Object(
    (1, 3, 6, 1, 4, 1, 711, 3, 1, 1, 1, 2),
    _LightStreamBrPortDefaultAction_Type()
)
lightStreamBrPortDefaultAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lightStreamBrPortDefaultAction.setStatus("mandatory")


class _LightStreamBrPortBcastRateLimit_Type(Integer32):
    """Custom type lightStreamBrPortBcastRateLimit based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 127),
    )


_LightStreamBrPortBcastRateLimit_Type.__name__ = "Integer32"
_LightStreamBrPortBcastRateLimit_Object = MibTableColumn
lightStreamBrPortBcastRateLimit = _LightStreamBrPortBcastRateLimit_Object(
    (1, 3, 6, 1, 4, 1, 711, 3, 1, 1, 1, 3),
    _LightStreamBrPortBcastRateLimit_Type()
)
lightStreamBrPortBcastRateLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lightStreamBrPortBcastRateLimit.setStatus("mandatory")
_LightStreamBrPortDroppedBcastPkts_Type = Counter32
_LightStreamBrPortDroppedBcastPkts_Object = MibTableColumn
lightStreamBrPortDroppedBcastPkts = _LightStreamBrPortDroppedBcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 711, 3, 1, 1, 1, 4),
    _LightStreamBrPortDroppedBcastPkts_Type()
)
lightStreamBrPortDroppedBcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lightStreamBrPortDroppedBcastPkts.setStatus("mandatory")
_LightStreamBridgeFilterTable_Object = MibTable
lightStreamBridgeFilterTable = _LightStreamBridgeFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 711, 3, 1, 2)
)
if mibBuilder.loadTexts:
    lightStreamBridgeFilterTable.setStatus("mandatory")
_LightStreamBridgeFilterEntry_Object = MibTableRow
lightStreamBridgeFilterEntry = _LightStreamBridgeFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 711, 3, 1, 2, 1)
)
lightStreamBridgeFilterEntry.setIndexNames(
    (0, "LIGHTSTREAM-MIB", "lightStreamBrFilterId"),
    (0, "LIGHTSTREAM-MIB", "lightStreamBrFilterTokenIndex"),
)
if mibBuilder.loadTexts:
    lightStreamBridgeFilterEntry.setStatus("mandatory")


class _LightStreamBrFilterId_Type(Integer32):
    """Custom type lightStreamBrFilterId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_LightStreamBrFilterId_Type.__name__ = "Integer32"
_LightStreamBrFilterId_Object = MibTableColumn
lightStreamBrFilterId = _LightStreamBrFilterId_Object(
    (1, 3, 6, 1, 4, 1, 711, 3, 1, 2, 1, 1),
    _LightStreamBrFilterId_Type()
)
lightStreamBrFilterId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lightStreamBrFilterId.setStatus("mandatory")
_LightStreamBrFilterTokenIndex_Type = Integer32
_LightStreamBrFilterTokenIndex_Object = MibTableColumn
lightStreamBrFilterTokenIndex = _LightStreamBrFilterTokenIndex_Object(
    (1, 3, 6, 1, 4, 1, 711, 3, 1, 2, 1, 2),
    _LightStreamBrFilterTokenIndex_Type()
)
lightStreamBrFilterTokenIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lightStreamBrFilterTokenIndex.setStatus("mandatory")


class _LightStreamBrFilterTokenType_Type(Integer32):
    """Custom type lightStreamBrFilterTokenType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("etherType", 4),
          ("frameField", 2),
          ("llcSAPType", 5),
          ("macAddrType", 3),
          ("operation", 1),
          ("reserved", 6),
          ("snapOuiType", 7))
    )


_LightStreamBrFilterTokenType_Type.__name__ = "Integer32"
_LightStreamBrFilterTokenType_Object = MibTableColumn
lightStreamBrFilterTokenType = _LightStreamBrFilterTokenType_Object(
    (1, 3, 6, 1, 4, 1, 711, 3, 1, 2, 1, 3),
    _LightStreamBrFilterTokenType_Type()
)
lightStreamBrFilterTokenType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lightStreamBrFilterTokenType.setStatus("mandatory")
_LightStreamBrFilterTokenValue_Type = DisplayString
_LightStreamBrFilterTokenValue_Object = MibTableColumn
lightStreamBrFilterTokenValue = _LightStreamBrFilterTokenValue_Object(
    (1, 3, 6, 1, 4, 1, 711, 3, 1, 2, 1, 4),
    _LightStreamBrFilterTokenValue_Type()
)
lightStreamBrFilterTokenValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lightStreamBrFilterTokenValue.setStatus("mandatory")


class _LightStreamBrFilterStatus_Type(Integer32):
    """Custom type lightStreamBrFilterStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4)
        )
    )
    namedValues = NamedValues(
        *(("complete", 1),
          ("delete", 2),
          ("intermediateToken", 4))
    )


_LightStreamBrFilterStatus_Type.__name__ = "Integer32"
_LightStreamBrFilterStatus_Object = MibTableColumn
lightStreamBrFilterStatus = _LightStreamBrFilterStatus_Object(
    (1, 3, 6, 1, 4, 1, 711, 3, 1, 2, 1, 5),
    _LightStreamBrFilterStatus_Type()
)
lightStreamBrFilterStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lightStreamBrFilterStatus.setStatus("mandatory")
_LightStreamBridgeFilterParameterTable_Object = MibTable
lightStreamBridgeFilterParameterTable = _LightStreamBridgeFilterParameterTable_Object(
    (1, 3, 6, 1, 4, 1, 711, 3, 1, 3)
)
if mibBuilder.loadTexts:
    lightStreamBridgeFilterParameterTable.setStatus("mandatory")
_LightStreamBridgeFilterParameterEntry_Object = MibTableRow
lightStreamBridgeFilterParameterEntry = _LightStreamBridgeFilterParameterEntry_Object(
    (1, 3, 6, 1, 4, 1, 711, 3, 1, 3, 1)
)
lightStreamBridgeFilterParameterEntry.setIndexNames(
    (0, "LIGHTSTREAM-MIB", "lightStreamBrFilterParmPort"),
    (0, "LIGHTSTREAM-MIB", "lightStreamBrFilterParmFilterId"),
)
if mibBuilder.loadTexts:
    lightStreamBridgeFilterParameterEntry.setStatus("mandatory")
_LightStreamBrFilterParmPort_Type = Integer32
_LightStreamBrFilterParmPort_Object = MibTableColumn
lightStreamBrFilterParmPort = _LightStreamBrFilterParmPort_Object(
    (1, 3, 6, 1, 4, 1, 711, 3, 1, 3, 1, 1),
    _LightStreamBrFilterParmPort_Type()
)
lightStreamBrFilterParmPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lightStreamBrFilterParmPort.setStatus("mandatory")
_LightStreamBrFilterParmFilterId_Type = Integer32
_LightStreamBrFilterParmFilterId_Object = MibTableColumn
lightStreamBrFilterParmFilterId = _LightStreamBrFilterParmFilterId_Object(
    (1, 3, 6, 1, 4, 1, 711, 3, 1, 3, 1, 2),
    _LightStreamBrFilterParmFilterId_Type()
)
lightStreamBrFilterParmFilterId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lightStreamBrFilterParmFilterId.setStatus("mandatory")
_LightStreamBrFilterParmFilterPriority_Type = Integer32
_LightStreamBrFilterParmFilterPriority_Object = MibTableColumn
lightStreamBrFilterParmFilterPriority = _LightStreamBrFilterParmFilterPriority_Object(
    (1, 3, 6, 1, 4, 1, 711, 3, 1, 3, 1, 3),
    _LightStreamBrFilterParmFilterPriority_Type()
)
lightStreamBrFilterParmFilterPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lightStreamBrFilterParmFilterPriority.setStatus("mandatory")
_LightStreamBrFilterParmAction_Type = LightStreamFilterAction
_LightStreamBrFilterParmAction_Object = MibTableColumn
lightStreamBrFilterParmAction = _LightStreamBrFilterParmAction_Object(
    (1, 3, 6, 1, 4, 1, 711, 3, 1, 3, 1, 4),
    _LightStreamBrFilterParmAction_Type()
)
lightStreamBrFilterParmAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lightStreamBrFilterParmAction.setStatus("mandatory")
_LightStreamBrFilterParmMatchCounts_Type = Counter32
_LightStreamBrFilterParmMatchCounts_Object = MibTableColumn
lightStreamBrFilterParmMatchCounts = _LightStreamBrFilterParmMatchCounts_Object(
    (1, 3, 6, 1, 4, 1, 711, 3, 1, 3, 1, 5),
    _LightStreamBrFilterParmMatchCounts_Type()
)
lightStreamBrFilterParmMatchCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lightStreamBrFilterParmMatchCounts.setStatus("mandatory")
_LightStreamBrFilterParmValidation_Type = LightStreamValidation
_LightStreamBrFilterParmValidation_Object = MibTableColumn
lightStreamBrFilterParmValidation = _LightStreamBrFilterParmValidation_Object(
    (1, 3, 6, 1, 4, 1, 711, 3, 1, 3, 1, 6),
    _LightStreamBrFilterParmValidation_Type()
)
lightStreamBrFilterParmValidation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lightStreamBrFilterParmValidation.setStatus("mandatory")
_LightStreamBrStaticGoToCardSize_Type = Integer32
_LightStreamBrStaticGoToCardSize_Object = MibScalar
lightStreamBrStaticGoToCardSize = _LightStreamBrStaticGoToCardSize_Object(
    (1, 3, 6, 1, 4, 1, 711, 3, 1, 4),
    _LightStreamBrStaticGoToCardSize_Type()
)
lightStreamBrStaticGoToCardSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lightStreamBrStaticGoToCardSize.setStatus("mandatory")
_LightStreamVli_ObjectIdentity = ObjectIdentity
lightStreamVli = _LightStreamVli_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 711, 4)
)


class _LightStreamVliVersion_Type(Integer32):
    """Custom type lightStreamVliVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("version-1", 1)
    )


_LightStreamVliVersion_Type.__name__ = "Integer32"
_LightStreamVliVersion_Object = MibScalar
lightStreamVliVersion = _LightStreamVliVersion_Object(
    (1, 3, 6, 1, 4, 1, 711, 4, 1),
    _LightStreamVliVersion_Type()
)
lightStreamVliVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lightStreamVliVersion.setStatus("mandatory")
_LightStreamVliPortCtlTable_Object = MibTable
lightStreamVliPortCtlTable = _LightStreamVliPortCtlTable_Object(
    (1, 3, 6, 1, 4, 1, 711, 4, 4)
)
if mibBuilder.loadTexts:
    lightStreamVliPortCtlTable.setStatus("mandatory")
_LightStreamVliPortCtlEntry_Object = MibTableRow
lightStreamVliPortCtlEntry = _LightStreamVliPortCtlEntry_Object(
    (1, 3, 6, 1, 4, 1, 711, 4, 4, 1)
)
lightStreamVliPortCtlEntry.setIndexNames(
    (0, "LIGHTSTREAM-MIB", "lightStreamVliPortCtlPort"),
)
if mibBuilder.loadTexts:
    lightStreamVliPortCtlEntry.setStatus("mandatory")
_LightStreamVliPortCtlPort_Type = Integer32
_LightStreamVliPortCtlPort_Object = MibTableColumn
lightStreamVliPortCtlPort = _LightStreamVliPortCtlPort_Object(
    (1, 3, 6, 1, 4, 1, 711, 4, 4, 1, 1),
    _LightStreamVliPortCtlPort_Type()
)
lightStreamVliPortCtlPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lightStreamVliPortCtlPort.setStatus("mandatory")


class _LightStreamVliPortCtlMode_Type(Integer32):
    """Custom type lightStreamVliPortCtlMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("exclude", 2),
          ("include", 1))
    )


_LightStreamVliPortCtlMode_Type.__name__ = "Integer32"
_LightStreamVliPortCtlMode_Object = MibTableColumn
lightStreamVliPortCtlMode = _LightStreamVliPortCtlMode_Object(
    (1, 3, 6, 1, 4, 1, 711, 4, 4, 1, 2),
    _LightStreamVliPortCtlMode_Type()
)
lightStreamVliPortCtlMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lightStreamVliPortCtlMode.setStatus("mandatory")
_LightStreamVliPortWorkGroupTable_Object = MibTable
lightStreamVliPortWorkGroupTable = _LightStreamVliPortWorkGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 711, 4, 5)
)
if mibBuilder.loadTexts:
    lightStreamVliPortWorkGroupTable.setStatus("mandatory")
_LightStreamVliPortWorkGroupEntry_Object = MibTableRow
lightStreamVliPortWorkGroupEntry = _LightStreamVliPortWorkGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 711, 4, 5, 1)
)
lightStreamVliPortWorkGroupEntry.setIndexNames(
    (0, "LIGHTSTREAM-MIB", "lightStreamVliPortWorkGroupPort"),
    (0, "LIGHTSTREAM-MIB", "lightStreamVliPortWorkGroupID"),
)
if mibBuilder.loadTexts:
    lightStreamVliPortWorkGroupEntry.setStatus("mandatory")
_LightStreamVliPortWorkGroupPort_Type = Integer32
_LightStreamVliPortWorkGroupPort_Object = MibTableColumn
lightStreamVliPortWorkGroupPort = _LightStreamVliPortWorkGroupPort_Object(
    (1, 3, 6, 1, 4, 1, 711, 4, 5, 1, 1),
    _LightStreamVliPortWorkGroupPort_Type()
)
lightStreamVliPortWorkGroupPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lightStreamVliPortWorkGroupPort.setStatus("mandatory")


class _LightStreamVliPortWorkGroupID_Type(Integer32):
    """Custom type lightStreamVliPortWorkGroupID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_LightStreamVliPortWorkGroupID_Type.__name__ = "Integer32"
_LightStreamVliPortWorkGroupID_Object = MibTableColumn
lightStreamVliPortWorkGroupID = _LightStreamVliPortWorkGroupID_Object(
    (1, 3, 6, 1, 4, 1, 711, 4, 5, 1, 2),
    _LightStreamVliPortWorkGroupID_Type()
)
lightStreamVliPortWorkGroupID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lightStreamVliPortWorkGroupID.setStatus("mandatory")
_LightStreamVliPortWorkGroupValidation_Type = LightStreamValidation
_LightStreamVliPortWorkGroupValidation_Object = MibTableColumn
lightStreamVliPortWorkGroupValidation = _LightStreamVliPortWorkGroupValidation_Object(
    (1, 3, 6, 1, 4, 1, 711, 4, 5, 1, 3),
    _LightStreamVliPortWorkGroupValidation_Type()
)
lightStreamVliPortWorkGroupValidation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lightStreamVliPortWorkGroupValidation.setStatus("mandatory")
_LightStreamEOM_ObjectIdentity = ObjectIdentity
lightStreamEOM = _LightStreamEOM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 711, 1000)
)
_LightStreamEndOfMib_Type = Integer32
_LightStreamEndOfMib_Object = MibScalar
lightStreamEndOfMib = _LightStreamEndOfMib_Object(
    (1, 3, 6, 1, 4, 1, 711, 1000, 1),
    _LightStreamEndOfMib_Type()
)
lightStreamEndOfMib.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lightStreamEndOfMib.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "LIGHTSTREAM-MIB",
    **{"LightStreamStatus": LightStreamStatus,
       "LightStreamValidation": LightStreamValidation,
       "LightStreamFilterAction": LightStreamFilterAction,
       "LightStreamUpToMaxAge": LightStreamUpToMaxAge,
       "LightStreamDLCI": LightStreamDLCI,
       "VCI": VCI,
       "lightStream": lightStream,
       "lightStreamOIDs": lightStreamOIDs,
       "lightStreamATM": lightStreamATM,
       "lsOther": lsOther,
       "lsTrapNumber": lsTrapNumber,
       "lsTrapText": lsTrapText,
       "lsTrapName": lsTrapName,
       "lsConfig": lsConfig,
       "lightStreamProducts": lightStreamProducts,
       "atmSwitch": atmSwitch,
       "chassisInfo": chassisInfo,
       "chassisId": chassisId,
       "chassisActiveIpAddr": chassisActiveIpAddr,
       "chassisSecondaryIpAddr": chassisSecondaryIpAddr,
       "chassisNetworkMask": chassisNetworkMask,
       "chassisEthernetIpAddr": chassisEthernetIpAddr,
       "chassisEthernetIpMask": chassisEthernetIpMask,
       "chassisDefaultIpRouter": chassisDefaultIpRouter,
       "chassisStatusWord": chassisStatusWord,
       "chassisConsoleTrapLevel": chassisConsoleTrapLevel,
       "cardInfo": cardInfo,
       "cardTable": cardTable,
       "cardEntry": cardEntry,
       "cardIndex": cardIndex,
       "cardName": cardName,
       "cardBoardType": cardBoardType,
       "cardLcSoftwareVersion": cardLcSoftwareVersion,
       "cardLccSoftwareVersion": cardLccSoftwareVersion,
       "cardPID": cardPID,
       "cardMaxVCs": cardMaxVCs,
       "cardOperStatus": cardOperStatus,
       "cardAdminStatus": cardAdminStatus,
       "cardStatusWord": cardStatusWord,
       "cardConfigRegister": cardConfigRegister,
       "portInfo": portInfo,
       "portInfoTable": portInfoTable,
       "portInfoEntry": portInfoEntry,
       "portInfoIndex": portInfoIndex,
       "portInfoType": portInfoType,
       "portInfoSpecific": portInfoSpecific,
       "portInfoName": portInfoName,
       "portInfoErrorLimit": portInfoErrorLimit,
       "portTransmission": portTransmission,
       "ls1InfoTable": ls1InfoTable,
       "ls1InfoEntry": ls1InfoEntry,
       "ls1InfoIfIndex": ls1InfoIfIndex,
       "ls1InfoType": ls1InfoType,
       "ls1InfoOperCsuType": ls1InfoOperCsuType,
       "ls1InfoAdminCsuType": ls1InfoAdminCsuType,
       "ls1InfoOperRcvBaudRate": ls1InfoOperRcvBaudRate,
       "ls1InfoAdminRcvBaudRate": ls1InfoAdminRcvBaudRate,
       "ls1InfoOperXmitBaudRate": ls1InfoOperXmitBaudRate,
       "ls1InfoAdminXmitBaudRate": ls1InfoAdminXmitBaudRate,
       "ls1InfoOperNetIntType": ls1InfoOperNetIntType,
       "ls1InfoAdminNetIntType": ls1InfoAdminNetIntType,
       "ls1InfoOperModemState": ls1InfoOperModemState,
       "ls1InfoOperProtocol": ls1InfoOperProtocol,
       "ls1InfoAdminProtocol": ls1InfoAdminProtocol,
       "ls1InfoOperControlBandwidthSize": ls1InfoOperControlBandwidthSize,
       "ls1InfoAdminControlBandwidthSize": ls1InfoAdminControlBandwidthSize,
       "ls1InfoOperDataBandwidthSize": ls1InfoOperDataBandwidthSize,
       "ls1InfoAdminDataBandwidthSize": ls1InfoAdminDataBandwidthSize,
       "ls1InfoOperLoopMode": ls1InfoOperLoopMode,
       "ls1InfoAdminLoopMode": ls1InfoAdminLoopMode,
       "ls1InfoLcAutoEnable": ls1InfoLcAutoEnable,
       "ls1InfoLcDebugLevel": ls1InfoLcDebugLevel,
       "ls1InfoDataCellCapacity": ls1InfoDataCellCapacity,
       "ls1InfoDataCellAvailable": ls1InfoDataCellAvailable,
       "ls1InfoMeasuredBaudRate": ls1InfoMeasuredBaudRate,
       "ls1InfoLinkUtilization": ls1InfoLinkUtilization,
       "ls1InfoAdminOperTrigger": ls1InfoAdminOperTrigger,
       "ms1InfoTable": ms1InfoTable,
       "ms1InfoEntry": ms1InfoEntry,
       "ms1InfoIfIndex": ms1InfoIfIndex,
       "ms1InfoOperCableLength": ms1InfoOperCableLength,
       "ms1InfoAdminCableLength": ms1InfoAdminCableLength,
       "ms1InfoOperProtocol": ms1InfoOperProtocol,
       "ms1InfoAdminProtocol": ms1InfoAdminProtocol,
       "ms1InfoOperControlBandwidthSize": ms1InfoOperControlBandwidthSize,
       "ms1InfoAdminControlBandwidthSize": ms1InfoAdminControlBandwidthSize,
       "ms1InfoOperDataBandwidthSize": ms1InfoOperDataBandwidthSize,
       "ms1InfoAdminDataBandwidthSize": ms1InfoAdminDataBandwidthSize,
       "ms1InfoLcAutoEnable": ms1InfoLcAutoEnable,
       "ms1InfoLcDebugLevel": ms1InfoLcDebugLevel,
       "ms1InfoOperScramble": ms1InfoOperScramble,
       "ms1InfoAdminScramble": ms1InfoAdminScramble,
       "ms1InfoDataCellCapacity": ms1InfoDataCellCapacity,
       "ms1InfoDataCellAvailable": ms1InfoDataCellAvailable,
       "ms1InfoLinkUtilization": ms1InfoLinkUtilization,
       "ms1InfoOperFraming": ms1InfoOperFraming,
       "ms1InfoAdminOperTrigger": ms1InfoAdminOperTrigger,
       "npInfoTable": npInfoTable,
       "npInfoEntry": npInfoEntry,
       "npInfoIfIndex": npInfoIfIndex,
       "npInfoIPCommittedRate": npInfoIPCommittedRate,
       "npInfoIPCommittedBurst": npInfoIPCommittedBurst,
       "npInfoIPExcessRate": npInfoIPExcessRate,
       "npInfoIPExcessBurst": npInfoIPExcessBurst,
       "npInfoIPNCircuits": npInfoIPNCircuits,
       "npInfoAdminOperTrigger": npInfoAdminOperTrigger,
       "clc1InfoTable": clc1InfoTable,
       "clc1InfoEntry": clc1InfoEntry,
       "clc1InfoIfIndex": clc1InfoIfIndex,
       "clc1InfoOperProtocol": clc1InfoOperProtocol,
       "clc1InfoAdminProtocol": clc1InfoAdminProtocol,
       "clc1InfoOperLoopMode": clc1InfoOperLoopMode,
       "clc1InfoAdminLoopMode": clc1InfoAdminLoopMode,
       "clc1InfoOperControlBandwidthSize": clc1InfoOperControlBandwidthSize,
       "clc1InfoAdminControlBandwidthSize": clc1InfoAdminControlBandwidthSize,
       "clc1InfoOperDataBandwidthSize": clc1InfoOperDataBandwidthSize,
       "clc1InfoAdminDataBandwidthSize": clc1InfoAdminDataBandwidthSize,
       "clc1InfoLcAutoEnable": clc1InfoLcAutoEnable,
       "clc1InfoLcDebugLevel": clc1InfoLcDebugLevel,
       "clc1InfoOperScramble": clc1InfoOperScramble,
       "clc1InfoAdminScramble": clc1InfoAdminScramble,
       "clc1InfoDataCellCapacity": clc1InfoDataCellCapacity,
       "clc1InfoDataCellAvailable": clc1InfoDataCellAvailable,
       "clc1InfoLinkUtilization": clc1InfoLinkUtilization,
       "clc1InfoOperClock": clc1InfoOperClock,
       "clc1InfoAdminClock": clc1InfoAdminClock,
       "clc1InfoAdminOperTrigger": clc1InfoAdminOperTrigger,
       "oc3InfoTable": oc3InfoTable,
       "oc3InfoEntry": oc3InfoEntry,
       "oc3InfoReceiveSignalDetect": oc3InfoReceiveSignalDetect,
       "oc3InfoTransmitSafetySwitch": oc3InfoTransmitSafetySwitch,
       "oc3InfoMediumType": oc3InfoMediumType,
       "congestionAvoidance": congestionAvoidance,
       "caMaxIntervalPermitLimit": caMaxIntervalPermitLimit,
       "caMinIntervalPermitLimit": caMinIntervalPermitLimit,
       "caMinIntervalCaInfo": caMinIntervalCaInfo,
       "mmaInfo": mmaInfo,
       "mmaDbActive": mmaDbActive,
       "mmaTrapFilter": mmaTrapFilter,
       "mmaTrapLanguage": mmaTrapLanguage,
       "mmaCollectionSpace": mmaCollectionSpace,
       "mmaConfigHost": mmaConfigHost,
       "mmaConfigAuthor": mmaConfigAuthor,
       "mmaConfigID": mmaConfigID,
       "mmaSetLock": mmaSetLock,
       "mmaPID": mmaPID,
       "mmaTrapLog": mmaTrapLog,
       "mmaTrapNumber": mmaTrapNumber,
       "mmaTrapOnOffState": mmaTrapOnOffState,
       "mmaNumNameTable": mmaNumNameTable,
       "mmaNumNameEntry": mmaNumNameEntry,
       "mmaNumNameNumber": mmaNumNameNumber,
       "mmaNumName": mmaNumName,
       "mmaLwmpTimeouts": mmaLwmpTimeouts,
       "collectInfo": collectInfo,
       "collectTable": collectTable,
       "collectEntry": collectEntry,
       "collectIndex": collectIndex,
       "collectStatus": collectStatus,
       "collectStart": collectStart,
       "collectFinish": collectFinish,
       "collectInterval": collectInterval,
       "collectFileName": collectFileName,
       "collectFileSize": collectFileSize,
       "collectOperStatus": collectOperStatus,
       "collectDataBase": collectDataBase,
       "collectDbEntry": collectDbEntry,
       "collectDBIndex": collectDBIndex,
       "collectDBInstance": collectDBInstance,
       "collectDBObjectID": collectDBObjectID,
       "collectDBStatus": collectDBStatus,
       "collectCommunityName": collectCommunityName,
       "rmonCommunityName": rmonCommunityName,
       "lsPortProtocols": lsPortProtocols,
       "edgePort": edgePort,
       "edgePortTable": edgePortTable,
       "edgePortEntry": edgePortEntry,
       "edgeIfIndex": edgeIfIndex,
       "edgeUpcType": edgeUpcType,
       "edgeUserDataPerCell": edgeUserDataPerCell,
       "edgeCellDelayVariance": edgeCellDelayVariance,
       "edgePrincipalScale": edgePrincipalScale,
       "edgeSecondaryScale": edgeSecondaryScale,
       "edgeMeteringFactor": edgeMeteringFactor,
       "edgeMeteringBurstSize": edgeMeteringBurstSize,
       "edgeCallSetupRetry": edgeCallSetupRetry,
       "edgeCallSetupBackoff": edgeCallSetupBackoff,
       "edgeMaxFrameSize": edgeMaxFrameSize,
       "frDceInfo": frDceInfo,
       "frProvMiTable": frProvMiTable,
       "frProvMiEntry": frProvMiEntry,
       "frProvMiIfIndex": frProvMiIfIndex,
       "frProvMiState": frProvMiState,
       "frProvMiAddressLen": frProvMiAddressLen,
       "frProvMiNetRequestInterval": frProvMiNetRequestInterval,
       "frProvMiNetErrorThreshold": frProvMiNetErrorThreshold,
       "frProvMiNetMonitoredEvents": frProvMiNetMonitoredEvents,
       "frProvMiMaxSupportedVCs": frProvMiMaxSupportedVCs,
       "frProvMiMulticast": frProvMiMulticast,
       "frProvMiUserPollingInterval": frProvMiUserPollingInterval,
       "frProvMiUserFullEnquiryInterval": frProvMiUserFullEnquiryInterval,
       "frProvMiUserErrorThreshold": frProvMiUserErrorThreshold,
       "frProvMiUserMonitoredEvents": frProvMiUserMonitoredEvents,
       "frProvMiNetInterfaceType": frProvMiNetInterfaceType,
       "frCktInfo": frCktInfo,
       "frCktCfgTable": frCktCfgTable,
       "frCktEntry": frCktEntry,
       "frCktSrcNode": frCktSrcNode,
       "frCktSrcIfIndex": frCktSrcIfIndex,
       "frCktSrcDlci": frCktSrcDlci,
       "frCktAdminDestNode": frCktAdminDestNode,
       "frCktOperDestNode": frCktOperDestNode,
       "frCktAdminDestIfIndex": frCktAdminDestIfIndex,
       "frCktOperDestIfIndex": frCktOperDestIfIndex,
       "frCktAdminDestDlci": frCktAdminDestDlci,
       "frCktOperDestDlci": frCktOperDestDlci,
       "frCktAdminSrcInsuredRate": frCktAdminSrcInsuredRate,
       "frCktOperSrcInsuredRate": frCktOperSrcInsuredRate,
       "frCktAdminSrcInsuredBurst": frCktAdminSrcInsuredBurst,
       "frCktOperSrcInsuredBurst": frCktOperSrcInsuredBurst,
       "frCktAdminSrcMaxRate": frCktAdminSrcMaxRate,
       "frCktOperSrcMaxRate": frCktOperSrcMaxRate,
       "frCktAdminSrcMaxBurst": frCktAdminSrcMaxBurst,
       "frCktOperSrcMaxBurst": frCktOperSrcMaxBurst,
       "frCktAdminDestInsuredRate": frCktAdminDestInsuredRate,
       "frCktOperDestInsuredRate": frCktOperDestInsuredRate,
       "frCktAdminDestInsuredBurst": frCktAdminDestInsuredBurst,
       "frCktOperDestInsuredBurst": frCktOperDestInsuredBurst,
       "frCktAdminDestMaxRate": frCktAdminDestMaxRate,
       "frCktOperDestMaxRate": frCktOperDestMaxRate,
       "frCktAdminDestMaxBurst": frCktAdminDestMaxBurst,
       "frCktOperDestMaxBurst": frCktOperDestMaxBurst,
       "frCktOperSecondaryScale": frCktOperSecondaryScale,
       "frCktAdminSecondaryScale": frCktAdminSecondaryScale,
       "frCktOperPrinBwType": frCktOperPrinBwType,
       "frCktAdminPrinBwType": frCktAdminPrinBwType,
       "frCktOperTransPri": frCktOperTransPri,
       "frCktAdminTransPri": frCktAdminTransPri,
       "frCktOperUserDataPerCell": frCktOperUserDataPerCell,
       "frCktAdminUserDataPerCell": frCktAdminUserDataPerCell,
       "frCktStatus": frCktStatus,
       "frCktInfoTable": frCktInfoTable,
       "frCktInfoEntry": frCktInfoEntry,
       "frCktInfoIfIndex": frCktInfoIfIndex,
       "frCktInfoDlci": frCktInfoDlci,
       "frCktInfoLclLMI": frCktInfoLclLMI,
       "frCktInfoRmtLMI": frCktInfoRmtLMI,
       "frCktInfoCallIDIncoming": frCktInfoCallIDIncoming,
       "frCktInfoCallIDOutgoing": frCktInfoCallIDOutgoing,
       "frCktInfoDownstreamState": frCktInfoDownstreamState,
       "frCktInfoUpstreamState": frCktInfoUpstreamState,
       "frCktInfoLastAtmErr": frCktInfoLastAtmErr,
       "frCktInfoDataCellsRequired": frCktInfoDataCellsRequired,
       "frCktInfoLastAtmLocation": frCktInfoLastAtmLocation,
       "ffCktInfo": ffCktInfo,
       "ffCktCfgTable": ffCktCfgTable,
       "ffCktEntry": ffCktEntry,
       "ffCktSrcNode": ffCktSrcNode,
       "ffCktSrcIfIndex": ffCktSrcIfIndex,
       "ffCktAdminDestNode": ffCktAdminDestNode,
       "ffCktOperDestNode": ffCktOperDestNode,
       "ffCktAdminDestIfIndex": ffCktAdminDestIfIndex,
       "ffCktOperDestIfIndex": ffCktOperDestIfIndex,
       "ffCktAdminSrcInsuredRate": ffCktAdminSrcInsuredRate,
       "ffCktOperSrcInsuredRate": ffCktOperSrcInsuredRate,
       "ffCktAdminSrcInsuredBurst": ffCktAdminSrcInsuredBurst,
       "ffCktOperSrcInsuredBurst": ffCktOperSrcInsuredBurst,
       "ffCktAdminSrcMaxRate": ffCktAdminSrcMaxRate,
       "ffCktOperSrcMaxRate": ffCktOperSrcMaxRate,
       "ffCktAdminSrcMaxBurst": ffCktAdminSrcMaxBurst,
       "ffCktOperSrcMaxBurst": ffCktOperSrcMaxBurst,
       "ffCktAdminDestInsuredRate": ffCktAdminDestInsuredRate,
       "ffCktOperDestInsuredRate": ffCktOperDestInsuredRate,
       "ffCktAdminDestInsuredBurst": ffCktAdminDestInsuredBurst,
       "ffCktOperDestInsuredBurst": ffCktOperDestInsuredBurst,
       "ffCktAdminDestMaxRate": ffCktAdminDestMaxRate,
       "ffCktOperDestMaxRate": ffCktOperDestMaxRate,
       "ffCktAdminDestMaxBurst": ffCktAdminDestMaxBurst,
       "ffCktOperDestMaxBurst": ffCktOperDestMaxBurst,
       "ffCktOperPrinBwType": ffCktOperPrinBwType,
       "ffCktAdminPrinBwType": ffCktAdminPrinBwType,
       "ffCktOperTransPri": ffCktOperTransPri,
       "ffCktAdminTransPri": ffCktAdminTransPri,
       "ffCktStatus": ffCktStatus,
       "ffCktInfoTable": ffCktInfoTable,
       "ffCktInfoEntry": ffCktInfoEntry,
       "ffCktInfoIfIndex": ffCktInfoIfIndex,
       "ffCktInfoDownstreamState": ffCktInfoDownstreamState,
       "ffCktInfoUpstreamState": ffCktInfoUpstreamState,
       "ffCktInfoCallIDIncoming": ffCktInfoCallIDIncoming,
       "ffCktInfoCallIDOutgoing": ffCktInfoCallIDOutgoing,
       "ffCktInfoLastAtmErr": ffCktInfoLastAtmErr,
       "ffCktInfoDataCellsRequired": ffCktInfoDataCellsRequired,
       "ffCktInfoLastAtmLocation": ffCktInfoLastAtmLocation,
       "sUniCktInfo": sUniCktInfo,
       "sUniCktCfgTable": sUniCktCfgTable,
       "sUniCktEntry": sUniCktEntry,
       "sUniCktSrcNode": sUniCktSrcNode,
       "sUniCktSrcIfIndex": sUniCktSrcIfIndex,
       "sUniCktSrcVCI": sUniCktSrcVCI,
       "sUniCktAdminDestNode": sUniCktAdminDestNode,
       "sUniCktOperDestNode": sUniCktOperDestNode,
       "sUniCktAdminDestIfIndex": sUniCktAdminDestIfIndex,
       "sUniCktOperDestIfIndex": sUniCktOperDestIfIndex,
       "sUniCktAdminDestVCI": sUniCktAdminDestVCI,
       "sUniCktOperDestVCI": sUniCktOperDestVCI,
       "sUniCktOperPrinBwType": sUniCktOperPrinBwType,
       "sUniCktAdminPrinBwType": sUniCktAdminPrinBwType,
       "sUniCktOperTransPri": sUniCktOperTransPri,
       "sUniCktAdminTransPri": sUniCktAdminTransPri,
       "sUniCktAdminSrcInsuredRate": sUniCktAdminSrcInsuredRate,
       "sUniCktOperSrcInsuredRate": sUniCktOperSrcInsuredRate,
       "sUniCktAdminSrcInsuredBurst": sUniCktAdminSrcInsuredBurst,
       "sUniCktOperSrcInsuredBurst": sUniCktOperSrcInsuredBurst,
       "sUniCktAdminSrcMaxRate": sUniCktAdminSrcMaxRate,
       "sUniCktOperSrcMaxRate": sUniCktOperSrcMaxRate,
       "sUniCktAdminSrcMaxBurst": sUniCktAdminSrcMaxBurst,
       "sUniCktOperSrcMaxBurst": sUniCktOperSrcMaxBurst,
       "sUniCktAdminDestInsuredRate": sUniCktAdminDestInsuredRate,
       "sUniCktOperDestInsuredRate": sUniCktOperDestInsuredRate,
       "sUniCktAdminDestInsuredBurst": sUniCktAdminDestInsuredBurst,
       "sUniCktOperDestInsuredBurst": sUniCktOperDestInsuredBurst,
       "sUniCktAdminDestMaxRate": sUniCktAdminDestMaxRate,
       "sUniCktOperDestMaxRate": sUniCktOperDestMaxRate,
       "sUniCktAdminDestMaxBurst": sUniCktAdminDestMaxBurst,
       "sUniCktOperDestMaxBurst": sUniCktOperDestMaxBurst,
       "sUniCktAdminSecondaryScale": sUniCktAdminSecondaryScale,
       "sUniCktOperSecondaryScale": sUniCktOperSecondaryScale,
       "sUniCktSts": sUniCktSts,
       "sUniCktInfoTable": sUniCktInfoTable,
       "sUniCktInfoEntry": sUniCktInfoEntry,
       "sUniCktInfoIfIndex": sUniCktInfoIfIndex,
       "sUniCktInfoVCI": sUniCktInfoVCI,
       "sUniCktInfoUniToNetCallID": sUniCktInfoUniToNetCallID,
       "sUniCktInfoNetToUniCallID": sUniCktInfoNetToUniCallID,
       "sUniCktInfoUniToNetState": sUniCktInfoUniToNetState,
       "sUniCktInfoNetToUniState": sUniCktInfoNetToUniState,
       "sUniCktInfoLastAtmErr": sUniCktInfoLastAtmErr,
       "sUniCktInfoDataCellsRequired": sUniCktInfoDataCellsRequired,
       "sUniCktInfoLastAtmLocation": sUniCktInfoLastAtmLocation,
       "pvcInfo": pvcInfo,
       "pvcCfgTable": pvcCfgTable,
       "pvcEntry": pvcEntry,
       "pvcSrcIfIndex": pvcSrcIfIndex,
       "pvcSrcPvcId": pvcSrcPvcId,
       "pvcSrcNode": pvcSrcNode,
       "pvcSrcInsuredRate": pvcSrcInsuredRate,
       "pvcSrcInsuredBurst": pvcSrcInsuredBurst,
       "pvcSrcMaxRate": pvcSrcMaxRate,
       "pvcSrcMaxBurst": pvcSrcMaxBurst,
       "pvcSecondaryScale": pvcSecondaryScale,
       "pvcPrinBwType": pvcPrinBwType,
       "pvcTransPri": pvcTransPri,
       "pvcUserDataPerCell": pvcUserDataPerCell,
       "pvcStatus": pvcStatus,
       "mcEndptInfo": mcEndptInfo,
       "mcEndptCfgTable": mcEndptCfgTable,
       "mcEndptEntry": mcEndptEntry,
       "mcEndptLclIfIndex": mcEndptLclIfIndex,
       "mcEndptLclCktid": mcEndptLclCktid,
       "mcEndptLclInstance": mcEndptLclInstance,
       "mcEndptDest": mcEndptDest,
       "mcEndptServiceType": mcEndptServiceType,
       "mcEndptRmtVCstatus": mcEndptRmtVCstatus,
       "mcEndptCallIDIncoming": mcEndptCallIDIncoming,
       "mcEndptDownstreamState": mcEndptDownstreamState,
       "mcEndptUpstreamState": mcEndptUpstreamState,
       "mcEndptLastAtmErr": mcEndptLastAtmErr,
       "mcEndptLastAtmLocation": mcEndptLastAtmLocation,
       "mcEndptStatus": mcEndptStatus,
       "lsPrivate": lsPrivate,
       "lsExperimental": lsExperimental,
       "lsExperimentalStatistics": lsExperimentalStatistics,
       "lsEdgeStatistics": lsEdgeStatistics,
       "lsEdgeStatTable": lsEdgeStatTable,
       "lsEdgeStatEntry": lsEdgeStatEntry,
       "edgeStatIndex": edgeStatIndex,
       "edgeStatFsuRATOs": edgeStatFsuRATOs,
       "edgeStatFsuRATOLastInfo": edgeStatFsuRATOLastInfo,
       "edgeStatTsuHoldQCells": edgeStatTsuHoldQCells,
       "edgeStatTsuHoldQs": edgeStatTsuHoldQs,
       "tluAAL5XsumErrs": tluAAL5XsumErrs,
       "tluAAL5AbortErrs": tluAAL5AbortErrs,
       "tluAAL5ErrLastVci": tluAAL5ErrLastVci,
       "lsEdgePortStatTable": lsEdgePortStatTable,
       "lsEdgePortStatEntry": lsEdgePortStatEntry,
       "edgePortStatIndex": edgePortStatIndex,
       "edgePortRcvOctets": edgePortRcvOctets,
       "edgePortXmtOctets": edgePortXmtOctets,
       "edgePortFsuCksmErrMsgs": edgePortFsuCksmErrMsgs,
       "edgePortCksmErrLastVci": edgePortCksmErrLastVci,
       "edgePortDownXmtFrames": edgePortDownXmtFrames,
       "edgePortRcvUcastPkts": edgePortRcvUcastPkts,
       "edgePortRcvNUcastPkts": edgePortRcvNUcastPkts,
       "edgePortXmtUcastPkts": edgePortXmtUcastPkts,
       "edgePortXmtNUcastPkts": edgePortXmtNUcastPkts,
       "edgePortRcvSmplPktSize": edgePortRcvSmplPktSize,
       "edgePortXmtSmplPktSize": edgePortXmtSmplPktSize,
       "edgePortRcvL3XsumErrs": edgePortRcvL3XsumErrs,
       "edgePortRcvL3XsumErrLastVci": edgePortRcvL3XsumErrLastVci,
       "edgePortRcvCRCErrors": edgePortRcvCRCErrors,
       "edgePortRcvAborts": edgePortRcvAborts,
       "edgePortXmtUnderflows": edgePortXmtUnderflows,
       "edgePortRcvShortFrames": edgePortRcvShortFrames,
       "lsFrameRelayDlciStatTable": lsFrameRelayDlciStatTable,
       "lsFrameRelayDlciStatEntry": lsFrameRelayDlciStatEntry,
       "frameRelayDlciStatPortIndex": frameRelayDlciStatPortIndex,
       "frameRelayDlciStatDlciIndex": frameRelayDlciStatDlciIndex,
       "frameRelayDlciToSwCLP0Frames": frameRelayDlciToSwCLP0Frames,
       "frameRelayDlciToSwCLP0Cells": frameRelayDlciToSwCLP0Cells,
       "frameRelayDlciToSwCLP1Frames": frameRelayDlciToSwCLP1Frames,
       "frameRelayDlciToSwCLP1Cells": frameRelayDlciToSwCLP1Cells,
       "frameRelayDlciToSwDiscardFrames": frameRelayDlciToSwDiscardFrames,
       "frameRelayDlciToSwDiscardCells": frameRelayDlciToSwDiscardCells,
       "frameRelayDlciFrSwCLP0Frames": frameRelayDlciFrSwCLP0Frames,
       "frameRelayDlciFrSwCLP0Cells": frameRelayDlciFrSwCLP0Cells,
       "frameRelayDlciFrSwCLP1Frames": frameRelayDlciFrSwCLP1Frames,
       "frameRelayDlciFrSwCLP1Cells": frameRelayDlciFrSwCLP1Cells,
       "lsEdgePortToSwMsgLenTable": lsEdgePortToSwMsgLenTable,
       "lsEdgePortToSwMsgLenEntry": lsEdgePortToSwMsgLenEntry,
       "edgeToSwMsgLenPortIndex": edgeToSwMsgLenPortIndex,
       "edgeToSwMsgLenBinIndex": edgeToSwMsgLenBinIndex,
       "edgeToSwMsgLenMsgs": edgeToSwMsgLenMsgs,
       "lsEdgeSwToPortMsgLenTable": lsEdgeSwToPortMsgLenTable,
       "lsEdgeSwToPortMsgLenEntry": lsEdgeSwToPortMsgLenEntry,
       "edgeToPortMsgLenPortIndex": edgeToPortMsgLenPortIndex,
       "edgeToPortMsgLenBinIndex": edgeToPortMsgLenBinIndex,
       "edgeToPortMsgLenMsgs": edgeToPortMsgLenMsgs,
       "lsEdgeCpuWorkloadTable": lsEdgeCpuWorkloadTable,
       "lsEdgeCpuWorkloadEntry": lsEdgeCpuWorkloadEntry,
       "lsEdgeWorkloadCardIndex": lsEdgeWorkloadCardIndex,
       "lsEdgeWorkloadTypeIndex": lsEdgeWorkloadTypeIndex,
       "lsEdgeWorkloadEvents": lsEdgeWorkloadEvents,
       "lsFrameForwardStatTable": lsFrameForwardStatTable,
       "lsFrameForwardStatEntry": lsFrameForwardStatEntry,
       "frameForwardStatPortIndex": frameForwardStatPortIndex,
       "frameForwardToSwCLP0Frames": frameForwardToSwCLP0Frames,
       "frameForwardToSwCLP0Cells": frameForwardToSwCLP0Cells,
       "frameForwardToSwCLP1Frames": frameForwardToSwCLP1Frames,
       "frameForwardToSwCLP1Cells": frameForwardToSwCLP1Cells,
       "frameForwardToSwDiscardFrames": frameForwardToSwDiscardFrames,
       "frameForwardToSwDiscardCells": frameForwardToSwDiscardCells,
       "frameForwardFrSwCLP0Frames": frameForwardFrSwCLP0Frames,
       "frameForwardFrSwCLP0Cells": frameForwardFrSwCLP0Cells,
       "frameForwardFrSwCLP1Frames": frameForwardFrSwCLP1Frames,
       "frameForwardFrSwCLP1Cells": frameForwardFrSwCLP1Cells,
       "lsTrunkStatistics": lsTrunkStatistics,
       "lsTrunkPortStatTable": lsTrunkPortStatTable,
       "lsTrunkPortStatEntry": lsTrunkPortStatEntry,
       "trunkPortStatIndex": trunkPortStatIndex,
       "trunkPortRcvCells": trunkPortRcvCells,
       "trunkPortXmtCells": trunkPortXmtCells,
       "trunkPortRcvRuns": trunkPortRcvRuns,
       "trunkPortDownXmtCells": trunkPortDownXmtCells,
       "trunkPortRcvCRCErrors": trunkPortRcvCRCErrors,
       "trunkPortRcvAborts": trunkPortRcvAborts,
       "trunkPortXmtUnderflows": trunkPortXmtUnderflows,
       "trunkPortRcvShortFrames": trunkPortRcvShortFrames,
       "lsTrunkCpuWorkloadTable": lsTrunkCpuWorkloadTable,
       "lsTrunkCpuWorkloadEntry": lsTrunkCpuWorkloadEntry,
       "lsTrunkWorkloadCardIndex": lsTrunkWorkloadCardIndex,
       "lsTrunkWorkloadTypeIndex": lsTrunkWorkloadTypeIndex,
       "lsTrunkWorkloadEvents": lsTrunkWorkloadEvents,
       "lsLcStatistics": lsLcStatistics,
       "lcStatTable": lcStatTable,
       "lcStatEntry": lcStatEntry,
       "lcStatCardIndex": lcStatCardIndex,
       "tsuFreeCells": tsuFreeCells,
       "fsuSharedFreeCells": fsuSharedFreeCells,
       "tsuCellDropLastVci": tsuCellDropLastVci,
       "switchCellDgRejectEvents": switchCellDgRejectEvents,
       "switchCellSchedRejectEvents": switchCellSchedRejectEvents,
       "tsuErrFutQCellDrops": tsuErrFutQCellDrops,
       "tsuErrFutQMsgDropLastVci": tsuErrFutQMsgDropLastVci,
       "fsuHdrLrcErrs": fsuHdrLrcErrs,
       "fsuPayloadLrcErrs": fsuPayloadLrcErrs,
       "lcPortStatTable": lcPortStatTable,
       "lcPortStatEntry": lcPortStatEntry,
       "lcStatPortIndex": lcStatPortIndex,
       "fsuPortFreeCells": fsuPortFreeCells,
       "fsuCellDropLastCellHdr": fsuCellDropLastCellHdr,
       "tsuPortErrL1UnconfigVcis": tsuPortErrL1UnconfigVcis,
       "tsuPortErrL2UnconfigVcis": tsuPortErrL2UnconfigVcis,
       "tsuPortErrL1UnconfigLastVci": tsuPortErrL1UnconfigLastVci,
       "tsuPortErrL2UnconfigLastVci": tsuPortErrL2UnconfigLastVci,
       "tsuPortErrNonZeroGfc": tsuPortErrNonZeroGfc,
       "fsuPortXmtCellsTable": fsuPortXmtCellsTable,
       "fsuPortXmtCellsEntry": fsuPortXmtCellsEntry,
       "fsuXmtCellsPortIndex": fsuXmtCellsPortIndex,
       "fsuXmtCellsPriorityIndex": fsuXmtCellsPriorityIndex,
       "fsuXmtCellEvents": fsuXmtCellEvents,
       "fsuQueueCellLengthTable": fsuQueueCellLengthTable,
       "fsuQueueCellLenEntry": fsuQueueCellLenEntry,
       "fsuQueueCellLenPortIndex": fsuQueueCellLenPortIndex,
       "fsuQueueCellLenSubQIndex": fsuQueueCellLenSubQIndex,
       "fsuQueueCellLength": fsuQueueCellLength,
       "fsuDropEventTable": fsuDropEventTable,
       "fsuDropEventEntry": fsuDropEventEntry,
       "fsuDropEventPortIndex": fsuDropEventPortIndex,
       "fsuDropEventWatermarkIndex": fsuDropEventWatermarkIndex,
       "fsuDropEvents": fsuDropEvents,
       "lsFsuFastDropTable": lsFsuFastDropTable,
       "lsFsuFastDropEntry": lsFsuFastDropEntry,
       "lsFsuFastDropWatermarkIndex": lsFsuFastDropWatermarkIndex,
       "lsFsuFastCellDropEvents": lsFsuFastCellDropEvents,
       "tsuDropEventTable": tsuDropEventTable,
       "tsuDropEventEntry": tsuDropEventEntry,
       "tsuDropEventPortIndex": tsuDropEventPortIndex,
       "tsuDropEventWatermarkIndex": tsuDropEventWatermarkIndex,
       "tsuDropEvents": tsuDropEvents,
       "lsUtStatistics": lsUtStatistics,
       "lsLcFsuIntervalTable": lsLcFsuIntervalTable,
       "lsLcFsuIntervalEntry": lsLcFsuIntervalEntry,
       "lsLcIntervalPortIndex": lsLcIntervalPortIndex,
       "lsLcIntervalNumber": lsLcIntervalNumber,
       "lsLcIntervalPSDepth": lsLcIntervalPSDepth,
       "lsLcIntervalASDepth": lsLcIntervalASDepth,
       "lsLcIntervalDropEvents": lsLcIntervalDropEvents,
       "lsLcIntervalAvgCells": lsLcIntervalAvgCells,
       "lsLcIntervalPeakCells": lsLcIntervalPeakCells,
       "lsLcIntervalMinPermits": lsLcIntervalMinPermits,
       "lsLcIntervalAvgPermits": lsLcIntervalAvgPermits,
       "lsLcIntervalMaxPermits": lsLcIntervalMaxPermits,
       "lsLcIntervalDecrPermits": lsLcIntervalDecrPermits,
       "lsLcIntervalIncrPermits": lsLcIntervalIncrPermits,
       "lsLcIntervalMinBwAlloc": lsLcIntervalMinBwAlloc,
       "lsLcIntervalAvgBwAlloc": lsLcIntervalAvgBwAlloc,
       "lsLcIntervalMaxBwAlloc": lsLcIntervalMaxBwAlloc,
       "lsNpStatistics": lsNpStatistics,
       "lsNpCpuWorkloadTable": lsNpCpuWorkloadTable,
       "lsNpCpuWorkloadEntry": lsNpCpuWorkloadEntry,
       "lsNpCpuWorkloadIndex": lsNpCpuWorkloadIndex,
       "lsNpCpuWorkloadEvents": lsNpCpuWorkloadEvents,
       "lsCellStatistics": lsCellStatistics,
       "lsCellVciStatTable": lsCellVciStatTable,
       "lsCellVciStatEntry": lsCellVciStatEntry,
       "cellVciStatPortIndex": cellVciStatPortIndex,
       "cellVciStatVciIndex": cellVciStatVciIndex,
       "cellVciToSwCLP0Cells": cellVciToSwCLP0Cells,
       "cellVciToSwCLP01Cells": cellVciToSwCLP01Cells,
       "cellVciToSwCLP1Cells": cellVciToSwCLP1Cells,
       "cellVciToSwDiscardCells": cellVciToSwDiscardCells,
       "lsIR": lsIR,
       "irRoutingGroup": irRoutingGroup,
       "irRoutingPathsGenerated": irRoutingPathsGenerated,
       "irRoutingPathGenSuccess": irRoutingPathGenSuccess,
       "irRoutingPathGenFailedNoResources": irRoutingPathGenFailedNoResources,
       "irRoutingPathGenFailedUnknown": irRoutingPathGenFailedUnknown,
       "irRoutingPathGenFailedOther": irRoutingPathGenFailedOther,
       "irRoutingAveragePathLength": irRoutingAveragePathLength,
       "lsStatistics": lsStatistics,
       "tcsInfo": tcsInfo,
       "tcsTable": tcsTable,
       "tcsEntry": tcsEntry,
       "tcsIndex": tcsIndex,
       "tcsTemp1": tcsTemp1,
       "tcsTemp2": tcsTemp2,
       "tcsTcsVoltage": tcsTcsVoltage,
       "tcsVccVoltage": tcsVccVoltage,
       "tcsScsiVoltage": tcsScsiVoltage,
       "tcsPostResult": tcsPostResult,
       "tcsCardType": tcsCardType,
       "tcsPaddleTemp1": tcsPaddleTemp1,
       "tcsPaddleTemp2": tcsPaddleTemp2,
       "tcsPaddleWarnTemp1": tcsPaddleWarnTemp1,
       "tcsPaddleWarnTemp2": tcsPaddleWarnTemp2,
       "tcsPaddleShutdownTemp1": tcsPaddleShutdownTemp1,
       "tcsPaddleShutdownTemp2": tcsPaddleShutdownTemp2,
       "tcsWarnTemp1": tcsWarnTemp1,
       "tcsWarnTemp2": tcsWarnTemp2,
       "tcsShutdownTemp1": tcsShutdownTemp1,
       "tcsShutdownTemp2": tcsShutdownTemp2,
       "tcsFaultLight": tcsFaultLight,
       "tcsReadyLight": tcsReadyLight,
       "tcsSwitchConnectivityMask": tcsSwitchConnectivityMask,
       "tcsPrimarySwitch": tcsPrimarySwitch,
       "tcsPowerSupplyA": tcsPowerSupplyA,
       "tcsPowerSupplyB": tcsPowerSupplyB,
       "tcsPowerSupplyTypeA": tcsPowerSupplyTypeA,
       "tcsPowerSupplyTypeB": tcsPowerSupplyTypeB,
       "tcsSwitchFaultMaskA": tcsSwitchFaultMaskA,
       "tcsSwitchFaultMaskB": tcsSwitchFaultMaskB,
       "tcsSwitchCutoverSupport": tcsSwitchCutoverSupport,
       "tcsFCPrimarySwitchA": tcsFCPrimarySwitchA,
       "tcsFCPrimarySwitchB": tcsFCPrimarySwitchB,
       "lsGID": lsGID,
       "gidGeneralGroup": gidGeneralGroup,
       "gidSoftwareVersionNumber": gidSoftwareVersionNumber,
       "gidProcessID": gidProcessID,
       "gidUpTime": gidUpTime,
       "gidMemoryUse": gidMemoryUse,
       "gidTimersProcessed": gidTimersProcessed,
       "gidMallocFailures": gidMallocFailures,
       "gidDebugFlag": gidDebugFlag,
       "gidDebugLevel": gidDebugLevel,
       "gidAcceptedBcastRateIn": gidAcceptedBcastRateIn,
       "gidNbrGroup": gidNbrGroup,
       "gidNbrCount": gidNbrCount,
       "gidNbrTable": gidNbrTable,
       "gidNbrEntry": gidNbrEntry,
       "gidNbrEIA": gidNbrEIA,
       "gidNbrVCI": gidNbrVCI,
       "gidNbrState": gidNbrState,
       "gidNbrSyncEvents": gidNbrSyncEvents,
       "gidNbrDBReqListLength": gidNbrDBReqListLength,
       "gidNbrDBSumListLength": gidNbrDBSumListLength,
       "gidNbrHellosRx": gidNbrHellosRx,
       "gidNbrLinkAnnouncementsRx": gidNbrLinkAnnouncementsRx,
       "gidNbrNewLinkAnnouncementsRx": gidNbrNewLinkAnnouncementsRx,
       "gidNbrIPAnnouncementsRx": gidNbrIPAnnouncementsRx,
       "gidNbrNewIPAnnouncementsRx": gidNbrNewIPAnnouncementsRx,
       "gidNbrGenericAnnouncementsRx": gidNbrGenericAnnouncementsRx,
       "gidNbrNewGenericAnnouncementsRx": gidNbrNewGenericAnnouncementsRx,
       "gidClientGroup": gidClientGroup,
       "gidClientCount": gidClientCount,
       "gidClientTable": gidClientTable,
       "gidClientEntry": gidClientEntry,
       "gidClientID": gidClientID,
       "gidClientEIA": gidClientEIA,
       "gidClientAnnouncementsRx": gidClientAnnouncementsRx,
       "gidClientLinkAnnouncementsRx": gidClientLinkAnnouncementsRx,
       "gidClientIPAnnouncementsRx": gidClientIPAnnouncementsRx,
       "gidClientGenericAnnouncementsRx": gidClientGenericAnnouncementsRx,
       "gidClientEventsTx": gidClientEventsTx,
       "gidClientPathsGenerated": gidClientPathsGenerated,
       "gidIOGroup": gidIOGroup,
       "gidIONbrMsgBuffersFree": gidIONbrMsgBuffersFree,
       "gidIONbrMsgBuffersActive": gidIONbrMsgBuffersActive,
       "gidIOClientMsgBuffersFree": gidIOClientMsgBuffersFree,
       "gidIOClientMsgBuffersActive": gidIOClientMsgBuffersActive,
       "gidSyncGroup": gidSyncGroup,
       "gidSyncNbrsExistent": gidSyncNbrsExistent,
       "gidSyncNbrsExStart": gidSyncNbrsExStart,
       "gidSyncNbrsExchange": gidSyncNbrsExchange,
       "gidSyncNbrsLoading": gidSyncNbrsLoading,
       "gidSyncNbrsFull": gidSyncNbrsFull,
       "gidLinkGroup": gidLinkGroup,
       "gidLinkDatabaseSize": gidLinkDatabaseSize,
       "gidLineCardTable": gidLineCardTable,
       "gidLineCardEntry": gidLineCardEntry,
       "gidLineCardChassis": gidLineCardChassis,
       "gidLineCardSlot": gidLineCardSlot,
       "gidLineCardEntryAge": gidLineCardEntryAge,
       "gidLineCardEntrySeqno": gidLineCardEntrySeqno,
       "gidLineCardEntryAdvNP": gidLineCardEntryAdvNP,
       "gidLineCardPorts": gidLineCardPorts,
       "gidPortTable": gidPortTable,
       "gidPortEntry": gidPortEntry,
       "gidPortChassis": gidPortChassis,
       "gidPortID": gidPortID,
       "gidPortService": gidPortService,
       "gidPortUpDown": gidPortUpDown,
       "gidPortBW0": gidPortBW0,
       "gidPortBW1": gidPortBW1,
       "gidPortBW2": gidPortBW2,
       "gidPortRemoteChassis": gidPortRemoteChassis,
       "gidPortRemotePort": gidPortRemotePort,
       "gidIpAddressGroup": gidIpAddressGroup,
       "gidIpAddressDatabaseSize": gidIpAddressDatabaseSize,
       "gidIpAddressTable": gidIpAddressTable,
       "gidIpAddressEntry": gidIpAddressEntry,
       "gidInternalIpAddress": gidInternalIpAddress,
       "gidIpEntryAge": gidIpEntryAge,
       "gidIpEntrySeqno": gidIpEntrySeqno,
       "gidIpEntryAdvNP": gidIpEntryAdvNP,
       "gidIpEntryNetMask": gidIpEntryNetMask,
       "gidIpEntryEIA": gidIpEntryEIA,
       "gidEventGroup": gidEventGroup,
       "gidEventLinkEventsDelivered": gidEventLinkEventsDelivered,
       "gidEventIpEventsDelivered": gidEventIpEventsDelivered,
       "gidEventGenericGinfoEventsDelivered": gidEventGenericGinfoEventsDelivered,
       "gidEventGenericGinfoEventTable": gidEventGenericGinfoEventTable,
       "gidEventGenericGinfoEventCount": gidEventGenericGinfoEventCount,
       "gidEventDistributionGroup": gidEventDistributionGroup,
       "gidEventGenericGinfoEvents": gidEventGenericGinfoEvents,
       "lsPID": lsPID,
       "pidTable": pidTable,
       "pidEntry": pidEntry,
       "pidIndex": pidIndex,
       "pidName": pidName,
       "pidCreationTime": pidCreationTime,
       "pidOperStatus": pidOperStatus,
       "pidAdminStatus": pidAdminStatus,
       "lsND": lsND,
       "ndGeneralGroup": ndGeneralGroup,
       "ndSoftwareVersionNumber": ndSoftwareVersionNumber,
       "ndProcessID": ndProcessID,
       "ndMemoryUse": ndMemoryUse,
       "ndTimersProcessed": ndTimersProcessed,
       "ndLCGroup": ndLCGroup,
       "ndLCCount": ndLCCount,
       "ndLCTable": ndLCTable,
       "ndLCEntry": ndLCEntry,
       "ndLCEIA": ndLCEIA,
       "ndLCChannel": ndLCChannel,
       "ndLCState": ndLCState,
       "ndNbrGroup": ndNbrGroup,
       "ndNbrCount": ndNbrCount,
       "ndNbrTable": ndNbrTable,
       "ndNbrEntry": ndNbrEntry,
       "ndNbrEIA": ndNbrEIA,
       "ndNbrChannel": ndNbrChannel,
       "ndNbrState": ndNbrState,
       "ndSwudGroup": ndSwudGroup,
       "ndSwudTable": ndSwudTable,
       "ndSwudEntry": ndSwudEntry,
       "ndSwudIndex": ndSwudIndex,
       "ndOperIntvl": ndOperIntvl,
       "ndOperJ": ndOperJ,
       "ndOperK": ndOperK,
       "ndOperM": ndOperM,
       "ndOperN": ndOperN,
       "ndAdminIntvl": ndAdminIntvl,
       "ndAdminJ": ndAdminJ,
       "ndAdminK": ndAdminK,
       "ndAdminM": ndAdminM,
       "ndAdminN": ndAdminN,
       "ndTrigger": ndTrigger,
       "ndSwudStatsInputErrors": ndSwudStatsInputErrors,
       "ndSwudStatsTable": ndSwudStatsTable,
       "ndSwudStatsEntry": ndSwudStatsEntry,
       "ndSwudStatsIndex": ndSwudStatsIndex,
       "ndInputCells": ndInputCells,
       "ndInputErrs": ndInputErrs,
       "ndOutputCells": ndOutputCells,
       "ndOutputErrs": ndOutputErrs,
       "ndClientGroup": ndClientGroup,
       "ndClientCount": ndClientCount,
       "ndClientTable": ndClientTable,
       "ndClientEntry": ndClientEntry,
       "ndClientID": ndClientID,
       "ndClientType": ndClientType,
       "ndClientSubType": ndClientSubType,
       "ndClientEIA": ndClientEIA,
       "ndClientRegistration": ndClientRegistration,
       "ndInternalGroup": ndInternalGroup,
       "ndInternalDebugLevel": ndInternalDebugLevel,
       "ndInternalDebugFlags": ndInternalDebugFlags,
       "ndRedundancyGroup": ndRedundancyGroup,
       "ndPrimaryNP": ndPrimaryNP,
       "ndThisNP": ndThisNP,
       "ndForceToBackup": ndForceToBackup,
       "lwmaInfo": lwmaInfo,
       "lwmaTable": lwmaTable,
       "lwmaEntry": lwmaEntry,
       "lwmaIndex": lwmaIndex,
       "lwmaCreationTime": lwmaCreationTime,
       "lwmaTableNotification": lwmaTableNotification,
       "lwmaTrapLevel": lwmaTrapLevel,
       "lwmaTrapNumber": lwmaTrapNumber,
       "lwmaTrapOnOffState": lwmaTrapOnOffState,
       "lwmaTrapCliAlias": lwmaTrapCliAlias,
       "lightStreamInternet": lightStreamInternet,
       "lightStreamBridge": lightStreamBridge,
       "lightStreamBridgePortTable": lightStreamBridgePortTable,
       "lightStreamBridgePortEntry": lightStreamBridgePortEntry,
       "lightStreamBrPortPort": lightStreamBrPortPort,
       "lightStreamBrPortDefaultAction": lightStreamBrPortDefaultAction,
       "lightStreamBrPortBcastRateLimit": lightStreamBrPortBcastRateLimit,
       "lightStreamBrPortDroppedBcastPkts": lightStreamBrPortDroppedBcastPkts,
       "lightStreamBridgeFilterTable": lightStreamBridgeFilterTable,
       "lightStreamBridgeFilterEntry": lightStreamBridgeFilterEntry,
       "lightStreamBrFilterId": lightStreamBrFilterId,
       "lightStreamBrFilterTokenIndex": lightStreamBrFilterTokenIndex,
       "lightStreamBrFilterTokenType": lightStreamBrFilterTokenType,
       "lightStreamBrFilterTokenValue": lightStreamBrFilterTokenValue,
       "lightStreamBrFilterStatus": lightStreamBrFilterStatus,
       "lightStreamBridgeFilterParameterTable": lightStreamBridgeFilterParameterTable,
       "lightStreamBridgeFilterParameterEntry": lightStreamBridgeFilterParameterEntry,
       "lightStreamBrFilterParmPort": lightStreamBrFilterParmPort,
       "lightStreamBrFilterParmFilterId": lightStreamBrFilterParmFilterId,
       "lightStreamBrFilterParmFilterPriority": lightStreamBrFilterParmFilterPriority,
       "lightStreamBrFilterParmAction": lightStreamBrFilterParmAction,
       "lightStreamBrFilterParmMatchCounts": lightStreamBrFilterParmMatchCounts,
       "lightStreamBrFilterParmValidation": lightStreamBrFilterParmValidation,
       "lightStreamBrStaticGoToCardSize": lightStreamBrStaticGoToCardSize,
       "lightStreamVli": lightStreamVli,
       "lightStreamVliVersion": lightStreamVliVersion,
       "lightStreamVliPortCtlTable": lightStreamVliPortCtlTable,
       "lightStreamVliPortCtlEntry": lightStreamVliPortCtlEntry,
       "lightStreamVliPortCtlPort": lightStreamVliPortCtlPort,
       "lightStreamVliPortCtlMode": lightStreamVliPortCtlMode,
       "lightStreamVliPortWorkGroupTable": lightStreamVliPortWorkGroupTable,
       "lightStreamVliPortWorkGroupEntry": lightStreamVliPortWorkGroupEntry,
       "lightStreamVliPortWorkGroupPort": lightStreamVliPortWorkGroupPort,
       "lightStreamVliPortWorkGroupID": lightStreamVliPortWorkGroupID,
       "lightStreamVliPortWorkGroupValidation": lightStreamVliPortWorkGroupValidation,
       "lightStreamEOM": lightStreamEOM,
       "lightStreamEndOfMib": lightStreamEndOfMib}
)
