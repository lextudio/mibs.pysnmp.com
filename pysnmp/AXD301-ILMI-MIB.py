# SNMP MIB module (AXD301-ILMI-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/AXD301-ILMI-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:44:53 2024
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

(AtmServiceCategory,) = mibBuilder.importSymbols(
    "ATM-TC-MIB",
    "AtmServiceCategory")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY


# Types definitions



class ClnpAddress(OctetString):
    """Custom type ClnpAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 21),
    )





class AtmAddress(OctetString):
    """Custom type AtmAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
        ValueSizeConstraint(20, 20),
    )





class NetPrefix(OctetString):
    """Custom type NetPrefix based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
        ValueSizeConstraint(13, 13),
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_System_ObjectIdentity = ObjectIdentity
system = _System_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 1)
)


class _SysDescr_Type(DisplayString):
    """Custom type sysDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SysDescr_Type.__name__ = "DisplayString"
_SysDescr_Object = MibScalar
sysDescr = _SysDescr_Object(
    (1, 3, 6, 1, 2, 1, 1, 1),
    _SysDescr_Type()
)
sysDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysDescr.setStatus("mandatory")
_SysObjectID_Type = ObjectIdentifier
_SysObjectID_Object = MibScalar
sysObjectID = _SysObjectID_Object(
    (1, 3, 6, 1, 2, 1, 1, 2),
    _SysObjectID_Type()
)
sysObjectID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysObjectID.setStatus("mandatory")
_SysUpTime_Type = TimeTicks
_SysUpTime_Object = MibScalar
sysUpTime = _SysUpTime_Object(
    (1, 3, 6, 1, 2, 1, 1, 3),
    _SysUpTime_Type()
)
sysUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysUpTime.setStatus("mandatory")


class _SysContact_Type(DisplayString):
    """Custom type sysContact based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SysContact_Type.__name__ = "DisplayString"
_SysContact_Object = MibScalar
sysContact = _SysContact_Object(
    (1, 3, 6, 1, 2, 1, 1, 4),
    _SysContact_Type()
)
sysContact.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysContact.setStatus("mandatory")


class _SysName_Type(DisplayString):
    """Custom type sysName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SysName_Type.__name__ = "DisplayString"
_SysName_Object = MibScalar
sysName = _SysName_Object(
    (1, 3, 6, 1, 2, 1, 1, 5),
    _SysName_Type()
)
sysName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysName.setStatus("mandatory")


class _SysLocation_Type(DisplayString):
    """Custom type sysLocation based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SysLocation_Type.__name__ = "DisplayString"
_SysLocation_Object = MibScalar
sysLocation = _SysLocation_Object(
    (1, 3, 6, 1, 2, 1, 1, 6),
    _SysLocation_Type()
)
sysLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysLocation.setStatus("mandatory")


class _SysServices_Type(Integer32):
    """Custom type sysServices based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_SysServices_Type.__name__ = "Integer32"
_SysServices_Object = MibScalar
sysServices = _SysServices_Object(
    (1, 3, 6, 1, 2, 1, 1, 7),
    _SysServices_Type()
)
sysServices.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysServices.setStatus("mandatory")
_AtmForum_ObjectIdentity = ObjectIdentity
atmForum = _AtmForum_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353)
)
_AtmForumAdmin_ObjectIdentity = ObjectIdentity
atmForumAdmin = _AtmForumAdmin_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353, 1)
)
_AtmfTransmissionTypes_ObjectIdentity = ObjectIdentity
atmfTransmissionTypes = _AtmfTransmissionTypes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353, 1, 2)
)
_AtmfUnknownType_ObjectIdentity = ObjectIdentity
atmfUnknownType = _AtmfUnknownType_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353, 1, 2, 1)
)
_AtmfSonetSTS3c_ObjectIdentity = ObjectIdentity
atmfSonetSTS3c = _AtmfSonetSTS3c_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353, 1, 2, 2)
)
_AtmfDs3_ObjectIdentity = ObjectIdentity
atmfDs3 = _AtmfDs3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353, 1, 2, 3)
)
_Atmf4B5B_ObjectIdentity = ObjectIdentity
atmf4B5B = _Atmf4B5B_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353, 1, 2, 4)
)
_Atmf8B10B_ObjectIdentity = ObjectIdentity
atmf8B10B = _Atmf8B10B_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353, 1, 2, 5)
)
_AtmfSonetSTS12c_ObjectIdentity = ObjectIdentity
atmfSonetSTS12c = _AtmfSonetSTS12c_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353, 1, 2, 6)
)
_AtmfE3_ObjectIdentity = ObjectIdentity
atmfE3 = _AtmfE3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353, 1, 2, 7)
)
_AtmfT1_ObjectIdentity = ObjectIdentity
atmfT1 = _AtmfT1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353, 1, 2, 8)
)
_AtmfE1_ObjectIdentity = ObjectIdentity
atmfE1 = _AtmfE1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353, 1, 2, 9)
)
_AtmfMediaTypes_ObjectIdentity = ObjectIdentity
atmfMediaTypes = _AtmfMediaTypes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353, 1, 3)
)
_AtmfMediaUnknownType_ObjectIdentity = ObjectIdentity
atmfMediaUnknownType = _AtmfMediaUnknownType_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353, 1, 3, 1)
)
_AtmfMediaCoaxCable_ObjectIdentity = ObjectIdentity
atmfMediaCoaxCable = _AtmfMediaCoaxCable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353, 1, 3, 2)
)
_AtmfMediaSingleMode_ObjectIdentity = ObjectIdentity
atmfMediaSingleMode = _AtmfMediaSingleMode_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353, 1, 3, 3)
)
_AtmfMediaMultiMode_ObjectIdentity = ObjectIdentity
atmfMediaMultiMode = _AtmfMediaMultiMode_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353, 1, 3, 4)
)
_AtmfMediaStp_ObjectIdentity = ObjectIdentity
atmfMediaStp = _AtmfMediaStp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353, 1, 3, 5)
)
_AtmfMediaUtp_ObjectIdentity = ObjectIdentity
atmfMediaUtp = _AtmfMediaUtp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353, 1, 3, 6)
)
_AtmfTrafficDescrTypes_ObjectIdentity = ObjectIdentity
atmfTrafficDescrTypes = _AtmfTrafficDescrTypes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353, 1, 4)
)
_AtmfNoDescriptor_ObjectIdentity = ObjectIdentity
atmfNoDescriptor = _AtmfNoDescriptor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353, 1, 4, 1)
)
_AtmfPeakRate_ObjectIdentity = ObjectIdentity
atmfPeakRate = _AtmfPeakRate_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353, 1, 4, 2)
)
_AtmfNoClpNoScr_ObjectIdentity = ObjectIdentity
atmfNoClpNoScr = _AtmfNoClpNoScr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353, 1, 4, 3)
)
_AtmfClpNoTaggingNoScr_ObjectIdentity = ObjectIdentity
atmfClpNoTaggingNoScr = _AtmfClpNoTaggingNoScr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353, 1, 4, 4)
)
_AtmfClpTaggingNoScr_ObjectIdentity = ObjectIdentity
atmfClpTaggingNoScr = _AtmfClpTaggingNoScr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353, 1, 4, 5)
)
_AtmfNoClpScr_ObjectIdentity = ObjectIdentity
atmfNoClpScr = _AtmfNoClpScr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353, 1, 4, 6)
)
_AtmfClpNoTaggingScr_ObjectIdentity = ObjectIdentity
atmfClpNoTaggingScr = _AtmfClpNoTaggingScr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353, 1, 4, 7)
)
_AtmfClpTaggingScr_ObjectIdentity = ObjectIdentity
atmfClpTaggingScr = _AtmfClpTaggingScr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353, 1, 4, 8)
)
_AtmfClpNoTaggingMcr_ObjectIdentity = ObjectIdentity
atmfClpNoTaggingMcr = _AtmfClpNoTaggingMcr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353, 1, 4, 9)
)
_AtmfSrvcRegTypes_ObjectIdentity = ObjectIdentity
atmfSrvcRegTypes = _AtmfSrvcRegTypes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353, 1, 5)
)
_AtmForumUni_ObjectIdentity = ObjectIdentity
atmForumUni = _AtmForumUni_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353, 2)
)
_AtmfPhysicalGroup_ObjectIdentity = ObjectIdentity
atmfPhysicalGroup = _AtmfPhysicalGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353, 2, 1)
)
_AtmfPortTable_Object = MibTable
atmfPortTable = _AtmfPortTable_Object(
    (1, 3, 6, 1, 4, 1, 353, 2, 1, 1)
)
if mibBuilder.loadTexts:
    atmfPortTable.setStatus("mandatory")
_AtmfPortEntry_Object = MibTableRow
atmfPortEntry = _AtmfPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 353, 2, 1, 1, 1)
)
atmfPortEntry.setIndexNames(
    (0, "AXD301-ILMI-MIB", "atmfPortIndex"),
)
if mibBuilder.loadTexts:
    atmfPortEntry.setStatus("mandatory")


class _AtmfPortIndex_Type(Integer32):
    """Custom type atmfPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AtmfPortIndex_Type.__name__ = "Integer32"
_AtmfPortIndex_Object = MibTableColumn
atmfPortIndex = _AtmfPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 353, 2, 1, 1, 1, 1),
    _AtmfPortIndex_Type()
)
atmfPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmfPortIndex.setStatus("mandatory")
_AtmfPortAddress_Type = AtmAddress
_AtmfPortAddress_Object = MibTableColumn
atmfPortAddress = _AtmfPortAddress_Object(
    (1, 3, 6, 1, 4, 1, 353, 2, 1, 1, 1, 2),
    _AtmfPortAddress_Type()
)
atmfPortAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmfPortAddress.setStatus("obsolete")
_AtmfPortTransmissionType_Type = ObjectIdentifier
_AtmfPortTransmissionType_Object = MibTableColumn
atmfPortTransmissionType = _AtmfPortTransmissionType_Object(
    (1, 3, 6, 1, 4, 1, 353, 2, 1, 1, 1, 3),
    _AtmfPortTransmissionType_Type()
)
atmfPortTransmissionType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmfPortTransmissionType.setStatus("obsolete")
_AtmfPortMediaType_Type = ObjectIdentifier
_AtmfPortMediaType_Object = MibTableColumn
atmfPortMediaType = _AtmfPortMediaType_Object(
    (1, 3, 6, 1, 4, 1, 353, 2, 1, 1, 1, 4),
    _AtmfPortMediaType_Type()
)
atmfPortMediaType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmfPortMediaType.setStatus("obsolete")


class _AtmfPortOperStatus_Type(Integer32):
    """Custom type atmfPortOperStatus based on Integer32"""
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
        *(("inService", 2),
          ("loopBack", 4),
          ("other", 1),
          ("outOfService", 3))
    )


_AtmfPortOperStatus_Type.__name__ = "Integer32"
_AtmfPortOperStatus_Object = MibTableColumn
atmfPortOperStatus = _AtmfPortOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 353, 2, 1, 1, 1, 5),
    _AtmfPortOperStatus_Type()
)
atmfPortOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmfPortOperStatus.setStatus("obsolete")
_AtmfPortSpecific_Type = ObjectIdentifier
_AtmfPortSpecific_Object = MibTableColumn
atmfPortSpecific = _AtmfPortSpecific_Object(
    (1, 3, 6, 1, 4, 1, 353, 2, 1, 1, 1, 6),
    _AtmfPortSpecific_Type()
)
atmfPortSpecific.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmfPortSpecific.setStatus("obsolete")
_AtmfPortMyIfName_Type = DisplayString
_AtmfPortMyIfName_Object = MibTableColumn
atmfPortMyIfName = _AtmfPortMyIfName_Object(
    (1, 3, 6, 1, 4, 1, 353, 2, 1, 1, 1, 7),
    _AtmfPortMyIfName_Type()
)
atmfPortMyIfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmfPortMyIfName.setStatus("mandatory")


class _AtmfPortMyIfIdentifier_Type(Integer32):
    """Custom type atmfPortMyIfIdentifier based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AtmfPortMyIfIdentifier_Type.__name__ = "Integer32"
_AtmfPortMyIfIdentifier_Object = MibTableColumn
atmfPortMyIfIdentifier = _AtmfPortMyIfIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 353, 2, 1, 1, 1, 8),
    _AtmfPortMyIfIdentifier_Type()
)
atmfPortMyIfIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmfPortMyIfIdentifier.setStatus("mandatory")
_AtmfMyIpNmAddress_Type = IpAddress
_AtmfMyIpNmAddress_Object = MibScalar
atmfMyIpNmAddress = _AtmfMyIpNmAddress_Object(
    (1, 3, 6, 1, 4, 1, 353, 2, 1, 2),
    _AtmfMyIpNmAddress_Type()
)
atmfMyIpNmAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmfMyIpNmAddress.setStatus("mandatory")
_AtmfMyOsiNmNsapAddress_Type = ClnpAddress
_AtmfMyOsiNmNsapAddress_Object = MibScalar
atmfMyOsiNmNsapAddress = _AtmfMyOsiNmNsapAddress_Object(
    (1, 3, 6, 1, 4, 1, 353, 2, 1, 3),
    _AtmfMyOsiNmNsapAddress_Type()
)
atmfMyOsiNmNsapAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmfMyOsiNmNsapAddress.setStatus("mandatory")


class _AtmfMySystemIdentifier_Type(OctetString):
    """Custom type atmfMySystemIdentifier based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_AtmfMySystemIdentifier_Type.__name__ = "OctetString"
_AtmfMySystemIdentifier_Object = MibScalar
atmfMySystemIdentifier = _AtmfMySystemIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 353, 2, 1, 4),
    _AtmfMySystemIdentifier_Type()
)
atmfMySystemIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmfMySystemIdentifier.setStatus("mandatory")
_AtmfAtmLayerGroup_ObjectIdentity = ObjectIdentity
atmfAtmLayerGroup = _AtmfAtmLayerGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353, 2, 2)
)
_AtmfAtmLayerTable_Object = MibTable
atmfAtmLayerTable = _AtmfAtmLayerTable_Object(
    (1, 3, 6, 1, 4, 1, 353, 2, 2, 1)
)
if mibBuilder.loadTexts:
    atmfAtmLayerTable.setStatus("mandatory")
_AtmfAtmLayerEntry_Object = MibTableRow
atmfAtmLayerEntry = _AtmfAtmLayerEntry_Object(
    (1, 3, 6, 1, 4, 1, 353, 2, 2, 1, 1)
)
atmfAtmLayerEntry.setIndexNames(
    (0, "AXD301-ILMI-MIB", "atmfAtmLayerIndex"),
)
if mibBuilder.loadTexts:
    atmfAtmLayerEntry.setStatus("mandatory")


class _AtmfAtmLayerIndex_Type(Integer32):
    """Custom type atmfAtmLayerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AtmfAtmLayerIndex_Type.__name__ = "Integer32"
_AtmfAtmLayerIndex_Object = MibTableColumn
atmfAtmLayerIndex = _AtmfAtmLayerIndex_Object(
    (1, 3, 6, 1, 4, 1, 353, 2, 2, 1, 1, 1),
    _AtmfAtmLayerIndex_Type()
)
atmfAtmLayerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmfAtmLayerIndex.setStatus("mandatory")


class _AtmfAtmLayerMaxVPCs_Type(Integer32):
    """Custom type atmfAtmLayerMaxVPCs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4096),
    )


_AtmfAtmLayerMaxVPCs_Type.__name__ = "Integer32"
_AtmfAtmLayerMaxVPCs_Object = MibTableColumn
atmfAtmLayerMaxVPCs = _AtmfAtmLayerMaxVPCs_Object(
    (1, 3, 6, 1, 4, 1, 353, 2, 2, 1, 1, 2),
    _AtmfAtmLayerMaxVPCs_Type()
)
atmfAtmLayerMaxVPCs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmfAtmLayerMaxVPCs.setStatus("mandatory")


class _AtmfAtmLayerMaxVCCs_Type(Integer32):
    """Custom type atmfAtmLayerMaxVCCs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 268435456),
    )


_AtmfAtmLayerMaxVCCs_Type.__name__ = "Integer32"
_AtmfAtmLayerMaxVCCs_Object = MibTableColumn
atmfAtmLayerMaxVCCs = _AtmfAtmLayerMaxVCCs_Object(
    (1, 3, 6, 1, 4, 1, 353, 2, 2, 1, 1, 3),
    _AtmfAtmLayerMaxVCCs_Type()
)
atmfAtmLayerMaxVCCs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmfAtmLayerMaxVCCs.setStatus("mandatory")


class _AtmfAtmLayerConfiguredVPCs_Type(Integer32):
    """Custom type atmfAtmLayerConfiguredVPCs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4096),
    )


_AtmfAtmLayerConfiguredVPCs_Type.__name__ = "Integer32"
_AtmfAtmLayerConfiguredVPCs_Object = MibTableColumn
atmfAtmLayerConfiguredVPCs = _AtmfAtmLayerConfiguredVPCs_Object(
    (1, 3, 6, 1, 4, 1, 353, 2, 2, 1, 1, 4),
    _AtmfAtmLayerConfiguredVPCs_Type()
)
atmfAtmLayerConfiguredVPCs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmfAtmLayerConfiguredVPCs.setStatus("mandatory")


class _AtmfAtmLayerConfiguredVCCs_Type(Integer32):
    """Custom type atmfAtmLayerConfiguredVCCs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 268435456),
    )


_AtmfAtmLayerConfiguredVCCs_Type.__name__ = "Integer32"
_AtmfAtmLayerConfiguredVCCs_Object = MibTableColumn
atmfAtmLayerConfiguredVCCs = _AtmfAtmLayerConfiguredVCCs_Object(
    (1, 3, 6, 1, 4, 1, 353, 2, 2, 1, 1, 5),
    _AtmfAtmLayerConfiguredVCCs_Type()
)
atmfAtmLayerConfiguredVCCs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmfAtmLayerConfiguredVCCs.setStatus("mandatory")


class _AtmfAtmLayerMaxVpiBits_Type(Integer32):
    """Custom type atmfAtmLayerMaxVpiBits based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 12),
    )


_AtmfAtmLayerMaxVpiBits_Type.__name__ = "Integer32"
_AtmfAtmLayerMaxVpiBits_Object = MibTableColumn
atmfAtmLayerMaxVpiBits = _AtmfAtmLayerMaxVpiBits_Object(
    (1, 3, 6, 1, 4, 1, 353, 2, 2, 1, 1, 6),
    _AtmfAtmLayerMaxVpiBits_Type()
)
atmfAtmLayerMaxVpiBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmfAtmLayerMaxVpiBits.setStatus("mandatory")


class _AtmfAtmLayerMaxVciBits_Type(Integer32):
    """Custom type atmfAtmLayerMaxVciBits based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_AtmfAtmLayerMaxVciBits_Type.__name__ = "Integer32"
_AtmfAtmLayerMaxVciBits_Object = MibTableColumn
atmfAtmLayerMaxVciBits = _AtmfAtmLayerMaxVciBits_Object(
    (1, 3, 6, 1, 4, 1, 353, 2, 2, 1, 1, 7),
    _AtmfAtmLayerMaxVciBits_Type()
)
atmfAtmLayerMaxVciBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmfAtmLayerMaxVciBits.setStatus("mandatory")


class _AtmfAtmLayerUniType_Type(Integer32):
    """Custom type atmfAtmLayerUniType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("private", 2),
          ("public", 1))
    )


_AtmfAtmLayerUniType_Type.__name__ = "Integer32"
_AtmfAtmLayerUniType_Object = MibTableColumn
atmfAtmLayerUniType = _AtmfAtmLayerUniType_Object(
    (1, 3, 6, 1, 4, 1, 353, 2, 2, 1, 1, 8),
    _AtmfAtmLayerUniType_Type()
)
atmfAtmLayerUniType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmfAtmLayerUniType.setStatus("mandatory")


class _AtmfAtmLayerUniVersion_Type(Integer32):
    """Custom type atmfAtmLayerUniVersion based on Integer32"""
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
        *(("unsupported", 5),
          ("version2point0", 1),
          ("version3point0", 2),
          ("version3point1", 3),
          ("version4point0", 4))
    )


_AtmfAtmLayerUniVersion_Type.__name__ = "Integer32"
_AtmfAtmLayerUniVersion_Object = MibTableColumn
atmfAtmLayerUniVersion = _AtmfAtmLayerUniVersion_Object(
    (1, 3, 6, 1, 4, 1, 353, 2, 2, 1, 1, 9),
    _AtmfAtmLayerUniVersion_Type()
)
atmfAtmLayerUniVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmfAtmLayerUniVersion.setStatus("mandatory")


class _AtmfAtmLayerDeviceType_Type(Integer32):
    """Custom type atmfAtmLayerDeviceType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("node", 2),
          ("user", 1))
    )


_AtmfAtmLayerDeviceType_Type.__name__ = "Integer32"
_AtmfAtmLayerDeviceType_Object = MibTableColumn
atmfAtmLayerDeviceType = _AtmfAtmLayerDeviceType_Object(
    (1, 3, 6, 1, 4, 1, 353, 2, 2, 1, 1, 10),
    _AtmfAtmLayerDeviceType_Type()
)
atmfAtmLayerDeviceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmfAtmLayerDeviceType.setStatus("mandatory")


class _AtmfAtmLayerIlmiVersion_Type(Integer32):
    """Custom type atmfAtmLayerIlmiVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unsupported", 1),
          ("version4point0", 2))
    )


_AtmfAtmLayerIlmiVersion_Type.__name__ = "Integer32"
_AtmfAtmLayerIlmiVersion_Object = MibTableColumn
atmfAtmLayerIlmiVersion = _AtmfAtmLayerIlmiVersion_Object(
    (1, 3, 6, 1, 4, 1, 353, 2, 2, 1, 1, 11),
    _AtmfAtmLayerIlmiVersion_Type()
)
atmfAtmLayerIlmiVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmfAtmLayerIlmiVersion.setStatus("mandatory")


class _AtmfAtmLayerNniSigVersion_Type(Integer32):
    """Custom type atmfAtmLayerNniSigVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("iisp", 2),
          ("pnniVersion1point0", 3),
          ("unsupported", 1))
    )


_AtmfAtmLayerNniSigVersion_Type.__name__ = "Integer32"
_AtmfAtmLayerNniSigVersion_Object = MibTableColumn
atmfAtmLayerNniSigVersion = _AtmfAtmLayerNniSigVersion_Object(
    (1, 3, 6, 1, 4, 1, 353, 2, 2, 1, 1, 12),
    _AtmfAtmLayerNniSigVersion_Type()
)
atmfAtmLayerNniSigVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmfAtmLayerNniSigVersion.setStatus("mandatory")


class _AtmfAtmLayerMaxSvpcVpi_Type(Integer32):
    """Custom type atmfAtmLayerMaxSvpcVpi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4096),
    )


_AtmfAtmLayerMaxSvpcVpi_Type.__name__ = "Integer32"
_AtmfAtmLayerMaxSvpcVpi_Object = MibTableColumn
atmfAtmLayerMaxSvpcVpi = _AtmfAtmLayerMaxSvpcVpi_Object(
    (1, 3, 6, 1, 4, 1, 353, 2, 2, 1, 1, 13),
    _AtmfAtmLayerMaxSvpcVpi_Type()
)
atmfAtmLayerMaxSvpcVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmfAtmLayerMaxSvpcVpi.setStatus("mandatory")


class _AtmfAtmLayerMaxSvccVpi_Type(Integer32):
    """Custom type atmfAtmLayerMaxSvccVpi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4096),
    )


_AtmfAtmLayerMaxSvccVpi_Type.__name__ = "Integer32"
_AtmfAtmLayerMaxSvccVpi_Object = MibTableColumn
atmfAtmLayerMaxSvccVpi = _AtmfAtmLayerMaxSvccVpi_Object(
    (1, 3, 6, 1, 4, 1, 353, 2, 2, 1, 1, 14),
    _AtmfAtmLayerMaxSvccVpi_Type()
)
atmfAtmLayerMaxSvccVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmfAtmLayerMaxSvccVpi.setStatus("mandatory")


class _AtmfAtmLayerMinSvccVci_Type(Integer32):
    """Custom type atmfAtmLayerMinSvccVci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_AtmfAtmLayerMinSvccVci_Type.__name__ = "Integer32"
_AtmfAtmLayerMinSvccVci_Object = MibTableColumn
atmfAtmLayerMinSvccVci = _AtmfAtmLayerMinSvccVci_Object(
    (1, 3, 6, 1, 4, 1, 353, 2, 2, 1, 1, 15),
    _AtmfAtmLayerMinSvccVci_Type()
)
atmfAtmLayerMinSvccVci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmfAtmLayerMinSvccVci.setStatus("mandatory")
_AtmfAtmStatsGroup_ObjectIdentity = ObjectIdentity
atmfAtmStatsGroup = _AtmfAtmStatsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353, 2, 3)
)
_AtmfVpcGroup_ObjectIdentity = ObjectIdentity
atmfVpcGroup = _AtmfVpcGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353, 2, 4)
)
_AtmfVpcTable_Object = MibTable
atmfVpcTable = _AtmfVpcTable_Object(
    (1, 3, 6, 1, 4, 1, 353, 2, 4, 1)
)
if mibBuilder.loadTexts:
    atmfVpcTable.setStatus("mandatory")
_AtmfVpcEntry_Object = MibTableRow
atmfVpcEntry = _AtmfVpcEntry_Object(
    (1, 3, 6, 1, 4, 1, 353, 2, 4, 1, 1)
)
atmfVpcEntry.setIndexNames(
    (0, "AXD301-ILMI-MIB", "atmfVpcPortIndex"),
    (0, "AXD301-ILMI-MIB", "atmfVpcVpi"),
)
if mibBuilder.loadTexts:
    atmfVpcEntry.setStatus("mandatory")


class _AtmfVpcPortIndex_Type(Integer32):
    """Custom type atmfVpcPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AtmfVpcPortIndex_Type.__name__ = "Integer32"
_AtmfVpcPortIndex_Object = MibTableColumn
atmfVpcPortIndex = _AtmfVpcPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 353, 2, 4, 1, 1, 1),
    _AtmfVpcPortIndex_Type()
)
atmfVpcPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmfVpcPortIndex.setStatus("mandatory")


class _AtmfVpcVpi_Type(Integer32):
    """Custom type atmfVpcVpi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_AtmfVpcVpi_Type.__name__ = "Integer32"
_AtmfVpcVpi_Object = MibTableColumn
atmfVpcVpi = _AtmfVpcVpi_Object(
    (1, 3, 6, 1, 4, 1, 353, 2, 4, 1, 1, 2),
    _AtmfVpcVpi_Type()
)
atmfVpcVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmfVpcVpi.setStatus("mandatory")


class _AtmfVpcOperStatus_Type(Integer32):
    """Custom type atmfVpcOperStatus based on Integer32"""
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
        *(("end2endDown", 3),
          ("end2endUp", 2),
          ("localDown", 5),
          ("localUpEnd2endUnknown", 4),
          ("unknown", 1))
    )


_AtmfVpcOperStatus_Type.__name__ = "Integer32"
_AtmfVpcOperStatus_Object = MibTableColumn
atmfVpcOperStatus = _AtmfVpcOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 353, 2, 4, 1, 1, 3),
    _AtmfVpcOperStatus_Type()
)
atmfVpcOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmfVpcOperStatus.setStatus("mandatory")
_AtmfVpcTransmitTrafficDescriptorType_Type = ObjectIdentifier
_AtmfVpcTransmitTrafficDescriptorType_Object = MibTableColumn
atmfVpcTransmitTrafficDescriptorType = _AtmfVpcTransmitTrafficDescriptorType_Object(
    (1, 3, 6, 1, 4, 1, 353, 2, 4, 1, 1, 4),
    _AtmfVpcTransmitTrafficDescriptorType_Type()
)
atmfVpcTransmitTrafficDescriptorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmfVpcTransmitTrafficDescriptorType.setStatus("mandatory")


class _AtmfVpcTransmitTrafficDescriptorParam1_Type(Integer32):
    """Custom type atmfVpcTransmitTrafficDescriptorParam1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AtmfVpcTransmitTrafficDescriptorParam1_Type.__name__ = "Integer32"
_AtmfVpcTransmitTrafficDescriptorParam1_Object = MibTableColumn
atmfVpcTransmitTrafficDescriptorParam1 = _AtmfVpcTransmitTrafficDescriptorParam1_Object(
    (1, 3, 6, 1, 4, 1, 353, 2, 4, 1, 1, 5),
    _AtmfVpcTransmitTrafficDescriptorParam1_Type()
)
atmfVpcTransmitTrafficDescriptorParam1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmfVpcTransmitTrafficDescriptorParam1.setStatus("mandatory")


class _AtmfVpcTransmitTrafficDescriptorParam2_Type(Integer32):
    """Custom type atmfVpcTransmitTrafficDescriptorParam2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AtmfVpcTransmitTrafficDescriptorParam2_Type.__name__ = "Integer32"
_AtmfVpcTransmitTrafficDescriptorParam2_Object = MibTableColumn
atmfVpcTransmitTrafficDescriptorParam2 = _AtmfVpcTransmitTrafficDescriptorParam2_Object(
    (1, 3, 6, 1, 4, 1, 353, 2, 4, 1, 1, 6),
    _AtmfVpcTransmitTrafficDescriptorParam2_Type()
)
atmfVpcTransmitTrafficDescriptorParam2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmfVpcTransmitTrafficDescriptorParam2.setStatus("mandatory")


class _AtmfVpcTransmitTrafficDescriptorParam3_Type(Integer32):
    """Custom type atmfVpcTransmitTrafficDescriptorParam3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AtmfVpcTransmitTrafficDescriptorParam3_Type.__name__ = "Integer32"
_AtmfVpcTransmitTrafficDescriptorParam3_Object = MibTableColumn
atmfVpcTransmitTrafficDescriptorParam3 = _AtmfVpcTransmitTrafficDescriptorParam3_Object(
    (1, 3, 6, 1, 4, 1, 353, 2, 4, 1, 1, 7),
    _AtmfVpcTransmitTrafficDescriptorParam3_Type()
)
atmfVpcTransmitTrafficDescriptorParam3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmfVpcTransmitTrafficDescriptorParam3.setStatus("mandatory")


class _AtmfVpcTransmitTrafficDescriptorParam4_Type(Integer32):
    """Custom type atmfVpcTransmitTrafficDescriptorParam4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AtmfVpcTransmitTrafficDescriptorParam4_Type.__name__ = "Integer32"
_AtmfVpcTransmitTrafficDescriptorParam4_Object = MibTableColumn
atmfVpcTransmitTrafficDescriptorParam4 = _AtmfVpcTransmitTrafficDescriptorParam4_Object(
    (1, 3, 6, 1, 4, 1, 353, 2, 4, 1, 1, 8),
    _AtmfVpcTransmitTrafficDescriptorParam4_Type()
)
atmfVpcTransmitTrafficDescriptorParam4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmfVpcTransmitTrafficDescriptorParam4.setStatus("mandatory")


class _AtmfVpcTransmitTrafficDescriptorParam5_Type(Integer32):
    """Custom type atmfVpcTransmitTrafficDescriptorParam5 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AtmfVpcTransmitTrafficDescriptorParam5_Type.__name__ = "Integer32"
_AtmfVpcTransmitTrafficDescriptorParam5_Object = MibTableColumn
atmfVpcTransmitTrafficDescriptorParam5 = _AtmfVpcTransmitTrafficDescriptorParam5_Object(
    (1, 3, 6, 1, 4, 1, 353, 2, 4, 1, 1, 9),
    _AtmfVpcTransmitTrafficDescriptorParam5_Type()
)
atmfVpcTransmitTrafficDescriptorParam5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmfVpcTransmitTrafficDescriptorParam5.setStatus("mandatory")
_AtmfVpcReceiveTrafficDescriptorType_Type = ObjectIdentifier
_AtmfVpcReceiveTrafficDescriptorType_Object = MibTableColumn
atmfVpcReceiveTrafficDescriptorType = _AtmfVpcReceiveTrafficDescriptorType_Object(
    (1, 3, 6, 1, 4, 1, 353, 2, 4, 1, 1, 10),
    _AtmfVpcReceiveTrafficDescriptorType_Type()
)
atmfVpcReceiveTrafficDescriptorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmfVpcReceiveTrafficDescriptorType.setStatus("mandatory")


class _AtmfVpcReceiveTrafficDescriptorParam1_Type(Integer32):
    """Custom type atmfVpcReceiveTrafficDescriptorParam1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AtmfVpcReceiveTrafficDescriptorParam1_Type.__name__ = "Integer32"
_AtmfVpcReceiveTrafficDescriptorParam1_Object = MibTableColumn
atmfVpcReceiveTrafficDescriptorParam1 = _AtmfVpcReceiveTrafficDescriptorParam1_Object(
    (1, 3, 6, 1, 4, 1, 353, 2, 4, 1, 1, 11),
    _AtmfVpcReceiveTrafficDescriptorParam1_Type()
)
atmfVpcReceiveTrafficDescriptorParam1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmfVpcReceiveTrafficDescriptorParam1.setStatus("mandatory")


class _AtmfVpcReceiveTrafficDescriptorParam2_Type(Integer32):
    """Custom type atmfVpcReceiveTrafficDescriptorParam2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AtmfVpcReceiveTrafficDescriptorParam2_Type.__name__ = "Integer32"
_AtmfVpcReceiveTrafficDescriptorParam2_Object = MibTableColumn
atmfVpcReceiveTrafficDescriptorParam2 = _AtmfVpcReceiveTrafficDescriptorParam2_Object(
    (1, 3, 6, 1, 4, 1, 353, 2, 4, 1, 1, 12),
    _AtmfVpcReceiveTrafficDescriptorParam2_Type()
)
atmfVpcReceiveTrafficDescriptorParam2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmfVpcReceiveTrafficDescriptorParam2.setStatus("mandatory")


class _AtmfVpcReceiveTrafficDescriptorParam3_Type(Integer32):
    """Custom type atmfVpcReceiveTrafficDescriptorParam3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AtmfVpcReceiveTrafficDescriptorParam3_Type.__name__ = "Integer32"
_AtmfVpcReceiveTrafficDescriptorParam3_Object = MibTableColumn
atmfVpcReceiveTrafficDescriptorParam3 = _AtmfVpcReceiveTrafficDescriptorParam3_Object(
    (1, 3, 6, 1, 4, 1, 353, 2, 4, 1, 1, 13),
    _AtmfVpcReceiveTrafficDescriptorParam3_Type()
)
atmfVpcReceiveTrafficDescriptorParam3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmfVpcReceiveTrafficDescriptorParam3.setStatus("mandatory")


class _AtmfVpcReceiveTrafficDescriptorParam4_Type(Integer32):
    """Custom type atmfVpcReceiveTrafficDescriptorParam4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AtmfVpcReceiveTrafficDescriptorParam4_Type.__name__ = "Integer32"
_AtmfVpcReceiveTrafficDescriptorParam4_Object = MibTableColumn
atmfVpcReceiveTrafficDescriptorParam4 = _AtmfVpcReceiveTrafficDescriptorParam4_Object(
    (1, 3, 6, 1, 4, 1, 353, 2, 4, 1, 1, 14),
    _AtmfVpcReceiveTrafficDescriptorParam4_Type()
)
atmfVpcReceiveTrafficDescriptorParam4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmfVpcReceiveTrafficDescriptorParam4.setStatus("mandatory")


class _AtmfVpcReceiveTrafficDescriptorParam5_Type(Integer32):
    """Custom type atmfVpcReceiveTrafficDescriptorParam5 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AtmfVpcReceiveTrafficDescriptorParam5_Type.__name__ = "Integer32"
_AtmfVpcReceiveTrafficDescriptorParam5_Object = MibTableColumn
atmfVpcReceiveTrafficDescriptorParam5 = _AtmfVpcReceiveTrafficDescriptorParam5_Object(
    (1, 3, 6, 1, 4, 1, 353, 2, 4, 1, 1, 15),
    _AtmfVpcReceiveTrafficDescriptorParam5_Type()
)
atmfVpcReceiveTrafficDescriptorParam5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmfVpcReceiveTrafficDescriptorParam5.setStatus("mandatory")


class _AtmfVpcQoSCategory_Type(Integer32):
    """Custom type atmfVpcQoSCategory based on Integer32"""
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
        *(("deterministic", 2),
          ("other", 1),
          ("statistical", 3),
          ("unspecified", 4))
    )


_AtmfVpcQoSCategory_Type.__name__ = "Integer32"
_AtmfVpcQoSCategory_Object = MibTableColumn
atmfVpcQoSCategory = _AtmfVpcQoSCategory_Object(
    (1, 3, 6, 1, 4, 1, 353, 2, 4, 1, 1, 16),
    _AtmfVpcQoSCategory_Type()
)
atmfVpcQoSCategory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmfVpcQoSCategory.setStatus("obsolete")


class _AtmfVpcTransmitQoSClass_Type(Integer32):
    """Custom type atmfVpcTransmitQoSClass based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AtmfVpcTransmitQoSClass_Type.__name__ = "Integer32"
_AtmfVpcTransmitQoSClass_Object = MibTableColumn
atmfVpcTransmitQoSClass = _AtmfVpcTransmitQoSClass_Object(
    (1, 3, 6, 1, 4, 1, 353, 2, 4, 1, 1, 17),
    _AtmfVpcTransmitQoSClass_Type()
)
atmfVpcTransmitQoSClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmfVpcTransmitQoSClass.setStatus("obsolete")


class _AtmfVpcReceiveQoSClass_Type(Integer32):
    """Custom type atmfVpcReceiveQoSClass based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AtmfVpcReceiveQoSClass_Type.__name__ = "Integer32"
_AtmfVpcReceiveQoSClass_Object = MibTableColumn
atmfVpcReceiveQoSClass = _AtmfVpcReceiveQoSClass_Object(
    (1, 3, 6, 1, 4, 1, 353, 2, 4, 1, 1, 18),
    _AtmfVpcReceiveQoSClass_Type()
)
atmfVpcReceiveQoSClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmfVpcReceiveQoSClass.setStatus("obsolete")
_AtmfVpcBestEffortIndicator_Type = TruthValue
_AtmfVpcBestEffortIndicator_Object = MibTableColumn
atmfVpcBestEffortIndicator = _AtmfVpcBestEffortIndicator_Object(
    (1, 3, 6, 1, 4, 1, 353, 2, 4, 1, 1, 19),
    _AtmfVpcBestEffortIndicator_Type()
)
atmfVpcBestEffortIndicator.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmfVpcBestEffortIndicator.setStatus("mandatory")
_AtmfVpcServiceCategory_Type = AtmServiceCategory
_AtmfVpcServiceCategory_Object = MibTableColumn
atmfVpcServiceCategory = _AtmfVpcServiceCategory_Object(
    (1, 3, 6, 1, 4, 1, 353, 2, 4, 1, 1, 20),
    _AtmfVpcServiceCategory_Type()
)
atmfVpcServiceCategory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmfVpcServiceCategory.setStatus("mandatory")
_AtmfVccGroup_ObjectIdentity = ObjectIdentity
atmfVccGroup = _AtmfVccGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353, 2, 5)
)
_AtmfVccTable_Object = MibTable
atmfVccTable = _AtmfVccTable_Object(
    (1, 3, 6, 1, 4, 1, 353, 2, 5, 1)
)
if mibBuilder.loadTexts:
    atmfVccTable.setStatus("mandatory")
_AtmfVccEntry_Object = MibTableRow
atmfVccEntry = _AtmfVccEntry_Object(
    (1, 3, 6, 1, 4, 1, 353, 2, 5, 1, 1)
)
atmfVccEntry.setIndexNames(
    (0, "AXD301-ILMI-MIB", "atmfVccPortIndex"),
    (0, "AXD301-ILMI-MIB", "atmfVccVpi"),
    (0, "AXD301-ILMI-MIB", "atmfVccVci"),
)
if mibBuilder.loadTexts:
    atmfVccEntry.setStatus("mandatory")


class _AtmfVccPortIndex_Type(Integer32):
    """Custom type atmfVccPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AtmfVccPortIndex_Type.__name__ = "Integer32"
_AtmfVccPortIndex_Object = MibTableColumn
atmfVccPortIndex = _AtmfVccPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 353, 2, 5, 1, 1, 1),
    _AtmfVccPortIndex_Type()
)
atmfVccPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmfVccPortIndex.setStatus("mandatory")


class _AtmfVccVpi_Type(Integer32):
    """Custom type atmfVccVpi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_AtmfVccVpi_Type.__name__ = "Integer32"
_AtmfVccVpi_Object = MibTableColumn
atmfVccVpi = _AtmfVccVpi_Object(
    (1, 3, 6, 1, 4, 1, 353, 2, 5, 1, 1, 2),
    _AtmfVccVpi_Type()
)
atmfVccVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmfVccVpi.setStatus("mandatory")


class _AtmfVccVci_Type(Integer32):
    """Custom type atmfVccVci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AtmfVccVci_Type.__name__ = "Integer32"
_AtmfVccVci_Object = MibTableColumn
atmfVccVci = _AtmfVccVci_Object(
    (1, 3, 6, 1, 4, 1, 353, 2, 5, 1, 1, 3),
    _AtmfVccVci_Type()
)
atmfVccVci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmfVccVci.setStatus("mandatory")


class _AtmfVccOperStatus_Type(Integer32):
    """Custom type atmfVccOperStatus based on Integer32"""
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
        *(("end2endDown", 3),
          ("end2endUp", 2),
          ("localDown", 5),
          ("localUpEnd2endUnknown", 4),
          ("unknown", 1))
    )


_AtmfVccOperStatus_Type.__name__ = "Integer32"
_AtmfVccOperStatus_Object = MibTableColumn
atmfVccOperStatus = _AtmfVccOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 353, 2, 5, 1, 1, 4),
    _AtmfVccOperStatus_Type()
)
atmfVccOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmfVccOperStatus.setStatus("mandatory")
_AtmfVccTransmitTrafficDescriptorType_Type = ObjectIdentifier
_AtmfVccTransmitTrafficDescriptorType_Object = MibTableColumn
atmfVccTransmitTrafficDescriptorType = _AtmfVccTransmitTrafficDescriptorType_Object(
    (1, 3, 6, 1, 4, 1, 353, 2, 5, 1, 1, 5),
    _AtmfVccTransmitTrafficDescriptorType_Type()
)
atmfVccTransmitTrafficDescriptorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmfVccTransmitTrafficDescriptorType.setStatus("mandatory")


class _AtmfVccTransmitTrafficDescriptorParam1_Type(Integer32):
    """Custom type atmfVccTransmitTrafficDescriptorParam1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AtmfVccTransmitTrafficDescriptorParam1_Type.__name__ = "Integer32"
_AtmfVccTransmitTrafficDescriptorParam1_Object = MibTableColumn
atmfVccTransmitTrafficDescriptorParam1 = _AtmfVccTransmitTrafficDescriptorParam1_Object(
    (1, 3, 6, 1, 4, 1, 353, 2, 5, 1, 1, 6),
    _AtmfVccTransmitTrafficDescriptorParam1_Type()
)
atmfVccTransmitTrafficDescriptorParam1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmfVccTransmitTrafficDescriptorParam1.setStatus("mandatory")


class _AtmfVccTransmitTrafficDescriptorParam2_Type(Integer32):
    """Custom type atmfVccTransmitTrafficDescriptorParam2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AtmfVccTransmitTrafficDescriptorParam2_Type.__name__ = "Integer32"
_AtmfVccTransmitTrafficDescriptorParam2_Object = MibTableColumn
atmfVccTransmitTrafficDescriptorParam2 = _AtmfVccTransmitTrafficDescriptorParam2_Object(
    (1, 3, 6, 1, 4, 1, 353, 2, 5, 1, 1, 7),
    _AtmfVccTransmitTrafficDescriptorParam2_Type()
)
atmfVccTransmitTrafficDescriptorParam2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmfVccTransmitTrafficDescriptorParam2.setStatus("mandatory")


class _AtmfVccTransmitTrafficDescriptorParam3_Type(Integer32):
    """Custom type atmfVccTransmitTrafficDescriptorParam3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AtmfVccTransmitTrafficDescriptorParam3_Type.__name__ = "Integer32"
_AtmfVccTransmitTrafficDescriptorParam3_Object = MibTableColumn
atmfVccTransmitTrafficDescriptorParam3 = _AtmfVccTransmitTrafficDescriptorParam3_Object(
    (1, 3, 6, 1, 4, 1, 353, 2, 5, 1, 1, 8),
    _AtmfVccTransmitTrafficDescriptorParam3_Type()
)
atmfVccTransmitTrafficDescriptorParam3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmfVccTransmitTrafficDescriptorParam3.setStatus("mandatory")


class _AtmfVccTransmitTrafficDescriptorParam4_Type(Integer32):
    """Custom type atmfVccTransmitTrafficDescriptorParam4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AtmfVccTransmitTrafficDescriptorParam4_Type.__name__ = "Integer32"
_AtmfVccTransmitTrafficDescriptorParam4_Object = MibTableColumn
atmfVccTransmitTrafficDescriptorParam4 = _AtmfVccTransmitTrafficDescriptorParam4_Object(
    (1, 3, 6, 1, 4, 1, 353, 2, 5, 1, 1, 9),
    _AtmfVccTransmitTrafficDescriptorParam4_Type()
)
atmfVccTransmitTrafficDescriptorParam4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmfVccTransmitTrafficDescriptorParam4.setStatus("mandatory")


class _AtmfVccTransmitTrafficDescriptorParam5_Type(Integer32):
    """Custom type atmfVccTransmitTrafficDescriptorParam5 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AtmfVccTransmitTrafficDescriptorParam5_Type.__name__ = "Integer32"
_AtmfVccTransmitTrafficDescriptorParam5_Object = MibTableColumn
atmfVccTransmitTrafficDescriptorParam5 = _AtmfVccTransmitTrafficDescriptorParam5_Object(
    (1, 3, 6, 1, 4, 1, 353, 2, 5, 1, 1, 10),
    _AtmfVccTransmitTrafficDescriptorParam5_Type()
)
atmfVccTransmitTrafficDescriptorParam5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmfVccTransmitTrafficDescriptorParam5.setStatus("mandatory")
_AtmfVccReceiveTrafficDescriptorType_Type = ObjectIdentifier
_AtmfVccReceiveTrafficDescriptorType_Object = MibTableColumn
atmfVccReceiveTrafficDescriptorType = _AtmfVccReceiveTrafficDescriptorType_Object(
    (1, 3, 6, 1, 4, 1, 353, 2, 5, 1, 1, 11),
    _AtmfVccReceiveTrafficDescriptorType_Type()
)
atmfVccReceiveTrafficDescriptorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmfVccReceiveTrafficDescriptorType.setStatus("mandatory")


class _AtmfVccReceiveTrafficDescriptorParam1_Type(Integer32):
    """Custom type atmfVccReceiveTrafficDescriptorParam1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AtmfVccReceiveTrafficDescriptorParam1_Type.__name__ = "Integer32"
_AtmfVccReceiveTrafficDescriptorParam1_Object = MibTableColumn
atmfVccReceiveTrafficDescriptorParam1 = _AtmfVccReceiveTrafficDescriptorParam1_Object(
    (1, 3, 6, 1, 4, 1, 353, 2, 5, 1, 1, 12),
    _AtmfVccReceiveTrafficDescriptorParam1_Type()
)
atmfVccReceiveTrafficDescriptorParam1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmfVccReceiveTrafficDescriptorParam1.setStatus("mandatory")


class _AtmfVccReceiveTrafficDescriptorParam2_Type(Integer32):
    """Custom type atmfVccReceiveTrafficDescriptorParam2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AtmfVccReceiveTrafficDescriptorParam2_Type.__name__ = "Integer32"
_AtmfVccReceiveTrafficDescriptorParam2_Object = MibTableColumn
atmfVccReceiveTrafficDescriptorParam2 = _AtmfVccReceiveTrafficDescriptorParam2_Object(
    (1, 3, 6, 1, 4, 1, 353, 2, 5, 1, 1, 13),
    _AtmfVccReceiveTrafficDescriptorParam2_Type()
)
atmfVccReceiveTrafficDescriptorParam2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmfVccReceiveTrafficDescriptorParam2.setStatus("mandatory")


class _AtmfVccReceiveTrafficDescriptorParam3_Type(Integer32):
    """Custom type atmfVccReceiveTrafficDescriptorParam3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AtmfVccReceiveTrafficDescriptorParam3_Type.__name__ = "Integer32"
_AtmfVccReceiveTrafficDescriptorParam3_Object = MibTableColumn
atmfVccReceiveTrafficDescriptorParam3 = _AtmfVccReceiveTrafficDescriptorParam3_Object(
    (1, 3, 6, 1, 4, 1, 353, 2, 5, 1, 1, 14),
    _AtmfVccReceiveTrafficDescriptorParam3_Type()
)
atmfVccReceiveTrafficDescriptorParam3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmfVccReceiveTrafficDescriptorParam3.setStatus("mandatory")


class _AtmfVccReceiveTrafficDescriptorParam4_Type(Integer32):
    """Custom type atmfVccReceiveTrafficDescriptorParam4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AtmfVccReceiveTrafficDescriptorParam4_Type.__name__ = "Integer32"
_AtmfVccReceiveTrafficDescriptorParam4_Object = MibTableColumn
atmfVccReceiveTrafficDescriptorParam4 = _AtmfVccReceiveTrafficDescriptorParam4_Object(
    (1, 3, 6, 1, 4, 1, 353, 2, 5, 1, 1, 15),
    _AtmfVccReceiveTrafficDescriptorParam4_Type()
)
atmfVccReceiveTrafficDescriptorParam4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmfVccReceiveTrafficDescriptorParam4.setStatus("mandatory")


class _AtmfVccReceiveTrafficDescriptorParam5_Type(Integer32):
    """Custom type atmfVccReceiveTrafficDescriptorParam5 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AtmfVccReceiveTrafficDescriptorParam5_Type.__name__ = "Integer32"
_AtmfVccReceiveTrafficDescriptorParam5_Object = MibTableColumn
atmfVccReceiveTrafficDescriptorParam5 = _AtmfVccReceiveTrafficDescriptorParam5_Object(
    (1, 3, 6, 1, 4, 1, 353, 2, 5, 1, 1, 16),
    _AtmfVccReceiveTrafficDescriptorParam5_Type()
)
atmfVccReceiveTrafficDescriptorParam5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmfVccReceiveTrafficDescriptorParam5.setStatus("mandatory")


class _AtmfVccQoSCategory_Type(Integer32):
    """Custom type atmfVccQoSCategory based on Integer32"""
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
        *(("deterministic", 2),
          ("other", 1),
          ("statistical", 3),
          ("unspecified", 4))
    )


_AtmfVccQoSCategory_Type.__name__ = "Integer32"
_AtmfVccQoSCategory_Object = MibTableColumn
atmfVccQoSCategory = _AtmfVccQoSCategory_Object(
    (1, 3, 6, 1, 4, 1, 353, 2, 5, 1, 1, 17),
    _AtmfVccQoSCategory_Type()
)
atmfVccQoSCategory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmfVccQoSCategory.setStatus("obsolete")


class _AtmfVccTransmitQoSClass_Type(Integer32):
    """Custom type atmfVccTransmitQoSClass based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AtmfVccTransmitQoSClass_Type.__name__ = "Integer32"
_AtmfVccTransmitQoSClass_Object = MibTableColumn
atmfVccTransmitQoSClass = _AtmfVccTransmitQoSClass_Object(
    (1, 3, 6, 1, 4, 1, 353, 2, 5, 1, 1, 18),
    _AtmfVccTransmitQoSClass_Type()
)
atmfVccTransmitQoSClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmfVccTransmitQoSClass.setStatus("obsolete")


class _AtmfVccReceiveQoSClass_Type(Integer32):
    """Custom type atmfVccReceiveQoSClass based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AtmfVccReceiveQoSClass_Type.__name__ = "Integer32"
_AtmfVccReceiveQoSClass_Object = MibTableColumn
atmfVccReceiveQoSClass = _AtmfVccReceiveQoSClass_Object(
    (1, 3, 6, 1, 4, 1, 353, 2, 5, 1, 1, 19),
    _AtmfVccReceiveQoSClass_Type()
)
atmfVccReceiveQoSClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmfVccReceiveQoSClass.setStatus("obsolete")
_AtmfVccBestEffortIndicator_Type = TruthValue
_AtmfVccBestEffortIndicator_Object = MibTableColumn
atmfVccBestEffortIndicator = _AtmfVccBestEffortIndicator_Object(
    (1, 3, 6, 1, 4, 1, 353, 2, 5, 1, 1, 20),
    _AtmfVccBestEffortIndicator_Type()
)
atmfVccBestEffortIndicator.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmfVccBestEffortIndicator.setStatus("mandatory")
_AtmfVccTransmitFrameDiscard_Type = TruthValue
_AtmfVccTransmitFrameDiscard_Object = MibTableColumn
atmfVccTransmitFrameDiscard = _AtmfVccTransmitFrameDiscard_Object(
    (1, 3, 6, 1, 4, 1, 353, 2, 5, 1, 1, 21),
    _AtmfVccTransmitFrameDiscard_Type()
)
atmfVccTransmitFrameDiscard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmfVccTransmitFrameDiscard.setStatus("mandatory")
_AtmfVccReceiveFrameDiscard_Type = TruthValue
_AtmfVccReceiveFrameDiscard_Object = MibTableColumn
atmfVccReceiveFrameDiscard = _AtmfVccReceiveFrameDiscard_Object(
    (1, 3, 6, 1, 4, 1, 353, 2, 5, 1, 1, 22),
    _AtmfVccReceiveFrameDiscard_Type()
)
atmfVccReceiveFrameDiscard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmfVccReceiveFrameDiscard.setStatus("mandatory")
_AtmfVccServiceCategory_Type = AtmServiceCategory
_AtmfVccServiceCategory_Object = MibTableColumn
atmfVccServiceCategory = _AtmfVccServiceCategory_Object(
    (1, 3, 6, 1, 4, 1, 353, 2, 5, 1, 1, 23),
    _AtmfVccServiceCategory_Type()
)
atmfVccServiceCategory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmfVccServiceCategory.setStatus("mandatory")
_AtmfAddressGroup_ObjectIdentity = ObjectIdentity
atmfAddressGroup = _AtmfAddressGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353, 2, 6)
)
_AtmfAddressTable_Object = MibTable
atmfAddressTable = _AtmfAddressTable_Object(
    (1, 3, 6, 1, 4, 1, 353, 2, 6, 1)
)
if mibBuilder.loadTexts:
    atmfAddressTable.setStatus("mandatory")
_AtmfAddressEntry_Object = MibTableRow
atmfAddressEntry = _AtmfAddressEntry_Object(
    (1, 3, 6, 1, 4, 1, 353, 2, 6, 1, 1)
)
atmfAddressEntry.setIndexNames(
    (0, "AXD301-ILMI-MIB", "atmfAddressPort"),
    (0, "AXD301-ILMI-MIB", "atmfAddressAtmAddress"),
)
if mibBuilder.loadTexts:
    atmfAddressEntry.setStatus("mandatory")


class _AtmfAddressPort_Type(Integer32):
    """Custom type atmfAddressPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AtmfAddressPort_Type.__name__ = "Integer32"
_AtmfAddressPort_Object = MibTableColumn
atmfAddressPort = _AtmfAddressPort_Object(
    (1, 3, 6, 1, 4, 1, 353, 2, 6, 1, 1, 1),
    _AtmfAddressPort_Type()
)
atmfAddressPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    atmfAddressPort.setStatus("mandatory")
_AtmfAddressAtmAddress_Type = AtmAddress
_AtmfAddressAtmAddress_Object = MibTableColumn
atmfAddressAtmAddress = _AtmfAddressAtmAddress_Object(
    (1, 3, 6, 1, 4, 1, 353, 2, 6, 1, 1, 2),
    _AtmfAddressAtmAddress_Type()
)
atmfAddressAtmAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    atmfAddressAtmAddress.setStatus("mandatory")


class _AtmfAddressStatus_Type(Integer32):
    """Custom type atmfAddressStatus based on Integer32"""
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


_AtmfAddressStatus_Type.__name__ = "Integer32"
_AtmfAddressStatus_Object = MibTableColumn
atmfAddressStatus = _AtmfAddressStatus_Object(
    (1, 3, 6, 1, 4, 1, 353, 2, 6, 1, 1, 3),
    _AtmfAddressStatus_Type()
)
atmfAddressStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmfAddressStatus.setStatus("mandatory")


class _AtmfAddressOrgScope_Type(Integer32):
    """Custom type atmfAddressOrgScope based on Integer32"""
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
              9,
              10,
              11,
              12,
              13,
              14,
              15)
        )
    )
    namedValues = NamedValues(
        *(("communityMinusOne", 10),
          ("communityPlusOne", 12),
          ("global", 15),
          ("interRegional", 14),
          ("intraCommunity", 11),
          ("intraOrganization", 8),
          ("intraSite", 5),
          ("localNetwork", 1),
          ("localNetworkPlusOne", 2),
          ("localNetworkPlusTwo", 3),
          ("organizationMinusOne", 7),
          ("organizationPlusOne", 9),
          ("regional", 13),
          ("siteMinusOne", 4),
          ("sitePlusOne", 6))
    )


_AtmfAddressOrgScope_Type.__name__ = "Integer32"
_AtmfAddressOrgScope_Object = MibTableColumn
atmfAddressOrgScope = _AtmfAddressOrgScope_Object(
    (1, 3, 6, 1, 4, 1, 353, 2, 6, 1, 1, 4),
    _AtmfAddressOrgScope_Type()
)
atmfAddressOrgScope.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmfAddressOrgScope.setStatus("mandatory")
_AtmfNetPrefixGroup_ObjectIdentity = ObjectIdentity
atmfNetPrefixGroup = _AtmfNetPrefixGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353, 2, 7)
)
_AtmfNetPrefixTable_Object = MibTable
atmfNetPrefixTable = _AtmfNetPrefixTable_Object(
    (1, 3, 6, 1, 4, 1, 353, 2, 7, 1)
)
if mibBuilder.loadTexts:
    atmfNetPrefixTable.setStatus("mandatory")
_AtmfNetPrefixEntry_Object = MibTableRow
atmfNetPrefixEntry = _AtmfNetPrefixEntry_Object(
    (1, 3, 6, 1, 4, 1, 353, 2, 7, 1, 1)
)
atmfNetPrefixEntry.setIndexNames(
    (0, "AXD301-ILMI-MIB", "atmfNetPrefixPort"),
    (0, "AXD301-ILMI-MIB", "atmfNetPrefixPrefix"),
)
if mibBuilder.loadTexts:
    atmfNetPrefixEntry.setStatus("mandatory")


class _AtmfNetPrefixPort_Type(Integer32):
    """Custom type atmfNetPrefixPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AtmfNetPrefixPort_Type.__name__ = "Integer32"
_AtmfNetPrefixPort_Object = MibTableColumn
atmfNetPrefixPort = _AtmfNetPrefixPort_Object(
    (1, 3, 6, 1, 4, 1, 353, 2, 7, 1, 1, 1),
    _AtmfNetPrefixPort_Type()
)
atmfNetPrefixPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    atmfNetPrefixPort.setStatus("mandatory")
_AtmfNetPrefixPrefix_Type = NetPrefix
_AtmfNetPrefixPrefix_Object = MibTableColumn
atmfNetPrefixPrefix = _AtmfNetPrefixPrefix_Object(
    (1, 3, 6, 1, 4, 1, 353, 2, 7, 1, 1, 2),
    _AtmfNetPrefixPrefix_Type()
)
atmfNetPrefixPrefix.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    atmfNetPrefixPrefix.setStatus("mandatory")


class _AtmfNetPrefixStatus_Type(Integer32):
    """Custom type atmfNetPrefixStatus based on Integer32"""
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


_AtmfNetPrefixStatus_Type.__name__ = "Integer32"
_AtmfNetPrefixStatus_Object = MibTableColumn
atmfNetPrefixStatus = _AtmfNetPrefixStatus_Object(
    (1, 3, 6, 1, 4, 1, 353, 2, 7, 1, 1, 3),
    _AtmfNetPrefixStatus_Type()
)
atmfNetPrefixStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmfNetPrefixStatus.setStatus("mandatory")
_AtmfSrvcRegistryGroup_ObjectIdentity = ObjectIdentity
atmfSrvcRegistryGroup = _AtmfSrvcRegistryGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353, 2, 8)
)
_AtmfVpcAbrGroup_ObjectIdentity = ObjectIdentity
atmfVpcAbrGroup = _AtmfVpcAbrGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353, 2, 9)
)
_AtmfVpcAbrTable_Object = MibTable
atmfVpcAbrTable = _AtmfVpcAbrTable_Object(
    (1, 3, 6, 1, 4, 1, 353, 2, 9, 1)
)
if mibBuilder.loadTexts:
    atmfVpcAbrTable.setStatus("mandatory")
_AtmfVpcAbrEntry_Object = MibTableRow
atmfVpcAbrEntry = _AtmfVpcAbrEntry_Object(
    (1, 3, 6, 1, 4, 1, 353, 2, 9, 1, 1)
)
atmfVpcAbrEntry.setIndexNames(
    (0, "AXD301-ILMI-MIB", "atmfVpcAbrPortIndex"),
    (0, "AXD301-ILMI-MIB", "atmfVpcAbrVpi"),
)
if mibBuilder.loadTexts:
    atmfVpcAbrEntry.setStatus("mandatory")


class _AtmfVpcAbrPortIndex_Type(Integer32):
    """Custom type atmfVpcAbrPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AtmfVpcAbrPortIndex_Type.__name__ = "Integer32"
_AtmfVpcAbrPortIndex_Object = MibTableColumn
atmfVpcAbrPortIndex = _AtmfVpcAbrPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 353, 2, 9, 1, 1, 1),
    _AtmfVpcAbrPortIndex_Type()
)
atmfVpcAbrPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmfVpcAbrPortIndex.setStatus("mandatory")


class _AtmfVpcAbrVpi_Type(Integer32):
    """Custom type atmfVpcAbrVpi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_AtmfVpcAbrVpi_Type.__name__ = "Integer32"
_AtmfVpcAbrVpi_Object = MibTableColumn
atmfVpcAbrVpi = _AtmfVpcAbrVpi_Object(
    (1, 3, 6, 1, 4, 1, 353, 2, 9, 1, 1, 2),
    _AtmfVpcAbrVpi_Type()
)
atmfVpcAbrVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmfVpcAbrVpi.setStatus("mandatory")


class _AtmfVpcAbrTransmitIcr_Type(Integer32):
    """Custom type atmfVpcAbrTransmitIcr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_AtmfVpcAbrTransmitIcr_Type.__name__ = "Integer32"
_AtmfVpcAbrTransmitIcr_Object = MibTableColumn
atmfVpcAbrTransmitIcr = _AtmfVpcAbrTransmitIcr_Object(
    (1, 3, 6, 1, 4, 1, 353, 2, 9, 1, 1, 3),
    _AtmfVpcAbrTransmitIcr_Type()
)
atmfVpcAbrTransmitIcr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmfVpcAbrTransmitIcr.setStatus("mandatory")


class _AtmfVpcAbrTransmitNrm_Type(Integer32):
    """Custom type atmfVpcAbrTransmitNrm based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("nrm128", 7),
          ("nrm16", 4),
          ("nrm2", 1),
          ("nrm256", 8),
          ("nrm32", 5),
          ("nrm4", 2),
          ("nrm64", 6),
          ("nrm8", 3))
    )


_AtmfVpcAbrTransmitNrm_Type.__name__ = "Integer32"
_AtmfVpcAbrTransmitNrm_Object = MibTableColumn
atmfVpcAbrTransmitNrm = _AtmfVpcAbrTransmitNrm_Object(
    (1, 3, 6, 1, 4, 1, 353, 2, 9, 1, 1, 4),
    _AtmfVpcAbrTransmitNrm_Type()
)
atmfVpcAbrTransmitNrm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmfVpcAbrTransmitNrm.setStatus("mandatory")


class _AtmfVpcAbrTransmitTrm_Type(Integer32):
    """Custom type atmfVpcAbrTransmitTrm based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("trm0point78125", 1),
          ("trm100", 8),
          ("trm12point5", 5),
          ("trm1point5625", 2),
          ("trm25", 6),
          ("trm3point125", 3),
          ("trm50", 7),
          ("trm6point25", 4))
    )


_AtmfVpcAbrTransmitTrm_Type.__name__ = "Integer32"
_AtmfVpcAbrTransmitTrm_Object = MibTableColumn
atmfVpcAbrTransmitTrm = _AtmfVpcAbrTransmitTrm_Object(
    (1, 3, 6, 1, 4, 1, 353, 2, 9, 1, 1, 5),
    _AtmfVpcAbrTransmitTrm_Type()
)
atmfVpcAbrTransmitTrm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmfVpcAbrTransmitTrm.setStatus("mandatory")


class _AtmfVpcAbrTransmitCdf_Type(Integer32):
    """Custom type atmfVpcAbrTransmitCdf based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("cdf0", 1),
          ("cdfOne", 8),
          ("cdfOneOver16", 4),
          ("cdfOneOver2", 7),
          ("cdfOneOver32", 3),
          ("cdfOneOver4", 6),
          ("cdfOneOver64", 2),
          ("cdfOneOver8", 5))
    )


_AtmfVpcAbrTransmitCdf_Type.__name__ = "Integer32"
_AtmfVpcAbrTransmitCdf_Object = MibTableColumn
atmfVpcAbrTransmitCdf = _AtmfVpcAbrTransmitCdf_Object(
    (1, 3, 6, 1, 4, 1, 353, 2, 9, 1, 1, 6),
    _AtmfVpcAbrTransmitCdf_Type()
)
atmfVpcAbrTransmitCdf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmfVpcAbrTransmitCdf.setStatus("mandatory")


class _AtmfVpcAbrTransmitRif_Type(Integer32):
    """Custom type atmfVpcAbrTransmitRif based on Integer32"""
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
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16)
        )
    )
    namedValues = NamedValues(
        *(("rifOne", 16),
          ("rifOneOver1024", 6),
          ("rifOneOver128", 9),
          ("rifOneOver16", 12),
          ("rifOneOver16384", 2),
          ("rifOneOver2", 15),
          ("rifOneOver2048", 5),
          ("rifOneOver256", 8),
          ("rifOneOver32", 11),
          ("rifOneOver32768", 1),
          ("rifOneOver4", 14),
          ("rifOneOver4096", 4),
          ("rifOneOver512", 7),
          ("rifOneOver64", 10),
          ("rifOneOver8", 13),
          ("rifOneOver8192", 3))
    )


_AtmfVpcAbrTransmitRif_Type.__name__ = "Integer32"
_AtmfVpcAbrTransmitRif_Object = MibTableColumn
atmfVpcAbrTransmitRif = _AtmfVpcAbrTransmitRif_Object(
    (1, 3, 6, 1, 4, 1, 353, 2, 9, 1, 1, 7),
    _AtmfVpcAbrTransmitRif_Type()
)
atmfVpcAbrTransmitRif.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmfVpcAbrTransmitRif.setStatus("mandatory")


class _AtmfVpcAbrTransmitRdf_Type(Integer32):
    """Custom type atmfVpcAbrTransmitRdf based on Integer32"""
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
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16)
        )
    )
    namedValues = NamedValues(
        *(("rdfOne", 16),
          ("rdfOneOver1024", 6),
          ("rdfOneOver128", 9),
          ("rdfOneOver16", 12),
          ("rdfOneOver16384", 2),
          ("rdfOneOver2", 15),
          ("rdfOneOver2048", 5),
          ("rdfOneOver256", 8),
          ("rdfOneOver32", 11),
          ("rdfOneOver32768", 1),
          ("rdfOneOver4", 14),
          ("rdfOneOver4096", 4),
          ("rdfOneOver512", 7),
          ("rdfOneOver64", 10),
          ("rdfOneOver8", 13),
          ("rdfOneOver8192", 3))
    )


_AtmfVpcAbrTransmitRdf_Type.__name__ = "Integer32"
_AtmfVpcAbrTransmitRdf_Object = MibTableColumn
atmfVpcAbrTransmitRdf = _AtmfVpcAbrTransmitRdf_Object(
    (1, 3, 6, 1, 4, 1, 353, 2, 9, 1, 1, 8),
    _AtmfVpcAbrTransmitRdf_Type()
)
atmfVpcAbrTransmitRdf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmfVpcAbrTransmitRdf.setStatus("mandatory")


class _AtmfVpcAbrTransmitAdtf_Type(Integer32):
    """Custom type atmfVpcAbrTransmitAdtf based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1023),
    )


_AtmfVpcAbrTransmitAdtf_Type.__name__ = "Integer32"
_AtmfVpcAbrTransmitAdtf_Object = MibTableColumn
atmfVpcAbrTransmitAdtf = _AtmfVpcAbrTransmitAdtf_Object(
    (1, 3, 6, 1, 4, 1, 353, 2, 9, 1, 1, 9),
    _AtmfVpcAbrTransmitAdtf_Type()
)
atmfVpcAbrTransmitAdtf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmfVpcAbrTransmitAdtf.setStatus("mandatory")


class _AtmfVpcAbrTransmitCrm_Type(Integer32):
    """Custom type atmfVpcAbrTransmitCrm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8388608),
    )


_AtmfVpcAbrTransmitCrm_Type.__name__ = "Integer32"
_AtmfVpcAbrTransmitCrm_Object = MibTableColumn
atmfVpcAbrTransmitCrm = _AtmfVpcAbrTransmitCrm_Object(
    (1, 3, 6, 1, 4, 1, 353, 2, 9, 1, 1, 10),
    _AtmfVpcAbrTransmitCrm_Type()
)
atmfVpcAbrTransmitCrm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmfVpcAbrTransmitCrm.setStatus("mandatory")
_AtmfVccAbrGroup_ObjectIdentity = ObjectIdentity
atmfVccAbrGroup = _AtmfVccAbrGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353, 2, 10)
)
_AtmfVccAbrTable_Object = MibTable
atmfVccAbrTable = _AtmfVccAbrTable_Object(
    (1, 3, 6, 1, 4, 1, 353, 2, 10, 1)
)
if mibBuilder.loadTexts:
    atmfVccAbrTable.setStatus("mandatory")
_AtmfVccAbrEntry_Object = MibTableRow
atmfVccAbrEntry = _AtmfVccAbrEntry_Object(
    (1, 3, 6, 1, 4, 1, 353, 2, 10, 1, 1)
)
atmfVccAbrEntry.setIndexNames(
    (0, "AXD301-ILMI-MIB", "atmfVccAbrPortIndex"),
    (0, "AXD301-ILMI-MIB", "atmfVccAbrVpi"),
    (0, "AXD301-ILMI-MIB", "atmfVccAbrVci"),
)
if mibBuilder.loadTexts:
    atmfVccAbrEntry.setStatus("mandatory")


class _AtmfVccAbrPortIndex_Type(Integer32):
    """Custom type atmfVccAbrPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AtmfVccAbrPortIndex_Type.__name__ = "Integer32"
_AtmfVccAbrPortIndex_Object = MibTableColumn
atmfVccAbrPortIndex = _AtmfVccAbrPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 353, 2, 10, 1, 1, 1),
    _AtmfVccAbrPortIndex_Type()
)
atmfVccAbrPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmfVccAbrPortIndex.setStatus("mandatory")


class _AtmfVccAbrVpi_Type(Integer32):
    """Custom type atmfVccAbrVpi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_AtmfVccAbrVpi_Type.__name__ = "Integer32"
_AtmfVccAbrVpi_Object = MibTableColumn
atmfVccAbrVpi = _AtmfVccAbrVpi_Object(
    (1, 3, 6, 1, 4, 1, 353, 2, 10, 1, 1, 2),
    _AtmfVccAbrVpi_Type()
)
atmfVccAbrVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmfVccAbrVpi.setStatus("mandatory")


class _AtmfVccAbrVci_Type(Integer32):
    """Custom type atmfVccAbrVci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AtmfVccAbrVci_Type.__name__ = "Integer32"
_AtmfVccAbrVci_Object = MibTableColumn
atmfVccAbrVci = _AtmfVccAbrVci_Object(
    (1, 3, 6, 1, 4, 1, 353, 2, 10, 1, 1, 3),
    _AtmfVccAbrVci_Type()
)
atmfVccAbrVci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmfVccAbrVci.setStatus("mandatory")


class _AtmfVccAbrTransmitIcr_Type(Integer32):
    """Custom type atmfVccAbrTransmitIcr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_AtmfVccAbrTransmitIcr_Type.__name__ = "Integer32"
_AtmfVccAbrTransmitIcr_Object = MibTableColumn
atmfVccAbrTransmitIcr = _AtmfVccAbrTransmitIcr_Object(
    (1, 3, 6, 1, 4, 1, 353, 2, 10, 1, 1, 4),
    _AtmfVccAbrTransmitIcr_Type()
)
atmfVccAbrTransmitIcr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmfVccAbrTransmitIcr.setStatus("mandatory")


class _AtmfVccAbrTransmitNrm_Type(Integer32):
    """Custom type atmfVccAbrTransmitNrm based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("nrm128", 7),
          ("nrm16", 4),
          ("nrm2", 1),
          ("nrm256", 8),
          ("nrm32", 5),
          ("nrm4", 2),
          ("nrm64", 6),
          ("nrm8", 3))
    )


_AtmfVccAbrTransmitNrm_Type.__name__ = "Integer32"
_AtmfVccAbrTransmitNrm_Object = MibTableColumn
atmfVccAbrTransmitNrm = _AtmfVccAbrTransmitNrm_Object(
    (1, 3, 6, 1, 4, 1, 353, 2, 10, 1, 1, 5),
    _AtmfVccAbrTransmitNrm_Type()
)
atmfVccAbrTransmitNrm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmfVccAbrTransmitNrm.setStatus("mandatory")


class _AtmfVccAbrTransmitTrm_Type(Integer32):
    """Custom type atmfVccAbrTransmitTrm based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("trm0point78125", 1),
          ("trm100", 8),
          ("trm12point5", 5),
          ("trm1point5625", 2),
          ("trm25", 6),
          ("trm3point125", 3),
          ("trm50", 7),
          ("trm6point25", 4))
    )


_AtmfVccAbrTransmitTrm_Type.__name__ = "Integer32"
_AtmfVccAbrTransmitTrm_Object = MibTableColumn
atmfVccAbrTransmitTrm = _AtmfVccAbrTransmitTrm_Object(
    (1, 3, 6, 1, 4, 1, 353, 2, 10, 1, 1, 6),
    _AtmfVccAbrTransmitTrm_Type()
)
atmfVccAbrTransmitTrm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmfVccAbrTransmitTrm.setStatus("mandatory")


class _AtmfVccAbrTransmitCdf_Type(Integer32):
    """Custom type atmfVccAbrTransmitCdf based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("cdf0", 1),
          ("cdfOne", 8),
          ("cdfOneOver16", 4),
          ("cdfOneOver2", 7),
          ("cdfOneOver32", 3),
          ("cdfOneOver4", 6),
          ("cdfOneOver64", 2),
          ("cdfOneOver8", 5))
    )


_AtmfVccAbrTransmitCdf_Type.__name__ = "Integer32"
_AtmfVccAbrTransmitCdf_Object = MibTableColumn
atmfVccAbrTransmitCdf = _AtmfVccAbrTransmitCdf_Object(
    (1, 3, 6, 1, 4, 1, 353, 2, 10, 1, 1, 7),
    _AtmfVccAbrTransmitCdf_Type()
)
atmfVccAbrTransmitCdf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmfVccAbrTransmitCdf.setStatus("mandatory")


class _AtmfVccAbrTransmitRif_Type(Integer32):
    """Custom type atmfVccAbrTransmitRif based on Integer32"""
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
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16)
        )
    )
    namedValues = NamedValues(
        *(("rifOne", 16),
          ("rifOneOver1024", 6),
          ("rifOneOver128", 9),
          ("rifOneOver16", 12),
          ("rifOneOver16384", 2),
          ("rifOneOver2", 15),
          ("rifOneOver2048", 5),
          ("rifOneOver256", 8),
          ("rifOneOver32", 11),
          ("rifOneOver32768", 1),
          ("rifOneOver4", 14),
          ("rifOneOver4096", 4),
          ("rifOneOver512", 7),
          ("rifOneOver64", 10),
          ("rifOneOver8", 13),
          ("rifOneOver8192", 3))
    )


_AtmfVccAbrTransmitRif_Type.__name__ = "Integer32"
_AtmfVccAbrTransmitRif_Object = MibTableColumn
atmfVccAbrTransmitRif = _AtmfVccAbrTransmitRif_Object(
    (1, 3, 6, 1, 4, 1, 353, 2, 10, 1, 1, 8),
    _AtmfVccAbrTransmitRif_Type()
)
atmfVccAbrTransmitRif.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmfVccAbrTransmitRif.setStatus("mandatory")


class _AtmfVccAbrTransmitRdf_Type(Integer32):
    """Custom type atmfVccAbrTransmitRdf based on Integer32"""
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
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16)
        )
    )
    namedValues = NamedValues(
        *(("rdfOne", 16),
          ("rdfOneOver1024", 6),
          ("rdfOneOver128", 9),
          ("rdfOneOver16", 12),
          ("rdfOneOver16384", 2),
          ("rdfOneOver2", 15),
          ("rdfOneOver2048", 5),
          ("rdfOneOver256", 8),
          ("rdfOneOver32", 11),
          ("rdfOneOver32768", 1),
          ("rdfOneOver4", 14),
          ("rdfOneOver4096", 4),
          ("rdfOneOver512", 7),
          ("rdfOneOver64", 10),
          ("rdfOneOver8", 13),
          ("rdfOneOver8192", 3))
    )


_AtmfVccAbrTransmitRdf_Type.__name__ = "Integer32"
_AtmfVccAbrTransmitRdf_Object = MibTableColumn
atmfVccAbrTransmitRdf = _AtmfVccAbrTransmitRdf_Object(
    (1, 3, 6, 1, 4, 1, 353, 2, 10, 1, 1, 9),
    _AtmfVccAbrTransmitRdf_Type()
)
atmfVccAbrTransmitRdf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmfVccAbrTransmitRdf.setStatus("mandatory")


class _AtmfVccAbrTransmitAdtf_Type(Integer32):
    """Custom type atmfVccAbrTransmitAdtf based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1023),
    )


_AtmfVccAbrTransmitAdtf_Type.__name__ = "Integer32"
_AtmfVccAbrTransmitAdtf_Object = MibTableColumn
atmfVccAbrTransmitAdtf = _AtmfVccAbrTransmitAdtf_Object(
    (1, 3, 6, 1, 4, 1, 353, 2, 10, 1, 1, 10),
    _AtmfVccAbrTransmitAdtf_Type()
)
atmfVccAbrTransmitAdtf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmfVccAbrTransmitAdtf.setStatus("mandatory")


class _AtmfVccAbrTransmitCrm_Type(Integer32):
    """Custom type atmfVccAbrTransmitCrm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8388608),
    )


_AtmfVccAbrTransmitCrm_Type.__name__ = "Integer32"
_AtmfVccAbrTransmitCrm_Object = MibTableColumn
atmfVccAbrTransmitCrm = _AtmfVccAbrTransmitCrm_Object(
    (1, 3, 6, 1, 4, 1, 353, 2, 10, 1, 1, 11),
    _AtmfVccAbrTransmitCrm_Type()
)
atmfVccAbrTransmitCrm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmfVccAbrTransmitCrm.setStatus("mandatory")
_AtmfAddressRegistrationAdminGroup_ObjectIdentity = ObjectIdentity
atmfAddressRegistrationAdminGroup = _AtmfAddressRegistrationAdminGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353, 2, 11)
)
_AtmfAddressRegistrationAdminTable_Object = MibTable
atmfAddressRegistrationAdminTable = _AtmfAddressRegistrationAdminTable_Object(
    (1, 3, 6, 1, 4, 1, 353, 2, 11, 1)
)
if mibBuilder.loadTexts:
    atmfAddressRegistrationAdminTable.setStatus("mandatory")
_AtmfAddressRegistrationAdminEntry_Object = MibTableRow
atmfAddressRegistrationAdminEntry = _AtmfAddressRegistrationAdminEntry_Object(
    (1, 3, 6, 1, 4, 1, 353, 2, 11, 1, 1)
)
atmfAddressRegistrationAdminEntry.setIndexNames(
    (0, "AXD301-ILMI-MIB", "atmfAddressRegistrationAdminIndex"),
)
if mibBuilder.loadTexts:
    atmfAddressRegistrationAdminEntry.setStatus("mandatory")


class _AtmfAddressRegistrationAdminIndex_Type(Integer32):
    """Custom type atmfAddressRegistrationAdminIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AtmfAddressRegistrationAdminIndex_Type.__name__ = "Integer32"
_AtmfAddressRegistrationAdminIndex_Object = MibTableColumn
atmfAddressRegistrationAdminIndex = _AtmfAddressRegistrationAdminIndex_Object(
    (1, 3, 6, 1, 4, 1, 353, 2, 11, 1, 1, 1),
    _AtmfAddressRegistrationAdminIndex_Type()
)
atmfAddressRegistrationAdminIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmfAddressRegistrationAdminIndex.setStatus("mandatory")


class _AtmfAddressRegistrationAdminStatus_Type(Integer32):
    """Custom type atmfAddressRegistrationAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("supported", 1),
          ("unsupported", 2))
    )


_AtmfAddressRegistrationAdminStatus_Type.__name__ = "Integer32"
_AtmfAddressRegistrationAdminStatus_Object = MibTableColumn
atmfAddressRegistrationAdminStatus = _AtmfAddressRegistrationAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 353, 2, 11, 1, 1, 2),
    _AtmfAddressRegistrationAdminStatus_Type()
)
atmfAddressRegistrationAdminStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmfAddressRegistrationAdminStatus.setStatus("mandatory")

# Managed Objects groups


# Notification objects

atmfVpcChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 353, 0, 1)
)
atmfVpcChange.setObjects(
      *(("AXD301-ILMI-MIB", "atmfVpcPortIndex"),
        ("AXD301-ILMI-MIB", "atmfVpcVpi"),
        ("AXD301-ILMI-MIB", "atmfVpcOperStatus"))
)
if mibBuilder.loadTexts:
    atmfVpcChange.setStatus(
        ""
    )

atmfVccChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 353, 0, 2)
)
atmfVccChange.setObjects(
      *(("AXD301-ILMI-MIB", "atmfVccPortIndex"),
        ("AXD301-ILMI-MIB", "atmfVccVci"),
        ("AXD301-ILMI-MIB", "atmfVccVpi"),
        ("AXD301-ILMI-MIB", "atmfVccOperStatus"))
)
if mibBuilder.loadTexts:
    atmfVccChange.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "AXD301-ILMI-MIB",
    **{"ClnpAddress": ClnpAddress,
       "AtmAddress": AtmAddress,
       "NetPrefix": NetPrefix,
       "system": system,
       "sysDescr": sysDescr,
       "sysObjectID": sysObjectID,
       "sysUpTime": sysUpTime,
       "sysContact": sysContact,
       "sysName": sysName,
       "sysLocation": sysLocation,
       "sysServices": sysServices,
       "atmForum": atmForum,
       "atmfVpcChange": atmfVpcChange,
       "atmfVccChange": atmfVccChange,
       "atmForumAdmin": atmForumAdmin,
       "atmfTransmissionTypes": atmfTransmissionTypes,
       "atmfUnknownType": atmfUnknownType,
       "atmfSonetSTS3c": atmfSonetSTS3c,
       "atmfDs3": atmfDs3,
       "atmf4B5B": atmf4B5B,
       "atmf8B10B": atmf8B10B,
       "atmfSonetSTS12c": atmfSonetSTS12c,
       "atmfE3": atmfE3,
       "atmfT1": atmfT1,
       "atmfE1": atmfE1,
       "atmfMediaTypes": atmfMediaTypes,
       "atmfMediaUnknownType": atmfMediaUnknownType,
       "atmfMediaCoaxCable": atmfMediaCoaxCable,
       "atmfMediaSingleMode": atmfMediaSingleMode,
       "atmfMediaMultiMode": atmfMediaMultiMode,
       "atmfMediaStp": atmfMediaStp,
       "atmfMediaUtp": atmfMediaUtp,
       "atmfTrafficDescrTypes": atmfTrafficDescrTypes,
       "atmfNoDescriptor": atmfNoDescriptor,
       "atmfPeakRate": atmfPeakRate,
       "atmfNoClpNoScr": atmfNoClpNoScr,
       "atmfClpNoTaggingNoScr": atmfClpNoTaggingNoScr,
       "atmfClpTaggingNoScr": atmfClpTaggingNoScr,
       "atmfNoClpScr": atmfNoClpScr,
       "atmfClpNoTaggingScr": atmfClpNoTaggingScr,
       "atmfClpTaggingScr": atmfClpTaggingScr,
       "atmfClpNoTaggingMcr": atmfClpNoTaggingMcr,
       "atmfSrvcRegTypes": atmfSrvcRegTypes,
       "atmForumUni": atmForumUni,
       "atmfPhysicalGroup": atmfPhysicalGroup,
       "atmfPortTable": atmfPortTable,
       "atmfPortEntry": atmfPortEntry,
       "atmfPortIndex": atmfPortIndex,
       "atmfPortAddress": atmfPortAddress,
       "atmfPortTransmissionType": atmfPortTransmissionType,
       "atmfPortMediaType": atmfPortMediaType,
       "atmfPortOperStatus": atmfPortOperStatus,
       "atmfPortSpecific": atmfPortSpecific,
       "atmfPortMyIfName": atmfPortMyIfName,
       "atmfPortMyIfIdentifier": atmfPortMyIfIdentifier,
       "atmfMyIpNmAddress": atmfMyIpNmAddress,
       "atmfMyOsiNmNsapAddress": atmfMyOsiNmNsapAddress,
       "atmfMySystemIdentifier": atmfMySystemIdentifier,
       "atmfAtmLayerGroup": atmfAtmLayerGroup,
       "atmfAtmLayerTable": atmfAtmLayerTable,
       "atmfAtmLayerEntry": atmfAtmLayerEntry,
       "atmfAtmLayerIndex": atmfAtmLayerIndex,
       "atmfAtmLayerMaxVPCs": atmfAtmLayerMaxVPCs,
       "atmfAtmLayerMaxVCCs": atmfAtmLayerMaxVCCs,
       "atmfAtmLayerConfiguredVPCs": atmfAtmLayerConfiguredVPCs,
       "atmfAtmLayerConfiguredVCCs": atmfAtmLayerConfiguredVCCs,
       "atmfAtmLayerMaxVpiBits": atmfAtmLayerMaxVpiBits,
       "atmfAtmLayerMaxVciBits": atmfAtmLayerMaxVciBits,
       "atmfAtmLayerUniType": atmfAtmLayerUniType,
       "atmfAtmLayerUniVersion": atmfAtmLayerUniVersion,
       "atmfAtmLayerDeviceType": atmfAtmLayerDeviceType,
       "atmfAtmLayerIlmiVersion": atmfAtmLayerIlmiVersion,
       "atmfAtmLayerNniSigVersion": atmfAtmLayerNniSigVersion,
       "atmfAtmLayerMaxSvpcVpi": atmfAtmLayerMaxSvpcVpi,
       "atmfAtmLayerMaxSvccVpi": atmfAtmLayerMaxSvccVpi,
       "atmfAtmLayerMinSvccVci": atmfAtmLayerMinSvccVci,
       "atmfAtmStatsGroup": atmfAtmStatsGroup,
       "atmfVpcGroup": atmfVpcGroup,
       "atmfVpcTable": atmfVpcTable,
       "atmfVpcEntry": atmfVpcEntry,
       "atmfVpcPortIndex": atmfVpcPortIndex,
       "atmfVpcVpi": atmfVpcVpi,
       "atmfVpcOperStatus": atmfVpcOperStatus,
       "atmfVpcTransmitTrafficDescriptorType": atmfVpcTransmitTrafficDescriptorType,
       "atmfVpcTransmitTrafficDescriptorParam1": atmfVpcTransmitTrafficDescriptorParam1,
       "atmfVpcTransmitTrafficDescriptorParam2": atmfVpcTransmitTrafficDescriptorParam2,
       "atmfVpcTransmitTrafficDescriptorParam3": atmfVpcTransmitTrafficDescriptorParam3,
       "atmfVpcTransmitTrafficDescriptorParam4": atmfVpcTransmitTrafficDescriptorParam4,
       "atmfVpcTransmitTrafficDescriptorParam5": atmfVpcTransmitTrafficDescriptorParam5,
       "atmfVpcReceiveTrafficDescriptorType": atmfVpcReceiveTrafficDescriptorType,
       "atmfVpcReceiveTrafficDescriptorParam1": atmfVpcReceiveTrafficDescriptorParam1,
       "atmfVpcReceiveTrafficDescriptorParam2": atmfVpcReceiveTrafficDescriptorParam2,
       "atmfVpcReceiveTrafficDescriptorParam3": atmfVpcReceiveTrafficDescriptorParam3,
       "atmfVpcReceiveTrafficDescriptorParam4": atmfVpcReceiveTrafficDescriptorParam4,
       "atmfVpcReceiveTrafficDescriptorParam5": atmfVpcReceiveTrafficDescriptorParam5,
       "atmfVpcQoSCategory": atmfVpcQoSCategory,
       "atmfVpcTransmitQoSClass": atmfVpcTransmitQoSClass,
       "atmfVpcReceiveQoSClass": atmfVpcReceiveQoSClass,
       "atmfVpcBestEffortIndicator": atmfVpcBestEffortIndicator,
       "atmfVpcServiceCategory": atmfVpcServiceCategory,
       "atmfVccGroup": atmfVccGroup,
       "atmfVccTable": atmfVccTable,
       "atmfVccEntry": atmfVccEntry,
       "atmfVccPortIndex": atmfVccPortIndex,
       "atmfVccVpi": atmfVccVpi,
       "atmfVccVci": atmfVccVci,
       "atmfVccOperStatus": atmfVccOperStatus,
       "atmfVccTransmitTrafficDescriptorType": atmfVccTransmitTrafficDescriptorType,
       "atmfVccTransmitTrafficDescriptorParam1": atmfVccTransmitTrafficDescriptorParam1,
       "atmfVccTransmitTrafficDescriptorParam2": atmfVccTransmitTrafficDescriptorParam2,
       "atmfVccTransmitTrafficDescriptorParam3": atmfVccTransmitTrafficDescriptorParam3,
       "atmfVccTransmitTrafficDescriptorParam4": atmfVccTransmitTrafficDescriptorParam4,
       "atmfVccTransmitTrafficDescriptorParam5": atmfVccTransmitTrafficDescriptorParam5,
       "atmfVccReceiveTrafficDescriptorType": atmfVccReceiveTrafficDescriptorType,
       "atmfVccReceiveTrafficDescriptorParam1": atmfVccReceiveTrafficDescriptorParam1,
       "atmfVccReceiveTrafficDescriptorParam2": atmfVccReceiveTrafficDescriptorParam2,
       "atmfVccReceiveTrafficDescriptorParam3": atmfVccReceiveTrafficDescriptorParam3,
       "atmfVccReceiveTrafficDescriptorParam4": atmfVccReceiveTrafficDescriptorParam4,
       "atmfVccReceiveTrafficDescriptorParam5": atmfVccReceiveTrafficDescriptorParam5,
       "atmfVccQoSCategory": atmfVccQoSCategory,
       "atmfVccTransmitQoSClass": atmfVccTransmitQoSClass,
       "atmfVccReceiveQoSClass": atmfVccReceiveQoSClass,
       "atmfVccBestEffortIndicator": atmfVccBestEffortIndicator,
       "atmfVccTransmitFrameDiscard": atmfVccTransmitFrameDiscard,
       "atmfVccReceiveFrameDiscard": atmfVccReceiveFrameDiscard,
       "atmfVccServiceCategory": atmfVccServiceCategory,
       "atmfAddressGroup": atmfAddressGroup,
       "atmfAddressTable": atmfAddressTable,
       "atmfAddressEntry": atmfAddressEntry,
       "atmfAddressPort": atmfAddressPort,
       "atmfAddressAtmAddress": atmfAddressAtmAddress,
       "atmfAddressStatus": atmfAddressStatus,
       "atmfAddressOrgScope": atmfAddressOrgScope,
       "atmfNetPrefixGroup": atmfNetPrefixGroup,
       "atmfNetPrefixTable": atmfNetPrefixTable,
       "atmfNetPrefixEntry": atmfNetPrefixEntry,
       "atmfNetPrefixPort": atmfNetPrefixPort,
       "atmfNetPrefixPrefix": atmfNetPrefixPrefix,
       "atmfNetPrefixStatus": atmfNetPrefixStatus,
       "atmfSrvcRegistryGroup": atmfSrvcRegistryGroup,
       "atmfVpcAbrGroup": atmfVpcAbrGroup,
       "atmfVpcAbrTable": atmfVpcAbrTable,
       "atmfVpcAbrEntry": atmfVpcAbrEntry,
       "atmfVpcAbrPortIndex": atmfVpcAbrPortIndex,
       "atmfVpcAbrVpi": atmfVpcAbrVpi,
       "atmfVpcAbrTransmitIcr": atmfVpcAbrTransmitIcr,
       "atmfVpcAbrTransmitNrm": atmfVpcAbrTransmitNrm,
       "atmfVpcAbrTransmitTrm": atmfVpcAbrTransmitTrm,
       "atmfVpcAbrTransmitCdf": atmfVpcAbrTransmitCdf,
       "atmfVpcAbrTransmitRif": atmfVpcAbrTransmitRif,
       "atmfVpcAbrTransmitRdf": atmfVpcAbrTransmitRdf,
       "atmfVpcAbrTransmitAdtf": atmfVpcAbrTransmitAdtf,
       "atmfVpcAbrTransmitCrm": atmfVpcAbrTransmitCrm,
       "atmfVccAbrGroup": atmfVccAbrGroup,
       "atmfVccAbrTable": atmfVccAbrTable,
       "atmfVccAbrEntry": atmfVccAbrEntry,
       "atmfVccAbrPortIndex": atmfVccAbrPortIndex,
       "atmfVccAbrVpi": atmfVccAbrVpi,
       "atmfVccAbrVci": atmfVccAbrVci,
       "atmfVccAbrTransmitIcr": atmfVccAbrTransmitIcr,
       "atmfVccAbrTransmitNrm": atmfVccAbrTransmitNrm,
       "atmfVccAbrTransmitTrm": atmfVccAbrTransmitTrm,
       "atmfVccAbrTransmitCdf": atmfVccAbrTransmitCdf,
       "atmfVccAbrTransmitRif": atmfVccAbrTransmitRif,
       "atmfVccAbrTransmitRdf": atmfVccAbrTransmitRdf,
       "atmfVccAbrTransmitAdtf": atmfVccAbrTransmitAdtf,
       "atmfVccAbrTransmitCrm": atmfVccAbrTransmitCrm,
       "atmfAddressRegistrationAdminGroup": atmfAddressRegistrationAdminGroup,
       "atmfAddressRegistrationAdminTable": atmfAddressRegistrationAdminTable,
       "atmfAddressRegistrationAdminEntry": atmfAddressRegistrationAdminEntry,
       "atmfAddressRegistrationAdminIndex": atmfAddressRegistrationAdminIndex,
       "atmfAddressRegistrationAdminStatus": atmfAddressRegistrationAdminStatus}
)
