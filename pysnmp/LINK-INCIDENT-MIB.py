# SNMP MIB module (LINK-INCIDENT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/LINK-INCIDENT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:18:16 2024
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

(fcSwitch,) = mibBuilder.importSymbols(
    "Brocade-REG-MIB",
    "fcSwitch")

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

linkIncidentMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 50)
)
linkIncidentMIB.setRevisions(
        ("2003-07-11 00:00",
         "2012-06-04 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class FcPortID(OctetString, TextualConvention):
    status = "current"
    displayHint = "x"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )



class RLIRLinkFailureType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("bitErrorRate", 2),
          ("invalidSeqForPortState", 6),
          ("loopInitializationTimeout", 7),
          ("lossOfSignal", 3),
          ("lossOfSignalInLoopInit", 8),
          ("nOSRecognized", 4),
          ("primitiveSequenceTimeout", 5))
    )



class LinkWwn(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )



class PortType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("e-port", 3),
          ("n-port", 1),
          ("nl-port", 2))
    )



class LinkFormat(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("common", 2),
          ("ficon", 1))
    )



class RegType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("conditional", 1),
          ("unconditional", 2))
    )



class LIRRProtocol(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fcp", 1),
          ("sb2", 2))
    )



class RNIDTagType(OctetString, TextualConvention):
    status = "current"
    displayHint = "x"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )



class RNIDFlags(OctetString, TextualConvention):
    status = "current"
    displayHint = "x"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )



class RNIDType(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )



class RNIDModel(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )



class RNIDManufacturer(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )



class RNIDManufacturerPlant(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )



class RNIDSequenceNumber(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(12, 12),
    )



class RNIDParams(OctetString, TextualConvention):
    status = "current"
    displayHint = "x"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )



# MIB Managed Objects in the order of their OIDs

_FiconRNID_ObjectIdentity = ObjectIdentity
ficonRNID = _FiconRNID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 50, 2)
)
if mibBuilder.loadTexts:
    ficonRNID.setStatus("current")
_NodeRNIDTableNumEntries_Type = Integer32
_NodeRNIDTableNumEntries_Object = MibScalar
nodeRNIDTableNumEntries = _NodeRNIDTableNumEntries_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 50, 2, 1),
    _NodeRNIDTableNumEntries_Type()
)
nodeRNIDTableNumEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodeRNIDTableNumEntries.setStatus("current")
_NodeRNIDTable_Object = MibTable
nodeRNIDTable = _NodeRNIDTable_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 50, 2, 2)
)
if mibBuilder.loadTexts:
    nodeRNIDTable.setStatus("current")
_NodeRNIDEntry_Object = MibTableRow
nodeRNIDEntry = _NodeRNIDEntry_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 50, 2, 2, 1)
)
nodeRNIDEntry.setIndexNames(
    (0, "LINK-INCIDENT-MIB", "nodeRNIDIndex"),
)
if mibBuilder.loadTexts:
    nodeRNIDEntry.setStatus("current")
_NodeRNIDIndex_Type = Integer32
_NodeRNIDIndex_Object = MibTableColumn
nodeRNIDIndex = _NodeRNIDIndex_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 50, 2, 2, 1, 1),
    _NodeRNIDIndex_Type()
)
nodeRNIDIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodeRNIDIndex.setStatus("current")
_NodeRNIDIncidentPortWWN_Type = LinkWwn
_NodeRNIDIncidentPortWWN_Object = MibTableColumn
nodeRNIDIncidentPortWWN = _NodeRNIDIncidentPortWWN_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 50, 2, 2, 1, 2),
    _NodeRNIDIncidentPortWWN_Type()
)
nodeRNIDIncidentPortWWN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodeRNIDIncidentPortWWN.setStatus("current")
_NodeRNIDPID_Type = FcPortID
_NodeRNIDPID_Object = MibTableColumn
nodeRNIDPID = _NodeRNIDPID_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 50, 2, 2, 1, 3),
    _NodeRNIDPID_Type()
)
nodeRNIDPID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodeRNIDPID.setStatus("current")
_NodeRNIDFlags_Type = RNIDFlags
_NodeRNIDFlags_Object = MibTableColumn
nodeRNIDFlags = _NodeRNIDFlags_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 50, 2, 2, 1, 4),
    _NodeRNIDFlags_Type()
)
nodeRNIDFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodeRNIDFlags.setStatus("current")
_NodeRNIDType_Type = RNIDType
_NodeRNIDType_Object = MibTableColumn
nodeRNIDType = _NodeRNIDType_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 50, 2, 2, 1, 5),
    _NodeRNIDType_Type()
)
nodeRNIDType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodeRNIDType.setStatus("current")
_NodeRNIDModel_Type = RNIDModel
_NodeRNIDModel_Object = MibTableColumn
nodeRNIDModel = _NodeRNIDModel_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 50, 2, 2, 1, 6),
    _NodeRNIDModel_Type()
)
nodeRNIDModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodeRNIDModel.setStatus("current")
_NodeRNIDManufacturer_Type = RNIDManufacturer
_NodeRNIDManufacturer_Object = MibTableColumn
nodeRNIDManufacturer = _NodeRNIDManufacturer_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 50, 2, 2, 1, 7),
    _NodeRNIDManufacturer_Type()
)
nodeRNIDManufacturer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodeRNIDManufacturer.setStatus("current")
_NodeRNIDManufacturerPlant_Type = RNIDManufacturerPlant
_NodeRNIDManufacturerPlant_Object = MibTableColumn
nodeRNIDManufacturerPlant = _NodeRNIDManufacturerPlant_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 50, 2, 2, 1, 8),
    _NodeRNIDManufacturerPlant_Type()
)
nodeRNIDManufacturerPlant.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodeRNIDManufacturerPlant.setStatus("current")
_NodeRNIDSequenceNumber_Type = RNIDSequenceNumber
_NodeRNIDSequenceNumber_Object = MibTableColumn
nodeRNIDSequenceNumber = _NodeRNIDSequenceNumber_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 50, 2, 2, 1, 9),
    _NodeRNIDSequenceNumber_Type()
)
nodeRNIDSequenceNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodeRNIDSequenceNumber.setStatus("current")
_NodeRNIDConnectedPortWWN_Type = LinkWwn
_NodeRNIDConnectedPortWWN_Object = MibTableColumn
nodeRNIDConnectedPortWWN = _NodeRNIDConnectedPortWWN_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 50, 2, 2, 1, 10),
    _NodeRNIDConnectedPortWWN_Type()
)
nodeRNIDConnectedPortWWN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodeRNIDConnectedPortWWN.setStatus("current")
_NodeRNIDPortType_Type = PortType
_NodeRNIDPortType_Object = MibTableColumn
nodeRNIDPortType = _NodeRNIDPortType_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 50, 2, 2, 1, 11),
    _NodeRNIDPortType_Type()
)
nodeRNIDPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodeRNIDPortType.setStatus("current")
_NodeRNIDFormat_Type = LinkFormat
_NodeRNIDFormat_Object = MibTableColumn
nodeRNIDFormat = _NodeRNIDFormat_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 50, 2, 2, 1, 12),
    _NodeRNIDFormat_Type()
)
nodeRNIDFormat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodeRNIDFormat.setStatus("current")
_NodeRNIDTag_Type = RNIDTagType
_NodeRNIDTag_Object = MibTableColumn
nodeRNIDTag = _NodeRNIDTag_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 50, 2, 2, 1, 13),
    _NodeRNIDTag_Type()
)
nodeRNIDTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodeRNIDTag.setStatus("current")
_NodeRNIDParams_Type = RNIDParams
_NodeRNIDParams_Object = MibTableColumn
nodeRNIDParams = _NodeRNIDParams_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 50, 2, 2, 1, 14),
    _NodeRNIDParams_Type()
)
nodeRNIDParams.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodeRNIDParams.setStatus("current")
_SwitchRNIDTableNumEntries_Type = Integer32
_SwitchRNIDTableNumEntries_Object = MibScalar
switchRNIDTableNumEntries = _SwitchRNIDTableNumEntries_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 50, 2, 3),
    _SwitchRNIDTableNumEntries_Type()
)
switchRNIDTableNumEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchRNIDTableNumEntries.setStatus("current")
_SwitchRNIDTable_Object = MibTable
switchRNIDTable = _SwitchRNIDTable_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 50, 2, 4)
)
if mibBuilder.loadTexts:
    switchRNIDTable.setStatus("current")
_SwitchRNIDEntry_Object = MibTableRow
switchRNIDEntry = _SwitchRNIDEntry_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 50, 2, 4, 1)
)
switchRNIDEntry.setIndexNames(
    (0, "LINK-INCIDENT-MIB", "switchRNIDIndex"),
)
if mibBuilder.loadTexts:
    switchRNIDEntry.setStatus("current")
_SwitchRNIDIndex_Type = Integer32
_SwitchRNIDIndex_Object = MibTableColumn
switchRNIDIndex = _SwitchRNIDIndex_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 50, 2, 4, 1, 1),
    _SwitchRNIDIndex_Type()
)
switchRNIDIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchRNIDIndex.setStatus("current")
_SwitchRNIDSwitchWWN_Type = LinkWwn
_SwitchRNIDSwitchWWN_Object = MibTableColumn
switchRNIDSwitchWWN = _SwitchRNIDSwitchWWN_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 50, 2, 4, 1, 2),
    _SwitchRNIDSwitchWWN_Type()
)
switchRNIDSwitchWWN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchRNIDSwitchWWN.setStatus("current")
_SwitchRNIDFlags_Type = RNIDFlags
_SwitchRNIDFlags_Object = MibTableColumn
switchRNIDFlags = _SwitchRNIDFlags_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 50, 2, 4, 1, 3),
    _SwitchRNIDFlags_Type()
)
switchRNIDFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchRNIDFlags.setStatus("current")
_SwitchRNIDType_Type = RNIDType
_SwitchRNIDType_Object = MibTableColumn
switchRNIDType = _SwitchRNIDType_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 50, 2, 4, 1, 4),
    _SwitchRNIDType_Type()
)
switchRNIDType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchRNIDType.setStatus("current")
_SwitchRNIDModel_Type = RNIDModel
_SwitchRNIDModel_Object = MibTableColumn
switchRNIDModel = _SwitchRNIDModel_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 50, 2, 4, 1, 5),
    _SwitchRNIDModel_Type()
)
switchRNIDModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchRNIDModel.setStatus("current")
_SwitchRNIDManufacturer_Type = RNIDManufacturer
_SwitchRNIDManufacturer_Object = MibTableColumn
switchRNIDManufacturer = _SwitchRNIDManufacturer_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 50, 2, 4, 1, 6),
    _SwitchRNIDManufacturer_Type()
)
switchRNIDManufacturer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchRNIDManufacturer.setStatus("current")
_SwitchRNIDManufacturerPlant_Type = RNIDManufacturerPlant
_SwitchRNIDManufacturerPlant_Object = MibTableColumn
switchRNIDManufacturerPlant = _SwitchRNIDManufacturerPlant_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 50, 2, 4, 1, 7),
    _SwitchRNIDManufacturerPlant_Type()
)
switchRNIDManufacturerPlant.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchRNIDManufacturerPlant.setStatus("current")
_SwitchRNIDSequenceNumber_Type = RNIDSequenceNumber
_SwitchRNIDSequenceNumber_Object = MibTableColumn
switchRNIDSequenceNumber = _SwitchRNIDSequenceNumber_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 50, 2, 4, 1, 8),
    _SwitchRNIDSequenceNumber_Type()
)
switchRNIDSequenceNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchRNIDSequenceNumber.setStatus("current")
_SwitchRNIDTag_Type = RNIDTagType
_SwitchRNIDTag_Object = MibTableColumn
switchRNIDTag = _SwitchRNIDTag_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 50, 2, 4, 1, 9),
    _SwitchRNIDTag_Type()
)
switchRNIDTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchRNIDTag.setStatus("current")
_SwitchRNIDParams_Type = RNIDParams
_SwitchRNIDParams_Object = MibTableColumn
switchRNIDParams = _SwitchRNIDParams_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 50, 2, 4, 1, 10),
    _SwitchRNIDParams_Type()
)
switchRNIDParams.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchRNIDParams.setStatus("current")


class _NodeVfId_Type(Integer32):
    """Custom type nodeVfId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_NodeVfId_Type.__name__ = "Integer32"
_NodeVfId_Object = MibScalar
nodeVfId = _NodeVfId_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 50, 2, 5),
    _NodeVfId_Type()
)
nodeVfId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodeVfId.setStatus("current")
_FiconSlot_Type = Integer32
_FiconSlot_Object = MibScalar
ficonSlot = _FiconSlot_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 50, 2, 6),
    _FiconSlot_Type()
)
ficonSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ficonSlot.setStatus("current")
_FiconPort_Type = Integer32
_FiconPort_Object = MibScalar
ficonPort = _FiconPort_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 50, 2, 7),
    _FiconPort_Type()
)
ficonPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ficonPort.setStatus("current")
_FiconLIRR_ObjectIdentity = ObjectIdentity
ficonLIRR = _FiconLIRR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 50, 3)
)
if mibBuilder.loadTexts:
    ficonLIRR.setStatus("current")
_LIRRTableNumEntries_Type = Integer32
_LIRRTableNumEntries_Object = MibScalar
lIRRTableNumEntries = _LIRRTableNumEntries_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 50, 3, 1),
    _LIRRTableNumEntries_Type()
)
lIRRTableNumEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lIRRTableNumEntries.setStatus("current")
_LIRRTable_Object = MibTable
lIRRTable = _LIRRTable_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 50, 3, 2)
)
if mibBuilder.loadTexts:
    lIRRTable.setStatus("current")
_LIRREntry_Object = MibTableRow
lIRREntry = _LIRREntry_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 50, 3, 2, 1)
)
lIRREntry.setIndexNames(
    (0, "LINK-INCIDENT-MIB", "lIRRIndex"),
)
if mibBuilder.loadTexts:
    lIRREntry.setStatus("current")
_LIRRIndex_Type = Integer32
_LIRRIndex_Object = MibTableColumn
lIRRIndex = _LIRRIndex_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 50, 3, 2, 1, 1),
    _LIRRIndex_Type()
)
lIRRIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lIRRIndex.setStatus("current")
_LIRRListenerPortWWN_Type = LinkWwn
_LIRRListenerPortWWN_Object = MibTableColumn
lIRRListenerPortWWN = _LIRRListenerPortWWN_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 50, 3, 2, 1, 2),
    _LIRRListenerPortWWN_Type()
)
lIRRListenerPortWWN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lIRRListenerPortWWN.setStatus("current")
_LIRRListenerPID_Type = FcPortID
_LIRRListenerPID_Object = MibTableColumn
lIRRListenerPID = _LIRRListenerPID_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 50, 3, 2, 1, 3),
    _LIRRListenerPID_Type()
)
lIRRListenerPID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lIRRListenerPID.setStatus("current")
_LIRRRegType_Type = RegType
_LIRRRegType_Object = MibTableColumn
lIRRRegType = _LIRRRegType_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 50, 3, 2, 1, 4),
    _LIRRRegType_Type()
)
lIRRRegType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lIRRRegType.setStatus("current")
_LIRRProtocol_Type = LIRRProtocol
_LIRRProtocol_Object = MibTableColumn
lIRRProtocol = _LIRRProtocol_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 50, 3, 2, 1, 5),
    _LIRRProtocol_Type()
)
lIRRProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lIRRProtocol.setStatus("current")
_LIRRPortType_Type = PortType
_LIRRPortType_Object = MibTableColumn
lIRRPortType = _LIRRPortType_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 50, 3, 2, 1, 6),
    _LIRRPortType_Type()
)
lIRRPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lIRRPortType.setStatus("current")
_LIRRFormat_Type = LinkFormat
_LIRRFormat_Object = MibTableColumn
lIRRFormat = _LIRRFormat_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 50, 3, 2, 1, 7),
    _LIRRFormat_Type()
)
lIRRFormat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lIRRFormat.setStatus("current")
_FiconRLIR_ObjectIdentity = ObjectIdentity
ficonRLIR = _FiconRLIR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 50, 4)
)
if mibBuilder.loadTexts:
    ficonRLIR.setStatus("current")
_RLIRTableNumEntries_Type = Integer32
_RLIRTableNumEntries_Object = MibScalar
rLIRTableNumEntries = _RLIRTableNumEntries_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 50, 4, 1),
    _RLIRTableNumEntries_Type()
)
rLIRTableNumEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rLIRTableNumEntries.setStatus("current")
_RLIRTable_Object = MibTable
rLIRTable = _RLIRTable_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 50, 4, 2)
)
if mibBuilder.loadTexts:
    rLIRTable.setStatus("current")
_RLIREntry_Object = MibTableRow
rLIREntry = _RLIREntry_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 50, 4, 2, 1)
)
rLIREntry.setIndexNames(
    (0, "LINK-INCIDENT-MIB", "rLIRIndex"),
)
if mibBuilder.loadTexts:
    rLIREntry.setStatus("current")
_RLIRIndex_Type = Integer32
_RLIRIndex_Object = MibTableColumn
rLIRIndex = _RLIRIndex_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 50, 4, 2, 1, 1),
    _RLIRIndex_Type()
)
rLIRIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rLIRIndex.setStatus("current")
_RLIRIncidentPortWwn_Type = LinkWwn
_RLIRIncidentPortWwn_Object = MibTableColumn
rLIRIncidentPortWwn = _RLIRIncidentPortWwn_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 50, 4, 2, 1, 2),
    _RLIRIncidentPortWwn_Type()
)
rLIRIncidentPortWwn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rLIRIncidentPortWwn.setStatus("current")
_RLIRIncidentNodeWwn_Type = LinkWwn
_RLIRIncidentNodeWwn_Object = MibTableColumn
rLIRIncidentNodeWwn = _RLIRIncidentNodeWwn_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 50, 4, 2, 1, 3),
    _RLIRIncidentNodeWwn_Type()
)
rLIRIncidentNodeWwn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rLIRIncidentNodeWwn.setStatus("current")
_RLIRIncidentPortType_Type = PortType
_RLIRIncidentPortType_Object = MibTableColumn
rLIRIncidentPortType = _RLIRIncidentPortType_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 50, 4, 2, 1, 5),
    _RLIRIncidentPortType_Type()
)
rLIRIncidentPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rLIRIncidentPortType.setStatus("current")
_RLIRIncidentPID_Type = FcPortID
_RLIRIncidentPID_Object = MibTableColumn
rLIRIncidentPID = _RLIRIncidentPID_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 50, 4, 2, 1, 6),
    _RLIRIncidentPID_Type()
)
rLIRIncidentPID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rLIRIncidentPID.setStatus("current")
_RLIRIncidentPortNumber_Type = Integer32
_RLIRIncidentPortNumber_Object = MibTableColumn
rLIRIncidentPortNumber = _RLIRIncidentPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 50, 4, 2, 1, 7),
    _RLIRIncidentPortNumber_Type()
)
rLIRIncidentPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rLIRIncidentPortNumber.setStatus("current")
_RLIRConnectedPortWwn_Type = LinkWwn
_RLIRConnectedPortWwn_Object = MibTableColumn
rLIRConnectedPortWwn = _RLIRConnectedPortWwn_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 50, 4, 2, 1, 8),
    _RLIRConnectedPortWwn_Type()
)
rLIRConnectedPortWwn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rLIRConnectedPortWwn.setStatus("current")
_RLIRConnectedNodeWwn_Type = LinkWwn
_RLIRConnectedNodeWwn_Object = MibTableColumn
rLIRConnectedNodeWwn = _RLIRConnectedNodeWwn_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 50, 4, 2, 1, 9),
    _RLIRConnectedNodeWwn_Type()
)
rLIRConnectedNodeWwn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rLIRConnectedNodeWwn.setStatus("current")
_RLIRFabricWwn_Type = LinkWwn
_RLIRFabricWwn_Object = MibTableColumn
rLIRFabricWwn = _RLIRFabricWwn_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 50, 4, 2, 1, 10),
    _RLIRFabricWwn_Type()
)
rLIRFabricWwn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rLIRFabricWwn.setStatus("current")
_RLIRLinkFailureType_Type = RLIRLinkFailureType
_RLIRLinkFailureType_Object = MibTableColumn
rLIRLinkFailureType = _RLIRLinkFailureType_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 50, 4, 2, 1, 11),
    _RLIRLinkFailureType_Type()
)
rLIRLinkFailureType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rLIRLinkFailureType.setStatus("current")


class _RLIRTimeStamp_Type(DisplayString):
    """Custom type rLIRTimeStamp based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_RLIRTimeStamp_Type.__name__ = "DisplayString"
_RLIRTimeStamp_Object = MibTableColumn
rLIRTimeStamp = _RLIRTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 50, 4, 2, 1, 12),
    _RLIRTimeStamp_Type()
)
rLIRTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rLIRTimeStamp.setStatus("current")
_RLIRFormat_Type = LinkFormat
_RLIRFormat_Object = MibTableColumn
rLIRFormat = _RLIRFormat_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 50, 4, 2, 1, 13),
    _RLIRFormat_Type()
)
rLIRFormat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rLIRFormat.setStatus("current")
_LinkIncidentMIBTraps_ObjectIdentity = ObjectIdentity
linkIncidentMIBTraps = _LinkIncidentMIBTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 50, 21)
)
if mibBuilder.loadTexts:
    linkIncidentMIBTraps.setStatus("current")
_LinkIncidentMIBTrapPrefix_ObjectIdentity = ObjectIdentity
linkIncidentMIBTrapPrefix = _LinkIncidentMIBTrapPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 50, 21, 0)
)
if mibBuilder.loadTexts:
    linkIncidentMIBTrapPrefix.setStatus("current")

# Managed Objects groups


# Notification objects

linkRNIDDeviceRegistration = NotificationType(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 50, 21, 0, 1)
)
linkRNIDDeviceRegistration.setObjects(
      *(("LINK-INCIDENT-MIB", "nodeRNIDIndex"),
        ("LINK-INCIDENT-MIB", "nodeRNIDIncidentPortWWN"),
        ("LINK-INCIDENT-MIB", "nodeRNIDConnectedPortWWN"),
        ("LINK-INCIDENT-MIB", "nodeVfId"),
        ("LINK-INCIDENT-MIB", "ficonSlot"),
        ("LINK-INCIDENT-MIB", "ficonPort"))
)
if mibBuilder.loadTexts:
    linkRNIDDeviceRegistration.setStatus(
        "current"
    )

linkRNIDDeviceDeRegistration = NotificationType(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 50, 21, 0, 2)
)
linkRNIDDeviceDeRegistration.setObjects(
      *(("LINK-INCIDENT-MIB", "nodeRNIDIndex"),
        ("LINK-INCIDENT-MIB", "nodeRNIDIncidentPortWWN"),
        ("LINK-INCIDENT-MIB", "nodeRNIDConnectedPortWWN"),
        ("LINK-INCIDENT-MIB", "nodeVfId"),
        ("LINK-INCIDENT-MIB", "ficonSlot"),
        ("LINK-INCIDENT-MIB", "ficonPort"))
)
if mibBuilder.loadTexts:
    linkRNIDDeviceDeRegistration.setStatus(
        "current"
    )

linkLIRRListenerAdded = NotificationType(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 50, 21, 0, 3)
)
linkLIRRListenerAdded.setObjects(
      *(("LINK-INCIDENT-MIB", "lIRRListenerPortWWN"),
        ("LINK-INCIDENT-MIB", "lIRRListenerPID"),
        ("LINK-INCIDENT-MIB", "lIRRIndex"),
        ("LINK-INCIDENT-MIB", "nodeVfId"),
        ("LINK-INCIDENT-MIB", "ficonSlot"),
        ("LINK-INCIDENT-MIB", "ficonPort"))
)
if mibBuilder.loadTexts:
    linkLIRRListenerAdded.setStatus(
        "current"
    )

linkLIRRListenerRemoved = NotificationType(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 50, 21, 0, 4)
)
linkLIRRListenerRemoved.setObjects(
      *(("LINK-INCIDENT-MIB", "lIRRListenerPortWWN"),
        ("LINK-INCIDENT-MIB", "lIRRListenerPID"),
        ("LINK-INCIDENT-MIB", "lIRRIndex"),
        ("LINK-INCIDENT-MIB", "nodeVfId"),
        ("LINK-INCIDENT-MIB", "ficonSlot"),
        ("LINK-INCIDENT-MIB", "ficonPort"))
)
if mibBuilder.loadTexts:
    linkLIRRListenerRemoved.setStatus(
        "current"
    )

linkRLIRFailureIncident = NotificationType(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 50, 21, 0, 5)
)
linkRLIRFailureIncident.setObjects(
      *(("LINK-INCIDENT-MIB", "nodeRNIDIndex"),
        ("LINK-INCIDENT-MIB", "lIRRIndex"),
        ("LINK-INCIDENT-MIB", "rLIRIncidentPortWwn"),
        ("LINK-INCIDENT-MIB", "rLIRConnectedPortWwn"),
        ("LINK-INCIDENT-MIB", "rLIRIndex"),
        ("LINK-INCIDENT-MIB", "rLIRLinkFailureType"),
        ("LINK-INCIDENT-MIB", "lIRRListenerPID"),
        ("LINK-INCIDENT-MIB", "nodeVfId"),
        ("LINK-INCIDENT-MIB", "ficonSlot"),
        ("LINK-INCIDENT-MIB", "ficonPort"))
)
if mibBuilder.loadTexts:
    linkRLIRFailureIncident.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "LINK-INCIDENT-MIB",
    **{"FcPortID": FcPortID,
       "RLIRLinkFailureType": RLIRLinkFailureType,
       "LinkWwn": LinkWwn,
       "PortType": PortType,
       "LinkFormat": LinkFormat,
       "RegType": RegType,
       "LIRRProtocol": LIRRProtocol,
       "RNIDTagType": RNIDTagType,
       "RNIDFlags": RNIDFlags,
       "RNIDType": RNIDType,
       "RNIDModel": RNIDModel,
       "RNIDManufacturer": RNIDManufacturer,
       "RNIDManufacturerPlant": RNIDManufacturerPlant,
       "RNIDSequenceNumber": RNIDSequenceNumber,
       "RNIDParams": RNIDParams,
       "linkIncidentMIB": linkIncidentMIB,
       "ficonRNID": ficonRNID,
       "nodeRNIDTableNumEntries": nodeRNIDTableNumEntries,
       "nodeRNIDTable": nodeRNIDTable,
       "nodeRNIDEntry": nodeRNIDEntry,
       "nodeRNIDIndex": nodeRNIDIndex,
       "nodeRNIDIncidentPortWWN": nodeRNIDIncidentPortWWN,
       "nodeRNIDPID": nodeRNIDPID,
       "nodeRNIDFlags": nodeRNIDFlags,
       "nodeRNIDType": nodeRNIDType,
       "nodeRNIDModel": nodeRNIDModel,
       "nodeRNIDManufacturer": nodeRNIDManufacturer,
       "nodeRNIDManufacturerPlant": nodeRNIDManufacturerPlant,
       "nodeRNIDSequenceNumber": nodeRNIDSequenceNumber,
       "nodeRNIDConnectedPortWWN": nodeRNIDConnectedPortWWN,
       "nodeRNIDPortType": nodeRNIDPortType,
       "nodeRNIDFormat": nodeRNIDFormat,
       "nodeRNIDTag": nodeRNIDTag,
       "nodeRNIDParams": nodeRNIDParams,
       "switchRNIDTableNumEntries": switchRNIDTableNumEntries,
       "switchRNIDTable": switchRNIDTable,
       "switchRNIDEntry": switchRNIDEntry,
       "switchRNIDIndex": switchRNIDIndex,
       "switchRNIDSwitchWWN": switchRNIDSwitchWWN,
       "switchRNIDFlags": switchRNIDFlags,
       "switchRNIDType": switchRNIDType,
       "switchRNIDModel": switchRNIDModel,
       "switchRNIDManufacturer": switchRNIDManufacturer,
       "switchRNIDManufacturerPlant": switchRNIDManufacturerPlant,
       "switchRNIDSequenceNumber": switchRNIDSequenceNumber,
       "switchRNIDTag": switchRNIDTag,
       "switchRNIDParams": switchRNIDParams,
       "nodeVfId": nodeVfId,
       "ficonSlot": ficonSlot,
       "ficonPort": ficonPort,
       "ficonLIRR": ficonLIRR,
       "lIRRTableNumEntries": lIRRTableNumEntries,
       "lIRRTable": lIRRTable,
       "lIRREntry": lIRREntry,
       "lIRRIndex": lIRRIndex,
       "lIRRListenerPortWWN": lIRRListenerPortWWN,
       "lIRRListenerPID": lIRRListenerPID,
       "lIRRRegType": lIRRRegType,
       "lIRRProtocol": lIRRProtocol,
       "lIRRPortType": lIRRPortType,
       "lIRRFormat": lIRRFormat,
       "ficonRLIR": ficonRLIR,
       "rLIRTableNumEntries": rLIRTableNumEntries,
       "rLIRTable": rLIRTable,
       "rLIREntry": rLIREntry,
       "rLIRIndex": rLIRIndex,
       "rLIRIncidentPortWwn": rLIRIncidentPortWwn,
       "rLIRIncidentNodeWwn": rLIRIncidentNodeWwn,
       "rLIRIncidentPortType": rLIRIncidentPortType,
       "rLIRIncidentPID": rLIRIncidentPID,
       "rLIRIncidentPortNumber": rLIRIncidentPortNumber,
       "rLIRConnectedPortWwn": rLIRConnectedPortWwn,
       "rLIRConnectedNodeWwn": rLIRConnectedNodeWwn,
       "rLIRFabricWwn": rLIRFabricWwn,
       "rLIRLinkFailureType": rLIRLinkFailureType,
       "rLIRTimeStamp": rLIRTimeStamp,
       "rLIRFormat": rLIRFormat,
       "linkIncidentMIBTraps": linkIncidentMIBTraps,
       "linkIncidentMIBTrapPrefix": linkIncidentMIBTrapPrefix,
       "linkRNIDDeviceRegistration": linkRNIDDeviceRegistration,
       "linkRNIDDeviceDeRegistration": linkRNIDDeviceDeRegistration,
       "linkLIRRListenerAdded": linkLIRRListenerAdded,
       "linkLIRRListenerRemoved": linkLIRRListenerRemoved,
       "linkRLIRFailureIncident": linkRLIRFailureIncident}
)
