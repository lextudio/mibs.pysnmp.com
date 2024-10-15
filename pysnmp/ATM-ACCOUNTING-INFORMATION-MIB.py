# SNMP MIB module (ATM-ACCOUNTING-INFORMATION-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ATM-ACCOUNTING-INFORMATION-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:43:47 2024
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

(AtmAddr,) = mibBuilder.importSymbols(
    "ATM-TC-MIB",
    "AtmAddr")

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
    "iso",
    "mib-2")

(DateAndTime,
 DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

atmAccountingInformationMIB = ModuleIdentity(
    (1, 3, 6, 1, 2, 1, 59)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AtmAcctngMIBObjects_ObjectIdentity = ObjectIdentity
atmAcctngMIBObjects = _AtmAcctngMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 59, 1)
)
_AtmAcctngDataObjects_ObjectIdentity = ObjectIdentity
atmAcctngDataObjects = _AtmAcctngDataObjects_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 59, 1, 1)
)
if mibBuilder.loadTexts:
    atmAcctngDataObjects.setStatus("current")


class _AtmAcctngConnectionType_Type(Integer32):
    """Custom type atmAcctngConnectionType based on Integer32"""
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("pvc", 1),
          ("pvp", 2),
          ("spvcInitiator", 7),
          ("spvcTarget", 8),
          ("spvpInitiator", 9),
          ("spvpTarget", 10),
          ("svcIncoming", 3),
          ("svcOutgoing", 4),
          ("svpIncoming", 5),
          ("svpOutgoing", 6))
    )


_AtmAcctngConnectionType_Type.__name__ = "Integer32"
_AtmAcctngConnectionType_Object = MibScalar
atmAcctngConnectionType = _AtmAcctngConnectionType_Object(
    (1, 3, 6, 1, 2, 1, 59, 1, 1, 1),
    _AtmAcctngConnectionType_Type()
)
atmAcctngConnectionType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    atmAcctngConnectionType.setStatus("current")


class _AtmAcctngCastType_Type(Integer32):
    """Custom type atmAcctngCastType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("p2mp", 2),
          ("p2p", 1))
    )


_AtmAcctngCastType_Type.__name__ = "Integer32"
_AtmAcctngCastType_Object = MibScalar
atmAcctngCastType = _AtmAcctngCastType_Object(
    (1, 3, 6, 1, 2, 1, 59, 1, 1, 2),
    _AtmAcctngCastType_Type()
)
atmAcctngCastType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    atmAcctngCastType.setStatus("current")
_AtmAcctngIfName_Type = DisplayString
_AtmAcctngIfName_Object = MibScalar
atmAcctngIfName = _AtmAcctngIfName_Object(
    (1, 3, 6, 1, 2, 1, 59, 1, 1, 3),
    _AtmAcctngIfName_Type()
)
atmAcctngIfName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    atmAcctngIfName.setStatus("current")
_AtmAcctngIfAlias_Type = DisplayString
_AtmAcctngIfAlias_Object = MibScalar
atmAcctngIfAlias = _AtmAcctngIfAlias_Object(
    (1, 3, 6, 1, 2, 1, 59, 1, 1, 4),
    _AtmAcctngIfAlias_Type()
)
atmAcctngIfAlias.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    atmAcctngIfAlias.setStatus("current")


class _AtmAcctngVpi_Type(Integer32):
    """Custom type atmAcctngVpi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_AtmAcctngVpi_Type.__name__ = "Integer32"
_AtmAcctngVpi_Object = MibScalar
atmAcctngVpi = _AtmAcctngVpi_Object(
    (1, 3, 6, 1, 2, 1, 59, 1, 1, 5),
    _AtmAcctngVpi_Type()
)
atmAcctngVpi.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    atmAcctngVpi.setStatus("current")


class _AtmAcctngVci_Type(Integer32):
    """Custom type atmAcctngVci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AtmAcctngVci_Type.__name__ = "Integer32"
_AtmAcctngVci_Object = MibScalar
atmAcctngVci = _AtmAcctngVci_Object(
    (1, 3, 6, 1, 2, 1, 59, 1, 1, 6),
    _AtmAcctngVci_Type()
)
atmAcctngVci.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    atmAcctngVci.setStatus("current")
_AtmAcctngCallingParty_Type = AtmAddr
_AtmAcctngCallingParty_Object = MibScalar
atmAcctngCallingParty = _AtmAcctngCallingParty_Object(
    (1, 3, 6, 1, 2, 1, 59, 1, 1, 7),
    _AtmAcctngCallingParty_Type()
)
atmAcctngCallingParty.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    atmAcctngCallingParty.setStatus("current")
_AtmAcctngCalledParty_Type = AtmAddr
_AtmAcctngCalledParty_Object = MibScalar
atmAcctngCalledParty = _AtmAcctngCalledParty_Object(
    (1, 3, 6, 1, 2, 1, 59, 1, 1, 8),
    _AtmAcctngCalledParty_Type()
)
atmAcctngCalledParty.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    atmAcctngCalledParty.setStatus("current")


class _AtmAcctngCallReference_Type(OctetString):
    """Custom type atmAcctngCallReference based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 3),
    )


_AtmAcctngCallReference_Type.__name__ = "OctetString"
_AtmAcctngCallReference_Object = MibScalar
atmAcctngCallReference = _AtmAcctngCallReference_Object(
    (1, 3, 6, 1, 2, 1, 59, 1, 1, 9),
    _AtmAcctngCallReference_Type()
)
atmAcctngCallReference.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    atmAcctngCallReference.setStatus("current")
_AtmAcctngStartTime_Type = DateAndTime
_AtmAcctngStartTime_Object = MibScalar
atmAcctngStartTime = _AtmAcctngStartTime_Object(
    (1, 3, 6, 1, 2, 1, 59, 1, 1, 10),
    _AtmAcctngStartTime_Type()
)
atmAcctngStartTime.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    atmAcctngStartTime.setStatus("current")
_AtmAcctngCollectionTime_Type = DateAndTime
_AtmAcctngCollectionTime_Object = MibScalar
atmAcctngCollectionTime = _AtmAcctngCollectionTime_Object(
    (1, 3, 6, 1, 2, 1, 59, 1, 1, 11),
    _AtmAcctngCollectionTime_Type()
)
atmAcctngCollectionTime.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    atmAcctngCollectionTime.setStatus("current")


class _AtmAcctngCollectMode_Type(Integer32):
    """Custom type atmAcctngCollectMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("onCommand", 3),
          ("onRelease", 1),
          ("periodically", 2))
    )


_AtmAcctngCollectMode_Type.__name__ = "Integer32"
_AtmAcctngCollectMode_Object = MibScalar
atmAcctngCollectMode = _AtmAcctngCollectMode_Object(
    (1, 3, 6, 1, 2, 1, 59, 1, 1, 12),
    _AtmAcctngCollectMode_Type()
)
atmAcctngCollectMode.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    atmAcctngCollectMode.setStatus("current")
_AtmAcctngReleaseCause_Type = Integer32
_AtmAcctngReleaseCause_Object = MibScalar
atmAcctngReleaseCause = _AtmAcctngReleaseCause_Object(
    (1, 3, 6, 1, 2, 1, 59, 1, 1, 13),
    _AtmAcctngReleaseCause_Type()
)
atmAcctngReleaseCause.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    atmAcctngReleaseCause.setStatus("current")


class _AtmAcctngServiceCategory_Type(Integer32):
    """Custom type atmAcctngServiceCategory based on Integer32"""
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
        *(("abr", 5),
          ("cbr", 2),
          ("other", 1),
          ("ubr", 6),
          ("unknown", 7),
          ("vbrNrt", 4),
          ("vbrRt", 3))
    )


_AtmAcctngServiceCategory_Type.__name__ = "Integer32"
_AtmAcctngServiceCategory_Object = MibScalar
atmAcctngServiceCategory = _AtmAcctngServiceCategory_Object(
    (1, 3, 6, 1, 2, 1, 59, 1, 1, 14),
    _AtmAcctngServiceCategory_Type()
)
atmAcctngServiceCategory.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    atmAcctngServiceCategory.setStatus("current")
_AtmAcctngTransmittedCells_Type = Counter64
_AtmAcctngTransmittedCells_Object = MibScalar
atmAcctngTransmittedCells = _AtmAcctngTransmittedCells_Object(
    (1, 3, 6, 1, 2, 1, 59, 1, 1, 15),
    _AtmAcctngTransmittedCells_Type()
)
atmAcctngTransmittedCells.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    atmAcctngTransmittedCells.setStatus("current")
_AtmAcctngTransmittedClp0Cells_Type = Counter64
_AtmAcctngTransmittedClp0Cells_Object = MibScalar
atmAcctngTransmittedClp0Cells = _AtmAcctngTransmittedClp0Cells_Object(
    (1, 3, 6, 1, 2, 1, 59, 1, 1, 16),
    _AtmAcctngTransmittedClp0Cells_Type()
)
atmAcctngTransmittedClp0Cells.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    atmAcctngTransmittedClp0Cells.setStatus("current")
_AtmAcctngReceivedCells_Type = Counter64
_AtmAcctngReceivedCells_Object = MibScalar
atmAcctngReceivedCells = _AtmAcctngReceivedCells_Object(
    (1, 3, 6, 1, 2, 1, 59, 1, 1, 17),
    _AtmAcctngReceivedCells_Type()
)
atmAcctngReceivedCells.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    atmAcctngReceivedCells.setStatus("current")
_AtmAcctngReceivedClp0Cells_Type = Counter64
_AtmAcctngReceivedClp0Cells_Object = MibScalar
atmAcctngReceivedClp0Cells = _AtmAcctngReceivedClp0Cells_Object(
    (1, 3, 6, 1, 2, 1, 59, 1, 1, 18),
    _AtmAcctngReceivedClp0Cells_Type()
)
atmAcctngReceivedClp0Cells.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    atmAcctngReceivedClp0Cells.setStatus("current")
_AtmAcctngTransmitTrafficDescriptorType_Type = ObjectIdentifier
_AtmAcctngTransmitTrafficDescriptorType_Object = MibScalar
atmAcctngTransmitTrafficDescriptorType = _AtmAcctngTransmitTrafficDescriptorType_Object(
    (1, 3, 6, 1, 2, 1, 59, 1, 1, 19),
    _AtmAcctngTransmitTrafficDescriptorType_Type()
)
atmAcctngTransmitTrafficDescriptorType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    atmAcctngTransmitTrafficDescriptorType.setStatus("current")


class _AtmAcctngTransmitTrafficDescriptorParam1_Type(Integer32):
    """Custom type atmAcctngTransmitTrafficDescriptorParam1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AtmAcctngTransmitTrafficDescriptorParam1_Type.__name__ = "Integer32"
_AtmAcctngTransmitTrafficDescriptorParam1_Object = MibScalar
atmAcctngTransmitTrafficDescriptorParam1 = _AtmAcctngTransmitTrafficDescriptorParam1_Object(
    (1, 3, 6, 1, 2, 1, 59, 1, 1, 20),
    _AtmAcctngTransmitTrafficDescriptorParam1_Type()
)
atmAcctngTransmitTrafficDescriptorParam1.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    atmAcctngTransmitTrafficDescriptorParam1.setStatus("current")


class _AtmAcctngTransmitTrafficDescriptorParam2_Type(Integer32):
    """Custom type atmAcctngTransmitTrafficDescriptorParam2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AtmAcctngTransmitTrafficDescriptorParam2_Type.__name__ = "Integer32"
_AtmAcctngTransmitTrafficDescriptorParam2_Object = MibScalar
atmAcctngTransmitTrafficDescriptorParam2 = _AtmAcctngTransmitTrafficDescriptorParam2_Object(
    (1, 3, 6, 1, 2, 1, 59, 1, 1, 21),
    _AtmAcctngTransmitTrafficDescriptorParam2_Type()
)
atmAcctngTransmitTrafficDescriptorParam2.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    atmAcctngTransmitTrafficDescriptorParam2.setStatus("current")


class _AtmAcctngTransmitTrafficDescriptorParam3_Type(Integer32):
    """Custom type atmAcctngTransmitTrafficDescriptorParam3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AtmAcctngTransmitTrafficDescriptorParam3_Type.__name__ = "Integer32"
_AtmAcctngTransmitTrafficDescriptorParam3_Object = MibScalar
atmAcctngTransmitTrafficDescriptorParam3 = _AtmAcctngTransmitTrafficDescriptorParam3_Object(
    (1, 3, 6, 1, 2, 1, 59, 1, 1, 22),
    _AtmAcctngTransmitTrafficDescriptorParam3_Type()
)
atmAcctngTransmitTrafficDescriptorParam3.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    atmAcctngTransmitTrafficDescriptorParam3.setStatus("current")


class _AtmAcctngTransmitTrafficDescriptorParam4_Type(Integer32):
    """Custom type atmAcctngTransmitTrafficDescriptorParam4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AtmAcctngTransmitTrafficDescriptorParam4_Type.__name__ = "Integer32"
_AtmAcctngTransmitTrafficDescriptorParam4_Object = MibScalar
atmAcctngTransmitTrafficDescriptorParam4 = _AtmAcctngTransmitTrafficDescriptorParam4_Object(
    (1, 3, 6, 1, 2, 1, 59, 1, 1, 23),
    _AtmAcctngTransmitTrafficDescriptorParam4_Type()
)
atmAcctngTransmitTrafficDescriptorParam4.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    atmAcctngTransmitTrafficDescriptorParam4.setStatus("current")


class _AtmAcctngTransmitTrafficDescriptorParam5_Type(Integer32):
    """Custom type atmAcctngTransmitTrafficDescriptorParam5 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AtmAcctngTransmitTrafficDescriptorParam5_Type.__name__ = "Integer32"
_AtmAcctngTransmitTrafficDescriptorParam5_Object = MibScalar
atmAcctngTransmitTrafficDescriptorParam5 = _AtmAcctngTransmitTrafficDescriptorParam5_Object(
    (1, 3, 6, 1, 2, 1, 59, 1, 1, 24),
    _AtmAcctngTransmitTrafficDescriptorParam5_Type()
)
atmAcctngTransmitTrafficDescriptorParam5.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    atmAcctngTransmitTrafficDescriptorParam5.setStatus("current")
_AtmAcctngReceiveTrafficDescriptorType_Type = ObjectIdentifier
_AtmAcctngReceiveTrafficDescriptorType_Object = MibScalar
atmAcctngReceiveTrafficDescriptorType = _AtmAcctngReceiveTrafficDescriptorType_Object(
    (1, 3, 6, 1, 2, 1, 59, 1, 1, 25),
    _AtmAcctngReceiveTrafficDescriptorType_Type()
)
atmAcctngReceiveTrafficDescriptorType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    atmAcctngReceiveTrafficDescriptorType.setStatus("current")


class _AtmAcctngReceiveTrafficDescriptorParam1_Type(Integer32):
    """Custom type atmAcctngReceiveTrafficDescriptorParam1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AtmAcctngReceiveTrafficDescriptorParam1_Type.__name__ = "Integer32"
_AtmAcctngReceiveTrafficDescriptorParam1_Object = MibScalar
atmAcctngReceiveTrafficDescriptorParam1 = _AtmAcctngReceiveTrafficDescriptorParam1_Object(
    (1, 3, 6, 1, 2, 1, 59, 1, 1, 26),
    _AtmAcctngReceiveTrafficDescriptorParam1_Type()
)
atmAcctngReceiveTrafficDescriptorParam1.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    atmAcctngReceiveTrafficDescriptorParam1.setStatus("current")


class _AtmAcctngReceiveTrafficDescriptorParam2_Type(Integer32):
    """Custom type atmAcctngReceiveTrafficDescriptorParam2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AtmAcctngReceiveTrafficDescriptorParam2_Type.__name__ = "Integer32"
_AtmAcctngReceiveTrafficDescriptorParam2_Object = MibScalar
atmAcctngReceiveTrafficDescriptorParam2 = _AtmAcctngReceiveTrafficDescriptorParam2_Object(
    (1, 3, 6, 1, 2, 1, 59, 1, 1, 27),
    _AtmAcctngReceiveTrafficDescriptorParam2_Type()
)
atmAcctngReceiveTrafficDescriptorParam2.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    atmAcctngReceiveTrafficDescriptorParam2.setStatus("current")


class _AtmAcctngReceiveTrafficDescriptorParam3_Type(Integer32):
    """Custom type atmAcctngReceiveTrafficDescriptorParam3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AtmAcctngReceiveTrafficDescriptorParam3_Type.__name__ = "Integer32"
_AtmAcctngReceiveTrafficDescriptorParam3_Object = MibScalar
atmAcctngReceiveTrafficDescriptorParam3 = _AtmAcctngReceiveTrafficDescriptorParam3_Object(
    (1, 3, 6, 1, 2, 1, 59, 1, 1, 28),
    _AtmAcctngReceiveTrafficDescriptorParam3_Type()
)
atmAcctngReceiveTrafficDescriptorParam3.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    atmAcctngReceiveTrafficDescriptorParam3.setStatus("current")


class _AtmAcctngReceiveTrafficDescriptorParam4_Type(Integer32):
    """Custom type atmAcctngReceiveTrafficDescriptorParam4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AtmAcctngReceiveTrafficDescriptorParam4_Type.__name__ = "Integer32"
_AtmAcctngReceiveTrafficDescriptorParam4_Object = MibScalar
atmAcctngReceiveTrafficDescriptorParam4 = _AtmAcctngReceiveTrafficDescriptorParam4_Object(
    (1, 3, 6, 1, 2, 1, 59, 1, 1, 29),
    _AtmAcctngReceiveTrafficDescriptorParam4_Type()
)
atmAcctngReceiveTrafficDescriptorParam4.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    atmAcctngReceiveTrafficDescriptorParam4.setStatus("current")


class _AtmAcctngReceiveTrafficDescriptorParam5_Type(Integer32):
    """Custom type atmAcctngReceiveTrafficDescriptorParam5 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AtmAcctngReceiveTrafficDescriptorParam5_Type.__name__ = "Integer32"
_AtmAcctngReceiveTrafficDescriptorParam5_Object = MibScalar
atmAcctngReceiveTrafficDescriptorParam5 = _AtmAcctngReceiveTrafficDescriptorParam5_Object(
    (1, 3, 6, 1, 2, 1, 59, 1, 1, 30),
    _AtmAcctngReceiveTrafficDescriptorParam5_Type()
)
atmAcctngReceiveTrafficDescriptorParam5.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    atmAcctngReceiveTrafficDescriptorParam5.setStatus("current")
_AtmAcctngCallingPartySubAddress_Type = AtmAddr
_AtmAcctngCallingPartySubAddress_Object = MibScalar
atmAcctngCallingPartySubAddress = _AtmAcctngCallingPartySubAddress_Object(
    (1, 3, 6, 1, 2, 1, 59, 1, 1, 31),
    _AtmAcctngCallingPartySubAddress_Type()
)
atmAcctngCallingPartySubAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    atmAcctngCallingPartySubAddress.setStatus("current")
_AtmAcctngCalledPartySubAddress_Type = AtmAddr
_AtmAcctngCalledPartySubAddress_Object = MibScalar
atmAcctngCalledPartySubAddress = _AtmAcctngCalledPartySubAddress_Object(
    (1, 3, 6, 1, 2, 1, 59, 1, 1, 32),
    _AtmAcctngCalledPartySubAddress_Type()
)
atmAcctngCalledPartySubAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    atmAcctngCalledPartySubAddress.setStatus("current")


class _AtmAcctngRecordCrc16_Type(OctetString):
    """Custom type atmAcctngRecordCrc16 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_AtmAcctngRecordCrc16_Type.__name__ = "OctetString"
_AtmAcctngRecordCrc16_Object = MibScalar
atmAcctngRecordCrc16 = _AtmAcctngRecordCrc16_Object(
    (1, 3, 6, 1, 2, 1, 59, 1, 1, 33),
    _AtmAcctngRecordCrc16_Type()
)
atmAcctngRecordCrc16.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    atmAcctngRecordCrc16.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ATM-ACCOUNTING-INFORMATION-MIB",
    **{"atmAccountingInformationMIB": atmAccountingInformationMIB,
       "atmAcctngMIBObjects": atmAcctngMIBObjects,
       "atmAcctngDataObjects": atmAcctngDataObjects,
       "atmAcctngConnectionType": atmAcctngConnectionType,
       "atmAcctngCastType": atmAcctngCastType,
       "atmAcctngIfName": atmAcctngIfName,
       "atmAcctngIfAlias": atmAcctngIfAlias,
       "atmAcctngVpi": atmAcctngVpi,
       "atmAcctngVci": atmAcctngVci,
       "atmAcctngCallingParty": atmAcctngCallingParty,
       "atmAcctngCalledParty": atmAcctngCalledParty,
       "atmAcctngCallReference": atmAcctngCallReference,
       "atmAcctngStartTime": atmAcctngStartTime,
       "atmAcctngCollectionTime": atmAcctngCollectionTime,
       "atmAcctngCollectMode": atmAcctngCollectMode,
       "atmAcctngReleaseCause": atmAcctngReleaseCause,
       "atmAcctngServiceCategory": atmAcctngServiceCategory,
       "atmAcctngTransmittedCells": atmAcctngTransmittedCells,
       "atmAcctngTransmittedClp0Cells": atmAcctngTransmittedClp0Cells,
       "atmAcctngReceivedCells": atmAcctngReceivedCells,
       "atmAcctngReceivedClp0Cells": atmAcctngReceivedClp0Cells,
       "atmAcctngTransmitTrafficDescriptorType": atmAcctngTransmitTrafficDescriptorType,
       "atmAcctngTransmitTrafficDescriptorParam1": atmAcctngTransmitTrafficDescriptorParam1,
       "atmAcctngTransmitTrafficDescriptorParam2": atmAcctngTransmitTrafficDescriptorParam2,
       "atmAcctngTransmitTrafficDescriptorParam3": atmAcctngTransmitTrafficDescriptorParam3,
       "atmAcctngTransmitTrafficDescriptorParam4": atmAcctngTransmitTrafficDescriptorParam4,
       "atmAcctngTransmitTrafficDescriptorParam5": atmAcctngTransmitTrafficDescriptorParam5,
       "atmAcctngReceiveTrafficDescriptorType": atmAcctngReceiveTrafficDescriptorType,
       "atmAcctngReceiveTrafficDescriptorParam1": atmAcctngReceiveTrafficDescriptorParam1,
       "atmAcctngReceiveTrafficDescriptorParam2": atmAcctngReceiveTrafficDescriptorParam2,
       "atmAcctngReceiveTrafficDescriptorParam3": atmAcctngReceiveTrafficDescriptorParam3,
       "atmAcctngReceiveTrafficDescriptorParam4": atmAcctngReceiveTrafficDescriptorParam4,
       "atmAcctngReceiveTrafficDescriptorParam5": atmAcctngReceiveTrafficDescriptorParam5,
       "atmAcctngCallingPartySubAddress": atmAcctngCallingPartySubAddress,
       "atmAcctngCalledPartySubAddress": atmAcctngCalledPartySubAddress,
       "atmAcctngRecordCrc16": atmAcctngRecordCrc16}
)
