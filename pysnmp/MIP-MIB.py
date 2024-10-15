# SNMP MIB module (MIP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/MIP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:05:47 2024
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
    "TimeTicks",
    "Unsigned32",
    "experimental",
    "iso",
    "mib-2")

(DisplayString,
 RowStatus,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

mipMIB = ModuleIdentity(
    (1, 3, 6, 1, 2, 1, 44)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class RegistrationFlags(Bits, TextualConvention):
    status = "current"


# MIB Managed Objects in the order of their OIDs

_MipMIBObjects_ObjectIdentity = ObjectIdentity
mipMIBObjects = _MipMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 44, 1)
)
_MipSystem_ObjectIdentity = ObjectIdentity
mipSystem = _MipSystem_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 44, 1, 1)
)


class _MipEntities_Type(Bits):
    """Custom type mipEntities based on Bits"""
    namedValues = NamedValues(
        *(("foreignAgent", 1),
          ("homeAgent", 2),
          ("mobileNode", 0))
    )

_MipEntities_Type.__name__ = "Bits"
_MipEntities_Object = MibScalar
mipEntities = _MipEntities_Object(
    (1, 3, 6, 1, 2, 1, 44, 1, 1, 1),
    _MipEntities_Type()
)
mipEntities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mipEntities.setStatus("current")


class _MipEnable_Type(Integer32):
    """Custom type mipEnable based on Integer32"""
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


_MipEnable_Type.__name__ = "Integer32"
_MipEnable_Object = MibScalar
mipEnable = _MipEnable_Object(
    (1, 3, 6, 1, 2, 1, 44, 1, 1, 2),
    _MipEnable_Type()
)
mipEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mipEnable.setStatus("current")


class _MipEncapsulationSupported_Type(Bits):
    """Custom type mipEncapsulationSupported based on Bits"""
    namedValues = NamedValues(
        *(("gre", 1),
          ("ipInIp", 0),
          ("minEnc", 2),
          ("other", 3))
    )

_MipEncapsulationSupported_Type.__name__ = "Bits"
_MipEncapsulationSupported_Object = MibScalar
mipEncapsulationSupported = _MipEncapsulationSupported_Object(
    (1, 3, 6, 1, 2, 1, 44, 1, 1, 3),
    _MipEncapsulationSupported_Type()
)
mipEncapsulationSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mipEncapsulationSupported.setStatus("current")
_MipSecurity_ObjectIdentity = ObjectIdentity
mipSecurity = _MipSecurity_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 44, 1, 2)
)
_MipSecAssocTable_Object = MibTable
mipSecAssocTable = _MipSecAssocTable_Object(
    (1, 3, 6, 1, 2, 1, 44, 1, 2, 1)
)
if mibBuilder.loadTexts:
    mipSecAssocTable.setStatus("current")
_MipSecAssocEntry_Object = MibTableRow
mipSecAssocEntry = _MipSecAssocEntry_Object(
    (1, 3, 6, 1, 2, 1, 44, 1, 2, 1, 1)
)
mipSecAssocEntry.setIndexNames(
    (0, "MIP-MIB", "mipSecPeerAddress"),
    (0, "MIP-MIB", "mipSecSPI"),
)
if mibBuilder.loadTexts:
    mipSecAssocEntry.setStatus("current")
_MipSecPeerAddress_Type = IpAddress
_MipSecPeerAddress_Object = MibTableColumn
mipSecPeerAddress = _MipSecPeerAddress_Object(
    (1, 3, 6, 1, 2, 1, 44, 1, 2, 1, 1, 1),
    _MipSecPeerAddress_Type()
)
mipSecPeerAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mipSecPeerAddress.setStatus("current")


class _MipSecSPI_Type(Unsigned32):
    """Custom type mipSecSPI based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MipSecSPI_Type.__name__ = "Unsigned32"
_MipSecSPI_Object = MibTableColumn
mipSecSPI = _MipSecSPI_Object(
    (1, 3, 6, 1, 2, 1, 44, 1, 2, 1, 1, 2),
    _MipSecSPI_Type()
)
mipSecSPI.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mipSecSPI.setStatus("current")


class _MipSecAlgorithmType_Type(Integer32):
    """Custom type mipSecAlgorithmType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("md5", 2),
          ("other", 1))
    )


_MipSecAlgorithmType_Type.__name__ = "Integer32"
_MipSecAlgorithmType_Object = MibTableColumn
mipSecAlgorithmType = _MipSecAlgorithmType_Object(
    (1, 3, 6, 1, 2, 1, 44, 1, 2, 1, 1, 3),
    _MipSecAlgorithmType_Type()
)
mipSecAlgorithmType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mipSecAlgorithmType.setStatus("current")


class _MipSecAlgorithmMode_Type(Integer32):
    """Custom type mipSecAlgorithmMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("prefixSuffix", 2))
    )


_MipSecAlgorithmMode_Type.__name__ = "Integer32"
_MipSecAlgorithmMode_Object = MibTableColumn
mipSecAlgorithmMode = _MipSecAlgorithmMode_Object(
    (1, 3, 6, 1, 2, 1, 44, 1, 2, 1, 1, 4),
    _MipSecAlgorithmMode_Type()
)
mipSecAlgorithmMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mipSecAlgorithmMode.setStatus("current")


class _MipSecKey_Type(OctetString):
    """Custom type mipSecKey based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_MipSecKey_Type.__name__ = "OctetString"
_MipSecKey_Object = MibTableColumn
mipSecKey = _MipSecKey_Object(
    (1, 3, 6, 1, 2, 1, 44, 1, 2, 1, 1, 5),
    _MipSecKey_Type()
)
mipSecKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mipSecKey.setStatus("current")


class _MipSecReplayMethod_Type(Integer32):
    """Custom type mipSecReplayMethod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("nonces", 3),
          ("other", 1),
          ("timestamps", 2))
    )


_MipSecReplayMethod_Type.__name__ = "Integer32"
_MipSecReplayMethod_Object = MibTableColumn
mipSecReplayMethod = _MipSecReplayMethod_Object(
    (1, 3, 6, 1, 2, 1, 44, 1, 2, 1, 1, 6),
    _MipSecReplayMethod_Type()
)
mipSecReplayMethod.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mipSecReplayMethod.setStatus("current")
_MipSecTotalViolations_Type = Counter32
_MipSecTotalViolations_Object = MibScalar
mipSecTotalViolations = _MipSecTotalViolations_Object(
    (1, 3, 6, 1, 2, 1, 44, 1, 2, 2),
    _MipSecTotalViolations_Type()
)
mipSecTotalViolations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mipSecTotalViolations.setStatus("current")
_MipSecViolationTable_Object = MibTable
mipSecViolationTable = _MipSecViolationTable_Object(
    (1, 3, 6, 1, 2, 1, 44, 1, 2, 3)
)
if mibBuilder.loadTexts:
    mipSecViolationTable.setStatus("current")
_MipSecViolationEntry_Object = MibTableRow
mipSecViolationEntry = _MipSecViolationEntry_Object(
    (1, 3, 6, 1, 2, 1, 44, 1, 2, 3, 1)
)
mipSecViolationEntry.setIndexNames(
    (0, "MIP-MIB", "mipSecViolatorAddress"),
)
if mibBuilder.loadTexts:
    mipSecViolationEntry.setStatus("current")
_MipSecViolatorAddress_Type = IpAddress
_MipSecViolatorAddress_Object = MibTableColumn
mipSecViolatorAddress = _MipSecViolatorAddress_Object(
    (1, 3, 6, 1, 2, 1, 44, 1, 2, 3, 1, 1),
    _MipSecViolatorAddress_Type()
)
mipSecViolatorAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mipSecViolatorAddress.setStatus("current")
_MipSecViolationCounter_Type = Counter32
_MipSecViolationCounter_Object = MibTableColumn
mipSecViolationCounter = _MipSecViolationCounter_Object(
    (1, 3, 6, 1, 2, 1, 44, 1, 2, 3, 1, 2),
    _MipSecViolationCounter_Type()
)
mipSecViolationCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mipSecViolationCounter.setStatus("current")
_MipSecRecentViolationSPI_Type = Integer32
_MipSecRecentViolationSPI_Object = MibTableColumn
mipSecRecentViolationSPI = _MipSecRecentViolationSPI_Object(
    (1, 3, 6, 1, 2, 1, 44, 1, 2, 3, 1, 3),
    _MipSecRecentViolationSPI_Type()
)
mipSecRecentViolationSPI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mipSecRecentViolationSPI.setStatus("current")
_MipSecRecentViolationTime_Type = TimeStamp
_MipSecRecentViolationTime_Object = MibTableColumn
mipSecRecentViolationTime = _MipSecRecentViolationTime_Object(
    (1, 3, 6, 1, 2, 1, 44, 1, 2, 3, 1, 4),
    _MipSecRecentViolationTime_Type()
)
mipSecRecentViolationTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mipSecRecentViolationTime.setStatus("current")
_MipSecRecentViolationIDLow_Type = Integer32
_MipSecRecentViolationIDLow_Object = MibTableColumn
mipSecRecentViolationIDLow = _MipSecRecentViolationIDLow_Object(
    (1, 3, 6, 1, 2, 1, 44, 1, 2, 3, 1, 5),
    _MipSecRecentViolationIDLow_Type()
)
mipSecRecentViolationIDLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mipSecRecentViolationIDLow.setStatus("current")
_MipSecRecentViolationIDHigh_Type = Integer32
_MipSecRecentViolationIDHigh_Object = MibTableColumn
mipSecRecentViolationIDHigh = _MipSecRecentViolationIDHigh_Object(
    (1, 3, 6, 1, 2, 1, 44, 1, 2, 3, 1, 6),
    _MipSecRecentViolationIDHigh_Type()
)
mipSecRecentViolationIDHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mipSecRecentViolationIDHigh.setStatus("current")


class _MipSecRecentViolationReason_Type(Integer32):
    """Custom type mipSecRecentViolationReason based on Integer32"""
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
        *(("badAuthenticator", 2),
          ("badIdentifier", 3),
          ("badSPI", 4),
          ("missingSecurityExtension", 5),
          ("noMobilitySecurityAssociation", 1),
          ("other", 6))
    )


_MipSecRecentViolationReason_Type.__name__ = "Integer32"
_MipSecRecentViolationReason_Object = MibTableColumn
mipSecRecentViolationReason = _MipSecRecentViolationReason_Object(
    (1, 3, 6, 1, 2, 1, 44, 1, 2, 3, 1, 7),
    _MipSecRecentViolationReason_Type()
)
mipSecRecentViolationReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mipSecRecentViolationReason.setStatus("current")
_MipMN_ObjectIdentity = ObjectIdentity
mipMN = _MipMN_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 44, 1, 3)
)
_MnSystem_ObjectIdentity = ObjectIdentity
mnSystem = _MnSystem_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 44, 1, 3, 1)
)


class _MnState_Type(Integer32):
    """Custom type mnState based on Integer32"""
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
        *(("home", 1),
          ("isolated", 4),
          ("pending", 3),
          ("registered", 2),
          ("unknown", 5))
    )


_MnState_Type.__name__ = "Integer32"
_MnState_Object = MibScalar
mnState = _MnState_Object(
    (1, 3, 6, 1, 2, 1, 44, 1, 3, 1, 1),
    _MnState_Type()
)
mnState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mnState.setStatus("current")
_MnHomeAddress_Type = IpAddress
_MnHomeAddress_Object = MibScalar
mnHomeAddress = _MnHomeAddress_Object(
    (1, 3, 6, 1, 2, 1, 44, 1, 3, 1, 2),
    _MnHomeAddress_Type()
)
mnHomeAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mnHomeAddress.setStatus("current")
_MnHATable_Object = MibTable
mnHATable = _MnHATable_Object(
    (1, 3, 6, 1, 2, 1, 44, 1, 3, 1, 3)
)
if mibBuilder.loadTexts:
    mnHATable.setStatus("current")
_MnHAEntry_Object = MibTableRow
mnHAEntry = _MnHAEntry_Object(
    (1, 3, 6, 1, 2, 1, 44, 1, 3, 1, 3, 1)
)
mnHAEntry.setIndexNames(
    (0, "MIP-MIB", "mnHAAddress"),
)
if mibBuilder.loadTexts:
    mnHAEntry.setStatus("current")
_MnHAAddress_Type = IpAddress
_MnHAAddress_Object = MibTableColumn
mnHAAddress = _MnHAAddress_Object(
    (1, 3, 6, 1, 2, 1, 44, 1, 3, 1, 3, 1, 1),
    _MnHAAddress_Type()
)
mnHAAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mnHAAddress.setStatus("current")
_MnCurrentHA_Type = TruthValue
_MnCurrentHA_Object = MibTableColumn
mnCurrentHA = _MnCurrentHA_Object(
    (1, 3, 6, 1, 2, 1, 44, 1, 3, 1, 3, 1, 2),
    _MnCurrentHA_Type()
)
mnCurrentHA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mnCurrentHA.setStatus("current")
_MnHAStatus_Type = RowStatus
_MnHAStatus_Object = MibTableColumn
mnHAStatus = _MnHAStatus_Object(
    (1, 3, 6, 1, 2, 1, 44, 1, 3, 1, 3, 1, 3),
    _MnHAStatus_Type()
)
mnHAStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mnHAStatus.setStatus("current")
_MnDiscovery_ObjectIdentity = ObjectIdentity
mnDiscovery = _MnDiscovery_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 44, 1, 3, 2)
)
_MnFATable_Object = MibTable
mnFATable = _MnFATable_Object(
    (1, 3, 6, 1, 2, 1, 44, 1, 3, 2, 1)
)
if mibBuilder.loadTexts:
    mnFATable.setStatus("current")
_MnFAEntry_Object = MibTableRow
mnFAEntry = _MnFAEntry_Object(
    (1, 3, 6, 1, 2, 1, 44, 1, 3, 2, 1, 1)
)
mnFAEntry.setIndexNames(
    (0, "MIP-MIB", "mnFAAddress"),
    (0, "MIP-MIB", "mnCOA"),
)
if mibBuilder.loadTexts:
    mnFAEntry.setStatus("current")
_MnFAAddress_Type = IpAddress
_MnFAAddress_Object = MibTableColumn
mnFAAddress = _MnFAAddress_Object(
    (1, 3, 6, 1, 2, 1, 44, 1, 3, 2, 1, 1, 1),
    _MnFAAddress_Type()
)
mnFAAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mnFAAddress.setStatus("current")
_MnCOA_Type = IpAddress
_MnCOA_Object = MibTableColumn
mnCOA = _MnCOA_Object(
    (1, 3, 6, 1, 2, 1, 44, 1, 3, 2, 1, 1, 2),
    _MnCOA_Type()
)
mnCOA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mnCOA.setStatus("current")
_MnRecentAdvReceived_ObjectIdentity = ObjectIdentity
mnRecentAdvReceived = _MnRecentAdvReceived_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 44, 1, 3, 2, 2)
)
_MnAdvSourceAddress_Type = IpAddress
_MnAdvSourceAddress_Object = MibScalar
mnAdvSourceAddress = _MnAdvSourceAddress_Object(
    (1, 3, 6, 1, 2, 1, 44, 1, 3, 2, 2, 1),
    _MnAdvSourceAddress_Type()
)
mnAdvSourceAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mnAdvSourceAddress.setStatus("current")


class _MnAdvSequence_Type(Integer32):
    """Custom type mnAdvSequence based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MnAdvSequence_Type.__name__ = "Integer32"
_MnAdvSequence_Object = MibScalar
mnAdvSequence = _MnAdvSequence_Object(
    (1, 3, 6, 1, 2, 1, 44, 1, 3, 2, 2, 2),
    _MnAdvSequence_Type()
)
mnAdvSequence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mnAdvSequence.setStatus("current")


class _MnAdvFlags_Type(Bits):
    """Custom type mnAdvFlags based on Bits"""
    namedValues = NamedValues(
        *(("busy", 5),
          ("foreignAgent", 3),
          ("gre", 1),
          ("homeAgent", 4),
          ("minEnc", 2),
          ("regRequired", 6),
          ("vjCompression", 0))
    )

_MnAdvFlags_Type.__name__ = "Bits"
_MnAdvFlags_Object = MibScalar
mnAdvFlags = _MnAdvFlags_Object(
    (1, 3, 6, 1, 2, 1, 44, 1, 3, 2, 2, 3),
    _MnAdvFlags_Type()
)
mnAdvFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mnAdvFlags.setStatus("current")


class _MnAdvMaxRegLifetime_Type(Integer32):
    """Custom type mnAdvMaxRegLifetime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MnAdvMaxRegLifetime_Type.__name__ = "Integer32"
_MnAdvMaxRegLifetime_Object = MibScalar
mnAdvMaxRegLifetime = _MnAdvMaxRegLifetime_Object(
    (1, 3, 6, 1, 2, 1, 44, 1, 3, 2, 2, 4),
    _MnAdvMaxRegLifetime_Type()
)
mnAdvMaxRegLifetime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mnAdvMaxRegLifetime.setStatus("current")
if mibBuilder.loadTexts:
    mnAdvMaxRegLifetime.setUnits("seconds")


class _MnAdvMaxAdvLifetime_Type(Integer32):
    """Custom type mnAdvMaxAdvLifetime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MnAdvMaxAdvLifetime_Type.__name__ = "Integer32"
_MnAdvMaxAdvLifetime_Object = MibScalar
mnAdvMaxAdvLifetime = _MnAdvMaxAdvLifetime_Object(
    (1, 3, 6, 1, 2, 1, 44, 1, 3, 2, 2, 5),
    _MnAdvMaxAdvLifetime_Type()
)
mnAdvMaxAdvLifetime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mnAdvMaxAdvLifetime.setStatus("current")
if mibBuilder.loadTexts:
    mnAdvMaxAdvLifetime.setUnits("seconds")
_MnAdvTimeReceived_Type = TimeStamp
_MnAdvTimeReceived_Object = MibScalar
mnAdvTimeReceived = _MnAdvTimeReceived_Object(
    (1, 3, 6, 1, 2, 1, 44, 1, 3, 2, 2, 6),
    _MnAdvTimeReceived_Type()
)
mnAdvTimeReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mnAdvTimeReceived.setStatus("current")
_MnSolicitationsSent_Type = Counter32
_MnSolicitationsSent_Object = MibScalar
mnSolicitationsSent = _MnSolicitationsSent_Object(
    (1, 3, 6, 1, 2, 1, 44, 1, 3, 2, 3),
    _MnSolicitationsSent_Type()
)
mnSolicitationsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mnSolicitationsSent.setStatus("current")
_MnAdvertisementsReceived_Type = Counter32
_MnAdvertisementsReceived_Object = MibScalar
mnAdvertisementsReceived = _MnAdvertisementsReceived_Object(
    (1, 3, 6, 1, 2, 1, 44, 1, 3, 2, 4),
    _MnAdvertisementsReceived_Type()
)
mnAdvertisementsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mnAdvertisementsReceived.setStatus("current")
_MnAdvsDroppedInvalidExtension_Type = Counter32
_MnAdvsDroppedInvalidExtension_Object = MibScalar
mnAdvsDroppedInvalidExtension = _MnAdvsDroppedInvalidExtension_Object(
    (1, 3, 6, 1, 2, 1, 44, 1, 3, 2, 5),
    _MnAdvsDroppedInvalidExtension_Type()
)
mnAdvsDroppedInvalidExtension.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mnAdvsDroppedInvalidExtension.setStatus("current")
_MnAdvsIgnoredUnknownExtension_Type = Counter32
_MnAdvsIgnoredUnknownExtension_Object = MibScalar
mnAdvsIgnoredUnknownExtension = _MnAdvsIgnoredUnknownExtension_Object(
    (1, 3, 6, 1, 2, 1, 44, 1, 3, 2, 6),
    _MnAdvsIgnoredUnknownExtension_Type()
)
mnAdvsIgnoredUnknownExtension.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mnAdvsIgnoredUnknownExtension.setStatus("current")
_MnMoveFromHAToFA_Type = Counter32
_MnMoveFromHAToFA_Object = MibScalar
mnMoveFromHAToFA = _MnMoveFromHAToFA_Object(
    (1, 3, 6, 1, 2, 1, 44, 1, 3, 2, 7),
    _MnMoveFromHAToFA_Type()
)
mnMoveFromHAToFA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mnMoveFromHAToFA.setStatus("current")
_MnMoveFromFAToFA_Type = Counter32
_MnMoveFromFAToFA_Object = MibScalar
mnMoveFromFAToFA = _MnMoveFromFAToFA_Object(
    (1, 3, 6, 1, 2, 1, 44, 1, 3, 2, 8),
    _MnMoveFromFAToFA_Type()
)
mnMoveFromFAToFA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mnMoveFromFAToFA.setStatus("current")
_MnMoveFromFAToHA_Type = Counter32
_MnMoveFromFAToHA_Object = MibScalar
mnMoveFromFAToHA = _MnMoveFromFAToHA_Object(
    (1, 3, 6, 1, 2, 1, 44, 1, 3, 2, 9),
    _MnMoveFromFAToHA_Type()
)
mnMoveFromFAToHA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mnMoveFromFAToHA.setStatus("current")
_MnGratuitousARPsSend_Type = Counter32
_MnGratuitousARPsSend_Object = MibScalar
mnGratuitousARPsSend = _MnGratuitousARPsSend_Object(
    (1, 3, 6, 1, 2, 1, 44, 1, 3, 2, 10),
    _MnGratuitousARPsSend_Type()
)
mnGratuitousARPsSend.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mnGratuitousARPsSend.setStatus("current")
_MnAgentRebootsDectected_Type = Counter32
_MnAgentRebootsDectected_Object = MibScalar
mnAgentRebootsDectected = _MnAgentRebootsDectected_Object(
    (1, 3, 6, 1, 2, 1, 44, 1, 3, 2, 11),
    _MnAgentRebootsDectected_Type()
)
mnAgentRebootsDectected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mnAgentRebootsDectected.setStatus("current")
_MnRegistration_ObjectIdentity = ObjectIdentity
mnRegistration = _MnRegistration_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 44, 1, 3, 3)
)
_MnRegistrationTable_Object = MibTable
mnRegistrationTable = _MnRegistrationTable_Object(
    (1, 3, 6, 1, 2, 1, 44, 1, 3, 3, 1)
)
if mibBuilder.loadTexts:
    mnRegistrationTable.setStatus("current")
_MnRegistrationEntry_Object = MibTableRow
mnRegistrationEntry = _MnRegistrationEntry_Object(
    (1, 3, 6, 1, 2, 1, 44, 1, 3, 3, 1, 1)
)
mnRegistrationEntry.setIndexNames(
    (0, "MIP-MIB", "mnRegAgentAddress"),
    (0, "MIP-MIB", "mnRegCOA"),
)
if mibBuilder.loadTexts:
    mnRegistrationEntry.setStatus("current")
_MnRegAgentAddress_Type = IpAddress
_MnRegAgentAddress_Object = MibTableColumn
mnRegAgentAddress = _MnRegAgentAddress_Object(
    (1, 3, 6, 1, 2, 1, 44, 1, 3, 3, 1, 1, 1),
    _MnRegAgentAddress_Type()
)
mnRegAgentAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mnRegAgentAddress.setStatus("current")
_MnRegCOA_Type = IpAddress
_MnRegCOA_Object = MibTableColumn
mnRegCOA = _MnRegCOA_Object(
    (1, 3, 6, 1, 2, 1, 44, 1, 3, 3, 1, 1, 2),
    _MnRegCOA_Type()
)
mnRegCOA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mnRegCOA.setStatus("current")
_MnRegFlags_Type = RegistrationFlags
_MnRegFlags_Object = MibTableColumn
mnRegFlags = _MnRegFlags_Object(
    (1, 3, 6, 1, 2, 1, 44, 1, 3, 3, 1, 1, 3),
    _MnRegFlags_Type()
)
mnRegFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mnRegFlags.setStatus("current")
_MnRegIDLow_Type = Integer32
_MnRegIDLow_Object = MibTableColumn
mnRegIDLow = _MnRegIDLow_Object(
    (1, 3, 6, 1, 2, 1, 44, 1, 3, 3, 1, 1, 4),
    _MnRegIDLow_Type()
)
mnRegIDLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mnRegIDLow.setStatus("current")
_MnRegIDHigh_Type = Integer32
_MnRegIDHigh_Object = MibTableColumn
mnRegIDHigh = _MnRegIDHigh_Object(
    (1, 3, 6, 1, 2, 1, 44, 1, 3, 3, 1, 1, 5),
    _MnRegIDHigh_Type()
)
mnRegIDHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mnRegIDHigh.setStatus("current")
_MnRegTimeRequested_Type = Integer32
_MnRegTimeRequested_Object = MibTableColumn
mnRegTimeRequested = _MnRegTimeRequested_Object(
    (1, 3, 6, 1, 2, 1, 44, 1, 3, 3, 1, 1, 6),
    _MnRegTimeRequested_Type()
)
mnRegTimeRequested.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mnRegTimeRequested.setStatus("current")
if mibBuilder.loadTexts:
    mnRegTimeRequested.setUnits("seconds")
_MnRegTimeRemaining_Type = Gauge32
_MnRegTimeRemaining_Object = MibTableColumn
mnRegTimeRemaining = _MnRegTimeRemaining_Object(
    (1, 3, 6, 1, 2, 1, 44, 1, 3, 3, 1, 1, 7),
    _MnRegTimeRemaining_Type()
)
mnRegTimeRemaining.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mnRegTimeRemaining.setStatus("current")
if mibBuilder.loadTexts:
    mnRegTimeRemaining.setUnits("seconds")
_MnRegTimeSent_Type = TimeStamp
_MnRegTimeSent_Object = MibTableColumn
mnRegTimeSent = _MnRegTimeSent_Object(
    (1, 3, 6, 1, 2, 1, 44, 1, 3, 3, 1, 1, 8),
    _MnRegTimeSent_Type()
)
mnRegTimeSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mnRegTimeSent.setStatus("current")
_MnRegIsAccepted_Type = TruthValue
_MnRegIsAccepted_Object = MibTableColumn
mnRegIsAccepted = _MnRegIsAccepted_Object(
    (1, 3, 6, 1, 2, 1, 44, 1, 3, 3, 1, 1, 9),
    _MnRegIsAccepted_Type()
)
mnRegIsAccepted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mnRegIsAccepted.setStatus("current")
_MnCOAIsLocal_Type = TruthValue
_MnCOAIsLocal_Object = MibTableColumn
mnCOAIsLocal = _MnCOAIsLocal_Object(
    (1, 3, 6, 1, 2, 1, 44, 1, 3, 3, 1, 1, 10),
    _MnCOAIsLocal_Type()
)
mnCOAIsLocal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mnCOAIsLocal.setStatus("current")
_MnRegRequestsSent_Type = Counter32
_MnRegRequestsSent_Object = MibScalar
mnRegRequestsSent = _MnRegRequestsSent_Object(
    (1, 3, 6, 1, 2, 1, 44, 1, 3, 3, 2),
    _MnRegRequestsSent_Type()
)
mnRegRequestsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mnRegRequestsSent.setStatus("current")
_MnDeRegRequestsSent_Type = Counter32
_MnDeRegRequestsSent_Object = MibScalar
mnDeRegRequestsSent = _MnDeRegRequestsSent_Object(
    (1, 3, 6, 1, 2, 1, 44, 1, 3, 3, 3),
    _MnDeRegRequestsSent_Type()
)
mnDeRegRequestsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mnDeRegRequestsSent.setStatus("current")
_MnRegRepliesRecieved_Type = Counter32
_MnRegRepliesRecieved_Object = MibScalar
mnRegRepliesRecieved = _MnRegRepliesRecieved_Object(
    (1, 3, 6, 1, 2, 1, 44, 1, 3, 3, 4),
    _MnRegRepliesRecieved_Type()
)
mnRegRepliesRecieved.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mnRegRepliesRecieved.setStatus("current")
_MnDeRegRepliesRecieved_Type = Counter32
_MnDeRegRepliesRecieved_Object = MibScalar
mnDeRegRepliesRecieved = _MnDeRegRepliesRecieved_Object(
    (1, 3, 6, 1, 2, 1, 44, 1, 3, 3, 5),
    _MnDeRegRepliesRecieved_Type()
)
mnDeRegRepliesRecieved.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mnDeRegRepliesRecieved.setStatus("current")
_MnRepliesInvalidHomeAddress_Type = Counter32
_MnRepliesInvalidHomeAddress_Object = MibScalar
mnRepliesInvalidHomeAddress = _MnRepliesInvalidHomeAddress_Object(
    (1, 3, 6, 1, 2, 1, 44, 1, 3, 3, 6),
    _MnRepliesInvalidHomeAddress_Type()
)
mnRepliesInvalidHomeAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mnRepliesInvalidHomeAddress.setStatus("current")
_MnRepliesUnknownHA_Type = Counter32
_MnRepliesUnknownHA_Object = MibScalar
mnRepliesUnknownHA = _MnRepliesUnknownHA_Object(
    (1, 3, 6, 1, 2, 1, 44, 1, 3, 3, 7),
    _MnRepliesUnknownHA_Type()
)
mnRepliesUnknownHA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mnRepliesUnknownHA.setStatus("current")
_MnRepliesUnknownFA_Type = Counter32
_MnRepliesUnknownFA_Object = MibScalar
mnRepliesUnknownFA = _MnRepliesUnknownFA_Object(
    (1, 3, 6, 1, 2, 1, 44, 1, 3, 3, 8),
    _MnRepliesUnknownFA_Type()
)
mnRepliesUnknownFA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mnRepliesUnknownFA.setStatus("current")
_MnRepliesInvalidID_Type = Counter32
_MnRepliesInvalidID_Object = MibScalar
mnRepliesInvalidID = _MnRepliesInvalidID_Object(
    (1, 3, 6, 1, 2, 1, 44, 1, 3, 3, 9),
    _MnRepliesInvalidID_Type()
)
mnRepliesInvalidID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mnRepliesInvalidID.setStatus("current")
_MnRepliesDroppedInvalidExtension_Type = Counter32
_MnRepliesDroppedInvalidExtension_Object = MibScalar
mnRepliesDroppedInvalidExtension = _MnRepliesDroppedInvalidExtension_Object(
    (1, 3, 6, 1, 2, 1, 44, 1, 3, 3, 10),
    _MnRepliesDroppedInvalidExtension_Type()
)
mnRepliesDroppedInvalidExtension.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mnRepliesDroppedInvalidExtension.setStatus("current")
_MnRepliesIgnoredUnknownExtension_Type = Counter32
_MnRepliesIgnoredUnknownExtension_Object = MibScalar
mnRepliesIgnoredUnknownExtension = _MnRepliesIgnoredUnknownExtension_Object(
    (1, 3, 6, 1, 2, 1, 44, 1, 3, 3, 11),
    _MnRepliesIgnoredUnknownExtension_Type()
)
mnRepliesIgnoredUnknownExtension.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mnRepliesIgnoredUnknownExtension.setStatus("current")
_MnRepliesHAAuthenticationFailure_Type = Counter32
_MnRepliesHAAuthenticationFailure_Object = MibScalar
mnRepliesHAAuthenticationFailure = _MnRepliesHAAuthenticationFailure_Object(
    (1, 3, 6, 1, 2, 1, 44, 1, 3, 3, 12),
    _MnRepliesHAAuthenticationFailure_Type()
)
mnRepliesHAAuthenticationFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mnRepliesHAAuthenticationFailure.setStatus("current")
_MnRepliesFAAuthenticationFailure_Type = Counter32
_MnRepliesFAAuthenticationFailure_Object = MibScalar
mnRepliesFAAuthenticationFailure = _MnRepliesFAAuthenticationFailure_Object(
    (1, 3, 6, 1, 2, 1, 44, 1, 3, 3, 13),
    _MnRepliesFAAuthenticationFailure_Type()
)
mnRepliesFAAuthenticationFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mnRepliesFAAuthenticationFailure.setStatus("current")
_MnRegRequestsAccepted_Type = Counter32
_MnRegRequestsAccepted_Object = MibScalar
mnRegRequestsAccepted = _MnRegRequestsAccepted_Object(
    (1, 3, 6, 1, 2, 1, 44, 1, 3, 3, 14),
    _MnRegRequestsAccepted_Type()
)
mnRegRequestsAccepted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mnRegRequestsAccepted.setStatus("current")
_MnRegRequestsDeniedByHA_Type = Counter32
_MnRegRequestsDeniedByHA_Object = MibScalar
mnRegRequestsDeniedByHA = _MnRegRequestsDeniedByHA_Object(
    (1, 3, 6, 1, 2, 1, 44, 1, 3, 3, 15),
    _MnRegRequestsDeniedByHA_Type()
)
mnRegRequestsDeniedByHA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mnRegRequestsDeniedByHA.setStatus("current")
_MnRegRequestsDeniedByFA_Type = Counter32
_MnRegRequestsDeniedByFA_Object = MibScalar
mnRegRequestsDeniedByFA = _MnRegRequestsDeniedByFA_Object(
    (1, 3, 6, 1, 2, 1, 44, 1, 3, 3, 16),
    _MnRegRequestsDeniedByFA_Type()
)
mnRegRequestsDeniedByFA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mnRegRequestsDeniedByFA.setStatus("current")
_MnRegRequestsDeniedByHADueToID_Type = Counter32
_MnRegRequestsDeniedByHADueToID_Object = MibScalar
mnRegRequestsDeniedByHADueToID = _MnRegRequestsDeniedByHADueToID_Object(
    (1, 3, 6, 1, 2, 1, 44, 1, 3, 3, 17),
    _MnRegRequestsDeniedByHADueToID_Type()
)
mnRegRequestsDeniedByHADueToID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mnRegRequestsDeniedByHADueToID.setStatus("current")
_MnRegRequestsWithDirectedBroadcast_Type = Counter32
_MnRegRequestsWithDirectedBroadcast_Object = MibScalar
mnRegRequestsWithDirectedBroadcast = _MnRegRequestsWithDirectedBroadcast_Object(
    (1, 3, 6, 1, 2, 1, 44, 1, 3, 3, 18),
    _MnRegRequestsWithDirectedBroadcast_Type()
)
mnRegRequestsWithDirectedBroadcast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mnRegRequestsWithDirectedBroadcast.setStatus("current")
_MipMA_ObjectIdentity = ObjectIdentity
mipMA = _MipMA_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 44, 1, 4)
)
_MaAdvertisement_ObjectIdentity = ObjectIdentity
maAdvertisement = _MaAdvertisement_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 44, 1, 4, 2)
)
_MaAdvConfigTable_Object = MibTable
maAdvConfigTable = _MaAdvConfigTable_Object(
    (1, 3, 6, 1, 2, 1, 44, 1, 4, 2, 1)
)
if mibBuilder.loadTexts:
    maAdvConfigTable.setStatus("current")
_MaAdvConfigEntry_Object = MibTableRow
maAdvConfigEntry = _MaAdvConfigEntry_Object(
    (1, 3, 6, 1, 2, 1, 44, 1, 4, 2, 1, 1)
)
maAdvConfigEntry.setIndexNames(
    (0, "MIP-MIB", "maInterfaceAddress"),
)
if mibBuilder.loadTexts:
    maAdvConfigEntry.setStatus("current")
_MaInterfaceAddress_Type = IpAddress
_MaInterfaceAddress_Object = MibTableColumn
maInterfaceAddress = _MaInterfaceAddress_Object(
    (1, 3, 6, 1, 2, 1, 44, 1, 4, 2, 1, 1, 1),
    _MaInterfaceAddress_Type()
)
maInterfaceAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    maInterfaceAddress.setStatus("current")


class _MaAdvMaxRegLifetime_Type(Integer32):
    """Custom type maAdvMaxRegLifetime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MaAdvMaxRegLifetime_Type.__name__ = "Integer32"
_MaAdvMaxRegLifetime_Object = MibTableColumn
maAdvMaxRegLifetime = _MaAdvMaxRegLifetime_Object(
    (1, 3, 6, 1, 2, 1, 44, 1, 4, 2, 1, 1, 2),
    _MaAdvMaxRegLifetime_Type()
)
maAdvMaxRegLifetime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    maAdvMaxRegLifetime.setStatus("current")
if mibBuilder.loadTexts:
    maAdvMaxRegLifetime.setUnits("seconds")
_MaAdvPrefixLengthInclusion_Type = TruthValue
_MaAdvPrefixLengthInclusion_Object = MibTableColumn
maAdvPrefixLengthInclusion = _MaAdvPrefixLengthInclusion_Object(
    (1, 3, 6, 1, 2, 1, 44, 1, 4, 2, 1, 1, 3),
    _MaAdvPrefixLengthInclusion_Type()
)
maAdvPrefixLengthInclusion.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    maAdvPrefixLengthInclusion.setStatus("current")
_MaAdvAddress_Type = IpAddress
_MaAdvAddress_Object = MibTableColumn
maAdvAddress = _MaAdvAddress_Object(
    (1, 3, 6, 1, 2, 1, 44, 1, 4, 2, 1, 1, 4),
    _MaAdvAddress_Type()
)
maAdvAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    maAdvAddress.setStatus("current")


class _MaAdvMaxInterval_Type(Integer32):
    """Custom type maAdvMaxInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 1800),
    )


_MaAdvMaxInterval_Type.__name__ = "Integer32"
_MaAdvMaxInterval_Object = MibTableColumn
maAdvMaxInterval = _MaAdvMaxInterval_Object(
    (1, 3, 6, 1, 2, 1, 44, 1, 4, 2, 1, 1, 5),
    _MaAdvMaxInterval_Type()
)
maAdvMaxInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    maAdvMaxInterval.setStatus("current")
if mibBuilder.loadTexts:
    maAdvMaxInterval.setUnits("seconds")


class _MaAdvMinInterval_Type(Integer32):
    """Custom type maAdvMinInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 1800),
    )


_MaAdvMinInterval_Type.__name__ = "Integer32"
_MaAdvMinInterval_Object = MibTableColumn
maAdvMinInterval = _MaAdvMinInterval_Object(
    (1, 3, 6, 1, 2, 1, 44, 1, 4, 2, 1, 1, 6),
    _MaAdvMinInterval_Type()
)
maAdvMinInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    maAdvMinInterval.setStatus("current")
if mibBuilder.loadTexts:
    maAdvMinInterval.setUnits("seconds")


class _MaAdvMaxAdvLifetime_Type(Integer32):
    """Custom type maAdvMaxAdvLifetime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 9000),
    )


_MaAdvMaxAdvLifetime_Type.__name__ = "Integer32"
_MaAdvMaxAdvLifetime_Object = MibTableColumn
maAdvMaxAdvLifetime = _MaAdvMaxAdvLifetime_Object(
    (1, 3, 6, 1, 2, 1, 44, 1, 4, 2, 1, 1, 7),
    _MaAdvMaxAdvLifetime_Type()
)
maAdvMaxAdvLifetime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    maAdvMaxAdvLifetime.setStatus("current")
if mibBuilder.loadTexts:
    maAdvMaxAdvLifetime.setUnits("seconds")


class _MaAdvResponseSolicitationOnly_Type(TruthValue):
    """Custom type maAdvResponseSolicitationOnly based on TruthValue"""


_MaAdvResponseSolicitationOnly_Object = MibTableColumn
maAdvResponseSolicitationOnly = _MaAdvResponseSolicitationOnly_Object(
    (1, 3, 6, 1, 2, 1, 44, 1, 4, 2, 1, 1, 8),
    _MaAdvResponseSolicitationOnly_Type()
)
maAdvResponseSolicitationOnly.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    maAdvResponseSolicitationOnly.setStatus("current")
_MaAdvStatus_Type = RowStatus
_MaAdvStatus_Object = MibTableColumn
maAdvStatus = _MaAdvStatus_Object(
    (1, 3, 6, 1, 2, 1, 44, 1, 4, 2, 1, 1, 9),
    _MaAdvStatus_Type()
)
maAdvStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    maAdvStatus.setStatus("current")
_MaAdvertisementsSent_Type = Counter32
_MaAdvertisementsSent_Object = MibScalar
maAdvertisementsSent = _MaAdvertisementsSent_Object(
    (1, 3, 6, 1, 2, 1, 44, 1, 4, 2, 2),
    _MaAdvertisementsSent_Type()
)
maAdvertisementsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maAdvertisementsSent.setStatus("current")
_MaAdvsSentForSolicitation_Type = Counter32
_MaAdvsSentForSolicitation_Object = MibScalar
maAdvsSentForSolicitation = _MaAdvsSentForSolicitation_Object(
    (1, 3, 6, 1, 2, 1, 44, 1, 4, 2, 3),
    _MaAdvsSentForSolicitation_Type()
)
maAdvsSentForSolicitation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maAdvsSentForSolicitation.setStatus("current")
_MaSolicitationsReceived_Type = Counter32
_MaSolicitationsReceived_Object = MibScalar
maSolicitationsReceived = _MaSolicitationsReceived_Object(
    (1, 3, 6, 1, 2, 1, 44, 1, 4, 2, 4),
    _MaSolicitationsReceived_Type()
)
maSolicitationsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maSolicitationsReceived.setStatus("current")
_MipFA_ObjectIdentity = ObjectIdentity
mipFA = _MipFA_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 44, 1, 5)
)
_FaSystem_ObjectIdentity = ObjectIdentity
faSystem = _FaSystem_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 44, 1, 5, 1)
)
_FaCOATable_Object = MibTable
faCOATable = _FaCOATable_Object(
    (1, 3, 6, 1, 2, 1, 44, 1, 5, 1, 1)
)
if mibBuilder.loadTexts:
    faCOATable.setStatus("current")
_FaCOAEntry_Object = MibTableRow
faCOAEntry = _FaCOAEntry_Object(
    (1, 3, 6, 1, 2, 1, 44, 1, 5, 1, 1, 1)
)
faCOAEntry.setIndexNames(
    (0, "MIP-MIB", "faSupportedCOA"),
)
if mibBuilder.loadTexts:
    faCOAEntry.setStatus("current")
_FaSupportedCOA_Type = IpAddress
_FaSupportedCOA_Object = MibTableColumn
faSupportedCOA = _FaSupportedCOA_Object(
    (1, 3, 6, 1, 2, 1, 44, 1, 5, 1, 1, 1, 1),
    _FaSupportedCOA_Type()
)
faSupportedCOA.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    faSupportedCOA.setStatus("current")
_FaCOAStatus_Type = RowStatus
_FaCOAStatus_Object = MibTableColumn
faCOAStatus = _FaCOAStatus_Object(
    (1, 3, 6, 1, 2, 1, 44, 1, 5, 1, 1, 1, 2),
    _FaCOAStatus_Type()
)
faCOAStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    faCOAStatus.setStatus("current")
_FaAdvertisement_ObjectIdentity = ObjectIdentity
faAdvertisement = _FaAdvertisement_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 44, 1, 5, 2)
)
_FaIsBusy_Type = TruthValue
_FaIsBusy_Object = MibScalar
faIsBusy = _FaIsBusy_Object(
    (1, 3, 6, 1, 2, 1, 44, 1, 5, 2, 1),
    _FaIsBusy_Type()
)
faIsBusy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    faIsBusy.setStatus("current")
_FaRegistrationRequired_Type = TruthValue
_FaRegistrationRequired_Object = MibScalar
faRegistrationRequired = _FaRegistrationRequired_Object(
    (1, 3, 6, 1, 2, 1, 44, 1, 5, 2, 2),
    _FaRegistrationRequired_Type()
)
faRegistrationRequired.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    faRegistrationRequired.setStatus("current")
_FaRegistration_ObjectIdentity = ObjectIdentity
faRegistration = _FaRegistration_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 44, 1, 5, 3)
)
_FaVisitorTable_Object = MibTable
faVisitorTable = _FaVisitorTable_Object(
    (1, 3, 6, 1, 2, 1, 44, 1, 5, 3, 1)
)
if mibBuilder.loadTexts:
    faVisitorTable.setStatus("current")
_FaVisitorEntry_Object = MibTableRow
faVisitorEntry = _FaVisitorEntry_Object(
    (1, 3, 6, 1, 2, 1, 44, 1, 5, 3, 1, 1)
)
faVisitorEntry.setIndexNames(
    (0, "MIP-MIB", "faVisitorIPAddress"),
)
if mibBuilder.loadTexts:
    faVisitorEntry.setStatus("current")
_FaVisitorIPAddress_Type = IpAddress
_FaVisitorIPAddress_Object = MibTableColumn
faVisitorIPAddress = _FaVisitorIPAddress_Object(
    (1, 3, 6, 1, 2, 1, 44, 1, 5, 3, 1, 1, 1),
    _FaVisitorIPAddress_Type()
)
faVisitorIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    faVisitorIPAddress.setStatus("current")
_FaVisitorHomeAddress_Type = IpAddress
_FaVisitorHomeAddress_Object = MibTableColumn
faVisitorHomeAddress = _FaVisitorHomeAddress_Object(
    (1, 3, 6, 1, 2, 1, 44, 1, 5, 3, 1, 1, 2),
    _FaVisitorHomeAddress_Type()
)
faVisitorHomeAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    faVisitorHomeAddress.setStatus("current")
_FaVisitorHomeAgentAddress_Type = IpAddress
_FaVisitorHomeAgentAddress_Object = MibTableColumn
faVisitorHomeAgentAddress = _FaVisitorHomeAgentAddress_Object(
    (1, 3, 6, 1, 2, 1, 44, 1, 5, 3, 1, 1, 3),
    _FaVisitorHomeAgentAddress_Type()
)
faVisitorHomeAgentAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    faVisitorHomeAgentAddress.setStatus("current")
_FaVisitorTimeGranted_Type = Integer32
_FaVisitorTimeGranted_Object = MibTableColumn
faVisitorTimeGranted = _FaVisitorTimeGranted_Object(
    (1, 3, 6, 1, 2, 1, 44, 1, 5, 3, 1, 1, 4),
    _FaVisitorTimeGranted_Type()
)
faVisitorTimeGranted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    faVisitorTimeGranted.setStatus("current")
if mibBuilder.loadTexts:
    faVisitorTimeGranted.setUnits("seconds")
_FaVisitorTimeRemaining_Type = Gauge32
_FaVisitorTimeRemaining_Object = MibTableColumn
faVisitorTimeRemaining = _FaVisitorTimeRemaining_Object(
    (1, 3, 6, 1, 2, 1, 44, 1, 5, 3, 1, 1, 5),
    _FaVisitorTimeRemaining_Type()
)
faVisitorTimeRemaining.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    faVisitorTimeRemaining.setStatus("current")
if mibBuilder.loadTexts:
    faVisitorTimeRemaining.setUnits("seconds")
_FaVisitorRegFlags_Type = RegistrationFlags
_FaVisitorRegFlags_Object = MibTableColumn
faVisitorRegFlags = _FaVisitorRegFlags_Object(
    (1, 3, 6, 1, 2, 1, 44, 1, 5, 3, 1, 1, 6),
    _FaVisitorRegFlags_Type()
)
faVisitorRegFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    faVisitorRegFlags.setStatus("current")
_FaVisitorRegIDLow_Type = Integer32
_FaVisitorRegIDLow_Object = MibTableColumn
faVisitorRegIDLow = _FaVisitorRegIDLow_Object(
    (1, 3, 6, 1, 2, 1, 44, 1, 5, 3, 1, 1, 7),
    _FaVisitorRegIDLow_Type()
)
faVisitorRegIDLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    faVisitorRegIDLow.setStatus("current")
_FaVisitorRegIDHigh_Type = Integer32
_FaVisitorRegIDHigh_Object = MibTableColumn
faVisitorRegIDHigh = _FaVisitorRegIDHigh_Object(
    (1, 3, 6, 1, 2, 1, 44, 1, 5, 3, 1, 1, 8),
    _FaVisitorRegIDHigh_Type()
)
faVisitorRegIDHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    faVisitorRegIDHigh.setStatus("current")
_FaVisitorRegIsAccepted_Type = TruthValue
_FaVisitorRegIsAccepted_Object = MibTableColumn
faVisitorRegIsAccepted = _FaVisitorRegIsAccepted_Object(
    (1, 3, 6, 1, 2, 1, 44, 1, 5, 3, 1, 1, 9),
    _FaVisitorRegIsAccepted_Type()
)
faVisitorRegIsAccepted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    faVisitorRegIsAccepted.setStatus("current")
_FaRegRequestsReceived_Type = Counter32
_FaRegRequestsReceived_Object = MibScalar
faRegRequestsReceived = _FaRegRequestsReceived_Object(
    (1, 3, 6, 1, 2, 1, 44, 1, 5, 3, 2),
    _FaRegRequestsReceived_Type()
)
faRegRequestsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    faRegRequestsReceived.setStatus("current")
_FaRegRequestsRelayed_Type = Counter32
_FaRegRequestsRelayed_Object = MibScalar
faRegRequestsRelayed = _FaRegRequestsRelayed_Object(
    (1, 3, 6, 1, 2, 1, 44, 1, 5, 3, 3),
    _FaRegRequestsRelayed_Type()
)
faRegRequestsRelayed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    faRegRequestsRelayed.setStatus("current")
_FaReasonUnspecified_Type = Counter32
_FaReasonUnspecified_Object = MibScalar
faReasonUnspecified = _FaReasonUnspecified_Object(
    (1, 3, 6, 1, 2, 1, 44, 1, 5, 3, 4),
    _FaReasonUnspecified_Type()
)
faReasonUnspecified.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    faReasonUnspecified.setStatus("current")
_FaAdmProhibited_Type = Counter32
_FaAdmProhibited_Object = MibScalar
faAdmProhibited = _FaAdmProhibited_Object(
    (1, 3, 6, 1, 2, 1, 44, 1, 5, 3, 5),
    _FaAdmProhibited_Type()
)
faAdmProhibited.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    faAdmProhibited.setStatus("current")
_FaInsufficientResource_Type = Counter32
_FaInsufficientResource_Object = MibScalar
faInsufficientResource = _FaInsufficientResource_Object(
    (1, 3, 6, 1, 2, 1, 44, 1, 5, 3, 6),
    _FaInsufficientResource_Type()
)
faInsufficientResource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    faInsufficientResource.setStatus("current")
_FaMNAuthenticationFailure_Type = Counter32
_FaMNAuthenticationFailure_Object = MibScalar
faMNAuthenticationFailure = _FaMNAuthenticationFailure_Object(
    (1, 3, 6, 1, 2, 1, 44, 1, 5, 3, 7),
    _FaMNAuthenticationFailure_Type()
)
faMNAuthenticationFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    faMNAuthenticationFailure.setStatus("current")
_FaRegLifetimeTooLong_Type = Counter32
_FaRegLifetimeTooLong_Object = MibScalar
faRegLifetimeTooLong = _FaRegLifetimeTooLong_Object(
    (1, 3, 6, 1, 2, 1, 44, 1, 5, 3, 8),
    _FaRegLifetimeTooLong_Type()
)
faRegLifetimeTooLong.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    faRegLifetimeTooLong.setStatus("current")
_FaPoorlyFormedRequests_Type = Counter32
_FaPoorlyFormedRequests_Object = MibScalar
faPoorlyFormedRequests = _FaPoorlyFormedRequests_Object(
    (1, 3, 6, 1, 2, 1, 44, 1, 5, 3, 9),
    _FaPoorlyFormedRequests_Type()
)
faPoorlyFormedRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    faPoorlyFormedRequests.setStatus("current")
_FaEncapsulationUnavailable_Type = Counter32
_FaEncapsulationUnavailable_Object = MibScalar
faEncapsulationUnavailable = _FaEncapsulationUnavailable_Object(
    (1, 3, 6, 1, 2, 1, 44, 1, 5, 3, 10),
    _FaEncapsulationUnavailable_Type()
)
faEncapsulationUnavailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    faEncapsulationUnavailable.setStatus("current")
_FaVJCompressionUnavailable_Type = Counter32
_FaVJCompressionUnavailable_Object = MibScalar
faVJCompressionUnavailable = _FaVJCompressionUnavailable_Object(
    (1, 3, 6, 1, 2, 1, 44, 1, 5, 3, 11),
    _FaVJCompressionUnavailable_Type()
)
faVJCompressionUnavailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    faVJCompressionUnavailable.setStatus("current")
_FaHAUnreachable_Type = Counter32
_FaHAUnreachable_Object = MibScalar
faHAUnreachable = _FaHAUnreachable_Object(
    (1, 3, 6, 1, 2, 1, 44, 1, 5, 3, 12),
    _FaHAUnreachable_Type()
)
faHAUnreachable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    faHAUnreachable.setStatus("current")
_FaRegRepliesRecieved_Type = Counter32
_FaRegRepliesRecieved_Object = MibScalar
faRegRepliesRecieved = _FaRegRepliesRecieved_Object(
    (1, 3, 6, 1, 2, 1, 44, 1, 5, 3, 13),
    _FaRegRepliesRecieved_Type()
)
faRegRepliesRecieved.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    faRegRepliesRecieved.setStatus("current")
_FaRegRepliesRelayed_Type = Counter32
_FaRegRepliesRelayed_Object = MibScalar
faRegRepliesRelayed = _FaRegRepliesRelayed_Object(
    (1, 3, 6, 1, 2, 1, 44, 1, 5, 3, 14),
    _FaRegRepliesRelayed_Type()
)
faRegRepliesRelayed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    faRegRepliesRelayed.setStatus("current")
_FaHAAuthenticationFailure_Type = Counter32
_FaHAAuthenticationFailure_Object = MibScalar
faHAAuthenticationFailure = _FaHAAuthenticationFailure_Object(
    (1, 3, 6, 1, 2, 1, 44, 1, 5, 3, 15),
    _FaHAAuthenticationFailure_Type()
)
faHAAuthenticationFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    faHAAuthenticationFailure.setStatus("current")
_FaPoorlyFormedReplies_Type = Counter32
_FaPoorlyFormedReplies_Object = MibScalar
faPoorlyFormedReplies = _FaPoorlyFormedReplies_Object(
    (1, 3, 6, 1, 2, 1, 44, 1, 5, 3, 16),
    _FaPoorlyFormedReplies_Type()
)
faPoorlyFormedReplies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    faPoorlyFormedReplies.setStatus("current")
_MipHA_ObjectIdentity = ObjectIdentity
mipHA = _MipHA_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 44, 1, 6)
)
_HaRegistration_ObjectIdentity = ObjectIdentity
haRegistration = _HaRegistration_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 44, 1, 6, 3)
)
_HaMobilityBindingTable_Object = MibTable
haMobilityBindingTable = _HaMobilityBindingTable_Object(
    (1, 3, 6, 1, 2, 1, 44, 1, 6, 3, 1)
)
if mibBuilder.loadTexts:
    haMobilityBindingTable.setStatus("current")
_HaMobilityBindingEntry_Object = MibTableRow
haMobilityBindingEntry = _HaMobilityBindingEntry_Object(
    (1, 3, 6, 1, 2, 1, 44, 1, 6, 3, 1, 1)
)
haMobilityBindingEntry.setIndexNames(
    (0, "MIP-MIB", "haMobilityBindingMN"),
    (0, "MIP-MIB", "haMobilityBindingCOA"),
)
if mibBuilder.loadTexts:
    haMobilityBindingEntry.setStatus("current")
_HaMobilityBindingMN_Type = IpAddress
_HaMobilityBindingMN_Object = MibTableColumn
haMobilityBindingMN = _HaMobilityBindingMN_Object(
    (1, 3, 6, 1, 2, 1, 44, 1, 6, 3, 1, 1, 1),
    _HaMobilityBindingMN_Type()
)
haMobilityBindingMN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    haMobilityBindingMN.setStatus("current")
_HaMobilityBindingCOA_Type = IpAddress
_HaMobilityBindingCOA_Object = MibTableColumn
haMobilityBindingCOA = _HaMobilityBindingCOA_Object(
    (1, 3, 6, 1, 2, 1, 44, 1, 6, 3, 1, 1, 2),
    _HaMobilityBindingCOA_Type()
)
haMobilityBindingCOA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    haMobilityBindingCOA.setStatus("current")
_HaMobilityBindingSourceAddress_Type = IpAddress
_HaMobilityBindingSourceAddress_Object = MibTableColumn
haMobilityBindingSourceAddress = _HaMobilityBindingSourceAddress_Object(
    (1, 3, 6, 1, 2, 1, 44, 1, 6, 3, 1, 1, 3),
    _HaMobilityBindingSourceAddress_Type()
)
haMobilityBindingSourceAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    haMobilityBindingSourceAddress.setStatus("current")
_HaMobilityBindingRegFlags_Type = RegistrationFlags
_HaMobilityBindingRegFlags_Object = MibTableColumn
haMobilityBindingRegFlags = _HaMobilityBindingRegFlags_Object(
    (1, 3, 6, 1, 2, 1, 44, 1, 6, 3, 1, 1, 4),
    _HaMobilityBindingRegFlags_Type()
)
haMobilityBindingRegFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    haMobilityBindingRegFlags.setStatus("current")
_HaMobilityBindingRegIDLow_Type = Integer32
_HaMobilityBindingRegIDLow_Object = MibTableColumn
haMobilityBindingRegIDLow = _HaMobilityBindingRegIDLow_Object(
    (1, 3, 6, 1, 2, 1, 44, 1, 6, 3, 1, 1, 5),
    _HaMobilityBindingRegIDLow_Type()
)
haMobilityBindingRegIDLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    haMobilityBindingRegIDLow.setStatus("current")
_HaMobilityBindingRegIDHigh_Type = Integer32
_HaMobilityBindingRegIDHigh_Object = MibTableColumn
haMobilityBindingRegIDHigh = _HaMobilityBindingRegIDHigh_Object(
    (1, 3, 6, 1, 2, 1, 44, 1, 6, 3, 1, 1, 6),
    _HaMobilityBindingRegIDHigh_Type()
)
haMobilityBindingRegIDHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    haMobilityBindingRegIDHigh.setStatus("current")
_HaMobilityBindingTimeGranted_Type = Integer32
_HaMobilityBindingTimeGranted_Object = MibTableColumn
haMobilityBindingTimeGranted = _HaMobilityBindingTimeGranted_Object(
    (1, 3, 6, 1, 2, 1, 44, 1, 6, 3, 1, 1, 7),
    _HaMobilityBindingTimeGranted_Type()
)
haMobilityBindingTimeGranted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    haMobilityBindingTimeGranted.setStatus("current")
if mibBuilder.loadTexts:
    haMobilityBindingTimeGranted.setUnits("seconds")
_HaMobilityBindingTimeRemaining_Type = Gauge32
_HaMobilityBindingTimeRemaining_Object = MibTableColumn
haMobilityBindingTimeRemaining = _HaMobilityBindingTimeRemaining_Object(
    (1, 3, 6, 1, 2, 1, 44, 1, 6, 3, 1, 1, 8),
    _HaMobilityBindingTimeRemaining_Type()
)
haMobilityBindingTimeRemaining.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    haMobilityBindingTimeRemaining.setStatus("current")
if mibBuilder.loadTexts:
    haMobilityBindingTimeRemaining.setUnits("seconds")
_HaCounterTable_Object = MibTable
haCounterTable = _HaCounterTable_Object(
    (1, 3, 6, 1, 2, 1, 44, 1, 6, 3, 2)
)
if mibBuilder.loadTexts:
    haCounterTable.setStatus("current")
_HaCounterEntry_Object = MibTableRow
haCounterEntry = _HaCounterEntry_Object(
    (1, 3, 6, 1, 2, 1, 44, 1, 6, 3, 2, 1)
)
haCounterEntry.setIndexNames(
    (0, "MIP-MIB", "haMobilityBindingMN"),
)
if mibBuilder.loadTexts:
    haCounterEntry.setStatus("current")
_HaServiceRequestsAccepted_Type = Counter32
_HaServiceRequestsAccepted_Object = MibTableColumn
haServiceRequestsAccepted = _HaServiceRequestsAccepted_Object(
    (1, 3, 6, 1, 2, 1, 44, 1, 6, 3, 2, 1, 2),
    _HaServiceRequestsAccepted_Type()
)
haServiceRequestsAccepted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    haServiceRequestsAccepted.setStatus("current")
_HaServiceRequestsDenied_Type = Counter32
_HaServiceRequestsDenied_Object = MibTableColumn
haServiceRequestsDenied = _HaServiceRequestsDenied_Object(
    (1, 3, 6, 1, 2, 1, 44, 1, 6, 3, 2, 1, 3),
    _HaServiceRequestsDenied_Type()
)
haServiceRequestsDenied.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    haServiceRequestsDenied.setStatus("current")
_HaOverallServiceTime_Type = Gauge32
_HaOverallServiceTime_Object = MibTableColumn
haOverallServiceTime = _HaOverallServiceTime_Object(
    (1, 3, 6, 1, 2, 1, 44, 1, 6, 3, 2, 1, 4),
    _HaOverallServiceTime_Type()
)
haOverallServiceTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    haOverallServiceTime.setStatus("current")
if mibBuilder.loadTexts:
    haOverallServiceTime.setUnits("seconds")
_HaRecentServiceAcceptedTime_Type = TimeStamp
_HaRecentServiceAcceptedTime_Object = MibTableColumn
haRecentServiceAcceptedTime = _HaRecentServiceAcceptedTime_Object(
    (1, 3, 6, 1, 2, 1, 44, 1, 6, 3, 2, 1, 5),
    _HaRecentServiceAcceptedTime_Type()
)
haRecentServiceAcceptedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    haRecentServiceAcceptedTime.setStatus("current")
_HaRecentServiceDeniedTime_Type = TimeStamp
_HaRecentServiceDeniedTime_Object = MibTableColumn
haRecentServiceDeniedTime = _HaRecentServiceDeniedTime_Object(
    (1, 3, 6, 1, 2, 1, 44, 1, 6, 3, 2, 1, 6),
    _HaRecentServiceDeniedTime_Type()
)
haRecentServiceDeniedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    haRecentServiceDeniedTime.setStatus("current")


class _HaRecentServiceDeniedCode_Type(Integer32):
    """Custom type haRecentServiceDeniedCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(128,
              129,
              130,
              131,
              132,
              133,
              134,
              135,
              136)
        )
    )
    namedValues = NamedValues(
        *(("admProhibited", 129),
          ("faAuthenticationFailure", 132),
          ("idMismatch", 133),
          ("insufficientResource", 130),
          ("mnAuthenticationFailure", 131),
          ("poorlyFormedRequest", 134),
          ("reasonUnspecified", 128),
          ("tooManyBindings", 135),
          ("unknownHA", 136))
    )


_HaRecentServiceDeniedCode_Type.__name__ = "Integer32"
_HaRecentServiceDeniedCode_Object = MibTableColumn
haRecentServiceDeniedCode = _HaRecentServiceDeniedCode_Object(
    (1, 3, 6, 1, 2, 1, 44, 1, 6, 3, 2, 1, 7),
    _HaRecentServiceDeniedCode_Type()
)
haRecentServiceDeniedCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    haRecentServiceDeniedCode.setStatus("current")
_HaRegistrationAccepted_Type = Counter32
_HaRegistrationAccepted_Object = MibScalar
haRegistrationAccepted = _HaRegistrationAccepted_Object(
    (1, 3, 6, 1, 2, 1, 44, 1, 6, 3, 3),
    _HaRegistrationAccepted_Type()
)
haRegistrationAccepted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    haRegistrationAccepted.setStatus("current")
_HaMultiBindingUnsupported_Type = Counter32
_HaMultiBindingUnsupported_Object = MibScalar
haMultiBindingUnsupported = _HaMultiBindingUnsupported_Object(
    (1, 3, 6, 1, 2, 1, 44, 1, 6, 3, 4),
    _HaMultiBindingUnsupported_Type()
)
haMultiBindingUnsupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    haMultiBindingUnsupported.setStatus("current")
_HaReasonUnspecified_Type = Counter32
_HaReasonUnspecified_Object = MibScalar
haReasonUnspecified = _HaReasonUnspecified_Object(
    (1, 3, 6, 1, 2, 1, 44, 1, 6, 3, 5),
    _HaReasonUnspecified_Type()
)
haReasonUnspecified.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    haReasonUnspecified.setStatus("current")
_HaAdmProhibited_Type = Counter32
_HaAdmProhibited_Object = MibScalar
haAdmProhibited = _HaAdmProhibited_Object(
    (1, 3, 6, 1, 2, 1, 44, 1, 6, 3, 6),
    _HaAdmProhibited_Type()
)
haAdmProhibited.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    haAdmProhibited.setStatus("current")
_HaInsufficientResource_Type = Counter32
_HaInsufficientResource_Object = MibScalar
haInsufficientResource = _HaInsufficientResource_Object(
    (1, 3, 6, 1, 2, 1, 44, 1, 6, 3, 7),
    _HaInsufficientResource_Type()
)
haInsufficientResource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    haInsufficientResource.setStatus("current")
_HaMNAuthenticationFailure_Type = Counter32
_HaMNAuthenticationFailure_Object = MibScalar
haMNAuthenticationFailure = _HaMNAuthenticationFailure_Object(
    (1, 3, 6, 1, 2, 1, 44, 1, 6, 3, 8),
    _HaMNAuthenticationFailure_Type()
)
haMNAuthenticationFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    haMNAuthenticationFailure.setStatus("current")
_HaFAAuthenticationFailure_Type = Counter32
_HaFAAuthenticationFailure_Object = MibScalar
haFAAuthenticationFailure = _HaFAAuthenticationFailure_Object(
    (1, 3, 6, 1, 2, 1, 44, 1, 6, 3, 9),
    _HaFAAuthenticationFailure_Type()
)
haFAAuthenticationFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    haFAAuthenticationFailure.setStatus("current")
_HaIDMismatch_Type = Counter32
_HaIDMismatch_Object = MibScalar
haIDMismatch = _HaIDMismatch_Object(
    (1, 3, 6, 1, 2, 1, 44, 1, 6, 3, 10),
    _HaIDMismatch_Type()
)
haIDMismatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    haIDMismatch.setStatus("current")
_HaPoorlyFormedRequest_Type = Counter32
_HaPoorlyFormedRequest_Object = MibScalar
haPoorlyFormedRequest = _HaPoorlyFormedRequest_Object(
    (1, 3, 6, 1, 2, 1, 44, 1, 6, 3, 11),
    _HaPoorlyFormedRequest_Type()
)
haPoorlyFormedRequest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    haPoorlyFormedRequest.setStatus("current")
_HaTooManyBindings_Type = Counter32
_HaTooManyBindings_Object = MibScalar
haTooManyBindings = _HaTooManyBindings_Object(
    (1, 3, 6, 1, 2, 1, 44, 1, 6, 3, 12),
    _HaTooManyBindings_Type()
)
haTooManyBindings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    haTooManyBindings.setStatus("current")
_HaUnknownHA_Type = Counter32
_HaUnknownHA_Object = MibScalar
haUnknownHA = _HaUnknownHA_Object(
    (1, 3, 6, 1, 2, 1, 44, 1, 6, 3, 13),
    _HaUnknownHA_Type()
)
haUnknownHA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    haUnknownHA.setStatus("current")
_HaGratuitiousARPsSent_Type = Counter32
_HaGratuitiousARPsSent_Object = MibScalar
haGratuitiousARPsSent = _HaGratuitiousARPsSent_Object(
    (1, 3, 6, 1, 2, 1, 44, 1, 6, 3, 14),
    _HaGratuitiousARPsSent_Type()
)
haGratuitiousARPsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    haGratuitiousARPsSent.setStatus("current")
_HaProxyARPsSent_Type = Counter32
_HaProxyARPsSent_Object = MibScalar
haProxyARPsSent = _HaProxyARPsSent_Object(
    (1, 3, 6, 1, 2, 1, 44, 1, 6, 3, 15),
    _HaProxyARPsSent_Type()
)
haProxyARPsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    haProxyARPsSent.setStatus("current")
_HaRegRequestsReceived_Type = Counter32
_HaRegRequestsReceived_Object = MibScalar
haRegRequestsReceived = _HaRegRequestsReceived_Object(
    (1, 3, 6, 1, 2, 1, 44, 1, 6, 3, 16),
    _HaRegRequestsReceived_Type()
)
haRegRequestsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    haRegRequestsReceived.setStatus("current")
_HaDeRegRequestsReceived_Type = Counter32
_HaDeRegRequestsReceived_Object = MibScalar
haDeRegRequestsReceived = _HaDeRegRequestsReceived_Object(
    (1, 3, 6, 1, 2, 1, 44, 1, 6, 3, 17),
    _HaDeRegRequestsReceived_Type()
)
haDeRegRequestsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    haDeRegRequestsReceived.setStatus("current")
_HaRegRepliesSent_Type = Counter32
_HaRegRepliesSent_Object = MibScalar
haRegRepliesSent = _HaRegRepliesSent_Object(
    (1, 3, 6, 1, 2, 1, 44, 1, 6, 3, 18),
    _HaRegRepliesSent_Type()
)
haRegRepliesSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    haRegRepliesSent.setStatus("current")
_HaDeRegRepliesSent_Type = Counter32
_HaDeRegRepliesSent_Object = MibScalar
haDeRegRepliesSent = _HaDeRegRepliesSent_Object(
    (1, 3, 6, 1, 2, 1, 44, 1, 6, 3, 19),
    _HaDeRegRepliesSent_Type()
)
haDeRegRepliesSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    haDeRegRepliesSent.setStatus("current")
_MipMIBNotificationPrefix_ObjectIdentity = ObjectIdentity
mipMIBNotificationPrefix = _MipMIBNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 44, 2)
)
_MipMIBNotifications_ObjectIdentity = ObjectIdentity
mipMIBNotifications = _MipMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 44, 2, 0)
)
_MipMIBConformance_ObjectIdentity = ObjectIdentity
mipMIBConformance = _MipMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 44, 3)
)
_MipGroups_ObjectIdentity = ObjectIdentity
mipGroups = _MipGroups_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 44, 3, 1)
)
_MipCompliances_ObjectIdentity = ObjectIdentity
mipCompliances = _MipCompliances_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 44, 3, 2)
)

# Managed Objects groups

mipSystemGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 44, 3, 1, 1)
)
mipSystemGroup.setObjects(
      *(("MIP-MIB", "mipEntities"),
        ("MIP-MIB", "mipEnable"),
        ("MIP-MIB", "mipEncapsulationSupported"))
)
if mibBuilder.loadTexts:
    mipSystemGroup.setStatus("current")

mipSecAssociationGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 44, 3, 1, 2)
)
mipSecAssociationGroup.setObjects(
      *(("MIP-MIB", "mipSecAlgorithmType"),
        ("MIP-MIB", "mipSecAlgorithmMode"),
        ("MIP-MIB", "mipSecKey"),
        ("MIP-MIB", "mipSecReplayMethod"))
)
if mibBuilder.loadTexts:
    mipSecAssociationGroup.setStatus("current")

mipSecViolationGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 44, 3, 1, 3)
)
mipSecViolationGroup.setObjects(
      *(("MIP-MIB", "mipSecTotalViolations"),
        ("MIP-MIB", "mipSecViolationCounter"),
        ("MIP-MIB", "mipSecRecentViolationSPI"),
        ("MIP-MIB", "mipSecRecentViolationTime"),
        ("MIP-MIB", "mipSecRecentViolationIDLow"),
        ("MIP-MIB", "mipSecRecentViolationIDHigh"),
        ("MIP-MIB", "mipSecRecentViolationReason"))
)
if mibBuilder.loadTexts:
    mipSecViolationGroup.setStatus("current")

mnSystemGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 44, 3, 1, 4)
)
mnSystemGroup.setObjects(
      *(("MIP-MIB", "mnState"),
        ("MIP-MIB", "mnCurrentHA"),
        ("MIP-MIB", "mnHomeAddress"),
        ("MIP-MIB", "mnHAStatus"))
)
if mibBuilder.loadTexts:
    mnSystemGroup.setStatus("current")

mnDiscoveryGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 44, 3, 1, 5)
)
mnDiscoveryGroup.setObjects(
      *(("MIP-MIB", "mnFAAddress"),
        ("MIP-MIB", "mnCOA"),
        ("MIP-MIB", "mnAdvSourceAddress"),
        ("MIP-MIB", "mnAdvSequence"),
        ("MIP-MIB", "mnAdvFlags"),
        ("MIP-MIB", "mnAdvMaxRegLifetime"),
        ("MIP-MIB", "mnAdvMaxAdvLifetime"),
        ("MIP-MIB", "mnAdvTimeReceived"),
        ("MIP-MIB", "mnSolicitationsSent"),
        ("MIP-MIB", "mnAdvertisementsReceived"),
        ("MIP-MIB", "mnAdvsDroppedInvalidExtension"),
        ("MIP-MIB", "mnAdvsIgnoredUnknownExtension"),
        ("MIP-MIB", "mnMoveFromHAToFA"),
        ("MIP-MIB", "mnMoveFromFAToFA"),
        ("MIP-MIB", "mnMoveFromFAToHA"),
        ("MIP-MIB", "mnGratuitousARPsSend"),
        ("MIP-MIB", "mnAgentRebootsDectected"))
)
if mibBuilder.loadTexts:
    mnDiscoveryGroup.setStatus("current")

mnRegistrationGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 44, 3, 1, 6)
)
mnRegistrationGroup.setObjects(
      *(("MIP-MIB", "mnRegAgentAddress"),
        ("MIP-MIB", "mnRegCOA"),
        ("MIP-MIB", "mnRegFlags"),
        ("MIP-MIB", "mnRegIDLow"),
        ("MIP-MIB", "mnRegIDHigh"),
        ("MIP-MIB", "mnRegTimeRequested"),
        ("MIP-MIB", "mnRegTimeRemaining"),
        ("MIP-MIB", "mnRegTimeSent"),
        ("MIP-MIB", "mnRegIsAccepted"),
        ("MIP-MIB", "mnCOAIsLocal"),
        ("MIP-MIB", "mnRegRequestsSent"),
        ("MIP-MIB", "mnRegRepliesRecieved"),
        ("MIP-MIB", "mnDeRegRequestsSent"),
        ("MIP-MIB", "mnDeRegRepliesRecieved"),
        ("MIP-MIB", "mnRepliesInvalidHomeAddress"),
        ("MIP-MIB", "mnRepliesUnknownHA"),
        ("MIP-MIB", "mnRepliesUnknownFA"),
        ("MIP-MIB", "mnRepliesInvalidID"),
        ("MIP-MIB", "mnRepliesDroppedInvalidExtension"),
        ("MIP-MIB", "mnRepliesIgnoredUnknownExtension"),
        ("MIP-MIB", "mnRepliesHAAuthenticationFailure"),
        ("MIP-MIB", "mnRepliesFAAuthenticationFailure"),
        ("MIP-MIB", "mnRegRequestsAccepted"),
        ("MIP-MIB", "mnRegRequestsDeniedByHA"),
        ("MIP-MIB", "mnRegRequestsDeniedByFA"),
        ("MIP-MIB", "mnRegRequestsDeniedByHADueToID"),
        ("MIP-MIB", "mnRegRequestsWithDirectedBroadcast"))
)
if mibBuilder.loadTexts:
    mnRegistrationGroup.setStatus("current")

maAdvertisementGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 44, 3, 1, 7)
)
maAdvertisementGroup.setObjects(
      *(("MIP-MIB", "maAdvMaxRegLifetime"),
        ("MIP-MIB", "maAdvPrefixLengthInclusion"),
        ("MIP-MIB", "maAdvAddress"),
        ("MIP-MIB", "maAdvMaxInterval"),
        ("MIP-MIB", "maAdvMinInterval"),
        ("MIP-MIB", "maAdvMaxAdvLifetime"),
        ("MIP-MIB", "maAdvResponseSolicitationOnly"),
        ("MIP-MIB", "maAdvStatus"),
        ("MIP-MIB", "maAdvertisementsSent"),
        ("MIP-MIB", "maAdvsSentForSolicitation"),
        ("MIP-MIB", "maSolicitationsReceived"))
)
if mibBuilder.loadTexts:
    maAdvertisementGroup.setStatus("current")

faSystemGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 44, 3, 1, 8)
)
faSystemGroup.setObjects(
    ("MIP-MIB", "faCOAStatus")
)
if mibBuilder.loadTexts:
    faSystemGroup.setStatus("current")

faAdvertisementGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 44, 3, 1, 9)
)
faAdvertisementGroup.setObjects(
      *(("MIP-MIB", "faIsBusy"),
        ("MIP-MIB", "faRegistrationRequired"))
)
if mibBuilder.loadTexts:
    faAdvertisementGroup.setStatus("current")

faRegistrationGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 44, 3, 1, 10)
)
faRegistrationGroup.setObjects(
      *(("MIP-MIB", "faVisitorIPAddress"),
        ("MIP-MIB", "faVisitorHomeAddress"),
        ("MIP-MIB", "faVisitorHomeAgentAddress"),
        ("MIP-MIB", "faVisitorTimeGranted"),
        ("MIP-MIB", "faVisitorTimeRemaining"),
        ("MIP-MIB", "faVisitorRegFlags"),
        ("MIP-MIB", "faVisitorRegIDLow"),
        ("MIP-MIB", "faVisitorRegIDHigh"),
        ("MIP-MIB", "faVisitorRegIsAccepted"),
        ("MIP-MIB", "faRegRequestsReceived"),
        ("MIP-MIB", "faRegRequestsRelayed"),
        ("MIP-MIB", "faReasonUnspecified"),
        ("MIP-MIB", "faAdmProhibited"),
        ("MIP-MIB", "faInsufficientResource"),
        ("MIP-MIB", "faMNAuthenticationFailure"),
        ("MIP-MIB", "faRegLifetimeTooLong"),
        ("MIP-MIB", "faPoorlyFormedRequests"),
        ("MIP-MIB", "faEncapsulationUnavailable"),
        ("MIP-MIB", "faVJCompressionUnavailable"),
        ("MIP-MIB", "faHAUnreachable"),
        ("MIP-MIB", "faRegRepliesRecieved"),
        ("MIP-MIB", "faRegRepliesRelayed"),
        ("MIP-MIB", "faHAAuthenticationFailure"),
        ("MIP-MIB", "faPoorlyFormedReplies"))
)
if mibBuilder.loadTexts:
    faRegistrationGroup.setStatus("current")

haRegistrationGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 44, 3, 1, 11)
)
haRegistrationGroup.setObjects(
      *(("MIP-MIB", "haMobilityBindingMN"),
        ("MIP-MIB", "haMobilityBindingCOA"),
        ("MIP-MIB", "haMobilityBindingSourceAddress"),
        ("MIP-MIB", "haMobilityBindingRegFlags"),
        ("MIP-MIB", "haMobilityBindingRegIDLow"),
        ("MIP-MIB", "haMobilityBindingRegIDHigh"),
        ("MIP-MIB", "haMobilityBindingTimeGranted"),
        ("MIP-MIB", "haMobilityBindingTimeRemaining"),
        ("MIP-MIB", "haRegistrationAccepted"),
        ("MIP-MIB", "haMultiBindingUnsupported"),
        ("MIP-MIB", "haReasonUnspecified"),
        ("MIP-MIB", "haAdmProhibited"),
        ("MIP-MIB", "haInsufficientResource"),
        ("MIP-MIB", "haMNAuthenticationFailure"),
        ("MIP-MIB", "haFAAuthenticationFailure"),
        ("MIP-MIB", "haIDMismatch"),
        ("MIP-MIB", "haPoorlyFormedRequest"),
        ("MIP-MIB", "haTooManyBindings"),
        ("MIP-MIB", "haUnknownHA"),
        ("MIP-MIB", "haGratuitiousARPsSent"),
        ("MIP-MIB", "haProxyARPsSent"),
        ("MIP-MIB", "haRegRequestsReceived"),
        ("MIP-MIB", "haDeRegRequestsReceived"),
        ("MIP-MIB", "haRegRepliesSent"),
        ("MIP-MIB", "haDeRegRepliesSent"))
)
if mibBuilder.loadTexts:
    haRegistrationGroup.setStatus("current")

haRegNodeCountersGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 44, 3, 1, 12)
)
haRegNodeCountersGroup.setObjects(
      *(("MIP-MIB", "haServiceRequestsAccepted"),
        ("MIP-MIB", "haServiceRequestsDenied"),
        ("MIP-MIB", "haOverallServiceTime"),
        ("MIP-MIB", "haRecentServiceAcceptedTime"),
        ("MIP-MIB", "haRecentServiceDeniedTime"),
        ("MIP-MIB", "haRecentServiceDeniedCode"))
)
if mibBuilder.loadTexts:
    haRegNodeCountersGroup.setStatus("current")


# Notification objects

mipAuthFailure = NotificationType(
    (1, 3, 6, 1, 2, 1, 44, 2, 0, 1)
)
mipAuthFailure.setObjects(
      *(("MIP-MIB", "mipSecViolatorAddress"),
        ("MIP-MIB", "mipSecRecentViolationSPI"),
        ("MIP-MIB", "mipSecRecentViolationIDLow"),
        ("MIP-MIB", "mipSecRecentViolationIDHigh"),
        ("MIP-MIB", "mipSecRecentViolationReason"))
)
if mibBuilder.loadTexts:
    mipAuthFailure.setStatus(
        "current"
    )


# Notifications groups

mipSecNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 2, 1, 44, 3, 1, 13)
)
mipSecNotificationsGroup.setObjects(
    ("MIP-MIB", "mipAuthFailure")
)
if mibBuilder.loadTexts:
    mipSecNotificationsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

mipCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 44, 3, 2, 1)
)
if mibBuilder.loadTexts:
    mipCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MIP-MIB",
    **{"RegistrationFlags": RegistrationFlags,
       "mipMIB": mipMIB,
       "mipMIBObjects": mipMIBObjects,
       "mipSystem": mipSystem,
       "mipEntities": mipEntities,
       "mipEnable": mipEnable,
       "mipEncapsulationSupported": mipEncapsulationSupported,
       "mipSecurity": mipSecurity,
       "mipSecAssocTable": mipSecAssocTable,
       "mipSecAssocEntry": mipSecAssocEntry,
       "mipSecPeerAddress": mipSecPeerAddress,
       "mipSecSPI": mipSecSPI,
       "mipSecAlgorithmType": mipSecAlgorithmType,
       "mipSecAlgorithmMode": mipSecAlgorithmMode,
       "mipSecKey": mipSecKey,
       "mipSecReplayMethod": mipSecReplayMethod,
       "mipSecTotalViolations": mipSecTotalViolations,
       "mipSecViolationTable": mipSecViolationTable,
       "mipSecViolationEntry": mipSecViolationEntry,
       "mipSecViolatorAddress": mipSecViolatorAddress,
       "mipSecViolationCounter": mipSecViolationCounter,
       "mipSecRecentViolationSPI": mipSecRecentViolationSPI,
       "mipSecRecentViolationTime": mipSecRecentViolationTime,
       "mipSecRecentViolationIDLow": mipSecRecentViolationIDLow,
       "mipSecRecentViolationIDHigh": mipSecRecentViolationIDHigh,
       "mipSecRecentViolationReason": mipSecRecentViolationReason,
       "mipMN": mipMN,
       "mnSystem": mnSystem,
       "mnState": mnState,
       "mnHomeAddress": mnHomeAddress,
       "mnHATable": mnHATable,
       "mnHAEntry": mnHAEntry,
       "mnHAAddress": mnHAAddress,
       "mnCurrentHA": mnCurrentHA,
       "mnHAStatus": mnHAStatus,
       "mnDiscovery": mnDiscovery,
       "mnFATable": mnFATable,
       "mnFAEntry": mnFAEntry,
       "mnFAAddress": mnFAAddress,
       "mnCOA": mnCOA,
       "mnRecentAdvReceived": mnRecentAdvReceived,
       "mnAdvSourceAddress": mnAdvSourceAddress,
       "mnAdvSequence": mnAdvSequence,
       "mnAdvFlags": mnAdvFlags,
       "mnAdvMaxRegLifetime": mnAdvMaxRegLifetime,
       "mnAdvMaxAdvLifetime": mnAdvMaxAdvLifetime,
       "mnAdvTimeReceived": mnAdvTimeReceived,
       "mnSolicitationsSent": mnSolicitationsSent,
       "mnAdvertisementsReceived": mnAdvertisementsReceived,
       "mnAdvsDroppedInvalidExtension": mnAdvsDroppedInvalidExtension,
       "mnAdvsIgnoredUnknownExtension": mnAdvsIgnoredUnknownExtension,
       "mnMoveFromHAToFA": mnMoveFromHAToFA,
       "mnMoveFromFAToFA": mnMoveFromFAToFA,
       "mnMoveFromFAToHA": mnMoveFromFAToHA,
       "mnGratuitousARPsSend": mnGratuitousARPsSend,
       "mnAgentRebootsDectected": mnAgentRebootsDectected,
       "mnRegistration": mnRegistration,
       "mnRegistrationTable": mnRegistrationTable,
       "mnRegistrationEntry": mnRegistrationEntry,
       "mnRegAgentAddress": mnRegAgentAddress,
       "mnRegCOA": mnRegCOA,
       "mnRegFlags": mnRegFlags,
       "mnRegIDLow": mnRegIDLow,
       "mnRegIDHigh": mnRegIDHigh,
       "mnRegTimeRequested": mnRegTimeRequested,
       "mnRegTimeRemaining": mnRegTimeRemaining,
       "mnRegTimeSent": mnRegTimeSent,
       "mnRegIsAccepted": mnRegIsAccepted,
       "mnCOAIsLocal": mnCOAIsLocal,
       "mnRegRequestsSent": mnRegRequestsSent,
       "mnDeRegRequestsSent": mnDeRegRequestsSent,
       "mnRegRepliesRecieved": mnRegRepliesRecieved,
       "mnDeRegRepliesRecieved": mnDeRegRepliesRecieved,
       "mnRepliesInvalidHomeAddress": mnRepliesInvalidHomeAddress,
       "mnRepliesUnknownHA": mnRepliesUnknownHA,
       "mnRepliesUnknownFA": mnRepliesUnknownFA,
       "mnRepliesInvalidID": mnRepliesInvalidID,
       "mnRepliesDroppedInvalidExtension": mnRepliesDroppedInvalidExtension,
       "mnRepliesIgnoredUnknownExtension": mnRepliesIgnoredUnknownExtension,
       "mnRepliesHAAuthenticationFailure": mnRepliesHAAuthenticationFailure,
       "mnRepliesFAAuthenticationFailure": mnRepliesFAAuthenticationFailure,
       "mnRegRequestsAccepted": mnRegRequestsAccepted,
       "mnRegRequestsDeniedByHA": mnRegRequestsDeniedByHA,
       "mnRegRequestsDeniedByFA": mnRegRequestsDeniedByFA,
       "mnRegRequestsDeniedByHADueToID": mnRegRequestsDeniedByHADueToID,
       "mnRegRequestsWithDirectedBroadcast": mnRegRequestsWithDirectedBroadcast,
       "mipMA": mipMA,
       "maAdvertisement": maAdvertisement,
       "maAdvConfigTable": maAdvConfigTable,
       "maAdvConfigEntry": maAdvConfigEntry,
       "maInterfaceAddress": maInterfaceAddress,
       "maAdvMaxRegLifetime": maAdvMaxRegLifetime,
       "maAdvPrefixLengthInclusion": maAdvPrefixLengthInclusion,
       "maAdvAddress": maAdvAddress,
       "maAdvMaxInterval": maAdvMaxInterval,
       "maAdvMinInterval": maAdvMinInterval,
       "maAdvMaxAdvLifetime": maAdvMaxAdvLifetime,
       "maAdvResponseSolicitationOnly": maAdvResponseSolicitationOnly,
       "maAdvStatus": maAdvStatus,
       "maAdvertisementsSent": maAdvertisementsSent,
       "maAdvsSentForSolicitation": maAdvsSentForSolicitation,
       "maSolicitationsReceived": maSolicitationsReceived,
       "mipFA": mipFA,
       "faSystem": faSystem,
       "faCOATable": faCOATable,
       "faCOAEntry": faCOAEntry,
       "faSupportedCOA": faSupportedCOA,
       "faCOAStatus": faCOAStatus,
       "faAdvertisement": faAdvertisement,
       "faIsBusy": faIsBusy,
       "faRegistrationRequired": faRegistrationRequired,
       "faRegistration": faRegistration,
       "faVisitorTable": faVisitorTable,
       "faVisitorEntry": faVisitorEntry,
       "faVisitorIPAddress": faVisitorIPAddress,
       "faVisitorHomeAddress": faVisitorHomeAddress,
       "faVisitorHomeAgentAddress": faVisitorHomeAgentAddress,
       "faVisitorTimeGranted": faVisitorTimeGranted,
       "faVisitorTimeRemaining": faVisitorTimeRemaining,
       "faVisitorRegFlags": faVisitorRegFlags,
       "faVisitorRegIDLow": faVisitorRegIDLow,
       "faVisitorRegIDHigh": faVisitorRegIDHigh,
       "faVisitorRegIsAccepted": faVisitorRegIsAccepted,
       "faRegRequestsReceived": faRegRequestsReceived,
       "faRegRequestsRelayed": faRegRequestsRelayed,
       "faReasonUnspecified": faReasonUnspecified,
       "faAdmProhibited": faAdmProhibited,
       "faInsufficientResource": faInsufficientResource,
       "faMNAuthenticationFailure": faMNAuthenticationFailure,
       "faRegLifetimeTooLong": faRegLifetimeTooLong,
       "faPoorlyFormedRequests": faPoorlyFormedRequests,
       "faEncapsulationUnavailable": faEncapsulationUnavailable,
       "faVJCompressionUnavailable": faVJCompressionUnavailable,
       "faHAUnreachable": faHAUnreachable,
       "faRegRepliesRecieved": faRegRepliesRecieved,
       "faRegRepliesRelayed": faRegRepliesRelayed,
       "faHAAuthenticationFailure": faHAAuthenticationFailure,
       "faPoorlyFormedReplies": faPoorlyFormedReplies,
       "mipHA": mipHA,
       "haRegistration": haRegistration,
       "haMobilityBindingTable": haMobilityBindingTable,
       "haMobilityBindingEntry": haMobilityBindingEntry,
       "haMobilityBindingMN": haMobilityBindingMN,
       "haMobilityBindingCOA": haMobilityBindingCOA,
       "haMobilityBindingSourceAddress": haMobilityBindingSourceAddress,
       "haMobilityBindingRegFlags": haMobilityBindingRegFlags,
       "haMobilityBindingRegIDLow": haMobilityBindingRegIDLow,
       "haMobilityBindingRegIDHigh": haMobilityBindingRegIDHigh,
       "haMobilityBindingTimeGranted": haMobilityBindingTimeGranted,
       "haMobilityBindingTimeRemaining": haMobilityBindingTimeRemaining,
       "haCounterTable": haCounterTable,
       "haCounterEntry": haCounterEntry,
       "haServiceRequestsAccepted": haServiceRequestsAccepted,
       "haServiceRequestsDenied": haServiceRequestsDenied,
       "haOverallServiceTime": haOverallServiceTime,
       "haRecentServiceAcceptedTime": haRecentServiceAcceptedTime,
       "haRecentServiceDeniedTime": haRecentServiceDeniedTime,
       "haRecentServiceDeniedCode": haRecentServiceDeniedCode,
       "haRegistrationAccepted": haRegistrationAccepted,
       "haMultiBindingUnsupported": haMultiBindingUnsupported,
       "haReasonUnspecified": haReasonUnspecified,
       "haAdmProhibited": haAdmProhibited,
       "haInsufficientResource": haInsufficientResource,
       "haMNAuthenticationFailure": haMNAuthenticationFailure,
       "haFAAuthenticationFailure": haFAAuthenticationFailure,
       "haIDMismatch": haIDMismatch,
       "haPoorlyFormedRequest": haPoorlyFormedRequest,
       "haTooManyBindings": haTooManyBindings,
       "haUnknownHA": haUnknownHA,
       "haGratuitiousARPsSent": haGratuitiousARPsSent,
       "haProxyARPsSent": haProxyARPsSent,
       "haRegRequestsReceived": haRegRequestsReceived,
       "haDeRegRequestsReceived": haDeRegRequestsReceived,
       "haRegRepliesSent": haRegRepliesSent,
       "haDeRegRepliesSent": haDeRegRepliesSent,
       "mipMIBNotificationPrefix": mipMIBNotificationPrefix,
       "mipMIBNotifications": mipMIBNotifications,
       "mipAuthFailure": mipAuthFailure,
       "mipMIBConformance": mipMIBConformance,
       "mipGroups": mipGroups,
       "mipSystemGroup": mipSystemGroup,
       "mipSecAssociationGroup": mipSecAssociationGroup,
       "mipSecViolationGroup": mipSecViolationGroup,
       "mnSystemGroup": mnSystemGroup,
       "mnDiscoveryGroup": mnDiscoveryGroup,
       "mnRegistrationGroup": mnRegistrationGroup,
       "maAdvertisementGroup": maAdvertisementGroup,
       "faSystemGroup": faSystemGroup,
       "faAdvertisementGroup": faAdvertisementGroup,
       "faRegistrationGroup": faRegistrationGroup,
       "haRegistrationGroup": haRegistrationGroup,
       "haRegNodeCountersGroup": haRegNodeCountersGroup,
       "mipSecNotificationsGroup": mipSecNotificationsGroup,
       "mipCompliances": mipCompliances,
       "mipCompliance": mipCompliance}
)
