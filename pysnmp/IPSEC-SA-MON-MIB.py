# SNMP MIB module (IPSEC-SA-MON-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/IPSEC-SA-MON-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:11:15 2024
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
 experimental,
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
    "experimental",
    "iso")

(DisplayString,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

ipsecSaMonModule = ModuleIdentity(
    (1, 3, 6, 1, 3, 98)
)
ipsecSaMonModule.setRevisions(
        ("1999-06-03 12:00",
         "1999-06-25 12:00",
         "1999-10-21 12:00")
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



class IpsecRawId(OctetString, TextualConvention):
    status = "current"
    displayHint = "x"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )



# MIB Managed Objects in the order of their OIDs

_IpsecSaMonitorMIB_ObjectIdentity = ObjectIdentity
ipsecSaMonitorMIB = _IpsecSaMonitorMIB_ObjectIdentity(
    (1, 3, 6, 1, 3, 98, 1)
)
if mibBuilder.loadTexts:
    ipsecSaMonitorMIB.setStatus("current")
_SaTables_ObjectIdentity = ObjectIdentity
saTables = _SaTables_ObjectIdentity(
    (1, 3, 6, 1, 3, 98, 1, 1)
)
if mibBuilder.loadTexts:
    saTables.setStatus("current")
_IpsecSaEspInTable_Object = MibTable
ipsecSaEspInTable = _IpsecSaEspInTable_Object(
    (1, 3, 6, 1, 3, 98, 1, 1, 1)
)
if mibBuilder.loadTexts:
    ipsecSaEspInTable.setStatus("current")
_IpsecSaEspInEntry_Object = MibTableRow
ipsecSaEspInEntry = _IpsecSaEspInEntry_Object(
    (1, 3, 6, 1, 3, 98, 1, 1, 1, 1)
)
ipsecSaEspInEntry.setIndexNames(
    (0, "IPSEC-SA-MON-MIB", "ipsecSaEspInAddress"),
    (0, "IPSEC-SA-MON-MIB", "ipsecSaEspInSpi"),
)
if mibBuilder.loadTexts:
    ipsecSaEspInEntry.setStatus("current")
_IpsecSaEspInAddress_Type = IpsecIpv6Address
_IpsecSaEspInAddress_Object = MibTableColumn
ipsecSaEspInAddress = _IpsecSaEspInAddress_Object(
    (1, 3, 6, 1, 3, 98, 1, 1, 1, 1, 1),
    _IpsecSaEspInAddress_Type()
)
ipsecSaEspInAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecSaEspInAddress.setStatus("current")
_IpsecSaEspInSpi_Type = Unsigned32
_IpsecSaEspInSpi_Object = MibTableColumn
ipsecSaEspInSpi = _IpsecSaEspInSpi_Object(
    (1, 3, 6, 1, 3, 98, 1, 1, 1, 1, 2),
    _IpsecSaEspInSpi_Type()
)
ipsecSaEspInSpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecSaEspInSpi.setStatus("current")
_IpsecSaEspInDestId_Type = IpsecRawId
_IpsecSaEspInDestId_Object = MibTableColumn
ipsecSaEspInDestId = _IpsecSaEspInDestId_Object(
    (1, 3, 6, 1, 3, 98, 1, 1, 1, 1, 3),
    _IpsecSaEspInDestId_Type()
)
ipsecSaEspInDestId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecSaEspInDestId.setStatus("current")
_IpsecSaEspInDestIdType_Type = IpsecDoiIdentType
_IpsecSaEspInDestIdType_Object = MibTableColumn
ipsecSaEspInDestIdType = _IpsecSaEspInDestIdType_Object(
    (1, 3, 6, 1, 3, 98, 1, 1, 1, 1, 4),
    _IpsecSaEspInDestIdType_Type()
)
ipsecSaEspInDestIdType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecSaEspInDestIdType.setStatus("current")
_IpsecSaEspInSourceId_Type = IpsecRawId
_IpsecSaEspInSourceId_Object = MibTableColumn
ipsecSaEspInSourceId = _IpsecSaEspInSourceId_Object(
    (1, 3, 6, 1, 3, 98, 1, 1, 1, 1, 5),
    _IpsecSaEspInSourceId_Type()
)
ipsecSaEspInSourceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecSaEspInSourceId.setStatus("current")
_IpsecSaEspInSourceIdType_Type = IpsecDoiIdentType
_IpsecSaEspInSourceIdType_Object = MibTableColumn
ipsecSaEspInSourceIdType = _IpsecSaEspInSourceIdType_Object(
    (1, 3, 6, 1, 3, 98, 1, 1, 1, 1, 6),
    _IpsecSaEspInSourceIdType_Type()
)
ipsecSaEspInSourceIdType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecSaEspInSourceIdType.setStatus("current")


class _IpsecSaEspInProtocol_Type(Integer32):
    """Custom type ipsecSaEspInProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_IpsecSaEspInProtocol_Type.__name__ = "Integer32"
_IpsecSaEspInProtocol_Object = MibTableColumn
ipsecSaEspInProtocol = _IpsecSaEspInProtocol_Object(
    (1, 3, 6, 1, 3, 98, 1, 1, 1, 1, 7),
    _IpsecSaEspInProtocol_Type()
)
ipsecSaEspInProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecSaEspInProtocol.setStatus("current")


class _IpsecSaEspInDestPort_Type(Integer32):
    """Custom type ipsecSaEspInDestPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_IpsecSaEspInDestPort_Type.__name__ = "Integer32"
_IpsecSaEspInDestPort_Object = MibTableColumn
ipsecSaEspInDestPort = _IpsecSaEspInDestPort_Object(
    (1, 3, 6, 1, 3, 98, 1, 1, 1, 1, 8),
    _IpsecSaEspInDestPort_Type()
)
ipsecSaEspInDestPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecSaEspInDestPort.setStatus("current")


class _IpsecSaEspInSourcePort_Type(Integer32):
    """Custom type ipsecSaEspInSourcePort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_IpsecSaEspInSourcePort_Type.__name__ = "Integer32"
_IpsecSaEspInSourcePort_Object = MibTableColumn
ipsecSaEspInSourcePort = _IpsecSaEspInSourcePort_Object(
    (1, 3, 6, 1, 3, 98, 1, 1, 1, 1, 9),
    _IpsecSaEspInSourcePort_Type()
)
ipsecSaEspInSourcePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecSaEspInSourcePort.setStatus("current")
_IpsecSaEspInCreator_Type = IpsecSaCreatorIdent
_IpsecSaEspInCreator_Object = MibTableColumn
ipsecSaEspInCreator = _IpsecSaEspInCreator_Object(
    (1, 3, 6, 1, 3, 98, 1, 1, 1, 1, 10),
    _IpsecSaEspInCreator_Type()
)
ipsecSaEspInCreator.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecSaEspInCreator.setStatus("current")
_IpsecSaEspInEncapsulation_Type = IpsecDoiEncapsulationMode
_IpsecSaEspInEncapsulation_Object = MibTableColumn
ipsecSaEspInEncapsulation = _IpsecSaEspInEncapsulation_Object(
    (1, 3, 6, 1, 3, 98, 1, 1, 1, 1, 11),
    _IpsecSaEspInEncapsulation_Type()
)
ipsecSaEspInEncapsulation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecSaEspInEncapsulation.setStatus("current")
_IpsecSaEspInEncAlg_Type = IpsecDoiEspTransform
_IpsecSaEspInEncAlg_Object = MibTableColumn
ipsecSaEspInEncAlg = _IpsecSaEspInEncAlg_Object(
    (1, 3, 6, 1, 3, 98, 1, 1, 1, 1, 12),
    _IpsecSaEspInEncAlg_Type()
)
ipsecSaEspInEncAlg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecSaEspInEncAlg.setStatus("current")


class _IpsecSaEspInEncKeyLength_Type(Unsigned32):
    """Custom type ipsecSaEspInEncKeyLength based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65531),
    )


_IpsecSaEspInEncKeyLength_Type.__name__ = "Unsigned32"
_IpsecSaEspInEncKeyLength_Object = MibTableColumn
ipsecSaEspInEncKeyLength = _IpsecSaEspInEncKeyLength_Object(
    (1, 3, 6, 1, 3, 98, 1, 1, 1, 1, 13),
    _IpsecSaEspInEncKeyLength_Type()
)
ipsecSaEspInEncKeyLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecSaEspInEncKeyLength.setStatus("current")
if mibBuilder.loadTexts:
    ipsecSaEspInEncKeyLength.setUnits("bits")
_IpsecSaEspInAuthAlg_Type = IpsecDoiAuthAlgorithm
_IpsecSaEspInAuthAlg_Object = MibTableColumn
ipsecSaEspInAuthAlg = _IpsecSaEspInAuthAlg_Object(
    (1, 3, 6, 1, 3, 98, 1, 1, 1, 1, 14),
    _IpsecSaEspInAuthAlg_Type()
)
ipsecSaEspInAuthAlg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecSaEspInAuthAlg.setStatus("current")


class _IpsecSaEspInAuthKeyLength_Type(Unsigned32):
    """Custom type ipsecSaEspInAuthKeyLength based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65531),
    )


_IpsecSaEspInAuthKeyLength_Type.__name__ = "Unsigned32"
_IpsecSaEspInAuthKeyLength_Object = MibTableColumn
ipsecSaEspInAuthKeyLength = _IpsecSaEspInAuthKeyLength_Object(
    (1, 3, 6, 1, 3, 98, 1, 1, 1, 1, 15),
    _IpsecSaEspInAuthKeyLength_Type()
)
ipsecSaEspInAuthKeyLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecSaEspInAuthKeyLength.setStatus("current")
if mibBuilder.loadTexts:
    ipsecSaEspInAuthKeyLength.setUnits("bits")
_IpsecSaEspInRepWinSize_Type = Unsigned32
_IpsecSaEspInRepWinSize_Object = MibTableColumn
ipsecSaEspInRepWinSize = _IpsecSaEspInRepWinSize_Object(
    (1, 3, 6, 1, 3, 98, 1, 1, 1, 1, 16),
    _IpsecSaEspInRepWinSize_Type()
)
ipsecSaEspInRepWinSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecSaEspInRepWinSize.setStatus("current")
_IpsecSaEspInLimitSeconds_Type = Unsigned32
_IpsecSaEspInLimitSeconds_Object = MibTableColumn
ipsecSaEspInLimitSeconds = _IpsecSaEspInLimitSeconds_Object(
    (1, 3, 6, 1, 3, 98, 1, 1, 1, 1, 17),
    _IpsecSaEspInLimitSeconds_Type()
)
ipsecSaEspInLimitSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecSaEspInLimitSeconds.setStatus("current")
if mibBuilder.loadTexts:
    ipsecSaEspInLimitSeconds.setUnits("seconds")
_IpsecSaEspInLimitKbytes_Type = Unsigned32
_IpsecSaEspInLimitKbytes_Object = MibTableColumn
ipsecSaEspInLimitKbytes = _IpsecSaEspInLimitKbytes_Object(
    (1, 3, 6, 1, 3, 98, 1, 1, 1, 1, 18),
    _IpsecSaEspInLimitKbytes_Type()
)
ipsecSaEspInLimitKbytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecSaEspInLimitKbytes.setStatus("current")
if mibBuilder.loadTexts:
    ipsecSaEspInLimitKbytes.setUnits("kilobytes")
_IpsecSaEspInAccSeconds_Type = Counter32
_IpsecSaEspInAccSeconds_Object = MibTableColumn
ipsecSaEspInAccSeconds = _IpsecSaEspInAccSeconds_Object(
    (1, 3, 6, 1, 3, 98, 1, 1, 1, 1, 19),
    _IpsecSaEspInAccSeconds_Type()
)
ipsecSaEspInAccSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecSaEspInAccSeconds.setStatus("current")
if mibBuilder.loadTexts:
    ipsecSaEspInAccSeconds.setUnits("seconds")
_IpsecSaEspInAccKbytes_Type = Counter32
_IpsecSaEspInAccKbytes_Object = MibTableColumn
ipsecSaEspInAccKbytes = _IpsecSaEspInAccKbytes_Object(
    (1, 3, 6, 1, 3, 98, 1, 1, 1, 1, 20),
    _IpsecSaEspInAccKbytes_Type()
)
ipsecSaEspInAccKbytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecSaEspInAccKbytes.setStatus("current")
if mibBuilder.loadTexts:
    ipsecSaEspInAccKbytes.setUnits("kilobytes")
_IpsecSaEspInUserOctets_Type = Counter64
_IpsecSaEspInUserOctets_Object = MibTableColumn
ipsecSaEspInUserOctets = _IpsecSaEspInUserOctets_Object(
    (1, 3, 6, 1, 3, 98, 1, 1, 1, 1, 21),
    _IpsecSaEspInUserOctets_Type()
)
ipsecSaEspInUserOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecSaEspInUserOctets.setStatus("current")
if mibBuilder.loadTexts:
    ipsecSaEspInUserOctets.setUnits("bytes")
_IpsecSaEspInPackets_Type = Counter64
_IpsecSaEspInPackets_Object = MibTableColumn
ipsecSaEspInPackets = _IpsecSaEspInPackets_Object(
    (1, 3, 6, 1, 3, 98, 1, 1, 1, 1, 22),
    _IpsecSaEspInPackets_Type()
)
ipsecSaEspInPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecSaEspInPackets.setStatus("current")
_IpsecSaEspInDecryptErrors_Type = Counter32
_IpsecSaEspInDecryptErrors_Object = MibTableColumn
ipsecSaEspInDecryptErrors = _IpsecSaEspInDecryptErrors_Object(
    (1, 3, 6, 1, 3, 98, 1, 1, 1, 1, 23),
    _IpsecSaEspInDecryptErrors_Type()
)
ipsecSaEspInDecryptErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecSaEspInDecryptErrors.setStatus("current")
_IpsecSaEspInAuthErrors_Type = Counter32
_IpsecSaEspInAuthErrors_Object = MibTableColumn
ipsecSaEspInAuthErrors = _IpsecSaEspInAuthErrors_Object(
    (1, 3, 6, 1, 3, 98, 1, 1, 1, 1, 24),
    _IpsecSaEspInAuthErrors_Type()
)
ipsecSaEspInAuthErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecSaEspInAuthErrors.setStatus("current")
_IpsecSaEspInReplayErrors_Type = Counter32
_IpsecSaEspInReplayErrors_Object = MibTableColumn
ipsecSaEspInReplayErrors = _IpsecSaEspInReplayErrors_Object(
    (1, 3, 6, 1, 3, 98, 1, 1, 1, 1, 25),
    _IpsecSaEspInReplayErrors_Type()
)
ipsecSaEspInReplayErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecSaEspInReplayErrors.setStatus("current")
_IpsecSaEspInPolicyErrors_Type = Counter32
_IpsecSaEspInPolicyErrors_Object = MibTableColumn
ipsecSaEspInPolicyErrors = _IpsecSaEspInPolicyErrors_Object(
    (1, 3, 6, 1, 3, 98, 1, 1, 1, 1, 26),
    _IpsecSaEspInPolicyErrors_Type()
)
ipsecSaEspInPolicyErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecSaEspInPolicyErrors.setStatus("current")
_IpsecSaEspInPadErrors_Type = Counter32
_IpsecSaEspInPadErrors_Object = MibTableColumn
ipsecSaEspInPadErrors = _IpsecSaEspInPadErrors_Object(
    (1, 3, 6, 1, 3, 98, 1, 1, 1, 1, 27),
    _IpsecSaEspInPadErrors_Type()
)
ipsecSaEspInPadErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecSaEspInPadErrors.setStatus("current")
_IpsecSaEspInOtherReceiveErrors_Type = Counter32
_IpsecSaEspInOtherReceiveErrors_Object = MibTableColumn
ipsecSaEspInOtherReceiveErrors = _IpsecSaEspInOtherReceiveErrors_Object(
    (1, 3, 6, 1, 3, 98, 1, 1, 1, 1, 28),
    _IpsecSaEspInOtherReceiveErrors_Type()
)
ipsecSaEspInOtherReceiveErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecSaEspInOtherReceiveErrors.setStatus("current")
_IpsecSaAhInTable_Object = MibTable
ipsecSaAhInTable = _IpsecSaAhInTable_Object(
    (1, 3, 6, 1, 3, 98, 1, 1, 2)
)
if mibBuilder.loadTexts:
    ipsecSaAhInTable.setStatus("current")
_IpsecSaAhInEntry_Object = MibTableRow
ipsecSaAhInEntry = _IpsecSaAhInEntry_Object(
    (1, 3, 6, 1, 3, 98, 1, 1, 2, 1)
)
ipsecSaAhInEntry.setIndexNames(
    (0, "IPSEC-SA-MON-MIB", "ipsecSaAhInAddress"),
    (0, "IPSEC-SA-MON-MIB", "ipsecSaAhInSpi"),
)
if mibBuilder.loadTexts:
    ipsecSaAhInEntry.setStatus("current")
_IpsecSaAhInAddress_Type = IpsecIpv6Address
_IpsecSaAhInAddress_Object = MibTableColumn
ipsecSaAhInAddress = _IpsecSaAhInAddress_Object(
    (1, 3, 6, 1, 3, 98, 1, 1, 2, 1, 1),
    _IpsecSaAhInAddress_Type()
)
ipsecSaAhInAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecSaAhInAddress.setStatus("current")
_IpsecSaAhInSpi_Type = Unsigned32
_IpsecSaAhInSpi_Object = MibTableColumn
ipsecSaAhInSpi = _IpsecSaAhInSpi_Object(
    (1, 3, 6, 1, 3, 98, 1, 1, 2, 1, 2),
    _IpsecSaAhInSpi_Type()
)
ipsecSaAhInSpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecSaAhInSpi.setStatus("current")
_IpsecSaAhInDestId_Type = IpsecRawId
_IpsecSaAhInDestId_Object = MibTableColumn
ipsecSaAhInDestId = _IpsecSaAhInDestId_Object(
    (1, 3, 6, 1, 3, 98, 1, 1, 2, 1, 3),
    _IpsecSaAhInDestId_Type()
)
ipsecSaAhInDestId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecSaAhInDestId.setStatus("current")
_IpsecSaAhInDestIdType_Type = IpsecDoiIdentType
_IpsecSaAhInDestIdType_Object = MibTableColumn
ipsecSaAhInDestIdType = _IpsecSaAhInDestIdType_Object(
    (1, 3, 6, 1, 3, 98, 1, 1, 2, 1, 4),
    _IpsecSaAhInDestIdType_Type()
)
ipsecSaAhInDestIdType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecSaAhInDestIdType.setStatus("current")
_IpsecSaAhInSourceId_Type = IpsecRawId
_IpsecSaAhInSourceId_Object = MibTableColumn
ipsecSaAhInSourceId = _IpsecSaAhInSourceId_Object(
    (1, 3, 6, 1, 3, 98, 1, 1, 2, 1, 5),
    _IpsecSaAhInSourceId_Type()
)
ipsecSaAhInSourceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecSaAhInSourceId.setStatus("current")
_IpsecSaAhInSourceIdType_Type = IpsecDoiIdentType
_IpsecSaAhInSourceIdType_Object = MibTableColumn
ipsecSaAhInSourceIdType = _IpsecSaAhInSourceIdType_Object(
    (1, 3, 6, 1, 3, 98, 1, 1, 2, 1, 6),
    _IpsecSaAhInSourceIdType_Type()
)
ipsecSaAhInSourceIdType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecSaAhInSourceIdType.setStatus("current")


class _IpsecSaAhInProtocol_Type(Integer32):
    """Custom type ipsecSaAhInProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_IpsecSaAhInProtocol_Type.__name__ = "Integer32"
_IpsecSaAhInProtocol_Object = MibTableColumn
ipsecSaAhInProtocol = _IpsecSaAhInProtocol_Object(
    (1, 3, 6, 1, 3, 98, 1, 1, 2, 1, 7),
    _IpsecSaAhInProtocol_Type()
)
ipsecSaAhInProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecSaAhInProtocol.setStatus("current")


class _IpsecSaAhInDestPort_Type(Integer32):
    """Custom type ipsecSaAhInDestPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_IpsecSaAhInDestPort_Type.__name__ = "Integer32"
_IpsecSaAhInDestPort_Object = MibTableColumn
ipsecSaAhInDestPort = _IpsecSaAhInDestPort_Object(
    (1, 3, 6, 1, 3, 98, 1, 1, 2, 1, 8),
    _IpsecSaAhInDestPort_Type()
)
ipsecSaAhInDestPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecSaAhInDestPort.setStatus("current")


class _IpsecSaAhInSourcePort_Type(Integer32):
    """Custom type ipsecSaAhInSourcePort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_IpsecSaAhInSourcePort_Type.__name__ = "Integer32"
_IpsecSaAhInSourcePort_Object = MibTableColumn
ipsecSaAhInSourcePort = _IpsecSaAhInSourcePort_Object(
    (1, 3, 6, 1, 3, 98, 1, 1, 2, 1, 9),
    _IpsecSaAhInSourcePort_Type()
)
ipsecSaAhInSourcePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecSaAhInSourcePort.setStatus("current")
_IpsecSaAhInCreator_Type = IpsecSaCreatorIdent
_IpsecSaAhInCreator_Object = MibTableColumn
ipsecSaAhInCreator = _IpsecSaAhInCreator_Object(
    (1, 3, 6, 1, 3, 98, 1, 1, 2, 1, 10),
    _IpsecSaAhInCreator_Type()
)
ipsecSaAhInCreator.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecSaAhInCreator.setStatus("current")
_IpsecSaAhInEncapsulation_Type = IpsecDoiEncapsulationMode
_IpsecSaAhInEncapsulation_Object = MibTableColumn
ipsecSaAhInEncapsulation = _IpsecSaAhInEncapsulation_Object(
    (1, 3, 6, 1, 3, 98, 1, 1, 2, 1, 11),
    _IpsecSaAhInEncapsulation_Type()
)
ipsecSaAhInEncapsulation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecSaAhInEncapsulation.setStatus("current")
_IpsecSaAhInAuthAlg_Type = IpsecDoiAhTransform
_IpsecSaAhInAuthAlg_Object = MibTableColumn
ipsecSaAhInAuthAlg = _IpsecSaAhInAuthAlg_Object(
    (1, 3, 6, 1, 3, 98, 1, 1, 2, 1, 12),
    _IpsecSaAhInAuthAlg_Type()
)
ipsecSaAhInAuthAlg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecSaAhInAuthAlg.setStatus("current")


class _IpsecSaAhInAuthKeyLength_Type(Unsigned32):
    """Custom type ipsecSaAhInAuthKeyLength based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65531),
    )


_IpsecSaAhInAuthKeyLength_Type.__name__ = "Unsigned32"
_IpsecSaAhInAuthKeyLength_Object = MibTableColumn
ipsecSaAhInAuthKeyLength = _IpsecSaAhInAuthKeyLength_Object(
    (1, 3, 6, 1, 3, 98, 1, 1, 2, 1, 13),
    _IpsecSaAhInAuthKeyLength_Type()
)
ipsecSaAhInAuthKeyLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecSaAhInAuthKeyLength.setStatus("current")
if mibBuilder.loadTexts:
    ipsecSaAhInAuthKeyLength.setUnits("bits")
_IpsecSaAhInRepWinSize_Type = Unsigned32
_IpsecSaAhInRepWinSize_Object = MibTableColumn
ipsecSaAhInRepWinSize = _IpsecSaAhInRepWinSize_Object(
    (1, 3, 6, 1, 3, 98, 1, 1, 2, 1, 14),
    _IpsecSaAhInRepWinSize_Type()
)
ipsecSaAhInRepWinSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecSaAhInRepWinSize.setStatus("current")
_IpsecSaAhInLimitSeconds_Type = Unsigned32
_IpsecSaAhInLimitSeconds_Object = MibTableColumn
ipsecSaAhInLimitSeconds = _IpsecSaAhInLimitSeconds_Object(
    (1, 3, 6, 1, 3, 98, 1, 1, 2, 1, 15),
    _IpsecSaAhInLimitSeconds_Type()
)
ipsecSaAhInLimitSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecSaAhInLimitSeconds.setStatus("current")
if mibBuilder.loadTexts:
    ipsecSaAhInLimitSeconds.setUnits("seconds")
_IpsecSaAhInLimitKbytes_Type = Unsigned32
_IpsecSaAhInLimitKbytes_Object = MibTableColumn
ipsecSaAhInLimitKbytes = _IpsecSaAhInLimitKbytes_Object(
    (1, 3, 6, 1, 3, 98, 1, 1, 2, 1, 16),
    _IpsecSaAhInLimitKbytes_Type()
)
ipsecSaAhInLimitKbytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecSaAhInLimitKbytes.setStatus("current")
if mibBuilder.loadTexts:
    ipsecSaAhInLimitKbytes.setUnits("kilobytes")
_IpsecSaAhInAccSeconds_Type = Counter32
_IpsecSaAhInAccSeconds_Object = MibTableColumn
ipsecSaAhInAccSeconds = _IpsecSaAhInAccSeconds_Object(
    (1, 3, 6, 1, 3, 98, 1, 1, 2, 1, 17),
    _IpsecSaAhInAccSeconds_Type()
)
ipsecSaAhInAccSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecSaAhInAccSeconds.setStatus("current")
if mibBuilder.loadTexts:
    ipsecSaAhInAccSeconds.setUnits("seconds")
_IpsecSaAhInAccKbytes_Type = Counter32
_IpsecSaAhInAccKbytes_Object = MibTableColumn
ipsecSaAhInAccKbytes = _IpsecSaAhInAccKbytes_Object(
    (1, 3, 6, 1, 3, 98, 1, 1, 2, 1, 18),
    _IpsecSaAhInAccKbytes_Type()
)
ipsecSaAhInAccKbytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecSaAhInAccKbytes.setStatus("current")
if mibBuilder.loadTexts:
    ipsecSaAhInAccKbytes.setUnits("kilobytes")
_IpsecSaAhInUserOctets_Type = Counter64
_IpsecSaAhInUserOctets_Object = MibTableColumn
ipsecSaAhInUserOctets = _IpsecSaAhInUserOctets_Object(
    (1, 3, 6, 1, 3, 98, 1, 1, 2, 1, 19),
    _IpsecSaAhInUserOctets_Type()
)
ipsecSaAhInUserOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecSaAhInUserOctets.setStatus("current")
if mibBuilder.loadTexts:
    ipsecSaAhInUserOctets.setUnits("bytes")
_IpsecSaAhInPackets_Type = Counter64
_IpsecSaAhInPackets_Object = MibTableColumn
ipsecSaAhInPackets = _IpsecSaAhInPackets_Object(
    (1, 3, 6, 1, 3, 98, 1, 1, 2, 1, 20),
    _IpsecSaAhInPackets_Type()
)
ipsecSaAhInPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecSaAhInPackets.setStatus("current")
_IpsecSaAhInAuthErrors_Type = Counter32
_IpsecSaAhInAuthErrors_Object = MibTableColumn
ipsecSaAhInAuthErrors = _IpsecSaAhInAuthErrors_Object(
    (1, 3, 6, 1, 3, 98, 1, 1, 2, 1, 21),
    _IpsecSaAhInAuthErrors_Type()
)
ipsecSaAhInAuthErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecSaAhInAuthErrors.setStatus("current")
_IpsecSaAhInReplayErrors_Type = Counter32
_IpsecSaAhInReplayErrors_Object = MibTableColumn
ipsecSaAhInReplayErrors = _IpsecSaAhInReplayErrors_Object(
    (1, 3, 6, 1, 3, 98, 1, 1, 2, 1, 22),
    _IpsecSaAhInReplayErrors_Type()
)
ipsecSaAhInReplayErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecSaAhInReplayErrors.setStatus("current")
_IpsecSaAhInPolicyErrors_Type = Counter32
_IpsecSaAhInPolicyErrors_Object = MibTableColumn
ipsecSaAhInPolicyErrors = _IpsecSaAhInPolicyErrors_Object(
    (1, 3, 6, 1, 3, 98, 1, 1, 2, 1, 23),
    _IpsecSaAhInPolicyErrors_Type()
)
ipsecSaAhInPolicyErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecSaAhInPolicyErrors.setStatus("current")
_IpsecSaAhInOtherReceiveErrors_Type = Counter32
_IpsecSaAhInOtherReceiveErrors_Object = MibTableColumn
ipsecSaAhInOtherReceiveErrors = _IpsecSaAhInOtherReceiveErrors_Object(
    (1, 3, 6, 1, 3, 98, 1, 1, 2, 1, 24),
    _IpsecSaAhInOtherReceiveErrors_Type()
)
ipsecSaAhInOtherReceiveErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecSaAhInOtherReceiveErrors.setStatus("current")
_IpsecSaIpcompInTable_Object = MibTable
ipsecSaIpcompInTable = _IpsecSaIpcompInTable_Object(
    (1, 3, 6, 1, 3, 98, 1, 1, 3)
)
if mibBuilder.loadTexts:
    ipsecSaIpcompInTable.setStatus("current")
_IpsecSaIpcompInEntry_Object = MibTableRow
ipsecSaIpcompInEntry = _IpsecSaIpcompInEntry_Object(
    (1, 3, 6, 1, 3, 98, 1, 1, 3, 1)
)
ipsecSaIpcompInEntry.setIndexNames(
    (0, "IPSEC-SA-MON-MIB", "ipsecSaIpcompInAddress"),
    (0, "IPSEC-SA-MON-MIB", "ipsecSaIpcompInCpi"),
)
if mibBuilder.loadTexts:
    ipsecSaIpcompInEntry.setStatus("current")
_IpsecSaIpcompInAddress_Type = IpsecIpv6Address
_IpsecSaIpcompInAddress_Object = MibTableColumn
ipsecSaIpcompInAddress = _IpsecSaIpcompInAddress_Object(
    (1, 3, 6, 1, 3, 98, 1, 1, 3, 1, 1),
    _IpsecSaIpcompInAddress_Type()
)
ipsecSaIpcompInAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecSaIpcompInAddress.setStatus("current")
_IpsecSaIpcompInCpi_Type = IpsecDoiIpcompTransform
_IpsecSaIpcompInCpi_Object = MibTableColumn
ipsecSaIpcompInCpi = _IpsecSaIpcompInCpi_Object(
    (1, 3, 6, 1, 3, 98, 1, 1, 3, 1, 2),
    _IpsecSaIpcompInCpi_Type()
)
ipsecSaIpcompInCpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecSaIpcompInCpi.setStatus("current")
_IpsecSaIpcompInDestId_Type = IpsecRawId
_IpsecSaIpcompInDestId_Object = MibTableColumn
ipsecSaIpcompInDestId = _IpsecSaIpcompInDestId_Object(
    (1, 3, 6, 1, 3, 98, 1, 1, 3, 1, 3),
    _IpsecSaIpcompInDestId_Type()
)
ipsecSaIpcompInDestId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecSaIpcompInDestId.setStatus("current")
_IpsecSaIpcompInDestIdType_Type = IpsecDoiIdentType
_IpsecSaIpcompInDestIdType_Object = MibTableColumn
ipsecSaIpcompInDestIdType = _IpsecSaIpcompInDestIdType_Object(
    (1, 3, 6, 1, 3, 98, 1, 1, 3, 1, 4),
    _IpsecSaIpcompInDestIdType_Type()
)
ipsecSaIpcompInDestIdType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecSaIpcompInDestIdType.setStatus("current")
_IpsecSaIpcompInSourceId_Type = IpsecRawId
_IpsecSaIpcompInSourceId_Object = MibTableColumn
ipsecSaIpcompInSourceId = _IpsecSaIpcompInSourceId_Object(
    (1, 3, 6, 1, 3, 98, 1, 1, 3, 1, 5),
    _IpsecSaIpcompInSourceId_Type()
)
ipsecSaIpcompInSourceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecSaIpcompInSourceId.setStatus("current")
_IpsecSaIpcompInSourceIdType_Type = IpsecDoiIdentType
_IpsecSaIpcompInSourceIdType_Object = MibTableColumn
ipsecSaIpcompInSourceIdType = _IpsecSaIpcompInSourceIdType_Object(
    (1, 3, 6, 1, 3, 98, 1, 1, 3, 1, 6),
    _IpsecSaIpcompInSourceIdType_Type()
)
ipsecSaIpcompInSourceIdType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecSaIpcompInSourceIdType.setStatus("current")


class _IpsecSaIpcompInProtocol_Type(Integer32):
    """Custom type ipsecSaIpcompInProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_IpsecSaIpcompInProtocol_Type.__name__ = "Integer32"
_IpsecSaIpcompInProtocol_Object = MibTableColumn
ipsecSaIpcompInProtocol = _IpsecSaIpcompInProtocol_Object(
    (1, 3, 6, 1, 3, 98, 1, 1, 3, 1, 7),
    _IpsecSaIpcompInProtocol_Type()
)
ipsecSaIpcompInProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecSaIpcompInProtocol.setStatus("current")


class _IpsecSaIpcompInDestPort_Type(Integer32):
    """Custom type ipsecSaIpcompInDestPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_IpsecSaIpcompInDestPort_Type.__name__ = "Integer32"
_IpsecSaIpcompInDestPort_Object = MibTableColumn
ipsecSaIpcompInDestPort = _IpsecSaIpcompInDestPort_Object(
    (1, 3, 6, 1, 3, 98, 1, 1, 3, 1, 8),
    _IpsecSaIpcompInDestPort_Type()
)
ipsecSaIpcompInDestPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecSaIpcompInDestPort.setStatus("current")


class _IpsecSaIpcompInSourcePort_Type(Integer32):
    """Custom type ipsecSaIpcompInSourcePort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_IpsecSaIpcompInSourcePort_Type.__name__ = "Integer32"
_IpsecSaIpcompInSourcePort_Object = MibTableColumn
ipsecSaIpcompInSourcePort = _IpsecSaIpcompInSourcePort_Object(
    (1, 3, 6, 1, 3, 98, 1, 1, 3, 1, 9),
    _IpsecSaIpcompInSourcePort_Type()
)
ipsecSaIpcompInSourcePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecSaIpcompInSourcePort.setStatus("current")
_IpsecSaIpcompInCreator_Type = IpsecSaCreatorIdent
_IpsecSaIpcompInCreator_Object = MibTableColumn
ipsecSaIpcompInCreator = _IpsecSaIpcompInCreator_Object(
    (1, 3, 6, 1, 3, 98, 1, 1, 3, 1, 10),
    _IpsecSaIpcompInCreator_Type()
)
ipsecSaIpcompInCreator.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecSaIpcompInCreator.setStatus("current")
_IpsecSaIpcompInEncapsulation_Type = IpsecDoiEncapsulationMode
_IpsecSaIpcompInEncapsulation_Object = MibTableColumn
ipsecSaIpcompInEncapsulation = _IpsecSaIpcompInEncapsulation_Object(
    (1, 3, 6, 1, 3, 98, 1, 1, 3, 1, 11),
    _IpsecSaIpcompInEncapsulation_Type()
)
ipsecSaIpcompInEncapsulation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecSaIpcompInEncapsulation.setStatus("current")
_IpsecSaIpcompInDecompAlg_Type = IpsecDoiIpcompTransform
_IpsecSaIpcompInDecompAlg_Object = MibTableColumn
ipsecSaIpcompInDecompAlg = _IpsecSaIpcompInDecompAlg_Object(
    (1, 3, 6, 1, 3, 98, 1, 1, 3, 1, 12),
    _IpsecSaIpcompInDecompAlg_Type()
)
ipsecSaIpcompInDecompAlg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecSaIpcompInDecompAlg.setStatus("current")
_IpsecSaIpcompInSeconds_Type = Counter32
_IpsecSaIpcompInSeconds_Object = MibTableColumn
ipsecSaIpcompInSeconds = _IpsecSaIpcompInSeconds_Object(
    (1, 3, 6, 1, 3, 98, 1, 1, 3, 1, 13),
    _IpsecSaIpcompInSeconds_Type()
)
ipsecSaIpcompInSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecSaIpcompInSeconds.setStatus("current")
if mibBuilder.loadTexts:
    ipsecSaIpcompInSeconds.setUnits("seconds")
_IpsecSaIpcompInUserOctets_Type = Counter64
_IpsecSaIpcompInUserOctets_Object = MibTableColumn
ipsecSaIpcompInUserOctets = _IpsecSaIpcompInUserOctets_Object(
    (1, 3, 6, 1, 3, 98, 1, 1, 3, 1, 14),
    _IpsecSaIpcompInUserOctets_Type()
)
ipsecSaIpcompInUserOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecSaIpcompInUserOctets.setStatus("current")
if mibBuilder.loadTexts:
    ipsecSaIpcompInUserOctets.setUnits("bytes")
_IpsecSaIpcompInPackets_Type = Counter64
_IpsecSaIpcompInPackets_Object = MibTableColumn
ipsecSaIpcompInPackets = _IpsecSaIpcompInPackets_Object(
    (1, 3, 6, 1, 3, 98, 1, 1, 3, 1, 15),
    _IpsecSaIpcompInPackets_Type()
)
ipsecSaIpcompInPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecSaIpcompInPackets.setStatus("current")
_IpsecSaIpcompInDecompErrors_Type = Counter32
_IpsecSaIpcompInDecompErrors_Object = MibTableColumn
ipsecSaIpcompInDecompErrors = _IpsecSaIpcompInDecompErrors_Object(
    (1, 3, 6, 1, 3, 98, 1, 1, 3, 1, 16),
    _IpsecSaIpcompInDecompErrors_Type()
)
ipsecSaIpcompInDecompErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecSaIpcompInDecompErrors.setStatus("current")
_IpsecSaIpcompInOtherReceiveErrors_Type = Counter32
_IpsecSaIpcompInOtherReceiveErrors_Object = MibTableColumn
ipsecSaIpcompInOtherReceiveErrors = _IpsecSaIpcompInOtherReceiveErrors_Object(
    (1, 3, 6, 1, 3, 98, 1, 1, 3, 1, 17),
    _IpsecSaIpcompInOtherReceiveErrors_Type()
)
ipsecSaIpcompInOtherReceiveErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecSaIpcompInOtherReceiveErrors.setStatus("current")
_IpsecSaEspOutTable_Object = MibTable
ipsecSaEspOutTable = _IpsecSaEspOutTable_Object(
    (1, 3, 6, 1, 3, 98, 1, 1, 4)
)
if mibBuilder.loadTexts:
    ipsecSaEspOutTable.setStatus("current")
_IpsecSaEspOutEntry_Object = MibTableRow
ipsecSaEspOutEntry = _IpsecSaEspOutEntry_Object(
    (1, 3, 6, 1, 3, 98, 1, 1, 4, 1)
)
ipsecSaEspOutEntry.setIndexNames(
    (0, "IPSEC-SA-MON-MIB", "ipsecSaEspOutAddress"),
    (0, "IPSEC-SA-MON-MIB", "ipsecSaEspOutSpi"),
)
if mibBuilder.loadTexts:
    ipsecSaEspOutEntry.setStatus("current")
_IpsecSaEspOutAddress_Type = IpsecIpv6Address
_IpsecSaEspOutAddress_Object = MibTableColumn
ipsecSaEspOutAddress = _IpsecSaEspOutAddress_Object(
    (1, 3, 6, 1, 3, 98, 1, 1, 4, 1, 1),
    _IpsecSaEspOutAddress_Type()
)
ipsecSaEspOutAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecSaEspOutAddress.setStatus("current")
_IpsecSaEspOutSpi_Type = Unsigned32
_IpsecSaEspOutSpi_Object = MibTableColumn
ipsecSaEspOutSpi = _IpsecSaEspOutSpi_Object(
    (1, 3, 6, 1, 3, 98, 1, 1, 4, 1, 2),
    _IpsecSaEspOutSpi_Type()
)
ipsecSaEspOutSpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecSaEspOutSpi.setStatus("current")
_IpsecSaEspOutSourceId_Type = IpsecRawId
_IpsecSaEspOutSourceId_Object = MibTableColumn
ipsecSaEspOutSourceId = _IpsecSaEspOutSourceId_Object(
    (1, 3, 6, 1, 3, 98, 1, 1, 4, 1, 3),
    _IpsecSaEspOutSourceId_Type()
)
ipsecSaEspOutSourceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecSaEspOutSourceId.setStatus("current")
_IpsecSaEspOutSourceIdType_Type = IpsecDoiIdentType
_IpsecSaEspOutSourceIdType_Object = MibTableColumn
ipsecSaEspOutSourceIdType = _IpsecSaEspOutSourceIdType_Object(
    (1, 3, 6, 1, 3, 98, 1, 1, 4, 1, 4),
    _IpsecSaEspOutSourceIdType_Type()
)
ipsecSaEspOutSourceIdType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecSaEspOutSourceIdType.setStatus("current")
_IpsecSaEspOutDestId_Type = IpsecRawId
_IpsecSaEspOutDestId_Object = MibTableColumn
ipsecSaEspOutDestId = _IpsecSaEspOutDestId_Object(
    (1, 3, 6, 1, 3, 98, 1, 1, 4, 1, 5),
    _IpsecSaEspOutDestId_Type()
)
ipsecSaEspOutDestId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecSaEspOutDestId.setStatus("current")
_IpsecSaEspOutDestIdType_Type = IpsecDoiIdentType
_IpsecSaEspOutDestIdType_Object = MibTableColumn
ipsecSaEspOutDestIdType = _IpsecSaEspOutDestIdType_Object(
    (1, 3, 6, 1, 3, 98, 1, 1, 4, 1, 6),
    _IpsecSaEspOutDestIdType_Type()
)
ipsecSaEspOutDestIdType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecSaEspOutDestIdType.setStatus("current")


class _IpsecSaEspOutProtocol_Type(Integer32):
    """Custom type ipsecSaEspOutProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_IpsecSaEspOutProtocol_Type.__name__ = "Integer32"
_IpsecSaEspOutProtocol_Object = MibTableColumn
ipsecSaEspOutProtocol = _IpsecSaEspOutProtocol_Object(
    (1, 3, 6, 1, 3, 98, 1, 1, 4, 1, 7),
    _IpsecSaEspOutProtocol_Type()
)
ipsecSaEspOutProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecSaEspOutProtocol.setStatus("current")


class _IpsecSaEspOutSourcePort_Type(Integer32):
    """Custom type ipsecSaEspOutSourcePort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_IpsecSaEspOutSourcePort_Type.__name__ = "Integer32"
_IpsecSaEspOutSourcePort_Object = MibTableColumn
ipsecSaEspOutSourcePort = _IpsecSaEspOutSourcePort_Object(
    (1, 3, 6, 1, 3, 98, 1, 1, 4, 1, 8),
    _IpsecSaEspOutSourcePort_Type()
)
ipsecSaEspOutSourcePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecSaEspOutSourcePort.setStatus("current")


class _IpsecSaEspOutDestPort_Type(Integer32):
    """Custom type ipsecSaEspOutDestPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_IpsecSaEspOutDestPort_Type.__name__ = "Integer32"
_IpsecSaEspOutDestPort_Object = MibTableColumn
ipsecSaEspOutDestPort = _IpsecSaEspOutDestPort_Object(
    (1, 3, 6, 1, 3, 98, 1, 1, 4, 1, 9),
    _IpsecSaEspOutDestPort_Type()
)
ipsecSaEspOutDestPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecSaEspOutDestPort.setStatus("current")
_IpsecSaEspOutCreator_Type = IpsecSaCreatorIdent
_IpsecSaEspOutCreator_Object = MibTableColumn
ipsecSaEspOutCreator = _IpsecSaEspOutCreator_Object(
    (1, 3, 6, 1, 3, 98, 1, 1, 4, 1, 10),
    _IpsecSaEspOutCreator_Type()
)
ipsecSaEspOutCreator.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecSaEspOutCreator.setStatus("current")
_IpsecSaEspOutEncapsulation_Type = IpsecDoiEncapsulationMode
_IpsecSaEspOutEncapsulation_Object = MibTableColumn
ipsecSaEspOutEncapsulation = _IpsecSaEspOutEncapsulation_Object(
    (1, 3, 6, 1, 3, 98, 1, 1, 4, 1, 11),
    _IpsecSaEspOutEncapsulation_Type()
)
ipsecSaEspOutEncapsulation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecSaEspOutEncapsulation.setStatus("current")
_IpsecSaEspOutEncAlg_Type = IpsecDoiEspTransform
_IpsecSaEspOutEncAlg_Object = MibTableColumn
ipsecSaEspOutEncAlg = _IpsecSaEspOutEncAlg_Object(
    (1, 3, 6, 1, 3, 98, 1, 1, 4, 1, 12),
    _IpsecSaEspOutEncAlg_Type()
)
ipsecSaEspOutEncAlg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecSaEspOutEncAlg.setStatus("current")


class _IpsecSaEspOutEncKeyLength_Type(Unsigned32):
    """Custom type ipsecSaEspOutEncKeyLength based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65531),
    )


_IpsecSaEspOutEncKeyLength_Type.__name__ = "Unsigned32"
_IpsecSaEspOutEncKeyLength_Object = MibTableColumn
ipsecSaEspOutEncKeyLength = _IpsecSaEspOutEncKeyLength_Object(
    (1, 3, 6, 1, 3, 98, 1, 1, 4, 1, 13),
    _IpsecSaEspOutEncKeyLength_Type()
)
ipsecSaEspOutEncKeyLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecSaEspOutEncKeyLength.setStatus("current")
if mibBuilder.loadTexts:
    ipsecSaEspOutEncKeyLength.setUnits("bits")
_IpsecSaEspOutAuthAlg_Type = IpsecDoiAuthAlgorithm
_IpsecSaEspOutAuthAlg_Object = MibTableColumn
ipsecSaEspOutAuthAlg = _IpsecSaEspOutAuthAlg_Object(
    (1, 3, 6, 1, 3, 98, 1, 1, 4, 1, 14),
    _IpsecSaEspOutAuthAlg_Type()
)
ipsecSaEspOutAuthAlg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecSaEspOutAuthAlg.setStatus("current")


class _IpsecSaEspOutAuthKeyLength_Type(Unsigned32):
    """Custom type ipsecSaEspOutAuthKeyLength based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65531),
    )


_IpsecSaEspOutAuthKeyLength_Type.__name__ = "Unsigned32"
_IpsecSaEspOutAuthKeyLength_Object = MibTableColumn
ipsecSaEspOutAuthKeyLength = _IpsecSaEspOutAuthKeyLength_Object(
    (1, 3, 6, 1, 3, 98, 1, 1, 4, 1, 15),
    _IpsecSaEspOutAuthKeyLength_Type()
)
ipsecSaEspOutAuthKeyLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecSaEspOutAuthKeyLength.setStatus("current")
if mibBuilder.loadTexts:
    ipsecSaEspOutAuthKeyLength.setUnits("bits")
_IpsecSaEspOutLimitSeconds_Type = Unsigned32
_IpsecSaEspOutLimitSeconds_Object = MibTableColumn
ipsecSaEspOutLimitSeconds = _IpsecSaEspOutLimitSeconds_Object(
    (1, 3, 6, 1, 3, 98, 1, 1, 4, 1, 16),
    _IpsecSaEspOutLimitSeconds_Type()
)
ipsecSaEspOutLimitSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecSaEspOutLimitSeconds.setStatus("current")
if mibBuilder.loadTexts:
    ipsecSaEspOutLimitSeconds.setUnits("seconds")
_IpsecSaEspOutLimitKbytes_Type = Unsigned32
_IpsecSaEspOutLimitKbytes_Object = MibTableColumn
ipsecSaEspOutLimitKbytes = _IpsecSaEspOutLimitKbytes_Object(
    (1, 3, 6, 1, 3, 98, 1, 1, 4, 1, 17),
    _IpsecSaEspOutLimitKbytes_Type()
)
ipsecSaEspOutLimitKbytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecSaEspOutLimitKbytes.setStatus("current")
if mibBuilder.loadTexts:
    ipsecSaEspOutLimitKbytes.setUnits("kilobytes")
_IpsecSaEspOutAccSeconds_Type = Counter32
_IpsecSaEspOutAccSeconds_Object = MibTableColumn
ipsecSaEspOutAccSeconds = _IpsecSaEspOutAccSeconds_Object(
    (1, 3, 6, 1, 3, 98, 1, 1, 4, 1, 18),
    _IpsecSaEspOutAccSeconds_Type()
)
ipsecSaEspOutAccSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecSaEspOutAccSeconds.setStatus("current")
if mibBuilder.loadTexts:
    ipsecSaEspOutAccSeconds.setUnits("seconds")
_IpsecSaEspOutAccKbytes_Type = Counter32
_IpsecSaEspOutAccKbytes_Object = MibTableColumn
ipsecSaEspOutAccKbytes = _IpsecSaEspOutAccKbytes_Object(
    (1, 3, 6, 1, 3, 98, 1, 1, 4, 1, 19),
    _IpsecSaEspOutAccKbytes_Type()
)
ipsecSaEspOutAccKbytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecSaEspOutAccKbytes.setStatus("current")
if mibBuilder.loadTexts:
    ipsecSaEspOutAccKbytes.setUnits("kilobytes")
_IpsecSaEspOutUserOctets_Type = Counter64
_IpsecSaEspOutUserOctets_Object = MibTableColumn
ipsecSaEspOutUserOctets = _IpsecSaEspOutUserOctets_Object(
    (1, 3, 6, 1, 3, 98, 1, 1, 4, 1, 20),
    _IpsecSaEspOutUserOctets_Type()
)
ipsecSaEspOutUserOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecSaEspOutUserOctets.setStatus("current")
if mibBuilder.loadTexts:
    ipsecSaEspOutUserOctets.setUnits("bytes")
_IpsecSaEspOutPackets_Type = Counter64
_IpsecSaEspOutPackets_Object = MibTableColumn
ipsecSaEspOutPackets = _IpsecSaEspOutPackets_Object(
    (1, 3, 6, 1, 3, 98, 1, 1, 4, 1, 21),
    _IpsecSaEspOutPackets_Type()
)
ipsecSaEspOutPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecSaEspOutPackets.setStatus("current")
_IpsecSaEspOutSendErrors_Type = Counter32
_IpsecSaEspOutSendErrors_Object = MibTableColumn
ipsecSaEspOutSendErrors = _IpsecSaEspOutSendErrors_Object(
    (1, 3, 6, 1, 3, 98, 1, 1, 4, 1, 22),
    _IpsecSaEspOutSendErrors_Type()
)
ipsecSaEspOutSendErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecSaEspOutSendErrors.setStatus("current")
_IpsecSaAhOutTable_Object = MibTable
ipsecSaAhOutTable = _IpsecSaAhOutTable_Object(
    (1, 3, 6, 1, 3, 98, 1, 1, 5)
)
if mibBuilder.loadTexts:
    ipsecSaAhOutTable.setStatus("current")
_IpsecSaAhOutEntry_Object = MibTableRow
ipsecSaAhOutEntry = _IpsecSaAhOutEntry_Object(
    (1, 3, 6, 1, 3, 98, 1, 1, 5, 1)
)
ipsecSaAhOutEntry.setIndexNames(
    (0, "IPSEC-SA-MON-MIB", "ipsecSaAhOutAddress"),
    (0, "IPSEC-SA-MON-MIB", "ipsecSaAhOutSpi"),
)
if mibBuilder.loadTexts:
    ipsecSaAhOutEntry.setStatus("current")
_IpsecSaAhOutAddress_Type = IpsecIpv6Address
_IpsecSaAhOutAddress_Object = MibTableColumn
ipsecSaAhOutAddress = _IpsecSaAhOutAddress_Object(
    (1, 3, 6, 1, 3, 98, 1, 1, 5, 1, 1),
    _IpsecSaAhOutAddress_Type()
)
ipsecSaAhOutAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecSaAhOutAddress.setStatus("current")
_IpsecSaAhOutSpi_Type = Unsigned32
_IpsecSaAhOutSpi_Object = MibTableColumn
ipsecSaAhOutSpi = _IpsecSaAhOutSpi_Object(
    (1, 3, 6, 1, 3, 98, 1, 1, 5, 1, 2),
    _IpsecSaAhOutSpi_Type()
)
ipsecSaAhOutSpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecSaAhOutSpi.setStatus("current")
_IpsecSaAhOutSourceId_Type = IpsecRawId
_IpsecSaAhOutSourceId_Object = MibTableColumn
ipsecSaAhOutSourceId = _IpsecSaAhOutSourceId_Object(
    (1, 3, 6, 1, 3, 98, 1, 1, 5, 1, 3),
    _IpsecSaAhOutSourceId_Type()
)
ipsecSaAhOutSourceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecSaAhOutSourceId.setStatus("current")
_IpsecSaAhOutSourceIdType_Type = IpsecDoiIdentType
_IpsecSaAhOutSourceIdType_Object = MibTableColumn
ipsecSaAhOutSourceIdType = _IpsecSaAhOutSourceIdType_Object(
    (1, 3, 6, 1, 3, 98, 1, 1, 5, 1, 4),
    _IpsecSaAhOutSourceIdType_Type()
)
ipsecSaAhOutSourceIdType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecSaAhOutSourceIdType.setStatus("current")
_IpsecSaAhOutDestId_Type = IpsecRawId
_IpsecSaAhOutDestId_Object = MibTableColumn
ipsecSaAhOutDestId = _IpsecSaAhOutDestId_Object(
    (1, 3, 6, 1, 3, 98, 1, 1, 5, 1, 5),
    _IpsecSaAhOutDestId_Type()
)
ipsecSaAhOutDestId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecSaAhOutDestId.setStatus("current")
_IpsecSaAhOutDestIdType_Type = IpsecDoiIdentType
_IpsecSaAhOutDestIdType_Object = MibTableColumn
ipsecSaAhOutDestIdType = _IpsecSaAhOutDestIdType_Object(
    (1, 3, 6, 1, 3, 98, 1, 1, 5, 1, 6),
    _IpsecSaAhOutDestIdType_Type()
)
ipsecSaAhOutDestIdType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecSaAhOutDestIdType.setStatus("current")


class _IpsecSaAhOutProtocol_Type(Integer32):
    """Custom type ipsecSaAhOutProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_IpsecSaAhOutProtocol_Type.__name__ = "Integer32"
_IpsecSaAhOutProtocol_Object = MibTableColumn
ipsecSaAhOutProtocol = _IpsecSaAhOutProtocol_Object(
    (1, 3, 6, 1, 3, 98, 1, 1, 5, 1, 7),
    _IpsecSaAhOutProtocol_Type()
)
ipsecSaAhOutProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecSaAhOutProtocol.setStatus("current")


class _IpsecSaAhOutSourcePort_Type(Integer32):
    """Custom type ipsecSaAhOutSourcePort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_IpsecSaAhOutSourcePort_Type.__name__ = "Integer32"
_IpsecSaAhOutSourcePort_Object = MibTableColumn
ipsecSaAhOutSourcePort = _IpsecSaAhOutSourcePort_Object(
    (1, 3, 6, 1, 3, 98, 1, 1, 5, 1, 8),
    _IpsecSaAhOutSourcePort_Type()
)
ipsecSaAhOutSourcePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecSaAhOutSourcePort.setStatus("current")


class _IpsecSaAhOutDestPort_Type(Integer32):
    """Custom type ipsecSaAhOutDestPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_IpsecSaAhOutDestPort_Type.__name__ = "Integer32"
_IpsecSaAhOutDestPort_Object = MibTableColumn
ipsecSaAhOutDestPort = _IpsecSaAhOutDestPort_Object(
    (1, 3, 6, 1, 3, 98, 1, 1, 5, 1, 9),
    _IpsecSaAhOutDestPort_Type()
)
ipsecSaAhOutDestPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecSaAhOutDestPort.setStatus("current")
_IpsecSaAhOutCreator_Type = IpsecSaCreatorIdent
_IpsecSaAhOutCreator_Object = MibTableColumn
ipsecSaAhOutCreator = _IpsecSaAhOutCreator_Object(
    (1, 3, 6, 1, 3, 98, 1, 1, 5, 1, 10),
    _IpsecSaAhOutCreator_Type()
)
ipsecSaAhOutCreator.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecSaAhOutCreator.setStatus("current")
_IpsecSaAhOutEncapsulation_Type = IpsecDoiEncapsulationMode
_IpsecSaAhOutEncapsulation_Object = MibTableColumn
ipsecSaAhOutEncapsulation = _IpsecSaAhOutEncapsulation_Object(
    (1, 3, 6, 1, 3, 98, 1, 1, 5, 1, 11),
    _IpsecSaAhOutEncapsulation_Type()
)
ipsecSaAhOutEncapsulation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecSaAhOutEncapsulation.setStatus("current")
_IpsecSaAhOutAuthAlg_Type = IpsecDoiAhTransform
_IpsecSaAhOutAuthAlg_Object = MibTableColumn
ipsecSaAhOutAuthAlg = _IpsecSaAhOutAuthAlg_Object(
    (1, 3, 6, 1, 3, 98, 1, 1, 5, 1, 12),
    _IpsecSaAhOutAuthAlg_Type()
)
ipsecSaAhOutAuthAlg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecSaAhOutAuthAlg.setStatus("current")


class _IpsecSaAhOutAuthKeyLength_Type(Unsigned32):
    """Custom type ipsecSaAhOutAuthKeyLength based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65531),
    )


_IpsecSaAhOutAuthKeyLength_Type.__name__ = "Unsigned32"
_IpsecSaAhOutAuthKeyLength_Object = MibTableColumn
ipsecSaAhOutAuthKeyLength = _IpsecSaAhOutAuthKeyLength_Object(
    (1, 3, 6, 1, 3, 98, 1, 1, 5, 1, 13),
    _IpsecSaAhOutAuthKeyLength_Type()
)
ipsecSaAhOutAuthKeyLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecSaAhOutAuthKeyLength.setStatus("current")
if mibBuilder.loadTexts:
    ipsecSaAhOutAuthKeyLength.setUnits("bits")
_IpsecSaAhOutLimitSeconds_Type = Unsigned32
_IpsecSaAhOutLimitSeconds_Object = MibTableColumn
ipsecSaAhOutLimitSeconds = _IpsecSaAhOutLimitSeconds_Object(
    (1, 3, 6, 1, 3, 98, 1, 1, 5, 1, 14),
    _IpsecSaAhOutLimitSeconds_Type()
)
ipsecSaAhOutLimitSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecSaAhOutLimitSeconds.setStatus("current")
if mibBuilder.loadTexts:
    ipsecSaAhOutLimitSeconds.setUnits("seconds")
_IpsecSaAhOutLimitKbytes_Type = Unsigned32
_IpsecSaAhOutLimitKbytes_Object = MibTableColumn
ipsecSaAhOutLimitKbytes = _IpsecSaAhOutLimitKbytes_Object(
    (1, 3, 6, 1, 3, 98, 1, 1, 5, 1, 15),
    _IpsecSaAhOutLimitKbytes_Type()
)
ipsecSaAhOutLimitKbytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecSaAhOutLimitKbytes.setStatus("current")
if mibBuilder.loadTexts:
    ipsecSaAhOutLimitKbytes.setUnits("kilobytes")
_IpsecSaAhOutAccSeconds_Type = Counter32
_IpsecSaAhOutAccSeconds_Object = MibTableColumn
ipsecSaAhOutAccSeconds = _IpsecSaAhOutAccSeconds_Object(
    (1, 3, 6, 1, 3, 98, 1, 1, 5, 1, 16),
    _IpsecSaAhOutAccSeconds_Type()
)
ipsecSaAhOutAccSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecSaAhOutAccSeconds.setStatus("current")
if mibBuilder.loadTexts:
    ipsecSaAhOutAccSeconds.setUnits("seconds")
_IpsecSaAhOutAccKbytes_Type = Counter32
_IpsecSaAhOutAccKbytes_Object = MibTableColumn
ipsecSaAhOutAccKbytes = _IpsecSaAhOutAccKbytes_Object(
    (1, 3, 6, 1, 3, 98, 1, 1, 5, 1, 17),
    _IpsecSaAhOutAccKbytes_Type()
)
ipsecSaAhOutAccKbytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecSaAhOutAccKbytes.setStatus("current")
if mibBuilder.loadTexts:
    ipsecSaAhOutAccKbytes.setUnits("kilobytes")
_IpsecSaAhOutUserOctets_Type = Counter64
_IpsecSaAhOutUserOctets_Object = MibTableColumn
ipsecSaAhOutUserOctets = _IpsecSaAhOutUserOctets_Object(
    (1, 3, 6, 1, 3, 98, 1, 1, 5, 1, 18),
    _IpsecSaAhOutUserOctets_Type()
)
ipsecSaAhOutUserOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecSaAhOutUserOctets.setStatus("current")
if mibBuilder.loadTexts:
    ipsecSaAhOutUserOctets.setUnits("bytes")
_IpsecSaAhOutPackets_Type = Counter64
_IpsecSaAhOutPackets_Object = MibTableColumn
ipsecSaAhOutPackets = _IpsecSaAhOutPackets_Object(
    (1, 3, 6, 1, 3, 98, 1, 1, 5, 1, 19),
    _IpsecSaAhOutPackets_Type()
)
ipsecSaAhOutPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecSaAhOutPackets.setStatus("current")
_IpsecSaAhOutSendErrors_Type = Counter32
_IpsecSaAhOutSendErrors_Object = MibTableColumn
ipsecSaAhOutSendErrors = _IpsecSaAhOutSendErrors_Object(
    (1, 3, 6, 1, 3, 98, 1, 1, 5, 1, 20),
    _IpsecSaAhOutSendErrors_Type()
)
ipsecSaAhOutSendErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecSaAhOutSendErrors.setStatus("current")
_IpsecSaIpcompOutTable_Object = MibTable
ipsecSaIpcompOutTable = _IpsecSaIpcompOutTable_Object(
    (1, 3, 6, 1, 3, 98, 1, 1, 6)
)
if mibBuilder.loadTexts:
    ipsecSaIpcompOutTable.setStatus("current")
_IpsecSaIpcompOutEntry_Object = MibTableRow
ipsecSaIpcompOutEntry = _IpsecSaIpcompOutEntry_Object(
    (1, 3, 6, 1, 3, 98, 1, 1, 6, 1)
)
ipsecSaIpcompOutEntry.setIndexNames(
    (0, "IPSEC-SA-MON-MIB", "ipsecSaIpcompOutAddress"),
    (0, "IPSEC-SA-MON-MIB", "ipsecSaIpcompOutCpi"),
)
if mibBuilder.loadTexts:
    ipsecSaIpcompOutEntry.setStatus("current")
_IpsecSaIpcompOutAddress_Type = IpsecIpv6Address
_IpsecSaIpcompOutAddress_Object = MibTableColumn
ipsecSaIpcompOutAddress = _IpsecSaIpcompOutAddress_Object(
    (1, 3, 6, 1, 3, 98, 1, 1, 6, 1, 1),
    _IpsecSaIpcompOutAddress_Type()
)
ipsecSaIpcompOutAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecSaIpcompOutAddress.setStatus("current")
_IpsecSaIpcompOutCpi_Type = IpsecDoiIpcompTransform
_IpsecSaIpcompOutCpi_Object = MibTableColumn
ipsecSaIpcompOutCpi = _IpsecSaIpcompOutCpi_Object(
    (1, 3, 6, 1, 3, 98, 1, 1, 6, 1, 2),
    _IpsecSaIpcompOutCpi_Type()
)
ipsecSaIpcompOutCpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecSaIpcompOutCpi.setStatus("current")
_IpsecSaIpcompOutSourceId_Type = IpsecRawId
_IpsecSaIpcompOutSourceId_Object = MibTableColumn
ipsecSaIpcompOutSourceId = _IpsecSaIpcompOutSourceId_Object(
    (1, 3, 6, 1, 3, 98, 1, 1, 6, 1, 3),
    _IpsecSaIpcompOutSourceId_Type()
)
ipsecSaIpcompOutSourceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecSaIpcompOutSourceId.setStatus("current")
_IpsecSaIpcompOutSourceIdType_Type = IpsecDoiIdentType
_IpsecSaIpcompOutSourceIdType_Object = MibTableColumn
ipsecSaIpcompOutSourceIdType = _IpsecSaIpcompOutSourceIdType_Object(
    (1, 3, 6, 1, 3, 98, 1, 1, 6, 1, 4),
    _IpsecSaIpcompOutSourceIdType_Type()
)
ipsecSaIpcompOutSourceIdType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecSaIpcompOutSourceIdType.setStatus("current")
_IpsecSaIpcompOutDestId_Type = IpsecRawId
_IpsecSaIpcompOutDestId_Object = MibTableColumn
ipsecSaIpcompOutDestId = _IpsecSaIpcompOutDestId_Object(
    (1, 3, 6, 1, 3, 98, 1, 1, 6, 1, 5),
    _IpsecSaIpcompOutDestId_Type()
)
ipsecSaIpcompOutDestId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecSaIpcompOutDestId.setStatus("current")
_IpsecSaIpcompOutDestIdType_Type = IpsecDoiIdentType
_IpsecSaIpcompOutDestIdType_Object = MibTableColumn
ipsecSaIpcompOutDestIdType = _IpsecSaIpcompOutDestIdType_Object(
    (1, 3, 6, 1, 3, 98, 1, 1, 6, 1, 6),
    _IpsecSaIpcompOutDestIdType_Type()
)
ipsecSaIpcompOutDestIdType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecSaIpcompOutDestIdType.setStatus("current")


class _IpsecSaIpcompOutProtocol_Type(Integer32):
    """Custom type ipsecSaIpcompOutProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_IpsecSaIpcompOutProtocol_Type.__name__ = "Integer32"
_IpsecSaIpcompOutProtocol_Object = MibTableColumn
ipsecSaIpcompOutProtocol = _IpsecSaIpcompOutProtocol_Object(
    (1, 3, 6, 1, 3, 98, 1, 1, 6, 1, 7),
    _IpsecSaIpcompOutProtocol_Type()
)
ipsecSaIpcompOutProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecSaIpcompOutProtocol.setStatus("current")


class _IpsecSaIpcompOutSourcePort_Type(Integer32):
    """Custom type ipsecSaIpcompOutSourcePort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_IpsecSaIpcompOutSourcePort_Type.__name__ = "Integer32"
_IpsecSaIpcompOutSourcePort_Object = MibTableColumn
ipsecSaIpcompOutSourcePort = _IpsecSaIpcompOutSourcePort_Object(
    (1, 3, 6, 1, 3, 98, 1, 1, 6, 1, 8),
    _IpsecSaIpcompOutSourcePort_Type()
)
ipsecSaIpcompOutSourcePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecSaIpcompOutSourcePort.setStatus("current")


class _IpsecSaIpcompOutDestPort_Type(Integer32):
    """Custom type ipsecSaIpcompOutDestPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_IpsecSaIpcompOutDestPort_Type.__name__ = "Integer32"
_IpsecSaIpcompOutDestPort_Object = MibTableColumn
ipsecSaIpcompOutDestPort = _IpsecSaIpcompOutDestPort_Object(
    (1, 3, 6, 1, 3, 98, 1, 1, 6, 1, 9),
    _IpsecSaIpcompOutDestPort_Type()
)
ipsecSaIpcompOutDestPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecSaIpcompOutDestPort.setStatus("current")
_IpsecSaIpcompOutCreator_Type = IpsecSaCreatorIdent
_IpsecSaIpcompOutCreator_Object = MibTableColumn
ipsecSaIpcompOutCreator = _IpsecSaIpcompOutCreator_Object(
    (1, 3, 6, 1, 3, 98, 1, 1, 6, 1, 10),
    _IpsecSaIpcompOutCreator_Type()
)
ipsecSaIpcompOutCreator.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecSaIpcompOutCreator.setStatus("current")
_IpsecSaIpcompOutEncapsulation_Type = IpsecDoiEncapsulationMode
_IpsecSaIpcompOutEncapsulation_Object = MibTableColumn
ipsecSaIpcompOutEncapsulation = _IpsecSaIpcompOutEncapsulation_Object(
    (1, 3, 6, 1, 3, 98, 1, 1, 6, 1, 11),
    _IpsecSaIpcompOutEncapsulation_Type()
)
ipsecSaIpcompOutEncapsulation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecSaIpcompOutEncapsulation.setStatus("current")
_IpsecSaIpcompOutCompAlg_Type = IpsecDoiIpcompTransform
_IpsecSaIpcompOutCompAlg_Object = MibTableColumn
ipsecSaIpcompOutCompAlg = _IpsecSaIpcompOutCompAlg_Object(
    (1, 3, 6, 1, 3, 98, 1, 1, 6, 1, 12),
    _IpsecSaIpcompOutCompAlg_Type()
)
ipsecSaIpcompOutCompAlg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecSaIpcompOutCompAlg.setStatus("current")
_IpsecSaIpcompOutSeconds_Type = Counter32
_IpsecSaIpcompOutSeconds_Object = MibTableColumn
ipsecSaIpcompOutSeconds = _IpsecSaIpcompOutSeconds_Object(
    (1, 3, 6, 1, 3, 98, 1, 1, 6, 1, 13),
    _IpsecSaIpcompOutSeconds_Type()
)
ipsecSaIpcompOutSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecSaIpcompOutSeconds.setStatus("current")
if mibBuilder.loadTexts:
    ipsecSaIpcompOutSeconds.setUnits("seconds")
_IpsecSaIpcompOutUserOctets_Type = Counter64
_IpsecSaIpcompOutUserOctets_Object = MibTableColumn
ipsecSaIpcompOutUserOctets = _IpsecSaIpcompOutUserOctets_Object(
    (1, 3, 6, 1, 3, 98, 1, 1, 6, 1, 14),
    _IpsecSaIpcompOutUserOctets_Type()
)
ipsecSaIpcompOutUserOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecSaIpcompOutUserOctets.setStatus("current")
if mibBuilder.loadTexts:
    ipsecSaIpcompOutUserOctets.setUnits("bytes")
_IpsecSaIpcompOutOutputOctets_Type = Counter64
_IpsecSaIpcompOutOutputOctets_Object = MibTableColumn
ipsecSaIpcompOutOutputOctets = _IpsecSaIpcompOutOutputOctets_Object(
    (1, 3, 6, 1, 3, 98, 1, 1, 6, 1, 15),
    _IpsecSaIpcompOutOutputOctets_Type()
)
ipsecSaIpcompOutOutputOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecSaIpcompOutOutputOctets.setStatus("current")
if mibBuilder.loadTexts:
    ipsecSaIpcompOutOutputOctets.setUnits("bytes")
_IpsecSaIpcompOutPackets_Type = Counter64
_IpsecSaIpcompOutPackets_Object = MibTableColumn
ipsecSaIpcompOutPackets = _IpsecSaIpcompOutPackets_Object(
    (1, 3, 6, 1, 3, 98, 1, 1, 6, 1, 16),
    _IpsecSaIpcompOutPackets_Type()
)
ipsecSaIpcompOutPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecSaIpcompOutPackets.setStatus("current")
_SaStatistics_ObjectIdentity = ObjectIdentity
saStatistics = _SaStatistics_ObjectIdentity(
    (1, 3, 6, 1, 3, 98, 1, 2)
)
if mibBuilder.loadTexts:
    saStatistics.setStatus("current")
_IpsecEspCurrentInboundSAs_Type = Gauge32
_IpsecEspCurrentInboundSAs_Object = MibScalar
ipsecEspCurrentInboundSAs = _IpsecEspCurrentInboundSAs_Object(
    (1, 3, 6, 1, 3, 98, 1, 2, 1),
    _IpsecEspCurrentInboundSAs_Type()
)
ipsecEspCurrentInboundSAs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecEspCurrentInboundSAs.setStatus("current")
_IpsecEspTotalInboundSAs_Type = Counter32
_IpsecEspTotalInboundSAs_Object = MibScalar
ipsecEspTotalInboundSAs = _IpsecEspTotalInboundSAs_Object(
    (1, 3, 6, 1, 3, 98, 1, 2, 2),
    _IpsecEspTotalInboundSAs_Type()
)
ipsecEspTotalInboundSAs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecEspTotalInboundSAs.setStatus("current")
_IpsecEspCurrentOutboundSAs_Type = Gauge32
_IpsecEspCurrentOutboundSAs_Object = MibScalar
ipsecEspCurrentOutboundSAs = _IpsecEspCurrentOutboundSAs_Object(
    (1, 3, 6, 1, 3, 98, 1, 2, 3),
    _IpsecEspCurrentOutboundSAs_Type()
)
ipsecEspCurrentOutboundSAs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecEspCurrentOutboundSAs.setStatus("current")
_IpsecEspTotalOutboundSAs_Type = Counter32
_IpsecEspTotalOutboundSAs_Object = MibScalar
ipsecEspTotalOutboundSAs = _IpsecEspTotalOutboundSAs_Object(
    (1, 3, 6, 1, 3, 98, 1, 2, 4),
    _IpsecEspTotalOutboundSAs_Type()
)
ipsecEspTotalOutboundSAs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecEspTotalOutboundSAs.setStatus("current")
_IpsecAhCurrentInboundSAs_Type = Gauge32
_IpsecAhCurrentInboundSAs_Object = MibScalar
ipsecAhCurrentInboundSAs = _IpsecAhCurrentInboundSAs_Object(
    (1, 3, 6, 1, 3, 98, 1, 2, 5),
    _IpsecAhCurrentInboundSAs_Type()
)
ipsecAhCurrentInboundSAs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecAhCurrentInboundSAs.setStatus("current")
_IpsecAhTotalInboundSAs_Type = Counter32
_IpsecAhTotalInboundSAs_Object = MibScalar
ipsecAhTotalInboundSAs = _IpsecAhTotalInboundSAs_Object(
    (1, 3, 6, 1, 3, 98, 1, 2, 6),
    _IpsecAhTotalInboundSAs_Type()
)
ipsecAhTotalInboundSAs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecAhTotalInboundSAs.setStatus("current")
_IpsecAhCurrentOutboundSAs_Type = Gauge32
_IpsecAhCurrentOutboundSAs_Object = MibScalar
ipsecAhCurrentOutboundSAs = _IpsecAhCurrentOutboundSAs_Object(
    (1, 3, 6, 1, 3, 98, 1, 2, 7),
    _IpsecAhCurrentOutboundSAs_Type()
)
ipsecAhCurrentOutboundSAs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecAhCurrentOutboundSAs.setStatus("current")
_IpsecAhTotalOutboundSAs_Type = Counter32
_IpsecAhTotalOutboundSAs_Object = MibScalar
ipsecAhTotalOutboundSAs = _IpsecAhTotalOutboundSAs_Object(
    (1, 3, 6, 1, 3, 98, 1, 2, 8),
    _IpsecAhTotalOutboundSAs_Type()
)
ipsecAhTotalOutboundSAs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecAhTotalOutboundSAs.setStatus("current")
_IpsecIpcompCurrentInboundSAs_Type = Gauge32
_IpsecIpcompCurrentInboundSAs_Object = MibScalar
ipsecIpcompCurrentInboundSAs = _IpsecIpcompCurrentInboundSAs_Object(
    (1, 3, 6, 1, 3, 98, 1, 2, 9),
    _IpsecIpcompCurrentInboundSAs_Type()
)
ipsecIpcompCurrentInboundSAs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecIpcompCurrentInboundSAs.setStatus("current")
_IpsecIpcompTotalInboundSAs_Type = Counter32
_IpsecIpcompTotalInboundSAs_Object = MibScalar
ipsecIpcompTotalInboundSAs = _IpsecIpcompTotalInboundSAs_Object(
    (1, 3, 6, 1, 3, 98, 1, 2, 10),
    _IpsecIpcompTotalInboundSAs_Type()
)
ipsecIpcompTotalInboundSAs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecIpcompTotalInboundSAs.setStatus("current")
_IpsecIpcompCurrentOutboundSAs_Type = Gauge32
_IpsecIpcompCurrentOutboundSAs_Object = MibScalar
ipsecIpcompCurrentOutboundSAs = _IpsecIpcompCurrentOutboundSAs_Object(
    (1, 3, 6, 1, 3, 98, 1, 2, 11),
    _IpsecIpcompCurrentOutboundSAs_Type()
)
ipsecIpcompCurrentOutboundSAs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecIpcompCurrentOutboundSAs.setStatus("current")
_IpsecIpcompTotalOutboundSAs_Type = Counter32
_IpsecIpcompTotalOutboundSAs_Object = MibScalar
ipsecIpcompTotalOutboundSAs = _IpsecIpcompTotalOutboundSAs_Object(
    (1, 3, 6, 1, 3, 98, 1, 2, 12),
    _IpsecIpcompTotalOutboundSAs_Type()
)
ipsecIpcompTotalOutboundSAs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecIpcompTotalOutboundSAs.setStatus("current")
_SaErrors_ObjectIdentity = ObjectIdentity
saErrors = _SaErrors_ObjectIdentity(
    (1, 3, 6, 1, 3, 98, 1, 3)
)
if mibBuilder.loadTexts:
    saErrors.setStatus("current")
_IpsecDecryptionErrors_Type = Counter32
_IpsecDecryptionErrors_Object = MibScalar
ipsecDecryptionErrors = _IpsecDecryptionErrors_Object(
    (1, 3, 6, 1, 3, 98, 1, 3, 1),
    _IpsecDecryptionErrors_Type()
)
ipsecDecryptionErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecDecryptionErrors.setStatus("current")
_IpsecAuthenticationErrors_Type = Counter32
_IpsecAuthenticationErrors_Object = MibScalar
ipsecAuthenticationErrors = _IpsecAuthenticationErrors_Object(
    (1, 3, 6, 1, 3, 98, 1, 3, 2),
    _IpsecAuthenticationErrors_Type()
)
ipsecAuthenticationErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecAuthenticationErrors.setStatus("current")
_IpsecReplayErrors_Type = Counter32
_IpsecReplayErrors_Object = MibScalar
ipsecReplayErrors = _IpsecReplayErrors_Object(
    (1, 3, 6, 1, 3, 98, 1, 3, 3),
    _IpsecReplayErrors_Type()
)
ipsecReplayErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecReplayErrors.setStatus("current")
_IpsecPolicyErrors_Type = Counter32
_IpsecPolicyErrors_Object = MibScalar
ipsecPolicyErrors = _IpsecPolicyErrors_Object(
    (1, 3, 6, 1, 3, 98, 1, 3, 4),
    _IpsecPolicyErrors_Type()
)
ipsecPolicyErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecPolicyErrors.setStatus("current")
_IpsecOtherReceiveErrors_Type = Counter32
_IpsecOtherReceiveErrors_Object = MibScalar
ipsecOtherReceiveErrors = _IpsecOtherReceiveErrors_Object(
    (1, 3, 6, 1, 3, 98, 1, 3, 5),
    _IpsecOtherReceiveErrors_Type()
)
ipsecOtherReceiveErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecOtherReceiveErrors.setStatus("current")
_IpsecSendErrors_Type = Counter32
_IpsecSendErrors_Object = MibScalar
ipsecSendErrors = _IpsecSendErrors_Object(
    (1, 3, 6, 1, 3, 98, 1, 3, 6),
    _IpsecSendErrors_Type()
)
ipsecSendErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecSendErrors.setStatus("current")
_IpsecUnknownSpiErrors_Type = Counter32
_IpsecUnknownSpiErrors_Object = MibScalar
ipsecUnknownSpiErrors = _IpsecUnknownSpiErrors_Object(
    (1, 3, 6, 1, 3, 98, 1, 3, 7),
    _IpsecUnknownSpiErrors_Type()
)
ipsecUnknownSpiErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecUnknownSpiErrors.setStatus("current")
_SaTraps_ObjectIdentity = ObjectIdentity
saTraps = _SaTraps_ObjectIdentity(
    (1, 3, 6, 1, 3, 98, 1, 4)
)
if mibBuilder.loadTexts:
    saTraps.setStatus("current")
_SaTrapObjects_ObjectIdentity = ObjectIdentity
saTrapObjects = _SaTrapObjects_ObjectIdentity(
    (1, 3, 6, 1, 3, 98, 1, 5)
)
if mibBuilder.loadTexts:
    saTrapObjects.setStatus("current")
_IpsecSecurityProtocol_Type = IpsecDoiSecProtocolId
_IpsecSecurityProtocol_Object = MibScalar
ipsecSecurityProtocol = _IpsecSecurityProtocol_Object(
    (1, 3, 6, 1, 3, 98, 1, 5, 1),
    _IpsecSecurityProtocol_Type()
)
ipsecSecurityProtocol.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ipsecSecurityProtocol.setStatus("current")
_IpsecSPI_Type = Unsigned32
_IpsecSPI_Object = MibScalar
ipsecSPI = _IpsecSPI_Object(
    (1, 3, 6, 1, 3, 98, 1, 5, 2),
    _IpsecSPI_Type()
)
ipsecSPI.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ipsecSPI.setStatus("current")
_IpsecLocalAddress_Type = IpsecIpv6Address
_IpsecLocalAddress_Object = MibScalar
ipsecLocalAddress = _IpsecLocalAddress_Object(
    (1, 3, 6, 1, 3, 98, 1, 5, 3),
    _IpsecLocalAddress_Type()
)
ipsecLocalAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ipsecLocalAddress.setStatus("current")
_IpsecPeerAddress_Type = IpsecIpv6Address
_IpsecPeerAddress_Object = MibScalar
ipsecPeerAddress = _IpsecPeerAddress_Object(
    (1, 3, 6, 1, 3, 98, 1, 5, 4),
    _IpsecPeerAddress_Type()
)
ipsecPeerAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ipsecPeerAddress.setStatus("current")
_SaTrapControl_ObjectIdentity = ObjectIdentity
saTrapControl = _SaTrapControl_ObjectIdentity(
    (1, 3, 6, 1, 3, 98, 1, 6)
)
if mibBuilder.loadTexts:
    saTrapControl.setStatus("current")


class _EspAuthFailureTrapEnable_Type(TruthValue):
    """Custom type espAuthFailureTrapEnable based on TruthValue"""


_EspAuthFailureTrapEnable_Object = MibScalar
espAuthFailureTrapEnable = _EspAuthFailureTrapEnable_Object(
    (1, 3, 6, 1, 3, 98, 1, 6, 1),
    _EspAuthFailureTrapEnable_Type()
)
espAuthFailureTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    espAuthFailureTrapEnable.setStatus("current")


class _AhAuthFailureTrapEnable_Type(TruthValue):
    """Custom type ahAuthFailureTrapEnable based on TruthValue"""


_AhAuthFailureTrapEnable_Object = MibScalar
ahAuthFailureTrapEnable = _AhAuthFailureTrapEnable_Object(
    (1, 3, 6, 1, 3, 98, 1, 6, 2),
    _AhAuthFailureTrapEnable_Type()
)
ahAuthFailureTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ahAuthFailureTrapEnable.setStatus("current")


class _EspReplayFailureTrapEnable_Type(TruthValue):
    """Custom type espReplayFailureTrapEnable based on TruthValue"""


_EspReplayFailureTrapEnable_Object = MibScalar
espReplayFailureTrapEnable = _EspReplayFailureTrapEnable_Object(
    (1, 3, 6, 1, 3, 98, 1, 6, 3),
    _EspReplayFailureTrapEnable_Type()
)
espReplayFailureTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    espReplayFailureTrapEnable.setStatus("current")


class _AhReplayFailureTrapEnable_Type(TruthValue):
    """Custom type ahReplayFailureTrapEnable based on TruthValue"""


_AhReplayFailureTrapEnable_Object = MibScalar
ahReplayFailureTrapEnable = _AhReplayFailureTrapEnable_Object(
    (1, 3, 6, 1, 3, 98, 1, 6, 4),
    _AhReplayFailureTrapEnable_Type()
)
ahReplayFailureTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ahReplayFailureTrapEnable.setStatus("current")


class _EspPolicyFailureTrapEnable_Type(TruthValue):
    """Custom type espPolicyFailureTrapEnable based on TruthValue"""


_EspPolicyFailureTrapEnable_Object = MibScalar
espPolicyFailureTrapEnable = _EspPolicyFailureTrapEnable_Object(
    (1, 3, 6, 1, 3, 98, 1, 6, 5),
    _EspPolicyFailureTrapEnable_Type()
)
espPolicyFailureTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    espPolicyFailureTrapEnable.setStatus("current")


class _AhPolicyFailureTrapEnable_Type(TruthValue):
    """Custom type ahPolicyFailureTrapEnable based on TruthValue"""


_AhPolicyFailureTrapEnable_Object = MibScalar
ahPolicyFailureTrapEnable = _AhPolicyFailureTrapEnable_Object(
    (1, 3, 6, 1, 3, 98, 1, 6, 6),
    _AhPolicyFailureTrapEnable_Type()
)
ahPolicyFailureTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ahPolicyFailureTrapEnable.setStatus("current")


class _InvalidSpiTrapEnable_Type(TruthValue):
    """Custom type invalidSpiTrapEnable based on TruthValue"""


_InvalidSpiTrapEnable_Object = MibScalar
invalidSpiTrapEnable = _InvalidSpiTrapEnable_Object(
    (1, 3, 6, 1, 3, 98, 1, 6, 7),
    _InvalidSpiTrapEnable_Type()
)
invalidSpiTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    invalidSpiTrapEnable.setStatus("current")


class _OtherPolicyFailureTrapEnable_Type(TruthValue):
    """Custom type otherPolicyFailureTrapEnable based on TruthValue"""


_OtherPolicyFailureTrapEnable_Object = MibScalar
otherPolicyFailureTrapEnable = _OtherPolicyFailureTrapEnable_Object(
    (1, 3, 6, 1, 3, 98, 1, 6, 8),
    _OtherPolicyFailureTrapEnable_Type()
)
otherPolicyFailureTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    otherPolicyFailureTrapEnable.setStatus("current")
_SaGroups_ObjectIdentity = ObjectIdentity
saGroups = _SaGroups_ObjectIdentity(
    (1, 3, 6, 1, 3, 98, 1, 7)
)
if mibBuilder.loadTexts:
    saGroups.setStatus("current")
_SaConformance_ObjectIdentity = ObjectIdentity
saConformance = _SaConformance_ObjectIdentity(
    (1, 3, 6, 1, 3, 98, 1, 8)
)
if mibBuilder.loadTexts:
    saConformance.setStatus("current")

# Managed Objects groups

ipsecSaEspGroup = ObjectGroup(
    (1, 3, 6, 1, 3, 98, 1, 7, 1)
)
ipsecSaEspGroup.setObjects(
      *(("IPSEC-SA-MON-MIB", "ipsecSaEspInAddress"),
        ("IPSEC-SA-MON-MIB", "ipsecSaEspInSpi"),
        ("IPSEC-SA-MON-MIB", "ipsecSaEspInDestId"),
        ("IPSEC-SA-MON-MIB", "ipsecSaEspInDestIdType"),
        ("IPSEC-SA-MON-MIB", "ipsecSaEspInSourceId"),
        ("IPSEC-SA-MON-MIB", "ipsecSaEspInSourceIdType"),
        ("IPSEC-SA-MON-MIB", "ipsecSaEspInProtocol"),
        ("IPSEC-SA-MON-MIB", "ipsecSaEspInDestPort"),
        ("IPSEC-SA-MON-MIB", "ipsecSaEspInSourcePort"),
        ("IPSEC-SA-MON-MIB", "ipsecSaEspInCreator"),
        ("IPSEC-SA-MON-MIB", "ipsecSaEspInEncapsulation"),
        ("IPSEC-SA-MON-MIB", "ipsecSaEspInEncAlg"),
        ("IPSEC-SA-MON-MIB", "ipsecSaEspInEncKeyLength"),
        ("IPSEC-SA-MON-MIB", "ipsecSaEspInAuthAlg"),
        ("IPSEC-SA-MON-MIB", "ipsecSaEspInAuthKeyLength"),
        ("IPSEC-SA-MON-MIB", "ipsecSaEspInRepWinSize"),
        ("IPSEC-SA-MON-MIB", "ipsecSaEspInLimitSeconds"),
        ("IPSEC-SA-MON-MIB", "ipsecSaEspInLimitKbytes"),
        ("IPSEC-SA-MON-MIB", "ipsecSaEspInAccSeconds"),
        ("IPSEC-SA-MON-MIB", "ipsecSaEspInAccKbytes"),
        ("IPSEC-SA-MON-MIB", "ipsecSaEspInUserOctets"),
        ("IPSEC-SA-MON-MIB", "ipsecSaEspInPackets"),
        ("IPSEC-SA-MON-MIB", "ipsecSaEspInDecryptErrors"),
        ("IPSEC-SA-MON-MIB", "ipsecSaEspInAuthErrors"),
        ("IPSEC-SA-MON-MIB", "ipsecSaEspInReplayErrors"),
        ("IPSEC-SA-MON-MIB", "ipsecSaEspInPolicyErrors"),
        ("IPSEC-SA-MON-MIB", "ipsecSaEspInPadErrors"),
        ("IPSEC-SA-MON-MIB", "ipsecSaEspInOtherReceiveErrors"),
        ("IPSEC-SA-MON-MIB", "ipsecSaEspOutAddress"),
        ("IPSEC-SA-MON-MIB", "ipsecSaEspOutSpi"),
        ("IPSEC-SA-MON-MIB", "ipsecSaEspOutSourceId"),
        ("IPSEC-SA-MON-MIB", "ipsecSaEspOutSourceIdType"),
        ("IPSEC-SA-MON-MIB", "ipsecSaEspOutDestId"),
        ("IPSEC-SA-MON-MIB", "ipsecSaEspOutDestIdType"),
        ("IPSEC-SA-MON-MIB", "ipsecSaEspOutProtocol"),
        ("IPSEC-SA-MON-MIB", "ipsecSaEspOutSourcePort"),
        ("IPSEC-SA-MON-MIB", "ipsecSaEspOutDestPort"),
        ("IPSEC-SA-MON-MIB", "ipsecSaEspOutCreator"),
        ("IPSEC-SA-MON-MIB", "ipsecSaEspOutEncapsulation"),
        ("IPSEC-SA-MON-MIB", "ipsecSaEspOutEncAlg"),
        ("IPSEC-SA-MON-MIB", "ipsecSaEspOutAuthKeyLength"),
        ("IPSEC-SA-MON-MIB", "ipsecSaEspOutEncKeyLength"),
        ("IPSEC-SA-MON-MIB", "ipsecSaEspOutAuthAlg"),
        ("IPSEC-SA-MON-MIB", "ipsecSaEspOutLimitSeconds"),
        ("IPSEC-SA-MON-MIB", "ipsecSaEspOutLimitKbytes"),
        ("IPSEC-SA-MON-MIB", "ipsecSaEspOutAccSeconds"),
        ("IPSEC-SA-MON-MIB", "ipsecSaEspOutAccKbytes"),
        ("IPSEC-SA-MON-MIB", "ipsecSaEspOutUserOctets"),
        ("IPSEC-SA-MON-MIB", "ipsecSaEspOutPackets"),
        ("IPSEC-SA-MON-MIB", "ipsecSaEspOutSendErrors"),
        ("IPSEC-SA-MON-MIB", "ipsecEspCurrentInboundSAs"),
        ("IPSEC-SA-MON-MIB", "ipsecEspTotalInboundSAs"),
        ("IPSEC-SA-MON-MIB", "ipsecEspCurrentOutboundSAs"),
        ("IPSEC-SA-MON-MIB", "ipsecEspTotalOutboundSAs"))
)
if mibBuilder.loadTexts:
    ipsecSaEspGroup.setStatus("current")

ipsecSaAhGroup = ObjectGroup(
    (1, 3, 6, 1, 3, 98, 1, 7, 2)
)
ipsecSaAhGroup.setObjects(
      *(("IPSEC-SA-MON-MIB", "ipsecSaAhInAddress"),
        ("IPSEC-SA-MON-MIB", "ipsecSaAhInSpi"),
        ("IPSEC-SA-MON-MIB", "ipsecSaAhInDestId"),
        ("IPSEC-SA-MON-MIB", "ipsecSaAhInDestIdType"),
        ("IPSEC-SA-MON-MIB", "ipsecSaAhInSourceId"),
        ("IPSEC-SA-MON-MIB", "ipsecSaAhInSourceIdType"),
        ("IPSEC-SA-MON-MIB", "ipsecSaAhInProtocol"),
        ("IPSEC-SA-MON-MIB", "ipsecSaAhInDestPort"),
        ("IPSEC-SA-MON-MIB", "ipsecSaAhInSourcePort"),
        ("IPSEC-SA-MON-MIB", "ipsecSaAhInCreator"),
        ("IPSEC-SA-MON-MIB", "ipsecSaAhInEncapsulation"),
        ("IPSEC-SA-MON-MIB", "ipsecSaAhInAuthAlg"),
        ("IPSEC-SA-MON-MIB", "ipsecSaAhInAuthKeyLength"),
        ("IPSEC-SA-MON-MIB", "ipsecSaAhInRepWinSize"),
        ("IPSEC-SA-MON-MIB", "ipsecSaAhInLimitSeconds"),
        ("IPSEC-SA-MON-MIB", "ipsecSaAhInLimitKbytes"),
        ("IPSEC-SA-MON-MIB", "ipsecSaAhInAccSeconds"),
        ("IPSEC-SA-MON-MIB", "ipsecSaAhInAccKbytes"),
        ("IPSEC-SA-MON-MIB", "ipsecSaAhInUserOctets"),
        ("IPSEC-SA-MON-MIB", "ipsecSaAhInPackets"),
        ("IPSEC-SA-MON-MIB", "ipsecSaAhInAuthErrors"),
        ("IPSEC-SA-MON-MIB", "ipsecSaAhInReplayErrors"),
        ("IPSEC-SA-MON-MIB", "ipsecSaAhInPolicyErrors"),
        ("IPSEC-SA-MON-MIB", "ipsecSaAhInOtherReceiveErrors"),
        ("IPSEC-SA-MON-MIB", "ipsecSaAhOutAddress"),
        ("IPSEC-SA-MON-MIB", "ipsecSaAhOutSpi"),
        ("IPSEC-SA-MON-MIB", "ipsecSaAhOutSourceId"),
        ("IPSEC-SA-MON-MIB", "ipsecSaAhOutSourceIdType"),
        ("IPSEC-SA-MON-MIB", "ipsecSaAhOutDestId"),
        ("IPSEC-SA-MON-MIB", "ipsecSaAhOutDestIdType"),
        ("IPSEC-SA-MON-MIB", "ipsecSaAhOutProtocol"),
        ("IPSEC-SA-MON-MIB", "ipsecSaAhOutSourcePort"),
        ("IPSEC-SA-MON-MIB", "ipsecSaAhOutDestPort"),
        ("IPSEC-SA-MON-MIB", "ipsecSaAhOutCreator"),
        ("IPSEC-SA-MON-MIB", "ipsecSaAhOutEncapsulation"),
        ("IPSEC-SA-MON-MIB", "ipsecSaAhOutAuthAlg"),
        ("IPSEC-SA-MON-MIB", "ipsecSaAhOutAuthKeyLength"),
        ("IPSEC-SA-MON-MIB", "ipsecSaAhOutLimitSeconds"),
        ("IPSEC-SA-MON-MIB", "ipsecSaAhOutLimitKbytes"),
        ("IPSEC-SA-MON-MIB", "ipsecSaAhOutAccSeconds"),
        ("IPSEC-SA-MON-MIB", "ipsecSaAhOutAccKbytes"),
        ("IPSEC-SA-MON-MIB", "ipsecSaAhOutUserOctets"),
        ("IPSEC-SA-MON-MIB", "ipsecSaAhOutPackets"),
        ("IPSEC-SA-MON-MIB", "ipsecSaAhOutSendErrors"),
        ("IPSEC-SA-MON-MIB", "ipsecAhCurrentInboundSAs"),
        ("IPSEC-SA-MON-MIB", "ipsecAhTotalInboundSAs"),
        ("IPSEC-SA-MON-MIB", "ipsecAhCurrentOutboundSAs"),
        ("IPSEC-SA-MON-MIB", "ipsecAhTotalOutboundSAs"))
)
if mibBuilder.loadTexts:
    ipsecSaAhGroup.setStatus("current")

ipsecSaIpcompGroup = ObjectGroup(
    (1, 3, 6, 1, 3, 98, 1, 7, 3)
)
ipsecSaIpcompGroup.setObjects(
      *(("IPSEC-SA-MON-MIB", "ipsecSaIpcompInAddress"),
        ("IPSEC-SA-MON-MIB", "ipsecSaIpcompInCpi"),
        ("IPSEC-SA-MON-MIB", "ipsecSaIpcompInDestId"),
        ("IPSEC-SA-MON-MIB", "ipsecSaIpcompInDestIdType"),
        ("IPSEC-SA-MON-MIB", "ipsecSaIpcompInSourceId"),
        ("IPSEC-SA-MON-MIB", "ipsecSaIpcompInSourceIdType"),
        ("IPSEC-SA-MON-MIB", "ipsecSaIpcompInProtocol"),
        ("IPSEC-SA-MON-MIB", "ipsecSaIpcompInDestPort"),
        ("IPSEC-SA-MON-MIB", "ipsecSaIpcompInSourcePort"),
        ("IPSEC-SA-MON-MIB", "ipsecSaIpcompInCreator"),
        ("IPSEC-SA-MON-MIB", "ipsecSaIpcompInEncapsulation"),
        ("IPSEC-SA-MON-MIB", "ipsecSaIpcompInDecompAlg"),
        ("IPSEC-SA-MON-MIB", "ipsecSaIpcompInSeconds"),
        ("IPSEC-SA-MON-MIB", "ipsecSaIpcompInUserOctets"),
        ("IPSEC-SA-MON-MIB", "ipsecSaIpcompInPackets"),
        ("IPSEC-SA-MON-MIB", "ipsecSaIpcompInDecompErrors"),
        ("IPSEC-SA-MON-MIB", "ipsecSaIpcompInOtherReceiveErrors"),
        ("IPSEC-SA-MON-MIB", "ipsecSaIpcompOutAddress"),
        ("IPSEC-SA-MON-MIB", "ipsecSaIpcompOutCpi"),
        ("IPSEC-SA-MON-MIB", "ipsecSaIpcompOutSourceId"),
        ("IPSEC-SA-MON-MIB", "ipsecSaIpcompOutSourceIdType"),
        ("IPSEC-SA-MON-MIB", "ipsecSaIpcompOutDestId"),
        ("IPSEC-SA-MON-MIB", "ipsecSaIpcompOutDestIdType"),
        ("IPSEC-SA-MON-MIB", "ipsecSaIpcompOutProtocol"),
        ("IPSEC-SA-MON-MIB", "ipsecSaIpcompOutSourcePort"),
        ("IPSEC-SA-MON-MIB", "ipsecSaIpcompOutDestPort"),
        ("IPSEC-SA-MON-MIB", "ipsecSaIpcompOutCreator"),
        ("IPSEC-SA-MON-MIB", "ipsecSaIpcompOutEncapsulation"),
        ("IPSEC-SA-MON-MIB", "ipsecSaIpcompOutCompAlg"),
        ("IPSEC-SA-MON-MIB", "ipsecSaIpcompOutSeconds"),
        ("IPSEC-SA-MON-MIB", "ipsecSaIpcompOutUserOctets"),
        ("IPSEC-SA-MON-MIB", "ipsecSaIpcompOutOutputOctets"),
        ("IPSEC-SA-MON-MIB", "ipsecSaIpcompOutPackets"),
        ("IPSEC-SA-MON-MIB", "ipsecIpcompCurrentInboundSAs"),
        ("IPSEC-SA-MON-MIB", "ipsecIpcompTotalInboundSAs"),
        ("IPSEC-SA-MON-MIB", "ipsecIpcompCurrentOutboundSAs"),
        ("IPSEC-SA-MON-MIB", "ipsecIpcompTotalOutboundSAs"))
)
if mibBuilder.loadTexts:
    ipsecSaIpcompGroup.setStatus("current")

ipsecSaErrorsGroup = ObjectGroup(
    (1, 3, 6, 1, 3, 98, 1, 7, 4)
)
ipsecSaErrorsGroup.setObjects(
      *(("IPSEC-SA-MON-MIB", "ipsecDecryptionErrors"),
        ("IPSEC-SA-MON-MIB", "ipsecAuthenticationErrors"),
        ("IPSEC-SA-MON-MIB", "ipsecReplayErrors"),
        ("IPSEC-SA-MON-MIB", "ipsecPolicyErrors"),
        ("IPSEC-SA-MON-MIB", "ipsecOtherReceiveErrors"),
        ("IPSEC-SA-MON-MIB", "ipsecUnknownSpiErrors"),
        ("IPSEC-SA-MON-MIB", "ipsecSendErrors"))
)
if mibBuilder.loadTexts:
    ipsecSaErrorsGroup.setStatus("current")

ipsecSaFailureTrapEnableGroup = ObjectGroup(
    (1, 3, 6, 1, 3, 98, 1, 7, 5)
)
ipsecSaFailureTrapEnableGroup.setObjects(
      *(("IPSEC-SA-MON-MIB", "espAuthFailureTrapEnable"),
        ("IPSEC-SA-MON-MIB", "ahAuthFailureTrapEnable"),
        ("IPSEC-SA-MON-MIB", "espReplayFailureTrapEnable"),
        ("IPSEC-SA-MON-MIB", "ahReplayFailureTrapEnable"),
        ("IPSEC-SA-MON-MIB", "espPolicyFailureTrapEnable"),
        ("IPSEC-SA-MON-MIB", "ahPolicyFailureTrapEnable"),
        ("IPSEC-SA-MON-MIB", "invalidSpiTrapEnable"),
        ("IPSEC-SA-MON-MIB", "otherPolicyFailureTrapEnable"))
)
if mibBuilder.loadTexts:
    ipsecSaFailureTrapEnableGroup.setStatus("current")

ipsecSaTrapArgumentGroup = ObjectGroup(
    (1, 3, 6, 1, 3, 98, 1, 7, 6)
)
ipsecSaTrapArgumentGroup.setObjects(
      *(("IPSEC-SA-MON-MIB", "ipsecSecurityProtocol"),
        ("IPSEC-SA-MON-MIB", "ipsecSPI"),
        ("IPSEC-SA-MON-MIB", "ipsecLocalAddress"),
        ("IPSEC-SA-MON-MIB", "ipsecPeerAddress"))
)
if mibBuilder.loadTexts:
    ipsecSaTrapArgumentGroup.setStatus("current")


# Notification objects

espAuthFailureTrap = NotificationType(
    (1, 3, 6, 1, 3, 98, 1, 4, 0, 1)
)
espAuthFailureTrap.setObjects(
    ("IPSEC-SA-MON-MIB", "ipsecSaEspInAuthErrors")
)
if mibBuilder.loadTexts:
    espAuthFailureTrap.setStatus(
        "current"
    )

ahAuthFailureTrap = NotificationType(
    (1, 3, 6, 1, 3, 98, 1, 4, 0, 2)
)
ahAuthFailureTrap.setObjects(
    ("IPSEC-SA-MON-MIB", "ipsecSaAhInAuthErrors")
)
if mibBuilder.loadTexts:
    ahAuthFailureTrap.setStatus(
        "current"
    )

espReplayFailureTrap = NotificationType(
    (1, 3, 6, 1, 3, 98, 1, 4, 0, 3)
)
espReplayFailureTrap.setObjects(
    ("IPSEC-SA-MON-MIB", "ipsecSaEspInReplayErrors")
)
if mibBuilder.loadTexts:
    espReplayFailureTrap.setStatus(
        "current"
    )

ahReplayFailureTrap = NotificationType(
    (1, 3, 6, 1, 3, 98, 1, 4, 0, 4)
)
ahReplayFailureTrap.setObjects(
    ("IPSEC-SA-MON-MIB", "ipsecSaAhInReplayErrors")
)
if mibBuilder.loadTexts:
    ahReplayFailureTrap.setStatus(
        "current"
    )

espPolicyFailureTrap = NotificationType(
    (1, 3, 6, 1, 3, 98, 1, 4, 0, 5)
)
espPolicyFailureTrap.setObjects(
    ("IPSEC-SA-MON-MIB", "ipsecSaEspInPolicyErrors")
)
if mibBuilder.loadTexts:
    espPolicyFailureTrap.setStatus(
        "current"
    )

ahPolicyFailureTrap = NotificationType(
    (1, 3, 6, 1, 3, 98, 1, 4, 0, 6)
)
ahPolicyFailureTrap.setObjects(
    ("IPSEC-SA-MON-MIB", "ipsecSaAhInPolicyErrors")
)
if mibBuilder.loadTexts:
    ahPolicyFailureTrap.setStatus(
        "current"
    )

espInvalidSpiTrap = NotificationType(
    (1, 3, 6, 1, 3, 98, 1, 4, 0, 7)
)
espInvalidSpiTrap.setObjects(
      *(("IPSEC-SA-MON-MIB", "ipsecLocalAddress"),
        ("IPSEC-SA-MON-MIB", "ipsecSecurityProtocol"),
        ("IPSEC-SA-MON-MIB", "ipsecPeerAddress"),
        ("IPSEC-SA-MON-MIB", "ipsecSPI"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    espInvalidSpiTrap.setStatus(
        "current"
    )

otherPolicyFailureTrap = NotificationType(
    (1, 3, 6, 1, 3, 98, 1, 4, 0, 8)
)
otherPolicyFailureTrap.setObjects(
      *(("IPSEC-SA-MON-MIB", "ipsecPolicyErrors"),
        ("IPSEC-SA-MON-MIB", "ipsecPeerAddress"),
        ("IPSEC-SA-MON-MIB", "ipsecLocalAddress"))
)
if mibBuilder.loadTexts:
    otherPolicyFailureTrap.setStatus(
        "current"
    )


# Notifications groups

ipsecSaFailureTrapGroup = NotificationGroup(
    (1, 3, 6, 1, 3, 98, 1, 7, 7)
)
ipsecSaFailureTrapGroup.setObjects(
      *(("IPSEC-SA-MON-MIB", "espAuthFailureTrap"),
        ("IPSEC-SA-MON-MIB", "ahAuthFailureTrap"),
        ("IPSEC-SA-MON-MIB", "espReplayFailureTrap"),
        ("IPSEC-SA-MON-MIB", "ahReplayFailureTrap"),
        ("IPSEC-SA-MON-MIB", "espPolicyFailureTrap"),
        ("IPSEC-SA-MON-MIB", "ahPolicyFailureTrap"),
        ("IPSEC-SA-MON-MIB", "espInvalidSpiTrap"),
        ("IPSEC-SA-MON-MIB", "otherPolicyFailureTrap"))
)
if mibBuilder.loadTexts:
    ipsecSaFailureTrapGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

ipsecSaMonitorCompliance = ModuleCompliance(
    (1, 3, 6, 1, 3, 98, 1, 8, 1)
)
if mibBuilder.loadTexts:
    ipsecSaMonitorCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "IPSEC-SA-MON-MIB",
    **{"IpsecSaCreatorIdent": IpsecSaCreatorIdent,
       "IpsecIpv6Address": IpsecIpv6Address,
       "IpsecRawId": IpsecRawId,
       "ipsecSaMonModule": ipsecSaMonModule,
       "ipsecSaMonitorMIB": ipsecSaMonitorMIB,
       "saTables": saTables,
       "ipsecSaEspInTable": ipsecSaEspInTable,
       "ipsecSaEspInEntry": ipsecSaEspInEntry,
       "ipsecSaEspInAddress": ipsecSaEspInAddress,
       "ipsecSaEspInSpi": ipsecSaEspInSpi,
       "ipsecSaEspInDestId": ipsecSaEspInDestId,
       "ipsecSaEspInDestIdType": ipsecSaEspInDestIdType,
       "ipsecSaEspInSourceId": ipsecSaEspInSourceId,
       "ipsecSaEspInSourceIdType": ipsecSaEspInSourceIdType,
       "ipsecSaEspInProtocol": ipsecSaEspInProtocol,
       "ipsecSaEspInDestPort": ipsecSaEspInDestPort,
       "ipsecSaEspInSourcePort": ipsecSaEspInSourcePort,
       "ipsecSaEspInCreator": ipsecSaEspInCreator,
       "ipsecSaEspInEncapsulation": ipsecSaEspInEncapsulation,
       "ipsecSaEspInEncAlg": ipsecSaEspInEncAlg,
       "ipsecSaEspInEncKeyLength": ipsecSaEspInEncKeyLength,
       "ipsecSaEspInAuthAlg": ipsecSaEspInAuthAlg,
       "ipsecSaEspInAuthKeyLength": ipsecSaEspInAuthKeyLength,
       "ipsecSaEspInRepWinSize": ipsecSaEspInRepWinSize,
       "ipsecSaEspInLimitSeconds": ipsecSaEspInLimitSeconds,
       "ipsecSaEspInLimitKbytes": ipsecSaEspInLimitKbytes,
       "ipsecSaEspInAccSeconds": ipsecSaEspInAccSeconds,
       "ipsecSaEspInAccKbytes": ipsecSaEspInAccKbytes,
       "ipsecSaEspInUserOctets": ipsecSaEspInUserOctets,
       "ipsecSaEspInPackets": ipsecSaEspInPackets,
       "ipsecSaEspInDecryptErrors": ipsecSaEspInDecryptErrors,
       "ipsecSaEspInAuthErrors": ipsecSaEspInAuthErrors,
       "ipsecSaEspInReplayErrors": ipsecSaEspInReplayErrors,
       "ipsecSaEspInPolicyErrors": ipsecSaEspInPolicyErrors,
       "ipsecSaEspInPadErrors": ipsecSaEspInPadErrors,
       "ipsecSaEspInOtherReceiveErrors": ipsecSaEspInOtherReceiveErrors,
       "ipsecSaAhInTable": ipsecSaAhInTable,
       "ipsecSaAhInEntry": ipsecSaAhInEntry,
       "ipsecSaAhInAddress": ipsecSaAhInAddress,
       "ipsecSaAhInSpi": ipsecSaAhInSpi,
       "ipsecSaAhInDestId": ipsecSaAhInDestId,
       "ipsecSaAhInDestIdType": ipsecSaAhInDestIdType,
       "ipsecSaAhInSourceId": ipsecSaAhInSourceId,
       "ipsecSaAhInSourceIdType": ipsecSaAhInSourceIdType,
       "ipsecSaAhInProtocol": ipsecSaAhInProtocol,
       "ipsecSaAhInDestPort": ipsecSaAhInDestPort,
       "ipsecSaAhInSourcePort": ipsecSaAhInSourcePort,
       "ipsecSaAhInCreator": ipsecSaAhInCreator,
       "ipsecSaAhInEncapsulation": ipsecSaAhInEncapsulation,
       "ipsecSaAhInAuthAlg": ipsecSaAhInAuthAlg,
       "ipsecSaAhInAuthKeyLength": ipsecSaAhInAuthKeyLength,
       "ipsecSaAhInRepWinSize": ipsecSaAhInRepWinSize,
       "ipsecSaAhInLimitSeconds": ipsecSaAhInLimitSeconds,
       "ipsecSaAhInLimitKbytes": ipsecSaAhInLimitKbytes,
       "ipsecSaAhInAccSeconds": ipsecSaAhInAccSeconds,
       "ipsecSaAhInAccKbytes": ipsecSaAhInAccKbytes,
       "ipsecSaAhInUserOctets": ipsecSaAhInUserOctets,
       "ipsecSaAhInPackets": ipsecSaAhInPackets,
       "ipsecSaAhInAuthErrors": ipsecSaAhInAuthErrors,
       "ipsecSaAhInReplayErrors": ipsecSaAhInReplayErrors,
       "ipsecSaAhInPolicyErrors": ipsecSaAhInPolicyErrors,
       "ipsecSaAhInOtherReceiveErrors": ipsecSaAhInOtherReceiveErrors,
       "ipsecSaIpcompInTable": ipsecSaIpcompInTable,
       "ipsecSaIpcompInEntry": ipsecSaIpcompInEntry,
       "ipsecSaIpcompInAddress": ipsecSaIpcompInAddress,
       "ipsecSaIpcompInCpi": ipsecSaIpcompInCpi,
       "ipsecSaIpcompInDestId": ipsecSaIpcompInDestId,
       "ipsecSaIpcompInDestIdType": ipsecSaIpcompInDestIdType,
       "ipsecSaIpcompInSourceId": ipsecSaIpcompInSourceId,
       "ipsecSaIpcompInSourceIdType": ipsecSaIpcompInSourceIdType,
       "ipsecSaIpcompInProtocol": ipsecSaIpcompInProtocol,
       "ipsecSaIpcompInDestPort": ipsecSaIpcompInDestPort,
       "ipsecSaIpcompInSourcePort": ipsecSaIpcompInSourcePort,
       "ipsecSaIpcompInCreator": ipsecSaIpcompInCreator,
       "ipsecSaIpcompInEncapsulation": ipsecSaIpcompInEncapsulation,
       "ipsecSaIpcompInDecompAlg": ipsecSaIpcompInDecompAlg,
       "ipsecSaIpcompInSeconds": ipsecSaIpcompInSeconds,
       "ipsecSaIpcompInUserOctets": ipsecSaIpcompInUserOctets,
       "ipsecSaIpcompInPackets": ipsecSaIpcompInPackets,
       "ipsecSaIpcompInDecompErrors": ipsecSaIpcompInDecompErrors,
       "ipsecSaIpcompInOtherReceiveErrors": ipsecSaIpcompInOtherReceiveErrors,
       "ipsecSaEspOutTable": ipsecSaEspOutTable,
       "ipsecSaEspOutEntry": ipsecSaEspOutEntry,
       "ipsecSaEspOutAddress": ipsecSaEspOutAddress,
       "ipsecSaEspOutSpi": ipsecSaEspOutSpi,
       "ipsecSaEspOutSourceId": ipsecSaEspOutSourceId,
       "ipsecSaEspOutSourceIdType": ipsecSaEspOutSourceIdType,
       "ipsecSaEspOutDestId": ipsecSaEspOutDestId,
       "ipsecSaEspOutDestIdType": ipsecSaEspOutDestIdType,
       "ipsecSaEspOutProtocol": ipsecSaEspOutProtocol,
       "ipsecSaEspOutSourcePort": ipsecSaEspOutSourcePort,
       "ipsecSaEspOutDestPort": ipsecSaEspOutDestPort,
       "ipsecSaEspOutCreator": ipsecSaEspOutCreator,
       "ipsecSaEspOutEncapsulation": ipsecSaEspOutEncapsulation,
       "ipsecSaEspOutEncAlg": ipsecSaEspOutEncAlg,
       "ipsecSaEspOutEncKeyLength": ipsecSaEspOutEncKeyLength,
       "ipsecSaEspOutAuthAlg": ipsecSaEspOutAuthAlg,
       "ipsecSaEspOutAuthKeyLength": ipsecSaEspOutAuthKeyLength,
       "ipsecSaEspOutLimitSeconds": ipsecSaEspOutLimitSeconds,
       "ipsecSaEspOutLimitKbytes": ipsecSaEspOutLimitKbytes,
       "ipsecSaEspOutAccSeconds": ipsecSaEspOutAccSeconds,
       "ipsecSaEspOutAccKbytes": ipsecSaEspOutAccKbytes,
       "ipsecSaEspOutUserOctets": ipsecSaEspOutUserOctets,
       "ipsecSaEspOutPackets": ipsecSaEspOutPackets,
       "ipsecSaEspOutSendErrors": ipsecSaEspOutSendErrors,
       "ipsecSaAhOutTable": ipsecSaAhOutTable,
       "ipsecSaAhOutEntry": ipsecSaAhOutEntry,
       "ipsecSaAhOutAddress": ipsecSaAhOutAddress,
       "ipsecSaAhOutSpi": ipsecSaAhOutSpi,
       "ipsecSaAhOutSourceId": ipsecSaAhOutSourceId,
       "ipsecSaAhOutSourceIdType": ipsecSaAhOutSourceIdType,
       "ipsecSaAhOutDestId": ipsecSaAhOutDestId,
       "ipsecSaAhOutDestIdType": ipsecSaAhOutDestIdType,
       "ipsecSaAhOutProtocol": ipsecSaAhOutProtocol,
       "ipsecSaAhOutSourcePort": ipsecSaAhOutSourcePort,
       "ipsecSaAhOutDestPort": ipsecSaAhOutDestPort,
       "ipsecSaAhOutCreator": ipsecSaAhOutCreator,
       "ipsecSaAhOutEncapsulation": ipsecSaAhOutEncapsulation,
       "ipsecSaAhOutAuthAlg": ipsecSaAhOutAuthAlg,
       "ipsecSaAhOutAuthKeyLength": ipsecSaAhOutAuthKeyLength,
       "ipsecSaAhOutLimitSeconds": ipsecSaAhOutLimitSeconds,
       "ipsecSaAhOutLimitKbytes": ipsecSaAhOutLimitKbytes,
       "ipsecSaAhOutAccSeconds": ipsecSaAhOutAccSeconds,
       "ipsecSaAhOutAccKbytes": ipsecSaAhOutAccKbytes,
       "ipsecSaAhOutUserOctets": ipsecSaAhOutUserOctets,
       "ipsecSaAhOutPackets": ipsecSaAhOutPackets,
       "ipsecSaAhOutSendErrors": ipsecSaAhOutSendErrors,
       "ipsecSaIpcompOutTable": ipsecSaIpcompOutTable,
       "ipsecSaIpcompOutEntry": ipsecSaIpcompOutEntry,
       "ipsecSaIpcompOutAddress": ipsecSaIpcompOutAddress,
       "ipsecSaIpcompOutCpi": ipsecSaIpcompOutCpi,
       "ipsecSaIpcompOutSourceId": ipsecSaIpcompOutSourceId,
       "ipsecSaIpcompOutSourceIdType": ipsecSaIpcompOutSourceIdType,
       "ipsecSaIpcompOutDestId": ipsecSaIpcompOutDestId,
       "ipsecSaIpcompOutDestIdType": ipsecSaIpcompOutDestIdType,
       "ipsecSaIpcompOutProtocol": ipsecSaIpcompOutProtocol,
       "ipsecSaIpcompOutSourcePort": ipsecSaIpcompOutSourcePort,
       "ipsecSaIpcompOutDestPort": ipsecSaIpcompOutDestPort,
       "ipsecSaIpcompOutCreator": ipsecSaIpcompOutCreator,
       "ipsecSaIpcompOutEncapsulation": ipsecSaIpcompOutEncapsulation,
       "ipsecSaIpcompOutCompAlg": ipsecSaIpcompOutCompAlg,
       "ipsecSaIpcompOutSeconds": ipsecSaIpcompOutSeconds,
       "ipsecSaIpcompOutUserOctets": ipsecSaIpcompOutUserOctets,
       "ipsecSaIpcompOutOutputOctets": ipsecSaIpcompOutOutputOctets,
       "ipsecSaIpcompOutPackets": ipsecSaIpcompOutPackets,
       "saStatistics": saStatistics,
       "ipsecEspCurrentInboundSAs": ipsecEspCurrentInboundSAs,
       "ipsecEspTotalInboundSAs": ipsecEspTotalInboundSAs,
       "ipsecEspCurrentOutboundSAs": ipsecEspCurrentOutboundSAs,
       "ipsecEspTotalOutboundSAs": ipsecEspTotalOutboundSAs,
       "ipsecAhCurrentInboundSAs": ipsecAhCurrentInboundSAs,
       "ipsecAhTotalInboundSAs": ipsecAhTotalInboundSAs,
       "ipsecAhCurrentOutboundSAs": ipsecAhCurrentOutboundSAs,
       "ipsecAhTotalOutboundSAs": ipsecAhTotalOutboundSAs,
       "ipsecIpcompCurrentInboundSAs": ipsecIpcompCurrentInboundSAs,
       "ipsecIpcompTotalInboundSAs": ipsecIpcompTotalInboundSAs,
       "ipsecIpcompCurrentOutboundSAs": ipsecIpcompCurrentOutboundSAs,
       "ipsecIpcompTotalOutboundSAs": ipsecIpcompTotalOutboundSAs,
       "saErrors": saErrors,
       "ipsecDecryptionErrors": ipsecDecryptionErrors,
       "ipsecAuthenticationErrors": ipsecAuthenticationErrors,
       "ipsecReplayErrors": ipsecReplayErrors,
       "ipsecPolicyErrors": ipsecPolicyErrors,
       "ipsecOtherReceiveErrors": ipsecOtherReceiveErrors,
       "ipsecSendErrors": ipsecSendErrors,
       "ipsecUnknownSpiErrors": ipsecUnknownSpiErrors,
       "saTraps": saTraps,
       "espAuthFailureTrap": espAuthFailureTrap,
       "ahAuthFailureTrap": ahAuthFailureTrap,
       "espReplayFailureTrap": espReplayFailureTrap,
       "ahReplayFailureTrap": ahReplayFailureTrap,
       "espPolicyFailureTrap": espPolicyFailureTrap,
       "ahPolicyFailureTrap": ahPolicyFailureTrap,
       "espInvalidSpiTrap": espInvalidSpiTrap,
       "otherPolicyFailureTrap": otherPolicyFailureTrap,
       "saTrapObjects": saTrapObjects,
       "ipsecSecurityProtocol": ipsecSecurityProtocol,
       "ipsecSPI": ipsecSPI,
       "ipsecLocalAddress": ipsecLocalAddress,
       "ipsecPeerAddress": ipsecPeerAddress,
       "saTrapControl": saTrapControl,
       "espAuthFailureTrapEnable": espAuthFailureTrapEnable,
       "ahAuthFailureTrapEnable": ahAuthFailureTrapEnable,
       "espReplayFailureTrapEnable": espReplayFailureTrapEnable,
       "ahReplayFailureTrapEnable": ahReplayFailureTrapEnable,
       "espPolicyFailureTrapEnable": espPolicyFailureTrapEnable,
       "ahPolicyFailureTrapEnable": ahPolicyFailureTrapEnable,
       "invalidSpiTrapEnable": invalidSpiTrapEnable,
       "otherPolicyFailureTrapEnable": otherPolicyFailureTrapEnable,
       "saGroups": saGroups,
       "ipsecSaEspGroup": ipsecSaEspGroup,
       "ipsecSaAhGroup": ipsecSaAhGroup,
       "ipsecSaIpcompGroup": ipsecSaIpcompGroup,
       "ipsecSaErrorsGroup": ipsecSaErrorsGroup,
       "ipsecSaFailureTrapEnableGroup": ipsecSaFailureTrapEnableGroup,
       "ipsecSaTrapArgumentGroup": ipsecSaTrapArgumentGroup,
       "ipsecSaFailureTrapGroup": ipsecSaFailureTrapGroup,
       "saConformance": saConformance,
       "ipsecSaMonitorCompliance": ipsecSaMonitorCompliance}
)
