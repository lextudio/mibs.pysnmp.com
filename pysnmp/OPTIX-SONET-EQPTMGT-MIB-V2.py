# SNMP MIB module (OPTIX-SONET-EQPTMGT-MIB-V2) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/OPTIX-SONET-EQPTMGT-MIB-V2
# Produced by pysmi-1.5.4 at Mon Oct 14 22:35:29 2024
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

(optixProvisionSonet,) = mibBuilder.importSymbols(
    "OPTIX-OID-MIB",
    "optixProvisionSonet")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

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

optixsonetEqptMgt = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 20, 3)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class IntfType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              10,
              12,
              13,
              17,
              65,
              100,
              254)
        )
    )
    namedValues = NamedValues(
        *(("ds1-asyn-vt1", 1),
          ("ds3-asyn-sts1", 10),
          ("ds3-srv-ds1", 17),
          ("ds3-tmux-ds1", 13),
          ("ec", 12),
          ("invalid", 254),
          ("mix", 100),
          ("uas", 65))
    )



# MIB Managed Objects in the order of their OIDs

_OptixsonetCardInfoTable_Object = MibTable
optixsonetCardInfoTable = _OptixsonetCardInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 20, 3, 1)
)
if mibBuilder.loadTexts:
    optixsonetCardInfoTable.setStatus("current")
_OptixsonetCardInfoEntry_Object = MibTableRow
optixsonetCardInfoEntry = _OptixsonetCardInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 20, 3, 1, 1)
)
optixsonetCardInfoEntry.setIndexNames(
    (0, "OPTIX-SONET-EQPTMGT-MIB-V2", "cardIndexSlotId"),
    (0, "OPTIX-SONET-EQPTMGT-MIB-V2", "cardIndexSfpId"),
)
if mibBuilder.loadTexts:
    optixsonetCardInfoEntry.setStatus("current")
_CardIndexSlotId_Type = Gauge32
_CardIndexSlotId_Object = MibTableColumn
cardIndexSlotId = _CardIndexSlotId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 20, 3, 1, 1, 1),
    _CardIndexSlotId_Type()
)
cardIndexSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cardIndexSlotId.setStatus("current")
_CardIndexSfpId_Type = Gauge32
_CardIndexSfpId_Object = MibTableColumn
cardIndexSfpId = _CardIndexSfpId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 20, 3, 1, 1, 2),
    _CardIndexSfpId_Type()
)
cardIndexSfpId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cardIndexSfpId.setStatus("current")


class _CardProvisionType_Type(OctetString):
    """Custom type cardProvisionType based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_CardProvisionType_Type.__name__ = "OctetString"
_CardProvisionType_Object = MibTableColumn
cardProvisionType = _CardProvisionType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 20, 3, 1, 1, 3),
    _CardProvisionType_Type()
)
cardProvisionType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cardProvisionType.setStatus("current")


class _CardPhysicalType_Type(OctetString):
    """Custom type cardPhysicalType based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CardPhysicalType_Type.__name__ = "OctetString"
_CardPhysicalType_Object = MibTableColumn
cardPhysicalType = _CardPhysicalType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 20, 3, 1, 1, 4),
    _CardPhysicalType_Type()
)
cardPhysicalType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cardPhysicalType.setStatus("current")
_CardInterfaceType_Type = IntfType
_CardInterfaceType_Object = MibTableColumn
cardInterfaceType = _CardInterfaceType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 20, 3, 1, 1, 5),
    _CardInterfaceType_Type()
)
cardInterfaceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cardInterfaceType.setStatus("current")
_CardBandwidth_Type = Integer32
_CardBandwidth_Object = MibTableColumn
cardBandwidth = _CardBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 20, 3, 1, 1, 6),
    _CardBandwidth_Type()
)
cardBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cardBandwidth.setStatus("current")


class _CardSerialNum_Type(OctetString):
    """Custom type cardSerialNum based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CardSerialNum_Type.__name__ = "OctetString"
_CardSerialNum_Object = MibTableColumn
cardSerialNum = _CardSerialNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 20, 3, 1, 1, 7),
    _CardSerialNum_Type()
)
cardSerialNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cardSerialNum.setStatus("current")


class _CardCLEICode_Type(OctetString):
    """Custom type cardCLEICode based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_CardCLEICode_Type.__name__ = "OctetString"
_CardCLEICode_Object = MibTableColumn
cardCLEICode = _CardCLEICode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 20, 3, 1, 1, 8),
    _CardCLEICode_Type()
)
cardCLEICode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cardCLEICode.setStatus("current")


class _CardPartNum_Type(OctetString):
    """Custom type cardPartNum based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_CardPartNum_Type.__name__ = "OctetString"
_CardPartNum_Object = MibTableColumn
cardPartNum = _CardPartNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 20, 3, 1, 1, 9),
    _CardPartNum_Type()
)
cardPartNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cardPartNum.setStatus("current")


class _CardDOM_Type(OctetString):
    """Custom type cardDOM based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_CardDOM_Type.__name__ = "OctetString"
_CardDOM_Object = MibTableColumn
cardDOM = _CardDOM_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 20, 3, 1, 1, 10),
    _CardDOM_Type()
)
cardDOM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cardDOM.setStatus("current")


class _CardPCBVersion_Type(OctetString):
    """Custom type cardPCBVersion based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_CardPCBVersion_Type.__name__ = "OctetString"
_CardPCBVersion_Object = MibTableColumn
cardPCBVersion = _CardPCBVersion_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 20, 3, 1, 1, 11),
    _CardPCBVersion_Type()
)
cardPCBVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cardPCBVersion.setStatus("current")


class _CardSWVersion_Type(OctetString):
    """Custom type cardSWVersion based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CardSWVersion_Type.__name__ = "OctetString"
_CardSWVersion_Object = MibTableColumn
cardSWVersion = _CardSWVersion_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 20, 3, 1, 1, 12),
    _CardSWVersion_Type()
)
cardSWVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cardSWVersion.setStatus("current")


class _CardFPGAVersion_Type(OctetString):
    """Custom type cardFPGAVersion based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CardFPGAVersion_Type.__name__ = "OctetString"
_CardFPGAVersion_Object = MibTableColumn
cardFPGAVersion = _CardFPGAVersion_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 20, 3, 1, 1, 13),
    _CardFPGAVersion_Type()
)
cardFPGAVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cardFPGAVersion.setStatus("current")


class _CardEPLDVersion_Type(OctetString):
    """Custom type cardEPLDVersion based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_CardEPLDVersion_Type.__name__ = "OctetString"
_CardEPLDVersion_Object = MibTableColumn
cardEPLDVersion = _CardEPLDVersion_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 20, 3, 1, 1, 14),
    _CardEPLDVersion_Type()
)
cardEPLDVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cardEPLDVersion.setStatus("current")


class _CardBIOSVersion_Type(OctetString):
    """Custom type cardBIOSVersion based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CardBIOSVersion_Type.__name__ = "OctetString"
_CardBIOSVersion_Object = MibTableColumn
cardBIOSVersion = _CardBIOSVersion_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 20, 3, 1, 1, 15),
    _CardBIOSVersion_Type()
)
cardBIOSVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cardBIOSVersion.setStatus("current")


class _CardMAC_Type(OctetString):
    """Custom type cardMAC based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CardMAC_Type.__name__ = "OctetString"
_CardMAC_Object = MibTableColumn
cardMAC = _CardMAC_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 20, 3, 1, 1, 16),
    _CardMAC_Type()
)
cardMAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cardMAC.setStatus("current")


class _CardPSTState_Type(OctetString):
    """Custom type cardPSTState based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_CardPSTState_Type.__name__ = "OctetString"
_CardPSTState_Object = MibTableColumn
cardPSTState = _CardPSTState_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 20, 3, 1, 1, 17),
    _CardPSTState_Type()
)
cardPSTState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cardPSTState.setStatus("current")


class _CardSSTState_Type(OctetString):
    """Custom type cardSSTState based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CardSSTState_Type.__name__ = "OctetString"
_CardSSTState_Object = MibTableColumn
cardSSTState = _CardSSTState_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 20, 3, 1, 1, 18),
    _CardSSTState_Type()
)
cardSSTState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cardSSTState.setStatus("current")
_CardTPSPriority_Type = Gauge32
_CardTPSPriority_Object = MibTableColumn
cardTPSPriority = _CardTPSPriority_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 20, 3, 1, 1, 19),
    _CardTPSPriority_Type()
)
cardTPSPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cardTPSPriority.setStatus("current")


class _CardSwitchState_Type(Integer32):
    """Custom type cardSwitchState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              254,
              255)
        )
    )
    namedValues = NamedValues(
        *(("stateAUTOSW", 4),
          ("stateDNR", 1),
          ("stateFRCD", 5),
          ("stateIDLE", 255),
          ("stateINVALID", 254),
          ("stateLOCK", 6),
          ("stateMAN", 3),
          ("stateWTR", 2))
    )


_CardSwitchState_Type.__name__ = "Integer32"
_CardSwitchState_Object = MibTableColumn
cardSwitchState = _CardSwitchState_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 20, 3, 1, 1, 20),
    _CardSwitchState_Type()
)
cardSwitchState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cardSwitchState.setStatus("current")


class _CardDescription_Type(OctetString):
    """Custom type cardDescription based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CardDescription_Type.__name__ = "OctetString"
_CardDescription_Object = MibTableColumn
cardDescription = _CardDescription_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 20, 3, 1, 1, 21),
    _CardDescription_Type()
)
cardDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cardDescription.setStatus("current")
_OptixsonetEqptMgtConformance_ObjectIdentity = ObjectIdentity
optixsonetEqptMgtConformance = _OptixsonetEqptMgtConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 20, 3, 2)
)
_OptixsonetEqptMgtGroups_ObjectIdentity = ObjectIdentity
optixsonetEqptMgtGroups = _OptixsonetEqptMgtGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 20, 3, 2, 1)
)
_OptixsonetEqptMgtCompliances_ObjectIdentity = ObjectIdentity
optixsonetEqptMgtCompliances = _OptixsonetEqptMgtCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 20, 3, 2, 2)
)

# Managed Objects groups

currentObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 20, 3, 2, 1, 1)
)
currentObjectGroup.setObjects(
      *(("OPTIX-SONET-EQPTMGT-MIB-V2", "cardIndexSlotId"),
        ("OPTIX-SONET-EQPTMGT-MIB-V2", "cardIndexSfpId"),
        ("OPTIX-SONET-EQPTMGT-MIB-V2", "cardProvisionType"),
        ("OPTIX-SONET-EQPTMGT-MIB-V2", "cardPhysicalType"),
        ("OPTIX-SONET-EQPTMGT-MIB-V2", "cardInterfaceType"),
        ("OPTIX-SONET-EQPTMGT-MIB-V2", "cardBandwidth"),
        ("OPTIX-SONET-EQPTMGT-MIB-V2", "cardSerialNum"),
        ("OPTIX-SONET-EQPTMGT-MIB-V2", "cardCLEICode"),
        ("OPTIX-SONET-EQPTMGT-MIB-V2", "cardPartNum"),
        ("OPTIX-SONET-EQPTMGT-MIB-V2", "cardDOM"),
        ("OPTIX-SONET-EQPTMGT-MIB-V2", "cardPCBVersion"),
        ("OPTIX-SONET-EQPTMGT-MIB-V2", "cardSWVersion"),
        ("OPTIX-SONET-EQPTMGT-MIB-V2", "cardFPGAVersion"),
        ("OPTIX-SONET-EQPTMGT-MIB-V2", "cardEPLDVersion"),
        ("OPTIX-SONET-EQPTMGT-MIB-V2", "cardBIOSVersion"),
        ("OPTIX-SONET-EQPTMGT-MIB-V2", "cardMAC"),
        ("OPTIX-SONET-EQPTMGT-MIB-V2", "cardPSTState"),
        ("OPTIX-SONET-EQPTMGT-MIB-V2", "cardSSTState"),
        ("OPTIX-SONET-EQPTMGT-MIB-V2", "cardTPSPriority"),
        ("OPTIX-SONET-EQPTMGT-MIB-V2", "cardSwitchState"),
        ("OPTIX-SONET-EQPTMGT-MIB-V2", "cardDescription"))
)
if mibBuilder.loadTexts:
    currentObjectGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

basicCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 20, 3, 2, 2, 1)
)
if mibBuilder.loadTexts:
    basicCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "OPTIX-SONET-EQPTMGT-MIB-V2",
    **{"IntfType": IntfType,
       "optixsonetEqptMgt": optixsonetEqptMgt,
       "optixsonetCardInfoTable": optixsonetCardInfoTable,
       "optixsonetCardInfoEntry": optixsonetCardInfoEntry,
       "cardIndexSlotId": cardIndexSlotId,
       "cardIndexSfpId": cardIndexSfpId,
       "cardProvisionType": cardProvisionType,
       "cardPhysicalType": cardPhysicalType,
       "cardInterfaceType": cardInterfaceType,
       "cardBandwidth": cardBandwidth,
       "cardSerialNum": cardSerialNum,
       "cardCLEICode": cardCLEICode,
       "cardPartNum": cardPartNum,
       "cardDOM": cardDOM,
       "cardPCBVersion": cardPCBVersion,
       "cardSWVersion": cardSWVersion,
       "cardFPGAVersion": cardFPGAVersion,
       "cardEPLDVersion": cardEPLDVersion,
       "cardBIOSVersion": cardBIOSVersion,
       "cardMAC": cardMAC,
       "cardPSTState": cardPSTState,
       "cardSSTState": cardSSTState,
       "cardTPSPriority": cardTPSPriority,
       "cardSwitchState": cardSwitchState,
       "cardDescription": cardDescription,
       "optixsonetEqptMgtConformance": optixsonetEqptMgtConformance,
       "optixsonetEqptMgtGroups": optixsonetEqptMgtGroups,
       "currentObjectGroup": currentObjectGroup,
       "optixsonetEqptMgtCompliances": optixsonetEqptMgtCompliances,
       "basicCompliance": basicCompliance}
)
