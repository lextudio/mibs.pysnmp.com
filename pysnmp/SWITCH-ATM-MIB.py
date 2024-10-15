# SNMP MIB module (SWITCH-ATM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/SWITCH-ATM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:59:13 2024
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
 MacAddress,
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention")

(atmModule,) = mibBuilder.importSymbols(
    "TELESYN-ATI-TC",
    "atmModule")


# MODULE-IDENTITY

switchAtmMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 1, 1)
)
switchAtmMib.setRevisions(
        ("1997-06-20 19:00",
         "1996-10-29 19:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class IfIndexOrZero(Integer32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )



class AtmAddress(OctetString, TextualConvention):
    status = "current"
    displayHint = "1x"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(20, 20),
    )



class AtmPortIndex(Integer32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )



class AtmVpi(Integer32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
    )



class AtmVci(Integer32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1023),
    )



class AtmClientVci(Integer32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(32, 1023),
    )



class AtmLecIndex(Integer32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )



class AtmCipIndex(Integer32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )



class AtmAdminStatus(Integer32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )



class AtmOperStatus(Integer32, TextualConvention):
    status = "current"
    displayHint = "d"
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
        *(("active", 3),
          ("inactive", 2),
          ("loopBack", 4),
          ("other", 1))
    )



class AtmConnectionOperStatusCodes(Integer32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 3),
          ("unknown", 1),
          ("up", 2))
    )



class AtmTransmissionTypes(Integer32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("sonetSTS3c", 2),
          ("unknown", 1))
    )



class AtmMediaTypes(Integer32, TextualConvention):
    status = "current"
    displayHint = "d"
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
        *(("coaxCable", 2),
          ("multiModeFiber", 4),
          ("singleModeFiber", 3),
          ("unknown", 1),
          ("utp", 5))
    )



class AtmQosClass(Integer32, TextualConvention):
    status = "current"
    displayHint = "d"
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
        *(("class1", 2),
          ("class2", 3),
          ("class3", 4),
          ("class4", 5),
          ("unspecified", 1))
    )



class AtmClearStats(Integer32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clearStats", 2),
          ("noOp", 1))
    )



class AtmxArpEntryType(Integer32, TextualConvention):
    status = "current"
    displayHint = "d"
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
        *(("learnedViaArp", 2),
          ("learnedViaData", 3),
          ("other", 1),
          ("staticNonVolatile", 5),
          ("staticVolatile", 4))
    )



class AtmxVlanRange(Integer32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )



# MIB Managed Objects in the order of their OIDs

_AtmxPortGroup_ObjectIdentity = ObjectIdentity
atmxPortGroup = _AtmxPortGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 1, 1, 1)
)
_AtmxPortTable_Object = MibTable
atmxPortTable = _AtmxPortTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 1, 1, 1, 1)
)
if mibBuilder.loadTexts:
    atmxPortTable.setStatus("current")
_AtmxPortEntry_Object = MibTableRow
atmxPortEntry = _AtmxPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 1, 1, 1, 1, 1)
)
atmxPortEntry.setIndexNames(
    (0, "SWITCH-ATM-MIB", "atmxPortIndex"),
)
if mibBuilder.loadTexts:
    atmxPortEntry.setStatus("current")
_AtmxPortIndex_Type = AtmPortIndex
_AtmxPortIndex_Object = MibTableColumn
atmxPortIndex = _AtmxPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 1, 1, 1, 1, 1, 1),
    _AtmxPortIndex_Type()
)
atmxPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    atmxPortIndex.setStatus("current")


class _AtmxPortDescription_Type(DisplayString):
    """Custom type atmxPortDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_AtmxPortDescription_Type.__name__ = "DisplayString"
_AtmxPortDescription_Object = MibTableColumn
atmxPortDescription = _AtmxPortDescription_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 1, 1, 1, 1, 1, 2),
    _AtmxPortDescription_Type()
)
atmxPortDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmxPortDescription.setStatus("current")
_AtmxPortTransmissionType_Type = AtmTransmissionTypes
_AtmxPortTransmissionType_Object = MibTableColumn
atmxPortTransmissionType = _AtmxPortTransmissionType_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 1, 1, 1, 1, 1, 3),
    _AtmxPortTransmissionType_Type()
)
atmxPortTransmissionType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmxPortTransmissionType.setStatus("current")
_AtmxPortMediaType_Type = AtmMediaTypes
_AtmxPortMediaType_Object = MibTableColumn
atmxPortMediaType = _AtmxPortMediaType_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 1, 1, 1, 1, 1, 4),
    _AtmxPortMediaType_Type()
)
atmxPortMediaType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmxPortMediaType.setStatus("current")
_AtmxPortOperStatus_Type = AtmOperStatus
_AtmxPortOperStatus_Object = MibTableColumn
atmxPortOperStatus = _AtmxPortOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 1, 1, 1, 1, 1, 5),
    _AtmxPortOperStatus_Type()
)
atmxPortOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmxPortOperStatus.setStatus("current")


class _AtmxPortMaxVCCs_Type(Integer32):
    """Custom type atmxPortMaxVCCs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1023),
    )


_AtmxPortMaxVCCs_Type.__name__ = "Integer32"
_AtmxPortMaxVCCs_Object = MibTableColumn
atmxPortMaxVCCs = _AtmxPortMaxVCCs_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 1, 1, 1, 1, 1, 6),
    _AtmxPortMaxVCCs_Type()
)
atmxPortMaxVCCs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmxPortMaxVCCs.setStatus("current")


class _AtmxPortMaxVciBits_Type(Integer32):
    """Custom type atmxPortMaxVciBits based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_AtmxPortMaxVciBits_Type.__name__ = "Integer32"
_AtmxPortMaxVciBits_Object = MibTableColumn
atmxPortMaxVciBits = _AtmxPortMaxVciBits_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 1, 1, 1, 1, 1, 7),
    _AtmxPortMaxVciBits_Type()
)
atmxPortMaxVciBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmxPortMaxVciBits.setStatus("current")
_AtmxPortAddress_Type = AtmAddress
_AtmxPortAddress_Object = MibTableColumn
atmxPortAddress = _AtmxPortAddress_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 1, 1, 1, 1, 1, 8),
    _AtmxPortAddress_Type()
)
atmxPortAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmxPortAddress.setStatus("current")


class _AtmxPortSignalingVersion_Type(Integer32):
    """Custom type atmxPortSignalingVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ver30", 1),
          ("ver31", 2))
    )


_AtmxPortSignalingVersion_Type.__name__ = "Integer32"
_AtmxPortSignalingVersion_Object = MibTableColumn
atmxPortSignalingVersion = _AtmxPortSignalingVersion_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 1, 1, 1, 1, 1, 9),
    _AtmxPortSignalingVersion_Type()
)
atmxPortSignalingVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmxPortSignalingVersion.setStatus("current")


class _AtmxPortSignalingVci_Type(Integer32):
    """Custom type atmxPortSignalingVci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 5),
    )


_AtmxPortSignalingVci_Type.__name__ = "Integer32"
_AtmxPortSignalingVci_Object = MibTableColumn
atmxPortSignalingVci = _AtmxPortSignalingVci_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 1, 1, 1, 1, 1, 10),
    _AtmxPortSignalingVci_Type()
)
atmxPortSignalingVci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmxPortSignalingVci.setStatus("current")


class _AtmxPortILMIVci_Type(Integer32):
    """Custom type atmxPortILMIVci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 16),
    )


_AtmxPortILMIVci_Type.__name__ = "Integer32"
_AtmxPortILMIVci_Object = MibTableColumn
atmxPortILMIVci = _AtmxPortILMIVci_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 1, 1, 1, 1, 1, 11),
    _AtmxPortILMIVci_Type()
)
atmxPortILMIVci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmxPortILMIVci.setStatus("current")


class _AtmxPortEnableIlmi_Type(Integer32):
    """Custom type atmxPortEnableIlmi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2))
    )


_AtmxPortEnableIlmi_Type.__name__ = "Integer32"
_AtmxPortEnableIlmi_Object = MibTableColumn
atmxPortEnableIlmi = _AtmxPortEnableIlmi_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 1, 1, 1, 1, 1, 12),
    _AtmxPortEnableIlmi_Type()
)
atmxPortEnableIlmi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmxPortEnableIlmi.setStatus("current")


class _AtmxPortEnableIlmiPoll_Type(Integer32):
    """Custom type atmxPortEnableIlmiPoll based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2))
    )


_AtmxPortEnableIlmiPoll_Type.__name__ = "Integer32"
_AtmxPortEnableIlmiPoll_Object = MibTableColumn
atmxPortEnableIlmiPoll = _AtmxPortEnableIlmiPoll_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 1, 1, 1, 1, 1, 13),
    _AtmxPortEnableIlmiPoll_Type()
)
atmxPortEnableIlmiPoll.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmxPortEnableIlmiPoll.setStatus("current")


class _AtmxPortEnablePlScramble_Type(Integer32):
    """Custom type atmxPortEnablePlScramble based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2))
    )


_AtmxPortEnablePlScramble_Type.__name__ = "Integer32"
_AtmxPortEnablePlScramble_Object = MibTableColumn
atmxPortEnablePlScramble = _AtmxPortEnablePlScramble_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 1, 1, 1, 1, 1, 14),
    _AtmxPortEnablePlScramble_Type()
)
atmxPortEnablePlScramble.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmxPortEnablePlScramble.setStatus("current")


class _AtmxPortClock_Type(Integer32):
    """Custom type atmxPortClock based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("local", 1),
          ("loopTimed", 2))
    )


_AtmxPortClock_Type.__name__ = "Integer32"
_AtmxPortClock_Object = MibTableColumn
atmxPortClock = _AtmxPortClock_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 1, 1, 1, 1, 1, 15),
    _AtmxPortClock_Type()
)
atmxPortClock.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmxPortClock.setStatus("current")
_AtmxPortMacAddress_Type = MacAddress
_AtmxPortMacAddress_Object = MibTableColumn
atmxPortMacAddress = _AtmxPortMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 1, 1, 1, 1, 1, 16),
    _AtmxPortMacAddress_Type()
)
atmxPortMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmxPortMacAddress.setStatus("current")


class _AtmxPortAdaptorRamSize_Type(Integer32):
    """Custom type atmxPortAdaptorRamSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AtmxPortAdaptorRamSize_Type.__name__ = "Integer32"
_AtmxPortAdaptorRamSize_Object = MibTableColumn
atmxPortAdaptorRamSize = _AtmxPortAdaptorRamSize_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 1, 1, 1, 1, 1, 17),
    _AtmxPortAdaptorRamSize_Type()
)
atmxPortAdaptorRamSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmxPortAdaptorRamSize.setStatus("current")
_AtmxPortIlmiStatus_Type = AtmConnectionOperStatusCodes
_AtmxPortIlmiStatus_Object = MibTableColumn
atmxPortIlmiStatus = _AtmxPortIlmiStatus_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 1, 1, 1, 1, 1, 18),
    _AtmxPortIlmiStatus_Type()
)
atmxPortIlmiStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmxPortIlmiStatus.setStatus("current")
_AtmxPortSignalingStatus_Type = AtmConnectionOperStatusCodes
_AtmxPortSignalingStatus_Object = MibTableColumn
atmxPortSignalingStatus = _AtmxPortSignalingStatus_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 1, 1, 1, 1, 1, 19),
    _AtmxPortSignalingStatus_Type()
)
atmxPortSignalingStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmxPortSignalingStatus.setStatus("current")


class _AtmxPortSignalingMode_Type(Integer32):
    """Custom type atmxPortSignalingMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("pvc", 1),
          ("svc", 2))
    )


_AtmxPortSignalingMode_Type.__name__ = "Integer32"
_AtmxPortSignalingMode_Object = MibTableColumn
atmxPortSignalingMode = _AtmxPortSignalingMode_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 1, 1, 1, 1, 1, 20),
    _AtmxPortSignalingMode_Type()
)
atmxPortSignalingMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmxPortSignalingMode.setStatus("current")
_AtmxLecGroup_ObjectIdentity = ObjectIdentity
atmxLecGroup = _AtmxLecGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 1, 1, 2)
)
_AtmxLecTable_Object = MibTable
atmxLecTable = _AtmxLecTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 1, 1, 2, 1)
)
if mibBuilder.loadTexts:
    atmxLecTable.setStatus("current")
_AtmxLecEntry_Object = MibTableRow
atmxLecEntry = _AtmxLecEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 1, 1, 2, 1, 1)
)
atmxLecEntry.setIndexNames(
    (0, "SWITCH-ATM-MIB", "atmxLecIndex"),
)
if mibBuilder.loadTexts:
    atmxLecEntry.setStatus("current")
_AtmxLecIndex_Type = AtmLecIndex
_AtmxLecIndex_Object = MibTableColumn
atmxLecIndex = _AtmxLecIndex_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 1, 1, 2, 1, 1, 1),
    _AtmxLecIndex_Type()
)
atmxLecIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    atmxLecIndex.setStatus("current")


class _AtmxLecDescription_Type(DisplayString):
    """Custom type atmxLecDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_AtmxLecDescription_Type.__name__ = "DisplayString"
_AtmxLecDescription_Object = MibTableColumn
atmxLecDescription = _AtmxLecDescription_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 1, 1, 2, 1, 1, 2),
    _AtmxLecDescription_Type()
)
atmxLecDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmxLecDescription.setStatus("current")


class _AtmxElanName_Type(DisplayString):
    """Custom type atmxElanName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_AtmxElanName_Type.__name__ = "DisplayString"
_AtmxElanName_Object = MibTableColumn
atmxElanName = _AtmxElanName_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 1, 1, 2, 1, 1, 3),
    _AtmxElanName_Type()
)
atmxElanName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmxElanName.setStatus("current")


class _AtmxLecConfigMode_Type(Integer32):
    """Custom type atmxLecConfigMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("manual", 2))
    )


_AtmxLecConfigMode_Type.__name__ = "Integer32"
_AtmxLecConfigMode_Object = MibTableColumn
atmxLecConfigMode = _AtmxLecConfigMode_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 1, 1, 2, 1, 1, 4),
    _AtmxLecConfigMode_Type()
)
atmxLecConfigMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmxLecConfigMode.setStatus("current")
_AtmxLecServerAddress_Type = AtmAddress
_AtmxLecServerAddress_Object = MibTableColumn
atmxLecServerAddress = _AtmxLecServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 1, 1, 2, 1, 1, 5),
    _AtmxLecServerAddress_Type()
)
atmxLecServerAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmxLecServerAddress.setStatus("current")
_AtmxLecUnicastMacAddress_Type = MacAddress
_AtmxLecUnicastMacAddress_Object = MibTableColumn
atmxLecUnicastMacAddress = _AtmxLecUnicastMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 1, 1, 2, 1, 1, 6),
    _AtmxLecUnicastMacAddress_Type()
)
atmxLecUnicastMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmxLecUnicastMacAddress.setStatus("obsolete")


class _AtmxLecMaxUnknownFrameCount_Type(Integer32):
    """Custom type atmxLecMaxUnknownFrameCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_AtmxLecMaxUnknownFrameCount_Type.__name__ = "Integer32"
_AtmxLecMaxUnknownFrameCount_Object = MibTableColumn
atmxLecMaxUnknownFrameCount = _AtmxLecMaxUnknownFrameCount_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 1, 1, 2, 1, 1, 7),
    _AtmxLecMaxUnknownFrameCount_Type()
)
atmxLecMaxUnknownFrameCount.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmxLecMaxUnknownFrameCount.setStatus("current")


class _AtmxLecMaxArpRetryCount_Type(Integer32):
    """Custom type atmxLecMaxArpRetryCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_AtmxLecMaxArpRetryCount_Type.__name__ = "Integer32"
_AtmxLecMaxArpRetryCount_Object = MibTableColumn
atmxLecMaxArpRetryCount = _AtmxLecMaxArpRetryCount_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 1, 1, 2, 1, 1, 8),
    _AtmxLecMaxArpRetryCount_Type()
)
atmxLecMaxArpRetryCount.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmxLecMaxArpRetryCount.setStatus("current")


class _AtmxLecArpRespTime_Type(Integer32):
    """Custom type atmxLecArpRespTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_AtmxLecArpRespTime_Type.__name__ = "Integer32"
_AtmxLecArpRespTime_Object = MibTableColumn
atmxLecArpRespTime = _AtmxLecArpRespTime_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 1, 1, 2, 1, 1, 9),
    _AtmxLecArpRespTime_Type()
)
atmxLecArpRespTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmxLecArpRespTime.setStatus("current")


class _AtmxLecMaxUnknownFrameTime_Type(Integer32):
    """Custom type atmxLecMaxUnknownFrameTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_AtmxLecMaxUnknownFrameTime_Type.__name__ = "Integer32"
_AtmxLecMaxUnknownFrameTime_Object = MibTableColumn
atmxLecMaxUnknownFrameTime = _AtmxLecMaxUnknownFrameTime_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 1, 1, 2, 1, 1, 10),
    _AtmxLecMaxUnknownFrameTime_Type()
)
atmxLecMaxUnknownFrameTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmxLecMaxUnknownFrameTime.setStatus("current")


class _AtmxLecControlTimeout_Type(Integer32):
    """Custom type atmxLecControlTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 300),
    )


_AtmxLecControlTimeout_Type.__name__ = "Integer32"
_AtmxLecControlTimeout_Object = MibTableColumn
atmxLecControlTimeout = _AtmxLecControlTimeout_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 1, 1, 2, 1, 1, 11),
    _AtmxLecControlTimeout_Type()
)
atmxLecControlTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmxLecControlTimeout.setStatus("current")
_AtmxLecVccTimeout_Type = Unsigned32
_AtmxLecVccTimeout_Object = MibTableColumn
atmxLecVccTimeout = _AtmxLecVccTimeout_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 1, 1, 2, 1, 1, 12),
    _AtmxLecVccTimeout_Type()
)
atmxLecVccTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmxLecVccTimeout.setStatus("current")


class _AtmxLecAgeingTime_Type(Integer32):
    """Custom type atmxLecAgeingTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 300),
    )


_AtmxLecAgeingTime_Type.__name__ = "Integer32"
_AtmxLecAgeingTime_Object = MibTableColumn
atmxLecAgeingTime = _AtmxLecAgeingTime_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 1, 1, 2, 1, 1, 13),
    _AtmxLecAgeingTime_Type()
)
atmxLecAgeingTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmxLecAgeingTime.setStatus("current")


class _AtmxLecFlushTimeout_Type(Integer32):
    """Custom type atmxLecFlushTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_AtmxLecFlushTimeout_Type.__name__ = "Integer32"
_AtmxLecFlushTimeout_Object = MibTableColumn
atmxLecFlushTimeout = _AtmxLecFlushTimeout_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 1, 1, 2, 1, 1, 14),
    _AtmxLecFlushTimeout_Type()
)
atmxLecFlushTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmxLecFlushTimeout.setStatus("current")


class _AtmxLecVPortNumber_Type(Integer32):
    """Custom type atmxLecVPortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256),
    )


_AtmxLecVPortNumber_Type.__name__ = "Integer32"
_AtmxLecVPortNumber_Object = MibTableColumn
atmxLecVPortNumber = _AtmxLecVPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 1, 1, 2, 1, 1, 15),
    _AtmxLecVPortNumber_Type()
)
atmxLecVPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmxLecVPortNumber.setStatus("deprecated")


class _AtmxLecProtocolState_Type(Integer32):
    """Custom type atmxLecProtocolState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
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
        *(("active", 11),
          ("busArpReq", 8),
          ("cfgDirConReq", 12),
          ("cfgReq", 9),
          ("ctrlDirConReq", 1),
          ("ctrlDistConRsp", 2),
          ("inActive", 0),
          ("joinReq", 10),
          ("mcastFwdConRsp", 7),
          ("mcastSndConCfm", 6),
          ("mcastSndConReq", 3),
          ("mcastSndFwdConCfm", 5),
          ("mcastSndFwdConRsp", 4))
    )


_AtmxLecProtocolState_Type.__name__ = "Integer32"
_AtmxLecProtocolState_Object = MibTableColumn
atmxLecProtocolState = _AtmxLecProtocolState_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 1, 1, 2, 1, 1, 16),
    _AtmxLecProtocolState_Type()
)
atmxLecProtocolState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmxLecProtocolState.setStatus("current")
_AtmxLecRowStatus_Type = RowStatus
_AtmxLecRowStatus_Object = MibTableColumn
atmxLecRowStatus = _AtmxLecRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 1, 1, 2, 1, 1, 17),
    _AtmxLecRowStatus_Type()
)
atmxLecRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmxLecRowStatus.setStatus("current")
_AtmxLecIfIndex_Type = IfIndexOrZero
_AtmxLecIfIndex_Object = MibTableColumn
atmxLecIfIndex = _AtmxLecIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 1, 1, 2, 1, 1, 18),
    _AtmxLecIfIndex_Type()
)
atmxLecIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmxLecIfIndex.setStatus("current")


class _AtmxLecId_Type(Integer32):
    """Custom type atmxLecId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_AtmxLecId_Type.__name__ = "Integer32"
_AtmxLecId_Object = MibTableColumn
atmxLecId = _AtmxLecId_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 1, 1, 2, 1, 1, 19),
    _AtmxLecId_Type()
)
atmxLecId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmxLecId.setStatus("current")
_AtmxLecControlDirectVcc_Type = AtmVci
_AtmxLecControlDirectVcc_Object = MibTableColumn
atmxLecControlDirectVcc = _AtmxLecControlDirectVcc_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 1, 1, 2, 1, 1, 20),
    _AtmxLecControlDirectVcc_Type()
)
atmxLecControlDirectVcc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmxLecControlDirectVcc.setStatus("current")
_AtmxLecControlDistributeVcc_Type = AtmVci
_AtmxLecControlDistributeVcc_Object = MibTableColumn
atmxLecControlDistributeVcc = _AtmxLecControlDistributeVcc_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 1, 1, 2, 1, 1, 21),
    _AtmxLecControlDistributeVcc_Type()
)
atmxLecControlDistributeVcc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmxLecControlDistributeVcc.setStatus("current")
_AtmxLecMulticastSendVcc_Type = AtmVci
_AtmxLecMulticastSendVcc_Object = MibTableColumn
atmxLecMulticastSendVcc = _AtmxLecMulticastSendVcc_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 1, 1, 2, 1, 1, 22),
    _AtmxLecMulticastSendVcc_Type()
)
atmxLecMulticastSendVcc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmxLecMulticastSendVcc.setStatus("current")
_AtmxLecMulticastForwardVcc_Type = AtmVci
_AtmxLecMulticastForwardVcc_Object = MibTableColumn
atmxLecMulticastForwardVcc = _AtmxLecMulticastForwardVcc_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 1, 1, 2, 1, 1, 23),
    _AtmxLecMulticastForwardVcc_Type()
)
atmxLecMulticastForwardVcc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmxLecMulticastForwardVcc.setStatus("current")
_AtmxLecVlanNumber_Type = AtmxVlanRange
_AtmxLecVlanNumber_Object = MibTableColumn
atmxLecVlanNumber = _AtmxLecVlanNumber_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 1, 1, 2, 1, 1, 24),
    _AtmxLecVlanNumber_Type()
)
atmxLecVlanNumber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmxLecVlanNumber.setStatus("current")
_AtmxCipGroup_ObjectIdentity = ObjectIdentity
atmxCipGroup = _AtmxCipGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 1, 1, 3)
)
_AtmxCipTable_Object = MibTable
atmxCipTable = _AtmxCipTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 1, 1, 3, 1)
)
if mibBuilder.loadTexts:
    atmxCipTable.setStatus("current")
_AtmxCipEntry_Object = MibTableRow
atmxCipEntry = _AtmxCipEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 1, 1, 3, 1, 1)
)
atmxCipEntry.setIndexNames(
    (0, "SWITCH-ATM-MIB", "atmxCipIndex"),
)
if mibBuilder.loadTexts:
    atmxCipEntry.setStatus("current")
_AtmxCipIndex_Type = AtmCipIndex
_AtmxCipIndex_Object = MibTableColumn
atmxCipIndex = _AtmxCipIndex_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 1, 1, 3, 1, 1, 1),
    _AtmxCipIndex_Type()
)
atmxCipIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    atmxCipIndex.setStatus("current")


class _AtmxCipDescription_Type(DisplayString):
    """Custom type atmxCipDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_AtmxCipDescription_Type.__name__ = "DisplayString"
_AtmxCipDescription_Object = MibTableColumn
atmxCipDescription = _AtmxCipDescription_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 1, 1, 3, 1, 1, 2),
    _AtmxCipDescription_Type()
)
atmxCipDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmxCipDescription.setStatus("current")
_AtmxCipIPAddress_Type = IpAddress
_AtmxCipIPAddress_Object = MibTableColumn
atmxCipIPAddress = _AtmxCipIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 1, 1, 3, 1, 1, 3),
    _AtmxCipIPAddress_Type()
)
atmxCipIPAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmxCipIPAddress.setStatus("current")
_AtmxCipIPSubnetMask_Type = IpAddress
_AtmxCipIPSubnetMask_Object = MibTableColumn
atmxCipIPSubnetMask = _AtmxCipIPSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 1, 1, 3, 1, 1, 4),
    _AtmxCipIPSubnetMask_Type()
)
atmxCipIPSubnetMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmxCipIPSubnetMask.setStatus("current")


class _AtmxCipConnectionType_Type(Integer32):
    """Custom type atmxCipConnectionType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("pvc", 1),
          ("svc", 2))
    )


_AtmxCipConnectionType_Type.__name__ = "Integer32"
_AtmxCipConnectionType_Object = MibTableColumn
atmxCipConnectionType = _AtmxCipConnectionType_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 1, 1, 3, 1, 1, 5),
    _AtmxCipConnectionType_Type()
)
atmxCipConnectionType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmxCipConnectionType.setStatus("current")
_AtmxCipVci_Type = AtmVci
_AtmxCipVci_Object = MibTableColumn
atmxCipVci = _AtmxCipVci_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 1, 1, 3, 1, 1, 6),
    _AtmxCipVci_Type()
)
atmxCipVci.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmxCipVci.setStatus("obsolete")
_AtmxCipServerAtmAddress_Type = AtmAddress
_AtmxCipServerAtmAddress_Object = MibTableColumn
atmxCipServerAtmAddress = _AtmxCipServerAtmAddress_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 1, 1, 3, 1, 1, 7),
    _AtmxCipServerAtmAddress_Type()
)
atmxCipServerAtmAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmxCipServerAtmAddress.setStatus("current")


class _AtmxCipMtuSize_Type(Integer32):
    """Custom type atmxCipMtuSize based on Integer32"""
    defaultValue = 9160

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(64, 9180),
    )


_AtmxCipMtuSize_Type.__name__ = "Integer32"
_AtmxCipMtuSize_Object = MibTableColumn
atmxCipMtuSize = _AtmxCipMtuSize_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 1, 1, 3, 1, 1, 8),
    _AtmxCipMtuSize_Type()
)
atmxCipMtuSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmxCipMtuSize.setStatus("current")
_AtmxCipIfIndex_Type = IfIndexOrZero
_AtmxCipIfIndex_Object = MibTableColumn
atmxCipIfIndex = _AtmxCipIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 1, 1, 3, 1, 1, 9),
    _AtmxCipIfIndex_Type()
)
atmxCipIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmxCipIfIndex.setStatus("current")


class _AtmxCipProtocolState_Type(Integer32):
    """Custom type atmxCipProtocolState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 2),
          ("arpConReq", 1),
          ("inactive", 0))
    )


_AtmxCipProtocolState_Type.__name__ = "Integer32"
_AtmxCipProtocolState_Object = MibTableColumn
atmxCipProtocolState = _AtmxCipProtocolState_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 1, 1, 3, 1, 1, 10),
    _AtmxCipProtocolState_Type()
)
atmxCipProtocolState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmxCipProtocolState.setStatus("current")
_AtmxCipAdmStatus_Type = AtmAdminStatus
_AtmxCipAdmStatus_Object = MibTableColumn
atmxCipAdmStatus = _AtmxCipAdmStatus_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 1, 1, 3, 1, 1, 11),
    _AtmxCipAdmStatus_Type()
)
atmxCipAdmStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmxCipAdmStatus.setStatus("current")
_AtmxCipOperStatus_Type = AtmOperStatus
_AtmxCipOperStatus_Object = MibTableColumn
atmxCipOperStatus = _AtmxCipOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 1, 1, 3, 1, 1, 12),
    _AtmxCipOperStatus_Type()
)
atmxCipOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmxCipOperStatus.setStatus("current")
_AtmxCipRowStatus_Type = RowStatus
_AtmxCipRowStatus_Object = MibTableColumn
atmxCipRowStatus = _AtmxCipRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 1, 1, 3, 1, 1, 13),
    _AtmxCipRowStatus_Type()
)
atmxCipRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmxCipRowStatus.setStatus("current")


class _AtmxCipRipMode_Type(Integer32):
    """Custom type atmxCipRipMode based on Integer32"""
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
        *(("active", 2),
          ("deaf", 3),
          ("inactive", 4),
          ("silent", 1))
    )


_AtmxCipRipMode_Type.__name__ = "Integer32"
_AtmxCipRipMode_Object = MibTableColumn
atmxCipRipMode = _AtmxCipRipMode_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 1, 1, 3, 1, 1, 14),
    _AtmxCipRipMode_Type()
)
atmxCipRipMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmxCipRipMode.setStatus("current")
_AtmxCipVciTable_Object = MibTable
atmxCipVciTable = _AtmxCipVciTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 1, 1, 3, 2)
)
if mibBuilder.loadTexts:
    atmxCipVciTable.setStatus("current")
_AtmxCipVciEntry_Object = MibTableRow
atmxCipVciEntry = _AtmxCipVciEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 1, 1, 3, 2, 1)
)
atmxCipVciEntry.setIndexNames(
    (0, "SWITCH-ATM-MIB", "atmxCipIndex"),
    (0, "SWITCH-ATM-MIB", "atmxCipVciId"),
)
if mibBuilder.loadTexts:
    atmxCipVciEntry.setStatus("current")
_AtmxCipVciId_Type = AtmClientVci
_AtmxCipVciId_Object = MibTableColumn
atmxCipVciId = _AtmxCipVciId_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 1, 1, 3, 2, 1, 1),
    _AtmxCipVciId_Type()
)
atmxCipVciId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    atmxCipVciId.setStatus("current")
_AtmxCipVciRowStatus_Type = RowStatus
_AtmxCipVciRowStatus_Object = MibTableColumn
atmxCipVciRowStatus = _AtmxCipVciRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 1, 1, 3, 2, 1, 2),
    _AtmxCipVciRowStatus_Type()
)
atmxCipVciRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmxCipVciRowStatus.setStatus("current")
_AtmxLayerStatsGroup_ObjectIdentity = ObjectIdentity
atmxLayerStatsGroup = _AtmxLayerStatsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 1, 1, 4)
)
_AtmxLayerStatsTable_Object = MibTable
atmxLayerStatsTable = _AtmxLayerStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 1, 1, 4, 1)
)
if mibBuilder.loadTexts:
    atmxLayerStatsTable.setStatus("current")
_AtmxLayerStatsEntry_Object = MibTableRow
atmxLayerStatsEntry = _AtmxLayerStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 1, 1, 4, 1, 1)
)
atmxLayerStatsEntry.setIndexNames(
    (0, "SWITCH-ATM-MIB", "atmxPortIndex"),
)
if mibBuilder.loadTexts:
    atmxLayerStatsEntry.setStatus("current")
_AtmxLayerStatsTxCells_Type = Counter32
_AtmxLayerStatsTxCells_Object = MibTableColumn
atmxLayerStatsTxCells = _AtmxLayerStatsTxCells_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 1, 1, 4, 1, 1, 2),
    _AtmxLayerStatsTxCells_Type()
)
atmxLayerStatsTxCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmxLayerStatsTxCells.setStatus("current")
_AtmxLayerStatsRxCells_Type = Counter32
_AtmxLayerStatsRxCells_Object = MibTableColumn
atmxLayerStatsRxCells = _AtmxLayerStatsRxCells_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 1, 1, 4, 1, 1, 3),
    _AtmxLayerStatsRxCells_Type()
)
atmxLayerStatsRxCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmxLayerStatsRxCells.setStatus("current")
_AtmxLayerStatsTxCellDiscards_Type = Counter32
_AtmxLayerStatsTxCellDiscards_Object = MibTableColumn
atmxLayerStatsTxCellDiscards = _AtmxLayerStatsTxCellDiscards_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 1, 1, 4, 1, 1, 4),
    _AtmxLayerStatsTxCellDiscards_Type()
)
atmxLayerStatsTxCellDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmxLayerStatsTxCellDiscards.setStatus("current")
_AtmxLayerStatsRxCellDiscards_Type = Counter32
_AtmxLayerStatsRxCellDiscards_Object = MibTableColumn
atmxLayerStatsRxCellDiscards = _AtmxLayerStatsRxCellDiscards_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 1, 1, 4, 1, 1, 5),
    _AtmxLayerStatsRxCellDiscards_Type()
)
atmxLayerStatsRxCellDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmxLayerStatsRxCellDiscards.setStatus("current")
_AtmxLayerStatsClear_Type = AtmClearStats
_AtmxLayerStatsClear_Object = MibTableColumn
atmxLayerStatsClear = _AtmxLayerStatsClear_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 1, 1, 4, 1, 1, 6),
    _AtmxLayerStatsClear_Type()
)
atmxLayerStatsClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmxLayerStatsClear.setStatus("current")


class _AtmxLayerStatsClearTime_Type(Integer32):
    """Custom type atmxLayerStatsClearTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AtmxLayerStatsClearTime_Type.__name__ = "Integer32"
_AtmxLayerStatsClearTime_Object = MibTableColumn
atmxLayerStatsClearTime = _AtmxLayerStatsClearTime_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 1, 1, 4, 1, 1, 7),
    _AtmxLayerStatsClearTime_Type()
)
atmxLayerStatsClearTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmxLayerStatsClearTime.setStatus("current")
_Aal5LayerStatsTable_Object = MibTable
aal5LayerStatsTable = _Aal5LayerStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 1, 1, 4, 2)
)
if mibBuilder.loadTexts:
    aal5LayerStatsTable.setStatus("current")
_Aal5LayerStatsEntry_Object = MibTableRow
aal5LayerStatsEntry = _Aal5LayerStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 1, 1, 4, 2, 1)
)
aal5LayerStatsEntry.setIndexNames(
    (0, "SWITCH-ATM-MIB", "atmxPortIndex"),
)
if mibBuilder.loadTexts:
    aal5LayerStatsEntry.setStatus("current")
_Aal5LayerTxOctets_Type = Counter32
_Aal5LayerTxOctets_Object = MibTableColumn
aal5LayerTxOctets = _Aal5LayerTxOctets_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 1, 1, 4, 2, 1, 2),
    _Aal5LayerTxOctets_Type()
)
aal5LayerTxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aal5LayerTxOctets.setStatus("current")
_Aal5LayerTxCells_Type = Counter32
_Aal5LayerTxCells_Object = MibTableColumn
aal5LayerTxCells = _Aal5LayerTxCells_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 1, 1, 4, 2, 1, 3),
    _Aal5LayerTxCells_Type()
)
aal5LayerTxCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aal5LayerTxCells.setStatus("current")
_Aal5LayerTxSDUs_Type = Counter32
_Aal5LayerTxSDUs_Object = MibTableColumn
aal5LayerTxSDUs = _Aal5LayerTxSDUs_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 1, 1, 4, 2, 1, 4),
    _Aal5LayerTxSDUs_Type()
)
aal5LayerTxSDUs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aal5LayerTxSDUs.setStatus("current")
_Aal5LayerTxSDUDiscards_Type = Counter32
_Aal5LayerTxSDUDiscards_Object = MibTableColumn
aal5LayerTxSDUDiscards = _Aal5LayerTxSDUDiscards_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 1, 1, 4, 2, 1, 5),
    _Aal5LayerTxSDUDiscards_Type()
)
aal5LayerTxSDUDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aal5LayerTxSDUDiscards.setStatus("current")
_Aal5LayerTxErrors_Type = Counter32
_Aal5LayerTxErrors_Object = MibTableColumn
aal5LayerTxErrors = _Aal5LayerTxErrors_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 1, 1, 4, 2, 1, 6),
    _Aal5LayerTxErrors_Type()
)
aal5LayerTxErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aal5LayerTxErrors.setStatus("current")
_Aal5LayerRxOctets_Type = Counter32
_Aal5LayerRxOctets_Object = MibTableColumn
aal5LayerRxOctets = _Aal5LayerRxOctets_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 1, 1, 4, 2, 1, 7),
    _Aal5LayerRxOctets_Type()
)
aal5LayerRxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aal5LayerRxOctets.setStatus("current")
_Aal5LayerRxCells_Type = Counter32
_Aal5LayerRxCells_Object = MibTableColumn
aal5LayerRxCells = _Aal5LayerRxCells_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 1, 1, 4, 2, 1, 8),
    _Aal5LayerRxCells_Type()
)
aal5LayerRxCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aal5LayerRxCells.setStatus("current")
_Aal5LayerRxSDUs_Type = Counter32
_Aal5LayerRxSDUs_Object = MibTableColumn
aal5LayerRxSDUs = _Aal5LayerRxSDUs_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 1, 1, 4, 2, 1, 9),
    _Aal5LayerRxSDUs_Type()
)
aal5LayerRxSDUs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aal5LayerRxSDUs.setStatus("current")
_Aal5LayerRxSDUDiscards_Type = Counter32
_Aal5LayerRxSDUDiscards_Object = MibTableColumn
aal5LayerRxSDUDiscards = _Aal5LayerRxSDUDiscards_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 1, 1, 4, 2, 1, 10),
    _Aal5LayerRxSDUDiscards_Type()
)
aal5LayerRxSDUDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aal5LayerRxSDUDiscards.setStatus("current")
_Aal5LayerRxErrors_Type = Counter32
_Aal5LayerRxErrors_Object = MibTableColumn
aal5LayerRxErrors = _Aal5LayerRxErrors_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 1, 1, 4, 2, 1, 11),
    _Aal5LayerRxErrors_Type()
)
aal5LayerRxErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aal5LayerRxErrors.setStatus("current")
_Aal5LayerRxSarTimeouts_Type = Counter32
_Aal5LayerRxSarTimeouts_Object = MibTableColumn
aal5LayerRxSarTimeouts = _Aal5LayerRxSarTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 1, 1, 4, 2, 1, 12),
    _Aal5LayerRxSarTimeouts_Type()
)
aal5LayerRxSarTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aal5LayerRxSarTimeouts.setStatus("current")
_Aal5LayerRxCrcErrors_Type = Counter32
_Aal5LayerRxCrcErrors_Object = MibTableColumn
aal5LayerRxCrcErrors = _Aal5LayerRxCrcErrors_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 1, 1, 4, 2, 1, 13),
    _Aal5LayerRxCrcErrors_Type()
)
aal5LayerRxCrcErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aal5LayerRxCrcErrors.setStatus("current")
_Aal5LayerRxSDUInvalidSz_Type = Counter32
_Aal5LayerRxSDUInvalidSz_Object = MibTableColumn
aal5LayerRxSDUInvalidSz = _Aal5LayerRxSDUInvalidSz_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 1, 1, 4, 2, 1, 14),
    _Aal5LayerRxSDUInvalidSz_Type()
)
aal5LayerRxSDUInvalidSz.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aal5LayerRxSDUInvalidSz.setStatus("current")
_Aal5LayerClearStats_Type = AtmClearStats
_Aal5LayerClearStats_Object = MibTableColumn
aal5LayerClearStats = _Aal5LayerClearStats_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 1, 1, 4, 2, 1, 15),
    _Aal5LayerClearStats_Type()
)
aal5LayerClearStats.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aal5LayerClearStats.setStatus("current")


class _Aal5LayerStatsClearTime_Type(Integer32):
    """Custom type aal5LayerStatsClearTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Aal5LayerStatsClearTime_Type.__name__ = "Integer32"
_Aal5LayerStatsClearTime_Object = MibTableColumn
aal5LayerStatsClearTime = _Aal5LayerStatsClearTime_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 1, 1, 4, 2, 1, 16),
    _Aal5LayerStatsClearTime_Type()
)
aal5LayerStatsClearTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aal5LayerStatsClearTime.setStatus("current")
_AtmxVccStatsGroup_ObjectIdentity = ObjectIdentity
atmxVccStatsGroup = _AtmxVccStatsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 1, 1, 5)
)
_AtmxVccStatsTable_Object = MibTable
atmxVccStatsTable = _AtmxVccStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 1, 1, 5, 1)
)
if mibBuilder.loadTexts:
    atmxVccStatsTable.setStatus("current")
_AtmxVccStatsEntry_Object = MibTableRow
atmxVccStatsEntry = _AtmxVccStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 1, 1, 5, 1, 1)
)
atmxVccStatsEntry.setIndexNames(
    (0, "SWITCH-ATM-MIB", "atmxPortIndex"),
    (0, "SWITCH-ATM-MIB", "atmxVccVci"),
)
if mibBuilder.loadTexts:
    atmxVccStatsEntry.setStatus("current")
_AtmxVccStatsTxSDUs_Type = Counter32
_AtmxVccStatsTxSDUs_Object = MibTableColumn
atmxVccStatsTxSDUs = _AtmxVccStatsTxSDUs_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 1, 1, 5, 1, 1, 3),
    _AtmxVccStatsTxSDUs_Type()
)
atmxVccStatsTxSDUs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmxVccStatsTxSDUs.setStatus("current")
_AtmxVccStatsTxCells_Type = Counter32
_AtmxVccStatsTxCells_Object = MibTableColumn
atmxVccStatsTxCells = _AtmxVccStatsTxCells_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 1, 1, 5, 1, 1, 4),
    _AtmxVccStatsTxCells_Type()
)
atmxVccStatsTxCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmxVccStatsTxCells.setStatus("current")
_AtmxVccStatsTxOctets_Type = Counter32
_AtmxVccStatsTxOctets_Object = MibTableColumn
atmxVccStatsTxOctets = _AtmxVccStatsTxOctets_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 1, 1, 5, 1, 1, 5),
    _AtmxVccStatsTxOctets_Type()
)
atmxVccStatsTxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmxVccStatsTxOctets.setStatus("current")
_AtmxVccStatsRxSDUs_Type = Counter32
_AtmxVccStatsRxSDUs_Object = MibTableColumn
atmxVccStatsRxSDUs = _AtmxVccStatsRxSDUs_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 1, 1, 5, 1, 1, 6),
    _AtmxVccStatsRxSDUs_Type()
)
atmxVccStatsRxSDUs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmxVccStatsRxSDUs.setStatus("current")
_AtmxVccStatsRxCells_Type = Counter32
_AtmxVccStatsRxCells_Object = MibTableColumn
atmxVccStatsRxCells = _AtmxVccStatsRxCells_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 1, 1, 5, 1, 1, 7),
    _AtmxVccStatsRxCells_Type()
)
atmxVccStatsRxCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmxVccStatsRxCells.setStatus("current")
_AtmxVccStatsRxOctets_Type = Counter32
_AtmxVccStatsRxOctets_Object = MibTableColumn
atmxVccStatsRxOctets = _AtmxVccStatsRxOctets_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 1, 1, 5, 1, 1, 8),
    _AtmxVccStatsRxOctets_Type()
)
atmxVccStatsRxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmxVccStatsRxOctets.setStatus("current")
_AtmxVccStatsTxSDUDiscards_Type = Counter32
_AtmxVccStatsTxSDUDiscards_Object = MibTableColumn
atmxVccStatsTxSDUDiscards = _AtmxVccStatsTxSDUDiscards_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 1, 1, 5, 1, 1, 9),
    _AtmxVccStatsTxSDUDiscards_Type()
)
atmxVccStatsTxSDUDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmxVccStatsTxSDUDiscards.setStatus("current")
_AtmxVccStatsTxErrors_Type = Counter32
_AtmxVccStatsTxErrors_Object = MibTableColumn
atmxVccStatsTxErrors = _AtmxVccStatsTxErrors_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 1, 1, 5, 1, 1, 10),
    _AtmxVccStatsTxErrors_Type()
)
atmxVccStatsTxErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmxVccStatsTxErrors.setStatus("current")
_AtmxVccStatsRxSDUDiscards_Type = Counter32
_AtmxVccStatsRxSDUDiscards_Object = MibTableColumn
atmxVccStatsRxSDUDiscards = _AtmxVccStatsRxSDUDiscards_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 1, 1, 5, 1, 1, 11),
    _AtmxVccStatsRxSDUDiscards_Type()
)
atmxVccStatsRxSDUDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmxVccStatsRxSDUDiscards.setStatus("current")
_AtmxVccStatsRxErrors_Type = Counter32
_AtmxVccStatsRxErrors_Object = MibTableColumn
atmxVccStatsRxErrors = _AtmxVccStatsRxErrors_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 1, 1, 5, 1, 1, 12),
    _AtmxVccStatsRxErrors_Type()
)
atmxVccStatsRxErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmxVccStatsRxErrors.setStatus("current")
_AtmxVccStatsRxSarTimeouts_Type = Counter32
_AtmxVccStatsRxSarTimeouts_Object = MibTableColumn
atmxVccStatsRxSarTimeouts = _AtmxVccStatsRxSarTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 1, 1, 5, 1, 1, 13),
    _AtmxVccStatsRxSarTimeouts_Type()
)
atmxVccStatsRxSarTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmxVccStatsRxSarTimeouts.setStatus("current")
_AtmxVccStatsRxCrcErrors_Type = Counter32
_AtmxVccStatsRxCrcErrors_Object = MibTableColumn
atmxVccStatsRxCrcErrors = _AtmxVccStatsRxCrcErrors_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 1, 1, 5, 1, 1, 14),
    _AtmxVccStatsRxCrcErrors_Type()
)
atmxVccStatsRxCrcErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmxVccStatsRxCrcErrors.setStatus("current")
_AtmxVccStatsRxOversizedSdus_Type = Counter32
_AtmxVccStatsRxOversizedSdus_Object = MibTableColumn
atmxVccStatsRxOversizedSdus = _AtmxVccStatsRxOversizedSdus_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 1, 1, 5, 1, 1, 15),
    _AtmxVccStatsRxOversizedSdus_Type()
)
atmxVccStatsRxOversizedSdus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmxVccStatsRxOversizedSdus.setStatus("current")


class _AtmxVccStatsConnCreateTime_Type(Integer32):
    """Custom type atmxVccStatsConnCreateTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AtmxVccStatsConnCreateTime_Type.__name__ = "Integer32"
_AtmxVccStatsConnCreateTime_Object = MibTableColumn
atmxVccStatsConnCreateTime = _AtmxVccStatsConnCreateTime_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 1, 1, 5, 1, 1, 16),
    _AtmxVccStatsConnCreateTime_Type()
)
atmxVccStatsConnCreateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmxVccStatsConnCreateTime.setStatus("current")


class _AtmxVccStatsConnInIdleTime_Type(Integer32):
    """Custom type atmxVccStatsConnInIdleTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AtmxVccStatsConnInIdleTime_Type.__name__ = "Integer32"
_AtmxVccStatsConnInIdleTime_Object = MibTableColumn
atmxVccStatsConnInIdleTime = _AtmxVccStatsConnInIdleTime_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 1, 1, 5, 1, 1, 17),
    _AtmxVccStatsConnInIdleTime_Type()
)
atmxVccStatsConnInIdleTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmxVccStatsConnInIdleTime.setStatus("current")


class _AtmxVccStatsConnOutIdleTime_Type(Integer32):
    """Custom type atmxVccStatsConnOutIdleTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AtmxVccStatsConnOutIdleTime_Type.__name__ = "Integer32"
_AtmxVccStatsConnOutIdleTime_Object = MibTableColumn
atmxVccStatsConnOutIdleTime = _AtmxVccStatsConnOutIdleTime_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 1, 1, 5, 1, 1, 18),
    _AtmxVccStatsConnOutIdleTime_Type()
)
atmxVccStatsConnOutIdleTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmxVccStatsConnOutIdleTime.setStatus("current")


class _AtmxVccStatsConnModifiedTime_Type(Integer32):
    """Custom type atmxVccStatsConnModifiedTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AtmxVccStatsConnModifiedTime_Type.__name__ = "Integer32"
_AtmxVccStatsConnModifiedTime_Object = MibTableColumn
atmxVccStatsConnModifiedTime = _AtmxVccStatsConnModifiedTime_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 1, 1, 5, 1, 1, 19),
    _AtmxVccStatsConnModifiedTime_Type()
)
atmxVccStatsConnModifiedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmxVccStatsConnModifiedTime.setStatus("current")
_AtmxLecStatsGroup_ObjectIdentity = ObjectIdentity
atmxLecStatsGroup = _AtmxLecStatsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 1, 1, 6)
)
_AtmxLecStatsTable_Object = MibTable
atmxLecStatsTable = _AtmxLecStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 1, 1, 6, 1)
)
if mibBuilder.loadTexts:
    atmxLecStatsTable.setStatus("current")
_AtmxLecStatsEntry_Object = MibTableRow
atmxLecStatsEntry = _AtmxLecStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 1, 1, 6, 1, 1)
)
atmxLecStatsEntry.setIndexNames(
    (0, "SWITCH-ATM-MIB", "atmxLecIndex"),
)
if mibBuilder.loadTexts:
    atmxLecStatsEntry.setStatus("current")
_AtmxLecStatsTxArpReq_Type = Counter32
_AtmxLecStatsTxArpReq_Object = MibTableColumn
atmxLecStatsTxArpReq = _AtmxLecStatsTxArpReq_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 1, 1, 6, 1, 1, 2),
    _AtmxLecStatsTxArpReq_Type()
)
atmxLecStatsTxArpReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmxLecStatsTxArpReq.setStatus("current")
_AtmxLecStatsTxArpRsp_Type = Counter32
_AtmxLecStatsTxArpRsp_Object = MibTableColumn
atmxLecStatsTxArpRsp = _AtmxLecStatsTxArpRsp_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 1, 1, 6, 1, 1, 3),
    _AtmxLecStatsTxArpRsp_Type()
)
atmxLecStatsTxArpRsp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmxLecStatsTxArpRsp.setStatus("current")
_AtmxLecStatsTxControlPkts_Type = Counter32
_AtmxLecStatsTxControlPkts_Object = MibTableColumn
atmxLecStatsTxControlPkts = _AtmxLecStatsTxControlPkts_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 1, 1, 6, 1, 1, 4),
    _AtmxLecStatsTxControlPkts_Type()
)
atmxLecStatsTxControlPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmxLecStatsTxControlPkts.setStatus("current")
_AtmxLecStatsTxUnicastPkts_Type = Counter32
_AtmxLecStatsTxUnicastPkts_Object = MibTableColumn
atmxLecStatsTxUnicastPkts = _AtmxLecStatsTxUnicastPkts_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 1, 1, 6, 1, 1, 5),
    _AtmxLecStatsTxUnicastPkts_Type()
)
atmxLecStatsTxUnicastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmxLecStatsTxUnicastPkts.setStatus("current")
_AtmxLecStatsTxMulticastPkts_Type = Counter32
_AtmxLecStatsTxMulticastPkts_Object = MibTableColumn
atmxLecStatsTxMulticastPkts = _AtmxLecStatsTxMulticastPkts_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 1, 1, 6, 1, 1, 6),
    _AtmxLecStatsTxMulticastPkts_Type()
)
atmxLecStatsTxMulticastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmxLecStatsTxMulticastPkts.setStatus("current")
_AtmxLecStatsTxBroadcastPkts_Type = Counter32
_AtmxLecStatsTxBroadcastPkts_Object = MibTableColumn
atmxLecStatsTxBroadcastPkts = _AtmxLecStatsTxBroadcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 1, 1, 6, 1, 1, 7),
    _AtmxLecStatsTxBroadcastPkts_Type()
)
atmxLecStatsTxBroadcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmxLecStatsTxBroadcastPkts.setStatus("current")
_AtmxLecStatsTxDiscardPkts_Type = Counter32
_AtmxLecStatsTxDiscardPkts_Object = MibTableColumn
atmxLecStatsTxDiscardPkts = _AtmxLecStatsTxDiscardPkts_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 1, 1, 6, 1, 1, 8),
    _AtmxLecStatsTxDiscardPkts_Type()
)
atmxLecStatsTxDiscardPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmxLecStatsTxDiscardPkts.setStatus("current")
_AtmxLecStatsRxArpReq_Type = Counter32
_AtmxLecStatsRxArpReq_Object = MibTableColumn
atmxLecStatsRxArpReq = _AtmxLecStatsRxArpReq_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 1, 1, 6, 1, 1, 9),
    _AtmxLecStatsRxArpReq_Type()
)
atmxLecStatsRxArpReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmxLecStatsRxArpReq.setStatus("current")
_AtmxLecStatsRxArpRsp_Type = Counter32
_AtmxLecStatsRxArpRsp_Object = MibTableColumn
atmxLecStatsRxArpRsp = _AtmxLecStatsRxArpRsp_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 1, 1, 6, 1, 1, 10),
    _AtmxLecStatsRxArpRsp_Type()
)
atmxLecStatsRxArpRsp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmxLecStatsRxArpRsp.setStatus("current")
_AtmxLecStatsRxControlPkts_Type = Counter32
_AtmxLecStatsRxControlPkts_Object = MibTableColumn
atmxLecStatsRxControlPkts = _AtmxLecStatsRxControlPkts_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 1, 1, 6, 1, 1, 11),
    _AtmxLecStatsRxControlPkts_Type()
)
atmxLecStatsRxControlPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmxLecStatsRxControlPkts.setStatus("current")
_AtmxLecStatsRxUnicastPkts_Type = Counter32
_AtmxLecStatsRxUnicastPkts_Object = MibTableColumn
atmxLecStatsRxUnicastPkts = _AtmxLecStatsRxUnicastPkts_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 1, 1, 6, 1, 1, 12),
    _AtmxLecStatsRxUnicastPkts_Type()
)
atmxLecStatsRxUnicastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmxLecStatsRxUnicastPkts.setStatus("current")
_AtmxLecStatsRxMulticastPkts_Type = Counter32
_AtmxLecStatsRxMulticastPkts_Object = MibTableColumn
atmxLecStatsRxMulticastPkts = _AtmxLecStatsRxMulticastPkts_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 1, 1, 6, 1, 1, 13),
    _AtmxLecStatsRxMulticastPkts_Type()
)
atmxLecStatsRxMulticastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmxLecStatsRxMulticastPkts.setStatus("current")
_AtmxLecStatsRxBroadcastPkts_Type = Counter32
_AtmxLecStatsRxBroadcastPkts_Object = MibTableColumn
atmxLecStatsRxBroadcastPkts = _AtmxLecStatsRxBroadcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 1, 1, 6, 1, 1, 14),
    _AtmxLecStatsRxBroadcastPkts_Type()
)
atmxLecStatsRxBroadcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmxLecStatsRxBroadcastPkts.setStatus("current")
_AtmxLecStatsRxDiscardPkts_Type = Counter32
_AtmxLecStatsRxDiscardPkts_Object = MibTableColumn
atmxLecStatsRxDiscardPkts = _AtmxLecStatsRxDiscardPkts_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 1, 1, 6, 1, 1, 15),
    _AtmxLecStatsRxDiscardPkts_Type()
)
atmxLecStatsRxDiscardPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmxLecStatsRxDiscardPkts.setStatus("current")
_AtmxCipStatsGroup_ObjectIdentity = ObjectIdentity
atmxCipStatsGroup = _AtmxCipStatsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 1, 1, 7)
)
_AtmxCipStatsTable_Object = MibTable
atmxCipStatsTable = _AtmxCipStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 1, 1, 7, 1)
)
if mibBuilder.loadTexts:
    atmxCipStatsTable.setStatus("current")
_AtmxCipStatsEntry_Object = MibTableRow
atmxCipStatsEntry = _AtmxCipStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 1, 1, 7, 1, 1)
)
atmxCipStatsEntry.setIndexNames(
    (0, "SWITCH-ATM-MIB", "atmxCipIndex"),
)
if mibBuilder.loadTexts:
    atmxCipStatsEntry.setStatus("current")
_AtmxCipStatsPktsFromOtherLIS_Type = Counter32
_AtmxCipStatsPktsFromOtherLIS_Object = MibTableColumn
atmxCipStatsPktsFromOtherLIS = _AtmxCipStatsPktsFromOtherLIS_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 1, 1, 7, 1, 1, 2),
    _AtmxCipStatsPktsFromOtherLIS_Type()
)
atmxCipStatsPktsFromOtherLIS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmxCipStatsPktsFromOtherLIS.setStatus("current")
_AtmxCipStatsTxArpReq_Type = Counter32
_AtmxCipStatsTxArpReq_Object = MibTableColumn
atmxCipStatsTxArpReq = _AtmxCipStatsTxArpReq_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 1, 1, 7, 1, 1, 3),
    _AtmxCipStatsTxArpReq_Type()
)
atmxCipStatsTxArpReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmxCipStatsTxArpReq.setStatus("current")
_AtmxCipStatsTxArpRsp_Type = Counter32
_AtmxCipStatsTxArpRsp_Object = MibTableColumn
atmxCipStatsTxArpRsp = _AtmxCipStatsTxArpRsp_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 1, 1, 7, 1, 1, 4),
    _AtmxCipStatsTxArpRsp_Type()
)
atmxCipStatsTxArpRsp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmxCipStatsTxArpRsp.setStatus("current")
_AtmxCipStatsTxInArpReq_Type = Counter32
_AtmxCipStatsTxInArpReq_Object = MibTableColumn
atmxCipStatsTxInArpReq = _AtmxCipStatsTxInArpReq_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 1, 1, 7, 1, 1, 5),
    _AtmxCipStatsTxInArpReq_Type()
)
atmxCipStatsTxInArpReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmxCipStatsTxInArpReq.setStatus("current")
_AtmxCipStatsTxInArpRsp_Type = Counter32
_AtmxCipStatsTxInArpRsp_Object = MibTableColumn
atmxCipStatsTxInArpRsp = _AtmxCipStatsTxInArpRsp_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 1, 1, 7, 1, 1, 6),
    _AtmxCipStatsTxInArpRsp_Type()
)
atmxCipStatsTxInArpRsp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmxCipStatsTxInArpRsp.setStatus("current")
_AtmxCipStatsTxDiscards_Type = Counter32
_AtmxCipStatsTxDiscards_Object = MibTableColumn
atmxCipStatsTxDiscards = _AtmxCipStatsTxDiscards_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 1, 1, 7, 1, 1, 7),
    _AtmxCipStatsTxDiscards_Type()
)
atmxCipStatsTxDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmxCipStatsTxDiscards.setStatus("current")
_AtmxCipStatsRxArpReq_Type = Counter32
_AtmxCipStatsRxArpReq_Object = MibTableColumn
atmxCipStatsRxArpReq = _AtmxCipStatsRxArpReq_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 1, 1, 7, 1, 1, 8),
    _AtmxCipStatsRxArpReq_Type()
)
atmxCipStatsRxArpReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmxCipStatsRxArpReq.setStatus("current")
_AtmxCipStatsRxArpRsp_Type = Counter32
_AtmxCipStatsRxArpRsp_Object = MibTableColumn
atmxCipStatsRxArpRsp = _AtmxCipStatsRxArpRsp_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 1, 1, 7, 1, 1, 9),
    _AtmxCipStatsRxArpRsp_Type()
)
atmxCipStatsRxArpRsp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmxCipStatsRxArpRsp.setStatus("current")
_AtmxCipStatsRxInArpReq_Type = Counter32
_AtmxCipStatsRxInArpReq_Object = MibTableColumn
atmxCipStatsRxInArpReq = _AtmxCipStatsRxInArpReq_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 1, 1, 7, 1, 1, 10),
    _AtmxCipStatsRxInArpReq_Type()
)
atmxCipStatsRxInArpReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmxCipStatsRxInArpReq.setStatus("current")
_AtmxCipStatsRxInArpRsp_Type = Counter32
_AtmxCipStatsRxInArpRsp_Object = MibTableColumn
atmxCipStatsRxInArpRsp = _AtmxCipStatsRxInArpRsp_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 1, 1, 7, 1, 1, 11),
    _AtmxCipStatsRxInArpRsp_Type()
)
atmxCipStatsRxInArpRsp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmxCipStatsRxInArpRsp.setStatus("current")
_AtmxCipStatsRxDiscards_Type = Counter32
_AtmxCipStatsRxDiscards_Object = MibTableColumn
atmxCipStatsRxDiscards = _AtmxCipStatsRxDiscards_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 1, 1, 7, 1, 1, 12),
    _AtmxCipStatsRxDiscards_Type()
)
atmxCipStatsRxDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmxCipStatsRxDiscards.setStatus("current")
_AtmxSscopStatsGroup_ObjectIdentity = ObjectIdentity
atmxSscopStatsGroup = _AtmxSscopStatsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 1, 1, 8)
)
_AtmxSscopStatsTable_Object = MibTable
atmxSscopStatsTable = _AtmxSscopStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 1, 1, 8, 1)
)
if mibBuilder.loadTexts:
    atmxSscopStatsTable.setStatus("current")
_AtmxSscopStatsEntry_Object = MibTableRow
atmxSscopStatsEntry = _AtmxSscopStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 1, 1, 8, 1, 1)
)
atmxSscopStatsEntry.setIndexNames(
    (0, "SWITCH-ATM-MIB", "atmxPortIndex"),
)
if mibBuilder.loadTexts:
    atmxSscopStatsEntry.setStatus("current")
_AtmxSscopStatsTxTotalPdus_Type = Counter32
_AtmxSscopStatsTxTotalPdus_Object = MibTableColumn
atmxSscopStatsTxTotalPdus = _AtmxSscopStatsTxTotalPdus_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 1, 1, 8, 1, 1, 1),
    _AtmxSscopStatsTxTotalPdus_Type()
)
atmxSscopStatsTxTotalPdus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmxSscopStatsTxTotalPdus.setStatus("current")
_AtmxSscopStatsTxDiscardSdus_Type = Counter32
_AtmxSscopStatsTxDiscardSdus_Object = MibTableColumn
atmxSscopStatsTxDiscardSdus = _AtmxSscopStatsTxDiscardSdus_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 1, 1, 8, 1, 1, 2),
    _AtmxSscopStatsTxDiscardSdus_Type()
)
atmxSscopStatsTxDiscardSdus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmxSscopStatsTxDiscardSdus.setStatus("current")
_AtmxSscopStatsTxDiscardPdus_Type = Counter32
_AtmxSscopStatsTxDiscardPdus_Object = MibTableColumn
atmxSscopStatsTxDiscardPdus = _AtmxSscopStatsTxDiscardPdus_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 1, 1, 8, 1, 1, 3),
    _AtmxSscopStatsTxDiscardPdus_Type()
)
atmxSscopStatsTxDiscardPdus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmxSscopStatsTxDiscardPdus.setStatus("current")
_AtmxSscopStatsTxErrorPdus_Type = Counter32
_AtmxSscopStatsTxErrorPdus_Object = MibTableColumn
atmxSscopStatsTxErrorPdus = _AtmxSscopStatsTxErrorPdus_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 1, 1, 8, 1, 1, 4),
    _AtmxSscopStatsTxErrorPdus_Type()
)
atmxSscopStatsTxErrorPdus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmxSscopStatsTxErrorPdus.setStatus("current")
_AtmxSscopStatsTxBufferInUseCtr_Type = Counter32
_AtmxSscopStatsTxBufferInUseCtr_Object = MibTableColumn
atmxSscopStatsTxBufferInUseCtr = _AtmxSscopStatsTxBufferInUseCtr_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 1, 1, 8, 1, 1, 5),
    _AtmxSscopStatsTxBufferInUseCtr_Type()
)
atmxSscopStatsTxBufferInUseCtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmxSscopStatsTxBufferInUseCtr.setStatus("current")
_AtmxSscopStatsTxBufferInUseGauge_Type = Gauge32
_AtmxSscopStatsTxBufferInUseGauge_Object = MibTableColumn
atmxSscopStatsTxBufferInUseGauge = _AtmxSscopStatsTxBufferInUseGauge_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 1, 1, 8, 1, 1, 6),
    _AtmxSscopStatsTxBufferInUseGauge_Type()
)
atmxSscopStatsTxBufferInUseGauge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmxSscopStatsTxBufferInUseGauge.setStatus("current")
_AtmxSscopStatsRxTotalPdus_Type = Counter32
_AtmxSscopStatsRxTotalPdus_Object = MibTableColumn
atmxSscopStatsRxTotalPdus = _AtmxSscopStatsRxTotalPdus_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 1, 1, 8, 1, 1, 7),
    _AtmxSscopStatsRxTotalPdus_Type()
)
atmxSscopStatsRxTotalPdus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmxSscopStatsRxTotalPdus.setStatus("current")
_AtmxSscopStatsRxDiscardPdus_Type = Counter32
_AtmxSscopStatsRxDiscardPdus_Object = MibTableColumn
atmxSscopStatsRxDiscardPdus = _AtmxSscopStatsRxDiscardPdus_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 1, 1, 8, 1, 1, 8),
    _AtmxSscopStatsRxDiscardPdus_Type()
)
atmxSscopStatsRxDiscardPdus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmxSscopStatsRxDiscardPdus.setStatus("current")
_AtmxSscopStatsRxErrorPdus_Type = Counter32
_AtmxSscopStatsRxErrorPdus_Object = MibTableColumn
atmxSscopStatsRxErrorPdus = _AtmxSscopStatsRxErrorPdus_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 1, 1, 8, 1, 1, 9),
    _AtmxSscopStatsRxErrorPdus_Type()
)
atmxSscopStatsRxErrorPdus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmxSscopStatsRxErrorPdus.setStatus("current")
_AtmxSscopStatsRxBufferInUseCtr_Type = Counter32
_AtmxSscopStatsRxBufferInUseCtr_Object = MibTableColumn
atmxSscopStatsRxBufferInUseCtr = _AtmxSscopStatsRxBufferInUseCtr_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 1, 1, 8, 1, 1, 10),
    _AtmxSscopStatsRxBufferInUseCtr_Type()
)
atmxSscopStatsRxBufferInUseCtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmxSscopStatsRxBufferInUseCtr.setStatus("current")
_AtmxSscopStatsRxBufferInUseGauge_Type = Gauge32
_AtmxSscopStatsRxBufferInUseGauge_Object = MibTableColumn
atmxSscopStatsRxBufferInUseGauge = _AtmxSscopStatsRxBufferInUseGauge_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 1, 1, 8, 1, 1, 11),
    _AtmxSscopStatsRxBufferInUseGauge_Type()
)
atmxSscopStatsRxBufferInUseGauge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmxSscopStatsRxBufferInUseGauge.setStatus("current")
_AtmxIlmiStatsGroup_ObjectIdentity = ObjectIdentity
atmxIlmiStatsGroup = _AtmxIlmiStatsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 1, 1, 9)
)
_AtmxIlmiStatsTable_Object = MibTable
atmxIlmiStatsTable = _AtmxIlmiStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 1, 1, 9, 1)
)
if mibBuilder.loadTexts:
    atmxIlmiStatsTable.setStatus("current")
_AtmxIlmiStatsEntry_Object = MibTableRow
atmxIlmiStatsEntry = _AtmxIlmiStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 1, 1, 9, 1, 1)
)
atmxIlmiStatsEntry.setIndexNames(
    (0, "SWITCH-ATM-MIB", "atmxPortIndex"),
)
if mibBuilder.loadTexts:
    atmxIlmiStatsEntry.setStatus("current")
_AtmxIlmiTxPDUs_Type = Counter32
_AtmxIlmiTxPDUs_Object = MibTableColumn
atmxIlmiTxPDUs = _AtmxIlmiTxPDUs_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 1, 1, 9, 1, 1, 2),
    _AtmxIlmiTxPDUs_Type()
)
atmxIlmiTxPDUs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmxIlmiTxPDUs.setStatus("current")
_AtmxIlmiRxPDUs_Type = Counter32
_AtmxIlmiRxPDUs_Object = MibTableColumn
atmxIlmiRxPDUs = _AtmxIlmiRxPDUs_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 1, 1, 9, 1, 1, 3),
    _AtmxIlmiRxPDUs_Type()
)
atmxIlmiRxPDUs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmxIlmiRxPDUs.setStatus("current")
_AtmxIlmiRxDiscardPDUs_Type = Counter32
_AtmxIlmiRxDiscardPDUs_Object = MibTableColumn
atmxIlmiRxDiscardPDUs = _AtmxIlmiRxDiscardPDUs_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 1, 1, 9, 1, 1, 4),
    _AtmxIlmiRxDiscardPDUs_Type()
)
atmxIlmiRxDiscardPDUs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmxIlmiRxDiscardPDUs.setStatus("current")
_AtmxVccGroup_ObjectIdentity = ObjectIdentity
atmxVccGroup = _AtmxVccGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 1, 1, 10)
)
_AtmxVccTable_Object = MibTable
atmxVccTable = _AtmxVccTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 1, 1, 10, 1)
)
if mibBuilder.loadTexts:
    atmxVccTable.setStatus("current")
_AtmxVccEntry_Object = MibTableRow
atmxVccEntry = _AtmxVccEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 1, 1, 10, 1, 1)
)
atmxVccEntry.setIndexNames(
    (0, "SWITCH-ATM-MIB", "atmxPortIndex"),
    (0, "SWITCH-ATM-MIB", "atmxVccVci"),
)
if mibBuilder.loadTexts:
    atmxVccEntry.setStatus("current")
_AtmxVccVpi_Type = AtmVpi
_AtmxVccVpi_Object = MibTableColumn
atmxVccVpi = _AtmxVccVpi_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 1, 1, 10, 1, 1, 2),
    _AtmxVccVpi_Type()
)
atmxVccVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmxVccVpi.setStatus("current")
_AtmxVccVci_Type = AtmVci
_AtmxVccVci_Object = MibTableColumn
atmxVccVci = _AtmxVccVci_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 1, 1, 10, 1, 1, 3),
    _AtmxVccVci_Type()
)
atmxVccVci.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    atmxVccVci.setStatus("current")


class _AtmxVccCircuitType_Type(Integer32):
    """Custom type atmxVccCircuitType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("pvc", 1),
          ("svc", 2))
    )


_AtmxVccCircuitType_Type.__name__ = "Integer32"
_AtmxVccCircuitType_Object = MibTableColumn
atmxVccCircuitType = _AtmxVccCircuitType_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 1, 1, 10, 1, 1, 4),
    _AtmxVccCircuitType_Type()
)
atmxVccCircuitType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmxVccCircuitType.setStatus("current")
_AtmxVccOperStatus_Type = AtmConnectionOperStatusCodes
_AtmxVccOperStatus_Object = MibTableColumn
atmxVccOperStatus = _AtmxVccOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 1, 1, 10, 1, 1, 5),
    _AtmxVccOperStatus_Type()
)
atmxVccOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmxVccOperStatus.setStatus("current")
_AtmxVccUpTime_Type = Unsigned32
_AtmxVccUpTime_Object = MibTableColumn
atmxVccUpTime = _AtmxVccUpTime_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 1, 1, 10, 1, 1, 6),
    _AtmxVccUpTime_Type()
)
atmxVccUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmxVccUpTime.setStatus("current")
_AtmxVccTxQosClass_Type = AtmQosClass
_AtmxVccTxQosClass_Object = MibTableColumn
atmxVccTxQosClass = _AtmxVccTxQosClass_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 1, 1, 10, 1, 1, 7),
    _AtmxVccTxQosClass_Type()
)
atmxVccTxQosClass.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmxVccTxQosClass.setStatus("current")


class _AtmxVccTxBestEffort_Type(Integer32):
    """Custom type atmxVccTxBestEffort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2))
    )


_AtmxVccTxBestEffort_Type.__name__ = "Integer32"
_AtmxVccTxBestEffort_Object = MibTableColumn
atmxVccTxBestEffort = _AtmxVccTxBestEffort_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 1, 1, 10, 1, 1, 8),
    _AtmxVccTxBestEffort_Type()
)
atmxVccTxBestEffort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmxVccTxBestEffort.setStatus("current")


class _AtmxVccTxPeakCellRate_Type(Integer32):
    """Custom type atmxVccTxPeakCellRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(192, 20000),
    )


_AtmxVccTxPeakCellRate_Type.__name__ = "Integer32"
_AtmxVccTxPeakCellRate_Object = MibTableColumn
atmxVccTxPeakCellRate = _AtmxVccTxPeakCellRate_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 1, 1, 10, 1, 1, 9),
    _AtmxVccTxPeakCellRate_Type()
)
atmxVccTxPeakCellRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmxVccTxPeakCellRate.setStatus("current")
_AtmxVccRxQosClass_Type = AtmQosClass
_AtmxVccRxQosClass_Object = MibTableColumn
atmxVccRxQosClass = _AtmxVccRxQosClass_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 1, 1, 10, 1, 1, 10),
    _AtmxVccRxQosClass_Type()
)
atmxVccRxQosClass.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmxVccRxQosClass.setStatus("current")


class _AtmxVccRxBestEffort_Type(Integer32):
    """Custom type atmxVccRxBestEffort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2))
    )


_AtmxVccRxBestEffort_Type.__name__ = "Integer32"
_AtmxVccRxBestEffort_Object = MibTableColumn
atmxVccRxBestEffort = _AtmxVccRxBestEffort_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 1, 1, 10, 1, 1, 11),
    _AtmxVccRxBestEffort_Type()
)
atmxVccRxBestEffort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmxVccRxBestEffort.setStatus("current")


class _AtmxVccRxPeakCellRate_Type(Integer32):
    """Custom type atmxVccRxPeakCellRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(192, 20000),
    )


_AtmxVccRxPeakCellRate_Type.__name__ = "Integer32"
_AtmxVccRxPeakCellRate_Object = MibTableColumn
atmxVccRxPeakCellRate = _AtmxVccRxPeakCellRate_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 1, 1, 10, 1, 1, 12),
    _AtmxVccRxPeakCellRate_Type()
)
atmxVccRxPeakCellRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmxVccRxPeakCellRate.setStatus("current")
_AtmxVccRowStatus_Type = RowStatus
_AtmxVccRowStatus_Object = MibTableColumn
atmxVccRowStatus = _AtmxVccRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 1, 1, 10, 1, 1, 13),
    _AtmxVccRowStatus_Type()
)
atmxVccRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmxVccRowStatus.setStatus("current")


class _AtmxVccServiceType_Type(Integer32):
    """Custom type atmxVccServiceType based on Integer32"""
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
        *(("cip", 4),
          ("csr", 8),
          ("ilmi", 2),
          ("lec", 3),
          ("oam", 5),
          ("pt-pt", 6),
          ("sscop", 1),
          ("trunk", 7))
    )


_AtmxVccServiceType_Type.__name__ = "Integer32"
_AtmxVccServiceType_Object = MibTableColumn
atmxVccServiceType = _AtmxVccServiceType_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 1, 1, 10, 1, 1, 14),
    _AtmxVccServiceType_Type()
)
atmxVccServiceType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmxVccServiceType.setStatus("current")
_AtmxAddressGroup_ObjectIdentity = ObjectIdentity
atmxAddressGroup = _AtmxAddressGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 1, 1, 11)
)
_AtmxCipArpGroup_ObjectIdentity = ObjectIdentity
atmxCipArpGroup = _AtmxCipArpGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 1, 1, 12)
)
_AtmxCipArpTable_Object = MibTable
atmxCipArpTable = _AtmxCipArpTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 1, 1, 12, 1)
)
if mibBuilder.loadTexts:
    atmxCipArpTable.setStatus("current")
_AtmxCipArpEntry_Object = MibTableRow
atmxCipArpEntry = _AtmxCipArpEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 1, 1, 12, 1, 1)
)
atmxCipArpEntry.setIndexNames(
    (0, "SWITCH-ATM-MIB", "atmxCipIndex"),
    (0, "SWITCH-ATM-MIB", "atmxCipArpIPAddress"),
)
if mibBuilder.loadTexts:
    atmxCipArpEntry.setStatus("current")
_AtmxCipArpIPAddress_Type = IpAddress
_AtmxCipArpIPAddress_Object = MibTableColumn
atmxCipArpIPAddress = _AtmxCipArpIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 1, 1, 12, 1, 1, 2),
    _AtmxCipArpIPAddress_Type()
)
atmxCipArpIPAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    atmxCipArpIPAddress.setStatus("current")
_AtmxCipArpAtmAddress_Type = AtmAddress
_AtmxCipArpAtmAddress_Object = MibTableColumn
atmxCipArpAtmAddress = _AtmxCipArpAtmAddress_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 1, 1, 12, 1, 1, 3),
    _AtmxCipArpAtmAddress_Type()
)
atmxCipArpAtmAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmxCipArpAtmAddress.setStatus("current")
_AtmxCipArpVci_Type = AtmClientVci
_AtmxCipArpVci_Object = MibTableColumn
atmxCipArpVci = _AtmxCipArpVci_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 1, 1, 12, 1, 1, 4),
    _AtmxCipArpVci_Type()
)
atmxCipArpVci.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmxCipArpVci.setStatus("current")


class _AtmxCipArpTimeToLive_Type(Integer32):
    """Custom type atmxCipArpTimeToLive based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_AtmxCipArpTimeToLive_Type.__name__ = "Integer32"
_AtmxCipArpTimeToLive_Object = MibTableColumn
atmxCipArpTimeToLive = _AtmxCipArpTimeToLive_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 1, 1, 12, 1, 1, 5),
    _AtmxCipArpTimeToLive_Type()
)
atmxCipArpTimeToLive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmxCipArpTimeToLive.setStatus("current")
_AtmxCipArpSource_Type = AtmxArpEntryType
_AtmxCipArpSource_Object = MibTableColumn
atmxCipArpSource = _AtmxCipArpSource_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 1, 1, 12, 1, 1, 6),
    _AtmxCipArpSource_Type()
)
atmxCipArpSource.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmxCipArpSource.setStatus("current")
_AtmxCipArpRowStatus_Type = RowStatus
_AtmxCipArpRowStatus_Object = MibTableColumn
atmxCipArpRowStatus = _AtmxCipArpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 1, 1, 12, 1, 1, 7),
    _AtmxCipArpRowStatus_Type()
)
atmxCipArpRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmxCipArpRowStatus.setStatus("current")
_AtmxLecArpGroup_ObjectIdentity = ObjectIdentity
atmxLecArpGroup = _AtmxLecArpGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 1, 1, 13)
)
_AtmxLecArpTable_Object = MibTable
atmxLecArpTable = _AtmxLecArpTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 1, 1, 13, 1)
)
if mibBuilder.loadTexts:
    atmxLecArpTable.setStatus("current")
_AtmxLecArpEntry_Object = MibTableRow
atmxLecArpEntry = _AtmxLecArpEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 1, 1, 13, 1, 1)
)
atmxLecArpEntry.setIndexNames(
    (0, "SWITCH-ATM-MIB", "atmxLecIndex"),
    (0, "SWITCH-ATM-MIB", "atmxLecArpMacAddress"),
)
if mibBuilder.loadTexts:
    atmxLecArpEntry.setStatus("current")
_AtmxLecArpMacAddress_Type = MacAddress
_AtmxLecArpMacAddress_Object = MibTableColumn
atmxLecArpMacAddress = _AtmxLecArpMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 1, 1, 13, 1, 1, 2),
    _AtmxLecArpMacAddress_Type()
)
atmxLecArpMacAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    atmxLecArpMacAddress.setStatus("current")
_AtmxLecArpAtmAddress_Type = AtmAddress
_AtmxLecArpAtmAddress_Object = MibTableColumn
atmxLecArpAtmAddress = _AtmxLecArpAtmAddress_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 1, 1, 13, 1, 1, 3),
    _AtmxLecArpAtmAddress_Type()
)
atmxLecArpAtmAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmxLecArpAtmAddress.setStatus("current")
_AtmxLecArpVci_Type = AtmVci
_AtmxLecArpVci_Object = MibTableColumn
atmxLecArpVci = _AtmxLecArpVci_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 1, 1, 13, 1, 1, 4),
    _AtmxLecArpVci_Type()
)
atmxLecArpVci.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmxLecArpVci.setStatus("current")


class _AtmxLecArpTimeToLive_Type(Integer32):
    """Custom type atmxLecArpTimeToLive based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_AtmxLecArpTimeToLive_Type.__name__ = "Integer32"
_AtmxLecArpTimeToLive_Object = MibTableColumn
atmxLecArpTimeToLive = _AtmxLecArpTimeToLive_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 1, 1, 13, 1, 1, 5),
    _AtmxLecArpTimeToLive_Type()
)
atmxLecArpTimeToLive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmxLecArpTimeToLive.setStatus("current")
_AtmxLecArpSource_Type = AtmxArpEntryType
_AtmxLecArpSource_Object = MibTableColumn
atmxLecArpSource = _AtmxLecArpSource_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 1, 1, 13, 1, 1, 6),
    _AtmxLecArpSource_Type()
)
atmxLecArpSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmxLecArpSource.setStatus("current")
_AtmxLecArpRowStatus_Type = RowStatus
_AtmxLecArpRowStatus_Object = MibTableColumn
atmxLecArpRowStatus = _AtmxLecArpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 1, 1, 13, 1, 1, 7),
    _AtmxLecArpRowStatus_Type()
)
atmxLecArpRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmxLecArpRowStatus.setStatus("current")
_AtmxPtToPtGroup_ObjectIdentity = ObjectIdentity
atmxPtToPtGroup = _AtmxPtToPtGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 1, 1, 14)
)
_AtmxPtToPtTable_Object = MibTable
atmxPtToPtTable = _AtmxPtToPtTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 1, 1, 14, 1)
)
if mibBuilder.loadTexts:
    atmxPtToPtTable.setStatus("current")
_AtmxPtToPtEntry_Object = MibTableRow
atmxPtToPtEntry = _AtmxPtToPtEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 1, 1, 14, 1, 1)
)
atmxPtToPtEntry.setIndexNames(
    (0, "SWITCH-ATM-MIB", "atmxPtToPtIndex"),
)
if mibBuilder.loadTexts:
    atmxPtToPtEntry.setStatus("current")


class _AtmxPtToPtIndex_Type(Integer32):
    """Custom type atmxPtToPtIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_AtmxPtToPtIndex_Type.__name__ = "Integer32"
_AtmxPtToPtIndex_Object = MibTableColumn
atmxPtToPtIndex = _AtmxPtToPtIndex_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 1, 1, 14, 1, 1, 1),
    _AtmxPtToPtIndex_Type()
)
atmxPtToPtIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    atmxPtToPtIndex.setStatus("current")


class _AtmxPtToPtDescription_Type(DisplayString):
    """Custom type atmxPtToPtDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_AtmxPtToPtDescription_Type.__name__ = "DisplayString"
_AtmxPtToPtDescription_Object = MibTableColumn
atmxPtToPtDescription = _AtmxPtToPtDescription_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 1, 1, 14, 1, 1, 2),
    _AtmxPtToPtDescription_Type()
)
atmxPtToPtDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmxPtToPtDescription.setStatus("current")


class _AtmxPtToPtEncap_Type(Integer32):
    """Custom type atmxPtToPtEncap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("private", 2),
          ("rfc1483", 1))
    )


_AtmxPtToPtEncap_Type.__name__ = "Integer32"
_AtmxPtToPtEncap_Object = MibTableColumn
atmxPtToPtEncap = _AtmxPtToPtEncap_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 1, 1, 14, 1, 1, 3),
    _AtmxPtToPtEncap_Type()
)
atmxPtToPtEncap.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmxPtToPtEncap.setStatus("current")


class _AtmxPtToPtConnType_Type(Integer32):
    """Custom type atmxPtToPtConnType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("pvc", 1),
          ("svc", 2))
    )


_AtmxPtToPtConnType_Type.__name__ = "Integer32"
_AtmxPtToPtConnType_Object = MibTableColumn
atmxPtToPtConnType = _AtmxPtToPtConnType_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 1, 1, 14, 1, 1, 4),
    _AtmxPtToPtConnType_Type()
)
atmxPtToPtConnType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmxPtToPtConnType.setStatus("current")
_AtmxPtToPtVci_Type = AtmClientVci
_AtmxPtToPtVci_Object = MibTableColumn
atmxPtToPtVci = _AtmxPtToPtVci_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 1, 1, 14, 1, 1, 5),
    _AtmxPtToPtVci_Type()
)
atmxPtToPtVci.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmxPtToPtVci.setStatus("current")
_AtmxPtToPtDestAddr_Type = AtmAddress
_AtmxPtToPtDestAddr_Object = MibTableColumn
atmxPtToPtDestAddr = _AtmxPtToPtDestAddr_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 1, 1, 14, 1, 1, 6),
    _AtmxPtToPtDestAddr_Type()
)
atmxPtToPtDestAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmxPtToPtDestAddr.setStatus("current")
_AtmxPtToPtRowStatus_Type = RowStatus
_AtmxPtToPtRowStatus_Object = MibTableColumn
atmxPtToPtRowStatus = _AtmxPtToPtRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 1, 1, 14, 1, 1, 7),
    _AtmxPtToPtRowStatus_Type()
)
atmxPtToPtRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmxPtToPtRowStatus.setStatus("current")
_AtmxPtToPtIfIndex_Type = IfIndexOrZero
_AtmxPtToPtIfIndex_Object = MibTableColumn
atmxPtToPtIfIndex = _AtmxPtToPtIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 1, 1, 14, 1, 1, 8),
    _AtmxPtToPtIfIndex_Type()
)
atmxPtToPtIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmxPtToPtIfIndex.setStatus("current")
_AtmxPtToPtVlanNumber_Type = AtmxVlanRange
_AtmxPtToPtVlanNumber_Object = MibTableColumn
atmxPtToPtVlanNumber = _AtmxPtToPtVlanNumber_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 1, 1, 14, 1, 1, 9),
    _AtmxPtToPtVlanNumber_Type()
)
atmxPtToPtVlanNumber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmxPtToPtVlanNumber.setStatus("current")
_AtmxPtToPtAdminStatus_Type = AtmAdminStatus
_AtmxPtToPtAdminStatus_Object = MibTableColumn
atmxPtToPtAdminStatus = _AtmxPtToPtAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 1, 1, 14, 1, 1, 10),
    _AtmxPtToPtAdminStatus_Type()
)
atmxPtToPtAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmxPtToPtAdminStatus.setStatus("current")
_AtmxPtToPtOperStatus_Type = AtmConnectionOperStatusCodes
_AtmxPtToPtOperStatus_Object = MibTableColumn
atmxPtToPtOperStatus = _AtmxPtToPtOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 1, 1, 14, 1, 1, 11),
    _AtmxPtToPtOperStatus_Type()
)
atmxPtToPtOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmxPtToPtOperStatus.setStatus("current")
_AtmxPtToPtStatsTable_Object = MibTable
atmxPtToPtStatsTable = _AtmxPtToPtStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 1, 1, 14, 2)
)
if mibBuilder.loadTexts:
    atmxPtToPtStatsTable.setStatus("current")
_AtmxPtToPtStatsEntry_Object = MibTableRow
atmxPtToPtStatsEntry = _AtmxPtToPtStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 1, 1, 14, 2, 1)
)
atmxPtToPtStatsEntry.setIndexNames(
    (0, "SWITCH-ATM-MIB", "atmxPtToPtIndex"),
)
if mibBuilder.loadTexts:
    atmxPtToPtStatsEntry.setStatus("current")
_AtmxPtToPtStatsTotalTxPkts_Type = Integer32
_AtmxPtToPtStatsTotalTxPkts_Object = MibTableColumn
atmxPtToPtStatsTotalTxPkts = _AtmxPtToPtStatsTotalTxPkts_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 1, 1, 14, 2, 1, 1),
    _AtmxPtToPtStatsTotalTxPkts_Type()
)
atmxPtToPtStatsTotalTxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmxPtToPtStatsTotalTxPkts.setStatus("current")
_AtmxPtToPtStatsTotalRxPkts_Type = Integer32
_AtmxPtToPtStatsTotalRxPkts_Object = MibTableColumn
atmxPtToPtStatsTotalRxPkts = _AtmxPtToPtStatsTotalRxPkts_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 1, 1, 14, 2, 1, 2),
    _AtmxPtToPtStatsTotalRxPkts_Type()
)
atmxPtToPtStatsTotalRxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmxPtToPtStatsTotalRxPkts.setStatus("current")
_AtmxPtToPtStatsTotalTxDiscards_Type = Integer32
_AtmxPtToPtStatsTotalTxDiscards_Object = MibTableColumn
atmxPtToPtStatsTotalTxDiscards = _AtmxPtToPtStatsTotalTxDiscards_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 1, 1, 14, 2, 1, 3),
    _AtmxPtToPtStatsTotalTxDiscards_Type()
)
atmxPtToPtStatsTotalTxDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmxPtToPtStatsTotalTxDiscards.setStatus("current")
_AtmxPtToPtStatsTotalRxDiscards_Type = Integer32
_AtmxPtToPtStatsTotalRxDiscards_Object = MibTableColumn
atmxPtToPtStatsTotalRxDiscards = _AtmxPtToPtStatsTotalRxDiscards_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 1, 1, 14, 2, 1, 4),
    _AtmxPtToPtStatsTotalRxDiscards_Type()
)
atmxPtToPtStatsTotalRxDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmxPtToPtStatsTotalRxDiscards.setStatus("current")
_AtmxTrunkGroup_ObjectIdentity = ObjectIdentity
atmxTrunkGroup = _AtmxTrunkGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 1, 1, 15)
)
_AtmxTrunkTable_Object = MibTable
atmxTrunkTable = _AtmxTrunkTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 1, 1, 15, 1)
)
if mibBuilder.loadTexts:
    atmxTrunkTable.setStatus("current")
_AtmxTrunkEntry_Object = MibTableRow
atmxTrunkEntry = _AtmxTrunkEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 1, 1, 15, 1, 1)
)
atmxTrunkEntry.setIndexNames(
    (0, "SWITCH-ATM-MIB", "atmxTrunkIndex"),
)
if mibBuilder.loadTexts:
    atmxTrunkEntry.setStatus("current")


class _AtmxTrunkIndex_Type(Integer32):
    """Custom type atmxTrunkIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_AtmxTrunkIndex_Type.__name__ = "Integer32"
_AtmxTrunkIndex_Object = MibTableColumn
atmxTrunkIndex = _AtmxTrunkIndex_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 1, 1, 15, 1, 1, 1),
    _AtmxTrunkIndex_Type()
)
atmxTrunkIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    atmxTrunkIndex.setStatus("current")


class _AtmxTrunkDescription_Type(DisplayString):
    """Custom type atmxTrunkDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_AtmxTrunkDescription_Type.__name__ = "DisplayString"
_AtmxTrunkDescription_Object = MibTableColumn
atmxTrunkDescription = _AtmxTrunkDescription_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 1, 1, 15, 1, 1, 2),
    _AtmxTrunkDescription_Type()
)
atmxTrunkDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmxTrunkDescription.setStatus("current")


class _AtmxTrunkConnType_Type(Integer32):
    """Custom type atmxTrunkConnType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("pvc", 1),
          ("svc", 2))
    )


_AtmxTrunkConnType_Type.__name__ = "Integer32"
_AtmxTrunkConnType_Object = MibTableColumn
atmxTrunkConnType = _AtmxTrunkConnType_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 1, 1, 15, 1, 1, 3),
    _AtmxTrunkConnType_Type()
)
atmxTrunkConnType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmxTrunkConnType.setStatus("current")
_AtmxTrunkVci_Type = AtmClientVci
_AtmxTrunkVci_Object = MibTableColumn
atmxTrunkVci = _AtmxTrunkVci_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 1, 1, 15, 1, 1, 4),
    _AtmxTrunkVci_Type()
)
atmxTrunkVci.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmxTrunkVci.setStatus("current")
_AtmxTrunkDestAddr_Type = AtmAddress
_AtmxTrunkDestAddr_Object = MibTableColumn
atmxTrunkDestAddr = _AtmxTrunkDestAddr_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 1, 1, 15, 1, 1, 5),
    _AtmxTrunkDestAddr_Type()
)
atmxTrunkDestAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmxTrunkDestAddr.setStatus("current")
_AtmxTrunkRowStatus_Type = RowStatus
_AtmxTrunkRowStatus_Object = MibTableColumn
atmxTrunkRowStatus = _AtmxTrunkRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 1, 1, 15, 1, 1, 6),
    _AtmxTrunkRowStatus_Type()
)
atmxTrunkRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmxTrunkRowStatus.setStatus("current")
_AtmxTrunkAdminStatus_Type = AtmAdminStatus
_AtmxTrunkAdminStatus_Object = MibTableColumn
atmxTrunkAdminStatus = _AtmxTrunkAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 1, 1, 15, 1, 1, 7),
    _AtmxTrunkAdminStatus_Type()
)
atmxTrunkAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmxTrunkAdminStatus.setStatus("current")
_AtmxTrunkOperStatus_Type = AtmConnectionOperStatusCodes
_AtmxTrunkOperStatus_Object = MibTableColumn
atmxTrunkOperStatus = _AtmxTrunkOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 1, 1, 15, 1, 1, 8),
    _AtmxTrunkOperStatus_Type()
)
atmxTrunkOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmxTrunkOperStatus.setStatus("current")
_AtmxTrunkVlanTable_Object = MibTable
atmxTrunkVlanTable = _AtmxTrunkVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 1, 1, 15, 2)
)
if mibBuilder.loadTexts:
    atmxTrunkVlanTable.setStatus("current")
_AtmxTrunkVlanEntry_Object = MibTableRow
atmxTrunkVlanEntry = _AtmxTrunkVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 1, 1, 15, 2, 1)
)
atmxTrunkVlanEntry.setIndexNames(
    (0, "SWITCH-ATM-MIB", "atmxTrunkIndex"),
    (0, "SWITCH-ATM-MIB", "atmxTrunkVlanNumber"),
)
if mibBuilder.loadTexts:
    atmxTrunkVlanEntry.setStatus("current")
_AtmxTrunkVlanNumber_Type = AtmxVlanRange
_AtmxTrunkVlanNumber_Object = MibTableColumn
atmxTrunkVlanNumber = _AtmxTrunkVlanNumber_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 1, 1, 15, 2, 1, 1),
    _AtmxTrunkVlanNumber_Type()
)
atmxTrunkVlanNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    atmxTrunkVlanNumber.setStatus("current")
_AtmxTrunkVlanIfIndex_Type = IfIndexOrZero
_AtmxTrunkVlanIfIndex_Object = MibTableColumn
atmxTrunkVlanIfIndex = _AtmxTrunkVlanIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 1, 1, 15, 2, 1, 2),
    _AtmxTrunkVlanIfIndex_Type()
)
atmxTrunkVlanIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmxTrunkVlanIfIndex.setStatus("current")
_AtmxTrunkVlanRowStatus_Type = RowStatus
_AtmxTrunkVlanRowStatus_Object = MibTableColumn
atmxTrunkVlanRowStatus = _AtmxTrunkVlanRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 1, 1, 15, 2, 1, 3),
    _AtmxTrunkVlanRowStatus_Type()
)
atmxTrunkVlanRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmxTrunkVlanRowStatus.setStatus("current")
_AtmxTrunkStatsTable_Object = MibTable
atmxTrunkStatsTable = _AtmxTrunkStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 1, 1, 15, 3)
)
if mibBuilder.loadTexts:
    atmxTrunkStatsTable.setStatus("current")
_AtmxTrunkStatsEntry_Object = MibTableRow
atmxTrunkStatsEntry = _AtmxTrunkStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 1, 1, 15, 3, 1)
)
atmxTrunkStatsEntry.setIndexNames(
    (0, "SWITCH-ATM-MIB", "atmxTrunkIndex"),
)
if mibBuilder.loadTexts:
    atmxTrunkStatsEntry.setStatus("current")
_AtmxTrunkStatsTotalTxPkts_Type = Integer32
_AtmxTrunkStatsTotalTxPkts_Object = MibTableColumn
atmxTrunkStatsTotalTxPkts = _AtmxTrunkStatsTotalTxPkts_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 1, 1, 15, 3, 1, 1),
    _AtmxTrunkStatsTotalTxPkts_Type()
)
atmxTrunkStatsTotalTxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmxTrunkStatsTotalTxPkts.setStatus("current")
_AtmxTrunkStatsTotalRxPkts_Type = Integer32
_AtmxTrunkStatsTotalRxPkts_Object = MibTableColumn
atmxTrunkStatsTotalRxPkts = _AtmxTrunkStatsTotalRxPkts_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 1, 1, 15, 3, 1, 2),
    _AtmxTrunkStatsTotalRxPkts_Type()
)
atmxTrunkStatsTotalRxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmxTrunkStatsTotalRxPkts.setStatus("current")
_AtmxTrunkStatsTotalTxDiscards_Type = Integer32
_AtmxTrunkStatsTotalTxDiscards_Object = MibTableColumn
atmxTrunkStatsTotalTxDiscards = _AtmxTrunkStatsTotalTxDiscards_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 1, 1, 15, 3, 1, 3),
    _AtmxTrunkStatsTotalTxDiscards_Type()
)
atmxTrunkStatsTotalTxDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmxTrunkStatsTotalTxDiscards.setStatus("current")
_AtmxTrunkStatsTotalRxDiscards_Type = Integer32
_AtmxTrunkStatsTotalRxDiscards_Object = MibTableColumn
atmxTrunkStatsTotalRxDiscards = _AtmxTrunkStatsTotalRxDiscards_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 1, 1, 15, 3, 1, 4),
    _AtmxTrunkStatsTotalRxDiscards_Type()
)
atmxTrunkStatsTotalRxDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmxTrunkStatsTotalRxDiscards.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SWITCH-ATM-MIB",
    **{"IfIndexOrZero": IfIndexOrZero,
       "AtmAddress": AtmAddress,
       "AtmPortIndex": AtmPortIndex,
       "AtmVpi": AtmVpi,
       "AtmVci": AtmVci,
       "AtmClientVci": AtmClientVci,
       "AtmLecIndex": AtmLecIndex,
       "AtmCipIndex": AtmCipIndex,
       "AtmAdminStatus": AtmAdminStatus,
       "AtmOperStatus": AtmOperStatus,
       "AtmConnectionOperStatusCodes": AtmConnectionOperStatusCodes,
       "AtmTransmissionTypes": AtmTransmissionTypes,
       "AtmMediaTypes": AtmMediaTypes,
       "AtmQosClass": AtmQosClass,
       "AtmClearStats": AtmClearStats,
       "AtmxArpEntryType": AtmxArpEntryType,
       "AtmxVlanRange": AtmxVlanRange,
       "switchAtmMib": switchAtmMib,
       "atmxPortGroup": atmxPortGroup,
       "atmxPortTable": atmxPortTable,
       "atmxPortEntry": atmxPortEntry,
       "atmxPortIndex": atmxPortIndex,
       "atmxPortDescription": atmxPortDescription,
       "atmxPortTransmissionType": atmxPortTransmissionType,
       "atmxPortMediaType": atmxPortMediaType,
       "atmxPortOperStatus": atmxPortOperStatus,
       "atmxPortMaxVCCs": atmxPortMaxVCCs,
       "atmxPortMaxVciBits": atmxPortMaxVciBits,
       "atmxPortAddress": atmxPortAddress,
       "atmxPortSignalingVersion": atmxPortSignalingVersion,
       "atmxPortSignalingVci": atmxPortSignalingVci,
       "atmxPortILMIVci": atmxPortILMIVci,
       "atmxPortEnableIlmi": atmxPortEnableIlmi,
       "atmxPortEnableIlmiPoll": atmxPortEnableIlmiPoll,
       "atmxPortEnablePlScramble": atmxPortEnablePlScramble,
       "atmxPortClock": atmxPortClock,
       "atmxPortMacAddress": atmxPortMacAddress,
       "atmxPortAdaptorRamSize": atmxPortAdaptorRamSize,
       "atmxPortIlmiStatus": atmxPortIlmiStatus,
       "atmxPortSignalingStatus": atmxPortSignalingStatus,
       "atmxPortSignalingMode": atmxPortSignalingMode,
       "atmxLecGroup": atmxLecGroup,
       "atmxLecTable": atmxLecTable,
       "atmxLecEntry": atmxLecEntry,
       "atmxLecIndex": atmxLecIndex,
       "atmxLecDescription": atmxLecDescription,
       "atmxElanName": atmxElanName,
       "atmxLecConfigMode": atmxLecConfigMode,
       "atmxLecServerAddress": atmxLecServerAddress,
       "atmxLecUnicastMacAddress": atmxLecUnicastMacAddress,
       "atmxLecMaxUnknownFrameCount": atmxLecMaxUnknownFrameCount,
       "atmxLecMaxArpRetryCount": atmxLecMaxArpRetryCount,
       "atmxLecArpRespTime": atmxLecArpRespTime,
       "atmxLecMaxUnknownFrameTime": atmxLecMaxUnknownFrameTime,
       "atmxLecControlTimeout": atmxLecControlTimeout,
       "atmxLecVccTimeout": atmxLecVccTimeout,
       "atmxLecAgeingTime": atmxLecAgeingTime,
       "atmxLecFlushTimeout": atmxLecFlushTimeout,
       "atmxLecVPortNumber": atmxLecVPortNumber,
       "atmxLecProtocolState": atmxLecProtocolState,
       "atmxLecRowStatus": atmxLecRowStatus,
       "atmxLecIfIndex": atmxLecIfIndex,
       "atmxLecId": atmxLecId,
       "atmxLecControlDirectVcc": atmxLecControlDirectVcc,
       "atmxLecControlDistributeVcc": atmxLecControlDistributeVcc,
       "atmxLecMulticastSendVcc": atmxLecMulticastSendVcc,
       "atmxLecMulticastForwardVcc": atmxLecMulticastForwardVcc,
       "atmxLecVlanNumber": atmxLecVlanNumber,
       "atmxCipGroup": atmxCipGroup,
       "atmxCipTable": atmxCipTable,
       "atmxCipEntry": atmxCipEntry,
       "atmxCipIndex": atmxCipIndex,
       "atmxCipDescription": atmxCipDescription,
       "atmxCipIPAddress": atmxCipIPAddress,
       "atmxCipIPSubnetMask": atmxCipIPSubnetMask,
       "atmxCipConnectionType": atmxCipConnectionType,
       "atmxCipVci": atmxCipVci,
       "atmxCipServerAtmAddress": atmxCipServerAtmAddress,
       "atmxCipMtuSize": atmxCipMtuSize,
       "atmxCipIfIndex": atmxCipIfIndex,
       "atmxCipProtocolState": atmxCipProtocolState,
       "atmxCipAdmStatus": atmxCipAdmStatus,
       "atmxCipOperStatus": atmxCipOperStatus,
       "atmxCipRowStatus": atmxCipRowStatus,
       "atmxCipRipMode": atmxCipRipMode,
       "atmxCipVciTable": atmxCipVciTable,
       "atmxCipVciEntry": atmxCipVciEntry,
       "atmxCipVciId": atmxCipVciId,
       "atmxCipVciRowStatus": atmxCipVciRowStatus,
       "atmxLayerStatsGroup": atmxLayerStatsGroup,
       "atmxLayerStatsTable": atmxLayerStatsTable,
       "atmxLayerStatsEntry": atmxLayerStatsEntry,
       "atmxLayerStatsTxCells": atmxLayerStatsTxCells,
       "atmxLayerStatsRxCells": atmxLayerStatsRxCells,
       "atmxLayerStatsTxCellDiscards": atmxLayerStatsTxCellDiscards,
       "atmxLayerStatsRxCellDiscards": atmxLayerStatsRxCellDiscards,
       "atmxLayerStatsClear": atmxLayerStatsClear,
       "atmxLayerStatsClearTime": atmxLayerStatsClearTime,
       "aal5LayerStatsTable": aal5LayerStatsTable,
       "aal5LayerStatsEntry": aal5LayerStatsEntry,
       "aal5LayerTxOctets": aal5LayerTxOctets,
       "aal5LayerTxCells": aal5LayerTxCells,
       "aal5LayerTxSDUs": aal5LayerTxSDUs,
       "aal5LayerTxSDUDiscards": aal5LayerTxSDUDiscards,
       "aal5LayerTxErrors": aal5LayerTxErrors,
       "aal5LayerRxOctets": aal5LayerRxOctets,
       "aal5LayerRxCells": aal5LayerRxCells,
       "aal5LayerRxSDUs": aal5LayerRxSDUs,
       "aal5LayerRxSDUDiscards": aal5LayerRxSDUDiscards,
       "aal5LayerRxErrors": aal5LayerRxErrors,
       "aal5LayerRxSarTimeouts": aal5LayerRxSarTimeouts,
       "aal5LayerRxCrcErrors": aal5LayerRxCrcErrors,
       "aal5LayerRxSDUInvalidSz": aal5LayerRxSDUInvalidSz,
       "aal5LayerClearStats": aal5LayerClearStats,
       "aal5LayerStatsClearTime": aal5LayerStatsClearTime,
       "atmxVccStatsGroup": atmxVccStatsGroup,
       "atmxVccStatsTable": atmxVccStatsTable,
       "atmxVccStatsEntry": atmxVccStatsEntry,
       "atmxVccStatsTxSDUs": atmxVccStatsTxSDUs,
       "atmxVccStatsTxCells": atmxVccStatsTxCells,
       "atmxVccStatsTxOctets": atmxVccStatsTxOctets,
       "atmxVccStatsRxSDUs": atmxVccStatsRxSDUs,
       "atmxVccStatsRxCells": atmxVccStatsRxCells,
       "atmxVccStatsRxOctets": atmxVccStatsRxOctets,
       "atmxVccStatsTxSDUDiscards": atmxVccStatsTxSDUDiscards,
       "atmxVccStatsTxErrors": atmxVccStatsTxErrors,
       "atmxVccStatsRxSDUDiscards": atmxVccStatsRxSDUDiscards,
       "atmxVccStatsRxErrors": atmxVccStatsRxErrors,
       "atmxVccStatsRxSarTimeouts": atmxVccStatsRxSarTimeouts,
       "atmxVccStatsRxCrcErrors": atmxVccStatsRxCrcErrors,
       "atmxVccStatsRxOversizedSdus": atmxVccStatsRxOversizedSdus,
       "atmxVccStatsConnCreateTime": atmxVccStatsConnCreateTime,
       "atmxVccStatsConnInIdleTime": atmxVccStatsConnInIdleTime,
       "atmxVccStatsConnOutIdleTime": atmxVccStatsConnOutIdleTime,
       "atmxVccStatsConnModifiedTime": atmxVccStatsConnModifiedTime,
       "atmxLecStatsGroup": atmxLecStatsGroup,
       "atmxLecStatsTable": atmxLecStatsTable,
       "atmxLecStatsEntry": atmxLecStatsEntry,
       "atmxLecStatsTxArpReq": atmxLecStatsTxArpReq,
       "atmxLecStatsTxArpRsp": atmxLecStatsTxArpRsp,
       "atmxLecStatsTxControlPkts": atmxLecStatsTxControlPkts,
       "atmxLecStatsTxUnicastPkts": atmxLecStatsTxUnicastPkts,
       "atmxLecStatsTxMulticastPkts": atmxLecStatsTxMulticastPkts,
       "atmxLecStatsTxBroadcastPkts": atmxLecStatsTxBroadcastPkts,
       "atmxLecStatsTxDiscardPkts": atmxLecStatsTxDiscardPkts,
       "atmxLecStatsRxArpReq": atmxLecStatsRxArpReq,
       "atmxLecStatsRxArpRsp": atmxLecStatsRxArpRsp,
       "atmxLecStatsRxControlPkts": atmxLecStatsRxControlPkts,
       "atmxLecStatsRxUnicastPkts": atmxLecStatsRxUnicastPkts,
       "atmxLecStatsRxMulticastPkts": atmxLecStatsRxMulticastPkts,
       "atmxLecStatsRxBroadcastPkts": atmxLecStatsRxBroadcastPkts,
       "atmxLecStatsRxDiscardPkts": atmxLecStatsRxDiscardPkts,
       "atmxCipStatsGroup": atmxCipStatsGroup,
       "atmxCipStatsTable": atmxCipStatsTable,
       "atmxCipStatsEntry": atmxCipStatsEntry,
       "atmxCipStatsPktsFromOtherLIS": atmxCipStatsPktsFromOtherLIS,
       "atmxCipStatsTxArpReq": atmxCipStatsTxArpReq,
       "atmxCipStatsTxArpRsp": atmxCipStatsTxArpRsp,
       "atmxCipStatsTxInArpReq": atmxCipStatsTxInArpReq,
       "atmxCipStatsTxInArpRsp": atmxCipStatsTxInArpRsp,
       "atmxCipStatsTxDiscards": atmxCipStatsTxDiscards,
       "atmxCipStatsRxArpReq": atmxCipStatsRxArpReq,
       "atmxCipStatsRxArpRsp": atmxCipStatsRxArpRsp,
       "atmxCipStatsRxInArpReq": atmxCipStatsRxInArpReq,
       "atmxCipStatsRxInArpRsp": atmxCipStatsRxInArpRsp,
       "atmxCipStatsRxDiscards": atmxCipStatsRxDiscards,
       "atmxSscopStatsGroup": atmxSscopStatsGroup,
       "atmxSscopStatsTable": atmxSscopStatsTable,
       "atmxSscopStatsEntry": atmxSscopStatsEntry,
       "atmxSscopStatsTxTotalPdus": atmxSscopStatsTxTotalPdus,
       "atmxSscopStatsTxDiscardSdus": atmxSscopStatsTxDiscardSdus,
       "atmxSscopStatsTxDiscardPdus": atmxSscopStatsTxDiscardPdus,
       "atmxSscopStatsTxErrorPdus": atmxSscopStatsTxErrorPdus,
       "atmxSscopStatsTxBufferInUseCtr": atmxSscopStatsTxBufferInUseCtr,
       "atmxSscopStatsTxBufferInUseGauge": atmxSscopStatsTxBufferInUseGauge,
       "atmxSscopStatsRxTotalPdus": atmxSscopStatsRxTotalPdus,
       "atmxSscopStatsRxDiscardPdus": atmxSscopStatsRxDiscardPdus,
       "atmxSscopStatsRxErrorPdus": atmxSscopStatsRxErrorPdus,
       "atmxSscopStatsRxBufferInUseCtr": atmxSscopStatsRxBufferInUseCtr,
       "atmxSscopStatsRxBufferInUseGauge": atmxSscopStatsRxBufferInUseGauge,
       "atmxIlmiStatsGroup": atmxIlmiStatsGroup,
       "atmxIlmiStatsTable": atmxIlmiStatsTable,
       "atmxIlmiStatsEntry": atmxIlmiStatsEntry,
       "atmxIlmiTxPDUs": atmxIlmiTxPDUs,
       "atmxIlmiRxPDUs": atmxIlmiRxPDUs,
       "atmxIlmiRxDiscardPDUs": atmxIlmiRxDiscardPDUs,
       "atmxVccGroup": atmxVccGroup,
       "atmxVccTable": atmxVccTable,
       "atmxVccEntry": atmxVccEntry,
       "atmxVccVpi": atmxVccVpi,
       "atmxVccVci": atmxVccVci,
       "atmxVccCircuitType": atmxVccCircuitType,
       "atmxVccOperStatus": atmxVccOperStatus,
       "atmxVccUpTime": atmxVccUpTime,
       "atmxVccTxQosClass": atmxVccTxQosClass,
       "atmxVccTxBestEffort": atmxVccTxBestEffort,
       "atmxVccTxPeakCellRate": atmxVccTxPeakCellRate,
       "atmxVccRxQosClass": atmxVccRxQosClass,
       "atmxVccRxBestEffort": atmxVccRxBestEffort,
       "atmxVccRxPeakCellRate": atmxVccRxPeakCellRate,
       "atmxVccRowStatus": atmxVccRowStatus,
       "atmxVccServiceType": atmxVccServiceType,
       "atmxAddressGroup": atmxAddressGroup,
       "atmxCipArpGroup": atmxCipArpGroup,
       "atmxCipArpTable": atmxCipArpTable,
       "atmxCipArpEntry": atmxCipArpEntry,
       "atmxCipArpIPAddress": atmxCipArpIPAddress,
       "atmxCipArpAtmAddress": atmxCipArpAtmAddress,
       "atmxCipArpVci": atmxCipArpVci,
       "atmxCipArpTimeToLive": atmxCipArpTimeToLive,
       "atmxCipArpSource": atmxCipArpSource,
       "atmxCipArpRowStatus": atmxCipArpRowStatus,
       "atmxLecArpGroup": atmxLecArpGroup,
       "atmxLecArpTable": atmxLecArpTable,
       "atmxLecArpEntry": atmxLecArpEntry,
       "atmxLecArpMacAddress": atmxLecArpMacAddress,
       "atmxLecArpAtmAddress": atmxLecArpAtmAddress,
       "atmxLecArpVci": atmxLecArpVci,
       "atmxLecArpTimeToLive": atmxLecArpTimeToLive,
       "atmxLecArpSource": atmxLecArpSource,
       "atmxLecArpRowStatus": atmxLecArpRowStatus,
       "atmxPtToPtGroup": atmxPtToPtGroup,
       "atmxPtToPtTable": atmxPtToPtTable,
       "atmxPtToPtEntry": atmxPtToPtEntry,
       "atmxPtToPtIndex": atmxPtToPtIndex,
       "atmxPtToPtDescription": atmxPtToPtDescription,
       "atmxPtToPtEncap": atmxPtToPtEncap,
       "atmxPtToPtConnType": atmxPtToPtConnType,
       "atmxPtToPtVci": atmxPtToPtVci,
       "atmxPtToPtDestAddr": atmxPtToPtDestAddr,
       "atmxPtToPtRowStatus": atmxPtToPtRowStatus,
       "atmxPtToPtIfIndex": atmxPtToPtIfIndex,
       "atmxPtToPtVlanNumber": atmxPtToPtVlanNumber,
       "atmxPtToPtAdminStatus": atmxPtToPtAdminStatus,
       "atmxPtToPtOperStatus": atmxPtToPtOperStatus,
       "atmxPtToPtStatsTable": atmxPtToPtStatsTable,
       "atmxPtToPtStatsEntry": atmxPtToPtStatsEntry,
       "atmxPtToPtStatsTotalTxPkts": atmxPtToPtStatsTotalTxPkts,
       "atmxPtToPtStatsTotalRxPkts": atmxPtToPtStatsTotalRxPkts,
       "atmxPtToPtStatsTotalTxDiscards": atmxPtToPtStatsTotalTxDiscards,
       "atmxPtToPtStatsTotalRxDiscards": atmxPtToPtStatsTotalRxDiscards,
       "atmxTrunkGroup": atmxTrunkGroup,
       "atmxTrunkTable": atmxTrunkTable,
       "atmxTrunkEntry": atmxTrunkEntry,
       "atmxTrunkIndex": atmxTrunkIndex,
       "atmxTrunkDescription": atmxTrunkDescription,
       "atmxTrunkConnType": atmxTrunkConnType,
       "atmxTrunkVci": atmxTrunkVci,
       "atmxTrunkDestAddr": atmxTrunkDestAddr,
       "atmxTrunkRowStatus": atmxTrunkRowStatus,
       "atmxTrunkAdminStatus": atmxTrunkAdminStatus,
       "atmxTrunkOperStatus": atmxTrunkOperStatus,
       "atmxTrunkVlanTable": atmxTrunkVlanTable,
       "atmxTrunkVlanEntry": atmxTrunkVlanEntry,
       "atmxTrunkVlanNumber": atmxTrunkVlanNumber,
       "atmxTrunkVlanIfIndex": atmxTrunkVlanIfIndex,
       "atmxTrunkVlanRowStatus": atmxTrunkVlanRowStatus,
       "atmxTrunkStatsTable": atmxTrunkStatsTable,
       "atmxTrunkStatsEntry": atmxTrunkStatsEntry,
       "atmxTrunkStatsTotalTxPkts": atmxTrunkStatsTotalTxPkts,
       "atmxTrunkStatsTotalRxPkts": atmxTrunkStatsTotalRxPkts,
       "atmxTrunkStatsTotalTxDiscards": atmxTrunkStatsTotalTxDiscards,
       "atmxTrunkStatsTotalRxDiscards": atmxTrunkStatsTotalRxDiscards}
)
