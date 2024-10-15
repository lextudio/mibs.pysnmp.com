# SNMP MIB module (WATCHGUARD-IPSEC-SA-MON-MIB-EXT) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/WATCHGUARD-IPSEC-SA-MON-MIB-EXT
# Produced by pysmi-1.5.4 at Mon Oct 14 23:13:34 2024
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

(watchguard,) = mibBuilder.importSymbols(
    "WATCHGUARD-MIB",
    "watchguard")


# MODULE-IDENTITY

wgIpsecSaMonModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3097, 3)
)
wgIpsecSaMonModule.setRevisions(
        ("2007-01-25 12:00",)
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

_WgIpsecSaMonitorMIB_ObjectIdentity = ObjectIdentity
wgIpsecSaMonitorMIB = _WgIpsecSaMonitorMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3097, 3, 1)
)
if mibBuilder.loadTexts:
    wgIpsecSaMonitorMIB.setStatus("current")
_WgSaTables_ObjectIdentity = ObjectIdentity
wgSaTables = _WgSaTables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3097, 3, 1, 1)
)
if mibBuilder.loadTexts:
    wgSaTables.setStatus("current")
_WgIpsecSaEspInTable_Object = MibTable
wgIpsecSaEspInTable = _WgIpsecSaEspInTable_Object(
    (1, 3, 6, 1, 4, 1, 3097, 3, 1, 1, 1)
)
if mibBuilder.loadTexts:
    wgIpsecSaEspInTable.setStatus("current")
_WgIpsecSaEspInEntry_Object = MibTableRow
wgIpsecSaEspInEntry = _WgIpsecSaEspInEntry_Object(
    (1, 3, 6, 1, 4, 1, 3097, 3, 1, 1, 1, 1)
)
wgIpsecSaEspInEntry.setIndexNames(
    (0, "WATCHGUARD-IPSEC-SA-MON-MIB-EXT", "wgIpsecSaEspInAddress"),
    (0, "WATCHGUARD-IPSEC-SA-MON-MIB-EXT", "wgIpsecSaEspInSpi"),
)
if mibBuilder.loadTexts:
    wgIpsecSaEspInEntry.setStatus("current")
_WgIpsecSaEspInAddress_Type = IpAddress
_WgIpsecSaEspInAddress_Object = MibTableColumn
wgIpsecSaEspInAddress = _WgIpsecSaEspInAddress_Object(
    (1, 3, 6, 1, 4, 1, 3097, 3, 1, 1, 1, 1, 1),
    _WgIpsecSaEspInAddress_Type()
)
wgIpsecSaEspInAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wgIpsecSaEspInAddress.setStatus("current")
_WgIpsecSaEspInSpi_Type = Integer32
_WgIpsecSaEspInSpi_Object = MibTableColumn
wgIpsecSaEspInSpi = _WgIpsecSaEspInSpi_Object(
    (1, 3, 6, 1, 4, 1, 3097, 3, 1, 1, 1, 1, 2),
    _WgIpsecSaEspInSpi_Type()
)
wgIpsecSaEspInSpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wgIpsecSaEspInSpi.setStatus("current")


class _WgIpsecSaEspInDestId_Type(OctetString):
    """Custom type wgIpsecSaEspInDestId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_WgIpsecSaEspInDestId_Type.__name__ = "OctetString"
_WgIpsecSaEspInDestId_Object = MibTableColumn
wgIpsecSaEspInDestId = _WgIpsecSaEspInDestId_Object(
    (1, 3, 6, 1, 4, 1, 3097, 3, 1, 1, 1, 1, 3),
    _WgIpsecSaEspInDestId_Type()
)
wgIpsecSaEspInDestId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wgIpsecSaEspInDestId.setStatus("current")
_WgIpsecSaEspInDestIdType_Type = IpsecDoiIdentType
_WgIpsecSaEspInDestIdType_Object = MibTableColumn
wgIpsecSaEspInDestIdType = _WgIpsecSaEspInDestIdType_Object(
    (1, 3, 6, 1, 4, 1, 3097, 3, 1, 1, 1, 1, 4),
    _WgIpsecSaEspInDestIdType_Type()
)
wgIpsecSaEspInDestIdType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wgIpsecSaEspInDestIdType.setStatus("current")


class _WgIpsecSaEspInSourceId_Type(OctetString):
    """Custom type wgIpsecSaEspInSourceId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_WgIpsecSaEspInSourceId_Type.__name__ = "OctetString"
_WgIpsecSaEspInSourceId_Object = MibTableColumn
wgIpsecSaEspInSourceId = _WgIpsecSaEspInSourceId_Object(
    (1, 3, 6, 1, 4, 1, 3097, 3, 1, 1, 1, 1, 5),
    _WgIpsecSaEspInSourceId_Type()
)
wgIpsecSaEspInSourceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wgIpsecSaEspInSourceId.setStatus("current")
_WgIpsecSaEspInSourceIdType_Type = IpsecDoiIdentType
_WgIpsecSaEspInSourceIdType_Object = MibTableColumn
wgIpsecSaEspInSourceIdType = _WgIpsecSaEspInSourceIdType_Object(
    (1, 3, 6, 1, 4, 1, 3097, 3, 1, 1, 1, 1, 6),
    _WgIpsecSaEspInSourceIdType_Type()
)
wgIpsecSaEspInSourceIdType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wgIpsecSaEspInSourceIdType.setStatus("current")


class _WgIpsecSaEspInProtocol_Type(Integer32):
    """Custom type wgIpsecSaEspInProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_WgIpsecSaEspInProtocol_Type.__name__ = "Integer32"
_WgIpsecSaEspInProtocol_Object = MibTableColumn
wgIpsecSaEspInProtocol = _WgIpsecSaEspInProtocol_Object(
    (1, 3, 6, 1, 4, 1, 3097, 3, 1, 1, 1, 1, 7),
    _WgIpsecSaEspInProtocol_Type()
)
wgIpsecSaEspInProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wgIpsecSaEspInProtocol.setStatus("current")


class _WgIpsecSaEspInDestPort_Type(Integer32):
    """Custom type wgIpsecSaEspInDestPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WgIpsecSaEspInDestPort_Type.__name__ = "Integer32"
_WgIpsecSaEspInDestPort_Object = MibTableColumn
wgIpsecSaEspInDestPort = _WgIpsecSaEspInDestPort_Object(
    (1, 3, 6, 1, 4, 1, 3097, 3, 1, 1, 1, 1, 8),
    _WgIpsecSaEspInDestPort_Type()
)
wgIpsecSaEspInDestPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wgIpsecSaEspInDestPort.setStatus("current")


class _WgIpsecSaEspInSourcePort_Type(Integer32):
    """Custom type wgIpsecSaEspInSourcePort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WgIpsecSaEspInSourcePort_Type.__name__ = "Integer32"
_WgIpsecSaEspInSourcePort_Object = MibTableColumn
wgIpsecSaEspInSourcePort = _WgIpsecSaEspInSourcePort_Object(
    (1, 3, 6, 1, 4, 1, 3097, 3, 1, 1, 1, 1, 9),
    _WgIpsecSaEspInSourcePort_Type()
)
wgIpsecSaEspInSourcePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wgIpsecSaEspInSourcePort.setStatus("current")
_WgIpsecSaEspInCreator_Type = IpsecSaCreatorIdent
_WgIpsecSaEspInCreator_Object = MibTableColumn
wgIpsecSaEspInCreator = _WgIpsecSaEspInCreator_Object(
    (1, 3, 6, 1, 4, 1, 3097, 3, 1, 1, 1, 1, 10),
    _WgIpsecSaEspInCreator_Type()
)
wgIpsecSaEspInCreator.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wgIpsecSaEspInCreator.setStatus("current")
_WgIpsecSaEspInEncapsulation_Type = IpsecDoiEncapsulationMode
_WgIpsecSaEspInEncapsulation_Object = MibTableColumn
wgIpsecSaEspInEncapsulation = _WgIpsecSaEspInEncapsulation_Object(
    (1, 3, 6, 1, 4, 1, 3097, 3, 1, 1, 1, 1, 11),
    _WgIpsecSaEspInEncapsulation_Type()
)
wgIpsecSaEspInEncapsulation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wgIpsecSaEspInEncapsulation.setStatus("current")
_WgIpsecSaEspInEncAlg_Type = IpsecDoiEspTransform
_WgIpsecSaEspInEncAlg_Object = MibTableColumn
wgIpsecSaEspInEncAlg = _WgIpsecSaEspInEncAlg_Object(
    (1, 3, 6, 1, 4, 1, 3097, 3, 1, 1, 1, 1, 12),
    _WgIpsecSaEspInEncAlg_Type()
)
wgIpsecSaEspInEncAlg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wgIpsecSaEspInEncAlg.setStatus("current")


class _WgIpsecSaEspInEncKeyLength_Type(Integer32):
    """Custom type wgIpsecSaEspInEncKeyLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65531),
    )


_WgIpsecSaEspInEncKeyLength_Type.__name__ = "Integer32"
_WgIpsecSaEspInEncKeyLength_Object = MibTableColumn
wgIpsecSaEspInEncKeyLength = _WgIpsecSaEspInEncKeyLength_Object(
    (1, 3, 6, 1, 4, 1, 3097, 3, 1, 1, 1, 1, 13),
    _WgIpsecSaEspInEncKeyLength_Type()
)
wgIpsecSaEspInEncKeyLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wgIpsecSaEspInEncKeyLength.setStatus("current")
if mibBuilder.loadTexts:
    wgIpsecSaEspInEncKeyLength.setUnits("bits")
_WgIpsecSaEspInAuthAlg_Type = IpsecDoiAuthAlgorithm
_WgIpsecSaEspInAuthAlg_Object = MibTableColumn
wgIpsecSaEspInAuthAlg = _WgIpsecSaEspInAuthAlg_Object(
    (1, 3, 6, 1, 4, 1, 3097, 3, 1, 1, 1, 1, 14),
    _WgIpsecSaEspInAuthAlg_Type()
)
wgIpsecSaEspInAuthAlg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wgIpsecSaEspInAuthAlg.setStatus("current")
_WgIpsecSaEspInLimitSeconds_Type = Integer32
_WgIpsecSaEspInLimitSeconds_Object = MibTableColumn
wgIpsecSaEspInLimitSeconds = _WgIpsecSaEspInLimitSeconds_Object(
    (1, 3, 6, 1, 4, 1, 3097, 3, 1, 1, 1, 1, 15),
    _WgIpsecSaEspInLimitSeconds_Type()
)
wgIpsecSaEspInLimitSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wgIpsecSaEspInLimitSeconds.setStatus("current")
if mibBuilder.loadTexts:
    wgIpsecSaEspInLimitSeconds.setUnits("seconds")
_WgIpsecSaEspInLimitKbytes_Type = Integer32
_WgIpsecSaEspInLimitKbytes_Object = MibTableColumn
wgIpsecSaEspInLimitKbytes = _WgIpsecSaEspInLimitKbytes_Object(
    (1, 3, 6, 1, 4, 1, 3097, 3, 1, 1, 1, 1, 16),
    _WgIpsecSaEspInLimitKbytes_Type()
)
wgIpsecSaEspInLimitKbytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wgIpsecSaEspInLimitKbytes.setStatus("current")
if mibBuilder.loadTexts:
    wgIpsecSaEspInLimitKbytes.setUnits("kilobytes")
_WgIpsecSaEspInAccSeconds_Type = Counter32
_WgIpsecSaEspInAccSeconds_Object = MibTableColumn
wgIpsecSaEspInAccSeconds = _WgIpsecSaEspInAccSeconds_Object(
    (1, 3, 6, 1, 4, 1, 3097, 3, 1, 1, 1, 1, 17),
    _WgIpsecSaEspInAccSeconds_Type()
)
wgIpsecSaEspInAccSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wgIpsecSaEspInAccSeconds.setStatus("current")
if mibBuilder.loadTexts:
    wgIpsecSaEspInAccSeconds.setUnits("seconds")
_WgIpsecSaEspInAccKbytes_Type = Counter32
_WgIpsecSaEspInAccKbytes_Object = MibTableColumn
wgIpsecSaEspInAccKbytes = _WgIpsecSaEspInAccKbytes_Object(
    (1, 3, 6, 1, 4, 1, 3097, 3, 1, 1, 1, 1, 18),
    _WgIpsecSaEspInAccKbytes_Type()
)
wgIpsecSaEspInAccKbytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wgIpsecSaEspInAccKbytes.setStatus("current")
if mibBuilder.loadTexts:
    wgIpsecSaEspInAccKbytes.setUnits("kilobytes")
_WgIpsecSaEspInUserOctets_Type = Counter32
_WgIpsecSaEspInUserOctets_Object = MibTableColumn
wgIpsecSaEspInUserOctets = _WgIpsecSaEspInUserOctets_Object(
    (1, 3, 6, 1, 4, 1, 3097, 3, 1, 1, 1, 1, 19),
    _WgIpsecSaEspInUserOctets_Type()
)
wgIpsecSaEspInUserOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wgIpsecSaEspInUserOctets.setStatus("current")
if mibBuilder.loadTexts:
    wgIpsecSaEspInUserOctets.setUnits("bytes")
_WgIpsecSaEspInPackets_Type = Counter32
_WgIpsecSaEspInPackets_Object = MibTableColumn
wgIpsecSaEspInPackets = _WgIpsecSaEspInPackets_Object(
    (1, 3, 6, 1, 4, 1, 3097, 3, 1, 1, 1, 1, 20),
    _WgIpsecSaEspInPackets_Type()
)
wgIpsecSaEspInPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wgIpsecSaEspInPackets.setStatus("current")
_WgIpsecSaEspInDecryptErrors_Type = Counter32
_WgIpsecSaEspInDecryptErrors_Object = MibTableColumn
wgIpsecSaEspInDecryptErrors = _WgIpsecSaEspInDecryptErrors_Object(
    (1, 3, 6, 1, 4, 1, 3097, 3, 1, 1, 1, 1, 21),
    _WgIpsecSaEspInDecryptErrors_Type()
)
wgIpsecSaEspInDecryptErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wgIpsecSaEspInDecryptErrors.setStatus("current")
_WgIpsecSaEspInAuthErrors_Type = Counter32
_WgIpsecSaEspInAuthErrors_Object = MibTableColumn
wgIpsecSaEspInAuthErrors = _WgIpsecSaEspInAuthErrors_Object(
    (1, 3, 6, 1, 4, 1, 3097, 3, 1, 1, 1, 1, 22),
    _WgIpsecSaEspInAuthErrors_Type()
)
wgIpsecSaEspInAuthErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wgIpsecSaEspInAuthErrors.setStatus("current")
_WgIpsecSaEspInReplayErrors_Type = Counter32
_WgIpsecSaEspInReplayErrors_Object = MibTableColumn
wgIpsecSaEspInReplayErrors = _WgIpsecSaEspInReplayErrors_Object(
    (1, 3, 6, 1, 4, 1, 3097, 3, 1, 1, 1, 1, 23),
    _WgIpsecSaEspInReplayErrors_Type()
)
wgIpsecSaEspInReplayErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wgIpsecSaEspInReplayErrors.setStatus("current")
_WgIpsecSaEspInPolicyErrors_Type = Counter32
_WgIpsecSaEspInPolicyErrors_Object = MibTableColumn
wgIpsecSaEspInPolicyErrors = _WgIpsecSaEspInPolicyErrors_Object(
    (1, 3, 6, 1, 4, 1, 3097, 3, 1, 1, 1, 1, 24),
    _WgIpsecSaEspInPolicyErrors_Type()
)
wgIpsecSaEspInPolicyErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wgIpsecSaEspInPolicyErrors.setStatus("current")
_WgIpsecSaEspInPadErrors_Type = Counter32
_WgIpsecSaEspInPadErrors_Object = MibTableColumn
wgIpsecSaEspInPadErrors = _WgIpsecSaEspInPadErrors_Object(
    (1, 3, 6, 1, 4, 1, 3097, 3, 1, 1, 1, 1, 25),
    _WgIpsecSaEspInPadErrors_Type()
)
wgIpsecSaEspInPadErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wgIpsecSaEspInPadErrors.setStatus("current")
_WgIpsecSaEspInOtherReceiveErrors_Type = Counter32
_WgIpsecSaEspInOtherReceiveErrors_Object = MibTableColumn
wgIpsecSaEspInOtherReceiveErrors = _WgIpsecSaEspInOtherReceiveErrors_Object(
    (1, 3, 6, 1, 4, 1, 3097, 3, 1, 1, 1, 1, 26),
    _WgIpsecSaEspInOtherReceiveErrors_Type()
)
wgIpsecSaEspInOtherReceiveErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wgIpsecSaEspInOtherReceiveErrors.setStatus("current")
_WgIpsecSaAhInTable_Object = MibTable
wgIpsecSaAhInTable = _WgIpsecSaAhInTable_Object(
    (1, 3, 6, 1, 4, 1, 3097, 3, 1, 1, 2)
)
if mibBuilder.loadTexts:
    wgIpsecSaAhInTable.setStatus("current")
_WgIpsecSaAhInEntry_Object = MibTableRow
wgIpsecSaAhInEntry = _WgIpsecSaAhInEntry_Object(
    (1, 3, 6, 1, 4, 1, 3097, 3, 1, 1, 2, 1)
)
wgIpsecSaAhInEntry.setIndexNames(
    (0, "WATCHGUARD-IPSEC-SA-MON-MIB-EXT", "wgIpsecSaAhInAddress"),
    (0, "WATCHGUARD-IPSEC-SA-MON-MIB-EXT", "wgIpsecSaAhInSpi"),
)
if mibBuilder.loadTexts:
    wgIpsecSaAhInEntry.setStatus("current")
_WgIpsecSaAhInAddress_Type = IpAddress
_WgIpsecSaAhInAddress_Object = MibTableColumn
wgIpsecSaAhInAddress = _WgIpsecSaAhInAddress_Object(
    (1, 3, 6, 1, 4, 1, 3097, 3, 1, 1, 2, 1, 1),
    _WgIpsecSaAhInAddress_Type()
)
wgIpsecSaAhInAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wgIpsecSaAhInAddress.setStatus("current")
_WgIpsecSaAhInSpi_Type = Integer32
_WgIpsecSaAhInSpi_Object = MibTableColumn
wgIpsecSaAhInSpi = _WgIpsecSaAhInSpi_Object(
    (1, 3, 6, 1, 4, 1, 3097, 3, 1, 1, 2, 1, 2),
    _WgIpsecSaAhInSpi_Type()
)
wgIpsecSaAhInSpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wgIpsecSaAhInSpi.setStatus("current")


class _WgIpsecSaAhInDestId_Type(OctetString):
    """Custom type wgIpsecSaAhInDestId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_WgIpsecSaAhInDestId_Type.__name__ = "OctetString"
_WgIpsecSaAhInDestId_Object = MibTableColumn
wgIpsecSaAhInDestId = _WgIpsecSaAhInDestId_Object(
    (1, 3, 6, 1, 4, 1, 3097, 3, 1, 1, 2, 1, 3),
    _WgIpsecSaAhInDestId_Type()
)
wgIpsecSaAhInDestId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wgIpsecSaAhInDestId.setStatus("current")
_WgIpsecSaAhInDestIdType_Type = IpsecDoiIdentType
_WgIpsecSaAhInDestIdType_Object = MibTableColumn
wgIpsecSaAhInDestIdType = _WgIpsecSaAhInDestIdType_Object(
    (1, 3, 6, 1, 4, 1, 3097, 3, 1, 1, 2, 1, 4),
    _WgIpsecSaAhInDestIdType_Type()
)
wgIpsecSaAhInDestIdType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wgIpsecSaAhInDestIdType.setStatus("current")


class _WgIpsecSaAhInSourceId_Type(OctetString):
    """Custom type wgIpsecSaAhInSourceId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_WgIpsecSaAhInSourceId_Type.__name__ = "OctetString"
_WgIpsecSaAhInSourceId_Object = MibTableColumn
wgIpsecSaAhInSourceId = _WgIpsecSaAhInSourceId_Object(
    (1, 3, 6, 1, 4, 1, 3097, 3, 1, 1, 2, 1, 5),
    _WgIpsecSaAhInSourceId_Type()
)
wgIpsecSaAhInSourceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wgIpsecSaAhInSourceId.setStatus("current")
_WgIpsecSaAhInSourceIdType_Type = IpsecDoiIdentType
_WgIpsecSaAhInSourceIdType_Object = MibTableColumn
wgIpsecSaAhInSourceIdType = _WgIpsecSaAhInSourceIdType_Object(
    (1, 3, 6, 1, 4, 1, 3097, 3, 1, 1, 2, 1, 6),
    _WgIpsecSaAhInSourceIdType_Type()
)
wgIpsecSaAhInSourceIdType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wgIpsecSaAhInSourceIdType.setStatus("current")


class _WgIpsecSaAhInProtocol_Type(Integer32):
    """Custom type wgIpsecSaAhInProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_WgIpsecSaAhInProtocol_Type.__name__ = "Integer32"
_WgIpsecSaAhInProtocol_Object = MibTableColumn
wgIpsecSaAhInProtocol = _WgIpsecSaAhInProtocol_Object(
    (1, 3, 6, 1, 4, 1, 3097, 3, 1, 1, 2, 1, 7),
    _WgIpsecSaAhInProtocol_Type()
)
wgIpsecSaAhInProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wgIpsecSaAhInProtocol.setStatus("current")


class _WgIpsecSaAhInDestPort_Type(Integer32):
    """Custom type wgIpsecSaAhInDestPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WgIpsecSaAhInDestPort_Type.__name__ = "Integer32"
_WgIpsecSaAhInDestPort_Object = MibTableColumn
wgIpsecSaAhInDestPort = _WgIpsecSaAhInDestPort_Object(
    (1, 3, 6, 1, 4, 1, 3097, 3, 1, 1, 2, 1, 8),
    _WgIpsecSaAhInDestPort_Type()
)
wgIpsecSaAhInDestPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wgIpsecSaAhInDestPort.setStatus("current")


class _WgIpsecSaAhInSourcePort_Type(Integer32):
    """Custom type wgIpsecSaAhInSourcePort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WgIpsecSaAhInSourcePort_Type.__name__ = "Integer32"
_WgIpsecSaAhInSourcePort_Object = MibTableColumn
wgIpsecSaAhInSourcePort = _WgIpsecSaAhInSourcePort_Object(
    (1, 3, 6, 1, 4, 1, 3097, 3, 1, 1, 2, 1, 9),
    _WgIpsecSaAhInSourcePort_Type()
)
wgIpsecSaAhInSourcePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wgIpsecSaAhInSourcePort.setStatus("current")
_WgIpsecSaAhInCreator_Type = IpsecSaCreatorIdent
_WgIpsecSaAhInCreator_Object = MibTableColumn
wgIpsecSaAhInCreator = _WgIpsecSaAhInCreator_Object(
    (1, 3, 6, 1, 4, 1, 3097, 3, 1, 1, 2, 1, 10),
    _WgIpsecSaAhInCreator_Type()
)
wgIpsecSaAhInCreator.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wgIpsecSaAhInCreator.setStatus("current")
_WgIpsecSaAhInEncapsulation_Type = IpsecDoiEncapsulationMode
_WgIpsecSaAhInEncapsulation_Object = MibTableColumn
wgIpsecSaAhInEncapsulation = _WgIpsecSaAhInEncapsulation_Object(
    (1, 3, 6, 1, 4, 1, 3097, 3, 1, 1, 2, 1, 11),
    _WgIpsecSaAhInEncapsulation_Type()
)
wgIpsecSaAhInEncapsulation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wgIpsecSaAhInEncapsulation.setStatus("current")
_WgIpsecSaAhInAuthAlg_Type = IpsecDoiAhTransform
_WgIpsecSaAhInAuthAlg_Object = MibTableColumn
wgIpsecSaAhInAuthAlg = _WgIpsecSaAhInAuthAlg_Object(
    (1, 3, 6, 1, 4, 1, 3097, 3, 1, 1, 2, 1, 12),
    _WgIpsecSaAhInAuthAlg_Type()
)
wgIpsecSaAhInAuthAlg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wgIpsecSaAhInAuthAlg.setStatus("current")
_WgIpsecSaAhInLimitSeconds_Type = Integer32
_WgIpsecSaAhInLimitSeconds_Object = MibTableColumn
wgIpsecSaAhInLimitSeconds = _WgIpsecSaAhInLimitSeconds_Object(
    (1, 3, 6, 1, 4, 1, 3097, 3, 1, 1, 2, 1, 13),
    _WgIpsecSaAhInLimitSeconds_Type()
)
wgIpsecSaAhInLimitSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wgIpsecSaAhInLimitSeconds.setStatus("current")
if mibBuilder.loadTexts:
    wgIpsecSaAhInLimitSeconds.setUnits("seconds")
_WgIpsecSaAhInLimitKbytes_Type = Integer32
_WgIpsecSaAhInLimitKbytes_Object = MibTableColumn
wgIpsecSaAhInLimitKbytes = _WgIpsecSaAhInLimitKbytes_Object(
    (1, 3, 6, 1, 4, 1, 3097, 3, 1, 1, 2, 1, 14),
    _WgIpsecSaAhInLimitKbytes_Type()
)
wgIpsecSaAhInLimitKbytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wgIpsecSaAhInLimitKbytes.setStatus("current")
if mibBuilder.loadTexts:
    wgIpsecSaAhInLimitKbytes.setUnits("kilobytes")
_WgIpsecSaAhInAccSeconds_Type = Counter32
_WgIpsecSaAhInAccSeconds_Object = MibTableColumn
wgIpsecSaAhInAccSeconds = _WgIpsecSaAhInAccSeconds_Object(
    (1, 3, 6, 1, 4, 1, 3097, 3, 1, 1, 2, 1, 15),
    _WgIpsecSaAhInAccSeconds_Type()
)
wgIpsecSaAhInAccSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wgIpsecSaAhInAccSeconds.setStatus("current")
if mibBuilder.loadTexts:
    wgIpsecSaAhInAccSeconds.setUnits("seconds")
_WgIpsecSaAhInAccKbytes_Type = Counter32
_WgIpsecSaAhInAccKbytes_Object = MibTableColumn
wgIpsecSaAhInAccKbytes = _WgIpsecSaAhInAccKbytes_Object(
    (1, 3, 6, 1, 4, 1, 3097, 3, 1, 1, 2, 1, 16),
    _WgIpsecSaAhInAccKbytes_Type()
)
wgIpsecSaAhInAccKbytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wgIpsecSaAhInAccKbytes.setStatus("current")
if mibBuilder.loadTexts:
    wgIpsecSaAhInAccKbytes.setUnits("kilobytes")
_WgIpsecSaAhInUserOctets_Type = Counter32
_WgIpsecSaAhInUserOctets_Object = MibTableColumn
wgIpsecSaAhInUserOctets = _WgIpsecSaAhInUserOctets_Object(
    (1, 3, 6, 1, 4, 1, 3097, 3, 1, 1, 2, 1, 17),
    _WgIpsecSaAhInUserOctets_Type()
)
wgIpsecSaAhInUserOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wgIpsecSaAhInUserOctets.setStatus("current")
if mibBuilder.loadTexts:
    wgIpsecSaAhInUserOctets.setUnits("bytes")
_WgIpsecSaAhInPackets_Type = Counter32
_WgIpsecSaAhInPackets_Object = MibTableColumn
wgIpsecSaAhInPackets = _WgIpsecSaAhInPackets_Object(
    (1, 3, 6, 1, 4, 1, 3097, 3, 1, 1, 2, 1, 18),
    _WgIpsecSaAhInPackets_Type()
)
wgIpsecSaAhInPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wgIpsecSaAhInPackets.setStatus("current")
_WgIpsecSaAhInAuthErrors_Type = Counter32
_WgIpsecSaAhInAuthErrors_Object = MibTableColumn
wgIpsecSaAhInAuthErrors = _WgIpsecSaAhInAuthErrors_Object(
    (1, 3, 6, 1, 4, 1, 3097, 3, 1, 1, 2, 1, 19),
    _WgIpsecSaAhInAuthErrors_Type()
)
wgIpsecSaAhInAuthErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wgIpsecSaAhInAuthErrors.setStatus("current")
_WgIpsecSaAhInReplayErrors_Type = Counter32
_WgIpsecSaAhInReplayErrors_Object = MibTableColumn
wgIpsecSaAhInReplayErrors = _WgIpsecSaAhInReplayErrors_Object(
    (1, 3, 6, 1, 4, 1, 3097, 3, 1, 1, 2, 1, 20),
    _WgIpsecSaAhInReplayErrors_Type()
)
wgIpsecSaAhInReplayErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wgIpsecSaAhInReplayErrors.setStatus("current")
_WgIpsecSaAhInPolicyErrors_Type = Counter32
_WgIpsecSaAhInPolicyErrors_Object = MibTableColumn
wgIpsecSaAhInPolicyErrors = _WgIpsecSaAhInPolicyErrors_Object(
    (1, 3, 6, 1, 4, 1, 3097, 3, 1, 1, 2, 1, 21),
    _WgIpsecSaAhInPolicyErrors_Type()
)
wgIpsecSaAhInPolicyErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wgIpsecSaAhInPolicyErrors.setStatus("current")
_WgIpsecSaAhInOtherReceiveErrors_Type = Counter32
_WgIpsecSaAhInOtherReceiveErrors_Object = MibTableColumn
wgIpsecSaAhInOtherReceiveErrors = _WgIpsecSaAhInOtherReceiveErrors_Object(
    (1, 3, 6, 1, 4, 1, 3097, 3, 1, 1, 2, 1, 22),
    _WgIpsecSaAhInOtherReceiveErrors_Type()
)
wgIpsecSaAhInOtherReceiveErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wgIpsecSaAhInOtherReceiveErrors.setStatus("current")
_WgIpsecSaIpcompInTable_Object = MibTable
wgIpsecSaIpcompInTable = _WgIpsecSaIpcompInTable_Object(
    (1, 3, 6, 1, 4, 1, 3097, 3, 1, 1, 3)
)
if mibBuilder.loadTexts:
    wgIpsecSaIpcompInTable.setStatus("current")
_WgIpsecSaIpcompInEntry_Object = MibTableRow
wgIpsecSaIpcompInEntry = _WgIpsecSaIpcompInEntry_Object(
    (1, 3, 6, 1, 4, 1, 3097, 3, 1, 1, 3, 1)
)
wgIpsecSaIpcompInEntry.setIndexNames(
    (0, "WATCHGUARD-IPSEC-SA-MON-MIB-EXT", "wgIpsecSaIpcompInAddress"),
    (0, "WATCHGUARD-IPSEC-SA-MON-MIB-EXT", "wgIpsecSaIpcompInCpi"),
)
if mibBuilder.loadTexts:
    wgIpsecSaIpcompInEntry.setStatus("current")
_WgIpsecSaIpcompInAddress_Type = IpAddress
_WgIpsecSaIpcompInAddress_Object = MibTableColumn
wgIpsecSaIpcompInAddress = _WgIpsecSaIpcompInAddress_Object(
    (1, 3, 6, 1, 4, 1, 3097, 3, 1, 1, 3, 1, 1),
    _WgIpsecSaIpcompInAddress_Type()
)
wgIpsecSaIpcompInAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wgIpsecSaIpcompInAddress.setStatus("current")
_WgIpsecSaIpcompInCpi_Type = IpsecDoiIpcompTransform
_WgIpsecSaIpcompInCpi_Object = MibTableColumn
wgIpsecSaIpcompInCpi = _WgIpsecSaIpcompInCpi_Object(
    (1, 3, 6, 1, 4, 1, 3097, 3, 1, 1, 3, 1, 2),
    _WgIpsecSaIpcompInCpi_Type()
)
wgIpsecSaIpcompInCpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wgIpsecSaIpcompInCpi.setStatus("current")


class _WgIpsecSaIpcompInDestId_Type(OctetString):
    """Custom type wgIpsecSaIpcompInDestId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_WgIpsecSaIpcompInDestId_Type.__name__ = "OctetString"
_WgIpsecSaIpcompInDestId_Object = MibTableColumn
wgIpsecSaIpcompInDestId = _WgIpsecSaIpcompInDestId_Object(
    (1, 3, 6, 1, 4, 1, 3097, 3, 1, 1, 3, 1, 3),
    _WgIpsecSaIpcompInDestId_Type()
)
wgIpsecSaIpcompInDestId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wgIpsecSaIpcompInDestId.setStatus("current")
_WgIpsecSaIpcompInDestIdType_Type = IpsecDoiIdentType
_WgIpsecSaIpcompInDestIdType_Object = MibTableColumn
wgIpsecSaIpcompInDestIdType = _WgIpsecSaIpcompInDestIdType_Object(
    (1, 3, 6, 1, 4, 1, 3097, 3, 1, 1, 3, 1, 4),
    _WgIpsecSaIpcompInDestIdType_Type()
)
wgIpsecSaIpcompInDestIdType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wgIpsecSaIpcompInDestIdType.setStatus("current")


class _WgIpsecSaIpcompInSourceId_Type(OctetString):
    """Custom type wgIpsecSaIpcompInSourceId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_WgIpsecSaIpcompInSourceId_Type.__name__ = "OctetString"
_WgIpsecSaIpcompInSourceId_Object = MibTableColumn
wgIpsecSaIpcompInSourceId = _WgIpsecSaIpcompInSourceId_Object(
    (1, 3, 6, 1, 4, 1, 3097, 3, 1, 1, 3, 1, 5),
    _WgIpsecSaIpcompInSourceId_Type()
)
wgIpsecSaIpcompInSourceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wgIpsecSaIpcompInSourceId.setStatus("current")
_WgIpsecSaIpcompInSourceIdType_Type = IpsecDoiIdentType
_WgIpsecSaIpcompInSourceIdType_Object = MibTableColumn
wgIpsecSaIpcompInSourceIdType = _WgIpsecSaIpcompInSourceIdType_Object(
    (1, 3, 6, 1, 4, 1, 3097, 3, 1, 1, 3, 1, 6),
    _WgIpsecSaIpcompInSourceIdType_Type()
)
wgIpsecSaIpcompInSourceIdType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wgIpsecSaIpcompInSourceIdType.setStatus("current")


class _WgIpsecSaIpcompInProtocol_Type(Integer32):
    """Custom type wgIpsecSaIpcompInProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_WgIpsecSaIpcompInProtocol_Type.__name__ = "Integer32"
_WgIpsecSaIpcompInProtocol_Object = MibTableColumn
wgIpsecSaIpcompInProtocol = _WgIpsecSaIpcompInProtocol_Object(
    (1, 3, 6, 1, 4, 1, 3097, 3, 1, 1, 3, 1, 7),
    _WgIpsecSaIpcompInProtocol_Type()
)
wgIpsecSaIpcompInProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wgIpsecSaIpcompInProtocol.setStatus("current")


class _WgIpsecSaIpcompInDestPort_Type(Integer32):
    """Custom type wgIpsecSaIpcompInDestPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WgIpsecSaIpcompInDestPort_Type.__name__ = "Integer32"
_WgIpsecSaIpcompInDestPort_Object = MibTableColumn
wgIpsecSaIpcompInDestPort = _WgIpsecSaIpcompInDestPort_Object(
    (1, 3, 6, 1, 4, 1, 3097, 3, 1, 1, 3, 1, 8),
    _WgIpsecSaIpcompInDestPort_Type()
)
wgIpsecSaIpcompInDestPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wgIpsecSaIpcompInDestPort.setStatus("current")


class _WgIpsecSaIpcompInSourcePort_Type(Integer32):
    """Custom type wgIpsecSaIpcompInSourcePort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WgIpsecSaIpcompInSourcePort_Type.__name__ = "Integer32"
_WgIpsecSaIpcompInSourcePort_Object = MibTableColumn
wgIpsecSaIpcompInSourcePort = _WgIpsecSaIpcompInSourcePort_Object(
    (1, 3, 6, 1, 4, 1, 3097, 3, 1, 1, 3, 1, 9),
    _WgIpsecSaIpcompInSourcePort_Type()
)
wgIpsecSaIpcompInSourcePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wgIpsecSaIpcompInSourcePort.setStatus("current")
_WgIpsecSaIpcompInCreator_Type = IpsecSaCreatorIdent
_WgIpsecSaIpcompInCreator_Object = MibTableColumn
wgIpsecSaIpcompInCreator = _WgIpsecSaIpcompInCreator_Object(
    (1, 3, 6, 1, 4, 1, 3097, 3, 1, 1, 3, 1, 10),
    _WgIpsecSaIpcompInCreator_Type()
)
wgIpsecSaIpcompInCreator.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wgIpsecSaIpcompInCreator.setStatus("current")
_WgIpsecSaIpcompInEncapsulation_Type = IpsecDoiEncapsulationMode
_WgIpsecSaIpcompInEncapsulation_Object = MibTableColumn
wgIpsecSaIpcompInEncapsulation = _WgIpsecSaIpcompInEncapsulation_Object(
    (1, 3, 6, 1, 4, 1, 3097, 3, 1, 1, 3, 1, 11),
    _WgIpsecSaIpcompInEncapsulation_Type()
)
wgIpsecSaIpcompInEncapsulation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wgIpsecSaIpcompInEncapsulation.setStatus("current")
_WgIpsecSaIpcompInDecompAlg_Type = IpsecDoiIpcompTransform
_WgIpsecSaIpcompInDecompAlg_Object = MibTableColumn
wgIpsecSaIpcompInDecompAlg = _WgIpsecSaIpcompInDecompAlg_Object(
    (1, 3, 6, 1, 4, 1, 3097, 3, 1, 1, 3, 1, 12),
    _WgIpsecSaIpcompInDecompAlg_Type()
)
wgIpsecSaIpcompInDecompAlg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wgIpsecSaIpcompInDecompAlg.setStatus("current")
_WgIpsecSaIpcompInSeconds_Type = Counter32
_WgIpsecSaIpcompInSeconds_Object = MibTableColumn
wgIpsecSaIpcompInSeconds = _WgIpsecSaIpcompInSeconds_Object(
    (1, 3, 6, 1, 4, 1, 3097, 3, 1, 1, 3, 1, 13),
    _WgIpsecSaIpcompInSeconds_Type()
)
wgIpsecSaIpcompInSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wgIpsecSaIpcompInSeconds.setStatus("current")
if mibBuilder.loadTexts:
    wgIpsecSaIpcompInSeconds.setUnits("seconds")
_WgIpsecSaIpcompInUserOctets_Type = Counter32
_WgIpsecSaIpcompInUserOctets_Object = MibTableColumn
wgIpsecSaIpcompInUserOctets = _WgIpsecSaIpcompInUserOctets_Object(
    (1, 3, 6, 1, 4, 1, 3097, 3, 1, 1, 3, 1, 14),
    _WgIpsecSaIpcompInUserOctets_Type()
)
wgIpsecSaIpcompInUserOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wgIpsecSaIpcompInUserOctets.setStatus("current")
if mibBuilder.loadTexts:
    wgIpsecSaIpcompInUserOctets.setUnits("bytes")
_WgIpsecSaIpcompInPackets_Type = Counter32
_WgIpsecSaIpcompInPackets_Object = MibTableColumn
wgIpsecSaIpcompInPackets = _WgIpsecSaIpcompInPackets_Object(
    (1, 3, 6, 1, 4, 1, 3097, 3, 1, 1, 3, 1, 15),
    _WgIpsecSaIpcompInPackets_Type()
)
wgIpsecSaIpcompInPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wgIpsecSaIpcompInPackets.setStatus("current")
_WgIpsecSaIpcompInDecompErrors_Type = Counter32
_WgIpsecSaIpcompInDecompErrors_Object = MibTableColumn
wgIpsecSaIpcompInDecompErrors = _WgIpsecSaIpcompInDecompErrors_Object(
    (1, 3, 6, 1, 4, 1, 3097, 3, 1, 1, 3, 1, 16),
    _WgIpsecSaIpcompInDecompErrors_Type()
)
wgIpsecSaIpcompInDecompErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wgIpsecSaIpcompInDecompErrors.setStatus("current")
_WgIpsecSaIpcompInOtherReceiveErrors_Type = Counter32
_WgIpsecSaIpcompInOtherReceiveErrors_Object = MibTableColumn
wgIpsecSaIpcompInOtherReceiveErrors = _WgIpsecSaIpcompInOtherReceiveErrors_Object(
    (1, 3, 6, 1, 4, 1, 3097, 3, 1, 1, 3, 1, 17),
    _WgIpsecSaIpcompInOtherReceiveErrors_Type()
)
wgIpsecSaIpcompInOtherReceiveErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wgIpsecSaIpcompInOtherReceiveErrors.setStatus("current")
_WgIpsecSaEspOutTable_Object = MibTable
wgIpsecSaEspOutTable = _WgIpsecSaEspOutTable_Object(
    (1, 3, 6, 1, 4, 1, 3097, 3, 1, 1, 4)
)
if mibBuilder.loadTexts:
    wgIpsecSaEspOutTable.setStatus("current")
_WgIpsecSaEspOutEntry_Object = MibTableRow
wgIpsecSaEspOutEntry = _WgIpsecSaEspOutEntry_Object(
    (1, 3, 6, 1, 4, 1, 3097, 3, 1, 1, 4, 1)
)
wgIpsecSaEspOutEntry.setIndexNames(
    (0, "WATCHGUARD-IPSEC-SA-MON-MIB-EXT", "wgIpsecSaEspOutAddress"),
    (0, "WATCHGUARD-IPSEC-SA-MON-MIB-EXT", "wgIpsecSaEspOutSpi"),
)
if mibBuilder.loadTexts:
    wgIpsecSaEspOutEntry.setStatus("current")
_WgIpsecSaEspOutAddress_Type = IpAddress
_WgIpsecSaEspOutAddress_Object = MibTableColumn
wgIpsecSaEspOutAddress = _WgIpsecSaEspOutAddress_Object(
    (1, 3, 6, 1, 4, 1, 3097, 3, 1, 1, 4, 1, 1),
    _WgIpsecSaEspOutAddress_Type()
)
wgIpsecSaEspOutAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wgIpsecSaEspOutAddress.setStatus("current")
_WgIpsecSaEspOutSpi_Type = Integer32
_WgIpsecSaEspOutSpi_Object = MibTableColumn
wgIpsecSaEspOutSpi = _WgIpsecSaEspOutSpi_Object(
    (1, 3, 6, 1, 4, 1, 3097, 3, 1, 1, 4, 1, 2),
    _WgIpsecSaEspOutSpi_Type()
)
wgIpsecSaEspOutSpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wgIpsecSaEspOutSpi.setStatus("current")


class _WgIpsecSaEspOutSourceId_Type(OctetString):
    """Custom type wgIpsecSaEspOutSourceId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 255),
    )


_WgIpsecSaEspOutSourceId_Type.__name__ = "OctetString"
_WgIpsecSaEspOutSourceId_Object = MibTableColumn
wgIpsecSaEspOutSourceId = _WgIpsecSaEspOutSourceId_Object(
    (1, 3, 6, 1, 4, 1, 3097, 3, 1, 1, 4, 1, 3),
    _WgIpsecSaEspOutSourceId_Type()
)
wgIpsecSaEspOutSourceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wgIpsecSaEspOutSourceId.setStatus("current")
_WgIpsecSaEspOutSourceIdType_Type = IpsecDoiIdentType
_WgIpsecSaEspOutSourceIdType_Object = MibTableColumn
wgIpsecSaEspOutSourceIdType = _WgIpsecSaEspOutSourceIdType_Object(
    (1, 3, 6, 1, 4, 1, 3097, 3, 1, 1, 4, 1, 4),
    _WgIpsecSaEspOutSourceIdType_Type()
)
wgIpsecSaEspOutSourceIdType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wgIpsecSaEspOutSourceIdType.setStatus("current")


class _WgIpsecSaEspOutDestId_Type(OctetString):
    """Custom type wgIpsecSaEspOutDestId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 255),
    )


_WgIpsecSaEspOutDestId_Type.__name__ = "OctetString"
_WgIpsecSaEspOutDestId_Object = MibTableColumn
wgIpsecSaEspOutDestId = _WgIpsecSaEspOutDestId_Object(
    (1, 3, 6, 1, 4, 1, 3097, 3, 1, 1, 4, 1, 5),
    _WgIpsecSaEspOutDestId_Type()
)
wgIpsecSaEspOutDestId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wgIpsecSaEspOutDestId.setStatus("current")
_WgIpsecSaEspOutDestIdType_Type = IpsecDoiIdentType
_WgIpsecSaEspOutDestIdType_Object = MibTableColumn
wgIpsecSaEspOutDestIdType = _WgIpsecSaEspOutDestIdType_Object(
    (1, 3, 6, 1, 4, 1, 3097, 3, 1, 1, 4, 1, 6),
    _WgIpsecSaEspOutDestIdType_Type()
)
wgIpsecSaEspOutDestIdType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wgIpsecSaEspOutDestIdType.setStatus("current")


class _WgIpsecSaEspOutProtocol_Type(Integer32):
    """Custom type wgIpsecSaEspOutProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_WgIpsecSaEspOutProtocol_Type.__name__ = "Integer32"
_WgIpsecSaEspOutProtocol_Object = MibTableColumn
wgIpsecSaEspOutProtocol = _WgIpsecSaEspOutProtocol_Object(
    (1, 3, 6, 1, 4, 1, 3097, 3, 1, 1, 4, 1, 7),
    _WgIpsecSaEspOutProtocol_Type()
)
wgIpsecSaEspOutProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wgIpsecSaEspOutProtocol.setStatus("current")


class _WgIpsecSaEspOutSourcePort_Type(Integer32):
    """Custom type wgIpsecSaEspOutSourcePort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WgIpsecSaEspOutSourcePort_Type.__name__ = "Integer32"
_WgIpsecSaEspOutSourcePort_Object = MibTableColumn
wgIpsecSaEspOutSourcePort = _WgIpsecSaEspOutSourcePort_Object(
    (1, 3, 6, 1, 4, 1, 3097, 3, 1, 1, 4, 1, 8),
    _WgIpsecSaEspOutSourcePort_Type()
)
wgIpsecSaEspOutSourcePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wgIpsecSaEspOutSourcePort.setStatus("current")


class _WgIpsecSaEspOutDestPort_Type(Integer32):
    """Custom type wgIpsecSaEspOutDestPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WgIpsecSaEspOutDestPort_Type.__name__ = "Integer32"
_WgIpsecSaEspOutDestPort_Object = MibTableColumn
wgIpsecSaEspOutDestPort = _WgIpsecSaEspOutDestPort_Object(
    (1, 3, 6, 1, 4, 1, 3097, 3, 1, 1, 4, 1, 9),
    _WgIpsecSaEspOutDestPort_Type()
)
wgIpsecSaEspOutDestPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wgIpsecSaEspOutDestPort.setStatus("current")
_WgIpsecSaEspOutCreator_Type = IpsecSaCreatorIdent
_WgIpsecSaEspOutCreator_Object = MibTableColumn
wgIpsecSaEspOutCreator = _WgIpsecSaEspOutCreator_Object(
    (1, 3, 6, 1, 4, 1, 3097, 3, 1, 1, 4, 1, 10),
    _WgIpsecSaEspOutCreator_Type()
)
wgIpsecSaEspOutCreator.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wgIpsecSaEspOutCreator.setStatus("current")
_WgIpsecSaEspOutEncapsulation_Type = IpsecDoiEncapsulationMode
_WgIpsecSaEspOutEncapsulation_Object = MibTableColumn
wgIpsecSaEspOutEncapsulation = _WgIpsecSaEspOutEncapsulation_Object(
    (1, 3, 6, 1, 4, 1, 3097, 3, 1, 1, 4, 1, 11),
    _WgIpsecSaEspOutEncapsulation_Type()
)
wgIpsecSaEspOutEncapsulation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wgIpsecSaEspOutEncapsulation.setStatus("current")
_WgIpsecSaEspOutEncAlg_Type = IpsecDoiEspTransform
_WgIpsecSaEspOutEncAlg_Object = MibTableColumn
wgIpsecSaEspOutEncAlg = _WgIpsecSaEspOutEncAlg_Object(
    (1, 3, 6, 1, 4, 1, 3097, 3, 1, 1, 4, 1, 12),
    _WgIpsecSaEspOutEncAlg_Type()
)
wgIpsecSaEspOutEncAlg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wgIpsecSaEspOutEncAlg.setStatus("current")


class _WgIpsecSaEspOutEncKeyLength_Type(Integer32):
    """Custom type wgIpsecSaEspOutEncKeyLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65531),
    )


_WgIpsecSaEspOutEncKeyLength_Type.__name__ = "Integer32"
_WgIpsecSaEspOutEncKeyLength_Object = MibTableColumn
wgIpsecSaEspOutEncKeyLength = _WgIpsecSaEspOutEncKeyLength_Object(
    (1, 3, 6, 1, 4, 1, 3097, 3, 1, 1, 4, 1, 13),
    _WgIpsecSaEspOutEncKeyLength_Type()
)
wgIpsecSaEspOutEncKeyLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wgIpsecSaEspOutEncKeyLength.setStatus("current")
if mibBuilder.loadTexts:
    wgIpsecSaEspOutEncKeyLength.setUnits("bits")
_WgIpsecSaEspOutAuthAlg_Type = IpsecDoiAuthAlgorithm
_WgIpsecSaEspOutAuthAlg_Object = MibTableColumn
wgIpsecSaEspOutAuthAlg = _WgIpsecSaEspOutAuthAlg_Object(
    (1, 3, 6, 1, 4, 1, 3097, 3, 1, 1, 4, 1, 14),
    _WgIpsecSaEspOutAuthAlg_Type()
)
wgIpsecSaEspOutAuthAlg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wgIpsecSaEspOutAuthAlg.setStatus("current")
_WgIpsecSaEspOutLimitSeconds_Type = Integer32
_WgIpsecSaEspOutLimitSeconds_Object = MibTableColumn
wgIpsecSaEspOutLimitSeconds = _WgIpsecSaEspOutLimitSeconds_Object(
    (1, 3, 6, 1, 4, 1, 3097, 3, 1, 1, 4, 1, 15),
    _WgIpsecSaEspOutLimitSeconds_Type()
)
wgIpsecSaEspOutLimitSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wgIpsecSaEspOutLimitSeconds.setStatus("current")
if mibBuilder.loadTexts:
    wgIpsecSaEspOutLimitSeconds.setUnits("seconds")
_WgIpsecSaEspOutLimitKbytes_Type = Integer32
_WgIpsecSaEspOutLimitKbytes_Object = MibTableColumn
wgIpsecSaEspOutLimitKbytes = _WgIpsecSaEspOutLimitKbytes_Object(
    (1, 3, 6, 1, 4, 1, 3097, 3, 1, 1, 4, 1, 16),
    _WgIpsecSaEspOutLimitKbytes_Type()
)
wgIpsecSaEspOutLimitKbytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wgIpsecSaEspOutLimitKbytes.setStatus("current")
if mibBuilder.loadTexts:
    wgIpsecSaEspOutLimitKbytes.setUnits("kilobytes")
_WgIpsecSaEspOutAccSeconds_Type = Counter32
_WgIpsecSaEspOutAccSeconds_Object = MibTableColumn
wgIpsecSaEspOutAccSeconds = _WgIpsecSaEspOutAccSeconds_Object(
    (1, 3, 6, 1, 4, 1, 3097, 3, 1, 1, 4, 1, 17),
    _WgIpsecSaEspOutAccSeconds_Type()
)
wgIpsecSaEspOutAccSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wgIpsecSaEspOutAccSeconds.setStatus("current")
if mibBuilder.loadTexts:
    wgIpsecSaEspOutAccSeconds.setUnits("seconds")
_WgIpsecSaEspOutAccKbytes_Type = Counter32
_WgIpsecSaEspOutAccKbytes_Object = MibTableColumn
wgIpsecSaEspOutAccKbytes = _WgIpsecSaEspOutAccKbytes_Object(
    (1, 3, 6, 1, 4, 1, 3097, 3, 1, 1, 4, 1, 18),
    _WgIpsecSaEspOutAccKbytes_Type()
)
wgIpsecSaEspOutAccKbytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wgIpsecSaEspOutAccKbytes.setStatus("current")
if mibBuilder.loadTexts:
    wgIpsecSaEspOutAccKbytes.setUnits("kilobytes")
_WgIpsecSaEspOutUserOctets_Type = Counter32
_WgIpsecSaEspOutUserOctets_Object = MibTableColumn
wgIpsecSaEspOutUserOctets = _WgIpsecSaEspOutUserOctets_Object(
    (1, 3, 6, 1, 4, 1, 3097, 3, 1, 1, 4, 1, 19),
    _WgIpsecSaEspOutUserOctets_Type()
)
wgIpsecSaEspOutUserOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wgIpsecSaEspOutUserOctets.setStatus("current")
if mibBuilder.loadTexts:
    wgIpsecSaEspOutUserOctets.setUnits("bytes")
_WgIpsecSaEspOutPackets_Type = Counter32
_WgIpsecSaEspOutPackets_Object = MibTableColumn
wgIpsecSaEspOutPackets = _WgIpsecSaEspOutPackets_Object(
    (1, 3, 6, 1, 4, 1, 3097, 3, 1, 1, 4, 1, 20),
    _WgIpsecSaEspOutPackets_Type()
)
wgIpsecSaEspOutPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wgIpsecSaEspOutPackets.setStatus("current")
_WgIpsecSaEspOutSendErrors_Type = Counter32
_WgIpsecSaEspOutSendErrors_Object = MibTableColumn
wgIpsecSaEspOutSendErrors = _WgIpsecSaEspOutSendErrors_Object(
    (1, 3, 6, 1, 4, 1, 3097, 3, 1, 1, 4, 1, 21),
    _WgIpsecSaEspOutSendErrors_Type()
)
wgIpsecSaEspOutSendErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wgIpsecSaEspOutSendErrors.setStatus("current")
_WgIpsecSaAhOutTable_Object = MibTable
wgIpsecSaAhOutTable = _WgIpsecSaAhOutTable_Object(
    (1, 3, 6, 1, 4, 1, 3097, 3, 1, 1, 5)
)
if mibBuilder.loadTexts:
    wgIpsecSaAhOutTable.setStatus("current")
_WgIpsecSaAhOutEntry_Object = MibTableRow
wgIpsecSaAhOutEntry = _WgIpsecSaAhOutEntry_Object(
    (1, 3, 6, 1, 4, 1, 3097, 3, 1, 1, 5, 1)
)
wgIpsecSaAhOutEntry.setIndexNames(
    (0, "WATCHGUARD-IPSEC-SA-MON-MIB-EXT", "wgIpsecSaAhOutAddress"),
    (0, "WATCHGUARD-IPSEC-SA-MON-MIB-EXT", "wgIpsecSaAhOutSpi"),
)
if mibBuilder.loadTexts:
    wgIpsecSaAhOutEntry.setStatus("current")
_WgIpsecSaAhOutAddress_Type = IpAddress
_WgIpsecSaAhOutAddress_Object = MibTableColumn
wgIpsecSaAhOutAddress = _WgIpsecSaAhOutAddress_Object(
    (1, 3, 6, 1, 4, 1, 3097, 3, 1, 1, 5, 1, 1),
    _WgIpsecSaAhOutAddress_Type()
)
wgIpsecSaAhOutAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wgIpsecSaAhOutAddress.setStatus("current")
_WgIpsecSaAhOutSpi_Type = Integer32
_WgIpsecSaAhOutSpi_Object = MibTableColumn
wgIpsecSaAhOutSpi = _WgIpsecSaAhOutSpi_Object(
    (1, 3, 6, 1, 4, 1, 3097, 3, 1, 1, 5, 1, 2),
    _WgIpsecSaAhOutSpi_Type()
)
wgIpsecSaAhOutSpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wgIpsecSaAhOutSpi.setStatus("current")


class _WgIpsecSaAhOutSourceId_Type(OctetString):
    """Custom type wgIpsecSaAhOutSourceId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 255),
    )


_WgIpsecSaAhOutSourceId_Type.__name__ = "OctetString"
_WgIpsecSaAhOutSourceId_Object = MibTableColumn
wgIpsecSaAhOutSourceId = _WgIpsecSaAhOutSourceId_Object(
    (1, 3, 6, 1, 4, 1, 3097, 3, 1, 1, 5, 1, 3),
    _WgIpsecSaAhOutSourceId_Type()
)
wgIpsecSaAhOutSourceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wgIpsecSaAhOutSourceId.setStatus("current")
_WgIpsecSaAhOutSourceIdType_Type = IpsecDoiIdentType
_WgIpsecSaAhOutSourceIdType_Object = MibTableColumn
wgIpsecSaAhOutSourceIdType = _WgIpsecSaAhOutSourceIdType_Object(
    (1, 3, 6, 1, 4, 1, 3097, 3, 1, 1, 5, 1, 4),
    _WgIpsecSaAhOutSourceIdType_Type()
)
wgIpsecSaAhOutSourceIdType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wgIpsecSaAhOutSourceIdType.setStatus("current")


class _WgIpsecSaAhOutDestId_Type(OctetString):
    """Custom type wgIpsecSaAhOutDestId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 255),
    )


_WgIpsecSaAhOutDestId_Type.__name__ = "OctetString"
_WgIpsecSaAhOutDestId_Object = MibTableColumn
wgIpsecSaAhOutDestId = _WgIpsecSaAhOutDestId_Object(
    (1, 3, 6, 1, 4, 1, 3097, 3, 1, 1, 5, 1, 5),
    _WgIpsecSaAhOutDestId_Type()
)
wgIpsecSaAhOutDestId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wgIpsecSaAhOutDestId.setStatus("current")
_WgIpsecSaAhOutDestIdType_Type = IpsecDoiIdentType
_WgIpsecSaAhOutDestIdType_Object = MibTableColumn
wgIpsecSaAhOutDestIdType = _WgIpsecSaAhOutDestIdType_Object(
    (1, 3, 6, 1, 4, 1, 3097, 3, 1, 1, 5, 1, 6),
    _WgIpsecSaAhOutDestIdType_Type()
)
wgIpsecSaAhOutDestIdType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wgIpsecSaAhOutDestIdType.setStatus("current")


class _WgIpsecSaAhOutProtocol_Type(Integer32):
    """Custom type wgIpsecSaAhOutProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_WgIpsecSaAhOutProtocol_Type.__name__ = "Integer32"
_WgIpsecSaAhOutProtocol_Object = MibTableColumn
wgIpsecSaAhOutProtocol = _WgIpsecSaAhOutProtocol_Object(
    (1, 3, 6, 1, 4, 1, 3097, 3, 1, 1, 5, 1, 7),
    _WgIpsecSaAhOutProtocol_Type()
)
wgIpsecSaAhOutProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wgIpsecSaAhOutProtocol.setStatus("current")


class _WgIpsecSaAhOutSourcePort_Type(Integer32):
    """Custom type wgIpsecSaAhOutSourcePort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WgIpsecSaAhOutSourcePort_Type.__name__ = "Integer32"
_WgIpsecSaAhOutSourcePort_Object = MibTableColumn
wgIpsecSaAhOutSourcePort = _WgIpsecSaAhOutSourcePort_Object(
    (1, 3, 6, 1, 4, 1, 3097, 3, 1, 1, 5, 1, 8),
    _WgIpsecSaAhOutSourcePort_Type()
)
wgIpsecSaAhOutSourcePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wgIpsecSaAhOutSourcePort.setStatus("current")


class _WgIpsecSaAhOutDestPort_Type(Integer32):
    """Custom type wgIpsecSaAhOutDestPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WgIpsecSaAhOutDestPort_Type.__name__ = "Integer32"
_WgIpsecSaAhOutDestPort_Object = MibTableColumn
wgIpsecSaAhOutDestPort = _WgIpsecSaAhOutDestPort_Object(
    (1, 3, 6, 1, 4, 1, 3097, 3, 1, 1, 5, 1, 9),
    _WgIpsecSaAhOutDestPort_Type()
)
wgIpsecSaAhOutDestPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wgIpsecSaAhOutDestPort.setStatus("current")
_WgIpsecSaAhOutCreator_Type = IpsecSaCreatorIdent
_WgIpsecSaAhOutCreator_Object = MibTableColumn
wgIpsecSaAhOutCreator = _WgIpsecSaAhOutCreator_Object(
    (1, 3, 6, 1, 4, 1, 3097, 3, 1, 1, 5, 1, 10),
    _WgIpsecSaAhOutCreator_Type()
)
wgIpsecSaAhOutCreator.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wgIpsecSaAhOutCreator.setStatus("current")
_WgIpsecSaAhOutEncapsulation_Type = IpsecDoiEncapsulationMode
_WgIpsecSaAhOutEncapsulation_Object = MibTableColumn
wgIpsecSaAhOutEncapsulation = _WgIpsecSaAhOutEncapsulation_Object(
    (1, 3, 6, 1, 4, 1, 3097, 3, 1, 1, 5, 1, 11),
    _WgIpsecSaAhOutEncapsulation_Type()
)
wgIpsecSaAhOutEncapsulation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wgIpsecSaAhOutEncapsulation.setStatus("current")
_WgIpsecSaAhOutAuthAlg_Type = IpsecDoiAhTransform
_WgIpsecSaAhOutAuthAlg_Object = MibTableColumn
wgIpsecSaAhOutAuthAlg = _WgIpsecSaAhOutAuthAlg_Object(
    (1, 3, 6, 1, 4, 1, 3097, 3, 1, 1, 5, 1, 12),
    _WgIpsecSaAhOutAuthAlg_Type()
)
wgIpsecSaAhOutAuthAlg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wgIpsecSaAhOutAuthAlg.setStatus("current")
_WgIpsecSaAhOutLimitSeconds_Type = Integer32
_WgIpsecSaAhOutLimitSeconds_Object = MibTableColumn
wgIpsecSaAhOutLimitSeconds = _WgIpsecSaAhOutLimitSeconds_Object(
    (1, 3, 6, 1, 4, 1, 3097, 3, 1, 1, 5, 1, 13),
    _WgIpsecSaAhOutLimitSeconds_Type()
)
wgIpsecSaAhOutLimitSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wgIpsecSaAhOutLimitSeconds.setStatus("current")
if mibBuilder.loadTexts:
    wgIpsecSaAhOutLimitSeconds.setUnits("seconds")
_WgIpsecSaAhOutLimitKbytes_Type = Integer32
_WgIpsecSaAhOutLimitKbytes_Object = MibTableColumn
wgIpsecSaAhOutLimitKbytes = _WgIpsecSaAhOutLimitKbytes_Object(
    (1, 3, 6, 1, 4, 1, 3097, 3, 1, 1, 5, 1, 14),
    _WgIpsecSaAhOutLimitKbytes_Type()
)
wgIpsecSaAhOutLimitKbytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wgIpsecSaAhOutLimitKbytes.setStatus("current")
if mibBuilder.loadTexts:
    wgIpsecSaAhOutLimitKbytes.setUnits("kilobytes")
_WgIpsecSaAhOutAccSeconds_Type = Counter32
_WgIpsecSaAhOutAccSeconds_Object = MibTableColumn
wgIpsecSaAhOutAccSeconds = _WgIpsecSaAhOutAccSeconds_Object(
    (1, 3, 6, 1, 4, 1, 3097, 3, 1, 1, 5, 1, 15),
    _WgIpsecSaAhOutAccSeconds_Type()
)
wgIpsecSaAhOutAccSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wgIpsecSaAhOutAccSeconds.setStatus("current")
if mibBuilder.loadTexts:
    wgIpsecSaAhOutAccSeconds.setUnits("seconds")
_WgIpsecSaAhOutAccKbytes_Type = Counter32
_WgIpsecSaAhOutAccKbytes_Object = MibTableColumn
wgIpsecSaAhOutAccKbytes = _WgIpsecSaAhOutAccKbytes_Object(
    (1, 3, 6, 1, 4, 1, 3097, 3, 1, 1, 5, 1, 16),
    _WgIpsecSaAhOutAccKbytes_Type()
)
wgIpsecSaAhOutAccKbytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wgIpsecSaAhOutAccKbytes.setStatus("current")
if mibBuilder.loadTexts:
    wgIpsecSaAhOutAccKbytes.setUnits("kilobytes")
_WgIpsecSaAhOutUserOctets_Type = Counter32
_WgIpsecSaAhOutUserOctets_Object = MibTableColumn
wgIpsecSaAhOutUserOctets = _WgIpsecSaAhOutUserOctets_Object(
    (1, 3, 6, 1, 4, 1, 3097, 3, 1, 1, 5, 1, 17),
    _WgIpsecSaAhOutUserOctets_Type()
)
wgIpsecSaAhOutUserOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wgIpsecSaAhOutUserOctets.setStatus("current")
if mibBuilder.loadTexts:
    wgIpsecSaAhOutUserOctets.setUnits("bytes")
_WgIpsecSaAhOutPackets_Type = Counter32
_WgIpsecSaAhOutPackets_Object = MibTableColumn
wgIpsecSaAhOutPackets = _WgIpsecSaAhOutPackets_Object(
    (1, 3, 6, 1, 4, 1, 3097, 3, 1, 1, 5, 1, 18),
    _WgIpsecSaAhOutPackets_Type()
)
wgIpsecSaAhOutPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wgIpsecSaAhOutPackets.setStatus("current")
_WgIpsecSaAhOutSendErrors_Type = Counter32
_WgIpsecSaAhOutSendErrors_Object = MibTableColumn
wgIpsecSaAhOutSendErrors = _WgIpsecSaAhOutSendErrors_Object(
    (1, 3, 6, 1, 4, 1, 3097, 3, 1, 1, 5, 1, 19),
    _WgIpsecSaAhOutSendErrors_Type()
)
wgIpsecSaAhOutSendErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wgIpsecSaAhOutSendErrors.setStatus("current")
_WgIpsecSaIpcompOutTable_Object = MibTable
wgIpsecSaIpcompOutTable = _WgIpsecSaIpcompOutTable_Object(
    (1, 3, 6, 1, 4, 1, 3097, 3, 1, 1, 6)
)
if mibBuilder.loadTexts:
    wgIpsecSaIpcompOutTable.setStatus("current")
_WgIpsecSaIpcompOutEntry_Object = MibTableRow
wgIpsecSaIpcompOutEntry = _WgIpsecSaIpcompOutEntry_Object(
    (1, 3, 6, 1, 4, 1, 3097, 3, 1, 1, 6, 1)
)
wgIpsecSaIpcompOutEntry.setIndexNames(
    (0, "WATCHGUARD-IPSEC-SA-MON-MIB-EXT", "wgIpsecSaIpcompOutAddress"),
    (0, "WATCHGUARD-IPSEC-SA-MON-MIB-EXT", "wgIpsecSaIpcompOutCpi"),
)
if mibBuilder.loadTexts:
    wgIpsecSaIpcompOutEntry.setStatus("current")
_WgIpsecSaIpcompOutAddress_Type = IpAddress
_WgIpsecSaIpcompOutAddress_Object = MibTableColumn
wgIpsecSaIpcompOutAddress = _WgIpsecSaIpcompOutAddress_Object(
    (1, 3, 6, 1, 4, 1, 3097, 3, 1, 1, 6, 1, 1),
    _WgIpsecSaIpcompOutAddress_Type()
)
wgIpsecSaIpcompOutAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wgIpsecSaIpcompOutAddress.setStatus("current")
_WgIpsecSaIpcompOutCpi_Type = IpsecDoiIpcompTransform
_WgIpsecSaIpcompOutCpi_Object = MibTableColumn
wgIpsecSaIpcompOutCpi = _WgIpsecSaIpcompOutCpi_Object(
    (1, 3, 6, 1, 4, 1, 3097, 3, 1, 1, 6, 1, 2),
    _WgIpsecSaIpcompOutCpi_Type()
)
wgIpsecSaIpcompOutCpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wgIpsecSaIpcompOutCpi.setStatus("current")


class _WgIpsecSaIpcompOutSourceId_Type(OctetString):
    """Custom type wgIpsecSaIpcompOutSourceId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 255),
    )


_WgIpsecSaIpcompOutSourceId_Type.__name__ = "OctetString"
_WgIpsecSaIpcompOutSourceId_Object = MibTableColumn
wgIpsecSaIpcompOutSourceId = _WgIpsecSaIpcompOutSourceId_Object(
    (1, 3, 6, 1, 4, 1, 3097, 3, 1, 1, 6, 1, 3),
    _WgIpsecSaIpcompOutSourceId_Type()
)
wgIpsecSaIpcompOutSourceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wgIpsecSaIpcompOutSourceId.setStatus("current")
_WgIpsecSaIpcompOutSourceIdType_Type = IpsecDoiIdentType
_WgIpsecSaIpcompOutSourceIdType_Object = MibTableColumn
wgIpsecSaIpcompOutSourceIdType = _WgIpsecSaIpcompOutSourceIdType_Object(
    (1, 3, 6, 1, 4, 1, 3097, 3, 1, 1, 6, 1, 4),
    _WgIpsecSaIpcompOutSourceIdType_Type()
)
wgIpsecSaIpcompOutSourceIdType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wgIpsecSaIpcompOutSourceIdType.setStatus("current")


class _WgIpsecSaIpcompOutDestId_Type(OctetString):
    """Custom type wgIpsecSaIpcompOutDestId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 255),
    )


_WgIpsecSaIpcompOutDestId_Type.__name__ = "OctetString"
_WgIpsecSaIpcompOutDestId_Object = MibTableColumn
wgIpsecSaIpcompOutDestId = _WgIpsecSaIpcompOutDestId_Object(
    (1, 3, 6, 1, 4, 1, 3097, 3, 1, 1, 6, 1, 5),
    _WgIpsecSaIpcompOutDestId_Type()
)
wgIpsecSaIpcompOutDestId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wgIpsecSaIpcompOutDestId.setStatus("current")
_WgIpsecSaIpcompOutDestIdType_Type = IpsecDoiIdentType
_WgIpsecSaIpcompOutDestIdType_Object = MibTableColumn
wgIpsecSaIpcompOutDestIdType = _WgIpsecSaIpcompOutDestIdType_Object(
    (1, 3, 6, 1, 4, 1, 3097, 3, 1, 1, 6, 1, 6),
    _WgIpsecSaIpcompOutDestIdType_Type()
)
wgIpsecSaIpcompOutDestIdType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wgIpsecSaIpcompOutDestIdType.setStatus("current")


class _WgIpsecSaIpcompOutProtocol_Type(Integer32):
    """Custom type wgIpsecSaIpcompOutProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_WgIpsecSaIpcompOutProtocol_Type.__name__ = "Integer32"
_WgIpsecSaIpcompOutProtocol_Object = MibTableColumn
wgIpsecSaIpcompOutProtocol = _WgIpsecSaIpcompOutProtocol_Object(
    (1, 3, 6, 1, 4, 1, 3097, 3, 1, 1, 6, 1, 7),
    _WgIpsecSaIpcompOutProtocol_Type()
)
wgIpsecSaIpcompOutProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wgIpsecSaIpcompOutProtocol.setStatus("current")


class _WgIpsecSaIpcompOutSourcePort_Type(Integer32):
    """Custom type wgIpsecSaIpcompOutSourcePort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WgIpsecSaIpcompOutSourcePort_Type.__name__ = "Integer32"
_WgIpsecSaIpcompOutSourcePort_Object = MibTableColumn
wgIpsecSaIpcompOutSourcePort = _WgIpsecSaIpcompOutSourcePort_Object(
    (1, 3, 6, 1, 4, 1, 3097, 3, 1, 1, 6, 1, 8),
    _WgIpsecSaIpcompOutSourcePort_Type()
)
wgIpsecSaIpcompOutSourcePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wgIpsecSaIpcompOutSourcePort.setStatus("current")


class _WgIpsecSaIpcompOutDestPort_Type(Integer32):
    """Custom type wgIpsecSaIpcompOutDestPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WgIpsecSaIpcompOutDestPort_Type.__name__ = "Integer32"
_WgIpsecSaIpcompOutDestPort_Object = MibTableColumn
wgIpsecSaIpcompOutDestPort = _WgIpsecSaIpcompOutDestPort_Object(
    (1, 3, 6, 1, 4, 1, 3097, 3, 1, 1, 6, 1, 9),
    _WgIpsecSaIpcompOutDestPort_Type()
)
wgIpsecSaIpcompOutDestPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wgIpsecSaIpcompOutDestPort.setStatus("current")
_WgIpsecSaIpcompOutCreator_Type = IpsecSaCreatorIdent
_WgIpsecSaIpcompOutCreator_Object = MibTableColumn
wgIpsecSaIpcompOutCreator = _WgIpsecSaIpcompOutCreator_Object(
    (1, 3, 6, 1, 4, 1, 3097, 3, 1, 1, 6, 1, 10),
    _WgIpsecSaIpcompOutCreator_Type()
)
wgIpsecSaIpcompOutCreator.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wgIpsecSaIpcompOutCreator.setStatus("current")
_WgIpsecSaIpcompOutEncapsulation_Type = IpsecDoiEncapsulationMode
_WgIpsecSaIpcompOutEncapsulation_Object = MibTableColumn
wgIpsecSaIpcompOutEncapsulation = _WgIpsecSaIpcompOutEncapsulation_Object(
    (1, 3, 6, 1, 4, 1, 3097, 3, 1, 1, 6, 1, 11),
    _WgIpsecSaIpcompOutEncapsulation_Type()
)
wgIpsecSaIpcompOutEncapsulation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wgIpsecSaIpcompOutEncapsulation.setStatus("current")
_WgIpsecSaIpcompOutCompAlg_Type = IpsecDoiIpcompTransform
_WgIpsecSaIpcompOutCompAlg_Object = MibTableColumn
wgIpsecSaIpcompOutCompAlg = _WgIpsecSaIpcompOutCompAlg_Object(
    (1, 3, 6, 1, 4, 1, 3097, 3, 1, 1, 6, 1, 12),
    _WgIpsecSaIpcompOutCompAlg_Type()
)
wgIpsecSaIpcompOutCompAlg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wgIpsecSaIpcompOutCompAlg.setStatus("current")
_WgIpsecSaIpcompOutSeconds_Type = Counter32
_WgIpsecSaIpcompOutSeconds_Object = MibTableColumn
wgIpsecSaIpcompOutSeconds = _WgIpsecSaIpcompOutSeconds_Object(
    (1, 3, 6, 1, 4, 1, 3097, 3, 1, 1, 6, 1, 13),
    _WgIpsecSaIpcompOutSeconds_Type()
)
wgIpsecSaIpcompOutSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wgIpsecSaIpcompOutSeconds.setStatus("current")
if mibBuilder.loadTexts:
    wgIpsecSaIpcompOutSeconds.setUnits("seconds")
_WgIpsecSaIpcompOutUserOctets_Type = Counter32
_WgIpsecSaIpcompOutUserOctets_Object = MibTableColumn
wgIpsecSaIpcompOutUserOctets = _WgIpsecSaIpcompOutUserOctets_Object(
    (1, 3, 6, 1, 4, 1, 3097, 3, 1, 1, 6, 1, 14),
    _WgIpsecSaIpcompOutUserOctets_Type()
)
wgIpsecSaIpcompOutUserOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wgIpsecSaIpcompOutUserOctets.setStatus("current")
if mibBuilder.loadTexts:
    wgIpsecSaIpcompOutUserOctets.setUnits("bytes")
_WgIpsecSaIpcompOutPackets_Type = Counter32
_WgIpsecSaIpcompOutPackets_Object = MibTableColumn
wgIpsecSaIpcompOutPackets = _WgIpsecSaIpcompOutPackets_Object(
    (1, 3, 6, 1, 4, 1, 3097, 3, 1, 1, 6, 1, 15),
    _WgIpsecSaIpcompOutPackets_Type()
)
wgIpsecSaIpcompOutPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wgIpsecSaIpcompOutPackets.setStatus("current")
_WgSaStatistics_ObjectIdentity = ObjectIdentity
wgSaStatistics = _WgSaStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3097, 3, 1, 2)
)
if mibBuilder.loadTexts:
    wgSaStatistics.setStatus("current")
_WgIpsecEspCurrentInboundSAs_Type = Gauge32
_WgIpsecEspCurrentInboundSAs_Object = MibScalar
wgIpsecEspCurrentInboundSAs = _WgIpsecEspCurrentInboundSAs_Object(
    (1, 3, 6, 1, 4, 1, 3097, 3, 1, 2, 1),
    _WgIpsecEspCurrentInboundSAs_Type()
)
wgIpsecEspCurrentInboundSAs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wgIpsecEspCurrentInboundSAs.setStatus("current")
_WgIpsecEspTotalInboundSAs_Type = Counter32
_WgIpsecEspTotalInboundSAs_Object = MibScalar
wgIpsecEspTotalInboundSAs = _WgIpsecEspTotalInboundSAs_Object(
    (1, 3, 6, 1, 4, 1, 3097, 3, 1, 2, 2),
    _WgIpsecEspTotalInboundSAs_Type()
)
wgIpsecEspTotalInboundSAs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wgIpsecEspTotalInboundSAs.setStatus("current")
_WgIpsecEspCurrentOutboundSAs_Type = Gauge32
_WgIpsecEspCurrentOutboundSAs_Object = MibScalar
wgIpsecEspCurrentOutboundSAs = _WgIpsecEspCurrentOutboundSAs_Object(
    (1, 3, 6, 1, 4, 1, 3097, 3, 1, 2, 3),
    _WgIpsecEspCurrentOutboundSAs_Type()
)
wgIpsecEspCurrentOutboundSAs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wgIpsecEspCurrentOutboundSAs.setStatus("current")
_WgIpsecEspTotalOutboundSAs_Type = Counter32
_WgIpsecEspTotalOutboundSAs_Object = MibScalar
wgIpsecEspTotalOutboundSAs = _WgIpsecEspTotalOutboundSAs_Object(
    (1, 3, 6, 1, 4, 1, 3097, 3, 1, 2, 4),
    _WgIpsecEspTotalOutboundSAs_Type()
)
wgIpsecEspTotalOutboundSAs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wgIpsecEspTotalOutboundSAs.setStatus("current")
_WgIpsecAhCurrentInboundSAs_Type = Gauge32
_WgIpsecAhCurrentInboundSAs_Object = MibScalar
wgIpsecAhCurrentInboundSAs = _WgIpsecAhCurrentInboundSAs_Object(
    (1, 3, 6, 1, 4, 1, 3097, 3, 1, 2, 5),
    _WgIpsecAhCurrentInboundSAs_Type()
)
wgIpsecAhCurrentInboundSAs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wgIpsecAhCurrentInboundSAs.setStatus("current")
_WgIpsecAhTotalInboundSAs_Type = Counter32
_WgIpsecAhTotalInboundSAs_Object = MibScalar
wgIpsecAhTotalInboundSAs = _WgIpsecAhTotalInboundSAs_Object(
    (1, 3, 6, 1, 4, 1, 3097, 3, 1, 2, 6),
    _WgIpsecAhTotalInboundSAs_Type()
)
wgIpsecAhTotalInboundSAs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wgIpsecAhTotalInboundSAs.setStatus("current")
_WgIpsecAhCurrentOutboundSAs_Type = Gauge32
_WgIpsecAhCurrentOutboundSAs_Object = MibScalar
wgIpsecAhCurrentOutboundSAs = _WgIpsecAhCurrentOutboundSAs_Object(
    (1, 3, 6, 1, 4, 1, 3097, 3, 1, 2, 7),
    _WgIpsecAhCurrentOutboundSAs_Type()
)
wgIpsecAhCurrentOutboundSAs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wgIpsecAhCurrentOutboundSAs.setStatus("current")
_WgIpsecAhTotalOutboundSAs_Type = Counter32
_WgIpsecAhTotalOutboundSAs_Object = MibScalar
wgIpsecAhTotalOutboundSAs = _WgIpsecAhTotalOutboundSAs_Object(
    (1, 3, 6, 1, 4, 1, 3097, 3, 1, 2, 8),
    _WgIpsecAhTotalOutboundSAs_Type()
)
wgIpsecAhTotalOutboundSAs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wgIpsecAhTotalOutboundSAs.setStatus("current")
_WgIpsecIpcompCurrentInboundSAs_Type = Gauge32
_WgIpsecIpcompCurrentInboundSAs_Object = MibScalar
wgIpsecIpcompCurrentInboundSAs = _WgIpsecIpcompCurrentInboundSAs_Object(
    (1, 3, 6, 1, 4, 1, 3097, 3, 1, 2, 9),
    _WgIpsecIpcompCurrentInboundSAs_Type()
)
wgIpsecIpcompCurrentInboundSAs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wgIpsecIpcompCurrentInboundSAs.setStatus("current")
_WgIpsecIpcompTotalInboundSAs_Type = Counter32
_WgIpsecIpcompTotalInboundSAs_Object = MibScalar
wgIpsecIpcompTotalInboundSAs = _WgIpsecIpcompTotalInboundSAs_Object(
    (1, 3, 6, 1, 4, 1, 3097, 3, 1, 2, 10),
    _WgIpsecIpcompTotalInboundSAs_Type()
)
wgIpsecIpcompTotalInboundSAs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wgIpsecIpcompTotalInboundSAs.setStatus("current")
_WgIpsecIpcompCurrentOutboundSAs_Type = Gauge32
_WgIpsecIpcompCurrentOutboundSAs_Object = MibScalar
wgIpsecIpcompCurrentOutboundSAs = _WgIpsecIpcompCurrentOutboundSAs_Object(
    (1, 3, 6, 1, 4, 1, 3097, 3, 1, 2, 11),
    _WgIpsecIpcompCurrentOutboundSAs_Type()
)
wgIpsecIpcompCurrentOutboundSAs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wgIpsecIpcompCurrentOutboundSAs.setStatus("current")
_WgIpsecIpcompTotalOutboundSAs_Type = Counter32
_WgIpsecIpcompTotalOutboundSAs_Object = MibScalar
wgIpsecIpcompTotalOutboundSAs = _WgIpsecIpcompTotalOutboundSAs_Object(
    (1, 3, 6, 1, 4, 1, 3097, 3, 1, 2, 12),
    _WgIpsecIpcompTotalOutboundSAs_Type()
)
wgIpsecIpcompTotalOutboundSAs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wgIpsecIpcompTotalOutboundSAs.setStatus("current")
_WgSaErrors_ObjectIdentity = ObjectIdentity
wgSaErrors = _WgSaErrors_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3097, 3, 1, 3)
)
if mibBuilder.loadTexts:
    wgSaErrors.setStatus("current")
_WgIpsecDecryptionErrors_Type = Counter32
_WgIpsecDecryptionErrors_Object = MibScalar
wgIpsecDecryptionErrors = _WgIpsecDecryptionErrors_Object(
    (1, 3, 6, 1, 4, 1, 3097, 3, 1, 3, 1),
    _WgIpsecDecryptionErrors_Type()
)
wgIpsecDecryptionErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wgIpsecDecryptionErrors.setStatus("current")
_WgIpsecAuthenticationErrors_Type = Counter32
_WgIpsecAuthenticationErrors_Object = MibScalar
wgIpsecAuthenticationErrors = _WgIpsecAuthenticationErrors_Object(
    (1, 3, 6, 1, 4, 1, 3097, 3, 1, 3, 2),
    _WgIpsecAuthenticationErrors_Type()
)
wgIpsecAuthenticationErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wgIpsecAuthenticationErrors.setStatus("current")
_WgIpsecReplayErrors_Type = Counter32
_WgIpsecReplayErrors_Object = MibScalar
wgIpsecReplayErrors = _WgIpsecReplayErrors_Object(
    (1, 3, 6, 1, 4, 1, 3097, 3, 1, 3, 3),
    _WgIpsecReplayErrors_Type()
)
wgIpsecReplayErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wgIpsecReplayErrors.setStatus("current")
_WgIpsecPolicyErrors_Type = Counter32
_WgIpsecPolicyErrors_Object = MibScalar
wgIpsecPolicyErrors = _WgIpsecPolicyErrors_Object(
    (1, 3, 6, 1, 4, 1, 3097, 3, 1, 3, 4),
    _WgIpsecPolicyErrors_Type()
)
wgIpsecPolicyErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wgIpsecPolicyErrors.setStatus("current")
_WgIpsecOtherReceiveErrors_Type = Counter32
_WgIpsecOtherReceiveErrors_Object = MibScalar
wgIpsecOtherReceiveErrors = _WgIpsecOtherReceiveErrors_Object(
    (1, 3, 6, 1, 4, 1, 3097, 3, 1, 3, 5),
    _WgIpsecOtherReceiveErrors_Type()
)
wgIpsecOtherReceiveErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wgIpsecOtherReceiveErrors.setStatus("current")
_WgIpsecSendErrors_Type = Counter32
_WgIpsecSendErrors_Object = MibScalar
wgIpsecSendErrors = _WgIpsecSendErrors_Object(
    (1, 3, 6, 1, 4, 1, 3097, 3, 1, 3, 6),
    _WgIpsecSendErrors_Type()
)
wgIpsecSendErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wgIpsecSendErrors.setStatus("current")
_WgIpsecUnknownSpiErrors_Type = Counter32
_WgIpsecUnknownSpiErrors_Object = MibScalar
wgIpsecUnknownSpiErrors = _WgIpsecUnknownSpiErrors_Object(
    (1, 3, 6, 1, 4, 1, 3097, 3, 1, 3, 7),
    _WgIpsecUnknownSpiErrors_Type()
)
wgIpsecUnknownSpiErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wgIpsecUnknownSpiErrors.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "WATCHGUARD-IPSEC-SA-MON-MIB-EXT",
    **{"IpsecSaCreatorIdent": IpsecSaCreatorIdent,
       "IpsecIpv6Address": IpsecIpv6Address,
       "wgIpsecSaMonModule": wgIpsecSaMonModule,
       "wgIpsecSaMonitorMIB": wgIpsecSaMonitorMIB,
       "wgSaTables": wgSaTables,
       "wgIpsecSaEspInTable": wgIpsecSaEspInTable,
       "wgIpsecSaEspInEntry": wgIpsecSaEspInEntry,
       "wgIpsecSaEspInAddress": wgIpsecSaEspInAddress,
       "wgIpsecSaEspInSpi": wgIpsecSaEspInSpi,
       "wgIpsecSaEspInDestId": wgIpsecSaEspInDestId,
       "wgIpsecSaEspInDestIdType": wgIpsecSaEspInDestIdType,
       "wgIpsecSaEspInSourceId": wgIpsecSaEspInSourceId,
       "wgIpsecSaEspInSourceIdType": wgIpsecSaEspInSourceIdType,
       "wgIpsecSaEspInProtocol": wgIpsecSaEspInProtocol,
       "wgIpsecSaEspInDestPort": wgIpsecSaEspInDestPort,
       "wgIpsecSaEspInSourcePort": wgIpsecSaEspInSourcePort,
       "wgIpsecSaEspInCreator": wgIpsecSaEspInCreator,
       "wgIpsecSaEspInEncapsulation": wgIpsecSaEspInEncapsulation,
       "wgIpsecSaEspInEncAlg": wgIpsecSaEspInEncAlg,
       "wgIpsecSaEspInEncKeyLength": wgIpsecSaEspInEncKeyLength,
       "wgIpsecSaEspInAuthAlg": wgIpsecSaEspInAuthAlg,
       "wgIpsecSaEspInLimitSeconds": wgIpsecSaEspInLimitSeconds,
       "wgIpsecSaEspInLimitKbytes": wgIpsecSaEspInLimitKbytes,
       "wgIpsecSaEspInAccSeconds": wgIpsecSaEspInAccSeconds,
       "wgIpsecSaEspInAccKbytes": wgIpsecSaEspInAccKbytes,
       "wgIpsecSaEspInUserOctets": wgIpsecSaEspInUserOctets,
       "wgIpsecSaEspInPackets": wgIpsecSaEspInPackets,
       "wgIpsecSaEspInDecryptErrors": wgIpsecSaEspInDecryptErrors,
       "wgIpsecSaEspInAuthErrors": wgIpsecSaEspInAuthErrors,
       "wgIpsecSaEspInReplayErrors": wgIpsecSaEspInReplayErrors,
       "wgIpsecSaEspInPolicyErrors": wgIpsecSaEspInPolicyErrors,
       "wgIpsecSaEspInPadErrors": wgIpsecSaEspInPadErrors,
       "wgIpsecSaEspInOtherReceiveErrors": wgIpsecSaEspInOtherReceiveErrors,
       "wgIpsecSaAhInTable": wgIpsecSaAhInTable,
       "wgIpsecSaAhInEntry": wgIpsecSaAhInEntry,
       "wgIpsecSaAhInAddress": wgIpsecSaAhInAddress,
       "wgIpsecSaAhInSpi": wgIpsecSaAhInSpi,
       "wgIpsecSaAhInDestId": wgIpsecSaAhInDestId,
       "wgIpsecSaAhInDestIdType": wgIpsecSaAhInDestIdType,
       "wgIpsecSaAhInSourceId": wgIpsecSaAhInSourceId,
       "wgIpsecSaAhInSourceIdType": wgIpsecSaAhInSourceIdType,
       "wgIpsecSaAhInProtocol": wgIpsecSaAhInProtocol,
       "wgIpsecSaAhInDestPort": wgIpsecSaAhInDestPort,
       "wgIpsecSaAhInSourcePort": wgIpsecSaAhInSourcePort,
       "wgIpsecSaAhInCreator": wgIpsecSaAhInCreator,
       "wgIpsecSaAhInEncapsulation": wgIpsecSaAhInEncapsulation,
       "wgIpsecSaAhInAuthAlg": wgIpsecSaAhInAuthAlg,
       "wgIpsecSaAhInLimitSeconds": wgIpsecSaAhInLimitSeconds,
       "wgIpsecSaAhInLimitKbytes": wgIpsecSaAhInLimitKbytes,
       "wgIpsecSaAhInAccSeconds": wgIpsecSaAhInAccSeconds,
       "wgIpsecSaAhInAccKbytes": wgIpsecSaAhInAccKbytes,
       "wgIpsecSaAhInUserOctets": wgIpsecSaAhInUserOctets,
       "wgIpsecSaAhInPackets": wgIpsecSaAhInPackets,
       "wgIpsecSaAhInAuthErrors": wgIpsecSaAhInAuthErrors,
       "wgIpsecSaAhInReplayErrors": wgIpsecSaAhInReplayErrors,
       "wgIpsecSaAhInPolicyErrors": wgIpsecSaAhInPolicyErrors,
       "wgIpsecSaAhInOtherReceiveErrors": wgIpsecSaAhInOtherReceiveErrors,
       "wgIpsecSaIpcompInTable": wgIpsecSaIpcompInTable,
       "wgIpsecSaIpcompInEntry": wgIpsecSaIpcompInEntry,
       "wgIpsecSaIpcompInAddress": wgIpsecSaIpcompInAddress,
       "wgIpsecSaIpcompInCpi": wgIpsecSaIpcompInCpi,
       "wgIpsecSaIpcompInDestId": wgIpsecSaIpcompInDestId,
       "wgIpsecSaIpcompInDestIdType": wgIpsecSaIpcompInDestIdType,
       "wgIpsecSaIpcompInSourceId": wgIpsecSaIpcompInSourceId,
       "wgIpsecSaIpcompInSourceIdType": wgIpsecSaIpcompInSourceIdType,
       "wgIpsecSaIpcompInProtocol": wgIpsecSaIpcompInProtocol,
       "wgIpsecSaIpcompInDestPort": wgIpsecSaIpcompInDestPort,
       "wgIpsecSaIpcompInSourcePort": wgIpsecSaIpcompInSourcePort,
       "wgIpsecSaIpcompInCreator": wgIpsecSaIpcompInCreator,
       "wgIpsecSaIpcompInEncapsulation": wgIpsecSaIpcompInEncapsulation,
       "wgIpsecSaIpcompInDecompAlg": wgIpsecSaIpcompInDecompAlg,
       "wgIpsecSaIpcompInSeconds": wgIpsecSaIpcompInSeconds,
       "wgIpsecSaIpcompInUserOctets": wgIpsecSaIpcompInUserOctets,
       "wgIpsecSaIpcompInPackets": wgIpsecSaIpcompInPackets,
       "wgIpsecSaIpcompInDecompErrors": wgIpsecSaIpcompInDecompErrors,
       "wgIpsecSaIpcompInOtherReceiveErrors": wgIpsecSaIpcompInOtherReceiveErrors,
       "wgIpsecSaEspOutTable": wgIpsecSaEspOutTable,
       "wgIpsecSaEspOutEntry": wgIpsecSaEspOutEntry,
       "wgIpsecSaEspOutAddress": wgIpsecSaEspOutAddress,
       "wgIpsecSaEspOutSpi": wgIpsecSaEspOutSpi,
       "wgIpsecSaEspOutSourceId": wgIpsecSaEspOutSourceId,
       "wgIpsecSaEspOutSourceIdType": wgIpsecSaEspOutSourceIdType,
       "wgIpsecSaEspOutDestId": wgIpsecSaEspOutDestId,
       "wgIpsecSaEspOutDestIdType": wgIpsecSaEspOutDestIdType,
       "wgIpsecSaEspOutProtocol": wgIpsecSaEspOutProtocol,
       "wgIpsecSaEspOutSourcePort": wgIpsecSaEspOutSourcePort,
       "wgIpsecSaEspOutDestPort": wgIpsecSaEspOutDestPort,
       "wgIpsecSaEspOutCreator": wgIpsecSaEspOutCreator,
       "wgIpsecSaEspOutEncapsulation": wgIpsecSaEspOutEncapsulation,
       "wgIpsecSaEspOutEncAlg": wgIpsecSaEspOutEncAlg,
       "wgIpsecSaEspOutEncKeyLength": wgIpsecSaEspOutEncKeyLength,
       "wgIpsecSaEspOutAuthAlg": wgIpsecSaEspOutAuthAlg,
       "wgIpsecSaEspOutLimitSeconds": wgIpsecSaEspOutLimitSeconds,
       "wgIpsecSaEspOutLimitKbytes": wgIpsecSaEspOutLimitKbytes,
       "wgIpsecSaEspOutAccSeconds": wgIpsecSaEspOutAccSeconds,
       "wgIpsecSaEspOutAccKbytes": wgIpsecSaEspOutAccKbytes,
       "wgIpsecSaEspOutUserOctets": wgIpsecSaEspOutUserOctets,
       "wgIpsecSaEspOutPackets": wgIpsecSaEspOutPackets,
       "wgIpsecSaEspOutSendErrors": wgIpsecSaEspOutSendErrors,
       "wgIpsecSaAhOutTable": wgIpsecSaAhOutTable,
       "wgIpsecSaAhOutEntry": wgIpsecSaAhOutEntry,
       "wgIpsecSaAhOutAddress": wgIpsecSaAhOutAddress,
       "wgIpsecSaAhOutSpi": wgIpsecSaAhOutSpi,
       "wgIpsecSaAhOutSourceId": wgIpsecSaAhOutSourceId,
       "wgIpsecSaAhOutSourceIdType": wgIpsecSaAhOutSourceIdType,
       "wgIpsecSaAhOutDestId": wgIpsecSaAhOutDestId,
       "wgIpsecSaAhOutDestIdType": wgIpsecSaAhOutDestIdType,
       "wgIpsecSaAhOutProtocol": wgIpsecSaAhOutProtocol,
       "wgIpsecSaAhOutSourcePort": wgIpsecSaAhOutSourcePort,
       "wgIpsecSaAhOutDestPort": wgIpsecSaAhOutDestPort,
       "wgIpsecSaAhOutCreator": wgIpsecSaAhOutCreator,
       "wgIpsecSaAhOutEncapsulation": wgIpsecSaAhOutEncapsulation,
       "wgIpsecSaAhOutAuthAlg": wgIpsecSaAhOutAuthAlg,
       "wgIpsecSaAhOutLimitSeconds": wgIpsecSaAhOutLimitSeconds,
       "wgIpsecSaAhOutLimitKbytes": wgIpsecSaAhOutLimitKbytes,
       "wgIpsecSaAhOutAccSeconds": wgIpsecSaAhOutAccSeconds,
       "wgIpsecSaAhOutAccKbytes": wgIpsecSaAhOutAccKbytes,
       "wgIpsecSaAhOutUserOctets": wgIpsecSaAhOutUserOctets,
       "wgIpsecSaAhOutPackets": wgIpsecSaAhOutPackets,
       "wgIpsecSaAhOutSendErrors": wgIpsecSaAhOutSendErrors,
       "wgIpsecSaIpcompOutTable": wgIpsecSaIpcompOutTable,
       "wgIpsecSaIpcompOutEntry": wgIpsecSaIpcompOutEntry,
       "wgIpsecSaIpcompOutAddress": wgIpsecSaIpcompOutAddress,
       "wgIpsecSaIpcompOutCpi": wgIpsecSaIpcompOutCpi,
       "wgIpsecSaIpcompOutSourceId": wgIpsecSaIpcompOutSourceId,
       "wgIpsecSaIpcompOutSourceIdType": wgIpsecSaIpcompOutSourceIdType,
       "wgIpsecSaIpcompOutDestId": wgIpsecSaIpcompOutDestId,
       "wgIpsecSaIpcompOutDestIdType": wgIpsecSaIpcompOutDestIdType,
       "wgIpsecSaIpcompOutProtocol": wgIpsecSaIpcompOutProtocol,
       "wgIpsecSaIpcompOutSourcePort": wgIpsecSaIpcompOutSourcePort,
       "wgIpsecSaIpcompOutDestPort": wgIpsecSaIpcompOutDestPort,
       "wgIpsecSaIpcompOutCreator": wgIpsecSaIpcompOutCreator,
       "wgIpsecSaIpcompOutEncapsulation": wgIpsecSaIpcompOutEncapsulation,
       "wgIpsecSaIpcompOutCompAlg": wgIpsecSaIpcompOutCompAlg,
       "wgIpsecSaIpcompOutSeconds": wgIpsecSaIpcompOutSeconds,
       "wgIpsecSaIpcompOutUserOctets": wgIpsecSaIpcompOutUserOctets,
       "wgIpsecSaIpcompOutPackets": wgIpsecSaIpcompOutPackets,
       "wgSaStatistics": wgSaStatistics,
       "wgIpsecEspCurrentInboundSAs": wgIpsecEspCurrentInboundSAs,
       "wgIpsecEspTotalInboundSAs": wgIpsecEspTotalInboundSAs,
       "wgIpsecEspCurrentOutboundSAs": wgIpsecEspCurrentOutboundSAs,
       "wgIpsecEspTotalOutboundSAs": wgIpsecEspTotalOutboundSAs,
       "wgIpsecAhCurrentInboundSAs": wgIpsecAhCurrentInboundSAs,
       "wgIpsecAhTotalInboundSAs": wgIpsecAhTotalInboundSAs,
       "wgIpsecAhCurrentOutboundSAs": wgIpsecAhCurrentOutboundSAs,
       "wgIpsecAhTotalOutboundSAs": wgIpsecAhTotalOutboundSAs,
       "wgIpsecIpcompCurrentInboundSAs": wgIpsecIpcompCurrentInboundSAs,
       "wgIpsecIpcompTotalInboundSAs": wgIpsecIpcompTotalInboundSAs,
       "wgIpsecIpcompCurrentOutboundSAs": wgIpsecIpcompCurrentOutboundSAs,
       "wgIpsecIpcompTotalOutboundSAs": wgIpsecIpcompTotalOutboundSAs,
       "wgSaErrors": wgSaErrors,
       "wgIpsecDecryptionErrors": wgIpsecDecryptionErrors,
       "wgIpsecAuthenticationErrors": wgIpsecAuthenticationErrors,
       "wgIpsecReplayErrors": wgIpsecReplayErrors,
       "wgIpsecPolicyErrors": wgIpsecPolicyErrors,
       "wgIpsecOtherReceiveErrors": wgIpsecOtherReceiveErrors,
       "wgIpsecSendErrors": wgIpsecSendErrors,
       "wgIpsecUnknownSpiErrors": wgIpsecUnknownSpiErrors}
)
