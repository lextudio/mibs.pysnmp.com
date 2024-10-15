# SNMP MIB module (DVB-RCS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/DVB-RCS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:33:55 2024
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

(Dscp,
 DscpOrAny) = mibBuilder.importSymbols(
    "DIFFSERV-DSCP-TC",
    "Dscp",
    "DscpOrAny")

(InetAddress,
 InetAddressPrefixLength,
 InetAddressType,
 InetPortNumber) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressPrefixLength",
    "InetAddressType",
    "InetPortNumber")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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
 iso,
 transmission) = mibBuilder.importSymbols(
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
    "iso",
    "transmission")

(DisplayString,
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")

(Uri,) = mibBuilder.importSymbols(
    "URI-TC-MIB",
    "Uri")


# MODULE-IDENTITY

dvbRcsMib = ModuleIdentity(
    (1, 3, 6, 1, 2, 1, 10, 239)
)
dvbRcsMib.setRevisions(
        ("2009-07-20 12:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class DvbRcsSatLabsProfileMap(Bits, TextualConvention):
    status = "current"


class DvbRcsSatLabsOptionMap(Bits, TextualConvention):
    status = "current"


class DvbRcsSatLabsFeatureMap(Bits, TextualConvention):
    status = "current"


# MIB Managed Objects in the order of their OIDs

_DvbRcsMibObjects_ObjectIdentity = ObjectIdentity
dvbRcsMibObjects = _DvbRcsMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 239, 1)
)
_DvbRcsRcst_ObjectIdentity = ObjectIdentity
dvbRcsRcst = _DvbRcsRcst_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 239, 1, 1)
)
_DvbRcsRcstSystem_ObjectIdentity = ObjectIdentity
dvbRcsRcstSystem = _DvbRcsRcstSystem_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 239, 1, 1, 1)
)
_DvbRcsSystemMibRevision_Type = SnmpAdminString
_DvbRcsSystemMibRevision_Object = MibScalar
dvbRcsSystemMibRevision = _DvbRcsSystemMibRevision_Object(
    (1, 3, 6, 1, 2, 1, 10, 239, 1, 1, 1, 1),
    _DvbRcsSystemMibRevision_Type()
)
dvbRcsSystemMibRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dvbRcsSystemMibRevision.setStatus("current")
_DvbRcsSystemSatLabsProfilesDeclaration_Type = DvbRcsSatLabsProfileMap
_DvbRcsSystemSatLabsProfilesDeclaration_Object = MibScalar
dvbRcsSystemSatLabsProfilesDeclaration = _DvbRcsSystemSatLabsProfilesDeclaration_Object(
    (1, 3, 6, 1, 2, 1, 10, 239, 1, 1, 1, 2),
    _DvbRcsSystemSatLabsProfilesDeclaration_Type()
)
dvbRcsSystemSatLabsProfilesDeclaration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dvbRcsSystemSatLabsProfilesDeclaration.setStatus("current")
_DvbRcsSystemSatLabsOptionsDeclaration_Type = DvbRcsSatLabsOptionMap
_DvbRcsSystemSatLabsOptionsDeclaration_Object = MibScalar
dvbRcsSystemSatLabsOptionsDeclaration = _DvbRcsSystemSatLabsOptionsDeclaration_Object(
    (1, 3, 6, 1, 2, 1, 10, 239, 1, 1, 1, 3),
    _DvbRcsSystemSatLabsOptionsDeclaration_Type()
)
dvbRcsSystemSatLabsOptionsDeclaration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dvbRcsSystemSatLabsOptionsDeclaration.setStatus("current")
_DvbRcsSystemSatLabsFeaturesDeclaration_Type = DvbRcsSatLabsFeatureMap
_DvbRcsSystemSatLabsFeaturesDeclaration_Object = MibScalar
dvbRcsSystemSatLabsFeaturesDeclaration = _DvbRcsSystemSatLabsFeaturesDeclaration_Object(
    (1, 3, 6, 1, 2, 1, 10, 239, 1, 1, 1, 4),
    _DvbRcsSystemSatLabsFeaturesDeclaration_Type()
)
dvbRcsSystemSatLabsFeaturesDeclaration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dvbRcsSystemSatLabsFeaturesDeclaration.setStatus("current")
_DvbRcsSystemLocation_Type = SnmpAdminString
_DvbRcsSystemLocation_Object = MibScalar
dvbRcsSystemLocation = _DvbRcsSystemLocation_Object(
    (1, 3, 6, 1, 2, 1, 10, 239, 1, 1, 1, 5),
    _DvbRcsSystemLocation_Type()
)
dvbRcsSystemLocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dvbRcsSystemLocation.setStatus("current")
_DvbRcsSystemOduAntennaSize_Type = Unsigned32
_DvbRcsSystemOduAntennaSize_Object = MibScalar
dvbRcsSystemOduAntennaSize = _DvbRcsSystemOduAntennaSize_Object(
    (1, 3, 6, 1, 2, 1, 10, 239, 1, 1, 1, 6),
    _DvbRcsSystemOduAntennaSize_Type()
)
dvbRcsSystemOduAntennaSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dvbRcsSystemOduAntennaSize.setStatus("current")
if mibBuilder.loadTexts:
    dvbRcsSystemOduAntennaSize.setUnits("cm")
_DvbRcsSystemOduAntennaGain_Type = Unsigned32
_DvbRcsSystemOduAntennaGain_Object = MibScalar
dvbRcsSystemOduAntennaGain = _DvbRcsSystemOduAntennaGain_Object(
    (1, 3, 6, 1, 2, 1, 10, 239, 1, 1, 1, 7),
    _DvbRcsSystemOduAntennaGain_Type()
)
dvbRcsSystemOduAntennaGain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dvbRcsSystemOduAntennaGain.setStatus("current")
if mibBuilder.loadTexts:
    dvbRcsSystemOduAntennaGain.setUnits("x0.1 dBi")
_DvbRcsSystemOduSspa_Type = Unsigned32
_DvbRcsSystemOduSspa_Object = MibScalar
dvbRcsSystemOduSspa = _DvbRcsSystemOduSspa_Object(
    (1, 3, 6, 1, 2, 1, 10, 239, 1, 1, 1, 8),
    _DvbRcsSystemOduSspa_Type()
)
dvbRcsSystemOduSspa.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dvbRcsSystemOduSspa.setStatus("current")
if mibBuilder.loadTexts:
    dvbRcsSystemOduSspa.setUnits("x0.1 W")
_DvbRcsSystemOduTxType_Type = SnmpAdminString
_DvbRcsSystemOduTxType_Object = MibScalar
dvbRcsSystemOduTxType = _DvbRcsSystemOduTxType_Object(
    (1, 3, 6, 1, 2, 1, 10, 239, 1, 1, 1, 9),
    _DvbRcsSystemOduTxType_Type()
)
dvbRcsSystemOduTxType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dvbRcsSystemOduTxType.setStatus("current")
_DvbRcsSystemOduRxType_Type = SnmpAdminString
_DvbRcsSystemOduRxType_Object = MibScalar
dvbRcsSystemOduRxType = _DvbRcsSystemOduRxType_Object(
    (1, 3, 6, 1, 2, 1, 10, 239, 1, 1, 1, 10),
    _DvbRcsSystemOduRxType_Type()
)
dvbRcsSystemOduRxType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dvbRcsSystemOduRxType.setStatus("current")


class _DvbRcsSystemOduRxBand_Type(Integer32):
    """Custom type dvbRcsSystemOduRxBand based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("oduHighRxBand", 0),
          ("oduLowRxBand", 1))
    )


_DvbRcsSystemOduRxBand_Type.__name__ = "Integer32"
_DvbRcsSystemOduRxBand_Object = MibScalar
dvbRcsSystemOduRxBand = _DvbRcsSystemOduRxBand_Object(
    (1, 3, 6, 1, 2, 1, 10, 239, 1, 1, 1, 11),
    _DvbRcsSystemOduRxBand_Type()
)
dvbRcsSystemOduRxBand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dvbRcsSystemOduRxBand.setStatus("current")
_DvbRcsSystemOduRxLO_Type = Unsigned32
_DvbRcsSystemOduRxLO_Object = MibScalar
dvbRcsSystemOduRxLO = _DvbRcsSystemOduRxLO_Object(
    (1, 3, 6, 1, 2, 1, 10, 239, 1, 1, 1, 12),
    _DvbRcsSystemOduRxLO_Type()
)
dvbRcsSystemOduRxLO.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dvbRcsSystemOduRxLO.setStatus("current")
if mibBuilder.loadTexts:
    dvbRcsSystemOduRxLO.setUnits("x100 Hz")
_DvbRcsSystemOduTxLO_Type = Unsigned32
_DvbRcsSystemOduTxLO_Object = MibScalar
dvbRcsSystemOduTxLO = _DvbRcsSystemOduTxLO_Object(
    (1, 3, 6, 1, 2, 1, 10, 239, 1, 1, 1, 13),
    _DvbRcsSystemOduTxLO_Type()
)
dvbRcsSystemOduTxLO.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dvbRcsSystemOduTxLO.setStatus("current")
if mibBuilder.loadTexts:
    dvbRcsSystemOduTxLO.setUnits("x100 Hz")
_DvbRcsSystemIduPep_ObjectIdentity = ObjectIdentity
dvbRcsSystemIduPep = _DvbRcsSystemIduPep_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 239, 1, 1, 1, 14)
)


class _DvbRcsTcpPep_Type(Integer32):
    """Custom type dvbRcsTcpPep based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_DvbRcsTcpPep_Type.__name__ = "Integer32"
_DvbRcsTcpPep_Object = MibScalar
dvbRcsTcpPep = _DvbRcsTcpPep_Object(
    (1, 3, 6, 1, 2, 1, 10, 239, 1, 1, 1, 14, 1),
    _DvbRcsTcpPep_Type()
)
dvbRcsTcpPep.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dvbRcsTcpPep.setStatus("current")


class _DvbRcsHttpPep_Type(Integer32):
    """Custom type dvbRcsHttpPep based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_DvbRcsHttpPep_Type.__name__ = "Integer32"
_DvbRcsHttpPep_Object = MibScalar
dvbRcsHttpPep = _DvbRcsHttpPep_Object(
    (1, 3, 6, 1, 2, 1, 10, 239, 1, 1, 1, 14, 2),
    _DvbRcsHttpPep_Type()
)
dvbRcsHttpPep.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dvbRcsHttpPep.setStatus("current")
_DvbRcsOduTx_ObjectIdentity = ObjectIdentity
dvbRcsOduTx = _DvbRcsOduTx_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 239, 1, 1, 1, 15)
)
_DvbRcsOduTxTypeTable_Object = MibTable
dvbRcsOduTxTypeTable = _DvbRcsOduTxTypeTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 239, 1, 1, 1, 15, 1)
)
if mibBuilder.loadTexts:
    dvbRcsOduTxTypeTable.setStatus("current")
_DvbRcsOduTxTypeEntry_Object = MibTableRow
dvbRcsOduTxTypeEntry = _DvbRcsOduTxTypeEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 239, 1, 1, 1, 15, 1, 1)
)
dvbRcsOduTxTypeEntry.setIndexNames(
    (0, "DVB-RCS-MIB", "dvbRcsOduTxTypeIndex"),
)
if mibBuilder.loadTexts:
    dvbRcsOduTxTypeEntry.setStatus("current")


class _DvbRcsOduTxTypeIndex_Type(Unsigned32):
    """Custom type dvbRcsOduTxTypeIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_DvbRcsOduTxTypeIndex_Type.__name__ = "Unsigned32"
_DvbRcsOduTxTypeIndex_Object = MibTableColumn
dvbRcsOduTxTypeIndex = _DvbRcsOduTxTypeIndex_Object(
    (1, 3, 6, 1, 2, 1, 10, 239, 1, 1, 1, 15, 1, 1, 1),
    _DvbRcsOduTxTypeIndex_Type()
)
dvbRcsOduTxTypeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dvbRcsOduTxTypeIndex.setStatus("current")
_DvbRcsOduTxTypeDescription_Type = SnmpAdminString
_DvbRcsOduTxTypeDescription_Object = MibTableColumn
dvbRcsOduTxTypeDescription = _DvbRcsOduTxTypeDescription_Object(
    (1, 3, 6, 1, 2, 1, 10, 239, 1, 1, 1, 15, 1, 1, 2),
    _DvbRcsOduTxTypeDescription_Type()
)
dvbRcsOduTxTypeDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dvbRcsOduTxTypeDescription.setStatus("current")
_DvbRcsOduTxType_Type = Unsigned32
_DvbRcsOduTxType_Object = MibScalar
dvbRcsOduTxType = _DvbRcsOduTxType_Object(
    (1, 3, 6, 1, 2, 1, 10, 239, 1, 1, 1, 15, 2),
    _DvbRcsOduTxType_Type()
)
dvbRcsOduTxType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dvbRcsOduTxType.setStatus("current")
_DvbRcsOduRx_ObjectIdentity = ObjectIdentity
dvbRcsOduRx = _DvbRcsOduRx_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 239, 1, 1, 1, 16)
)
_DvbRcsOduRxTypeTable_Object = MibTable
dvbRcsOduRxTypeTable = _DvbRcsOduRxTypeTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 239, 1, 1, 1, 16, 1)
)
if mibBuilder.loadTexts:
    dvbRcsOduRxTypeTable.setStatus("current")
_DvbRcsOduRxTypeEntry_Object = MibTableRow
dvbRcsOduRxTypeEntry = _DvbRcsOduRxTypeEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 239, 1, 1, 1, 16, 1, 1)
)
dvbRcsOduRxTypeEntry.setIndexNames(
    (0, "DVB-RCS-MIB", "dvbRcsOduRxTypeIndex"),
)
if mibBuilder.loadTexts:
    dvbRcsOduRxTypeEntry.setStatus("current")


class _DvbRcsOduRxTypeIndex_Type(Unsigned32):
    """Custom type dvbRcsOduRxTypeIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_DvbRcsOduRxTypeIndex_Type.__name__ = "Unsigned32"
_DvbRcsOduRxTypeIndex_Object = MibTableColumn
dvbRcsOduRxTypeIndex = _DvbRcsOduRxTypeIndex_Object(
    (1, 3, 6, 1, 2, 1, 10, 239, 1, 1, 1, 16, 1, 1, 1),
    _DvbRcsOduRxTypeIndex_Type()
)
dvbRcsOduRxTypeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dvbRcsOduRxTypeIndex.setStatus("current")
_DvbRcsOduRxTypeDescription_Type = SnmpAdminString
_DvbRcsOduRxTypeDescription_Object = MibTableColumn
dvbRcsOduRxTypeDescription = _DvbRcsOduRxTypeDescription_Object(
    (1, 3, 6, 1, 2, 1, 10, 239, 1, 1, 1, 16, 1, 1, 2),
    _DvbRcsOduRxTypeDescription_Type()
)
dvbRcsOduRxTypeDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dvbRcsOduRxTypeDescription.setStatus("current")
_DvbRcsOduRxType_Type = Unsigned32
_DvbRcsOduRxType_Object = MibScalar
dvbRcsOduRxType = _DvbRcsOduRxType_Object(
    (1, 3, 6, 1, 2, 1, 10, 239, 1, 1, 1, 16, 2),
    _DvbRcsOduRxType_Type()
)
dvbRcsOduRxType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dvbRcsOduRxType.setStatus("current")
_DvbRcsOduAntenna_ObjectIdentity = ObjectIdentity
dvbRcsOduAntenna = _DvbRcsOduAntenna_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 239, 1, 1, 1, 17)
)
_DvbRcsOduAntennaTypeTable_Object = MibTable
dvbRcsOduAntennaTypeTable = _DvbRcsOduAntennaTypeTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 239, 1, 1, 1, 17, 1)
)
if mibBuilder.loadTexts:
    dvbRcsOduAntennaTypeTable.setStatus("current")
_DvbRcsOduAntennaTypeEntry_Object = MibTableRow
dvbRcsOduAntennaTypeEntry = _DvbRcsOduAntennaTypeEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 239, 1, 1, 1, 17, 1, 1)
)
dvbRcsOduAntennaTypeEntry.setIndexNames(
    (0, "DVB-RCS-MIB", "dvbRcsOduAntennaTypeIndex"),
)
if mibBuilder.loadTexts:
    dvbRcsOduAntennaTypeEntry.setStatus("current")


class _DvbRcsOduAntennaTypeIndex_Type(Unsigned32):
    """Custom type dvbRcsOduAntennaTypeIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_DvbRcsOduAntennaTypeIndex_Type.__name__ = "Unsigned32"
_DvbRcsOduAntennaTypeIndex_Object = MibTableColumn
dvbRcsOduAntennaTypeIndex = _DvbRcsOduAntennaTypeIndex_Object(
    (1, 3, 6, 1, 2, 1, 10, 239, 1, 1, 1, 17, 1, 1, 1),
    _DvbRcsOduAntennaTypeIndex_Type()
)
dvbRcsOduAntennaTypeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dvbRcsOduAntennaTypeIndex.setStatus("current")
_DvbRcsOduAntennaTypeDescription_Type = SnmpAdminString
_DvbRcsOduAntennaTypeDescription_Object = MibTableColumn
dvbRcsOduAntennaTypeDescription = _DvbRcsOduAntennaTypeDescription_Object(
    (1, 3, 6, 1, 2, 1, 10, 239, 1, 1, 1, 17, 1, 1, 2),
    _DvbRcsOduAntennaTypeDescription_Type()
)
dvbRcsOduAntennaTypeDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dvbRcsOduAntennaTypeDescription.setStatus("current")
_DvbRcsOduAntennaType_Type = Unsigned32
_DvbRcsOduAntennaType_Object = MibScalar
dvbRcsOduAntennaType = _DvbRcsOduAntennaType_Object(
    (1, 3, 6, 1, 2, 1, 10, 239, 1, 1, 1, 17, 2),
    _DvbRcsOduAntennaType_Type()
)
dvbRcsOduAntennaType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dvbRcsOduAntennaType.setStatus("current")
_DvbRcsRcstNetwork_ObjectIdentity = ObjectIdentity
dvbRcsRcstNetwork = _DvbRcsRcstNetwork_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 239, 1, 1, 2)
)
_DvbRcsNetworkOamInetAddressType_Type = InetAddressType
_DvbRcsNetworkOamInetAddressType_Object = MibScalar
dvbRcsNetworkOamInetAddressType = _DvbRcsNetworkOamInetAddressType_Object(
    (1, 3, 6, 1, 2, 1, 10, 239, 1, 1, 2, 1),
    _DvbRcsNetworkOamInetAddressType_Type()
)
dvbRcsNetworkOamInetAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dvbRcsNetworkOamInetAddressType.setStatus("current")
_DvbRcsNetworkOamInetAddress_Type = InetAddress
_DvbRcsNetworkOamInetAddress_Object = MibScalar
dvbRcsNetworkOamInetAddress = _DvbRcsNetworkOamInetAddress_Object(
    (1, 3, 6, 1, 2, 1, 10, 239, 1, 1, 2, 2),
    _DvbRcsNetworkOamInetAddress_Type()
)
dvbRcsNetworkOamInetAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dvbRcsNetworkOamInetAddress.setStatus("current")
_DvbRcsNetworkOamInetAddressPrefixLength_Type = InetAddressPrefixLength
_DvbRcsNetworkOamInetAddressPrefixLength_Object = MibScalar
dvbRcsNetworkOamInetAddressPrefixLength = _DvbRcsNetworkOamInetAddressPrefixLength_Object(
    (1, 3, 6, 1, 2, 1, 10, 239, 1, 1, 2, 3),
    _DvbRcsNetworkOamInetAddressPrefixLength_Type()
)
dvbRcsNetworkOamInetAddressPrefixLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dvbRcsNetworkOamInetAddressPrefixLength.setStatus("current")


class _DvbRcsNetworkOamInetAddressAssign_Type(Integer32):
    """Custom type dvbRcsNetworkOamInetAddressAssign based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("oamInetAddressDynamic", 2),
          ("oamInetAddressStatic", 1))
    )


_DvbRcsNetworkOamInetAddressAssign_Type.__name__ = "Integer32"
_DvbRcsNetworkOamInetAddressAssign_Object = MibScalar
dvbRcsNetworkOamInetAddressAssign = _DvbRcsNetworkOamInetAddressAssign_Object(
    (1, 3, 6, 1, 2, 1, 10, 239, 1, 1, 2, 4),
    _DvbRcsNetworkOamInetAddressAssign_Type()
)
dvbRcsNetworkOamInetAddressAssign.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dvbRcsNetworkOamInetAddressAssign.setStatus("current")
_DvbRcsNetworkLanInetAddressType_Type = InetAddressType
_DvbRcsNetworkLanInetAddressType_Object = MibScalar
dvbRcsNetworkLanInetAddressType = _DvbRcsNetworkLanInetAddressType_Object(
    (1, 3, 6, 1, 2, 1, 10, 239, 1, 1, 2, 5),
    _DvbRcsNetworkLanInetAddressType_Type()
)
dvbRcsNetworkLanInetAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dvbRcsNetworkLanInetAddressType.setStatus("current")
_DvbRcsNetworkLanInetAddress_Type = InetAddress
_DvbRcsNetworkLanInetAddress_Object = MibScalar
dvbRcsNetworkLanInetAddress = _DvbRcsNetworkLanInetAddress_Object(
    (1, 3, 6, 1, 2, 1, 10, 239, 1, 1, 2, 6),
    _DvbRcsNetworkLanInetAddress_Type()
)
dvbRcsNetworkLanInetAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dvbRcsNetworkLanInetAddress.setStatus("current")
_DvbRcsNetworkLanInetAddressPrefixLength_Type = InetAddressPrefixLength
_DvbRcsNetworkLanInetAddressPrefixLength_Object = MibScalar
dvbRcsNetworkLanInetAddressPrefixLength = _DvbRcsNetworkLanInetAddressPrefixLength_Object(
    (1, 3, 6, 1, 2, 1, 10, 239, 1, 1, 2, 7),
    _DvbRcsNetworkLanInetAddressPrefixLength_Type()
)
dvbRcsNetworkLanInetAddressPrefixLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dvbRcsNetworkLanInetAddressPrefixLength.setStatus("current")
_DvbRcsNetworkAirInterfaceDefaultGatewayInetAddressType_Type = InetAddressType
_DvbRcsNetworkAirInterfaceDefaultGatewayInetAddressType_Object = MibScalar
dvbRcsNetworkAirInterfaceDefaultGatewayInetAddressType = _DvbRcsNetworkAirInterfaceDefaultGatewayInetAddressType_Object(
    (1, 3, 6, 1, 2, 1, 10, 239, 1, 1, 2, 8),
    _DvbRcsNetworkAirInterfaceDefaultGatewayInetAddressType_Type()
)
dvbRcsNetworkAirInterfaceDefaultGatewayInetAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dvbRcsNetworkAirInterfaceDefaultGatewayInetAddressType.setStatus("current")
_DvbRcsNetworkAirInterfaceDefaultGatewayInetAddress_Type = InetAddress
_DvbRcsNetworkAirInterfaceDefaultGatewayInetAddress_Object = MibScalar
dvbRcsNetworkAirInterfaceDefaultGatewayInetAddress = _DvbRcsNetworkAirInterfaceDefaultGatewayInetAddress_Object(
    (1, 3, 6, 1, 2, 1, 10, 239, 1, 1, 2, 9),
    _DvbRcsNetworkAirInterfaceDefaultGatewayInetAddress_Type()
)
dvbRcsNetworkAirInterfaceDefaultGatewayInetAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dvbRcsNetworkAirInterfaceDefaultGatewayInetAddress.setStatus("current")
_DvbRcsNetworkAirInterfaceDefaultGatewayInetAddressPrefixLength_Type = InetAddressPrefixLength
_DvbRcsNetworkAirInterfaceDefaultGatewayInetAddressPrefixLength_Object = MibScalar
dvbRcsNetworkAirInterfaceDefaultGatewayInetAddressPrefixLength = _DvbRcsNetworkAirInterfaceDefaultGatewayInetAddressPrefixLength_Object(
    (1, 3, 6, 1, 2, 1, 10, 239, 1, 1, 2, 10),
    _DvbRcsNetworkAirInterfaceDefaultGatewayInetAddressPrefixLength_Type()
)
dvbRcsNetworkAirInterfaceDefaultGatewayInetAddressPrefixLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dvbRcsNetworkAirInterfaceDefaultGatewayInetAddressPrefixLength.setStatus("current")
_DvbRcsNetworkDnsServers_ObjectIdentity = ObjectIdentity
dvbRcsNetworkDnsServers = _DvbRcsNetworkDnsServers_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 239, 1, 1, 2, 11)
)
_DvbRcsPrimaryDnsServerInetAddressType_Type = InetAddressType
_DvbRcsPrimaryDnsServerInetAddressType_Object = MibScalar
dvbRcsPrimaryDnsServerInetAddressType = _DvbRcsPrimaryDnsServerInetAddressType_Object(
    (1, 3, 6, 1, 2, 1, 10, 239, 1, 1, 2, 11, 1),
    _DvbRcsPrimaryDnsServerInetAddressType_Type()
)
dvbRcsPrimaryDnsServerInetAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dvbRcsPrimaryDnsServerInetAddressType.setStatus("current")
_DvbRcsPrimaryDnsServerInetAddress_Type = InetAddress
_DvbRcsPrimaryDnsServerInetAddress_Object = MibScalar
dvbRcsPrimaryDnsServerInetAddress = _DvbRcsPrimaryDnsServerInetAddress_Object(
    (1, 3, 6, 1, 2, 1, 10, 239, 1, 1, 2, 11, 2),
    _DvbRcsPrimaryDnsServerInetAddress_Type()
)
dvbRcsPrimaryDnsServerInetAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dvbRcsPrimaryDnsServerInetAddress.setStatus("current")
_DvbRcsPrimaryDnsServerInetAddressPrefixLength_Type = InetAddressPrefixLength
_DvbRcsPrimaryDnsServerInetAddressPrefixLength_Object = MibScalar
dvbRcsPrimaryDnsServerInetAddressPrefixLength = _DvbRcsPrimaryDnsServerInetAddressPrefixLength_Object(
    (1, 3, 6, 1, 2, 1, 10, 239, 1, 1, 2, 11, 3),
    _DvbRcsPrimaryDnsServerInetAddressPrefixLength_Type()
)
dvbRcsPrimaryDnsServerInetAddressPrefixLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dvbRcsPrimaryDnsServerInetAddressPrefixLength.setStatus("current")
_DvbRcsSecondaryDnsServerInetAddressType_Type = InetAddressType
_DvbRcsSecondaryDnsServerInetAddressType_Object = MibScalar
dvbRcsSecondaryDnsServerInetAddressType = _DvbRcsSecondaryDnsServerInetAddressType_Object(
    (1, 3, 6, 1, 2, 1, 10, 239, 1, 1, 2, 11, 4),
    _DvbRcsSecondaryDnsServerInetAddressType_Type()
)
dvbRcsSecondaryDnsServerInetAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dvbRcsSecondaryDnsServerInetAddressType.setStatus("current")
_DvbRcsSecondaryDnsServerInetAddress_Type = InetAddress
_DvbRcsSecondaryDnsServerInetAddress_Object = MibScalar
dvbRcsSecondaryDnsServerInetAddress = _DvbRcsSecondaryDnsServerInetAddress_Object(
    (1, 3, 6, 1, 2, 1, 10, 239, 1, 1, 2, 11, 5),
    _DvbRcsSecondaryDnsServerInetAddress_Type()
)
dvbRcsSecondaryDnsServerInetAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dvbRcsSecondaryDnsServerInetAddress.setStatus("current")
_DvbRcsSecondaryDnsServerInetAddressPrefixLength_Type = InetAddressPrefixLength
_DvbRcsSecondaryDnsServerInetAddressPrefixLength_Object = MibScalar
dvbRcsSecondaryDnsServerInetAddressPrefixLength = _DvbRcsSecondaryDnsServerInetAddressPrefixLength_Object(
    (1, 3, 6, 1, 2, 1, 10, 239, 1, 1, 2, 11, 6),
    _DvbRcsSecondaryDnsServerInetAddressPrefixLength_Type()
)
dvbRcsSecondaryDnsServerInetAddressPrefixLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dvbRcsSecondaryDnsServerInetAddressPrefixLength.setStatus("current")
_DvbRcsNetworkNccMgtInetAddressType_Type = InetAddressType
_DvbRcsNetworkNccMgtInetAddressType_Object = MibScalar
dvbRcsNetworkNccMgtInetAddressType = _DvbRcsNetworkNccMgtInetAddressType_Object(
    (1, 3, 6, 1, 2, 1, 10, 239, 1, 1, 2, 12),
    _DvbRcsNetworkNccMgtInetAddressType_Type()
)
dvbRcsNetworkNccMgtInetAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dvbRcsNetworkNccMgtInetAddressType.setStatus("current")
_DvbRcsNetworkNccMgtInetAddress_Type = InetAddress
_DvbRcsNetworkNccMgtInetAddress_Object = MibScalar
dvbRcsNetworkNccMgtInetAddress = _DvbRcsNetworkNccMgtInetAddress_Object(
    (1, 3, 6, 1, 2, 1, 10, 239, 1, 1, 2, 13),
    _DvbRcsNetworkNccMgtInetAddress_Type()
)
dvbRcsNetworkNccMgtInetAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dvbRcsNetworkNccMgtInetAddress.setStatus("current")
_DvbRcsNetworkNccMgtInetAddressPrefixLength_Type = InetAddressPrefixLength
_DvbRcsNetworkNccMgtInetAddressPrefixLength_Object = MibScalar
dvbRcsNetworkNccMgtInetAddressPrefixLength = _DvbRcsNetworkNccMgtInetAddressPrefixLength_Object(
    (1, 3, 6, 1, 2, 1, 10, 239, 1, 1, 2, 14),
    _DvbRcsNetworkNccMgtInetAddressPrefixLength_Type()
)
dvbRcsNetworkNccMgtInetAddressPrefixLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dvbRcsNetworkNccMgtInetAddressPrefixLength.setStatus("current")


class _DvbRcsNetworkConfigFileDownloadUrl_Type(Uri):
    """Custom type dvbRcsNetworkConfigFileDownloadUrl based on Uri"""
    subtypeSpec = Uri.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65535),
    )


_DvbRcsNetworkConfigFileDownloadUrl_Type.__name__ = "Uri"
_DvbRcsNetworkConfigFileDownloadUrl_Object = MibScalar
dvbRcsNetworkConfigFileDownloadUrl = _DvbRcsNetworkConfigFileDownloadUrl_Object(
    (1, 3, 6, 1, 2, 1, 10, 239, 1, 1, 2, 15),
    _DvbRcsNetworkConfigFileDownloadUrl_Type()
)
dvbRcsNetworkConfigFileDownloadUrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dvbRcsNetworkConfigFileDownloadUrl.setStatus("current")


class _DvbRcsNetworkInstallLogFileDownloadUrl_Type(Uri):
    """Custom type dvbRcsNetworkInstallLogFileDownloadUrl based on Uri"""
    subtypeSpec = Uri.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65535),
    )


_DvbRcsNetworkInstallLogFileDownloadUrl_Type.__name__ = "Uri"
_DvbRcsNetworkInstallLogFileDownloadUrl_Object = MibScalar
dvbRcsNetworkInstallLogFileDownloadUrl = _DvbRcsNetworkInstallLogFileDownloadUrl_Object(
    (1, 3, 6, 1, 2, 1, 10, 239, 1, 1, 2, 16),
    _DvbRcsNetworkInstallLogFileDownloadUrl_Type()
)
dvbRcsNetworkInstallLogFileDownloadUrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dvbRcsNetworkInstallLogFileDownloadUrl.setStatus("current")


class _DvbRcsNetworkConfigFileUploadUrl_Type(Uri):
    """Custom type dvbRcsNetworkConfigFileUploadUrl based on Uri"""
    subtypeSpec = Uri.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65535),
    )


_DvbRcsNetworkConfigFileUploadUrl_Type.__name__ = "Uri"
_DvbRcsNetworkConfigFileUploadUrl_Object = MibScalar
dvbRcsNetworkConfigFileUploadUrl = _DvbRcsNetworkConfigFileUploadUrl_Object(
    (1, 3, 6, 1, 2, 1, 10, 239, 1, 1, 2, 17),
    _DvbRcsNetworkConfigFileUploadUrl_Type()
)
dvbRcsNetworkConfigFileUploadUrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dvbRcsNetworkConfigFileUploadUrl.setStatus("current")


class _DvbRcsNetworkLogFileUploadUrl_Type(Uri):
    """Custom type dvbRcsNetworkLogFileUploadUrl based on Uri"""
    subtypeSpec = Uri.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65535),
    )


_DvbRcsNetworkLogFileUploadUrl_Type.__name__ = "Uri"
_DvbRcsNetworkLogFileUploadUrl_Object = MibScalar
dvbRcsNetworkLogFileUploadUrl = _DvbRcsNetworkLogFileUploadUrl_Object(
    (1, 3, 6, 1, 2, 1, 10, 239, 1, 1, 2, 18),
    _DvbRcsNetworkLogFileUploadUrl_Type()
)
dvbRcsNetworkLogFileUploadUrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dvbRcsNetworkLogFileUploadUrl.setStatus("current")


class _DvbRcsNetworkInstallLogFileUploadUrl_Type(Uri):
    """Custom type dvbRcsNetworkInstallLogFileUploadUrl based on Uri"""
    subtypeSpec = Uri.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65535),
    )


_DvbRcsNetworkInstallLogFileUploadUrl_Type.__name__ = "Uri"
_DvbRcsNetworkInstallLogFileUploadUrl_Object = MibScalar
dvbRcsNetworkInstallLogFileUploadUrl = _DvbRcsNetworkInstallLogFileUploadUrl_Object(
    (1, 3, 6, 1, 2, 1, 10, 239, 1, 1, 2, 19),
    _DvbRcsNetworkInstallLogFileUploadUrl_Type()
)
dvbRcsNetworkInstallLogFileUploadUrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dvbRcsNetworkInstallLogFileUploadUrl.setStatus("current")
_DvbRcsRcstInstall_ObjectIdentity = ObjectIdentity
dvbRcsRcstInstall = _DvbRcsRcstInstall_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 239, 1, 1, 3)
)


class _DvbRcsInstallAntennaAlignmentState_Type(Integer32):
    """Custom type dvbRcsInstallAntennaAlignmentState based on Integer32"""
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
        *(("antennaAlignmentContinue", 3),
          ("antennaAlignmentDeny", 2),
          ("antennaAlignmentFail", 6),
          ("antennaAlignmentStart", 1),
          ("antennaAlignmentStop", 4),
          ("antennaAlignmentSuccess", 5))
    )


_DvbRcsInstallAntennaAlignmentState_Type.__name__ = "Integer32"
_DvbRcsInstallAntennaAlignmentState_Object = MibScalar
dvbRcsInstallAntennaAlignmentState = _DvbRcsInstallAntennaAlignmentState_Object(
    (1, 3, 6, 1, 2, 1, 10, 239, 1, 1, 3, 1),
    _DvbRcsInstallAntennaAlignmentState_Type()
)
dvbRcsInstallAntennaAlignmentState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dvbRcsInstallAntennaAlignmentState.setStatus("current")
_DvbRcsInstallCwFrequency_Type = Unsigned32
_DvbRcsInstallCwFrequency_Object = MibScalar
dvbRcsInstallCwFrequency = _DvbRcsInstallCwFrequency_Object(
    (1, 3, 6, 1, 2, 1, 10, 239, 1, 1, 3, 2),
    _DvbRcsInstallCwFrequency_Type()
)
dvbRcsInstallCwFrequency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dvbRcsInstallCwFrequency.setStatus("current")
if mibBuilder.loadTexts:
    dvbRcsInstallCwFrequency.setUnits("x100 Hz")
_DvbRcsInstallCwMaxDuration_Type = Unsigned32
_DvbRcsInstallCwMaxDuration_Object = MibScalar
dvbRcsInstallCwMaxDuration = _DvbRcsInstallCwMaxDuration_Object(
    (1, 3, 6, 1, 2, 1, 10, 239, 1, 1, 3, 3),
    _DvbRcsInstallCwMaxDuration_Type()
)
dvbRcsInstallCwMaxDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dvbRcsInstallCwMaxDuration.setStatus("current")
if mibBuilder.loadTexts:
    dvbRcsInstallCwMaxDuration.setUnits("seconds")
_DvbRcsInstallCwPower_Type = Integer32
_DvbRcsInstallCwPower_Object = MibScalar
dvbRcsInstallCwPower = _DvbRcsInstallCwPower_Object(
    (1, 3, 6, 1, 2, 1, 10, 239, 1, 1, 3, 4),
    _DvbRcsInstallCwPower_Type()
)
dvbRcsInstallCwPower.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dvbRcsInstallCwPower.setStatus("current")
if mibBuilder.loadTexts:
    dvbRcsInstallCwPower.setUnits("x0.1 dBm")
_DvbRcsInstallCoPolReading_Type = Unsigned32
_DvbRcsInstallCoPolReading_Object = MibScalar
dvbRcsInstallCoPolReading = _DvbRcsInstallCoPolReading_Object(
    (1, 3, 6, 1, 2, 1, 10, 239, 1, 1, 3, 5),
    _DvbRcsInstallCoPolReading_Type()
)
dvbRcsInstallCoPolReading.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dvbRcsInstallCoPolReading.setStatus("current")
if mibBuilder.loadTexts:
    dvbRcsInstallCoPolReading.setUnits("x0.1 dB")
_DvbRcsInstallXPolReading_Type = Unsigned32
_DvbRcsInstallXPolReading_Object = MibScalar
dvbRcsInstallXPolReading = _DvbRcsInstallXPolReading_Object(
    (1, 3, 6, 1, 2, 1, 10, 239, 1, 1, 3, 6),
    _DvbRcsInstallXPolReading_Type()
)
dvbRcsInstallXPolReading.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dvbRcsInstallXPolReading.setStatus("current")
if mibBuilder.loadTexts:
    dvbRcsInstallXPolReading.setUnits("x0.1 dB")
_DvbRcsInstallCoPolTarget_Type = Unsigned32
_DvbRcsInstallCoPolTarget_Object = MibScalar
dvbRcsInstallCoPolTarget = _DvbRcsInstallCoPolTarget_Object(
    (1, 3, 6, 1, 2, 1, 10, 239, 1, 1, 3, 7),
    _DvbRcsInstallCoPolTarget_Type()
)
dvbRcsInstallCoPolTarget.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dvbRcsInstallCoPolTarget.setStatus("current")
if mibBuilder.loadTexts:
    dvbRcsInstallCoPolTarget.setUnits("x0.1 dB")
_DvbRcsInstallXPolTarget_Type = Unsigned32
_DvbRcsInstallXPolTarget_Object = MibScalar
dvbRcsInstallXPolTarget = _DvbRcsInstallXPolTarget_Object(
    (1, 3, 6, 1, 2, 1, 10, 239, 1, 1, 3, 8),
    _DvbRcsInstallXPolTarget_Type()
)
dvbRcsInstallXPolTarget.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dvbRcsInstallXPolTarget.setStatus("current")
if mibBuilder.loadTexts:
    dvbRcsInstallXPolTarget.setUnits("x0.1 dB")
_DvbRcsInstallStandByDuration_Type = Unsigned32
_DvbRcsInstallStandByDuration_Object = MibScalar
dvbRcsInstallStandByDuration = _DvbRcsInstallStandByDuration_Object(
    (1, 3, 6, 1, 2, 1, 10, 239, 1, 1, 3, 9),
    _DvbRcsInstallStandByDuration_Type()
)
dvbRcsInstallStandByDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dvbRcsInstallStandByDuration.setStatus("current")
if mibBuilder.loadTexts:
    dvbRcsInstallStandByDuration.setUnits("seconds")


class _DvbRcsInstallTargetEsN0_Type(Unsigned32):
    """Custom type dvbRcsInstallTargetEsN0 based on Unsigned32"""
    defaultValue = 70

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 315),
    )


_DvbRcsInstallTargetEsN0_Type.__name__ = "Unsigned32"
_DvbRcsInstallTargetEsN0_Object = MibScalar
dvbRcsInstallTargetEsN0 = _DvbRcsInstallTargetEsN0_Object(
    (1, 3, 6, 1, 2, 1, 10, 239, 1, 1, 3, 10),
    _DvbRcsInstallTargetEsN0_Type()
)
dvbRcsInstallTargetEsN0.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dvbRcsInstallTargetEsN0.setStatus("current")
if mibBuilder.loadTexts:
    dvbRcsInstallTargetEsN0.setUnits("x0.1 dB")
_DvbRcsRcstQos_ObjectIdentity = ObjectIdentity
dvbRcsRcstQos = _DvbRcsRcstQos_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 239, 1, 1, 4)
)
_DvbRcsPktClassTable_Object = MibTable
dvbRcsPktClassTable = _DvbRcsPktClassTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 239, 1, 1, 4, 1)
)
if mibBuilder.loadTexts:
    dvbRcsPktClassTable.setStatus("current")
_DvbRcsPktClassEntry_Object = MibTableRow
dvbRcsPktClassEntry = _DvbRcsPktClassEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 239, 1, 1, 4, 1, 1)
)
dvbRcsPktClassEntry.setIndexNames(
    (0, "DVB-RCS-MIB", "dvbRcsPktClassIndex"),
)
if mibBuilder.loadTexts:
    dvbRcsPktClassEntry.setStatus("current")


class _DvbRcsPktClassIndex_Type(Unsigned32):
    """Custom type dvbRcsPktClassIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_DvbRcsPktClassIndex_Type.__name__ = "Unsigned32"
_DvbRcsPktClassIndex_Object = MibTableColumn
dvbRcsPktClassIndex = _DvbRcsPktClassIndex_Object(
    (1, 3, 6, 1, 2, 1, 10, 239, 1, 1, 4, 1, 1, 1),
    _DvbRcsPktClassIndex_Type()
)
dvbRcsPktClassIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dvbRcsPktClassIndex.setStatus("current")


class _DvbRcsPktClassDscpLow_Type(Dscp):
    """Custom type dvbRcsPktClassDscpLow based on Dscp"""
    defaultValue = 0


_DvbRcsPktClassDscpLow_Object = MibTableColumn
dvbRcsPktClassDscpLow = _DvbRcsPktClassDscpLow_Object(
    (1, 3, 6, 1, 2, 1, 10, 239, 1, 1, 4, 1, 1, 2),
    _DvbRcsPktClassDscpLow_Type()
)
dvbRcsPktClassDscpLow.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dvbRcsPktClassDscpLow.setStatus("current")


class _DvbRcsPktClassDscpHigh_Type(Dscp):
    """Custom type dvbRcsPktClassDscpHigh based on Dscp"""
    defaultValue = 63


_DvbRcsPktClassDscpHigh_Object = MibTableColumn
dvbRcsPktClassDscpHigh = _DvbRcsPktClassDscpHigh_Object(
    (1, 3, 6, 1, 2, 1, 10, 239, 1, 1, 4, 1, 1, 3),
    _DvbRcsPktClassDscpHigh_Type()
)
dvbRcsPktClassDscpHigh.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dvbRcsPktClassDscpHigh.setStatus("current")


class _DvbRcsPktClassDscpMarkValue_Type(DscpOrAny):
    """Custom type dvbRcsPktClassDscpMarkValue based on DscpOrAny"""
    defaultValue = -1


_DvbRcsPktClassDscpMarkValue_Object = MibTableColumn
dvbRcsPktClassDscpMarkValue = _DvbRcsPktClassDscpMarkValue_Object(
    (1, 3, 6, 1, 2, 1, 10, 239, 1, 1, 4, 1, 1, 4),
    _DvbRcsPktClassDscpMarkValue_Type()
)
dvbRcsPktClassDscpMarkValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dvbRcsPktClassDscpMarkValue.setStatus("current")


class _DvbRcsPktClassIpProtocol_Type(Unsigned32):
    """Custom type dvbRcsPktClassIpProtocol based on Unsigned32"""
    defaultValue = 255

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_DvbRcsPktClassIpProtocol_Type.__name__ = "Unsigned32"
_DvbRcsPktClassIpProtocol_Object = MibTableColumn
dvbRcsPktClassIpProtocol = _DvbRcsPktClassIpProtocol_Object(
    (1, 3, 6, 1, 2, 1, 10, 239, 1, 1, 4, 1, 1, 5),
    _DvbRcsPktClassIpProtocol_Type()
)
dvbRcsPktClassIpProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dvbRcsPktClassIpProtocol.setStatus("current")
_DvbRcsPktClassSrcInetAddressType_Type = InetAddressType
_DvbRcsPktClassSrcInetAddressType_Object = MibTableColumn
dvbRcsPktClassSrcInetAddressType = _DvbRcsPktClassSrcInetAddressType_Object(
    (1, 3, 6, 1, 2, 1, 10, 239, 1, 1, 4, 1, 1, 6),
    _DvbRcsPktClassSrcInetAddressType_Type()
)
dvbRcsPktClassSrcInetAddressType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dvbRcsPktClassSrcInetAddressType.setStatus("current")
_DvbRcsPktClassSrcInetAddress_Type = InetAddress
_DvbRcsPktClassSrcInetAddress_Object = MibTableColumn
dvbRcsPktClassSrcInetAddress = _DvbRcsPktClassSrcInetAddress_Object(
    (1, 3, 6, 1, 2, 1, 10, 239, 1, 1, 4, 1, 1, 7),
    _DvbRcsPktClassSrcInetAddress_Type()
)
dvbRcsPktClassSrcInetAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dvbRcsPktClassSrcInetAddress.setStatus("current")


class _DvbRcsPktClassSrcInetAddressPrefixLength_Type(InetAddressPrefixLength):
    """Custom type dvbRcsPktClassSrcInetAddressPrefixLength based on InetAddressPrefixLength"""
    defaultValue = 0


_DvbRcsPktClassSrcInetAddressPrefixLength_Object = MibTableColumn
dvbRcsPktClassSrcInetAddressPrefixLength = _DvbRcsPktClassSrcInetAddressPrefixLength_Object(
    (1, 3, 6, 1, 2, 1, 10, 239, 1, 1, 4, 1, 1, 8),
    _DvbRcsPktClassSrcInetAddressPrefixLength_Type()
)
dvbRcsPktClassSrcInetAddressPrefixLength.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dvbRcsPktClassSrcInetAddressPrefixLength.setStatus("current")
_DvbRcsPktClassDstInetAddressType_Type = InetAddressType
_DvbRcsPktClassDstInetAddressType_Object = MibTableColumn
dvbRcsPktClassDstInetAddressType = _DvbRcsPktClassDstInetAddressType_Object(
    (1, 3, 6, 1, 2, 1, 10, 239, 1, 1, 4, 1, 1, 9),
    _DvbRcsPktClassDstInetAddressType_Type()
)
dvbRcsPktClassDstInetAddressType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dvbRcsPktClassDstInetAddressType.setStatus("current")
_DvbRcsPktClassDstInetAddress_Type = InetAddress
_DvbRcsPktClassDstInetAddress_Object = MibTableColumn
dvbRcsPktClassDstInetAddress = _DvbRcsPktClassDstInetAddress_Object(
    (1, 3, 6, 1, 2, 1, 10, 239, 1, 1, 4, 1, 1, 10),
    _DvbRcsPktClassDstInetAddress_Type()
)
dvbRcsPktClassDstInetAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dvbRcsPktClassDstInetAddress.setStatus("current")


class _DvbRcsPktClassDstInetAddressPrefixLength_Type(InetAddressPrefixLength):
    """Custom type dvbRcsPktClassDstInetAddressPrefixLength based on InetAddressPrefixLength"""
    defaultValue = 0


_DvbRcsPktClassDstInetAddressPrefixLength_Object = MibTableColumn
dvbRcsPktClassDstInetAddressPrefixLength = _DvbRcsPktClassDstInetAddressPrefixLength_Object(
    (1, 3, 6, 1, 2, 1, 10, 239, 1, 1, 4, 1, 1, 11),
    _DvbRcsPktClassDstInetAddressPrefixLength_Type()
)
dvbRcsPktClassDstInetAddressPrefixLength.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dvbRcsPktClassDstInetAddressPrefixLength.setStatus("current")


class _DvbRcsPktClassSrcPortLow_Type(InetPortNumber):
    """Custom type dvbRcsPktClassSrcPortLow based on InetPortNumber"""
    defaultValue = 0


_DvbRcsPktClassSrcPortLow_Object = MibTableColumn
dvbRcsPktClassSrcPortLow = _DvbRcsPktClassSrcPortLow_Object(
    (1, 3, 6, 1, 2, 1, 10, 239, 1, 1, 4, 1, 1, 12),
    _DvbRcsPktClassSrcPortLow_Type()
)
dvbRcsPktClassSrcPortLow.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dvbRcsPktClassSrcPortLow.setStatus("current")


class _DvbRcsPktClassSrcPortHigh_Type(InetPortNumber):
    """Custom type dvbRcsPktClassSrcPortHigh based on InetPortNumber"""
    defaultValue = 65535


_DvbRcsPktClassSrcPortHigh_Object = MibTableColumn
dvbRcsPktClassSrcPortHigh = _DvbRcsPktClassSrcPortHigh_Object(
    (1, 3, 6, 1, 2, 1, 10, 239, 1, 1, 4, 1, 1, 13),
    _DvbRcsPktClassSrcPortHigh_Type()
)
dvbRcsPktClassSrcPortHigh.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dvbRcsPktClassSrcPortHigh.setStatus("current")


class _DvbRcsPktClassDstPortLow_Type(InetPortNumber):
    """Custom type dvbRcsPktClassDstPortLow based on InetPortNumber"""
    defaultValue = 0


_DvbRcsPktClassDstPortLow_Object = MibTableColumn
dvbRcsPktClassDstPortLow = _DvbRcsPktClassDstPortLow_Object(
    (1, 3, 6, 1, 2, 1, 10, 239, 1, 1, 4, 1, 1, 14),
    _DvbRcsPktClassDstPortLow_Type()
)
dvbRcsPktClassDstPortLow.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dvbRcsPktClassDstPortLow.setStatus("current")


class _DvbRcsPktClassDstPortHigh_Type(InetPortNumber):
    """Custom type dvbRcsPktClassDstPortHigh based on InetPortNumber"""
    defaultValue = 65535


_DvbRcsPktClassDstPortHigh_Object = MibTableColumn
dvbRcsPktClassDstPortHigh = _DvbRcsPktClassDstPortHigh_Object(
    (1, 3, 6, 1, 2, 1, 10, 239, 1, 1, 4, 1, 1, 15),
    _DvbRcsPktClassDstPortHigh_Type()
)
dvbRcsPktClassDstPortHigh.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dvbRcsPktClassDstPortHigh.setStatus("current")


class _DvbRcsPktClassVlanUserPri_Type(Integer32):
    """Custom type dvbRcsPktClassVlanUserPri based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 7),
    )


_DvbRcsPktClassVlanUserPri_Type.__name__ = "Integer32"
_DvbRcsPktClassVlanUserPri_Object = MibTableColumn
dvbRcsPktClassVlanUserPri = _DvbRcsPktClassVlanUserPri_Object(
    (1, 3, 6, 1, 2, 1, 10, 239, 1, 1, 4, 1, 1, 16),
    _DvbRcsPktClassVlanUserPri_Type()
)
dvbRcsPktClassVlanUserPri.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dvbRcsPktClassVlanUserPri.setStatus("current")


class _DvbRcsPktClassPhbAssociation_Type(Unsigned32):
    """Custom type dvbRcsPktClassPhbAssociation based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DvbRcsPktClassPhbAssociation_Type.__name__ = "Unsigned32"
_DvbRcsPktClassPhbAssociation_Object = MibTableColumn
dvbRcsPktClassPhbAssociation = _DvbRcsPktClassPhbAssociation_Object(
    (1, 3, 6, 1, 2, 1, 10, 239, 1, 1, 4, 1, 1, 17),
    _DvbRcsPktClassPhbAssociation_Type()
)
dvbRcsPktClassPhbAssociation.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dvbRcsPktClassPhbAssociation.setStatus("current")
_DvbRcsPktClassRowStatus_Type = RowStatus
_DvbRcsPktClassRowStatus_Object = MibTableColumn
dvbRcsPktClassRowStatus = _DvbRcsPktClassRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 10, 239, 1, 1, 4, 1, 1, 18),
    _DvbRcsPktClassRowStatus_Type()
)
dvbRcsPktClassRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dvbRcsPktClassRowStatus.setStatus("current")
_DvbRcsPhbMappingTable_Object = MibTable
dvbRcsPhbMappingTable = _DvbRcsPhbMappingTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 239, 1, 1, 4, 2)
)
if mibBuilder.loadTexts:
    dvbRcsPhbMappingTable.setStatus("current")
_DvbRcsPhbMappingEntry_Object = MibTableRow
dvbRcsPhbMappingEntry = _DvbRcsPhbMappingEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 239, 1, 1, 4, 2, 1)
)
dvbRcsPhbMappingEntry.setIndexNames(
    (0, "DVB-RCS-MIB", "dvbRcsPhbIdentifier"),
)
if mibBuilder.loadTexts:
    dvbRcsPhbMappingEntry.setStatus("current")


class _DvbRcsPhbIdentifier_Type(Unsigned32):
    """Custom type dvbRcsPhbIdentifier based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DvbRcsPhbIdentifier_Type.__name__ = "Unsigned32"
_DvbRcsPhbIdentifier_Object = MibTableColumn
dvbRcsPhbIdentifier = _DvbRcsPhbIdentifier_Object(
    (1, 3, 6, 1, 2, 1, 10, 239, 1, 1, 4, 2, 1, 1),
    _DvbRcsPhbIdentifier_Type()
)
dvbRcsPhbIdentifier.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dvbRcsPhbIdentifier.setStatus("current")
_DvbRcsPhbName_Type = SnmpAdminString
_DvbRcsPhbName_Object = MibTableColumn
dvbRcsPhbName = _DvbRcsPhbName_Object(
    (1, 3, 6, 1, 2, 1, 10, 239, 1, 1, 4, 2, 1, 2),
    _DvbRcsPhbName_Type()
)
dvbRcsPhbName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dvbRcsPhbName.setStatus("current")


class _DvbRcsPhbRequestClassAssociation_Type(Unsigned32):
    """Custom type dvbRcsPhbRequestClassAssociation based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_DvbRcsPhbRequestClassAssociation_Type.__name__ = "Unsigned32"
_DvbRcsPhbRequestClassAssociation_Object = MibTableColumn
dvbRcsPhbRequestClassAssociation = _DvbRcsPhbRequestClassAssociation_Object(
    (1, 3, 6, 1, 2, 1, 10, 239, 1, 1, 4, 2, 1, 3),
    _DvbRcsPhbRequestClassAssociation_Type()
)
dvbRcsPhbRequestClassAssociation.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dvbRcsPhbRequestClassAssociation.setStatus("current")


class _DvbRcsPhbMappingRowStatus_Type(RowStatus):
    """Custom type dvbRcsPhbMappingRowStatus based on RowStatus"""


_DvbRcsPhbMappingRowStatus_Object = MibTableColumn
dvbRcsPhbMappingRowStatus = _DvbRcsPhbMappingRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 10, 239, 1, 1, 4, 2, 1, 4),
    _DvbRcsPhbMappingRowStatus_Type()
)
dvbRcsPhbMappingRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dvbRcsPhbMappingRowStatus.setStatus("current")
_DvbRcsRequestClassTable_Object = MibTable
dvbRcsRequestClassTable = _DvbRcsRequestClassTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 239, 1, 1, 4, 3)
)
if mibBuilder.loadTexts:
    dvbRcsRequestClassTable.setStatus("current")
_DvbRcsRequestClassEntry_Object = MibTableRow
dvbRcsRequestClassEntry = _DvbRcsRequestClassEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 239, 1, 1, 4, 3, 1)
)
dvbRcsRequestClassEntry.setIndexNames(
    (0, "DVB-RCS-MIB", "dvbRcsRequestClassIndex"),
)
if mibBuilder.loadTexts:
    dvbRcsRequestClassEntry.setStatus("current")


class _DvbRcsRequestClassIndex_Type(Unsigned32):
    """Custom type dvbRcsRequestClassIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_DvbRcsRequestClassIndex_Type.__name__ = "Unsigned32"
_DvbRcsRequestClassIndex_Object = MibTableColumn
dvbRcsRequestClassIndex = _DvbRcsRequestClassIndex_Object(
    (1, 3, 6, 1, 2, 1, 10, 239, 1, 1, 4, 3, 1, 1),
    _DvbRcsRequestClassIndex_Type()
)
dvbRcsRequestClassIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dvbRcsRequestClassIndex.setStatus("current")
_DvbRcsRequestClassName_Type = SnmpAdminString
_DvbRcsRequestClassName_Object = MibTableColumn
dvbRcsRequestClassName = _DvbRcsRequestClassName_Object(
    (1, 3, 6, 1, 2, 1, 10, 239, 1, 1, 4, 3, 1, 2),
    _DvbRcsRequestClassName_Type()
)
dvbRcsRequestClassName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dvbRcsRequestClassName.setStatus("current")


class _DvbRcsRequestClassChanId_Type(Unsigned32):
    """Custom type dvbRcsRequestClassChanId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_DvbRcsRequestClassChanId_Type.__name__ = "Unsigned32"
_DvbRcsRequestClassChanId_Object = MibTableColumn
dvbRcsRequestClassChanId = _DvbRcsRequestClassChanId_Object(
    (1, 3, 6, 1, 2, 1, 10, 239, 1, 1, 4, 3, 1, 3),
    _DvbRcsRequestClassChanId_Type()
)
dvbRcsRequestClassChanId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dvbRcsRequestClassChanId.setStatus("current")


class _DvbRcsRequestClassVccVpi_Type(Unsigned32):
    """Custom type dvbRcsRequestClassVccVpi based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_DvbRcsRequestClassVccVpi_Type.__name__ = "Unsigned32"
_DvbRcsRequestClassVccVpi_Object = MibTableColumn
dvbRcsRequestClassVccVpi = _DvbRcsRequestClassVccVpi_Object(
    (1, 3, 6, 1, 2, 1, 10, 239, 1, 1, 4, 3, 1, 4),
    _DvbRcsRequestClassVccVpi_Type()
)
dvbRcsRequestClassVccVpi.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dvbRcsRequestClassVccVpi.setStatus("current")


class _DvbRcsRequestClassVccVci_Type(Unsigned32):
    """Custom type dvbRcsRequestClassVccVci based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DvbRcsRequestClassVccVci_Type.__name__ = "Unsigned32"
_DvbRcsRequestClassVccVci_Object = MibTableColumn
dvbRcsRequestClassVccVci = _DvbRcsRequestClassVccVci_Object(
    (1, 3, 6, 1, 2, 1, 10, 239, 1, 1, 4, 3, 1, 5),
    _DvbRcsRequestClassVccVci_Type()
)
dvbRcsRequestClassVccVci.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dvbRcsRequestClassVccVci.setStatus("current")


class _DvbRcsRequestClassPidPoolReference_Type(Unsigned32):
    """Custom type dvbRcsRequestClassPidPoolReference based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_DvbRcsRequestClassPidPoolReference_Type.__name__ = "Unsigned32"
_DvbRcsRequestClassPidPoolReference_Object = MibTableColumn
dvbRcsRequestClassPidPoolReference = _DvbRcsRequestClassPidPoolReference_Object(
    (1, 3, 6, 1, 2, 1, 10, 239, 1, 1, 4, 3, 1, 6),
    _DvbRcsRequestClassPidPoolReference_Type()
)
dvbRcsRequestClassPidPoolReference.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dvbRcsRequestClassPidPoolReference.setStatus("current")
_DvbRcsRequestClassCra_Type = Unsigned32
_DvbRcsRequestClassCra_Object = MibTableColumn
dvbRcsRequestClassCra = _DvbRcsRequestClassCra_Object(
    (1, 3, 6, 1, 2, 1, 10, 239, 1, 1, 4, 3, 1, 7),
    _DvbRcsRequestClassCra_Type()
)
dvbRcsRequestClassCra.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dvbRcsRequestClassCra.setStatus("current")
if mibBuilder.loadTexts:
    dvbRcsRequestClassCra.setUnits("bit/s")
_DvbRcsRequestClassRbdcMax_Type = Unsigned32
_DvbRcsRequestClassRbdcMax_Object = MibTableColumn
dvbRcsRequestClassRbdcMax = _DvbRcsRequestClassRbdcMax_Object(
    (1, 3, 6, 1, 2, 1, 10, 239, 1, 1, 4, 3, 1, 8),
    _DvbRcsRequestClassRbdcMax_Type()
)
dvbRcsRequestClassRbdcMax.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dvbRcsRequestClassRbdcMax.setStatus("current")
if mibBuilder.loadTexts:
    dvbRcsRequestClassRbdcMax.setUnits("x2 kbit/s")
_DvbRcsRequestClassRbdcTimeout_Type = Unsigned32
_DvbRcsRequestClassRbdcTimeout_Object = MibTableColumn
dvbRcsRequestClassRbdcTimeout = _DvbRcsRequestClassRbdcTimeout_Object(
    (1, 3, 6, 1, 2, 1, 10, 239, 1, 1, 4, 3, 1, 9),
    _DvbRcsRequestClassRbdcTimeout_Type()
)
dvbRcsRequestClassRbdcTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dvbRcsRequestClassRbdcTimeout.setStatus("current")
if mibBuilder.loadTexts:
    dvbRcsRequestClassRbdcTimeout.setUnits("superframes")
_DvbRcsRequestClassVbdcMax_Type = Unsigned32
_DvbRcsRequestClassVbdcMax_Object = MibTableColumn
dvbRcsRequestClassVbdcMax = _DvbRcsRequestClassVbdcMax_Object(
    (1, 3, 6, 1, 2, 1, 10, 239, 1, 1, 4, 3, 1, 10),
    _DvbRcsRequestClassVbdcMax_Type()
)
dvbRcsRequestClassVbdcMax.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dvbRcsRequestClassVbdcMax.setStatus("current")
if mibBuilder.loadTexts:
    dvbRcsRequestClassVbdcMax.setUnits("ATM cells/MPEG packets")
_DvbRcsRequestClassVbdcTimeout_Type = Unsigned32
_DvbRcsRequestClassVbdcTimeout_Object = MibTableColumn
dvbRcsRequestClassVbdcTimeout = _DvbRcsRequestClassVbdcTimeout_Object(
    (1, 3, 6, 1, 2, 1, 10, 239, 1, 1, 4, 3, 1, 11),
    _DvbRcsRequestClassVbdcTimeout_Type()
)
dvbRcsRequestClassVbdcTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dvbRcsRequestClassVbdcTimeout.setStatus("current")
if mibBuilder.loadTexts:
    dvbRcsRequestClassVbdcTimeout.setUnits("superframes")
_DvbRcsRequestClassVbdcMaxBackLog_Type = Unsigned32
_DvbRcsRequestClassVbdcMaxBackLog_Object = MibTableColumn
dvbRcsRequestClassVbdcMaxBackLog = _DvbRcsRequestClassVbdcMaxBackLog_Object(
    (1, 3, 6, 1, 2, 1, 10, 239, 1, 1, 4, 3, 1, 12),
    _DvbRcsRequestClassVbdcMaxBackLog_Type()
)
dvbRcsRequestClassVbdcMaxBackLog.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dvbRcsRequestClassVbdcMaxBackLog.setStatus("current")
if mibBuilder.loadTexts:
    dvbRcsRequestClassVbdcMaxBackLog.setUnits("bytes")
_DvbRcsRequestClassRowStatus_Type = RowStatus
_DvbRcsRequestClassRowStatus_Object = MibTableColumn
dvbRcsRequestClassRowStatus = _DvbRcsRequestClassRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 10, 239, 1, 1, 4, 3, 1, 13),
    _DvbRcsRequestClassRowStatus_Type()
)
dvbRcsRequestClassRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dvbRcsRequestClassRowStatus.setStatus("current")
_DvbRcsPidPoolTable_Object = MibTable
dvbRcsPidPoolTable = _DvbRcsPidPoolTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 239, 1, 1, 4, 4)
)
if mibBuilder.loadTexts:
    dvbRcsPidPoolTable.setStatus("current")
_DvbRcsPidPoolEntry_Object = MibTableRow
dvbRcsPidPoolEntry = _DvbRcsPidPoolEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 239, 1, 1, 4, 4, 1)
)
dvbRcsPidPoolEntry.setIndexNames(
    (0, "DVB-RCS-MIB", "dvbRcsPidPoolIndex"),
    (0, "DVB-RCS-MIB", "dvbRcsPidIndex"),
)
if mibBuilder.loadTexts:
    dvbRcsPidPoolEntry.setStatus("current")


class _DvbRcsPidPoolIndex_Type(Unsigned32):
    """Custom type dvbRcsPidPoolIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_DvbRcsPidPoolIndex_Type.__name__ = "Unsigned32"
_DvbRcsPidPoolIndex_Object = MibTableColumn
dvbRcsPidPoolIndex = _DvbRcsPidPoolIndex_Object(
    (1, 3, 6, 1, 2, 1, 10, 239, 1, 1, 4, 4, 1, 1),
    _DvbRcsPidPoolIndex_Type()
)
dvbRcsPidPoolIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dvbRcsPidPoolIndex.setStatus("current")


class _DvbRcsPidIndex_Type(Unsigned32):
    """Custom type dvbRcsPidIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_DvbRcsPidIndex_Type.__name__ = "Unsigned32"
_DvbRcsPidIndex_Object = MibTableColumn
dvbRcsPidIndex = _DvbRcsPidIndex_Object(
    (1, 3, 6, 1, 2, 1, 10, 239, 1, 1, 4, 4, 1, 2),
    _DvbRcsPidIndex_Type()
)
dvbRcsPidIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dvbRcsPidIndex.setStatus("current")


class _DvbRcsPidValue_Type(Unsigned32):
    """Custom type dvbRcsPidValue based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8191),
    )


_DvbRcsPidValue_Type.__name__ = "Unsigned32"
_DvbRcsPidValue_Object = MibTableColumn
dvbRcsPidValue = _DvbRcsPidValue_Object(
    (1, 3, 6, 1, 2, 1, 10, 239, 1, 1, 4, 4, 1, 3),
    _DvbRcsPidValue_Type()
)
dvbRcsPidValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dvbRcsPidValue.setStatus("current")


class _DvbRcsPidPoolRowStatus_Type(RowStatus):
    """Custom type dvbRcsPidPoolRowStatus based on RowStatus"""


_DvbRcsPidPoolRowStatus_Object = MibTableColumn
dvbRcsPidPoolRowStatus = _DvbRcsPidPoolRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 10, 239, 1, 1, 4, 4, 1, 4),
    _DvbRcsPidPoolRowStatus_Type()
)
dvbRcsPidPoolRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dvbRcsPidPoolRowStatus.setStatus("current")
_DvbRcsQosGlobalRbdcMax_Type = Unsigned32
_DvbRcsQosGlobalRbdcMax_Object = MibScalar
dvbRcsQosGlobalRbdcMax = _DvbRcsQosGlobalRbdcMax_Object(
    (1, 3, 6, 1, 2, 1, 10, 239, 1, 1, 4, 5),
    _DvbRcsQosGlobalRbdcMax_Type()
)
dvbRcsQosGlobalRbdcMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dvbRcsQosGlobalRbdcMax.setStatus("current")
if mibBuilder.loadTexts:
    dvbRcsQosGlobalRbdcMax.setUnits("x2 kbit/s")
_DvbRcsQosGlobalVbdcMax_Type = Unsigned32
_DvbRcsQosGlobalVbdcMax_Object = MibScalar
dvbRcsQosGlobalVbdcMax = _DvbRcsQosGlobalVbdcMax_Object(
    (1, 3, 6, 1, 2, 1, 10, 239, 1, 1, 4, 6),
    _DvbRcsQosGlobalVbdcMax_Type()
)
dvbRcsQosGlobalVbdcMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dvbRcsQosGlobalVbdcMax.setStatus("current")
if mibBuilder.loadTexts:
    dvbRcsQosGlobalVbdcMax.setUnits("ATM cells/MPEG packets")
_DvbRcsQosGlobalVbdcMaxBackLog_Type = Unsigned32
_DvbRcsQosGlobalVbdcMaxBackLog_Object = MibScalar
dvbRcsQosGlobalVbdcMaxBackLog = _DvbRcsQosGlobalVbdcMaxBackLog_Object(
    (1, 3, 6, 1, 2, 1, 10, 239, 1, 1, 4, 7),
    _DvbRcsQosGlobalVbdcMaxBackLog_Type()
)
dvbRcsQosGlobalVbdcMaxBackLog.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dvbRcsQosGlobalVbdcMaxBackLog.setStatus("current")
if mibBuilder.loadTexts:
    dvbRcsQosGlobalVbdcMaxBackLog.setUnits("bytes")


class _DvbRcsQosChannelIdStrictDispatching_Type(Integer32):
    """Custom type dvbRcsQosChannelIdStrictDispatching based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("notStrict", 0),
          ("strict", 1))
    )


_DvbRcsQosChannelIdStrictDispatching_Type.__name__ = "Integer32"
_DvbRcsQosChannelIdStrictDispatching_Object = MibScalar
dvbRcsQosChannelIdStrictDispatching = _DvbRcsQosChannelIdStrictDispatching_Object(
    (1, 3, 6, 1, 2, 1, 10, 239, 1, 1, 4, 8),
    _DvbRcsQosChannelIdStrictDispatching_Type()
)
dvbRcsQosChannelIdStrictDispatching.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dvbRcsQosChannelIdStrictDispatching.setStatus("current")
_DvbRcsRcstControl_ObjectIdentity = ObjectIdentity
dvbRcsRcstControl = _DvbRcsRcstControl_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 239, 1, 1, 5)
)


class _DvbRcsCtrlRebootCommand_Type(Integer32):
    """Custom type dvbRcsCtrlRebootCommand based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("alternate", 3),
          ("idle", 1),
          ("normal", 2))
    )


_DvbRcsCtrlRebootCommand_Type.__name__ = "Integer32"
_DvbRcsCtrlRebootCommand_Object = MibScalar
dvbRcsCtrlRebootCommand = _DvbRcsCtrlRebootCommand_Object(
    (1, 3, 6, 1, 2, 1, 10, 239, 1, 1, 5, 1),
    _DvbRcsCtrlRebootCommand_Type()
)
dvbRcsCtrlRebootCommand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dvbRcsCtrlRebootCommand.setStatus("current")


class _DvbRcsCtrlRcstTxDisable_Type(Integer32):
    """Custom type dvbRcsCtrlRcstTxDisable based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("idle", 1))
    )


_DvbRcsCtrlRcstTxDisable_Type.__name__ = "Integer32"
_DvbRcsCtrlRcstTxDisable_Object = MibScalar
dvbRcsCtrlRcstTxDisable = _DvbRcsCtrlRcstTxDisable_Object(
    (1, 3, 6, 1, 2, 1, 10, 239, 1, 1, 5, 2),
    _DvbRcsCtrlRcstTxDisable_Type()
)
dvbRcsCtrlRcstTxDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dvbRcsCtrlRcstTxDisable.setStatus("current")


class _DvbRcsCtrlUserTrafficDisable_Type(Integer32):
    """Custom type dvbRcsCtrlUserTrafficDisable based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("idle", 1))
    )


_DvbRcsCtrlUserTrafficDisable_Type.__name__ = "Integer32"
_DvbRcsCtrlUserTrafficDisable_Object = MibScalar
dvbRcsCtrlUserTrafficDisable = _DvbRcsCtrlUserTrafficDisable_Object(
    (1, 3, 6, 1, 2, 1, 10, 239, 1, 1, 5, 3),
    _DvbRcsCtrlUserTrafficDisable_Type()
)
dvbRcsCtrlUserTrafficDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dvbRcsCtrlUserTrafficDisable.setStatus("current")


class _DvbRcsCtrlCwEnable_Type(Integer32):
    """Custom type dvbRcsCtrlCwEnable based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_DvbRcsCtrlCwEnable_Type.__name__ = "Integer32"
_DvbRcsCtrlCwEnable_Object = MibScalar
dvbRcsCtrlCwEnable = _DvbRcsCtrlCwEnable_Object(
    (1, 3, 6, 1, 2, 1, 10, 239, 1, 1, 5, 4),
    _DvbRcsCtrlCwEnable_Type()
)
dvbRcsCtrlCwEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dvbRcsCtrlCwEnable.setStatus("current")


class _DvbRcsCtrlOduTxReferenceEnable_Type(Integer32):
    """Custom type dvbRcsCtrlOduTxReferenceEnable based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_DvbRcsCtrlOduTxReferenceEnable_Type.__name__ = "Integer32"
_DvbRcsCtrlOduTxReferenceEnable_Object = MibScalar
dvbRcsCtrlOduTxReferenceEnable = _DvbRcsCtrlOduTxReferenceEnable_Object(
    (1, 3, 6, 1, 2, 1, 10, 239, 1, 1, 5, 5),
    _DvbRcsCtrlOduTxReferenceEnable_Type()
)
dvbRcsCtrlOduTxReferenceEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dvbRcsCtrlOduTxReferenceEnable.setStatus("current")


class _DvbRcsCtrlOduTxDCEnable_Type(Integer32):
    """Custom type dvbRcsCtrlOduTxDCEnable based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_DvbRcsCtrlOduTxDCEnable_Type.__name__ = "Integer32"
_DvbRcsCtrlOduTxDCEnable_Object = MibScalar
dvbRcsCtrlOduTxDCEnable = _DvbRcsCtrlOduTxDCEnable_Object(
    (1, 3, 6, 1, 2, 1, 10, 239, 1, 1, 5, 6),
    _DvbRcsCtrlOduTxDCEnable_Type()
)
dvbRcsCtrlOduTxDCEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dvbRcsCtrlOduTxDCEnable.setStatus("current")


class _DvbRcsCtrlOduRxDCEnable_Type(Integer32):
    """Custom type dvbRcsCtrlOduRxDCEnable based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_DvbRcsCtrlOduRxDCEnable_Type.__name__ = "Integer32"
_DvbRcsCtrlOduRxDCEnable_Object = MibScalar
dvbRcsCtrlOduRxDCEnable = _DvbRcsCtrlOduRxDCEnable_Object(
    (1, 3, 6, 1, 2, 1, 10, 239, 1, 1, 5, 7),
    _DvbRcsCtrlOduRxDCEnable_Type()
)
dvbRcsCtrlOduRxDCEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dvbRcsCtrlOduRxDCEnable.setStatus("current")


class _DvbRcsCtrlDownloadFileCommand_Type(Integer32):
    """Custom type dvbRcsCtrlDownloadFileCommand based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("config", 2),
          ("idle", 1),
          ("installationLog", 3))
    )


_DvbRcsCtrlDownloadFileCommand_Type.__name__ = "Integer32"
_DvbRcsCtrlDownloadFileCommand_Object = MibScalar
dvbRcsCtrlDownloadFileCommand = _DvbRcsCtrlDownloadFileCommand_Object(
    (1, 3, 6, 1, 2, 1, 10, 239, 1, 1, 5, 8),
    _DvbRcsCtrlDownloadFileCommand_Type()
)
dvbRcsCtrlDownloadFileCommand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dvbRcsCtrlDownloadFileCommand.setStatus("current")


class _DvbRcsCtrlUploadFileCommand_Type(Integer32):
    """Custom type dvbRcsCtrlUploadFileCommand based on Integer32"""
    defaultValue = 1

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
        *(("config", 2),
          ("eventAlarm", 3),
          ("idle", 1),
          ("installationLog", 4))
    )


_DvbRcsCtrlUploadFileCommand_Type.__name__ = "Integer32"
_DvbRcsCtrlUploadFileCommand_Object = MibScalar
dvbRcsCtrlUploadFileCommand = _DvbRcsCtrlUploadFileCommand_Object(
    (1, 3, 6, 1, 2, 1, 10, 239, 1, 1, 5, 9),
    _DvbRcsCtrlUploadFileCommand_Type()
)
dvbRcsCtrlUploadFileCommand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dvbRcsCtrlUploadFileCommand.setStatus("current")


class _DvbRcsCtrlActivateConfigFileCommand_Type(Integer32):
    """Custom type dvbRcsCtrlActivateConfigFileCommand based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("activate", 2),
          ("idle", 1))
    )


_DvbRcsCtrlActivateConfigFileCommand_Type.__name__ = "Integer32"
_DvbRcsCtrlActivateConfigFileCommand_Object = MibScalar
dvbRcsCtrlActivateConfigFileCommand = _DvbRcsCtrlActivateConfigFileCommand_Object(
    (1, 3, 6, 1, 2, 1, 10, 239, 1, 1, 5, 10),
    _DvbRcsCtrlActivateConfigFileCommand_Type()
)
dvbRcsCtrlActivateConfigFileCommand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dvbRcsCtrlActivateConfigFileCommand.setStatus("current")


class _DvbRcsCtrlRcstLogonCommand_Type(Integer32):
    """Custom type dvbRcsCtrlRcstLogonCommand based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("idle", 1),
          ("logon", 2))
    )


_DvbRcsCtrlRcstLogonCommand_Type.__name__ = "Integer32"
_DvbRcsCtrlRcstLogonCommand_Object = MibScalar
dvbRcsCtrlRcstLogonCommand = _DvbRcsCtrlRcstLogonCommand_Object(
    (1, 3, 6, 1, 2, 1, 10, 239, 1, 1, 5, 11),
    _DvbRcsCtrlRcstLogonCommand_Type()
)
dvbRcsCtrlRcstLogonCommand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dvbRcsCtrlRcstLogonCommand.setStatus("current")


class _DvbRcsCtrlRcstLogoffCommand_Type(Integer32):
    """Custom type dvbRcsCtrlRcstLogoffCommand based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("idle", 1),
          ("logoff", 2))
    )


_DvbRcsCtrlRcstLogoffCommand_Type.__name__ = "Integer32"
_DvbRcsCtrlRcstLogoffCommand_Object = MibScalar
dvbRcsCtrlRcstLogoffCommand = _DvbRcsCtrlRcstLogoffCommand_Object(
    (1, 3, 6, 1, 2, 1, 10, 239, 1, 1, 5, 12),
    _DvbRcsCtrlRcstLogoffCommand_Type()
)
dvbRcsCtrlRcstLogoffCommand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dvbRcsCtrlRcstLogoffCommand.setStatus("current")


class _DvbRcsCtrlRcstRxReacquire_Type(Integer32):
    """Custom type dvbRcsCtrlRcstRxReacquire based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("idle", 1),
          ("reacquireForwardLink", 2))
    )


_DvbRcsCtrlRcstRxReacquire_Type.__name__ = "Integer32"
_DvbRcsCtrlRcstRxReacquire_Object = MibScalar
dvbRcsCtrlRcstRxReacquire = _DvbRcsCtrlRcstRxReacquire_Object(
    (1, 3, 6, 1, 2, 1, 10, 239, 1, 1, 5, 13),
    _DvbRcsCtrlRcstRxReacquire_Type()
)
dvbRcsCtrlRcstRxReacquire.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dvbRcsCtrlRcstRxReacquire.setStatus("current")
_DvbRcsRcstState_ObjectIdentity = ObjectIdentity
dvbRcsRcstState = _DvbRcsRcstState_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 239, 1, 1, 6)
)


class _DvbRcsRcstMode_Type(Integer32):
    """Custom type dvbRcsRcstMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("installation", 0),
          ("operational", 1))
    )


_DvbRcsRcstMode_Type.__name__ = "Integer32"
_DvbRcsRcstMode_Object = MibScalar
dvbRcsRcstMode = _DvbRcsRcstMode_Object(
    (1, 3, 6, 1, 2, 1, 10, 239, 1, 1, 6, 1),
    _DvbRcsRcstMode_Type()
)
dvbRcsRcstMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dvbRcsRcstMode.setStatus("current")


class _DvbRcsRcstFaultStatus_Type(Integer32):
    """Custom type dvbRcsRcstFaultStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("fault", 1),
          ("nofault", 0))
    )


_DvbRcsRcstFaultStatus_Type.__name__ = "Integer32"
_DvbRcsRcstFaultStatus_Object = MibScalar
dvbRcsRcstFaultStatus = _DvbRcsRcstFaultStatus_Object(
    (1, 3, 6, 1, 2, 1, 10, 239, 1, 1, 6, 2),
    _DvbRcsRcstFaultStatus_Type()
)
dvbRcsRcstFaultStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dvbRcsRcstFaultStatus.setStatus("current")


class _DvbRcsRcstFwdLinkStatus_Type(Integer32):
    """Custom type dvbRcsRcstFwdLinkStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("acquired", 1),
          ("notAcquired", 0))
    )


_DvbRcsRcstFwdLinkStatus_Type.__name__ = "Integer32"
_DvbRcsRcstFwdLinkStatus_Object = MibScalar
dvbRcsRcstFwdLinkStatus = _DvbRcsRcstFwdLinkStatus_Object(
    (1, 3, 6, 1, 2, 1, 10, 239, 1, 1, 6, 3),
    _DvbRcsRcstFwdLinkStatus_Type()
)
dvbRcsRcstFwdLinkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dvbRcsRcstFwdLinkStatus.setStatus("current")


class _DvbRcsRcstRtnLinkStatus_Type(Integer32):
    """Custom type dvbRcsRcstRtnLinkStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("loggedOff", 0),
          ("loggedOn", 1))
    )


_DvbRcsRcstRtnLinkStatus_Type.__name__ = "Integer32"
_DvbRcsRcstRtnLinkStatus_Object = MibScalar
dvbRcsRcstRtnLinkStatus = _DvbRcsRcstRtnLinkStatus_Object(
    (1, 3, 6, 1, 2, 1, 10, 239, 1, 1, 6, 4),
    _DvbRcsRcstRtnLinkStatus_Type()
)
dvbRcsRcstRtnLinkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dvbRcsRcstRtnLinkStatus.setStatus("current")


class _DvbRcsRcstLogUpdated_Type(Integer32):
    """Custom type dvbRcsRcstLogUpdated based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("logfileUpdated", 1),
          ("noUpdate", 0))
    )


_DvbRcsRcstLogUpdated_Type.__name__ = "Integer32"
_DvbRcsRcstLogUpdated_Object = MibScalar
dvbRcsRcstLogUpdated = _DvbRcsRcstLogUpdated_Object(
    (1, 3, 6, 1, 2, 1, 10, 239, 1, 1, 6, 5),
    _DvbRcsRcstLogUpdated_Type()
)
dvbRcsRcstLogUpdated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dvbRcsRcstLogUpdated.setStatus("current")
_DvbRcsRcstCurrentSoftwareVersion_Type = SnmpAdminString
_DvbRcsRcstCurrentSoftwareVersion_Object = MibScalar
dvbRcsRcstCurrentSoftwareVersion = _DvbRcsRcstCurrentSoftwareVersion_Object(
    (1, 3, 6, 1, 2, 1, 10, 239, 1, 1, 6, 6),
    _DvbRcsRcstCurrentSoftwareVersion_Type()
)
dvbRcsRcstCurrentSoftwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dvbRcsRcstCurrentSoftwareVersion.setStatus("current")
_DvbRcsRcstAlternateSoftwareVersion_Type = SnmpAdminString
_DvbRcsRcstAlternateSoftwareVersion_Object = MibScalar
dvbRcsRcstAlternateSoftwareVersion = _DvbRcsRcstAlternateSoftwareVersion_Object(
    (1, 3, 6, 1, 2, 1, 10, 239, 1, 1, 6, 7),
    _DvbRcsRcstAlternateSoftwareVersion_Type()
)
dvbRcsRcstAlternateSoftwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dvbRcsRcstAlternateSoftwareVersion.setStatus("current")
_DvbRcsRcstActivatedConfigFileVersion_Type = SnmpAdminString
_DvbRcsRcstActivatedConfigFileVersion_Object = MibScalar
dvbRcsRcstActivatedConfigFileVersion = _DvbRcsRcstActivatedConfigFileVersion_Object(
    (1, 3, 6, 1, 2, 1, 10, 239, 1, 1, 6, 8),
    _DvbRcsRcstActivatedConfigFileVersion_Type()
)
dvbRcsRcstActivatedConfigFileVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dvbRcsRcstActivatedConfigFileVersion.setStatus("current")
_DvbRcsRcstDownloadedConfigFileVersion_Type = SnmpAdminString
_DvbRcsRcstDownloadedConfigFileVersion_Object = MibScalar
dvbRcsRcstDownloadedConfigFileVersion = _DvbRcsRcstDownloadedConfigFileVersion_Object(
    (1, 3, 6, 1, 2, 1, 10, 239, 1, 1, 6, 9),
    _DvbRcsRcstDownloadedConfigFileVersion_Type()
)
dvbRcsRcstDownloadedConfigFileVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dvbRcsRcstDownloadedConfigFileVersion.setStatus("current")
_DvbRcsFwdLink_ObjectIdentity = ObjectIdentity
dvbRcsFwdLink = _DvbRcsFwdLink_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 239, 1, 2)
)
_DvbRcsFwdConfig_ObjectIdentity = ObjectIdentity
dvbRcsFwdConfig = _DvbRcsFwdConfig_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 239, 1, 2, 1)
)
_DvbRcsFwdStartTable_Object = MibTable
dvbRcsFwdStartTable = _DvbRcsFwdStartTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 239, 1, 2, 1, 1)
)
if mibBuilder.loadTexts:
    dvbRcsFwdStartTable.setStatus("current")
_DvbRcsFwdStartEntry_Object = MibTableRow
dvbRcsFwdStartEntry = _DvbRcsFwdStartEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 239, 1, 2, 1, 1, 1)
)
dvbRcsFwdStartEntry.setIndexNames(
    (0, "DVB-RCS-MIB", "dvbRcsFwdStartIndex"),
)
if mibBuilder.loadTexts:
    dvbRcsFwdStartEntry.setStatus("current")


class _DvbRcsFwdStartIndex_Type(Unsigned32):
    """Custom type dvbRcsFwdStartIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_DvbRcsFwdStartIndex_Type.__name__ = "Unsigned32"
_DvbRcsFwdStartIndex_Object = MibTableColumn
dvbRcsFwdStartIndex = _DvbRcsFwdStartIndex_Object(
    (1, 3, 6, 1, 2, 1, 10, 239, 1, 2, 1, 1, 1, 1),
    _DvbRcsFwdStartIndex_Type()
)
dvbRcsFwdStartIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dvbRcsFwdStartIndex.setStatus("current")


class _DvbRcsFwdStartPopId_Type(Integer32):
    """Custom type dvbRcsFwdStartPopId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 65535),
    )


_DvbRcsFwdStartPopId_Type.__name__ = "Integer32"
_DvbRcsFwdStartPopId_Object = MibTableColumn
dvbRcsFwdStartPopId = _DvbRcsFwdStartPopId_Object(
    (1, 3, 6, 1, 2, 1, 10, 239, 1, 2, 1, 1, 1, 2),
    _DvbRcsFwdStartPopId_Type()
)
dvbRcsFwdStartPopId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dvbRcsFwdStartPopId.setStatus("current")
_DvbRcsFwdStartFrequency_Type = Unsigned32
_DvbRcsFwdStartFrequency_Object = MibTableColumn
dvbRcsFwdStartFrequency = _DvbRcsFwdStartFrequency_Object(
    (1, 3, 6, 1, 2, 1, 10, 239, 1, 2, 1, 1, 1, 3),
    _DvbRcsFwdStartFrequency_Type()
)
dvbRcsFwdStartFrequency.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dvbRcsFwdStartFrequency.setStatus("current")
if mibBuilder.loadTexts:
    dvbRcsFwdStartFrequency.setUnits("x100 kHz")


class _DvbRcsFwdStartPolar_Type(Integer32):
    """Custom type dvbRcsFwdStartPolar based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("circularLeft", 2),
          ("circularRight", 3),
          ("linearHorizontal", 0),
          ("linearVertical", 1))
    )


_DvbRcsFwdStartPolar_Type.__name__ = "Integer32"
_DvbRcsFwdStartPolar_Object = MibTableColumn
dvbRcsFwdStartPolar = _DvbRcsFwdStartPolar_Object(
    (1, 3, 6, 1, 2, 1, 10, 239, 1, 2, 1, 1, 1, 4),
    _DvbRcsFwdStartPolar_Type()
)
dvbRcsFwdStartPolar.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dvbRcsFwdStartPolar.setStatus("current")


class _DvbRcsFwdStartFormat_Type(Integer32):
    """Custom type dvbRcsFwdStartFormat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("auto", -1),
          ("dvbs", 0),
          ("dvbs2acm", 2),
          ("dvbs2ccm", 1))
    )


_DvbRcsFwdStartFormat_Type.__name__ = "Integer32"
_DvbRcsFwdStartFormat_Object = MibTableColumn
dvbRcsFwdStartFormat = _DvbRcsFwdStartFormat_Object(
    (1, 3, 6, 1, 2, 1, 10, 239, 1, 2, 1, 1, 1, 5),
    _DvbRcsFwdStartFormat_Type()
)
dvbRcsFwdStartFormat.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dvbRcsFwdStartFormat.setStatus("current")


class _DvbRcsFwdStartRolloff_Type(Integer32):
    """Custom type dvbRcsFwdStartRolloff based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("autoRolloff", 0),
          ("rolloff020", 1),
          ("rolloff025", 2),
          ("rolloff035", 3))
    )


_DvbRcsFwdStartRolloff_Type.__name__ = "Integer32"
_DvbRcsFwdStartRolloff_Object = MibTableColumn
dvbRcsFwdStartRolloff = _DvbRcsFwdStartRolloff_Object(
    (1, 3, 6, 1, 2, 1, 10, 239, 1, 2, 1, 1, 1, 6),
    _DvbRcsFwdStartRolloff_Type()
)
dvbRcsFwdStartRolloff.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dvbRcsFwdStartRolloff.setStatus("current")
_DvbRcsFwdStartSymbolRate_Type = Unsigned32
_DvbRcsFwdStartSymbolRate_Object = MibTableColumn
dvbRcsFwdStartSymbolRate = _DvbRcsFwdStartSymbolRate_Object(
    (1, 3, 6, 1, 2, 1, 10, 239, 1, 2, 1, 1, 1, 7),
    _DvbRcsFwdStartSymbolRate_Type()
)
dvbRcsFwdStartSymbolRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dvbRcsFwdStartSymbolRate.setStatus("current")
if mibBuilder.loadTexts:
    dvbRcsFwdStartSymbolRate.setUnits("x100 symbols/s")


class _DvbRcsFwdStartInnerFec_Type(Integer32):
    """Custom type dvbRcsFwdStartInnerFec based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1,
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
              12)
        )
    )
    namedValues = NamedValues(
        *(("autoFec", -1),
          ("fecRate12", 0),
          ("fecRate13", 10),
          ("fecRate14", 11),
          ("fecRate23", 1),
          ("fecRate25", 9),
          ("fecRate34", 2),
          ("fecRate35", 6),
          ("fecRate45", 7),
          ("fecRate56", 3),
          ("fecRate78", 4),
          ("fecRate89", 5),
          ("fecRate910", 8),
          ("noInnerCode", 12))
    )


_DvbRcsFwdStartInnerFec_Type.__name__ = "Integer32"
_DvbRcsFwdStartInnerFec_Object = MibTableColumn
dvbRcsFwdStartInnerFec = _DvbRcsFwdStartInnerFec_Object(
    (1, 3, 6, 1, 2, 1, 10, 239, 1, 2, 1, 1, 1, 8),
    _DvbRcsFwdStartInnerFec_Type()
)
dvbRcsFwdStartInnerFec.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dvbRcsFwdStartInnerFec.setStatus("current")
_DvbRcsFwdStartRowStatus_Type = RowStatus
_DvbRcsFwdStartRowStatus_Object = MibTableColumn
dvbRcsFwdStartRowStatus = _DvbRcsFwdStartRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 10, 239, 1, 2, 1, 1, 1, 9),
    _DvbRcsFwdStartRowStatus_Type()
)
dvbRcsFwdStartRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dvbRcsFwdStartRowStatus.setStatus("current")
_DvbRcsFwdStatus_ObjectIdentity = ObjectIdentity
dvbRcsFwdStatus = _DvbRcsFwdStatus_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 239, 1, 2, 2)
)


class _DvbRcsFwdStatusPopId_Type(Unsigned32):
    """Custom type dvbRcsFwdStatusPopId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DvbRcsFwdStatusPopId_Type.__name__ = "Unsigned32"
_DvbRcsFwdStatusPopId_Object = MibScalar
dvbRcsFwdStatusPopId = _DvbRcsFwdStatusPopId_Object(
    (1, 3, 6, 1, 2, 1, 10, 239, 1, 2, 2, 1),
    _DvbRcsFwdStatusPopId_Type()
)
dvbRcsFwdStatusPopId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dvbRcsFwdStatusPopId.setStatus("current")
_DvbRcsFwdStatusTable_Object = MibTable
dvbRcsFwdStatusTable = _DvbRcsFwdStatusTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 239, 1, 2, 2, 2)
)
if mibBuilder.loadTexts:
    dvbRcsFwdStatusTable.setStatus("current")
_DvbRcsFwdStatusEntry_Object = MibTableRow
dvbRcsFwdStatusEntry = _DvbRcsFwdStatusEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 239, 1, 2, 2, 2, 1)
)
dvbRcsFwdStatusEntry.setIndexNames(
    (0, "DVB-RCS-MIB", "dvbRcsFwdStatusIndex"),
)
if mibBuilder.loadTexts:
    dvbRcsFwdStatusEntry.setStatus("current")


class _DvbRcsFwdStatusIndex_Type(Unsigned32):
    """Custom type dvbRcsFwdStatusIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_DvbRcsFwdStatusIndex_Type.__name__ = "Unsigned32"
_DvbRcsFwdStatusIndex_Object = MibTableColumn
dvbRcsFwdStatusIndex = _DvbRcsFwdStatusIndex_Object(
    (1, 3, 6, 1, 2, 1, 10, 239, 1, 2, 2, 2, 1, 1),
    _DvbRcsFwdStatusIndex_Type()
)
dvbRcsFwdStatusIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dvbRcsFwdStatusIndex.setStatus("current")


class _DvbRcsFwdStatusIfReference_Type(Unsigned32):
    """Custom type dvbRcsFwdStatusIfReference based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_DvbRcsFwdStatusIfReference_Type.__name__ = "Unsigned32"
_DvbRcsFwdStatusIfReference_Object = MibTableColumn
dvbRcsFwdStatusIfReference = _DvbRcsFwdStatusIfReference_Object(
    (1, 3, 6, 1, 2, 1, 10, 239, 1, 2, 2, 2, 1, 2),
    _DvbRcsFwdStatusIfReference_Type()
)
dvbRcsFwdStatusIfReference.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dvbRcsFwdStatusIfReference.setStatus("current")
_DvbRcsFwdStatusNetId_Type = Unsigned32
_DvbRcsFwdStatusNetId_Object = MibTableColumn
dvbRcsFwdStatusNetId = _DvbRcsFwdStatusNetId_Object(
    (1, 3, 6, 1, 2, 1, 10, 239, 1, 2, 2, 2, 1, 3),
    _DvbRcsFwdStatusNetId_Type()
)
dvbRcsFwdStatusNetId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dvbRcsFwdStatusNetId.setStatus("current")
_DvbRcsFwdStatusNetName_Type = SnmpAdminString
_DvbRcsFwdStatusNetName_Object = MibTableColumn
dvbRcsFwdStatusNetName = _DvbRcsFwdStatusNetName_Object(
    (1, 3, 6, 1, 2, 1, 10, 239, 1, 2, 2, 2, 1, 4),
    _DvbRcsFwdStatusNetName_Type()
)
dvbRcsFwdStatusNetName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dvbRcsFwdStatusNetName.setStatus("current")


class _DvbRcsFwdStatusFormat_Type(Integer32):
    """Custom type dvbRcsFwdStatusFormat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dvbs", 0),
          ("dvbs2acm", 2),
          ("dvbs2ccm", 1),
          ("reservedFormat", 3))
    )


_DvbRcsFwdStatusFormat_Type.__name__ = "Integer32"
_DvbRcsFwdStatusFormat_Object = MibTableColumn
dvbRcsFwdStatusFormat = _DvbRcsFwdStatusFormat_Object(
    (1, 3, 6, 1, 2, 1, 10, 239, 1, 2, 2, 2, 1, 5),
    _DvbRcsFwdStatusFormat_Type()
)
dvbRcsFwdStatusFormat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dvbRcsFwdStatusFormat.setStatus("current")
_DvbRcsFwdStatusFrequency_Type = Unsigned32
_DvbRcsFwdStatusFrequency_Object = MibTableColumn
dvbRcsFwdStatusFrequency = _DvbRcsFwdStatusFrequency_Object(
    (1, 3, 6, 1, 2, 1, 10, 239, 1, 2, 2, 2, 1, 6),
    _DvbRcsFwdStatusFrequency_Type()
)
dvbRcsFwdStatusFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dvbRcsFwdStatusFrequency.setStatus("current")
if mibBuilder.loadTexts:
    dvbRcsFwdStatusFrequency.setUnits("x100 kHz")


class _DvbRcsFwdStatusPolar_Type(Integer32):
    """Custom type dvbRcsFwdStatusPolar based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("circularLeft", 2),
          ("circularRight", 3),
          ("linearHorizontal", 0),
          ("linearVertical", 1))
    )


_DvbRcsFwdStatusPolar_Type.__name__ = "Integer32"
_DvbRcsFwdStatusPolar_Object = MibTableColumn
dvbRcsFwdStatusPolar = _DvbRcsFwdStatusPolar_Object(
    (1, 3, 6, 1, 2, 1, 10, 239, 1, 2, 2, 2, 1, 7),
    _DvbRcsFwdStatusPolar_Type()
)
dvbRcsFwdStatusPolar.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dvbRcsFwdStatusPolar.setStatus("current")


class _DvbRcsFwdStatusInnerFec_Type(Integer32):
    """Custom type dvbRcsFwdStatusInnerFec based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1,
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
              12)
        )
    )
    namedValues = NamedValues(
        *(("fecRate12", 0),
          ("fecRate13", 10),
          ("fecRate14", 11),
          ("fecRate23", 1),
          ("fecRate25", 9),
          ("fecRate34", 2),
          ("fecRate35", 6),
          ("fecRate45", 7),
          ("fecRate56", 3),
          ("fecRate78", 4),
          ("fecRate89", 5),
          ("fecRate910", 8),
          ("noInnerCode", 12),
          ("unknown", -1))
    )


_DvbRcsFwdStatusInnerFec_Type.__name__ = "Integer32"
_DvbRcsFwdStatusInnerFec_Object = MibTableColumn
dvbRcsFwdStatusInnerFec = _DvbRcsFwdStatusInnerFec_Object(
    (1, 3, 6, 1, 2, 1, 10, 239, 1, 2, 2, 2, 1, 8),
    _DvbRcsFwdStatusInnerFec_Type()
)
dvbRcsFwdStatusInnerFec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dvbRcsFwdStatusInnerFec.setStatus("current")
_DvbRcsFwdStatusSymbolRate_Type = Unsigned32
_DvbRcsFwdStatusSymbolRate_Object = MibTableColumn
dvbRcsFwdStatusSymbolRate = _DvbRcsFwdStatusSymbolRate_Object(
    (1, 3, 6, 1, 2, 1, 10, 239, 1, 2, 2, 2, 1, 9),
    _DvbRcsFwdStatusSymbolRate_Type()
)
dvbRcsFwdStatusSymbolRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dvbRcsFwdStatusSymbolRate.setStatus("current")
if mibBuilder.loadTexts:
    dvbRcsFwdStatusSymbolRate.setUnits("x100 symbols/s")


class _DvbRcsFwdStatusRolloff_Type(Integer32):
    """Custom type dvbRcsFwdStatusRolloff based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("rolloff020", 1),
          ("rolloff025", 2),
          ("rolloff035", 3),
          ("undefRolloff", 0))
    )


_DvbRcsFwdStatusRolloff_Type.__name__ = "Integer32"
_DvbRcsFwdStatusRolloff_Object = MibTableColumn
dvbRcsFwdStatusRolloff = _DvbRcsFwdStatusRolloff_Object(
    (1, 3, 6, 1, 2, 1, 10, 239, 1, 2, 2, 2, 1, 10),
    _DvbRcsFwdStatusRolloff_Type()
)
dvbRcsFwdStatusRolloff.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dvbRcsFwdStatusRolloff.setStatus("current")


class _DvbRcsFwdStatusModulation_Type(Integer32):
    """Custom type dvbRcsFwdStatusModulation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("m16APSK", 4),
          ("m32APSK", 5),
          ("m8PSK", 3),
          ("mBPSK", 1),
          ("mQPSK", 2),
          ("unknown", 0))
    )


_DvbRcsFwdStatusModulation_Type.__name__ = "Integer32"
_DvbRcsFwdStatusModulation_Object = MibTableColumn
dvbRcsFwdStatusModulation = _DvbRcsFwdStatusModulation_Object(
    (1, 3, 6, 1, 2, 1, 10, 239, 1, 2, 2, 2, 1, 11),
    _DvbRcsFwdStatusModulation_Type()
)
dvbRcsFwdStatusModulation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dvbRcsFwdStatusModulation.setStatus("current")


class _DvbRcsFwdStatusFecFrame_Type(Integer32):
    """Custom type dvbRcsFwdStatusFecFrame based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("longframe", 2),
          ("shortframe", 1),
          ("unknown", 0))
    )


_DvbRcsFwdStatusFecFrame_Type.__name__ = "Integer32"
_DvbRcsFwdStatusFecFrame_Object = MibTableColumn
dvbRcsFwdStatusFecFrame = _DvbRcsFwdStatusFecFrame_Object(
    (1, 3, 6, 1, 2, 1, 10, 239, 1, 2, 2, 2, 1, 12),
    _DvbRcsFwdStatusFecFrame_Type()
)
dvbRcsFwdStatusFecFrame.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dvbRcsFwdStatusFecFrame.setStatus("current")


class _DvbRcsFwdStatusPilot_Type(Integer32):
    """Custom type dvbRcsFwdStatusPilot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("pilotNotused", 1),
          ("pilotUsed", 2),
          ("unknown", 0))
    )


_DvbRcsFwdStatusPilot_Type.__name__ = "Integer32"
_DvbRcsFwdStatusPilot_Object = MibTableColumn
dvbRcsFwdStatusPilot = _DvbRcsFwdStatusPilot_Object(
    (1, 3, 6, 1, 2, 1, 10, 239, 1, 2, 2, 2, 1, 13),
    _DvbRcsFwdStatusPilot_Type()
)
dvbRcsFwdStatusPilot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dvbRcsFwdStatusPilot.setStatus("current")
_DvbRcsFwdStatusBer_Type = Integer32
_DvbRcsFwdStatusBer_Object = MibTableColumn
dvbRcsFwdStatusBer = _DvbRcsFwdStatusBer_Object(
    (1, 3, 6, 1, 2, 1, 10, 239, 1, 2, 2, 2, 1, 14),
    _DvbRcsFwdStatusBer_Type()
)
dvbRcsFwdStatusBer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dvbRcsFwdStatusBer.setStatus("current")
if mibBuilder.loadTexts:
    dvbRcsFwdStatusBer.setUnits("exponent of 10")
_DvbRcsFwdStatusCnr_Type = Integer32
_DvbRcsFwdStatusCnr_Object = MibTableColumn
dvbRcsFwdStatusCnr = _DvbRcsFwdStatusCnr_Object(
    (1, 3, 6, 1, 2, 1, 10, 239, 1, 2, 2, 2, 1, 15),
    _DvbRcsFwdStatusCnr_Type()
)
dvbRcsFwdStatusCnr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dvbRcsFwdStatusCnr.setStatus("current")
if mibBuilder.loadTexts:
    dvbRcsFwdStatusCnr.setUnits("0.1 dB")


class _DvbRcsFwdStatusRxPower_Type(Integer32):
    """Custom type dvbRcsFwdStatusRxPower based on Integer32"""
    defaultValue = -500


_DvbRcsFwdStatusRxPower_Object = MibTableColumn
dvbRcsFwdStatusRxPower = _DvbRcsFwdStatusRxPower_Object(
    (1, 3, 6, 1, 2, 1, 10, 239, 1, 2, 2, 2, 1, 16),
    _DvbRcsFwdStatusRxPower_Type()
)
dvbRcsFwdStatusRxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dvbRcsFwdStatusRxPower.setStatus("current")
if mibBuilder.loadTexts:
    dvbRcsFwdStatusRxPower.setUnits("0.1 dBm")
_DvbRcsRtnLink_ObjectIdentity = ObjectIdentity
dvbRcsRtnLink = _DvbRcsRtnLink_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 239, 1, 3)
)
_DvbRcsRtnConfig_ObjectIdentity = ObjectIdentity
dvbRcsRtnConfig = _DvbRcsRtnConfig_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 239, 1, 3, 1)
)
_DvbRcsRtnConfigMaxEirp_Type = Integer32
_DvbRcsRtnConfigMaxEirp_Object = MibScalar
dvbRcsRtnConfigMaxEirp = _DvbRcsRtnConfigMaxEirp_Object(
    (1, 3, 6, 1, 2, 1, 10, 239, 1, 3, 1, 1),
    _DvbRcsRtnConfigMaxEirp_Type()
)
dvbRcsRtnConfigMaxEirp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dvbRcsRtnConfigMaxEirp.setStatus("current")
if mibBuilder.loadTexts:
    dvbRcsRtnConfigMaxEirp.setUnits("x0.1 dBm")
_DvbRcsRtnConfigDefIfLevel_Type = Integer32
_DvbRcsRtnConfigDefIfLevel_Object = MibScalar
dvbRcsRtnConfigDefIfLevel = _DvbRcsRtnConfigDefIfLevel_Object(
    (1, 3, 6, 1, 2, 1, 10, 239, 1, 3, 1, 2),
    _DvbRcsRtnConfigDefIfLevel_Type()
)
dvbRcsRtnConfigDefIfLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dvbRcsRtnConfigDefIfLevel.setStatus("current")
if mibBuilder.loadTexts:
    dvbRcsRtnConfigDefIfLevel.setUnits("x0.1 dBm")
_DvbRcsRtnStatus_ObjectIdentity = ObjectIdentity
dvbRcsRtnStatus = _DvbRcsRtnStatus_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 239, 1, 3, 2)
)
_DvbRcsRtnStatusEbN0_Type = Integer32
_DvbRcsRtnStatusEbN0_Object = MibScalar
dvbRcsRtnStatusEbN0 = _DvbRcsRtnStatusEbN0_Object(
    (1, 3, 6, 1, 2, 1, 10, 239, 1, 3, 2, 1),
    _DvbRcsRtnStatusEbN0_Type()
)
dvbRcsRtnStatusEbN0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dvbRcsRtnStatusEbN0.setStatus("current")
if mibBuilder.loadTexts:
    dvbRcsRtnStatusEbN0.setUnits("x0.1 dB")


class _DvbRcsRtnStatusSFDuration_Type(Unsigned32):
    """Custom type dvbRcsRtnStatusSFDuration based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(250, 7500),
    )


_DvbRcsRtnStatusSFDuration_Type.__name__ = "Unsigned32"
_DvbRcsRtnStatusSFDuration_Object = MibScalar
dvbRcsRtnStatusSFDuration = _DvbRcsRtnStatusSFDuration_Object(
    (1, 3, 6, 1, 2, 1, 10, 239, 1, 3, 2, 2),
    _DvbRcsRtnStatusSFDuration_Type()
)
dvbRcsRtnStatusSFDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dvbRcsRtnStatusSFDuration.setStatus("current")
if mibBuilder.loadTexts:
    dvbRcsRtnStatusSFDuration.setUnits("0.1 ms")


class _DvbRcsRtnStatusPayloadUnit_Type(Integer32):
    """Custom type dvbRcsRtnStatusPayloadUnit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("unitATM", 0),
          ("unitMPEG", 1))
    )


_DvbRcsRtnStatusPayloadUnit_Type.__name__ = "Integer32"
_DvbRcsRtnStatusPayloadUnit_Object = MibScalar
dvbRcsRtnStatusPayloadUnit = _DvbRcsRtnStatusPayloadUnit_Object(
    (1, 3, 6, 1, 2, 1, 10, 239, 1, 3, 2, 3),
    _DvbRcsRtnStatusPayloadUnit_Type()
)
dvbRcsRtnStatusPayloadUnit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dvbRcsRtnStatusPayloadUnit.setStatus("current")
_DvbRcsConformance_ObjectIdentity = ObjectIdentity
dvbRcsConformance = _DvbRcsConformance_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 239, 2)
)
_DvbRcsRcstGroups_ObjectIdentity = ObjectIdentity
dvbRcsRcstGroups = _DvbRcsRcstGroups_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 239, 2, 1)
)
_DvbRcsRcstCompliances_ObjectIdentity = ObjectIdentity
dvbRcsRcstCompliances = _DvbRcsRcstCompliances_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 239, 2, 2)
)

# Managed Objects groups

dvbRcsRcstSystemGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 239, 2, 1, 1)
)
dvbRcsRcstSystemGroup.setObjects(
      *(("DVB-RCS-MIB", "dvbRcsSystemMibRevision"),
        ("DVB-RCS-MIB", "dvbRcsSystemSatLabsProfilesDeclaration"),
        ("DVB-RCS-MIB", "dvbRcsSystemSatLabsOptionsDeclaration"),
        ("DVB-RCS-MIB", "dvbRcsSystemSatLabsFeaturesDeclaration"),
        ("DVB-RCS-MIB", "dvbRcsSystemLocation"),
        ("DVB-RCS-MIB", "dvbRcsSystemOduAntennaSize"),
        ("DVB-RCS-MIB", "dvbRcsSystemOduAntennaGain"),
        ("DVB-RCS-MIB", "dvbRcsSystemOduSspa"),
        ("DVB-RCS-MIB", "dvbRcsSystemOduTxType"),
        ("DVB-RCS-MIB", "dvbRcsSystemOduRxType"),
        ("DVB-RCS-MIB", "dvbRcsSystemOduRxBand"),
        ("DVB-RCS-MIB", "dvbRcsSystemOduRxLO"),
        ("DVB-RCS-MIB", "dvbRcsSystemOduTxLO"),
        ("DVB-RCS-MIB", "dvbRcsTcpPep"),
        ("DVB-RCS-MIB", "dvbRcsHttpPep"))
)
if mibBuilder.loadTexts:
    dvbRcsRcstSystemGroup.setStatus("current")

dvbRcsRcstNetworkGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 239, 2, 1, 2)
)
dvbRcsRcstNetworkGroup.setObjects(
      *(("DVB-RCS-MIB", "dvbRcsNetworkOamInetAddressType"),
        ("DVB-RCS-MIB", "dvbRcsNetworkOamInetAddress"),
        ("DVB-RCS-MIB", "dvbRcsNetworkOamInetAddressPrefixLength"),
        ("DVB-RCS-MIB", "dvbRcsNetworkLanInetAddressType"),
        ("DVB-RCS-MIB", "dvbRcsNetworkLanInetAddress"),
        ("DVB-RCS-MIB", "dvbRcsNetworkLanInetAddressPrefixLength"),
        ("DVB-RCS-MIB", "dvbRcsNetworkConfigFileDownloadUrl"),
        ("DVB-RCS-MIB", "dvbRcsNetworkConfigFileUploadUrl"),
        ("DVB-RCS-MIB", "dvbRcsNetworkLogFileUploadUrl"))
)
if mibBuilder.loadTexts:
    dvbRcsRcstNetworkGroup.setStatus("current")

dvbRcsRcstExtNetworkGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 239, 2, 1, 3)
)
dvbRcsRcstExtNetworkGroup.setObjects(
      *(("DVB-RCS-MIB", "dvbRcsNetworkOamInetAddressAssign"),
        ("DVB-RCS-MIB", "dvbRcsNetworkAirInterfaceDefaultGatewayInetAddressType"),
        ("DVB-RCS-MIB", "dvbRcsNetworkAirInterfaceDefaultGatewayInetAddress"),
        ("DVB-RCS-MIB", "dvbRcsNetworkAirInterfaceDefaultGatewayInetAddressPrefixLength"),
        ("DVB-RCS-MIB", "dvbRcsNetworkNccMgtInetAddressType"),
        ("DVB-RCS-MIB", "dvbRcsNetworkNccMgtInetAddress"),
        ("DVB-RCS-MIB", "dvbRcsNetworkNccMgtInetAddressPrefixLength"))
)
if mibBuilder.loadTexts:
    dvbRcsRcstExtNetworkGroup.setStatus("current")

dvbRcsRcstDnsGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 239, 2, 1, 4)
)
dvbRcsRcstDnsGroup.setObjects(
      *(("DVB-RCS-MIB", "dvbRcsPrimaryDnsServerInetAddressType"),
        ("DVB-RCS-MIB", "dvbRcsPrimaryDnsServerInetAddress"),
        ("DVB-RCS-MIB", "dvbRcsPrimaryDnsServerInetAddressPrefixLength"),
        ("DVB-RCS-MIB", "dvbRcsSecondaryDnsServerInetAddressType"),
        ("DVB-RCS-MIB", "dvbRcsSecondaryDnsServerInetAddress"),
        ("DVB-RCS-MIB", "dvbRcsSecondaryDnsServerInetAddressPrefixLength"))
)
if mibBuilder.loadTexts:
    dvbRcsRcstDnsGroup.setStatus("current")

dvbRcsRcstInstallGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 239, 2, 1, 5)
)
dvbRcsRcstInstallGroup.setObjects(
      *(("DVB-RCS-MIB", "dvbRcsInstallAntennaAlignmentState"),
        ("DVB-RCS-MIB", "dvbRcsInstallCwFrequency"),
        ("DVB-RCS-MIB", "dvbRcsInstallCwMaxDuration"),
        ("DVB-RCS-MIB", "dvbRcsInstallCwPower"),
        ("DVB-RCS-MIB", "dvbRcsInstallCoPolReading"),
        ("DVB-RCS-MIB", "dvbRcsInstallXPolReading"),
        ("DVB-RCS-MIB", "dvbRcsInstallCoPolTarget"),
        ("DVB-RCS-MIB", "dvbRcsInstallXPolTarget"),
        ("DVB-RCS-MIB", "dvbRcsInstallStandByDuration"),
        ("DVB-RCS-MIB", "dvbRcsInstallTargetEsN0"))
)
if mibBuilder.loadTexts:
    dvbRcsRcstInstallGroup.setStatus("current")

dvbRcsRcstExtInstallGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 239, 2, 1, 6)
)
dvbRcsRcstExtInstallGroup.setObjects(
      *(("DVB-RCS-MIB", "dvbRcsNetworkInstallLogFileDownloadUrl"),
        ("DVB-RCS-MIB", "dvbRcsNetworkInstallLogFileUploadUrl"))
)
if mibBuilder.loadTexts:
    dvbRcsRcstExtInstallGroup.setStatus("current")

dvbRcsRcstQosGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 239, 2, 1, 7)
)
dvbRcsRcstQosGroup.setObjects(
      *(("DVB-RCS-MIB", "dvbRcsPktClassDscpLow"),
        ("DVB-RCS-MIB", "dvbRcsPktClassDscpHigh"),
        ("DVB-RCS-MIB", "dvbRcsPktClassDscpMarkValue"),
        ("DVB-RCS-MIB", "dvbRcsPktClassPhbAssociation"),
        ("DVB-RCS-MIB", "dvbRcsPktClassRowStatus"),
        ("DVB-RCS-MIB", "dvbRcsPhbName"),
        ("DVB-RCS-MIB", "dvbRcsPhbRequestClassAssociation"),
        ("DVB-RCS-MIB", "dvbRcsPhbMappingRowStatus"),
        ("DVB-RCS-MIB", "dvbRcsRequestClassName"),
        ("DVB-RCS-MIB", "dvbRcsRequestClassChanId"),
        ("DVB-RCS-MIB", "dvbRcsRequestClassVccVpi"),
        ("DVB-RCS-MIB", "dvbRcsRequestClassVccVci"),
        ("DVB-RCS-MIB", "dvbRcsRequestClassCra"),
        ("DVB-RCS-MIB", "dvbRcsRequestClassRbdcMax"),
        ("DVB-RCS-MIB", "dvbRcsRequestClassRbdcTimeout"),
        ("DVB-RCS-MIB", "dvbRcsRequestClassVbdcMax"),
        ("DVB-RCS-MIB", "dvbRcsRequestClassVbdcTimeout"),
        ("DVB-RCS-MIB", "dvbRcsRequestClassVbdcMaxBackLog"),
        ("DVB-RCS-MIB", "dvbRcsRequestClassRowStatus"))
)
if mibBuilder.loadTexts:
    dvbRcsRcstQosGroup.setStatus("current")

dvbRcsRcstEnhancedClassifierGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 239, 2, 1, 8)
)
dvbRcsRcstEnhancedClassifierGroup.setObjects(
      *(("DVB-RCS-MIB", "dvbRcsPktClassIpProtocol"),
        ("DVB-RCS-MIB", "dvbRcsPktClassSrcInetAddressType"),
        ("DVB-RCS-MIB", "dvbRcsPktClassSrcInetAddress"),
        ("DVB-RCS-MIB", "dvbRcsPktClassSrcInetAddressPrefixLength"),
        ("DVB-RCS-MIB", "dvbRcsPktClassDstInetAddressType"),
        ("DVB-RCS-MIB", "dvbRcsPktClassDstInetAddress"),
        ("DVB-RCS-MIB", "dvbRcsPktClassDstInetAddressPrefixLength"),
        ("DVB-RCS-MIB", "dvbRcsPktClassSrcPortLow"),
        ("DVB-RCS-MIB", "dvbRcsPktClassSrcPortHigh"),
        ("DVB-RCS-MIB", "dvbRcsPktClassDstPortLow"),
        ("DVB-RCS-MIB", "dvbRcsPktClassDstPortHigh"),
        ("DVB-RCS-MIB", "dvbRcsPktClassVlanUserPri"))
)
if mibBuilder.loadTexts:
    dvbRcsRcstEnhancedClassifierGroup.setStatus("current")

dvbRcsRcstMpegQosGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 239, 2, 1, 9)
)
dvbRcsRcstMpegQosGroup.setObjects(
      *(("DVB-RCS-MIB", "dvbRcsRequestClassPidPoolReference"),
        ("DVB-RCS-MIB", "dvbRcsPidValue"),
        ("DVB-RCS-MIB", "dvbRcsPidPoolRowStatus"))
)
if mibBuilder.loadTexts:
    dvbRcsRcstMpegQosGroup.setStatus("current")

dvbRcsRcstGlobalQosGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 239, 2, 1, 10)
)
dvbRcsRcstGlobalQosGroup.setObjects(
      *(("DVB-RCS-MIB", "dvbRcsQosGlobalRbdcMax"),
        ("DVB-RCS-MIB", "dvbRcsQosGlobalVbdcMax"),
        ("DVB-RCS-MIB", "dvbRcsQosGlobalVbdcMaxBackLog"))
)
if mibBuilder.loadTexts:
    dvbRcsRcstGlobalQosGroup.setStatus("current")

dvbRcsRcstStrictQosGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 239, 2, 1, 11)
)
dvbRcsRcstStrictQosGroup.setObjects(
    ("DVB-RCS-MIB", "dvbRcsQosChannelIdStrictDispatching")
)
if mibBuilder.loadTexts:
    dvbRcsRcstStrictQosGroup.setStatus("current")

dvbRcsRcstControlGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 239, 2, 1, 12)
)
dvbRcsRcstControlGroup.setObjects(
      *(("DVB-RCS-MIB", "dvbRcsCtrlRebootCommand"),
        ("DVB-RCS-MIB", "dvbRcsCtrlUserTrafficDisable"),
        ("DVB-RCS-MIB", "dvbRcsCtrlCwEnable"),
        ("DVB-RCS-MIB", "dvbRcsCtrlDownloadFileCommand"),
        ("DVB-RCS-MIB", "dvbRcsCtrlUploadFileCommand"),
        ("DVB-RCS-MIB", "dvbRcsCtrlActivateConfigFileCommand"),
        ("DVB-RCS-MIB", "dvbRcsCtrlRcstRxReacquire"))
)
if mibBuilder.loadTexts:
    dvbRcsRcstControlGroup.setStatus("current")

dvbRcsRcstExtControlGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 239, 2, 1, 13)
)
dvbRcsRcstExtControlGroup.setObjects(
      *(("DVB-RCS-MIB", "dvbRcsCtrlRcstTxDisable"),
        ("DVB-RCS-MIB", "dvbRcsCtrlOduTxReferenceEnable"),
        ("DVB-RCS-MIB", "dvbRcsCtrlOduTxDCEnable"),
        ("DVB-RCS-MIB", "dvbRcsCtrlOduRxDCEnable"),
        ("DVB-RCS-MIB", "dvbRcsCtrlRcstLogonCommand"),
        ("DVB-RCS-MIB", "dvbRcsCtrlRcstLogoffCommand"))
)
if mibBuilder.loadTexts:
    dvbRcsRcstExtControlGroup.setStatus("current")

dvbRcsRcstStateGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 239, 2, 1, 14)
)
dvbRcsRcstStateGroup.setObjects(
      *(("DVB-RCS-MIB", "dvbRcsRcstMode"),
        ("DVB-RCS-MIB", "dvbRcsRcstFaultStatus"),
        ("DVB-RCS-MIB", "dvbRcsRcstFwdLinkStatus"),
        ("DVB-RCS-MIB", "dvbRcsRcstLogUpdated"),
        ("DVB-RCS-MIB", "dvbRcsRcstCurrentSoftwareVersion"),
        ("DVB-RCS-MIB", "dvbRcsRcstAlternateSoftwareVersion"),
        ("DVB-RCS-MIB", "dvbRcsRcstActivatedConfigFileVersion"),
        ("DVB-RCS-MIB", "dvbRcsRcstDownloadedConfigFileVersion"))
)
if mibBuilder.loadTexts:
    dvbRcsRcstStateGroup.setStatus("current")

dvbRcsFwdConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 239, 2, 1, 15)
)
dvbRcsFwdConfigGroup.setObjects(
      *(("DVB-RCS-MIB", "dvbRcsFwdStartPopId"),
        ("DVB-RCS-MIB", "dvbRcsFwdStartFrequency"),
        ("DVB-RCS-MIB", "dvbRcsFwdStartPolar"),
        ("DVB-RCS-MIB", "dvbRcsFwdStartFormat"),
        ("DVB-RCS-MIB", "dvbRcsFwdStartRolloff"),
        ("DVB-RCS-MIB", "dvbRcsFwdStartSymbolRate"),
        ("DVB-RCS-MIB", "dvbRcsFwdStartInnerFec"),
        ("DVB-RCS-MIB", "dvbRcsFwdStartRowStatus"))
)
if mibBuilder.loadTexts:
    dvbRcsFwdConfigGroup.setStatus("current")

dvbRcsFwdStatusGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 239, 2, 1, 16)
)
dvbRcsFwdStatusGroup.setObjects(
      *(("DVB-RCS-MIB", "dvbRcsFwdStatusPopId"),
        ("DVB-RCS-MIB", "dvbRcsFwdStatusIfReference"),
        ("DVB-RCS-MIB", "dvbRcsFwdStatusNetId"),
        ("DVB-RCS-MIB", "dvbRcsFwdStatusNetName"),
        ("DVB-RCS-MIB", "dvbRcsFwdStatusFormat"),
        ("DVB-RCS-MIB", "dvbRcsFwdStatusFrequency"),
        ("DVB-RCS-MIB", "dvbRcsFwdStatusPolar"),
        ("DVB-RCS-MIB", "dvbRcsFwdStatusInnerFec"),
        ("DVB-RCS-MIB", "dvbRcsFwdStatusSymbolRate"),
        ("DVB-RCS-MIB", "dvbRcsFwdStatusRolloff"),
        ("DVB-RCS-MIB", "dvbRcsFwdStatusModulation"),
        ("DVB-RCS-MIB", "dvbRcsFwdStatusFecFrame"),
        ("DVB-RCS-MIB", "dvbRcsFwdStatusPilot"),
        ("DVB-RCS-MIB", "dvbRcsFwdStatusBer"),
        ("DVB-RCS-MIB", "dvbRcsFwdStatusCnr"),
        ("DVB-RCS-MIB", "dvbRcsFwdStatusRxPower"))
)
if mibBuilder.loadTexts:
    dvbRcsFwdStatusGroup.setStatus("current")

dvbRcsRtnConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 239, 2, 1, 17)
)
dvbRcsRtnConfigGroup.setObjects(
    ("DVB-RCS-MIB", "dvbRcsRtnConfigDefIfLevel")
)
if mibBuilder.loadTexts:
    dvbRcsRtnConfigGroup.setStatus("current")

dvbRcsRtnExtConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 239, 2, 1, 18)
)
dvbRcsRtnExtConfigGroup.setObjects(
    ("DVB-RCS-MIB", "dvbRcsRtnConfigMaxEirp")
)
if mibBuilder.loadTexts:
    dvbRcsRtnExtConfigGroup.setStatus("current")

dvbRcsRtnStatusGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 239, 2, 1, 19)
)
dvbRcsRtnStatusGroup.setObjects(
    ("DVB-RCS-MIB", "dvbRcsRtnStatusPayloadUnit")
)
if mibBuilder.loadTexts:
    dvbRcsRtnStatusGroup.setStatus("current")

dvbRcsRtnExtStatusGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 239, 2, 1, 20)
)
dvbRcsRtnExtStatusGroup.setObjects(
      *(("DVB-RCS-MIB", "dvbRcsRcstRtnLinkStatus"),
        ("DVB-RCS-MIB", "dvbRcsRtnStatusEbN0"),
        ("DVB-RCS-MIB", "dvbRcsRtnStatusSFDuration"))
)
if mibBuilder.loadTexts:
    dvbRcsRtnExtStatusGroup.setStatus("current")

dvbRcsRcstOduListGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 239, 2, 1, 21)
)
dvbRcsRcstOduListGroup.setObjects(
      *(("DVB-RCS-MIB", "dvbRcsOduTxTypeDescription"),
        ("DVB-RCS-MIB", "dvbRcsOduTxType"),
        ("DVB-RCS-MIB", "dvbRcsOduRxTypeDescription"),
        ("DVB-RCS-MIB", "dvbRcsOduRxType"),
        ("DVB-RCS-MIB", "dvbRcsOduAntennaTypeDescription"),
        ("DVB-RCS-MIB", "dvbRcsOduAntennaType"))
)
if mibBuilder.loadTexts:
    dvbRcsRcstOduListGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

dvbRcsRcstCompliance1 = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 10, 239, 2, 2, 1)
)
if mibBuilder.loadTexts:
    dvbRcsRcstCompliance1.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DVB-RCS-MIB",
    **{"DvbRcsSatLabsProfileMap": DvbRcsSatLabsProfileMap,
       "DvbRcsSatLabsOptionMap": DvbRcsSatLabsOptionMap,
       "DvbRcsSatLabsFeatureMap": DvbRcsSatLabsFeatureMap,
       "dvbRcsMib": dvbRcsMib,
       "dvbRcsMibObjects": dvbRcsMibObjects,
       "dvbRcsRcst": dvbRcsRcst,
       "dvbRcsRcstSystem": dvbRcsRcstSystem,
       "dvbRcsSystemMibRevision": dvbRcsSystemMibRevision,
       "dvbRcsSystemSatLabsProfilesDeclaration": dvbRcsSystemSatLabsProfilesDeclaration,
       "dvbRcsSystemSatLabsOptionsDeclaration": dvbRcsSystemSatLabsOptionsDeclaration,
       "dvbRcsSystemSatLabsFeaturesDeclaration": dvbRcsSystemSatLabsFeaturesDeclaration,
       "dvbRcsSystemLocation": dvbRcsSystemLocation,
       "dvbRcsSystemOduAntennaSize": dvbRcsSystemOduAntennaSize,
       "dvbRcsSystemOduAntennaGain": dvbRcsSystemOduAntennaGain,
       "dvbRcsSystemOduSspa": dvbRcsSystemOduSspa,
       "dvbRcsSystemOduTxType": dvbRcsSystemOduTxType,
       "dvbRcsSystemOduRxType": dvbRcsSystemOduRxType,
       "dvbRcsSystemOduRxBand": dvbRcsSystemOduRxBand,
       "dvbRcsSystemOduRxLO": dvbRcsSystemOduRxLO,
       "dvbRcsSystemOduTxLO": dvbRcsSystemOduTxLO,
       "dvbRcsSystemIduPep": dvbRcsSystemIduPep,
       "dvbRcsTcpPep": dvbRcsTcpPep,
       "dvbRcsHttpPep": dvbRcsHttpPep,
       "dvbRcsOduTx": dvbRcsOduTx,
       "dvbRcsOduTxTypeTable": dvbRcsOduTxTypeTable,
       "dvbRcsOduTxTypeEntry": dvbRcsOduTxTypeEntry,
       "dvbRcsOduTxTypeIndex": dvbRcsOduTxTypeIndex,
       "dvbRcsOduTxTypeDescription": dvbRcsOduTxTypeDescription,
       "dvbRcsOduTxType": dvbRcsOduTxType,
       "dvbRcsOduRx": dvbRcsOduRx,
       "dvbRcsOduRxTypeTable": dvbRcsOduRxTypeTable,
       "dvbRcsOduRxTypeEntry": dvbRcsOduRxTypeEntry,
       "dvbRcsOduRxTypeIndex": dvbRcsOduRxTypeIndex,
       "dvbRcsOduRxTypeDescription": dvbRcsOduRxTypeDescription,
       "dvbRcsOduRxType": dvbRcsOduRxType,
       "dvbRcsOduAntenna": dvbRcsOduAntenna,
       "dvbRcsOduAntennaTypeTable": dvbRcsOduAntennaTypeTable,
       "dvbRcsOduAntennaTypeEntry": dvbRcsOduAntennaTypeEntry,
       "dvbRcsOduAntennaTypeIndex": dvbRcsOduAntennaTypeIndex,
       "dvbRcsOduAntennaTypeDescription": dvbRcsOduAntennaTypeDescription,
       "dvbRcsOduAntennaType": dvbRcsOduAntennaType,
       "dvbRcsRcstNetwork": dvbRcsRcstNetwork,
       "dvbRcsNetworkOamInetAddressType": dvbRcsNetworkOamInetAddressType,
       "dvbRcsNetworkOamInetAddress": dvbRcsNetworkOamInetAddress,
       "dvbRcsNetworkOamInetAddressPrefixLength": dvbRcsNetworkOamInetAddressPrefixLength,
       "dvbRcsNetworkOamInetAddressAssign": dvbRcsNetworkOamInetAddressAssign,
       "dvbRcsNetworkLanInetAddressType": dvbRcsNetworkLanInetAddressType,
       "dvbRcsNetworkLanInetAddress": dvbRcsNetworkLanInetAddress,
       "dvbRcsNetworkLanInetAddressPrefixLength": dvbRcsNetworkLanInetAddressPrefixLength,
       "dvbRcsNetworkAirInterfaceDefaultGatewayInetAddressType": dvbRcsNetworkAirInterfaceDefaultGatewayInetAddressType,
       "dvbRcsNetworkAirInterfaceDefaultGatewayInetAddress": dvbRcsNetworkAirInterfaceDefaultGatewayInetAddress,
       "dvbRcsNetworkAirInterfaceDefaultGatewayInetAddressPrefixLength": dvbRcsNetworkAirInterfaceDefaultGatewayInetAddressPrefixLength,
       "dvbRcsNetworkDnsServers": dvbRcsNetworkDnsServers,
       "dvbRcsPrimaryDnsServerInetAddressType": dvbRcsPrimaryDnsServerInetAddressType,
       "dvbRcsPrimaryDnsServerInetAddress": dvbRcsPrimaryDnsServerInetAddress,
       "dvbRcsPrimaryDnsServerInetAddressPrefixLength": dvbRcsPrimaryDnsServerInetAddressPrefixLength,
       "dvbRcsSecondaryDnsServerInetAddressType": dvbRcsSecondaryDnsServerInetAddressType,
       "dvbRcsSecondaryDnsServerInetAddress": dvbRcsSecondaryDnsServerInetAddress,
       "dvbRcsSecondaryDnsServerInetAddressPrefixLength": dvbRcsSecondaryDnsServerInetAddressPrefixLength,
       "dvbRcsNetworkNccMgtInetAddressType": dvbRcsNetworkNccMgtInetAddressType,
       "dvbRcsNetworkNccMgtInetAddress": dvbRcsNetworkNccMgtInetAddress,
       "dvbRcsNetworkNccMgtInetAddressPrefixLength": dvbRcsNetworkNccMgtInetAddressPrefixLength,
       "dvbRcsNetworkConfigFileDownloadUrl": dvbRcsNetworkConfigFileDownloadUrl,
       "dvbRcsNetworkInstallLogFileDownloadUrl": dvbRcsNetworkInstallLogFileDownloadUrl,
       "dvbRcsNetworkConfigFileUploadUrl": dvbRcsNetworkConfigFileUploadUrl,
       "dvbRcsNetworkLogFileUploadUrl": dvbRcsNetworkLogFileUploadUrl,
       "dvbRcsNetworkInstallLogFileUploadUrl": dvbRcsNetworkInstallLogFileUploadUrl,
       "dvbRcsRcstInstall": dvbRcsRcstInstall,
       "dvbRcsInstallAntennaAlignmentState": dvbRcsInstallAntennaAlignmentState,
       "dvbRcsInstallCwFrequency": dvbRcsInstallCwFrequency,
       "dvbRcsInstallCwMaxDuration": dvbRcsInstallCwMaxDuration,
       "dvbRcsInstallCwPower": dvbRcsInstallCwPower,
       "dvbRcsInstallCoPolReading": dvbRcsInstallCoPolReading,
       "dvbRcsInstallXPolReading": dvbRcsInstallXPolReading,
       "dvbRcsInstallCoPolTarget": dvbRcsInstallCoPolTarget,
       "dvbRcsInstallXPolTarget": dvbRcsInstallXPolTarget,
       "dvbRcsInstallStandByDuration": dvbRcsInstallStandByDuration,
       "dvbRcsInstallTargetEsN0": dvbRcsInstallTargetEsN0,
       "dvbRcsRcstQos": dvbRcsRcstQos,
       "dvbRcsPktClassTable": dvbRcsPktClassTable,
       "dvbRcsPktClassEntry": dvbRcsPktClassEntry,
       "dvbRcsPktClassIndex": dvbRcsPktClassIndex,
       "dvbRcsPktClassDscpLow": dvbRcsPktClassDscpLow,
       "dvbRcsPktClassDscpHigh": dvbRcsPktClassDscpHigh,
       "dvbRcsPktClassDscpMarkValue": dvbRcsPktClassDscpMarkValue,
       "dvbRcsPktClassIpProtocol": dvbRcsPktClassIpProtocol,
       "dvbRcsPktClassSrcInetAddressType": dvbRcsPktClassSrcInetAddressType,
       "dvbRcsPktClassSrcInetAddress": dvbRcsPktClassSrcInetAddress,
       "dvbRcsPktClassSrcInetAddressPrefixLength": dvbRcsPktClassSrcInetAddressPrefixLength,
       "dvbRcsPktClassDstInetAddressType": dvbRcsPktClassDstInetAddressType,
       "dvbRcsPktClassDstInetAddress": dvbRcsPktClassDstInetAddress,
       "dvbRcsPktClassDstInetAddressPrefixLength": dvbRcsPktClassDstInetAddressPrefixLength,
       "dvbRcsPktClassSrcPortLow": dvbRcsPktClassSrcPortLow,
       "dvbRcsPktClassSrcPortHigh": dvbRcsPktClassSrcPortHigh,
       "dvbRcsPktClassDstPortLow": dvbRcsPktClassDstPortLow,
       "dvbRcsPktClassDstPortHigh": dvbRcsPktClassDstPortHigh,
       "dvbRcsPktClassVlanUserPri": dvbRcsPktClassVlanUserPri,
       "dvbRcsPktClassPhbAssociation": dvbRcsPktClassPhbAssociation,
       "dvbRcsPktClassRowStatus": dvbRcsPktClassRowStatus,
       "dvbRcsPhbMappingTable": dvbRcsPhbMappingTable,
       "dvbRcsPhbMappingEntry": dvbRcsPhbMappingEntry,
       "dvbRcsPhbIdentifier": dvbRcsPhbIdentifier,
       "dvbRcsPhbName": dvbRcsPhbName,
       "dvbRcsPhbRequestClassAssociation": dvbRcsPhbRequestClassAssociation,
       "dvbRcsPhbMappingRowStatus": dvbRcsPhbMappingRowStatus,
       "dvbRcsRequestClassTable": dvbRcsRequestClassTable,
       "dvbRcsRequestClassEntry": dvbRcsRequestClassEntry,
       "dvbRcsRequestClassIndex": dvbRcsRequestClassIndex,
       "dvbRcsRequestClassName": dvbRcsRequestClassName,
       "dvbRcsRequestClassChanId": dvbRcsRequestClassChanId,
       "dvbRcsRequestClassVccVpi": dvbRcsRequestClassVccVpi,
       "dvbRcsRequestClassVccVci": dvbRcsRequestClassVccVci,
       "dvbRcsRequestClassPidPoolReference": dvbRcsRequestClassPidPoolReference,
       "dvbRcsRequestClassCra": dvbRcsRequestClassCra,
       "dvbRcsRequestClassRbdcMax": dvbRcsRequestClassRbdcMax,
       "dvbRcsRequestClassRbdcTimeout": dvbRcsRequestClassRbdcTimeout,
       "dvbRcsRequestClassVbdcMax": dvbRcsRequestClassVbdcMax,
       "dvbRcsRequestClassVbdcTimeout": dvbRcsRequestClassVbdcTimeout,
       "dvbRcsRequestClassVbdcMaxBackLog": dvbRcsRequestClassVbdcMaxBackLog,
       "dvbRcsRequestClassRowStatus": dvbRcsRequestClassRowStatus,
       "dvbRcsPidPoolTable": dvbRcsPidPoolTable,
       "dvbRcsPidPoolEntry": dvbRcsPidPoolEntry,
       "dvbRcsPidPoolIndex": dvbRcsPidPoolIndex,
       "dvbRcsPidIndex": dvbRcsPidIndex,
       "dvbRcsPidValue": dvbRcsPidValue,
       "dvbRcsPidPoolRowStatus": dvbRcsPidPoolRowStatus,
       "dvbRcsQosGlobalRbdcMax": dvbRcsQosGlobalRbdcMax,
       "dvbRcsQosGlobalVbdcMax": dvbRcsQosGlobalVbdcMax,
       "dvbRcsQosGlobalVbdcMaxBackLog": dvbRcsQosGlobalVbdcMaxBackLog,
       "dvbRcsQosChannelIdStrictDispatching": dvbRcsQosChannelIdStrictDispatching,
       "dvbRcsRcstControl": dvbRcsRcstControl,
       "dvbRcsCtrlRebootCommand": dvbRcsCtrlRebootCommand,
       "dvbRcsCtrlRcstTxDisable": dvbRcsCtrlRcstTxDisable,
       "dvbRcsCtrlUserTrafficDisable": dvbRcsCtrlUserTrafficDisable,
       "dvbRcsCtrlCwEnable": dvbRcsCtrlCwEnable,
       "dvbRcsCtrlOduTxReferenceEnable": dvbRcsCtrlOduTxReferenceEnable,
       "dvbRcsCtrlOduTxDCEnable": dvbRcsCtrlOduTxDCEnable,
       "dvbRcsCtrlOduRxDCEnable": dvbRcsCtrlOduRxDCEnable,
       "dvbRcsCtrlDownloadFileCommand": dvbRcsCtrlDownloadFileCommand,
       "dvbRcsCtrlUploadFileCommand": dvbRcsCtrlUploadFileCommand,
       "dvbRcsCtrlActivateConfigFileCommand": dvbRcsCtrlActivateConfigFileCommand,
       "dvbRcsCtrlRcstLogonCommand": dvbRcsCtrlRcstLogonCommand,
       "dvbRcsCtrlRcstLogoffCommand": dvbRcsCtrlRcstLogoffCommand,
       "dvbRcsCtrlRcstRxReacquire": dvbRcsCtrlRcstRxReacquire,
       "dvbRcsRcstState": dvbRcsRcstState,
       "dvbRcsRcstMode": dvbRcsRcstMode,
       "dvbRcsRcstFaultStatus": dvbRcsRcstFaultStatus,
       "dvbRcsRcstFwdLinkStatus": dvbRcsRcstFwdLinkStatus,
       "dvbRcsRcstRtnLinkStatus": dvbRcsRcstRtnLinkStatus,
       "dvbRcsRcstLogUpdated": dvbRcsRcstLogUpdated,
       "dvbRcsRcstCurrentSoftwareVersion": dvbRcsRcstCurrentSoftwareVersion,
       "dvbRcsRcstAlternateSoftwareVersion": dvbRcsRcstAlternateSoftwareVersion,
       "dvbRcsRcstActivatedConfigFileVersion": dvbRcsRcstActivatedConfigFileVersion,
       "dvbRcsRcstDownloadedConfigFileVersion": dvbRcsRcstDownloadedConfigFileVersion,
       "dvbRcsFwdLink": dvbRcsFwdLink,
       "dvbRcsFwdConfig": dvbRcsFwdConfig,
       "dvbRcsFwdStartTable": dvbRcsFwdStartTable,
       "dvbRcsFwdStartEntry": dvbRcsFwdStartEntry,
       "dvbRcsFwdStartIndex": dvbRcsFwdStartIndex,
       "dvbRcsFwdStartPopId": dvbRcsFwdStartPopId,
       "dvbRcsFwdStartFrequency": dvbRcsFwdStartFrequency,
       "dvbRcsFwdStartPolar": dvbRcsFwdStartPolar,
       "dvbRcsFwdStartFormat": dvbRcsFwdStartFormat,
       "dvbRcsFwdStartRolloff": dvbRcsFwdStartRolloff,
       "dvbRcsFwdStartSymbolRate": dvbRcsFwdStartSymbolRate,
       "dvbRcsFwdStartInnerFec": dvbRcsFwdStartInnerFec,
       "dvbRcsFwdStartRowStatus": dvbRcsFwdStartRowStatus,
       "dvbRcsFwdStatus": dvbRcsFwdStatus,
       "dvbRcsFwdStatusPopId": dvbRcsFwdStatusPopId,
       "dvbRcsFwdStatusTable": dvbRcsFwdStatusTable,
       "dvbRcsFwdStatusEntry": dvbRcsFwdStatusEntry,
       "dvbRcsFwdStatusIndex": dvbRcsFwdStatusIndex,
       "dvbRcsFwdStatusIfReference": dvbRcsFwdStatusIfReference,
       "dvbRcsFwdStatusNetId": dvbRcsFwdStatusNetId,
       "dvbRcsFwdStatusNetName": dvbRcsFwdStatusNetName,
       "dvbRcsFwdStatusFormat": dvbRcsFwdStatusFormat,
       "dvbRcsFwdStatusFrequency": dvbRcsFwdStatusFrequency,
       "dvbRcsFwdStatusPolar": dvbRcsFwdStatusPolar,
       "dvbRcsFwdStatusInnerFec": dvbRcsFwdStatusInnerFec,
       "dvbRcsFwdStatusSymbolRate": dvbRcsFwdStatusSymbolRate,
       "dvbRcsFwdStatusRolloff": dvbRcsFwdStatusRolloff,
       "dvbRcsFwdStatusModulation": dvbRcsFwdStatusModulation,
       "dvbRcsFwdStatusFecFrame": dvbRcsFwdStatusFecFrame,
       "dvbRcsFwdStatusPilot": dvbRcsFwdStatusPilot,
       "dvbRcsFwdStatusBer": dvbRcsFwdStatusBer,
       "dvbRcsFwdStatusCnr": dvbRcsFwdStatusCnr,
       "dvbRcsFwdStatusRxPower": dvbRcsFwdStatusRxPower,
       "dvbRcsRtnLink": dvbRcsRtnLink,
       "dvbRcsRtnConfig": dvbRcsRtnConfig,
       "dvbRcsRtnConfigMaxEirp": dvbRcsRtnConfigMaxEirp,
       "dvbRcsRtnConfigDefIfLevel": dvbRcsRtnConfigDefIfLevel,
       "dvbRcsRtnStatus": dvbRcsRtnStatus,
       "dvbRcsRtnStatusEbN0": dvbRcsRtnStatusEbN0,
       "dvbRcsRtnStatusSFDuration": dvbRcsRtnStatusSFDuration,
       "dvbRcsRtnStatusPayloadUnit": dvbRcsRtnStatusPayloadUnit,
       "dvbRcsConformance": dvbRcsConformance,
       "dvbRcsRcstGroups": dvbRcsRcstGroups,
       "dvbRcsRcstSystemGroup": dvbRcsRcstSystemGroup,
       "dvbRcsRcstNetworkGroup": dvbRcsRcstNetworkGroup,
       "dvbRcsRcstExtNetworkGroup": dvbRcsRcstExtNetworkGroup,
       "dvbRcsRcstDnsGroup": dvbRcsRcstDnsGroup,
       "dvbRcsRcstInstallGroup": dvbRcsRcstInstallGroup,
       "dvbRcsRcstExtInstallGroup": dvbRcsRcstExtInstallGroup,
       "dvbRcsRcstQosGroup": dvbRcsRcstQosGroup,
       "dvbRcsRcstEnhancedClassifierGroup": dvbRcsRcstEnhancedClassifierGroup,
       "dvbRcsRcstMpegQosGroup": dvbRcsRcstMpegQosGroup,
       "dvbRcsRcstGlobalQosGroup": dvbRcsRcstGlobalQosGroup,
       "dvbRcsRcstStrictQosGroup": dvbRcsRcstStrictQosGroup,
       "dvbRcsRcstControlGroup": dvbRcsRcstControlGroup,
       "dvbRcsRcstExtControlGroup": dvbRcsRcstExtControlGroup,
       "dvbRcsRcstStateGroup": dvbRcsRcstStateGroup,
       "dvbRcsFwdConfigGroup": dvbRcsFwdConfigGroup,
       "dvbRcsFwdStatusGroup": dvbRcsFwdStatusGroup,
       "dvbRcsRtnConfigGroup": dvbRcsRtnConfigGroup,
       "dvbRcsRtnExtConfigGroup": dvbRcsRtnExtConfigGroup,
       "dvbRcsRtnStatusGroup": dvbRcsRtnStatusGroup,
       "dvbRcsRtnExtStatusGroup": dvbRcsRtnExtStatusGroup,
       "dvbRcsRcstOduListGroup": dvbRcsRcstOduListGroup,
       "dvbRcsRcstCompliances": dvbRcsRcstCompliances,
       "dvbRcsRcstCompliance1": dvbRcsRcstCompliance1}
)
