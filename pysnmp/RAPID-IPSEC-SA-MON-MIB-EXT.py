# SNMP MIB module (RAPID-IPSEC-SA-MON-MIB-EXT) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/RAPID-IPSEC-SA-MON-MIB-EXT
# Produced by pysmi-1.5.4 at Mon Oct 14 22:44:38 2024
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

(IpsecDoiAhTransform,
 IpsecDoiAuthAlgorithm,
 IpsecDoiEncapsulationMode,
 IpsecDoiEspTransform,
 IpsecDoiIdentType,
 IpsecDoiIpcompTransform,
 IpsecDoiSecProtocolId) = mibBuilder.importSymbols(
    "IPSEC-ISAKMP-IKE-DOI-TC",
    "IpsecDoiAhTransform",
    "IpsecDoiAuthAlgorithm",
    "IpsecDoiEncapsulationMode",
    "IpsecDoiEspTransform",
    "IpsecDoiIdentType",
    "IpsecDoiIpcompTransform",
    "IpsecDoiSecProtocolId")

(rapidstream,) = mibBuilder.importSymbols(
    "RAPID-MIB",
    "rapidstream")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

rsIpsecSaMonModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4355, 3)
)
rsIpsecSaMonModule.setRevisions(
        ("2000-03-21 12:00",
         "2002-11-01 12:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class IpsecSaCreatorIdent(Integer32, TextualConvention):
    status = "current"
    displayHint = "d"
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
        *(("ike", 2),
          ("other", 3),
          ("static", 1),
          ("unknown", 0))
    )



class IpsecIpv6Address(OctetString, TextualConvention):
    status = "current"
    displayHint = "2x:2x:2x:2x:2x:2x:1d.1d.1d.1d"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )



# MIB Managed Objects in the order of their OIDs

_RsIpsecSaMonitorMIB_ObjectIdentity = ObjectIdentity
rsIpsecSaMonitorMIB = _RsIpsecSaMonitorMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4355, 3, 1)
)
if mibBuilder.loadTexts:
    rsIpsecSaMonitorMIB.setStatus("current")
_RsSaTables_ObjectIdentity = ObjectIdentity
rsSaTables = _RsSaTables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4355, 3, 1, 1)
)
if mibBuilder.loadTexts:
    rsSaTables.setStatus("current")
_RsIpsecSaEspInTable_Object = MibTable
rsIpsecSaEspInTable = _RsIpsecSaEspInTable_Object(
    (1, 3, 6, 1, 4, 1, 4355, 3, 1, 1, 1)
)
if mibBuilder.loadTexts:
    rsIpsecSaEspInTable.setStatus("current")
_RsIpsecSaEspInEntry_Object = MibTableRow
rsIpsecSaEspInEntry = _RsIpsecSaEspInEntry_Object(
    (1, 3, 6, 1, 4, 1, 4355, 3, 1, 1, 1, 1)
)
rsIpsecSaEspInEntry.setIndexNames(
    (0, "RAPID-IPSEC-SA-MON-MIB-EXT", "rsIpsecSaEspInAddress"),
    (0, "RAPID-IPSEC-SA-MON-MIB-EXT", "rsIpsecSaEspInSpi"),
)
if mibBuilder.loadTexts:
    rsIpsecSaEspInEntry.setStatus("current")
_RsIpsecSaEspInAddress_Type = IpAddress
_RsIpsecSaEspInAddress_Object = MibTableColumn
rsIpsecSaEspInAddress = _RsIpsecSaEspInAddress_Object(
    (1, 3, 6, 1, 4, 1, 4355, 3, 1, 1, 1, 1, 1),
    _RsIpsecSaEspInAddress_Type()
)
rsIpsecSaEspInAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsIpsecSaEspInAddress.setStatus("current")
_RsIpsecSaEspInSpi_Type = Integer32
_RsIpsecSaEspInSpi_Object = MibTableColumn
rsIpsecSaEspInSpi = _RsIpsecSaEspInSpi_Object(
    (1, 3, 6, 1, 4, 1, 4355, 3, 1, 1, 1, 1, 2),
    _RsIpsecSaEspInSpi_Type()
)
rsIpsecSaEspInSpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsIpsecSaEspInSpi.setStatus("current")


class _RsIpsecSaEspInDestId_Type(OctetString):
    """Custom type rsIpsecSaEspInDestId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_RsIpsecSaEspInDestId_Type.__name__ = "OctetString"
_RsIpsecSaEspInDestId_Object = MibTableColumn
rsIpsecSaEspInDestId = _RsIpsecSaEspInDestId_Object(
    (1, 3, 6, 1, 4, 1, 4355, 3, 1, 1, 1, 1, 3),
    _RsIpsecSaEspInDestId_Type()
)
rsIpsecSaEspInDestId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsIpsecSaEspInDestId.setStatus("current")
_RsIpsecSaEspInDestIdType_Type = IpsecDoiIdentType
_RsIpsecSaEspInDestIdType_Object = MibTableColumn
rsIpsecSaEspInDestIdType = _RsIpsecSaEspInDestIdType_Object(
    (1, 3, 6, 1, 4, 1, 4355, 3, 1, 1, 1, 1, 4),
    _RsIpsecSaEspInDestIdType_Type()
)
rsIpsecSaEspInDestIdType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsIpsecSaEspInDestIdType.setStatus("current")


class _RsIpsecSaEspInSourceId_Type(OctetString):
    """Custom type rsIpsecSaEspInSourceId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_RsIpsecSaEspInSourceId_Type.__name__ = "OctetString"
_RsIpsecSaEspInSourceId_Object = MibTableColumn
rsIpsecSaEspInSourceId = _RsIpsecSaEspInSourceId_Object(
    (1, 3, 6, 1, 4, 1, 4355, 3, 1, 1, 1, 1, 5),
    _RsIpsecSaEspInSourceId_Type()
)
rsIpsecSaEspInSourceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsIpsecSaEspInSourceId.setStatus("current")
_RsIpsecSaEspInSourceIdType_Type = IpsecDoiIdentType
_RsIpsecSaEspInSourceIdType_Object = MibTableColumn
rsIpsecSaEspInSourceIdType = _RsIpsecSaEspInSourceIdType_Object(
    (1, 3, 6, 1, 4, 1, 4355, 3, 1, 1, 1, 1, 6),
    _RsIpsecSaEspInSourceIdType_Type()
)
rsIpsecSaEspInSourceIdType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsIpsecSaEspInSourceIdType.setStatus("current")


class _RsIpsecSaEspInProtocol_Type(Integer32):
    """Custom type rsIpsecSaEspInProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_RsIpsecSaEspInProtocol_Type.__name__ = "Integer32"
_RsIpsecSaEspInProtocol_Object = MibTableColumn
rsIpsecSaEspInProtocol = _RsIpsecSaEspInProtocol_Object(
    (1, 3, 6, 1, 4, 1, 4355, 3, 1, 1, 1, 1, 7),
    _RsIpsecSaEspInProtocol_Type()
)
rsIpsecSaEspInProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsIpsecSaEspInProtocol.setStatus("current")


class _RsIpsecSaEspInDestPort_Type(Integer32):
    """Custom type rsIpsecSaEspInDestPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RsIpsecSaEspInDestPort_Type.__name__ = "Integer32"
_RsIpsecSaEspInDestPort_Object = MibTableColumn
rsIpsecSaEspInDestPort = _RsIpsecSaEspInDestPort_Object(
    (1, 3, 6, 1, 4, 1, 4355, 3, 1, 1, 1, 1, 8),
    _RsIpsecSaEspInDestPort_Type()
)
rsIpsecSaEspInDestPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsIpsecSaEspInDestPort.setStatus("current")


class _RsIpsecSaEspInSourcePort_Type(Integer32):
    """Custom type rsIpsecSaEspInSourcePort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RsIpsecSaEspInSourcePort_Type.__name__ = "Integer32"
_RsIpsecSaEspInSourcePort_Object = MibTableColumn
rsIpsecSaEspInSourcePort = _RsIpsecSaEspInSourcePort_Object(
    (1, 3, 6, 1, 4, 1, 4355, 3, 1, 1, 1, 1, 9),
    _RsIpsecSaEspInSourcePort_Type()
)
rsIpsecSaEspInSourcePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsIpsecSaEspInSourcePort.setStatus("current")
_RsIpsecSaEspInCreator_Type = IpsecSaCreatorIdent
_RsIpsecSaEspInCreator_Object = MibTableColumn
rsIpsecSaEspInCreator = _RsIpsecSaEspInCreator_Object(
    (1, 3, 6, 1, 4, 1, 4355, 3, 1, 1, 1, 1, 10),
    _RsIpsecSaEspInCreator_Type()
)
rsIpsecSaEspInCreator.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsIpsecSaEspInCreator.setStatus("current")
_RsIpsecSaEspInEncapsulation_Type = IpsecDoiEncapsulationMode
_RsIpsecSaEspInEncapsulation_Object = MibTableColumn
rsIpsecSaEspInEncapsulation = _RsIpsecSaEspInEncapsulation_Object(
    (1, 3, 6, 1, 4, 1, 4355, 3, 1, 1, 1, 1, 11),
    _RsIpsecSaEspInEncapsulation_Type()
)
rsIpsecSaEspInEncapsulation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsIpsecSaEspInEncapsulation.setStatus("current")
_RsIpsecSaEspInEncAlg_Type = IpsecDoiEspTransform
_RsIpsecSaEspInEncAlg_Object = MibTableColumn
rsIpsecSaEspInEncAlg = _RsIpsecSaEspInEncAlg_Object(
    (1, 3, 6, 1, 4, 1, 4355, 3, 1, 1, 1, 1, 12),
    _RsIpsecSaEspInEncAlg_Type()
)
rsIpsecSaEspInEncAlg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsIpsecSaEspInEncAlg.setStatus("current")


class _RsIpsecSaEspInEncKeyLength_Type(Integer32):
    """Custom type rsIpsecSaEspInEncKeyLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65531),
    )


_RsIpsecSaEspInEncKeyLength_Type.__name__ = "Integer32"
_RsIpsecSaEspInEncKeyLength_Object = MibTableColumn
rsIpsecSaEspInEncKeyLength = _RsIpsecSaEspInEncKeyLength_Object(
    (1, 3, 6, 1, 4, 1, 4355, 3, 1, 1, 1, 1, 13),
    _RsIpsecSaEspInEncKeyLength_Type()
)
rsIpsecSaEspInEncKeyLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsIpsecSaEspInEncKeyLength.setStatus("current")
if mibBuilder.loadTexts:
    rsIpsecSaEspInEncKeyLength.setUnits("bits")
_RsIpsecSaEspInAuthAlg_Type = IpsecDoiAuthAlgorithm
_RsIpsecSaEspInAuthAlg_Object = MibTableColumn
rsIpsecSaEspInAuthAlg = _RsIpsecSaEspInAuthAlg_Object(
    (1, 3, 6, 1, 4, 1, 4355, 3, 1, 1, 1, 1, 14),
    _RsIpsecSaEspInAuthAlg_Type()
)
rsIpsecSaEspInAuthAlg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsIpsecSaEspInAuthAlg.setStatus("current")
_RsIpsecSaEspInLimitSeconds_Type = Integer32
_RsIpsecSaEspInLimitSeconds_Object = MibTableColumn
rsIpsecSaEspInLimitSeconds = _RsIpsecSaEspInLimitSeconds_Object(
    (1, 3, 6, 1, 4, 1, 4355, 3, 1, 1, 1, 1, 15),
    _RsIpsecSaEspInLimitSeconds_Type()
)
rsIpsecSaEspInLimitSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsIpsecSaEspInLimitSeconds.setStatus("current")
if mibBuilder.loadTexts:
    rsIpsecSaEspInLimitSeconds.setUnits("seconds")
_RsIpsecSaEspInLimitKbytes_Type = Integer32
_RsIpsecSaEspInLimitKbytes_Object = MibTableColumn
rsIpsecSaEspInLimitKbytes = _RsIpsecSaEspInLimitKbytes_Object(
    (1, 3, 6, 1, 4, 1, 4355, 3, 1, 1, 1, 1, 16),
    _RsIpsecSaEspInLimitKbytes_Type()
)
rsIpsecSaEspInLimitKbytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsIpsecSaEspInLimitKbytes.setStatus("current")
if mibBuilder.loadTexts:
    rsIpsecSaEspInLimitKbytes.setUnits("kilobytes")
_RsIpsecSaEspInAccSeconds_Type = Counter32
_RsIpsecSaEspInAccSeconds_Object = MibTableColumn
rsIpsecSaEspInAccSeconds = _RsIpsecSaEspInAccSeconds_Object(
    (1, 3, 6, 1, 4, 1, 4355, 3, 1, 1, 1, 1, 17),
    _RsIpsecSaEspInAccSeconds_Type()
)
rsIpsecSaEspInAccSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsIpsecSaEspInAccSeconds.setStatus("current")
if mibBuilder.loadTexts:
    rsIpsecSaEspInAccSeconds.setUnits("seconds")
_RsIpsecSaEspInAccKbytes_Type = Counter32
_RsIpsecSaEspInAccKbytes_Object = MibTableColumn
rsIpsecSaEspInAccKbytes = _RsIpsecSaEspInAccKbytes_Object(
    (1, 3, 6, 1, 4, 1, 4355, 3, 1, 1, 1, 1, 18),
    _RsIpsecSaEspInAccKbytes_Type()
)
rsIpsecSaEspInAccKbytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsIpsecSaEspInAccKbytes.setStatus("current")
if mibBuilder.loadTexts:
    rsIpsecSaEspInAccKbytes.setUnits("kilobytes")
_RsIpsecSaEspInUserOctets_Type = Counter32
_RsIpsecSaEspInUserOctets_Object = MibTableColumn
rsIpsecSaEspInUserOctets = _RsIpsecSaEspInUserOctets_Object(
    (1, 3, 6, 1, 4, 1, 4355, 3, 1, 1, 1, 1, 19),
    _RsIpsecSaEspInUserOctets_Type()
)
rsIpsecSaEspInUserOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsIpsecSaEspInUserOctets.setStatus("current")
if mibBuilder.loadTexts:
    rsIpsecSaEspInUserOctets.setUnits("bytes")
_RsIpsecSaEspInPackets_Type = Counter32
_RsIpsecSaEspInPackets_Object = MibTableColumn
rsIpsecSaEspInPackets = _RsIpsecSaEspInPackets_Object(
    (1, 3, 6, 1, 4, 1, 4355, 3, 1, 1, 1, 1, 20),
    _RsIpsecSaEspInPackets_Type()
)
rsIpsecSaEspInPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsIpsecSaEspInPackets.setStatus("current")
_RsIpsecSaEspInDecryptErrors_Type = Counter32
_RsIpsecSaEspInDecryptErrors_Object = MibTableColumn
rsIpsecSaEspInDecryptErrors = _RsIpsecSaEspInDecryptErrors_Object(
    (1, 3, 6, 1, 4, 1, 4355, 3, 1, 1, 1, 1, 21),
    _RsIpsecSaEspInDecryptErrors_Type()
)
rsIpsecSaEspInDecryptErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsIpsecSaEspInDecryptErrors.setStatus("current")
_RsIpsecSaEspInAuthErrors_Type = Counter32
_RsIpsecSaEspInAuthErrors_Object = MibTableColumn
rsIpsecSaEspInAuthErrors = _RsIpsecSaEspInAuthErrors_Object(
    (1, 3, 6, 1, 4, 1, 4355, 3, 1, 1, 1, 1, 22),
    _RsIpsecSaEspInAuthErrors_Type()
)
rsIpsecSaEspInAuthErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsIpsecSaEspInAuthErrors.setStatus("current")
_RsIpsecSaEspInReplayErrors_Type = Counter32
_RsIpsecSaEspInReplayErrors_Object = MibTableColumn
rsIpsecSaEspInReplayErrors = _RsIpsecSaEspInReplayErrors_Object(
    (1, 3, 6, 1, 4, 1, 4355, 3, 1, 1, 1, 1, 23),
    _RsIpsecSaEspInReplayErrors_Type()
)
rsIpsecSaEspInReplayErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsIpsecSaEspInReplayErrors.setStatus("current")
_RsIpsecSaEspInPolicyErrors_Type = Counter32
_RsIpsecSaEspInPolicyErrors_Object = MibTableColumn
rsIpsecSaEspInPolicyErrors = _RsIpsecSaEspInPolicyErrors_Object(
    (1, 3, 6, 1, 4, 1, 4355, 3, 1, 1, 1, 1, 24),
    _RsIpsecSaEspInPolicyErrors_Type()
)
rsIpsecSaEspInPolicyErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsIpsecSaEspInPolicyErrors.setStatus("current")
_RsIpsecSaEspInPadErrors_Type = Counter32
_RsIpsecSaEspInPadErrors_Object = MibTableColumn
rsIpsecSaEspInPadErrors = _RsIpsecSaEspInPadErrors_Object(
    (1, 3, 6, 1, 4, 1, 4355, 3, 1, 1, 1, 1, 25),
    _RsIpsecSaEspInPadErrors_Type()
)
rsIpsecSaEspInPadErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsIpsecSaEspInPadErrors.setStatus("current")
_RsIpsecSaEspInOtherReceiveErrors_Type = Counter32
_RsIpsecSaEspInOtherReceiveErrors_Object = MibTableColumn
rsIpsecSaEspInOtherReceiveErrors = _RsIpsecSaEspInOtherReceiveErrors_Object(
    (1, 3, 6, 1, 4, 1, 4355, 3, 1, 1, 1, 1, 26),
    _RsIpsecSaEspInOtherReceiveErrors_Type()
)
rsIpsecSaEspInOtherReceiveErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsIpsecSaEspInOtherReceiveErrors.setStatus("current")
_RsIpsecSaAhInTable_Object = MibTable
rsIpsecSaAhInTable = _RsIpsecSaAhInTable_Object(
    (1, 3, 6, 1, 4, 1, 4355, 3, 1, 1, 2)
)
if mibBuilder.loadTexts:
    rsIpsecSaAhInTable.setStatus("current")
_RsIpsecSaAhInEntry_Object = MibTableRow
rsIpsecSaAhInEntry = _RsIpsecSaAhInEntry_Object(
    (1, 3, 6, 1, 4, 1, 4355, 3, 1, 1, 2, 1)
)
rsIpsecSaAhInEntry.setIndexNames(
    (0, "RAPID-IPSEC-SA-MON-MIB-EXT", "rsIpsecSaAhInAddress"),
    (0, "RAPID-IPSEC-SA-MON-MIB-EXT", "rsIpsecSaAhInSpi"),
)
if mibBuilder.loadTexts:
    rsIpsecSaAhInEntry.setStatus("current")
_RsIpsecSaAhInAddress_Type = IpAddress
_RsIpsecSaAhInAddress_Object = MibTableColumn
rsIpsecSaAhInAddress = _RsIpsecSaAhInAddress_Object(
    (1, 3, 6, 1, 4, 1, 4355, 3, 1, 1, 2, 1, 1),
    _RsIpsecSaAhInAddress_Type()
)
rsIpsecSaAhInAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsIpsecSaAhInAddress.setStatus("current")
_RsIpsecSaAhInSpi_Type = Integer32
_RsIpsecSaAhInSpi_Object = MibTableColumn
rsIpsecSaAhInSpi = _RsIpsecSaAhInSpi_Object(
    (1, 3, 6, 1, 4, 1, 4355, 3, 1, 1, 2, 1, 2),
    _RsIpsecSaAhInSpi_Type()
)
rsIpsecSaAhInSpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsIpsecSaAhInSpi.setStatus("current")


class _RsIpsecSaAhInDestId_Type(OctetString):
    """Custom type rsIpsecSaAhInDestId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_RsIpsecSaAhInDestId_Type.__name__ = "OctetString"
_RsIpsecSaAhInDestId_Object = MibTableColumn
rsIpsecSaAhInDestId = _RsIpsecSaAhInDestId_Object(
    (1, 3, 6, 1, 4, 1, 4355, 3, 1, 1, 2, 1, 3),
    _RsIpsecSaAhInDestId_Type()
)
rsIpsecSaAhInDestId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsIpsecSaAhInDestId.setStatus("current")
_RsIpsecSaAhInDestIdType_Type = IpsecDoiIdentType
_RsIpsecSaAhInDestIdType_Object = MibTableColumn
rsIpsecSaAhInDestIdType = _RsIpsecSaAhInDestIdType_Object(
    (1, 3, 6, 1, 4, 1, 4355, 3, 1, 1, 2, 1, 4),
    _RsIpsecSaAhInDestIdType_Type()
)
rsIpsecSaAhInDestIdType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsIpsecSaAhInDestIdType.setStatus("current")


class _RsIpsecSaAhInSourceId_Type(OctetString):
    """Custom type rsIpsecSaAhInSourceId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_RsIpsecSaAhInSourceId_Type.__name__ = "OctetString"
_RsIpsecSaAhInSourceId_Object = MibTableColumn
rsIpsecSaAhInSourceId = _RsIpsecSaAhInSourceId_Object(
    (1, 3, 6, 1, 4, 1, 4355, 3, 1, 1, 2, 1, 5),
    _RsIpsecSaAhInSourceId_Type()
)
rsIpsecSaAhInSourceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsIpsecSaAhInSourceId.setStatus("current")
_RsIpsecSaAhInSourceIdType_Type = IpsecDoiIdentType
_RsIpsecSaAhInSourceIdType_Object = MibTableColumn
rsIpsecSaAhInSourceIdType = _RsIpsecSaAhInSourceIdType_Object(
    (1, 3, 6, 1, 4, 1, 4355, 3, 1, 1, 2, 1, 6),
    _RsIpsecSaAhInSourceIdType_Type()
)
rsIpsecSaAhInSourceIdType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsIpsecSaAhInSourceIdType.setStatus("current")


class _RsIpsecSaAhInProtocol_Type(Integer32):
    """Custom type rsIpsecSaAhInProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_RsIpsecSaAhInProtocol_Type.__name__ = "Integer32"
_RsIpsecSaAhInProtocol_Object = MibTableColumn
rsIpsecSaAhInProtocol = _RsIpsecSaAhInProtocol_Object(
    (1, 3, 6, 1, 4, 1, 4355, 3, 1, 1, 2, 1, 7),
    _RsIpsecSaAhInProtocol_Type()
)
rsIpsecSaAhInProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsIpsecSaAhInProtocol.setStatus("current")


class _RsIpsecSaAhInDestPort_Type(Integer32):
    """Custom type rsIpsecSaAhInDestPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RsIpsecSaAhInDestPort_Type.__name__ = "Integer32"
_RsIpsecSaAhInDestPort_Object = MibTableColumn
rsIpsecSaAhInDestPort = _RsIpsecSaAhInDestPort_Object(
    (1, 3, 6, 1, 4, 1, 4355, 3, 1, 1, 2, 1, 8),
    _RsIpsecSaAhInDestPort_Type()
)
rsIpsecSaAhInDestPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsIpsecSaAhInDestPort.setStatus("current")


class _RsIpsecSaAhInSourcePort_Type(Integer32):
    """Custom type rsIpsecSaAhInSourcePort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RsIpsecSaAhInSourcePort_Type.__name__ = "Integer32"
_RsIpsecSaAhInSourcePort_Object = MibTableColumn
rsIpsecSaAhInSourcePort = _RsIpsecSaAhInSourcePort_Object(
    (1, 3, 6, 1, 4, 1, 4355, 3, 1, 1, 2, 1, 9),
    _RsIpsecSaAhInSourcePort_Type()
)
rsIpsecSaAhInSourcePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsIpsecSaAhInSourcePort.setStatus("current")
_RsIpsecSaAhInCreator_Type = IpsecSaCreatorIdent
_RsIpsecSaAhInCreator_Object = MibTableColumn
rsIpsecSaAhInCreator = _RsIpsecSaAhInCreator_Object(
    (1, 3, 6, 1, 4, 1, 4355, 3, 1, 1, 2, 1, 10),
    _RsIpsecSaAhInCreator_Type()
)
rsIpsecSaAhInCreator.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsIpsecSaAhInCreator.setStatus("current")
_RsIpsecSaAhInEncapsulation_Type = IpsecDoiEncapsulationMode
_RsIpsecSaAhInEncapsulation_Object = MibTableColumn
rsIpsecSaAhInEncapsulation = _RsIpsecSaAhInEncapsulation_Object(
    (1, 3, 6, 1, 4, 1, 4355, 3, 1, 1, 2, 1, 11),
    _RsIpsecSaAhInEncapsulation_Type()
)
rsIpsecSaAhInEncapsulation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsIpsecSaAhInEncapsulation.setStatus("current")
_RsIpsecSaAhInAuthAlg_Type = IpsecDoiAhTransform
_RsIpsecSaAhInAuthAlg_Object = MibTableColumn
rsIpsecSaAhInAuthAlg = _RsIpsecSaAhInAuthAlg_Object(
    (1, 3, 6, 1, 4, 1, 4355, 3, 1, 1, 2, 1, 12),
    _RsIpsecSaAhInAuthAlg_Type()
)
rsIpsecSaAhInAuthAlg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsIpsecSaAhInAuthAlg.setStatus("current")
_RsIpsecSaAhInLimitSeconds_Type = Integer32
_RsIpsecSaAhInLimitSeconds_Object = MibTableColumn
rsIpsecSaAhInLimitSeconds = _RsIpsecSaAhInLimitSeconds_Object(
    (1, 3, 6, 1, 4, 1, 4355, 3, 1, 1, 2, 1, 13),
    _RsIpsecSaAhInLimitSeconds_Type()
)
rsIpsecSaAhInLimitSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsIpsecSaAhInLimitSeconds.setStatus("current")
if mibBuilder.loadTexts:
    rsIpsecSaAhInLimitSeconds.setUnits("seconds")
_RsIpsecSaAhInLimitKbytes_Type = Integer32
_RsIpsecSaAhInLimitKbytes_Object = MibTableColumn
rsIpsecSaAhInLimitKbytes = _RsIpsecSaAhInLimitKbytes_Object(
    (1, 3, 6, 1, 4, 1, 4355, 3, 1, 1, 2, 1, 14),
    _RsIpsecSaAhInLimitKbytes_Type()
)
rsIpsecSaAhInLimitKbytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsIpsecSaAhInLimitKbytes.setStatus("current")
if mibBuilder.loadTexts:
    rsIpsecSaAhInLimitKbytes.setUnits("kilobytes")
_RsIpsecSaAhInAccSeconds_Type = Counter32
_RsIpsecSaAhInAccSeconds_Object = MibTableColumn
rsIpsecSaAhInAccSeconds = _RsIpsecSaAhInAccSeconds_Object(
    (1, 3, 6, 1, 4, 1, 4355, 3, 1, 1, 2, 1, 15),
    _RsIpsecSaAhInAccSeconds_Type()
)
rsIpsecSaAhInAccSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsIpsecSaAhInAccSeconds.setStatus("current")
if mibBuilder.loadTexts:
    rsIpsecSaAhInAccSeconds.setUnits("seconds")
_RsIpsecSaAhInAccKbytes_Type = Counter32
_RsIpsecSaAhInAccKbytes_Object = MibTableColumn
rsIpsecSaAhInAccKbytes = _RsIpsecSaAhInAccKbytes_Object(
    (1, 3, 6, 1, 4, 1, 4355, 3, 1, 1, 2, 1, 16),
    _RsIpsecSaAhInAccKbytes_Type()
)
rsIpsecSaAhInAccKbytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsIpsecSaAhInAccKbytes.setStatus("current")
if mibBuilder.loadTexts:
    rsIpsecSaAhInAccKbytes.setUnits("kilobytes")
_RsIpsecSaAhInUserOctets_Type = Counter32
_RsIpsecSaAhInUserOctets_Object = MibTableColumn
rsIpsecSaAhInUserOctets = _RsIpsecSaAhInUserOctets_Object(
    (1, 3, 6, 1, 4, 1, 4355, 3, 1, 1, 2, 1, 17),
    _RsIpsecSaAhInUserOctets_Type()
)
rsIpsecSaAhInUserOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsIpsecSaAhInUserOctets.setStatus("current")
if mibBuilder.loadTexts:
    rsIpsecSaAhInUserOctets.setUnits("bytes")
_RsIpsecSaAhInPackets_Type = Counter32
_RsIpsecSaAhInPackets_Object = MibTableColumn
rsIpsecSaAhInPackets = _RsIpsecSaAhInPackets_Object(
    (1, 3, 6, 1, 4, 1, 4355, 3, 1, 1, 2, 1, 18),
    _RsIpsecSaAhInPackets_Type()
)
rsIpsecSaAhInPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsIpsecSaAhInPackets.setStatus("current")
_RsIpsecSaAhInAuthErrors_Type = Counter32
_RsIpsecSaAhInAuthErrors_Object = MibTableColumn
rsIpsecSaAhInAuthErrors = _RsIpsecSaAhInAuthErrors_Object(
    (1, 3, 6, 1, 4, 1, 4355, 3, 1, 1, 2, 1, 19),
    _RsIpsecSaAhInAuthErrors_Type()
)
rsIpsecSaAhInAuthErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsIpsecSaAhInAuthErrors.setStatus("current")
_RsIpsecSaAhInReplayErrors_Type = Counter32
_RsIpsecSaAhInReplayErrors_Object = MibTableColumn
rsIpsecSaAhInReplayErrors = _RsIpsecSaAhInReplayErrors_Object(
    (1, 3, 6, 1, 4, 1, 4355, 3, 1, 1, 2, 1, 20),
    _RsIpsecSaAhInReplayErrors_Type()
)
rsIpsecSaAhInReplayErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsIpsecSaAhInReplayErrors.setStatus("current")
_RsIpsecSaAhInPolicyErrors_Type = Counter32
_RsIpsecSaAhInPolicyErrors_Object = MibTableColumn
rsIpsecSaAhInPolicyErrors = _RsIpsecSaAhInPolicyErrors_Object(
    (1, 3, 6, 1, 4, 1, 4355, 3, 1, 1, 2, 1, 21),
    _RsIpsecSaAhInPolicyErrors_Type()
)
rsIpsecSaAhInPolicyErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsIpsecSaAhInPolicyErrors.setStatus("current")
_RsIpsecSaAhInOtherReceiveErrors_Type = Counter32
_RsIpsecSaAhInOtherReceiveErrors_Object = MibTableColumn
rsIpsecSaAhInOtherReceiveErrors = _RsIpsecSaAhInOtherReceiveErrors_Object(
    (1, 3, 6, 1, 4, 1, 4355, 3, 1, 1, 2, 1, 22),
    _RsIpsecSaAhInOtherReceiveErrors_Type()
)
rsIpsecSaAhInOtherReceiveErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsIpsecSaAhInOtherReceiveErrors.setStatus("current")
_RsIpsecSaIpcompInTable_Object = MibTable
rsIpsecSaIpcompInTable = _RsIpsecSaIpcompInTable_Object(
    (1, 3, 6, 1, 4, 1, 4355, 3, 1, 1, 3)
)
if mibBuilder.loadTexts:
    rsIpsecSaIpcompInTable.setStatus("current")
_RsIpsecSaIpcompInEntry_Object = MibTableRow
rsIpsecSaIpcompInEntry = _RsIpsecSaIpcompInEntry_Object(
    (1, 3, 6, 1, 4, 1, 4355, 3, 1, 1, 3, 1)
)
rsIpsecSaIpcompInEntry.setIndexNames(
    (0, "RAPID-IPSEC-SA-MON-MIB-EXT", "rsIpsecSaIpcompInAddress"),
    (0, "RAPID-IPSEC-SA-MON-MIB-EXT", "rsIpsecSaIpcompInCpi"),
)
if mibBuilder.loadTexts:
    rsIpsecSaIpcompInEntry.setStatus("current")
_RsIpsecSaIpcompInAddress_Type = IpAddress
_RsIpsecSaIpcompInAddress_Object = MibTableColumn
rsIpsecSaIpcompInAddress = _RsIpsecSaIpcompInAddress_Object(
    (1, 3, 6, 1, 4, 1, 4355, 3, 1, 1, 3, 1, 1),
    _RsIpsecSaIpcompInAddress_Type()
)
rsIpsecSaIpcompInAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsIpsecSaIpcompInAddress.setStatus("current")
_RsIpsecSaIpcompInCpi_Type = IpsecDoiIpcompTransform
_RsIpsecSaIpcompInCpi_Object = MibTableColumn
rsIpsecSaIpcompInCpi = _RsIpsecSaIpcompInCpi_Object(
    (1, 3, 6, 1, 4, 1, 4355, 3, 1, 1, 3, 1, 2),
    _RsIpsecSaIpcompInCpi_Type()
)
rsIpsecSaIpcompInCpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsIpsecSaIpcompInCpi.setStatus("current")


class _RsIpsecSaIpcompInDestId_Type(OctetString):
    """Custom type rsIpsecSaIpcompInDestId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_RsIpsecSaIpcompInDestId_Type.__name__ = "OctetString"
_RsIpsecSaIpcompInDestId_Object = MibTableColumn
rsIpsecSaIpcompInDestId = _RsIpsecSaIpcompInDestId_Object(
    (1, 3, 6, 1, 4, 1, 4355, 3, 1, 1, 3, 1, 3),
    _RsIpsecSaIpcompInDestId_Type()
)
rsIpsecSaIpcompInDestId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsIpsecSaIpcompInDestId.setStatus("current")
_RsIpsecSaIpcompInDestIdType_Type = IpsecDoiIdentType
_RsIpsecSaIpcompInDestIdType_Object = MibTableColumn
rsIpsecSaIpcompInDestIdType = _RsIpsecSaIpcompInDestIdType_Object(
    (1, 3, 6, 1, 4, 1, 4355, 3, 1, 1, 3, 1, 4),
    _RsIpsecSaIpcompInDestIdType_Type()
)
rsIpsecSaIpcompInDestIdType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsIpsecSaIpcompInDestIdType.setStatus("current")


class _RsIpsecSaIpcompInSourceId_Type(OctetString):
    """Custom type rsIpsecSaIpcompInSourceId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_RsIpsecSaIpcompInSourceId_Type.__name__ = "OctetString"
_RsIpsecSaIpcompInSourceId_Object = MibTableColumn
rsIpsecSaIpcompInSourceId = _RsIpsecSaIpcompInSourceId_Object(
    (1, 3, 6, 1, 4, 1, 4355, 3, 1, 1, 3, 1, 5),
    _RsIpsecSaIpcompInSourceId_Type()
)
rsIpsecSaIpcompInSourceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsIpsecSaIpcompInSourceId.setStatus("current")
_RsIpsecSaIpcompInSourceIdType_Type = IpsecDoiIdentType
_RsIpsecSaIpcompInSourceIdType_Object = MibTableColumn
rsIpsecSaIpcompInSourceIdType = _RsIpsecSaIpcompInSourceIdType_Object(
    (1, 3, 6, 1, 4, 1, 4355, 3, 1, 1, 3, 1, 6),
    _RsIpsecSaIpcompInSourceIdType_Type()
)
rsIpsecSaIpcompInSourceIdType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsIpsecSaIpcompInSourceIdType.setStatus("current")


class _RsIpsecSaIpcompInProtocol_Type(Integer32):
    """Custom type rsIpsecSaIpcompInProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_RsIpsecSaIpcompInProtocol_Type.__name__ = "Integer32"
_RsIpsecSaIpcompInProtocol_Object = MibTableColumn
rsIpsecSaIpcompInProtocol = _RsIpsecSaIpcompInProtocol_Object(
    (1, 3, 6, 1, 4, 1, 4355, 3, 1, 1, 3, 1, 7),
    _RsIpsecSaIpcompInProtocol_Type()
)
rsIpsecSaIpcompInProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsIpsecSaIpcompInProtocol.setStatus("current")


class _RsIpsecSaIpcompInDestPort_Type(Integer32):
    """Custom type rsIpsecSaIpcompInDestPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RsIpsecSaIpcompInDestPort_Type.__name__ = "Integer32"
_RsIpsecSaIpcompInDestPort_Object = MibTableColumn
rsIpsecSaIpcompInDestPort = _RsIpsecSaIpcompInDestPort_Object(
    (1, 3, 6, 1, 4, 1, 4355, 3, 1, 1, 3, 1, 8),
    _RsIpsecSaIpcompInDestPort_Type()
)
rsIpsecSaIpcompInDestPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsIpsecSaIpcompInDestPort.setStatus("current")


class _RsIpsecSaIpcompInSourcePort_Type(Integer32):
    """Custom type rsIpsecSaIpcompInSourcePort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RsIpsecSaIpcompInSourcePort_Type.__name__ = "Integer32"
_RsIpsecSaIpcompInSourcePort_Object = MibTableColumn
rsIpsecSaIpcompInSourcePort = _RsIpsecSaIpcompInSourcePort_Object(
    (1, 3, 6, 1, 4, 1, 4355, 3, 1, 1, 3, 1, 9),
    _RsIpsecSaIpcompInSourcePort_Type()
)
rsIpsecSaIpcompInSourcePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsIpsecSaIpcompInSourcePort.setStatus("current")
_RsIpsecSaIpcompInCreator_Type = IpsecSaCreatorIdent
_RsIpsecSaIpcompInCreator_Object = MibTableColumn
rsIpsecSaIpcompInCreator = _RsIpsecSaIpcompInCreator_Object(
    (1, 3, 6, 1, 4, 1, 4355, 3, 1, 1, 3, 1, 10),
    _RsIpsecSaIpcompInCreator_Type()
)
rsIpsecSaIpcompInCreator.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsIpsecSaIpcompInCreator.setStatus("current")
_RsIpsecSaIpcompInEncapsulation_Type = IpsecDoiEncapsulationMode
_RsIpsecSaIpcompInEncapsulation_Object = MibTableColumn
rsIpsecSaIpcompInEncapsulation = _RsIpsecSaIpcompInEncapsulation_Object(
    (1, 3, 6, 1, 4, 1, 4355, 3, 1, 1, 3, 1, 11),
    _RsIpsecSaIpcompInEncapsulation_Type()
)
rsIpsecSaIpcompInEncapsulation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsIpsecSaIpcompInEncapsulation.setStatus("current")
_RsIpsecSaIpcompInDecompAlg_Type = IpsecDoiIpcompTransform
_RsIpsecSaIpcompInDecompAlg_Object = MibTableColumn
rsIpsecSaIpcompInDecompAlg = _RsIpsecSaIpcompInDecompAlg_Object(
    (1, 3, 6, 1, 4, 1, 4355, 3, 1, 1, 3, 1, 12),
    _RsIpsecSaIpcompInDecompAlg_Type()
)
rsIpsecSaIpcompInDecompAlg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsIpsecSaIpcompInDecompAlg.setStatus("current")
_RsIpsecSaIpcompInSeconds_Type = Counter32
_RsIpsecSaIpcompInSeconds_Object = MibTableColumn
rsIpsecSaIpcompInSeconds = _RsIpsecSaIpcompInSeconds_Object(
    (1, 3, 6, 1, 4, 1, 4355, 3, 1, 1, 3, 1, 13),
    _RsIpsecSaIpcompInSeconds_Type()
)
rsIpsecSaIpcompInSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsIpsecSaIpcompInSeconds.setStatus("current")
if mibBuilder.loadTexts:
    rsIpsecSaIpcompInSeconds.setUnits("seconds")
_RsIpsecSaIpcompInUserOctets_Type = Counter32
_RsIpsecSaIpcompInUserOctets_Object = MibTableColumn
rsIpsecSaIpcompInUserOctets = _RsIpsecSaIpcompInUserOctets_Object(
    (1, 3, 6, 1, 4, 1, 4355, 3, 1, 1, 3, 1, 14),
    _RsIpsecSaIpcompInUserOctets_Type()
)
rsIpsecSaIpcompInUserOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsIpsecSaIpcompInUserOctets.setStatus("current")
if mibBuilder.loadTexts:
    rsIpsecSaIpcompInUserOctets.setUnits("bytes")
_RsIpsecSaIpcompInPackets_Type = Counter32
_RsIpsecSaIpcompInPackets_Object = MibTableColumn
rsIpsecSaIpcompInPackets = _RsIpsecSaIpcompInPackets_Object(
    (1, 3, 6, 1, 4, 1, 4355, 3, 1, 1, 3, 1, 15),
    _RsIpsecSaIpcompInPackets_Type()
)
rsIpsecSaIpcompInPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsIpsecSaIpcompInPackets.setStatus("current")
_RsIpsecSaIpcompInDecompErrors_Type = Counter32
_RsIpsecSaIpcompInDecompErrors_Object = MibTableColumn
rsIpsecSaIpcompInDecompErrors = _RsIpsecSaIpcompInDecompErrors_Object(
    (1, 3, 6, 1, 4, 1, 4355, 3, 1, 1, 3, 1, 16),
    _RsIpsecSaIpcompInDecompErrors_Type()
)
rsIpsecSaIpcompInDecompErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsIpsecSaIpcompInDecompErrors.setStatus("current")
_RsIpsecSaIpcompInOtherReceiveErrors_Type = Counter32
_RsIpsecSaIpcompInOtherReceiveErrors_Object = MibTableColumn
rsIpsecSaIpcompInOtherReceiveErrors = _RsIpsecSaIpcompInOtherReceiveErrors_Object(
    (1, 3, 6, 1, 4, 1, 4355, 3, 1, 1, 3, 1, 17),
    _RsIpsecSaIpcompInOtherReceiveErrors_Type()
)
rsIpsecSaIpcompInOtherReceiveErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsIpsecSaIpcompInOtherReceiveErrors.setStatus("current")
_RsIpsecSaEspOutTable_Object = MibTable
rsIpsecSaEspOutTable = _RsIpsecSaEspOutTable_Object(
    (1, 3, 6, 1, 4, 1, 4355, 3, 1, 1, 4)
)
if mibBuilder.loadTexts:
    rsIpsecSaEspOutTable.setStatus("current")
_RsIpsecSaEspOutEntry_Object = MibTableRow
rsIpsecSaEspOutEntry = _RsIpsecSaEspOutEntry_Object(
    (1, 3, 6, 1, 4, 1, 4355, 3, 1, 1, 4, 1)
)
rsIpsecSaEspOutEntry.setIndexNames(
    (0, "RAPID-IPSEC-SA-MON-MIB-EXT", "rsIpsecSaEspOutAddress"),
    (0, "RAPID-IPSEC-SA-MON-MIB-EXT", "rsIpsecSaEspOutSpi"),
)
if mibBuilder.loadTexts:
    rsIpsecSaEspOutEntry.setStatus("current")
_RsIpsecSaEspOutAddress_Type = IpAddress
_RsIpsecSaEspOutAddress_Object = MibTableColumn
rsIpsecSaEspOutAddress = _RsIpsecSaEspOutAddress_Object(
    (1, 3, 6, 1, 4, 1, 4355, 3, 1, 1, 4, 1, 1),
    _RsIpsecSaEspOutAddress_Type()
)
rsIpsecSaEspOutAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsIpsecSaEspOutAddress.setStatus("current")
_RsIpsecSaEspOutSpi_Type = Integer32
_RsIpsecSaEspOutSpi_Object = MibTableColumn
rsIpsecSaEspOutSpi = _RsIpsecSaEspOutSpi_Object(
    (1, 3, 6, 1, 4, 1, 4355, 3, 1, 1, 4, 1, 2),
    _RsIpsecSaEspOutSpi_Type()
)
rsIpsecSaEspOutSpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsIpsecSaEspOutSpi.setStatus("current")


class _RsIpsecSaEspOutSourceId_Type(OctetString):
    """Custom type rsIpsecSaEspOutSourceId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 255),
    )


_RsIpsecSaEspOutSourceId_Type.__name__ = "OctetString"
_RsIpsecSaEspOutSourceId_Object = MibTableColumn
rsIpsecSaEspOutSourceId = _RsIpsecSaEspOutSourceId_Object(
    (1, 3, 6, 1, 4, 1, 4355, 3, 1, 1, 4, 1, 3),
    _RsIpsecSaEspOutSourceId_Type()
)
rsIpsecSaEspOutSourceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsIpsecSaEspOutSourceId.setStatus("current")
_RsIpsecSaEspOutSourceIdType_Type = IpsecDoiIdentType
_RsIpsecSaEspOutSourceIdType_Object = MibTableColumn
rsIpsecSaEspOutSourceIdType = _RsIpsecSaEspOutSourceIdType_Object(
    (1, 3, 6, 1, 4, 1, 4355, 3, 1, 1, 4, 1, 4),
    _RsIpsecSaEspOutSourceIdType_Type()
)
rsIpsecSaEspOutSourceIdType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsIpsecSaEspOutSourceIdType.setStatus("current")


class _RsIpsecSaEspOutDestId_Type(OctetString):
    """Custom type rsIpsecSaEspOutDestId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 255),
    )


_RsIpsecSaEspOutDestId_Type.__name__ = "OctetString"
_RsIpsecSaEspOutDestId_Object = MibTableColumn
rsIpsecSaEspOutDestId = _RsIpsecSaEspOutDestId_Object(
    (1, 3, 6, 1, 4, 1, 4355, 3, 1, 1, 4, 1, 5),
    _RsIpsecSaEspOutDestId_Type()
)
rsIpsecSaEspOutDestId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsIpsecSaEspOutDestId.setStatus("current")
_RsIpsecSaEspOutDestIdType_Type = IpsecDoiIdentType
_RsIpsecSaEspOutDestIdType_Object = MibTableColumn
rsIpsecSaEspOutDestIdType = _RsIpsecSaEspOutDestIdType_Object(
    (1, 3, 6, 1, 4, 1, 4355, 3, 1, 1, 4, 1, 6),
    _RsIpsecSaEspOutDestIdType_Type()
)
rsIpsecSaEspOutDestIdType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsIpsecSaEspOutDestIdType.setStatus("current")


class _RsIpsecSaEspOutProtocol_Type(Integer32):
    """Custom type rsIpsecSaEspOutProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_RsIpsecSaEspOutProtocol_Type.__name__ = "Integer32"
_RsIpsecSaEspOutProtocol_Object = MibTableColumn
rsIpsecSaEspOutProtocol = _RsIpsecSaEspOutProtocol_Object(
    (1, 3, 6, 1, 4, 1, 4355, 3, 1, 1, 4, 1, 7),
    _RsIpsecSaEspOutProtocol_Type()
)
rsIpsecSaEspOutProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsIpsecSaEspOutProtocol.setStatus("current")


class _RsIpsecSaEspOutSourcePort_Type(Integer32):
    """Custom type rsIpsecSaEspOutSourcePort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RsIpsecSaEspOutSourcePort_Type.__name__ = "Integer32"
_RsIpsecSaEspOutSourcePort_Object = MibTableColumn
rsIpsecSaEspOutSourcePort = _RsIpsecSaEspOutSourcePort_Object(
    (1, 3, 6, 1, 4, 1, 4355, 3, 1, 1, 4, 1, 8),
    _RsIpsecSaEspOutSourcePort_Type()
)
rsIpsecSaEspOutSourcePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsIpsecSaEspOutSourcePort.setStatus("current")


class _RsIpsecSaEspOutDestPort_Type(Integer32):
    """Custom type rsIpsecSaEspOutDestPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RsIpsecSaEspOutDestPort_Type.__name__ = "Integer32"
_RsIpsecSaEspOutDestPort_Object = MibTableColumn
rsIpsecSaEspOutDestPort = _RsIpsecSaEspOutDestPort_Object(
    (1, 3, 6, 1, 4, 1, 4355, 3, 1, 1, 4, 1, 9),
    _RsIpsecSaEspOutDestPort_Type()
)
rsIpsecSaEspOutDestPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsIpsecSaEspOutDestPort.setStatus("current")
_RsIpsecSaEspOutCreator_Type = IpsecSaCreatorIdent
_RsIpsecSaEspOutCreator_Object = MibTableColumn
rsIpsecSaEspOutCreator = _RsIpsecSaEspOutCreator_Object(
    (1, 3, 6, 1, 4, 1, 4355, 3, 1, 1, 4, 1, 10),
    _RsIpsecSaEspOutCreator_Type()
)
rsIpsecSaEspOutCreator.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsIpsecSaEspOutCreator.setStatus("current")
_RsIpsecSaEspOutEncapsulation_Type = IpsecDoiEncapsulationMode
_RsIpsecSaEspOutEncapsulation_Object = MibTableColumn
rsIpsecSaEspOutEncapsulation = _RsIpsecSaEspOutEncapsulation_Object(
    (1, 3, 6, 1, 4, 1, 4355, 3, 1, 1, 4, 1, 11),
    _RsIpsecSaEspOutEncapsulation_Type()
)
rsIpsecSaEspOutEncapsulation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsIpsecSaEspOutEncapsulation.setStatus("current")
_RsIpsecSaEspOutEncAlg_Type = IpsecDoiEspTransform
_RsIpsecSaEspOutEncAlg_Object = MibTableColumn
rsIpsecSaEspOutEncAlg = _RsIpsecSaEspOutEncAlg_Object(
    (1, 3, 6, 1, 4, 1, 4355, 3, 1, 1, 4, 1, 12),
    _RsIpsecSaEspOutEncAlg_Type()
)
rsIpsecSaEspOutEncAlg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsIpsecSaEspOutEncAlg.setStatus("current")


class _RsIpsecSaEspOutEncKeyLength_Type(Integer32):
    """Custom type rsIpsecSaEspOutEncKeyLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65531),
    )


_RsIpsecSaEspOutEncKeyLength_Type.__name__ = "Integer32"
_RsIpsecSaEspOutEncKeyLength_Object = MibTableColumn
rsIpsecSaEspOutEncKeyLength = _RsIpsecSaEspOutEncKeyLength_Object(
    (1, 3, 6, 1, 4, 1, 4355, 3, 1, 1, 4, 1, 13),
    _RsIpsecSaEspOutEncKeyLength_Type()
)
rsIpsecSaEspOutEncKeyLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsIpsecSaEspOutEncKeyLength.setStatus("current")
if mibBuilder.loadTexts:
    rsIpsecSaEspOutEncKeyLength.setUnits("bits")
_RsIpsecSaEspOutAuthAlg_Type = IpsecDoiAuthAlgorithm
_RsIpsecSaEspOutAuthAlg_Object = MibTableColumn
rsIpsecSaEspOutAuthAlg = _RsIpsecSaEspOutAuthAlg_Object(
    (1, 3, 6, 1, 4, 1, 4355, 3, 1, 1, 4, 1, 14),
    _RsIpsecSaEspOutAuthAlg_Type()
)
rsIpsecSaEspOutAuthAlg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsIpsecSaEspOutAuthAlg.setStatus("current")
_RsIpsecSaEspOutLimitSeconds_Type = Integer32
_RsIpsecSaEspOutLimitSeconds_Object = MibTableColumn
rsIpsecSaEspOutLimitSeconds = _RsIpsecSaEspOutLimitSeconds_Object(
    (1, 3, 6, 1, 4, 1, 4355, 3, 1, 1, 4, 1, 15),
    _RsIpsecSaEspOutLimitSeconds_Type()
)
rsIpsecSaEspOutLimitSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsIpsecSaEspOutLimitSeconds.setStatus("current")
if mibBuilder.loadTexts:
    rsIpsecSaEspOutLimitSeconds.setUnits("seconds")
_RsIpsecSaEspOutLimitKbytes_Type = Integer32
_RsIpsecSaEspOutLimitKbytes_Object = MibTableColumn
rsIpsecSaEspOutLimitKbytes = _RsIpsecSaEspOutLimitKbytes_Object(
    (1, 3, 6, 1, 4, 1, 4355, 3, 1, 1, 4, 1, 16),
    _RsIpsecSaEspOutLimitKbytes_Type()
)
rsIpsecSaEspOutLimitKbytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsIpsecSaEspOutLimitKbytes.setStatus("current")
if mibBuilder.loadTexts:
    rsIpsecSaEspOutLimitKbytes.setUnits("kilobytes")
_RsIpsecSaEspOutAccSeconds_Type = Counter32
_RsIpsecSaEspOutAccSeconds_Object = MibTableColumn
rsIpsecSaEspOutAccSeconds = _RsIpsecSaEspOutAccSeconds_Object(
    (1, 3, 6, 1, 4, 1, 4355, 3, 1, 1, 4, 1, 17),
    _RsIpsecSaEspOutAccSeconds_Type()
)
rsIpsecSaEspOutAccSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsIpsecSaEspOutAccSeconds.setStatus("current")
if mibBuilder.loadTexts:
    rsIpsecSaEspOutAccSeconds.setUnits("seconds")
_RsIpsecSaEspOutAccKbytes_Type = Counter32
_RsIpsecSaEspOutAccKbytes_Object = MibTableColumn
rsIpsecSaEspOutAccKbytes = _RsIpsecSaEspOutAccKbytes_Object(
    (1, 3, 6, 1, 4, 1, 4355, 3, 1, 1, 4, 1, 18),
    _RsIpsecSaEspOutAccKbytes_Type()
)
rsIpsecSaEspOutAccKbytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsIpsecSaEspOutAccKbytes.setStatus("current")
if mibBuilder.loadTexts:
    rsIpsecSaEspOutAccKbytes.setUnits("kilobytes")
_RsIpsecSaEspOutUserOctets_Type = Counter32
_RsIpsecSaEspOutUserOctets_Object = MibTableColumn
rsIpsecSaEspOutUserOctets = _RsIpsecSaEspOutUserOctets_Object(
    (1, 3, 6, 1, 4, 1, 4355, 3, 1, 1, 4, 1, 19),
    _RsIpsecSaEspOutUserOctets_Type()
)
rsIpsecSaEspOutUserOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsIpsecSaEspOutUserOctets.setStatus("current")
if mibBuilder.loadTexts:
    rsIpsecSaEspOutUserOctets.setUnits("bytes")
_RsIpsecSaEspOutPackets_Type = Counter32
_RsIpsecSaEspOutPackets_Object = MibTableColumn
rsIpsecSaEspOutPackets = _RsIpsecSaEspOutPackets_Object(
    (1, 3, 6, 1, 4, 1, 4355, 3, 1, 1, 4, 1, 20),
    _RsIpsecSaEspOutPackets_Type()
)
rsIpsecSaEspOutPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsIpsecSaEspOutPackets.setStatus("current")
_RsIpsecSaEspOutSendErrors_Type = Counter32
_RsIpsecSaEspOutSendErrors_Object = MibTableColumn
rsIpsecSaEspOutSendErrors = _RsIpsecSaEspOutSendErrors_Object(
    (1, 3, 6, 1, 4, 1, 4355, 3, 1, 1, 4, 1, 21),
    _RsIpsecSaEspOutSendErrors_Type()
)
rsIpsecSaEspOutSendErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsIpsecSaEspOutSendErrors.setStatus("current")
_RsIpsecSaAhOutTable_Object = MibTable
rsIpsecSaAhOutTable = _RsIpsecSaAhOutTable_Object(
    (1, 3, 6, 1, 4, 1, 4355, 3, 1, 1, 5)
)
if mibBuilder.loadTexts:
    rsIpsecSaAhOutTable.setStatus("current")
_RsIpsecSaAhOutEntry_Object = MibTableRow
rsIpsecSaAhOutEntry = _RsIpsecSaAhOutEntry_Object(
    (1, 3, 6, 1, 4, 1, 4355, 3, 1, 1, 5, 1)
)
rsIpsecSaAhOutEntry.setIndexNames(
    (0, "RAPID-IPSEC-SA-MON-MIB-EXT", "rsIpsecSaAhOutAddress"),
    (0, "RAPID-IPSEC-SA-MON-MIB-EXT", "rsIpsecSaAhOutSpi"),
)
if mibBuilder.loadTexts:
    rsIpsecSaAhOutEntry.setStatus("current")
_RsIpsecSaAhOutAddress_Type = IpAddress
_RsIpsecSaAhOutAddress_Object = MibTableColumn
rsIpsecSaAhOutAddress = _RsIpsecSaAhOutAddress_Object(
    (1, 3, 6, 1, 4, 1, 4355, 3, 1, 1, 5, 1, 1),
    _RsIpsecSaAhOutAddress_Type()
)
rsIpsecSaAhOutAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsIpsecSaAhOutAddress.setStatus("current")
_RsIpsecSaAhOutSpi_Type = Integer32
_RsIpsecSaAhOutSpi_Object = MibTableColumn
rsIpsecSaAhOutSpi = _RsIpsecSaAhOutSpi_Object(
    (1, 3, 6, 1, 4, 1, 4355, 3, 1, 1, 5, 1, 2),
    _RsIpsecSaAhOutSpi_Type()
)
rsIpsecSaAhOutSpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsIpsecSaAhOutSpi.setStatus("current")


class _RsIpsecSaAhOutSourceId_Type(OctetString):
    """Custom type rsIpsecSaAhOutSourceId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 255),
    )


_RsIpsecSaAhOutSourceId_Type.__name__ = "OctetString"
_RsIpsecSaAhOutSourceId_Object = MibTableColumn
rsIpsecSaAhOutSourceId = _RsIpsecSaAhOutSourceId_Object(
    (1, 3, 6, 1, 4, 1, 4355, 3, 1, 1, 5, 1, 3),
    _RsIpsecSaAhOutSourceId_Type()
)
rsIpsecSaAhOutSourceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsIpsecSaAhOutSourceId.setStatus("current")
_RsIpsecSaAhOutSourceIdType_Type = IpsecDoiIdentType
_RsIpsecSaAhOutSourceIdType_Object = MibTableColumn
rsIpsecSaAhOutSourceIdType = _RsIpsecSaAhOutSourceIdType_Object(
    (1, 3, 6, 1, 4, 1, 4355, 3, 1, 1, 5, 1, 4),
    _RsIpsecSaAhOutSourceIdType_Type()
)
rsIpsecSaAhOutSourceIdType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsIpsecSaAhOutSourceIdType.setStatus("current")


class _RsIpsecSaAhOutDestId_Type(OctetString):
    """Custom type rsIpsecSaAhOutDestId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 255),
    )


_RsIpsecSaAhOutDestId_Type.__name__ = "OctetString"
_RsIpsecSaAhOutDestId_Object = MibTableColumn
rsIpsecSaAhOutDestId = _RsIpsecSaAhOutDestId_Object(
    (1, 3, 6, 1, 4, 1, 4355, 3, 1, 1, 5, 1, 5),
    _RsIpsecSaAhOutDestId_Type()
)
rsIpsecSaAhOutDestId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsIpsecSaAhOutDestId.setStatus("current")
_RsIpsecSaAhOutDestIdType_Type = IpsecDoiIdentType
_RsIpsecSaAhOutDestIdType_Object = MibTableColumn
rsIpsecSaAhOutDestIdType = _RsIpsecSaAhOutDestIdType_Object(
    (1, 3, 6, 1, 4, 1, 4355, 3, 1, 1, 5, 1, 6),
    _RsIpsecSaAhOutDestIdType_Type()
)
rsIpsecSaAhOutDestIdType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsIpsecSaAhOutDestIdType.setStatus("current")


class _RsIpsecSaAhOutProtocol_Type(Integer32):
    """Custom type rsIpsecSaAhOutProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_RsIpsecSaAhOutProtocol_Type.__name__ = "Integer32"
_RsIpsecSaAhOutProtocol_Object = MibTableColumn
rsIpsecSaAhOutProtocol = _RsIpsecSaAhOutProtocol_Object(
    (1, 3, 6, 1, 4, 1, 4355, 3, 1, 1, 5, 1, 7),
    _RsIpsecSaAhOutProtocol_Type()
)
rsIpsecSaAhOutProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsIpsecSaAhOutProtocol.setStatus("current")


class _RsIpsecSaAhOutSourcePort_Type(Integer32):
    """Custom type rsIpsecSaAhOutSourcePort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RsIpsecSaAhOutSourcePort_Type.__name__ = "Integer32"
_RsIpsecSaAhOutSourcePort_Object = MibTableColumn
rsIpsecSaAhOutSourcePort = _RsIpsecSaAhOutSourcePort_Object(
    (1, 3, 6, 1, 4, 1, 4355, 3, 1, 1, 5, 1, 8),
    _RsIpsecSaAhOutSourcePort_Type()
)
rsIpsecSaAhOutSourcePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsIpsecSaAhOutSourcePort.setStatus("current")


class _RsIpsecSaAhOutDestPort_Type(Integer32):
    """Custom type rsIpsecSaAhOutDestPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RsIpsecSaAhOutDestPort_Type.__name__ = "Integer32"
_RsIpsecSaAhOutDestPort_Object = MibTableColumn
rsIpsecSaAhOutDestPort = _RsIpsecSaAhOutDestPort_Object(
    (1, 3, 6, 1, 4, 1, 4355, 3, 1, 1, 5, 1, 9),
    _RsIpsecSaAhOutDestPort_Type()
)
rsIpsecSaAhOutDestPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsIpsecSaAhOutDestPort.setStatus("current")
_RsIpsecSaAhOutCreator_Type = IpsecSaCreatorIdent
_RsIpsecSaAhOutCreator_Object = MibTableColumn
rsIpsecSaAhOutCreator = _RsIpsecSaAhOutCreator_Object(
    (1, 3, 6, 1, 4, 1, 4355, 3, 1, 1, 5, 1, 10),
    _RsIpsecSaAhOutCreator_Type()
)
rsIpsecSaAhOutCreator.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsIpsecSaAhOutCreator.setStatus("current")
_RsIpsecSaAhOutEncapsulation_Type = IpsecDoiEncapsulationMode
_RsIpsecSaAhOutEncapsulation_Object = MibTableColumn
rsIpsecSaAhOutEncapsulation = _RsIpsecSaAhOutEncapsulation_Object(
    (1, 3, 6, 1, 4, 1, 4355, 3, 1, 1, 5, 1, 11),
    _RsIpsecSaAhOutEncapsulation_Type()
)
rsIpsecSaAhOutEncapsulation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsIpsecSaAhOutEncapsulation.setStatus("current")
_RsIpsecSaAhOutAuthAlg_Type = IpsecDoiAhTransform
_RsIpsecSaAhOutAuthAlg_Object = MibTableColumn
rsIpsecSaAhOutAuthAlg = _RsIpsecSaAhOutAuthAlg_Object(
    (1, 3, 6, 1, 4, 1, 4355, 3, 1, 1, 5, 1, 12),
    _RsIpsecSaAhOutAuthAlg_Type()
)
rsIpsecSaAhOutAuthAlg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsIpsecSaAhOutAuthAlg.setStatus("current")
_RsIpsecSaAhOutLimitSeconds_Type = Integer32
_RsIpsecSaAhOutLimitSeconds_Object = MibTableColumn
rsIpsecSaAhOutLimitSeconds = _RsIpsecSaAhOutLimitSeconds_Object(
    (1, 3, 6, 1, 4, 1, 4355, 3, 1, 1, 5, 1, 13),
    _RsIpsecSaAhOutLimitSeconds_Type()
)
rsIpsecSaAhOutLimitSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsIpsecSaAhOutLimitSeconds.setStatus("current")
if mibBuilder.loadTexts:
    rsIpsecSaAhOutLimitSeconds.setUnits("seconds")
_RsIpsecSaAhOutLimitKbytes_Type = Integer32
_RsIpsecSaAhOutLimitKbytes_Object = MibTableColumn
rsIpsecSaAhOutLimitKbytes = _RsIpsecSaAhOutLimitKbytes_Object(
    (1, 3, 6, 1, 4, 1, 4355, 3, 1, 1, 5, 1, 14),
    _RsIpsecSaAhOutLimitKbytes_Type()
)
rsIpsecSaAhOutLimitKbytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsIpsecSaAhOutLimitKbytes.setStatus("current")
if mibBuilder.loadTexts:
    rsIpsecSaAhOutLimitKbytes.setUnits("kilobytes")
_RsIpsecSaAhOutAccSeconds_Type = Counter32
_RsIpsecSaAhOutAccSeconds_Object = MibTableColumn
rsIpsecSaAhOutAccSeconds = _RsIpsecSaAhOutAccSeconds_Object(
    (1, 3, 6, 1, 4, 1, 4355, 3, 1, 1, 5, 1, 15),
    _RsIpsecSaAhOutAccSeconds_Type()
)
rsIpsecSaAhOutAccSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsIpsecSaAhOutAccSeconds.setStatus("current")
if mibBuilder.loadTexts:
    rsIpsecSaAhOutAccSeconds.setUnits("seconds")
_RsIpsecSaAhOutAccKbytes_Type = Counter32
_RsIpsecSaAhOutAccKbytes_Object = MibTableColumn
rsIpsecSaAhOutAccKbytes = _RsIpsecSaAhOutAccKbytes_Object(
    (1, 3, 6, 1, 4, 1, 4355, 3, 1, 1, 5, 1, 16),
    _RsIpsecSaAhOutAccKbytes_Type()
)
rsIpsecSaAhOutAccKbytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsIpsecSaAhOutAccKbytes.setStatus("current")
if mibBuilder.loadTexts:
    rsIpsecSaAhOutAccKbytes.setUnits("kilobytes")
_RsIpsecSaAhOutUserOctets_Type = Counter32
_RsIpsecSaAhOutUserOctets_Object = MibTableColumn
rsIpsecSaAhOutUserOctets = _RsIpsecSaAhOutUserOctets_Object(
    (1, 3, 6, 1, 4, 1, 4355, 3, 1, 1, 5, 1, 17),
    _RsIpsecSaAhOutUserOctets_Type()
)
rsIpsecSaAhOutUserOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsIpsecSaAhOutUserOctets.setStatus("current")
if mibBuilder.loadTexts:
    rsIpsecSaAhOutUserOctets.setUnits("bytes")
_RsIpsecSaAhOutPackets_Type = Counter32
_RsIpsecSaAhOutPackets_Object = MibTableColumn
rsIpsecSaAhOutPackets = _RsIpsecSaAhOutPackets_Object(
    (1, 3, 6, 1, 4, 1, 4355, 3, 1, 1, 5, 1, 18),
    _RsIpsecSaAhOutPackets_Type()
)
rsIpsecSaAhOutPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsIpsecSaAhOutPackets.setStatus("current")
_RsIpsecSaAhOutSendErrors_Type = Counter32
_RsIpsecSaAhOutSendErrors_Object = MibTableColumn
rsIpsecSaAhOutSendErrors = _RsIpsecSaAhOutSendErrors_Object(
    (1, 3, 6, 1, 4, 1, 4355, 3, 1, 1, 5, 1, 19),
    _RsIpsecSaAhOutSendErrors_Type()
)
rsIpsecSaAhOutSendErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsIpsecSaAhOutSendErrors.setStatus("current")
_RsIpsecSaIpcompOutTable_Object = MibTable
rsIpsecSaIpcompOutTable = _RsIpsecSaIpcompOutTable_Object(
    (1, 3, 6, 1, 4, 1, 4355, 3, 1, 1, 6)
)
if mibBuilder.loadTexts:
    rsIpsecSaIpcompOutTable.setStatus("current")
_RsIpsecSaIpcompOutEntry_Object = MibTableRow
rsIpsecSaIpcompOutEntry = _RsIpsecSaIpcompOutEntry_Object(
    (1, 3, 6, 1, 4, 1, 4355, 3, 1, 1, 6, 1)
)
rsIpsecSaIpcompOutEntry.setIndexNames(
    (0, "RAPID-IPSEC-SA-MON-MIB-EXT", "rsIpsecSaIpcompOutAddress"),
    (0, "RAPID-IPSEC-SA-MON-MIB-EXT", "rsIpsecSaIpcompOutCpi"),
)
if mibBuilder.loadTexts:
    rsIpsecSaIpcompOutEntry.setStatus("current")
_RsIpsecSaIpcompOutAddress_Type = IpAddress
_RsIpsecSaIpcompOutAddress_Object = MibTableColumn
rsIpsecSaIpcompOutAddress = _RsIpsecSaIpcompOutAddress_Object(
    (1, 3, 6, 1, 4, 1, 4355, 3, 1, 1, 6, 1, 1),
    _RsIpsecSaIpcompOutAddress_Type()
)
rsIpsecSaIpcompOutAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsIpsecSaIpcompOutAddress.setStatus("current")
_RsIpsecSaIpcompOutCpi_Type = IpsecDoiIpcompTransform
_RsIpsecSaIpcompOutCpi_Object = MibTableColumn
rsIpsecSaIpcompOutCpi = _RsIpsecSaIpcompOutCpi_Object(
    (1, 3, 6, 1, 4, 1, 4355, 3, 1, 1, 6, 1, 2),
    _RsIpsecSaIpcompOutCpi_Type()
)
rsIpsecSaIpcompOutCpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsIpsecSaIpcompOutCpi.setStatus("current")


class _RsIpsecSaIpcompOutSourceId_Type(OctetString):
    """Custom type rsIpsecSaIpcompOutSourceId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 255),
    )


_RsIpsecSaIpcompOutSourceId_Type.__name__ = "OctetString"
_RsIpsecSaIpcompOutSourceId_Object = MibTableColumn
rsIpsecSaIpcompOutSourceId = _RsIpsecSaIpcompOutSourceId_Object(
    (1, 3, 6, 1, 4, 1, 4355, 3, 1, 1, 6, 1, 3),
    _RsIpsecSaIpcompOutSourceId_Type()
)
rsIpsecSaIpcompOutSourceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsIpsecSaIpcompOutSourceId.setStatus("current")
_RsIpsecSaIpcompOutSourceIdType_Type = IpsecDoiIdentType
_RsIpsecSaIpcompOutSourceIdType_Object = MibTableColumn
rsIpsecSaIpcompOutSourceIdType = _RsIpsecSaIpcompOutSourceIdType_Object(
    (1, 3, 6, 1, 4, 1, 4355, 3, 1, 1, 6, 1, 4),
    _RsIpsecSaIpcompOutSourceIdType_Type()
)
rsIpsecSaIpcompOutSourceIdType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsIpsecSaIpcompOutSourceIdType.setStatus("current")


class _RsIpsecSaIpcompOutDestId_Type(OctetString):
    """Custom type rsIpsecSaIpcompOutDestId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 255),
    )


_RsIpsecSaIpcompOutDestId_Type.__name__ = "OctetString"
_RsIpsecSaIpcompOutDestId_Object = MibTableColumn
rsIpsecSaIpcompOutDestId = _RsIpsecSaIpcompOutDestId_Object(
    (1, 3, 6, 1, 4, 1, 4355, 3, 1, 1, 6, 1, 5),
    _RsIpsecSaIpcompOutDestId_Type()
)
rsIpsecSaIpcompOutDestId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsIpsecSaIpcompOutDestId.setStatus("current")
_RsIpsecSaIpcompOutDestIdType_Type = IpsecDoiIdentType
_RsIpsecSaIpcompOutDestIdType_Object = MibTableColumn
rsIpsecSaIpcompOutDestIdType = _RsIpsecSaIpcompOutDestIdType_Object(
    (1, 3, 6, 1, 4, 1, 4355, 3, 1, 1, 6, 1, 6),
    _RsIpsecSaIpcompOutDestIdType_Type()
)
rsIpsecSaIpcompOutDestIdType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsIpsecSaIpcompOutDestIdType.setStatus("current")


class _RsIpsecSaIpcompOutProtocol_Type(Integer32):
    """Custom type rsIpsecSaIpcompOutProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_RsIpsecSaIpcompOutProtocol_Type.__name__ = "Integer32"
_RsIpsecSaIpcompOutProtocol_Object = MibTableColumn
rsIpsecSaIpcompOutProtocol = _RsIpsecSaIpcompOutProtocol_Object(
    (1, 3, 6, 1, 4, 1, 4355, 3, 1, 1, 6, 1, 7),
    _RsIpsecSaIpcompOutProtocol_Type()
)
rsIpsecSaIpcompOutProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsIpsecSaIpcompOutProtocol.setStatus("current")


class _RsIpsecSaIpcompOutSourcePort_Type(Integer32):
    """Custom type rsIpsecSaIpcompOutSourcePort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RsIpsecSaIpcompOutSourcePort_Type.__name__ = "Integer32"
_RsIpsecSaIpcompOutSourcePort_Object = MibTableColumn
rsIpsecSaIpcompOutSourcePort = _RsIpsecSaIpcompOutSourcePort_Object(
    (1, 3, 6, 1, 4, 1, 4355, 3, 1, 1, 6, 1, 8),
    _RsIpsecSaIpcompOutSourcePort_Type()
)
rsIpsecSaIpcompOutSourcePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsIpsecSaIpcompOutSourcePort.setStatus("current")


class _RsIpsecSaIpcompOutDestPort_Type(Integer32):
    """Custom type rsIpsecSaIpcompOutDestPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RsIpsecSaIpcompOutDestPort_Type.__name__ = "Integer32"
_RsIpsecSaIpcompOutDestPort_Object = MibTableColumn
rsIpsecSaIpcompOutDestPort = _RsIpsecSaIpcompOutDestPort_Object(
    (1, 3, 6, 1, 4, 1, 4355, 3, 1, 1, 6, 1, 9),
    _RsIpsecSaIpcompOutDestPort_Type()
)
rsIpsecSaIpcompOutDestPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsIpsecSaIpcompOutDestPort.setStatus("current")
_RsIpsecSaIpcompOutCreator_Type = IpsecSaCreatorIdent
_RsIpsecSaIpcompOutCreator_Object = MibTableColumn
rsIpsecSaIpcompOutCreator = _RsIpsecSaIpcompOutCreator_Object(
    (1, 3, 6, 1, 4, 1, 4355, 3, 1, 1, 6, 1, 10),
    _RsIpsecSaIpcompOutCreator_Type()
)
rsIpsecSaIpcompOutCreator.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsIpsecSaIpcompOutCreator.setStatus("current")
_RsIpsecSaIpcompOutEncapsulation_Type = IpsecDoiEncapsulationMode
_RsIpsecSaIpcompOutEncapsulation_Object = MibTableColumn
rsIpsecSaIpcompOutEncapsulation = _RsIpsecSaIpcompOutEncapsulation_Object(
    (1, 3, 6, 1, 4, 1, 4355, 3, 1, 1, 6, 1, 11),
    _RsIpsecSaIpcompOutEncapsulation_Type()
)
rsIpsecSaIpcompOutEncapsulation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsIpsecSaIpcompOutEncapsulation.setStatus("current")
_RsIpsecSaIpcompOutCompAlg_Type = IpsecDoiIpcompTransform
_RsIpsecSaIpcompOutCompAlg_Object = MibTableColumn
rsIpsecSaIpcompOutCompAlg = _RsIpsecSaIpcompOutCompAlg_Object(
    (1, 3, 6, 1, 4, 1, 4355, 3, 1, 1, 6, 1, 12),
    _RsIpsecSaIpcompOutCompAlg_Type()
)
rsIpsecSaIpcompOutCompAlg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsIpsecSaIpcompOutCompAlg.setStatus("current")
_RsIpsecSaIpcompOutSeconds_Type = Counter32
_RsIpsecSaIpcompOutSeconds_Object = MibTableColumn
rsIpsecSaIpcompOutSeconds = _RsIpsecSaIpcompOutSeconds_Object(
    (1, 3, 6, 1, 4, 1, 4355, 3, 1, 1, 6, 1, 13),
    _RsIpsecSaIpcompOutSeconds_Type()
)
rsIpsecSaIpcompOutSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsIpsecSaIpcompOutSeconds.setStatus("current")
if mibBuilder.loadTexts:
    rsIpsecSaIpcompOutSeconds.setUnits("seconds")
_RsIpsecSaIpcompOutUserOctets_Type = Counter32
_RsIpsecSaIpcompOutUserOctets_Object = MibTableColumn
rsIpsecSaIpcompOutUserOctets = _RsIpsecSaIpcompOutUserOctets_Object(
    (1, 3, 6, 1, 4, 1, 4355, 3, 1, 1, 6, 1, 14),
    _RsIpsecSaIpcompOutUserOctets_Type()
)
rsIpsecSaIpcompOutUserOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsIpsecSaIpcompOutUserOctets.setStatus("current")
if mibBuilder.loadTexts:
    rsIpsecSaIpcompOutUserOctets.setUnits("bytes")
_RsIpsecSaIpcompOutPackets_Type = Counter32
_RsIpsecSaIpcompOutPackets_Object = MibTableColumn
rsIpsecSaIpcompOutPackets = _RsIpsecSaIpcompOutPackets_Object(
    (1, 3, 6, 1, 4, 1, 4355, 3, 1, 1, 6, 1, 15),
    _RsIpsecSaIpcompOutPackets_Type()
)
rsIpsecSaIpcompOutPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsIpsecSaIpcompOutPackets.setStatus("current")
_RsSaStatistics_ObjectIdentity = ObjectIdentity
rsSaStatistics = _RsSaStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4355, 3, 1, 2)
)
if mibBuilder.loadTexts:
    rsSaStatistics.setStatus("current")
_RsIpsecEspCurrentInboundSAs_Type = Gauge32
_RsIpsecEspCurrentInboundSAs_Object = MibScalar
rsIpsecEspCurrentInboundSAs = _RsIpsecEspCurrentInboundSAs_Object(
    (1, 3, 6, 1, 4, 1, 4355, 3, 1, 2, 1),
    _RsIpsecEspCurrentInboundSAs_Type()
)
rsIpsecEspCurrentInboundSAs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsIpsecEspCurrentInboundSAs.setStatus("current")
_RsIpsecEspTotalInboundSAs_Type = Counter32
_RsIpsecEspTotalInboundSAs_Object = MibScalar
rsIpsecEspTotalInboundSAs = _RsIpsecEspTotalInboundSAs_Object(
    (1, 3, 6, 1, 4, 1, 4355, 3, 1, 2, 2),
    _RsIpsecEspTotalInboundSAs_Type()
)
rsIpsecEspTotalInboundSAs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsIpsecEspTotalInboundSAs.setStatus("current")
_RsIpsecEspCurrentOutboundSAs_Type = Gauge32
_RsIpsecEspCurrentOutboundSAs_Object = MibScalar
rsIpsecEspCurrentOutboundSAs = _RsIpsecEspCurrentOutboundSAs_Object(
    (1, 3, 6, 1, 4, 1, 4355, 3, 1, 2, 3),
    _RsIpsecEspCurrentOutboundSAs_Type()
)
rsIpsecEspCurrentOutboundSAs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsIpsecEspCurrentOutboundSAs.setStatus("current")
_RsIpsecEspTotalOutboundSAs_Type = Counter32
_RsIpsecEspTotalOutboundSAs_Object = MibScalar
rsIpsecEspTotalOutboundSAs = _RsIpsecEspTotalOutboundSAs_Object(
    (1, 3, 6, 1, 4, 1, 4355, 3, 1, 2, 4),
    _RsIpsecEspTotalOutboundSAs_Type()
)
rsIpsecEspTotalOutboundSAs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsIpsecEspTotalOutboundSAs.setStatus("current")
_RsIpsecAhCurrentInboundSAs_Type = Gauge32
_RsIpsecAhCurrentInboundSAs_Object = MibScalar
rsIpsecAhCurrentInboundSAs = _RsIpsecAhCurrentInboundSAs_Object(
    (1, 3, 6, 1, 4, 1, 4355, 3, 1, 2, 5),
    _RsIpsecAhCurrentInboundSAs_Type()
)
rsIpsecAhCurrentInboundSAs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsIpsecAhCurrentInboundSAs.setStatus("current")
_RsIpsecAhTotalInboundSAs_Type = Counter32
_RsIpsecAhTotalInboundSAs_Object = MibScalar
rsIpsecAhTotalInboundSAs = _RsIpsecAhTotalInboundSAs_Object(
    (1, 3, 6, 1, 4, 1, 4355, 3, 1, 2, 6),
    _RsIpsecAhTotalInboundSAs_Type()
)
rsIpsecAhTotalInboundSAs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsIpsecAhTotalInboundSAs.setStatus("current")
_RsIpsecAhCurrentOutboundSAs_Type = Gauge32
_RsIpsecAhCurrentOutboundSAs_Object = MibScalar
rsIpsecAhCurrentOutboundSAs = _RsIpsecAhCurrentOutboundSAs_Object(
    (1, 3, 6, 1, 4, 1, 4355, 3, 1, 2, 7),
    _RsIpsecAhCurrentOutboundSAs_Type()
)
rsIpsecAhCurrentOutboundSAs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsIpsecAhCurrentOutboundSAs.setStatus("current")
_RsIpsecAhTotalOutboundSAs_Type = Counter32
_RsIpsecAhTotalOutboundSAs_Object = MibScalar
rsIpsecAhTotalOutboundSAs = _RsIpsecAhTotalOutboundSAs_Object(
    (1, 3, 6, 1, 4, 1, 4355, 3, 1, 2, 8),
    _RsIpsecAhTotalOutboundSAs_Type()
)
rsIpsecAhTotalOutboundSAs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsIpsecAhTotalOutboundSAs.setStatus("current")
_RsIpsecIpcompCurrentInboundSAs_Type = Gauge32
_RsIpsecIpcompCurrentInboundSAs_Object = MibScalar
rsIpsecIpcompCurrentInboundSAs = _RsIpsecIpcompCurrentInboundSAs_Object(
    (1, 3, 6, 1, 4, 1, 4355, 3, 1, 2, 9),
    _RsIpsecIpcompCurrentInboundSAs_Type()
)
rsIpsecIpcompCurrentInboundSAs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsIpsecIpcompCurrentInboundSAs.setStatus("current")
_RsIpsecIpcompTotalInboundSAs_Type = Counter32
_RsIpsecIpcompTotalInboundSAs_Object = MibScalar
rsIpsecIpcompTotalInboundSAs = _RsIpsecIpcompTotalInboundSAs_Object(
    (1, 3, 6, 1, 4, 1, 4355, 3, 1, 2, 10),
    _RsIpsecIpcompTotalInboundSAs_Type()
)
rsIpsecIpcompTotalInboundSAs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsIpsecIpcompTotalInboundSAs.setStatus("current")
_RsIpsecIpcompCurrentOutboundSAs_Type = Gauge32
_RsIpsecIpcompCurrentOutboundSAs_Object = MibScalar
rsIpsecIpcompCurrentOutboundSAs = _RsIpsecIpcompCurrentOutboundSAs_Object(
    (1, 3, 6, 1, 4, 1, 4355, 3, 1, 2, 11),
    _RsIpsecIpcompCurrentOutboundSAs_Type()
)
rsIpsecIpcompCurrentOutboundSAs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsIpsecIpcompCurrentOutboundSAs.setStatus("current")
_RsIpsecIpcompTotalOutboundSAs_Type = Counter32
_RsIpsecIpcompTotalOutboundSAs_Object = MibScalar
rsIpsecIpcompTotalOutboundSAs = _RsIpsecIpcompTotalOutboundSAs_Object(
    (1, 3, 6, 1, 4, 1, 4355, 3, 1, 2, 12),
    _RsIpsecIpcompTotalOutboundSAs_Type()
)
rsIpsecIpcompTotalOutboundSAs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsIpsecIpcompTotalOutboundSAs.setStatus("current")
_RsSaErrors_ObjectIdentity = ObjectIdentity
rsSaErrors = _RsSaErrors_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4355, 3, 1, 3)
)
if mibBuilder.loadTexts:
    rsSaErrors.setStatus("current")
_RsIpsecDecryptionErrors_Type = Counter32
_RsIpsecDecryptionErrors_Object = MibScalar
rsIpsecDecryptionErrors = _RsIpsecDecryptionErrors_Object(
    (1, 3, 6, 1, 4, 1, 4355, 3, 1, 3, 1),
    _RsIpsecDecryptionErrors_Type()
)
rsIpsecDecryptionErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsIpsecDecryptionErrors.setStatus("current")
_RsIpsecAuthenticationErrors_Type = Counter32
_RsIpsecAuthenticationErrors_Object = MibScalar
rsIpsecAuthenticationErrors = _RsIpsecAuthenticationErrors_Object(
    (1, 3, 6, 1, 4, 1, 4355, 3, 1, 3, 2),
    _RsIpsecAuthenticationErrors_Type()
)
rsIpsecAuthenticationErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsIpsecAuthenticationErrors.setStatus("current")
_RsIpsecReplayErrors_Type = Counter32
_RsIpsecReplayErrors_Object = MibScalar
rsIpsecReplayErrors = _RsIpsecReplayErrors_Object(
    (1, 3, 6, 1, 4, 1, 4355, 3, 1, 3, 3),
    _RsIpsecReplayErrors_Type()
)
rsIpsecReplayErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsIpsecReplayErrors.setStatus("current")
_RsIpsecPolicyErrors_Type = Counter32
_RsIpsecPolicyErrors_Object = MibScalar
rsIpsecPolicyErrors = _RsIpsecPolicyErrors_Object(
    (1, 3, 6, 1, 4, 1, 4355, 3, 1, 3, 4),
    _RsIpsecPolicyErrors_Type()
)
rsIpsecPolicyErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsIpsecPolicyErrors.setStatus("current")
_RsIpsecOtherReceiveErrors_Type = Counter32
_RsIpsecOtherReceiveErrors_Object = MibScalar
rsIpsecOtherReceiveErrors = _RsIpsecOtherReceiveErrors_Object(
    (1, 3, 6, 1, 4, 1, 4355, 3, 1, 3, 5),
    _RsIpsecOtherReceiveErrors_Type()
)
rsIpsecOtherReceiveErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsIpsecOtherReceiveErrors.setStatus("current")
_RsIpsecSendErrors_Type = Counter32
_RsIpsecSendErrors_Object = MibScalar
rsIpsecSendErrors = _RsIpsecSendErrors_Object(
    (1, 3, 6, 1, 4, 1, 4355, 3, 1, 3, 6),
    _RsIpsecSendErrors_Type()
)
rsIpsecSendErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsIpsecSendErrors.setStatus("current")
_RsIpsecUnknownSpiErrors_Type = Counter32
_RsIpsecUnknownSpiErrors_Object = MibScalar
rsIpsecUnknownSpiErrors = _RsIpsecUnknownSpiErrors_Object(
    (1, 3, 6, 1, 4, 1, 4355, 3, 1, 3, 7),
    _RsIpsecUnknownSpiErrors_Type()
)
rsIpsecUnknownSpiErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsIpsecUnknownSpiErrors.setStatus("current")
_RsSaTraps_ObjectIdentity = ObjectIdentity
rsSaTraps = _RsSaTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4355, 3, 1, 4)
)
if mibBuilder.loadTexts:
    rsSaTraps.setStatus("current")
_RsSaTrapObjects_ObjectIdentity = ObjectIdentity
rsSaTrapObjects = _RsSaTrapObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4355, 3, 1, 5)
)
if mibBuilder.loadTexts:
    rsSaTrapObjects.setStatus("current")
_RsIpsecSecurityProtocol_Type = IpsecDoiSecProtocolId
_RsIpsecSecurityProtocol_Object = MibScalar
rsIpsecSecurityProtocol = _RsIpsecSecurityProtocol_Object(
    (1, 3, 6, 1, 4, 1, 4355, 3, 1, 5, 1),
    _RsIpsecSecurityProtocol_Type()
)
rsIpsecSecurityProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsIpsecSecurityProtocol.setStatus("current")
_RsIpsecSPI_Type = Integer32
_RsIpsecSPI_Object = MibScalar
rsIpsecSPI = _RsIpsecSPI_Object(
    (1, 3, 6, 1, 4, 1, 4355, 3, 1, 5, 2),
    _RsIpsecSPI_Type()
)
rsIpsecSPI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsIpsecSPI.setStatus("current")
_RsIpsecLocalAddress_Type = IpAddress
_RsIpsecLocalAddress_Object = MibScalar
rsIpsecLocalAddress = _RsIpsecLocalAddress_Object(
    (1, 3, 6, 1, 4, 1, 4355, 3, 1, 5, 3),
    _RsIpsecLocalAddress_Type()
)
rsIpsecLocalAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsIpsecLocalAddress.setStatus("current")
_RsIpsecPeerAddress_Type = IpAddress
_RsIpsecPeerAddress_Object = MibScalar
rsIpsecPeerAddress = _RsIpsecPeerAddress_Object(
    (1, 3, 6, 1, 4, 1, 4355, 3, 1, 5, 4),
    _RsIpsecPeerAddress_Type()
)
rsIpsecPeerAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsIpsecPeerAddress.setStatus("current")
_RsSaTrapControl_ObjectIdentity = ObjectIdentity
rsSaTrapControl = _RsSaTrapControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4355, 3, 1, 6)
)
if mibBuilder.loadTexts:
    rsSaTrapControl.setStatus("current")


class _RsEspAuthFailureTrapEnable_Type(TruthValue):
    """Custom type rsEspAuthFailureTrapEnable based on TruthValue"""


_RsEspAuthFailureTrapEnable_Object = MibScalar
rsEspAuthFailureTrapEnable = _RsEspAuthFailureTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 4355, 3, 1, 6, 1),
    _RsEspAuthFailureTrapEnable_Type()
)
rsEspAuthFailureTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsEspAuthFailureTrapEnable.setStatus("current")


class _RsAhAuthFailureTrapEnable_Type(TruthValue):
    """Custom type rsAhAuthFailureTrapEnable based on TruthValue"""


_RsAhAuthFailureTrapEnable_Object = MibScalar
rsAhAuthFailureTrapEnable = _RsAhAuthFailureTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 4355, 3, 1, 6, 2),
    _RsAhAuthFailureTrapEnable_Type()
)
rsAhAuthFailureTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsAhAuthFailureTrapEnable.setStatus("current")


class _RsEspReplayFailureTrapEnable_Type(TruthValue):
    """Custom type rsEspReplayFailureTrapEnable based on TruthValue"""


_RsEspReplayFailureTrapEnable_Object = MibScalar
rsEspReplayFailureTrapEnable = _RsEspReplayFailureTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 4355, 3, 1, 6, 3),
    _RsEspReplayFailureTrapEnable_Type()
)
rsEspReplayFailureTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsEspReplayFailureTrapEnable.setStatus("current")


class _RsAhReplayFailureTrapEnable_Type(TruthValue):
    """Custom type rsAhReplayFailureTrapEnable based on TruthValue"""


_RsAhReplayFailureTrapEnable_Object = MibScalar
rsAhReplayFailureTrapEnable = _RsAhReplayFailureTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 4355, 3, 1, 6, 4),
    _RsAhReplayFailureTrapEnable_Type()
)
rsAhReplayFailureTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsAhReplayFailureTrapEnable.setStatus("current")


class _RsEspPolicyFailureTrapEnable_Type(TruthValue):
    """Custom type rsEspPolicyFailureTrapEnable based on TruthValue"""


_RsEspPolicyFailureTrapEnable_Object = MibScalar
rsEspPolicyFailureTrapEnable = _RsEspPolicyFailureTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 4355, 3, 1, 6, 5),
    _RsEspPolicyFailureTrapEnable_Type()
)
rsEspPolicyFailureTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsEspPolicyFailureTrapEnable.setStatus("current")


class _RsAhPolicyFailureTrapEnable_Type(TruthValue):
    """Custom type rsAhPolicyFailureTrapEnable based on TruthValue"""


_RsAhPolicyFailureTrapEnable_Object = MibScalar
rsAhPolicyFailureTrapEnable = _RsAhPolicyFailureTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 4355, 3, 1, 6, 6),
    _RsAhPolicyFailureTrapEnable_Type()
)
rsAhPolicyFailureTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsAhPolicyFailureTrapEnable.setStatus("current")


class _RsInvalidSpiTrapEnable_Type(TruthValue):
    """Custom type rsInvalidSpiTrapEnable based on TruthValue"""


_RsInvalidSpiTrapEnable_Object = MibScalar
rsInvalidSpiTrapEnable = _RsInvalidSpiTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 4355, 3, 1, 6, 7),
    _RsInvalidSpiTrapEnable_Type()
)
rsInvalidSpiTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsInvalidSpiTrapEnable.setStatus("current")
_RsSaGroups_ObjectIdentity = ObjectIdentity
rsSaGroups = _RsSaGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4355, 3, 1, 7)
)
if mibBuilder.loadTexts:
    rsSaGroups.setStatus("current")
_RsSaConformance_ObjectIdentity = ObjectIdentity
rsSaConformance = _RsSaConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4355, 3, 1, 8)
)
if mibBuilder.loadTexts:
    rsSaConformance.setStatus("current")

# Managed Objects groups


# Notification objects

rsEspAuthFailureTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 4355, 3, 1, 4, 0, 1)
)
rsEspAuthFailureTrap.setObjects(
    ("RAPID-IPSEC-SA-MON-MIB-EXT", "rsIpsecSaEspInAuthErrors")
)
if mibBuilder.loadTexts:
    rsEspAuthFailureTrap.setStatus(
        "current"
    )

rsAhAuthFailureTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 4355, 3, 1, 4, 0, 2)
)
rsAhAuthFailureTrap.setObjects(
    ("RAPID-IPSEC-SA-MON-MIB-EXT", "rsIpsecSaAhInAuthErrors")
)
if mibBuilder.loadTexts:
    rsAhAuthFailureTrap.setStatus(
        "current"
    )

rsEspReplayFailureTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 4355, 3, 1, 4, 0, 3)
)
rsEspReplayFailureTrap.setObjects(
    ("RAPID-IPSEC-SA-MON-MIB-EXT", "rsIpsecSaEspInReplayErrors")
)
if mibBuilder.loadTexts:
    rsEspReplayFailureTrap.setStatus(
        "current"
    )

rsAhReplayFailureTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 4355, 3, 1, 4, 0, 4)
)
rsAhReplayFailureTrap.setObjects(
    ("RAPID-IPSEC-SA-MON-MIB-EXT", "rsIpsecSaAhInReplayErrors")
)
if mibBuilder.loadTexts:
    rsAhReplayFailureTrap.setStatus(
        "current"
    )

rsEspPolicyFailureTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 4355, 3, 1, 4, 0, 5)
)
rsEspPolicyFailureTrap.setObjects(
    ("RAPID-IPSEC-SA-MON-MIB-EXT", "rsIpsecSaEspInPolicyErrors")
)
if mibBuilder.loadTexts:
    rsEspPolicyFailureTrap.setStatus(
        "current"
    )

rsAhPolicyFailureTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 4355, 3, 1, 4, 0, 6)
)
rsAhPolicyFailureTrap.setObjects(
    ("RAPID-IPSEC-SA-MON-MIB-EXT", "rsIpsecSaAhInPolicyErrors")
)
if mibBuilder.loadTexts:
    rsAhPolicyFailureTrap.setStatus(
        "current"
    )

rsInvalidSpiTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 4355, 3, 1, 4, 0, 7)
)
rsInvalidSpiTrap.setObjects(
      *(("RAPID-IPSEC-SA-MON-MIB-EXT", "rsIpsecLocalAddress"),
        ("RAPID-IPSEC-SA-MON-MIB-EXT", "rsIpsecSecurityProtocol"),
        ("RAPID-IPSEC-SA-MON-MIB-EXT", "rsIpsecPeerAddress"),
        ("RAPID-IPSEC-SA-MON-MIB-EXT", "rsIpsecSPI"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    rsInvalidSpiTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RAPID-IPSEC-SA-MON-MIB-EXT",
    **{"IpsecSaCreatorIdent": IpsecSaCreatorIdent,
       "IpsecIpv6Address": IpsecIpv6Address,
       "rsIpsecSaMonModule": rsIpsecSaMonModule,
       "rsIpsecSaMonitorMIB": rsIpsecSaMonitorMIB,
       "rsSaTables": rsSaTables,
       "rsIpsecSaEspInTable": rsIpsecSaEspInTable,
       "rsIpsecSaEspInEntry": rsIpsecSaEspInEntry,
       "rsIpsecSaEspInAddress": rsIpsecSaEspInAddress,
       "rsIpsecSaEspInSpi": rsIpsecSaEspInSpi,
       "rsIpsecSaEspInDestId": rsIpsecSaEspInDestId,
       "rsIpsecSaEspInDestIdType": rsIpsecSaEspInDestIdType,
       "rsIpsecSaEspInSourceId": rsIpsecSaEspInSourceId,
       "rsIpsecSaEspInSourceIdType": rsIpsecSaEspInSourceIdType,
       "rsIpsecSaEspInProtocol": rsIpsecSaEspInProtocol,
       "rsIpsecSaEspInDestPort": rsIpsecSaEspInDestPort,
       "rsIpsecSaEspInSourcePort": rsIpsecSaEspInSourcePort,
       "rsIpsecSaEspInCreator": rsIpsecSaEspInCreator,
       "rsIpsecSaEspInEncapsulation": rsIpsecSaEspInEncapsulation,
       "rsIpsecSaEspInEncAlg": rsIpsecSaEspInEncAlg,
       "rsIpsecSaEspInEncKeyLength": rsIpsecSaEspInEncKeyLength,
       "rsIpsecSaEspInAuthAlg": rsIpsecSaEspInAuthAlg,
       "rsIpsecSaEspInLimitSeconds": rsIpsecSaEspInLimitSeconds,
       "rsIpsecSaEspInLimitKbytes": rsIpsecSaEspInLimitKbytes,
       "rsIpsecSaEspInAccSeconds": rsIpsecSaEspInAccSeconds,
       "rsIpsecSaEspInAccKbytes": rsIpsecSaEspInAccKbytes,
       "rsIpsecSaEspInUserOctets": rsIpsecSaEspInUserOctets,
       "rsIpsecSaEspInPackets": rsIpsecSaEspInPackets,
       "rsIpsecSaEspInDecryptErrors": rsIpsecSaEspInDecryptErrors,
       "rsIpsecSaEspInAuthErrors": rsIpsecSaEspInAuthErrors,
       "rsIpsecSaEspInReplayErrors": rsIpsecSaEspInReplayErrors,
       "rsIpsecSaEspInPolicyErrors": rsIpsecSaEspInPolicyErrors,
       "rsIpsecSaEspInPadErrors": rsIpsecSaEspInPadErrors,
       "rsIpsecSaEspInOtherReceiveErrors": rsIpsecSaEspInOtherReceiveErrors,
       "rsIpsecSaAhInTable": rsIpsecSaAhInTable,
       "rsIpsecSaAhInEntry": rsIpsecSaAhInEntry,
       "rsIpsecSaAhInAddress": rsIpsecSaAhInAddress,
       "rsIpsecSaAhInSpi": rsIpsecSaAhInSpi,
       "rsIpsecSaAhInDestId": rsIpsecSaAhInDestId,
       "rsIpsecSaAhInDestIdType": rsIpsecSaAhInDestIdType,
       "rsIpsecSaAhInSourceId": rsIpsecSaAhInSourceId,
       "rsIpsecSaAhInSourceIdType": rsIpsecSaAhInSourceIdType,
       "rsIpsecSaAhInProtocol": rsIpsecSaAhInProtocol,
       "rsIpsecSaAhInDestPort": rsIpsecSaAhInDestPort,
       "rsIpsecSaAhInSourcePort": rsIpsecSaAhInSourcePort,
       "rsIpsecSaAhInCreator": rsIpsecSaAhInCreator,
       "rsIpsecSaAhInEncapsulation": rsIpsecSaAhInEncapsulation,
       "rsIpsecSaAhInAuthAlg": rsIpsecSaAhInAuthAlg,
       "rsIpsecSaAhInLimitSeconds": rsIpsecSaAhInLimitSeconds,
       "rsIpsecSaAhInLimitKbytes": rsIpsecSaAhInLimitKbytes,
       "rsIpsecSaAhInAccSeconds": rsIpsecSaAhInAccSeconds,
       "rsIpsecSaAhInAccKbytes": rsIpsecSaAhInAccKbytes,
       "rsIpsecSaAhInUserOctets": rsIpsecSaAhInUserOctets,
       "rsIpsecSaAhInPackets": rsIpsecSaAhInPackets,
       "rsIpsecSaAhInAuthErrors": rsIpsecSaAhInAuthErrors,
       "rsIpsecSaAhInReplayErrors": rsIpsecSaAhInReplayErrors,
       "rsIpsecSaAhInPolicyErrors": rsIpsecSaAhInPolicyErrors,
       "rsIpsecSaAhInOtherReceiveErrors": rsIpsecSaAhInOtherReceiveErrors,
       "rsIpsecSaIpcompInTable": rsIpsecSaIpcompInTable,
       "rsIpsecSaIpcompInEntry": rsIpsecSaIpcompInEntry,
       "rsIpsecSaIpcompInAddress": rsIpsecSaIpcompInAddress,
       "rsIpsecSaIpcompInCpi": rsIpsecSaIpcompInCpi,
       "rsIpsecSaIpcompInDestId": rsIpsecSaIpcompInDestId,
       "rsIpsecSaIpcompInDestIdType": rsIpsecSaIpcompInDestIdType,
       "rsIpsecSaIpcompInSourceId": rsIpsecSaIpcompInSourceId,
       "rsIpsecSaIpcompInSourceIdType": rsIpsecSaIpcompInSourceIdType,
       "rsIpsecSaIpcompInProtocol": rsIpsecSaIpcompInProtocol,
       "rsIpsecSaIpcompInDestPort": rsIpsecSaIpcompInDestPort,
       "rsIpsecSaIpcompInSourcePort": rsIpsecSaIpcompInSourcePort,
       "rsIpsecSaIpcompInCreator": rsIpsecSaIpcompInCreator,
       "rsIpsecSaIpcompInEncapsulation": rsIpsecSaIpcompInEncapsulation,
       "rsIpsecSaIpcompInDecompAlg": rsIpsecSaIpcompInDecompAlg,
       "rsIpsecSaIpcompInSeconds": rsIpsecSaIpcompInSeconds,
       "rsIpsecSaIpcompInUserOctets": rsIpsecSaIpcompInUserOctets,
       "rsIpsecSaIpcompInPackets": rsIpsecSaIpcompInPackets,
       "rsIpsecSaIpcompInDecompErrors": rsIpsecSaIpcompInDecompErrors,
       "rsIpsecSaIpcompInOtherReceiveErrors": rsIpsecSaIpcompInOtherReceiveErrors,
       "rsIpsecSaEspOutTable": rsIpsecSaEspOutTable,
       "rsIpsecSaEspOutEntry": rsIpsecSaEspOutEntry,
       "rsIpsecSaEspOutAddress": rsIpsecSaEspOutAddress,
       "rsIpsecSaEspOutSpi": rsIpsecSaEspOutSpi,
       "rsIpsecSaEspOutSourceId": rsIpsecSaEspOutSourceId,
       "rsIpsecSaEspOutSourceIdType": rsIpsecSaEspOutSourceIdType,
       "rsIpsecSaEspOutDestId": rsIpsecSaEspOutDestId,
       "rsIpsecSaEspOutDestIdType": rsIpsecSaEspOutDestIdType,
       "rsIpsecSaEspOutProtocol": rsIpsecSaEspOutProtocol,
       "rsIpsecSaEspOutSourcePort": rsIpsecSaEspOutSourcePort,
       "rsIpsecSaEspOutDestPort": rsIpsecSaEspOutDestPort,
       "rsIpsecSaEspOutCreator": rsIpsecSaEspOutCreator,
       "rsIpsecSaEspOutEncapsulation": rsIpsecSaEspOutEncapsulation,
       "rsIpsecSaEspOutEncAlg": rsIpsecSaEspOutEncAlg,
       "rsIpsecSaEspOutEncKeyLength": rsIpsecSaEspOutEncKeyLength,
       "rsIpsecSaEspOutAuthAlg": rsIpsecSaEspOutAuthAlg,
       "rsIpsecSaEspOutLimitSeconds": rsIpsecSaEspOutLimitSeconds,
       "rsIpsecSaEspOutLimitKbytes": rsIpsecSaEspOutLimitKbytes,
       "rsIpsecSaEspOutAccSeconds": rsIpsecSaEspOutAccSeconds,
       "rsIpsecSaEspOutAccKbytes": rsIpsecSaEspOutAccKbytes,
       "rsIpsecSaEspOutUserOctets": rsIpsecSaEspOutUserOctets,
       "rsIpsecSaEspOutPackets": rsIpsecSaEspOutPackets,
       "rsIpsecSaEspOutSendErrors": rsIpsecSaEspOutSendErrors,
       "rsIpsecSaAhOutTable": rsIpsecSaAhOutTable,
       "rsIpsecSaAhOutEntry": rsIpsecSaAhOutEntry,
       "rsIpsecSaAhOutAddress": rsIpsecSaAhOutAddress,
       "rsIpsecSaAhOutSpi": rsIpsecSaAhOutSpi,
       "rsIpsecSaAhOutSourceId": rsIpsecSaAhOutSourceId,
       "rsIpsecSaAhOutSourceIdType": rsIpsecSaAhOutSourceIdType,
       "rsIpsecSaAhOutDestId": rsIpsecSaAhOutDestId,
       "rsIpsecSaAhOutDestIdType": rsIpsecSaAhOutDestIdType,
       "rsIpsecSaAhOutProtocol": rsIpsecSaAhOutProtocol,
       "rsIpsecSaAhOutSourcePort": rsIpsecSaAhOutSourcePort,
       "rsIpsecSaAhOutDestPort": rsIpsecSaAhOutDestPort,
       "rsIpsecSaAhOutCreator": rsIpsecSaAhOutCreator,
       "rsIpsecSaAhOutEncapsulation": rsIpsecSaAhOutEncapsulation,
       "rsIpsecSaAhOutAuthAlg": rsIpsecSaAhOutAuthAlg,
       "rsIpsecSaAhOutLimitSeconds": rsIpsecSaAhOutLimitSeconds,
       "rsIpsecSaAhOutLimitKbytes": rsIpsecSaAhOutLimitKbytes,
       "rsIpsecSaAhOutAccSeconds": rsIpsecSaAhOutAccSeconds,
       "rsIpsecSaAhOutAccKbytes": rsIpsecSaAhOutAccKbytes,
       "rsIpsecSaAhOutUserOctets": rsIpsecSaAhOutUserOctets,
       "rsIpsecSaAhOutPackets": rsIpsecSaAhOutPackets,
       "rsIpsecSaAhOutSendErrors": rsIpsecSaAhOutSendErrors,
       "rsIpsecSaIpcompOutTable": rsIpsecSaIpcompOutTable,
       "rsIpsecSaIpcompOutEntry": rsIpsecSaIpcompOutEntry,
       "rsIpsecSaIpcompOutAddress": rsIpsecSaIpcompOutAddress,
       "rsIpsecSaIpcompOutCpi": rsIpsecSaIpcompOutCpi,
       "rsIpsecSaIpcompOutSourceId": rsIpsecSaIpcompOutSourceId,
       "rsIpsecSaIpcompOutSourceIdType": rsIpsecSaIpcompOutSourceIdType,
       "rsIpsecSaIpcompOutDestId": rsIpsecSaIpcompOutDestId,
       "rsIpsecSaIpcompOutDestIdType": rsIpsecSaIpcompOutDestIdType,
       "rsIpsecSaIpcompOutProtocol": rsIpsecSaIpcompOutProtocol,
       "rsIpsecSaIpcompOutSourcePort": rsIpsecSaIpcompOutSourcePort,
       "rsIpsecSaIpcompOutDestPort": rsIpsecSaIpcompOutDestPort,
       "rsIpsecSaIpcompOutCreator": rsIpsecSaIpcompOutCreator,
       "rsIpsecSaIpcompOutEncapsulation": rsIpsecSaIpcompOutEncapsulation,
       "rsIpsecSaIpcompOutCompAlg": rsIpsecSaIpcompOutCompAlg,
       "rsIpsecSaIpcompOutSeconds": rsIpsecSaIpcompOutSeconds,
       "rsIpsecSaIpcompOutUserOctets": rsIpsecSaIpcompOutUserOctets,
       "rsIpsecSaIpcompOutPackets": rsIpsecSaIpcompOutPackets,
       "rsSaStatistics": rsSaStatistics,
       "rsIpsecEspCurrentInboundSAs": rsIpsecEspCurrentInboundSAs,
       "rsIpsecEspTotalInboundSAs": rsIpsecEspTotalInboundSAs,
       "rsIpsecEspCurrentOutboundSAs": rsIpsecEspCurrentOutboundSAs,
       "rsIpsecEspTotalOutboundSAs": rsIpsecEspTotalOutboundSAs,
       "rsIpsecAhCurrentInboundSAs": rsIpsecAhCurrentInboundSAs,
       "rsIpsecAhTotalInboundSAs": rsIpsecAhTotalInboundSAs,
       "rsIpsecAhCurrentOutboundSAs": rsIpsecAhCurrentOutboundSAs,
       "rsIpsecAhTotalOutboundSAs": rsIpsecAhTotalOutboundSAs,
       "rsIpsecIpcompCurrentInboundSAs": rsIpsecIpcompCurrentInboundSAs,
       "rsIpsecIpcompTotalInboundSAs": rsIpsecIpcompTotalInboundSAs,
       "rsIpsecIpcompCurrentOutboundSAs": rsIpsecIpcompCurrentOutboundSAs,
       "rsIpsecIpcompTotalOutboundSAs": rsIpsecIpcompTotalOutboundSAs,
       "rsSaErrors": rsSaErrors,
       "rsIpsecDecryptionErrors": rsIpsecDecryptionErrors,
       "rsIpsecAuthenticationErrors": rsIpsecAuthenticationErrors,
       "rsIpsecReplayErrors": rsIpsecReplayErrors,
       "rsIpsecPolicyErrors": rsIpsecPolicyErrors,
       "rsIpsecOtherReceiveErrors": rsIpsecOtherReceiveErrors,
       "rsIpsecSendErrors": rsIpsecSendErrors,
       "rsIpsecUnknownSpiErrors": rsIpsecUnknownSpiErrors,
       "rsSaTraps": rsSaTraps,
       "rsEspAuthFailureTrap": rsEspAuthFailureTrap,
       "rsAhAuthFailureTrap": rsAhAuthFailureTrap,
       "rsEspReplayFailureTrap": rsEspReplayFailureTrap,
       "rsAhReplayFailureTrap": rsAhReplayFailureTrap,
       "rsEspPolicyFailureTrap": rsEspPolicyFailureTrap,
       "rsAhPolicyFailureTrap": rsAhPolicyFailureTrap,
       "rsInvalidSpiTrap": rsInvalidSpiTrap,
       "rsSaTrapObjects": rsSaTrapObjects,
       "rsIpsecSecurityProtocol": rsIpsecSecurityProtocol,
       "rsIpsecSPI": rsIpsecSPI,
       "rsIpsecLocalAddress": rsIpsecLocalAddress,
       "rsIpsecPeerAddress": rsIpsecPeerAddress,
       "rsSaTrapControl": rsSaTrapControl,
       "rsEspAuthFailureTrapEnable": rsEspAuthFailureTrapEnable,
       "rsAhAuthFailureTrapEnable": rsAhAuthFailureTrapEnable,
       "rsEspReplayFailureTrapEnable": rsEspReplayFailureTrapEnable,
       "rsAhReplayFailureTrapEnable": rsAhReplayFailureTrapEnable,
       "rsEspPolicyFailureTrapEnable": rsEspPolicyFailureTrapEnable,
       "rsAhPolicyFailureTrapEnable": rsAhPolicyFailureTrapEnable,
       "rsInvalidSpiTrapEnable": rsInvalidSpiTrapEnable,
       "rsSaGroups": rsSaGroups,
       "rsSaConformance": rsSaConformance}
)
