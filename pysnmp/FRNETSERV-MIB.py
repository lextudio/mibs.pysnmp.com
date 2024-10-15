# SNMP MIB module (FRNETSERV-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/FRNETSERV-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:46:25 2024
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

(InterfaceIndex,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "ifIndex")

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
 TextualConvention,
 TimeStamp) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TimeStamp")


# MODULE-IDENTITY

frnetservMIB = ModuleIdentity(
    (1, 3, 6, 1, 2, 1, 10, 44)
)
frnetservMIB.setRevisions(
        ("2000-09-28 00:00",
         "1993-11-16 12:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_FrnetservObjects_ObjectIdentity = ObjectIdentity
frnetservObjects = _FrnetservObjects_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 44, 1)
)
_FrLportTable_Object = MibTable
frLportTable = _FrLportTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 44, 1, 1)
)
if mibBuilder.loadTexts:
    frLportTable.setStatus("current")
_FrLportEntry_Object = MibTableRow
frLportEntry = _FrLportEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 44, 1, 1, 1)
)
frLportEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    frLportEntry.setStatus("current")


class _FrLportNumPlan_Type(Integer32):
    """Custom type frLportNumPlan based on Integer32"""
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
        *(("e164", 2),
          ("none", 4),
          ("other", 1),
          ("x121", 3))
    )


_FrLportNumPlan_Type.__name__ = "Integer32"
_FrLportNumPlan_Object = MibTableColumn
frLportNumPlan = _FrLportNumPlan_Object(
    (1, 3, 6, 1, 2, 1, 10, 44, 1, 1, 1, 1),
    _FrLportNumPlan_Type()
)
frLportNumPlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frLportNumPlan.setStatus("current")
_FrLportContact_Type = SnmpAdminString
_FrLportContact_Object = MibTableColumn
frLportContact = _FrLportContact_Object(
    (1, 3, 6, 1, 2, 1, 10, 44, 1, 1, 1, 2),
    _FrLportContact_Type()
)
frLportContact.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frLportContact.setStatus("current")
_FrLportLocation_Type = SnmpAdminString
_FrLportLocation_Object = MibTableColumn
frLportLocation = _FrLportLocation_Object(
    (1, 3, 6, 1, 2, 1, 10, 44, 1, 1, 1, 3),
    _FrLportLocation_Type()
)
frLportLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frLportLocation.setStatus("current")


class _FrLportType_Type(Integer32):
    """Custom type frLportType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("nni", 2),
          ("uni", 1))
    )


_FrLportType_Type.__name__ = "Integer32"
_FrLportType_Object = MibTableColumn
frLportType = _FrLportType_Object(
    (1, 3, 6, 1, 2, 1, 10, 44, 1, 1, 1, 4),
    _FrLportType_Type()
)
frLportType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frLportType.setStatus("current")


class _FrLportAddrDLCILen_Type(Integer32):
    """Custom type frLportAddrDLCILen based on Integer32"""
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
        *(("fourOctets17Bits", 4),
          ("fourOctets23Bits", 5),
          ("threeOctets10Bits", 2),
          ("threeOctets16Bits", 3),
          ("twoOctets10Bits", 1))
    )


_FrLportAddrDLCILen_Type.__name__ = "Integer32"
_FrLportAddrDLCILen_Object = MibTableColumn
frLportAddrDLCILen = _FrLportAddrDLCILen_Object(
    (1, 3, 6, 1, 2, 1, 10, 44, 1, 1, 1, 5),
    _FrLportAddrDLCILen_Type()
)
frLportAddrDLCILen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frLportAddrDLCILen.setStatus("current")
if mibBuilder.loadTexts:
    frLportAddrDLCILen.setUnits("Octets")


class _FrLportVCSigProtocol_Type(Integer32):
    """Custom type frLportVCSigProtocol based on Integer32"""
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
        *(("ansiT1617B", 4),
          ("ansiT1617D", 3),
          ("ccittQ933A", 5),
          ("lmi", 2),
          ("none", 1))
    )


_FrLportVCSigProtocol_Type.__name__ = "Integer32"
_FrLportVCSigProtocol_Object = MibTableColumn
frLportVCSigProtocol = _FrLportVCSigProtocol_Object(
    (1, 3, 6, 1, 2, 1, 10, 44, 1, 1, 1, 6),
    _FrLportVCSigProtocol_Type()
)
frLportVCSigProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frLportVCSigProtocol.setStatus("current")
_FrLportVCSigPointer_Type = ObjectIdentifier
_FrLportVCSigPointer_Object = MibTableColumn
frLportVCSigPointer = _FrLportVCSigPointer_Object(
    (1, 3, 6, 1, 2, 1, 10, 44, 1, 1, 1, 7),
    _FrLportVCSigPointer_Type()
)
frLportVCSigPointer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frLportVCSigPointer.setStatus("deprecated")


class _FrLportDLCIIndexValue_Type(Integer32):
    """Custom type frLportDLCIIndexValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 4194303),
    )


_FrLportDLCIIndexValue_Type.__name__ = "Integer32"
_FrLportDLCIIndexValue_Object = MibTableColumn
frLportDLCIIndexValue = _FrLportDLCIIndexValue_Object(
    (1, 3, 6, 1, 2, 1, 10, 44, 1, 1, 1, 8),
    _FrLportDLCIIndexValue_Type()
)
frLportDLCIIndexValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frLportDLCIIndexValue.setStatus("current")


class _FrLportTypeAdmin_Type(Integer32):
    """Custom type frLportTypeAdmin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("nni", 2),
          ("uni", 1))
    )


_FrLportTypeAdmin_Type.__name__ = "Integer32"
_FrLportTypeAdmin_Object = MibTableColumn
frLportTypeAdmin = _FrLportTypeAdmin_Object(
    (1, 3, 6, 1, 2, 1, 10, 44, 1, 1, 1, 9),
    _FrLportTypeAdmin_Type()
)
frLportTypeAdmin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frLportTypeAdmin.setStatus("current")


class _FrLportVCSigProtocolAdmin_Type(Integer32):
    """Custom type frLportVCSigProtocolAdmin based on Integer32"""
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
        *(("ansiT1617B", 4),
          ("ansiT1617D", 3),
          ("ccittQ933A", 5),
          ("lmi", 2),
          ("none", 1))
    )


_FrLportVCSigProtocolAdmin_Type.__name__ = "Integer32"
_FrLportVCSigProtocolAdmin_Object = MibTableColumn
frLportVCSigProtocolAdmin = _FrLportVCSigProtocolAdmin_Object(
    (1, 3, 6, 1, 2, 1, 10, 44, 1, 1, 1, 10),
    _FrLportVCSigProtocolAdmin_Type()
)
frLportVCSigProtocolAdmin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frLportVCSigProtocolAdmin.setStatus("current")


class _FrLportFragControl_Type(Integer32):
    """Custom type frLportFragControl based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_FrLportFragControl_Type.__name__ = "Integer32"
_FrLportFragControl_Object = MibTableColumn
frLportFragControl = _FrLportFragControl_Object(
    (1, 3, 6, 1, 2, 1, 10, 44, 1, 1, 1, 11),
    _FrLportFragControl_Type()
)
frLportFragControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frLportFragControl.setStatus("current")


class _FrLportFragSize_Type(Integer32):
    """Custom type frLportFragSize based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4096),
    )


_FrLportFragSize_Type.__name__ = "Integer32"
_FrLportFragSize_Object = MibTableColumn
frLportFragSize = _FrLportFragSize_Object(
    (1, 3, 6, 1, 2, 1, 10, 44, 1, 1, 1, 12),
    _FrLportFragSize_Type()
)
frLportFragSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frLportFragSize.setStatus("current")
if mibBuilder.loadTexts:
    frLportFragSize.setUnits("Octets")
_FrMgtVCSigTable_Object = MibTable
frMgtVCSigTable = _FrMgtVCSigTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 44, 1, 2)
)
if mibBuilder.loadTexts:
    frMgtVCSigTable.setStatus("current")
_FrMgtVCSigEntry_Object = MibTableRow
frMgtVCSigEntry = _FrMgtVCSigEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 44, 1, 2, 1)
)
frMgtVCSigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    frMgtVCSigEntry.setStatus("current")


class _FrMgtVCSigProced_Type(Integer32):
    """Custom type frMgtVCSigProced based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("bidirect", 2),
          ("u2nnet", 1),
          ("u2nuser", 3))
    )


_FrMgtVCSigProced_Type.__name__ = "Integer32"
_FrMgtVCSigProced_Object = MibTableColumn
frMgtVCSigProced = _FrMgtVCSigProced_Object(
    (1, 3, 6, 1, 2, 1, 10, 44, 1, 2, 1, 1),
    _FrMgtVCSigProced_Type()
)
frMgtVCSigProced.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frMgtVCSigProced.setStatus("current")


class _FrMgtVCSigUserN391_Type(Integer32):
    """Custom type frMgtVCSigUserN391 based on Integer32"""
    defaultValue = 6

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_FrMgtVCSigUserN391_Type.__name__ = "Integer32"
_FrMgtVCSigUserN391_Object = MibTableColumn
frMgtVCSigUserN391 = _FrMgtVCSigUserN391_Object(
    (1, 3, 6, 1, 2, 1, 10, 44, 1, 2, 1, 2),
    _FrMgtVCSigUserN391_Type()
)
frMgtVCSigUserN391.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frMgtVCSigUserN391.setStatus("current")
if mibBuilder.loadTexts:
    frMgtVCSigUserN391.setUnits("Polls")


class _FrMgtVCSigUserN392_Type(Integer32):
    """Custom type frMgtVCSigUserN392 based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_FrMgtVCSigUserN392_Type.__name__ = "Integer32"
_FrMgtVCSigUserN392_Object = MibTableColumn
frMgtVCSigUserN392 = _FrMgtVCSigUserN392_Object(
    (1, 3, 6, 1, 2, 1, 10, 44, 1, 2, 1, 3),
    _FrMgtVCSigUserN392_Type()
)
frMgtVCSigUserN392.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frMgtVCSigUserN392.setStatus("current")
if mibBuilder.loadTexts:
    frMgtVCSigUserN392.setUnits("Events")


class _FrMgtVCSigUserN393_Type(Integer32):
    """Custom type frMgtVCSigUserN393 based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_FrMgtVCSigUserN393_Type.__name__ = "Integer32"
_FrMgtVCSigUserN393_Object = MibTableColumn
frMgtVCSigUserN393 = _FrMgtVCSigUserN393_Object(
    (1, 3, 6, 1, 2, 1, 10, 44, 1, 2, 1, 4),
    _FrMgtVCSigUserN393_Type()
)
frMgtVCSigUserN393.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frMgtVCSigUserN393.setStatus("current")
if mibBuilder.loadTexts:
    frMgtVCSigUserN393.setUnits("Events")


class _FrMgtVCSigUserT391_Type(Integer32):
    """Custom type frMgtVCSigUserT391 based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 30),
    )


_FrMgtVCSigUserT391_Type.__name__ = "Integer32"
_FrMgtVCSigUserT391_Object = MibTableColumn
frMgtVCSigUserT391 = _FrMgtVCSigUserT391_Object(
    (1, 3, 6, 1, 2, 1, 10, 44, 1, 2, 1, 5),
    _FrMgtVCSigUserT391_Type()
)
frMgtVCSigUserT391.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frMgtVCSigUserT391.setStatus("current")
if mibBuilder.loadTexts:
    frMgtVCSigUserT391.setUnits("Seconds")


class _FrMgtVCSigNetN392_Type(Integer32):
    """Custom type frMgtVCSigNetN392 based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_FrMgtVCSigNetN392_Type.__name__ = "Integer32"
_FrMgtVCSigNetN392_Object = MibTableColumn
frMgtVCSigNetN392 = _FrMgtVCSigNetN392_Object(
    (1, 3, 6, 1, 2, 1, 10, 44, 1, 2, 1, 6),
    _FrMgtVCSigNetN392_Type()
)
frMgtVCSigNetN392.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frMgtVCSigNetN392.setStatus("current")
if mibBuilder.loadTexts:
    frMgtVCSigNetN392.setUnits("Events")


class _FrMgtVCSigNetN393_Type(Integer32):
    """Custom type frMgtVCSigNetN393 based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_FrMgtVCSigNetN393_Type.__name__ = "Integer32"
_FrMgtVCSigNetN393_Object = MibTableColumn
frMgtVCSigNetN393 = _FrMgtVCSigNetN393_Object(
    (1, 3, 6, 1, 2, 1, 10, 44, 1, 2, 1, 7),
    _FrMgtVCSigNetN393_Type()
)
frMgtVCSigNetN393.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frMgtVCSigNetN393.setStatus("current")
if mibBuilder.loadTexts:
    frMgtVCSigNetN393.setUnits("Events")


class _FrMgtVCSigNetT392_Type(Integer32):
    """Custom type frMgtVCSigNetT392 based on Integer32"""
    defaultValue = 15

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 30),
    )


_FrMgtVCSigNetT392_Type.__name__ = "Integer32"
_FrMgtVCSigNetT392_Object = MibTableColumn
frMgtVCSigNetT392 = _FrMgtVCSigNetT392_Object(
    (1, 3, 6, 1, 2, 1, 10, 44, 1, 2, 1, 8),
    _FrMgtVCSigNetT392_Type()
)
frMgtVCSigNetT392.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frMgtVCSigNetT392.setStatus("current")
if mibBuilder.loadTexts:
    frMgtVCSigNetT392.setUnits("Seconds")


class _FrMgtVCSigNetnN4_Type(Integer32):
    """Custom type frMgtVCSigNetnN4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 5),
    )


_FrMgtVCSigNetnN4_Type.__name__ = "Integer32"
_FrMgtVCSigNetnN4_Object = MibTableColumn
frMgtVCSigNetnN4 = _FrMgtVCSigNetnN4_Object(
    (1, 3, 6, 1, 2, 1, 10, 44, 1, 2, 1, 9),
    _FrMgtVCSigNetnN4_Type()
)
frMgtVCSigNetnN4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frMgtVCSigNetnN4.setStatus("current")
if mibBuilder.loadTexts:
    frMgtVCSigNetnN4.setUnits("Events")


class _FrMgtVCSigNetnT3_Type(Integer32):
    """Custom type frMgtVCSigNetnT3 based on Integer32"""
    defaultValue = 20

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 5),
        ValueRangeConstraint(10, 10),
        ValueRangeConstraint(15, 15),
        ValueRangeConstraint(20, 20),
        ValueRangeConstraint(25, 25),
        ValueRangeConstraint(30, 30),
    )


_FrMgtVCSigNetnT3_Type.__name__ = "Integer32"
_FrMgtVCSigNetnT3_Object = MibTableColumn
frMgtVCSigNetnT3 = _FrMgtVCSigNetnT3_Object(
    (1, 3, 6, 1, 2, 1, 10, 44, 1, 2, 1, 10),
    _FrMgtVCSigNetnT3_Type()
)
frMgtVCSigNetnT3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frMgtVCSigNetnT3.setStatus("current")
if mibBuilder.loadTexts:
    frMgtVCSigNetnT3.setUnits("Seconds")
_FrMgtVCSigUserLinkRelErrors_Type = Counter32
_FrMgtVCSigUserLinkRelErrors_Object = MibTableColumn
frMgtVCSigUserLinkRelErrors = _FrMgtVCSigUserLinkRelErrors_Object(
    (1, 3, 6, 1, 2, 1, 10, 44, 1, 2, 1, 11),
    _FrMgtVCSigUserLinkRelErrors_Type()
)
frMgtVCSigUserLinkRelErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frMgtVCSigUserLinkRelErrors.setStatus("current")
if mibBuilder.loadTexts:
    frMgtVCSigUserLinkRelErrors.setUnits("Errors")
_FrMgtVCSigUserProtErrors_Type = Counter32
_FrMgtVCSigUserProtErrors_Object = MibTableColumn
frMgtVCSigUserProtErrors = _FrMgtVCSigUserProtErrors_Object(
    (1, 3, 6, 1, 2, 1, 10, 44, 1, 2, 1, 12),
    _FrMgtVCSigUserProtErrors_Type()
)
frMgtVCSigUserProtErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frMgtVCSigUserProtErrors.setStatus("current")
if mibBuilder.loadTexts:
    frMgtVCSigUserProtErrors.setUnits("Errors")
_FrMgtVCSigUserChanInactive_Type = Counter32
_FrMgtVCSigUserChanInactive_Object = MibTableColumn
frMgtVCSigUserChanInactive = _FrMgtVCSigUserChanInactive_Object(
    (1, 3, 6, 1, 2, 1, 10, 44, 1, 2, 1, 13),
    _FrMgtVCSigUserChanInactive_Type()
)
frMgtVCSigUserChanInactive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frMgtVCSigUserChanInactive.setStatus("current")
if mibBuilder.loadTexts:
    frMgtVCSigUserChanInactive.setUnits("Events")
_FrMgtVCSigNetLinkRelErrors_Type = Counter32
_FrMgtVCSigNetLinkRelErrors_Object = MibTableColumn
frMgtVCSigNetLinkRelErrors = _FrMgtVCSigNetLinkRelErrors_Object(
    (1, 3, 6, 1, 2, 1, 10, 44, 1, 2, 1, 14),
    _FrMgtVCSigNetLinkRelErrors_Type()
)
frMgtVCSigNetLinkRelErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frMgtVCSigNetLinkRelErrors.setStatus("current")
if mibBuilder.loadTexts:
    frMgtVCSigNetLinkRelErrors.setUnits("Errors")
_FrMgtVCSigNetProtErrors_Type = Counter32
_FrMgtVCSigNetProtErrors_Object = MibTableColumn
frMgtVCSigNetProtErrors = _FrMgtVCSigNetProtErrors_Object(
    (1, 3, 6, 1, 2, 1, 10, 44, 1, 2, 1, 15),
    _FrMgtVCSigNetProtErrors_Type()
)
frMgtVCSigNetProtErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frMgtVCSigNetProtErrors.setStatus("current")
if mibBuilder.loadTexts:
    frMgtVCSigNetProtErrors.setUnits("Errors")
_FrMgtVCSigNetChanInactive_Type = Counter32
_FrMgtVCSigNetChanInactive_Object = MibTableColumn
frMgtVCSigNetChanInactive = _FrMgtVCSigNetChanInactive_Object(
    (1, 3, 6, 1, 2, 1, 10, 44, 1, 2, 1, 16),
    _FrMgtVCSigNetChanInactive_Type()
)
frMgtVCSigNetChanInactive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frMgtVCSigNetChanInactive.setStatus("current")
if mibBuilder.loadTexts:
    frMgtVCSigNetChanInactive.setUnits("Events")


class _FrMgtVCSigProcedAdmin_Type(Integer32):
    """Custom type frMgtVCSigProcedAdmin based on Integer32"""
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
        *(("bidirect", 2),
          ("u2nnet", 1),
          ("u2nuser", 3))
    )


_FrMgtVCSigProcedAdmin_Type.__name__ = "Integer32"
_FrMgtVCSigProcedAdmin_Object = MibTableColumn
frMgtVCSigProcedAdmin = _FrMgtVCSigProcedAdmin_Object(
    (1, 3, 6, 1, 2, 1, 10, 44, 1, 2, 1, 17),
    _FrMgtVCSigProcedAdmin_Type()
)
frMgtVCSigProcedAdmin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frMgtVCSigProcedAdmin.setStatus("current")


class _FrMgtVCSigUserN391Admin_Type(Integer32):
    """Custom type frMgtVCSigUserN391Admin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_FrMgtVCSigUserN391Admin_Type.__name__ = "Integer32"
_FrMgtVCSigUserN391Admin_Object = MibTableColumn
frMgtVCSigUserN391Admin = _FrMgtVCSigUserN391Admin_Object(
    (1, 3, 6, 1, 2, 1, 10, 44, 1, 2, 1, 18),
    _FrMgtVCSigUserN391Admin_Type()
)
frMgtVCSigUserN391Admin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frMgtVCSigUserN391Admin.setStatus("current")
if mibBuilder.loadTexts:
    frMgtVCSigUserN391Admin.setUnits("Polls")


class _FrMgtVCSigUserN392Admin_Type(Integer32):
    """Custom type frMgtVCSigUserN392Admin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_FrMgtVCSigUserN392Admin_Type.__name__ = "Integer32"
_FrMgtVCSigUserN392Admin_Object = MibTableColumn
frMgtVCSigUserN392Admin = _FrMgtVCSigUserN392Admin_Object(
    (1, 3, 6, 1, 2, 1, 10, 44, 1, 2, 1, 19),
    _FrMgtVCSigUserN392Admin_Type()
)
frMgtVCSigUserN392Admin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frMgtVCSigUserN392Admin.setStatus("current")
if mibBuilder.loadTexts:
    frMgtVCSigUserN392Admin.setUnits("Events")


class _FrMgtVCSigUserN393Admin_Type(Integer32):
    """Custom type frMgtVCSigUserN393Admin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_FrMgtVCSigUserN393Admin_Type.__name__ = "Integer32"
_FrMgtVCSigUserN393Admin_Object = MibTableColumn
frMgtVCSigUserN393Admin = _FrMgtVCSigUserN393Admin_Object(
    (1, 3, 6, 1, 2, 1, 10, 44, 1, 2, 1, 20),
    _FrMgtVCSigUserN393Admin_Type()
)
frMgtVCSigUserN393Admin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frMgtVCSigUserN393Admin.setStatus("current")
if mibBuilder.loadTexts:
    frMgtVCSigUserN393Admin.setUnits("Events")


class _FrMgtVCSigUserT391Admin_Type(Integer32):
    """Custom type frMgtVCSigUserT391Admin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 30),
    )


_FrMgtVCSigUserT391Admin_Type.__name__ = "Integer32"
_FrMgtVCSigUserT391Admin_Object = MibTableColumn
frMgtVCSigUserT391Admin = _FrMgtVCSigUserT391Admin_Object(
    (1, 3, 6, 1, 2, 1, 10, 44, 1, 2, 1, 21),
    _FrMgtVCSigUserT391Admin_Type()
)
frMgtVCSigUserT391Admin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frMgtVCSigUserT391Admin.setStatus("current")
if mibBuilder.loadTexts:
    frMgtVCSigUserT391Admin.setUnits("Seconds")


class _FrMgtVCSigNetN392Admin_Type(Integer32):
    """Custom type frMgtVCSigNetN392Admin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_FrMgtVCSigNetN392Admin_Type.__name__ = "Integer32"
_FrMgtVCSigNetN392Admin_Object = MibTableColumn
frMgtVCSigNetN392Admin = _FrMgtVCSigNetN392Admin_Object(
    (1, 3, 6, 1, 2, 1, 10, 44, 1, 2, 1, 22),
    _FrMgtVCSigNetN392Admin_Type()
)
frMgtVCSigNetN392Admin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frMgtVCSigNetN392Admin.setStatus("current")
if mibBuilder.loadTexts:
    frMgtVCSigNetN392Admin.setUnits("Events")


class _FrMgtVCSigNetN393Admin_Type(Integer32):
    """Custom type frMgtVCSigNetN393Admin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_FrMgtVCSigNetN393Admin_Type.__name__ = "Integer32"
_FrMgtVCSigNetN393Admin_Object = MibTableColumn
frMgtVCSigNetN393Admin = _FrMgtVCSigNetN393Admin_Object(
    (1, 3, 6, 1, 2, 1, 10, 44, 1, 2, 1, 23),
    _FrMgtVCSigNetN393Admin_Type()
)
frMgtVCSigNetN393Admin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frMgtVCSigNetN393Admin.setStatus("current")
if mibBuilder.loadTexts:
    frMgtVCSigNetN393Admin.setUnits("Events")


class _FrMgtVCSigNetT392Admin_Type(Integer32):
    """Custom type frMgtVCSigNetT392Admin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 30),
    )


_FrMgtVCSigNetT392Admin_Type.__name__ = "Integer32"
_FrMgtVCSigNetT392Admin_Object = MibTableColumn
frMgtVCSigNetT392Admin = _FrMgtVCSigNetT392Admin_Object(
    (1, 3, 6, 1, 2, 1, 10, 44, 1, 2, 1, 24),
    _FrMgtVCSigNetT392Admin_Type()
)
frMgtVCSigNetT392Admin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frMgtVCSigNetT392Admin.setStatus("current")
if mibBuilder.loadTexts:
    frMgtVCSigNetT392Admin.setUnits("Seconds")


class _FrMgtVCSigNetnT3Admin_Type(Integer32):
    """Custom type frMgtVCSigNetnT3Admin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 5),
        ValueRangeConstraint(10, 10),
        ValueRangeConstraint(15, 15),
        ValueRangeConstraint(20, 20),
        ValueRangeConstraint(25, 25),
        ValueRangeConstraint(30, 30),
    )


_FrMgtVCSigNetnT3Admin_Type.__name__ = "Integer32"
_FrMgtVCSigNetnT3Admin_Object = MibTableColumn
frMgtVCSigNetnT3Admin = _FrMgtVCSigNetnT3Admin_Object(
    (1, 3, 6, 1, 2, 1, 10, 44, 1, 2, 1, 25),
    _FrMgtVCSigNetnT3Admin_Type()
)
frMgtVCSigNetnT3Admin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frMgtVCSigNetnT3Admin.setStatus("current")
if mibBuilder.loadTexts:
    frMgtVCSigNetnT3Admin.setUnits("Seconds")
_FrPVCEndptTable_Object = MibTable
frPVCEndptTable = _FrPVCEndptTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 44, 1, 3)
)
if mibBuilder.loadTexts:
    frPVCEndptTable.setStatus("current")
_FrPVCEndptEntry_Object = MibTableRow
frPVCEndptEntry = _FrPVCEndptEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 44, 1, 3, 1)
)
frPVCEndptEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "FRNETSERV-MIB", "frPVCEndptDLCIIndex"),
)
if mibBuilder.loadTexts:
    frPVCEndptEntry.setStatus("current")


class _FrPVCEndptDLCIIndex_Type(Integer32):
    """Custom type frPVCEndptDLCIIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 4194303),
    )


_FrPVCEndptDLCIIndex_Type.__name__ = "Integer32"
_FrPVCEndptDLCIIndex_Object = MibTableColumn
frPVCEndptDLCIIndex = _FrPVCEndptDLCIIndex_Object(
    (1, 3, 6, 1, 2, 1, 10, 44, 1, 3, 1, 1),
    _FrPVCEndptDLCIIndex_Type()
)
frPVCEndptDLCIIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    frPVCEndptDLCIIndex.setStatus("current")


class _FrPVCEndptInMaxFrameSize_Type(Integer32):
    """Custom type frPVCEndptInMaxFrameSize based on Integer32"""
    defaultValue = 1600

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4096),
    )


_FrPVCEndptInMaxFrameSize_Type.__name__ = "Integer32"
_FrPVCEndptInMaxFrameSize_Object = MibTableColumn
frPVCEndptInMaxFrameSize = _FrPVCEndptInMaxFrameSize_Object(
    (1, 3, 6, 1, 2, 1, 10, 44, 1, 3, 1, 2),
    _FrPVCEndptInMaxFrameSize_Type()
)
frPVCEndptInMaxFrameSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    frPVCEndptInMaxFrameSize.setStatus("current")
if mibBuilder.loadTexts:
    frPVCEndptInMaxFrameSize.setUnits("Octets")


class _FrPVCEndptInBc_Type(Integer32):
    """Custom type frPVCEndptInBc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_FrPVCEndptInBc_Type.__name__ = "Integer32"
_FrPVCEndptInBc_Object = MibTableColumn
frPVCEndptInBc = _FrPVCEndptInBc_Object(
    (1, 3, 6, 1, 2, 1, 10, 44, 1, 3, 1, 3),
    _FrPVCEndptInBc_Type()
)
frPVCEndptInBc.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    frPVCEndptInBc.setStatus("current")
if mibBuilder.loadTexts:
    frPVCEndptInBc.setUnits("Bits")


class _FrPVCEndptInBe_Type(Integer32):
    """Custom type frPVCEndptInBe based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_FrPVCEndptInBe_Type.__name__ = "Integer32"
_FrPVCEndptInBe_Object = MibTableColumn
frPVCEndptInBe = _FrPVCEndptInBe_Object(
    (1, 3, 6, 1, 2, 1, 10, 44, 1, 3, 1, 4),
    _FrPVCEndptInBe_Type()
)
frPVCEndptInBe.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    frPVCEndptInBe.setStatus("current")
if mibBuilder.loadTexts:
    frPVCEndptInBe.setUnits("Bits")


class _FrPVCEndptInCIR_Type(Integer32):
    """Custom type frPVCEndptInCIR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_FrPVCEndptInCIR_Type.__name__ = "Integer32"
_FrPVCEndptInCIR_Object = MibTableColumn
frPVCEndptInCIR = _FrPVCEndptInCIR_Object(
    (1, 3, 6, 1, 2, 1, 10, 44, 1, 3, 1, 5),
    _FrPVCEndptInCIR_Type()
)
frPVCEndptInCIR.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    frPVCEndptInCIR.setStatus("current")
if mibBuilder.loadTexts:
    frPVCEndptInCIR.setUnits("Bits per Second")


class _FrPVCEndptOutMaxFrameSize_Type(Integer32):
    """Custom type frPVCEndptOutMaxFrameSize based on Integer32"""
    defaultValue = 1600

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4096),
    )


_FrPVCEndptOutMaxFrameSize_Type.__name__ = "Integer32"
_FrPVCEndptOutMaxFrameSize_Object = MibTableColumn
frPVCEndptOutMaxFrameSize = _FrPVCEndptOutMaxFrameSize_Object(
    (1, 3, 6, 1, 2, 1, 10, 44, 1, 3, 1, 6),
    _FrPVCEndptOutMaxFrameSize_Type()
)
frPVCEndptOutMaxFrameSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    frPVCEndptOutMaxFrameSize.setStatus("current")
if mibBuilder.loadTexts:
    frPVCEndptOutMaxFrameSize.setUnits("Octets")


class _FrPVCEndptOutBc_Type(Integer32):
    """Custom type frPVCEndptOutBc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_FrPVCEndptOutBc_Type.__name__ = "Integer32"
_FrPVCEndptOutBc_Object = MibTableColumn
frPVCEndptOutBc = _FrPVCEndptOutBc_Object(
    (1, 3, 6, 1, 2, 1, 10, 44, 1, 3, 1, 7),
    _FrPVCEndptOutBc_Type()
)
frPVCEndptOutBc.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    frPVCEndptOutBc.setStatus("current")
if mibBuilder.loadTexts:
    frPVCEndptOutBc.setUnits("Bits")


class _FrPVCEndptOutBe_Type(Integer32):
    """Custom type frPVCEndptOutBe based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_FrPVCEndptOutBe_Type.__name__ = "Integer32"
_FrPVCEndptOutBe_Object = MibTableColumn
frPVCEndptOutBe = _FrPVCEndptOutBe_Object(
    (1, 3, 6, 1, 2, 1, 10, 44, 1, 3, 1, 8),
    _FrPVCEndptOutBe_Type()
)
frPVCEndptOutBe.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    frPVCEndptOutBe.setStatus("current")
if mibBuilder.loadTexts:
    frPVCEndptOutBe.setUnits("Bits")


class _FrPVCEndptOutCIR_Type(Integer32):
    """Custom type frPVCEndptOutCIR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_FrPVCEndptOutCIR_Type.__name__ = "Integer32"
_FrPVCEndptOutCIR_Object = MibTableColumn
frPVCEndptOutCIR = _FrPVCEndptOutCIR_Object(
    (1, 3, 6, 1, 2, 1, 10, 44, 1, 3, 1, 9),
    _FrPVCEndptOutCIR_Type()
)
frPVCEndptOutCIR.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    frPVCEndptOutCIR.setStatus("current")
if mibBuilder.loadTexts:
    frPVCEndptOutCIR.setUnits("Bits per Second")


class _FrPVCEndptConnectIdentifier_Type(Integer32):
    """Custom type frPVCEndptConnectIdentifier based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FrPVCEndptConnectIdentifier_Type.__name__ = "Integer32"
_FrPVCEndptConnectIdentifier_Object = MibTableColumn
frPVCEndptConnectIdentifier = _FrPVCEndptConnectIdentifier_Object(
    (1, 3, 6, 1, 2, 1, 10, 44, 1, 3, 1, 10),
    _FrPVCEndptConnectIdentifier_Type()
)
frPVCEndptConnectIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frPVCEndptConnectIdentifier.setStatus("current")
_FrPVCEndptRowStatus_Type = RowStatus
_FrPVCEndptRowStatus_Object = MibTableColumn
frPVCEndptRowStatus = _FrPVCEndptRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 10, 44, 1, 3, 1, 11),
    _FrPVCEndptRowStatus_Type()
)
frPVCEndptRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    frPVCEndptRowStatus.setStatus("current")


class _FrPVCEndptRcvdSigStatus_Type(Integer32):
    """Custom type frPVCEndptRcvdSigStatus based on Integer32"""
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
          ("deleted", 1),
          ("inactive", 3),
          ("none", 4))
    )


_FrPVCEndptRcvdSigStatus_Type.__name__ = "Integer32"
_FrPVCEndptRcvdSigStatus_Object = MibTableColumn
frPVCEndptRcvdSigStatus = _FrPVCEndptRcvdSigStatus_Object(
    (1, 3, 6, 1, 2, 1, 10, 44, 1, 3, 1, 12),
    _FrPVCEndptRcvdSigStatus_Type()
)
frPVCEndptRcvdSigStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frPVCEndptRcvdSigStatus.setStatus("current")
_FrPVCEndptInFrames_Type = Counter32
_FrPVCEndptInFrames_Object = MibTableColumn
frPVCEndptInFrames = _FrPVCEndptInFrames_Object(
    (1, 3, 6, 1, 2, 1, 10, 44, 1, 3, 1, 13),
    _FrPVCEndptInFrames_Type()
)
frPVCEndptInFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frPVCEndptInFrames.setStatus("current")
if mibBuilder.loadTexts:
    frPVCEndptInFrames.setUnits("Frames")
_FrPVCEndptOutFrames_Type = Counter32
_FrPVCEndptOutFrames_Object = MibTableColumn
frPVCEndptOutFrames = _FrPVCEndptOutFrames_Object(
    (1, 3, 6, 1, 2, 1, 10, 44, 1, 3, 1, 14),
    _FrPVCEndptOutFrames_Type()
)
frPVCEndptOutFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frPVCEndptOutFrames.setStatus("current")
if mibBuilder.loadTexts:
    frPVCEndptOutFrames.setUnits("Frames")
_FrPVCEndptInDEFrames_Type = Counter32
_FrPVCEndptInDEFrames_Object = MibTableColumn
frPVCEndptInDEFrames = _FrPVCEndptInDEFrames_Object(
    (1, 3, 6, 1, 2, 1, 10, 44, 1, 3, 1, 15),
    _FrPVCEndptInDEFrames_Type()
)
frPVCEndptInDEFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frPVCEndptInDEFrames.setStatus("current")
if mibBuilder.loadTexts:
    frPVCEndptInDEFrames.setUnits("Frames")
_FrPVCEndptInExcessFrames_Type = Counter32
_FrPVCEndptInExcessFrames_Object = MibTableColumn
frPVCEndptInExcessFrames = _FrPVCEndptInExcessFrames_Object(
    (1, 3, 6, 1, 2, 1, 10, 44, 1, 3, 1, 16),
    _FrPVCEndptInExcessFrames_Type()
)
frPVCEndptInExcessFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frPVCEndptInExcessFrames.setStatus("current")
if mibBuilder.loadTexts:
    frPVCEndptInExcessFrames.setUnits("Frames")
_FrPVCEndptOutExcessFrames_Type = Counter32
_FrPVCEndptOutExcessFrames_Object = MibTableColumn
frPVCEndptOutExcessFrames = _FrPVCEndptOutExcessFrames_Object(
    (1, 3, 6, 1, 2, 1, 10, 44, 1, 3, 1, 17),
    _FrPVCEndptOutExcessFrames_Type()
)
frPVCEndptOutExcessFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frPVCEndptOutExcessFrames.setStatus("current")
if mibBuilder.loadTexts:
    frPVCEndptOutExcessFrames.setUnits("Frames")
_FrPVCEndptInDiscards_Type = Counter32
_FrPVCEndptInDiscards_Object = MibTableColumn
frPVCEndptInDiscards = _FrPVCEndptInDiscards_Object(
    (1, 3, 6, 1, 2, 1, 10, 44, 1, 3, 1, 18),
    _FrPVCEndptInDiscards_Type()
)
frPVCEndptInDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frPVCEndptInDiscards.setStatus("current")
if mibBuilder.loadTexts:
    frPVCEndptInDiscards.setUnits("Frames")
_FrPVCEndptInOctets_Type = Counter32
_FrPVCEndptInOctets_Object = MibTableColumn
frPVCEndptInOctets = _FrPVCEndptInOctets_Object(
    (1, 3, 6, 1, 2, 1, 10, 44, 1, 3, 1, 19),
    _FrPVCEndptInOctets_Type()
)
frPVCEndptInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frPVCEndptInOctets.setStatus("current")
if mibBuilder.loadTexts:
    frPVCEndptInOctets.setUnits("Octets")
_FrPVCEndptOutOctets_Type = Counter32
_FrPVCEndptOutOctets_Object = MibTableColumn
frPVCEndptOutOctets = _FrPVCEndptOutOctets_Object(
    (1, 3, 6, 1, 2, 1, 10, 44, 1, 3, 1, 20),
    _FrPVCEndptOutOctets_Type()
)
frPVCEndptOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frPVCEndptOutOctets.setStatus("current")
if mibBuilder.loadTexts:
    frPVCEndptOutOctets.setUnits("Octets")
_FrPVCEndptInDiscardsDESet_Type = Counter32
_FrPVCEndptInDiscardsDESet_Object = MibTableColumn
frPVCEndptInDiscardsDESet = _FrPVCEndptInDiscardsDESet_Object(
    (1, 3, 6, 1, 2, 1, 10, 44, 1, 3, 1, 21),
    _FrPVCEndptInDiscardsDESet_Type()
)
frPVCEndptInDiscardsDESet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frPVCEndptInDiscardsDESet.setStatus("current")
if mibBuilder.loadTexts:
    frPVCEndptInDiscardsDESet.setUnits("Frames")
_FrPVCEndptInFramesFECNSet_Type = Counter32
_FrPVCEndptInFramesFECNSet_Object = MibTableColumn
frPVCEndptInFramesFECNSet = _FrPVCEndptInFramesFECNSet_Object(
    (1, 3, 6, 1, 2, 1, 10, 44, 1, 3, 1, 22),
    _FrPVCEndptInFramesFECNSet_Type()
)
frPVCEndptInFramesFECNSet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frPVCEndptInFramesFECNSet.setStatus("current")
if mibBuilder.loadTexts:
    frPVCEndptInFramesFECNSet.setUnits("Frames")
_FrPVCEndptOutFramesFECNSet_Type = Counter32
_FrPVCEndptOutFramesFECNSet_Object = MibTableColumn
frPVCEndptOutFramesFECNSet = _FrPVCEndptOutFramesFECNSet_Object(
    (1, 3, 6, 1, 2, 1, 10, 44, 1, 3, 1, 23),
    _FrPVCEndptOutFramesFECNSet_Type()
)
frPVCEndptOutFramesFECNSet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frPVCEndptOutFramesFECNSet.setStatus("current")
if mibBuilder.loadTexts:
    frPVCEndptOutFramesFECNSet.setUnits("Frames")
_FrPVCEndptInFramesBECNSet_Type = Counter32
_FrPVCEndptInFramesBECNSet_Object = MibTableColumn
frPVCEndptInFramesBECNSet = _FrPVCEndptInFramesBECNSet_Object(
    (1, 3, 6, 1, 2, 1, 10, 44, 1, 3, 1, 24),
    _FrPVCEndptInFramesBECNSet_Type()
)
frPVCEndptInFramesBECNSet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frPVCEndptInFramesBECNSet.setStatus("current")
if mibBuilder.loadTexts:
    frPVCEndptInFramesBECNSet.setUnits("Frames")
_FrPVCEndptOutFramesBECNSet_Type = Counter32
_FrPVCEndptOutFramesBECNSet_Object = MibTableColumn
frPVCEndptOutFramesBECNSet = _FrPVCEndptOutFramesBECNSet_Object(
    (1, 3, 6, 1, 2, 1, 10, 44, 1, 3, 1, 25),
    _FrPVCEndptOutFramesBECNSet_Type()
)
frPVCEndptOutFramesBECNSet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frPVCEndptOutFramesBECNSet.setStatus("current")
if mibBuilder.loadTexts:
    frPVCEndptOutFramesBECNSet.setUnits("Frames")
_FrPVCEndptInCongDiscards_Type = Counter32
_FrPVCEndptInCongDiscards_Object = MibTableColumn
frPVCEndptInCongDiscards = _FrPVCEndptInCongDiscards_Object(
    (1, 3, 6, 1, 2, 1, 10, 44, 1, 3, 1, 26),
    _FrPVCEndptInCongDiscards_Type()
)
frPVCEndptInCongDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frPVCEndptInCongDiscards.setStatus("current")
if mibBuilder.loadTexts:
    frPVCEndptInCongDiscards.setUnits("Frames")
_FrPVCEndptInDECongDiscards_Type = Counter32
_FrPVCEndptInDECongDiscards_Object = MibTableColumn
frPVCEndptInDECongDiscards = _FrPVCEndptInDECongDiscards_Object(
    (1, 3, 6, 1, 2, 1, 10, 44, 1, 3, 1, 27),
    _FrPVCEndptInDECongDiscards_Type()
)
frPVCEndptInDECongDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frPVCEndptInDECongDiscards.setStatus("current")
if mibBuilder.loadTexts:
    frPVCEndptInDECongDiscards.setUnits("Frames")
_FrPVCEndptOutCongDiscards_Type = Counter32
_FrPVCEndptOutCongDiscards_Object = MibTableColumn
frPVCEndptOutCongDiscards = _FrPVCEndptOutCongDiscards_Object(
    (1, 3, 6, 1, 2, 1, 10, 44, 1, 3, 1, 28),
    _FrPVCEndptOutCongDiscards_Type()
)
frPVCEndptOutCongDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frPVCEndptOutCongDiscards.setStatus("current")
if mibBuilder.loadTexts:
    frPVCEndptOutCongDiscards.setUnits("Frames")
_FrPVCEndptOutDECongDiscards_Type = Counter32
_FrPVCEndptOutDECongDiscards_Object = MibTableColumn
frPVCEndptOutDECongDiscards = _FrPVCEndptOutDECongDiscards_Object(
    (1, 3, 6, 1, 2, 1, 10, 44, 1, 3, 1, 29),
    _FrPVCEndptOutDECongDiscards_Type()
)
frPVCEndptOutDECongDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frPVCEndptOutDECongDiscards.setStatus("current")
if mibBuilder.loadTexts:
    frPVCEndptOutDECongDiscards.setUnits("Frames")
_FrPVCEndptOutDEFrames_Type = Counter32
_FrPVCEndptOutDEFrames_Object = MibTableColumn
frPVCEndptOutDEFrames = _FrPVCEndptOutDEFrames_Object(
    (1, 3, 6, 1, 2, 1, 10, 44, 1, 3, 1, 30),
    _FrPVCEndptOutDEFrames_Type()
)
frPVCEndptOutDEFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frPVCEndptOutDEFrames.setStatus("current")
if mibBuilder.loadTexts:
    frPVCEndptOutDEFrames.setUnits("Frames")


class _FrPVCEndptAtmIwfConnIndex_Type(Integer32):
    """Custom type frPVCEndptAtmIwfConnIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FrPVCEndptAtmIwfConnIndex_Type.__name__ = "Integer32"
_FrPVCEndptAtmIwfConnIndex_Object = MibTableColumn
frPVCEndptAtmIwfConnIndex = _FrPVCEndptAtmIwfConnIndex_Object(
    (1, 3, 6, 1, 2, 1, 10, 44, 1, 3, 1, 31),
    _FrPVCEndptAtmIwfConnIndex_Type()
)
frPVCEndptAtmIwfConnIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frPVCEndptAtmIwfConnIndex.setStatus("current")


class _FrPVCConnectIndexValue_Type(Integer32):
    """Custom type frPVCConnectIndexValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FrPVCConnectIndexValue_Type.__name__ = "Integer32"
_FrPVCConnectIndexValue_Object = MibScalar
frPVCConnectIndexValue = _FrPVCConnectIndexValue_Object(
    (1, 3, 6, 1, 2, 1, 10, 44, 1, 4),
    _FrPVCConnectIndexValue_Type()
)
frPVCConnectIndexValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frPVCConnectIndexValue.setStatus("current")
_FrPVCConnectTable_Object = MibTable
frPVCConnectTable = _FrPVCConnectTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 44, 1, 5)
)
if mibBuilder.loadTexts:
    frPVCConnectTable.setStatus("current")
_FrPVCConnectEntry_Object = MibTableRow
frPVCConnectEntry = _FrPVCConnectEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 44, 1, 5, 1)
)
frPVCConnectEntry.setIndexNames(
    (0, "FRNETSERV-MIB", "frPVCConnectIndex"),
    (0, "FRNETSERV-MIB", "frPVCConnectLowIfIndex"),
    (0, "FRNETSERV-MIB", "frPVCConnectLowDLCIIndex"),
    (0, "FRNETSERV-MIB", "frPVCConnectHighIfIndex"),
    (0, "FRNETSERV-MIB", "frPVCConnectHighDLCIIndex"),
)
if mibBuilder.loadTexts:
    frPVCConnectEntry.setStatus("current")


class _FrPVCConnectIndex_Type(Integer32):
    """Custom type frPVCConnectIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FrPVCConnectIndex_Type.__name__ = "Integer32"
_FrPVCConnectIndex_Object = MibTableColumn
frPVCConnectIndex = _FrPVCConnectIndex_Object(
    (1, 3, 6, 1, 2, 1, 10, 44, 1, 5, 1, 1),
    _FrPVCConnectIndex_Type()
)
frPVCConnectIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    frPVCConnectIndex.setStatus("current")
_FrPVCConnectLowIfIndex_Type = InterfaceIndex
_FrPVCConnectLowIfIndex_Object = MibTableColumn
frPVCConnectLowIfIndex = _FrPVCConnectLowIfIndex_Object(
    (1, 3, 6, 1, 2, 1, 10, 44, 1, 5, 1, 2),
    _FrPVCConnectLowIfIndex_Type()
)
frPVCConnectLowIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    frPVCConnectLowIfIndex.setStatus("current")


class _FrPVCConnectLowDLCIIndex_Type(Integer32):
    """Custom type frPVCConnectLowDLCIIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 4194303),
    )


_FrPVCConnectLowDLCIIndex_Type.__name__ = "Integer32"
_FrPVCConnectLowDLCIIndex_Object = MibTableColumn
frPVCConnectLowDLCIIndex = _FrPVCConnectLowDLCIIndex_Object(
    (1, 3, 6, 1, 2, 1, 10, 44, 1, 5, 1, 3),
    _FrPVCConnectLowDLCIIndex_Type()
)
frPVCConnectLowDLCIIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    frPVCConnectLowDLCIIndex.setStatus("current")
_FrPVCConnectHighIfIndex_Type = InterfaceIndex
_FrPVCConnectHighIfIndex_Object = MibTableColumn
frPVCConnectHighIfIndex = _FrPVCConnectHighIfIndex_Object(
    (1, 3, 6, 1, 2, 1, 10, 44, 1, 5, 1, 4),
    _FrPVCConnectHighIfIndex_Type()
)
frPVCConnectHighIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    frPVCConnectHighIfIndex.setStatus("current")


class _FrPVCConnectHighDLCIIndex_Type(Integer32):
    """Custom type frPVCConnectHighDLCIIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 4194303),
    )


_FrPVCConnectHighDLCIIndex_Type.__name__ = "Integer32"
_FrPVCConnectHighDLCIIndex_Object = MibTableColumn
frPVCConnectHighDLCIIndex = _FrPVCConnectHighDLCIIndex_Object(
    (1, 3, 6, 1, 2, 1, 10, 44, 1, 5, 1, 5),
    _FrPVCConnectHighDLCIIndex_Type()
)
frPVCConnectHighDLCIIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    frPVCConnectHighDLCIIndex.setStatus("current")


class _FrPVCConnectAdminStatus_Type(Integer32):
    """Custom type frPVCConnectAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 2),
          ("testing", 3))
    )


_FrPVCConnectAdminStatus_Type.__name__ = "Integer32"
_FrPVCConnectAdminStatus_Object = MibTableColumn
frPVCConnectAdminStatus = _FrPVCConnectAdminStatus_Object(
    (1, 3, 6, 1, 2, 1, 10, 44, 1, 5, 1, 6),
    _FrPVCConnectAdminStatus_Type()
)
frPVCConnectAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    frPVCConnectAdminStatus.setStatus("current")


class _FrPVCConnectL2hOperStatus_Type(Integer32):
    """Custom type frPVCConnectL2hOperStatus based on Integer32"""
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
        *(("active", 1),
          ("inactive", 2),
          ("testing", 3),
          ("unknown", 4))
    )


_FrPVCConnectL2hOperStatus_Type.__name__ = "Integer32"
_FrPVCConnectL2hOperStatus_Object = MibTableColumn
frPVCConnectL2hOperStatus = _FrPVCConnectL2hOperStatus_Object(
    (1, 3, 6, 1, 2, 1, 10, 44, 1, 5, 1, 7),
    _FrPVCConnectL2hOperStatus_Type()
)
frPVCConnectL2hOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frPVCConnectL2hOperStatus.setStatus("current")


class _FrPVCConnectH2lOperStatus_Type(Integer32):
    """Custom type frPVCConnectH2lOperStatus based on Integer32"""
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
        *(("active", 1),
          ("inactive", 2),
          ("testing", 3),
          ("unknown", 4))
    )


_FrPVCConnectH2lOperStatus_Type.__name__ = "Integer32"
_FrPVCConnectH2lOperStatus_Object = MibTableColumn
frPVCConnectH2lOperStatus = _FrPVCConnectH2lOperStatus_Object(
    (1, 3, 6, 1, 2, 1, 10, 44, 1, 5, 1, 8),
    _FrPVCConnectH2lOperStatus_Type()
)
frPVCConnectH2lOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frPVCConnectH2lOperStatus.setStatus("current")
_FrPVCConnectL2hLastChange_Type = TimeStamp
_FrPVCConnectL2hLastChange_Object = MibTableColumn
frPVCConnectL2hLastChange = _FrPVCConnectL2hLastChange_Object(
    (1, 3, 6, 1, 2, 1, 10, 44, 1, 5, 1, 9),
    _FrPVCConnectL2hLastChange_Type()
)
frPVCConnectL2hLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frPVCConnectL2hLastChange.setStatus("current")
_FrPVCConnectH2lLastChange_Type = TimeStamp
_FrPVCConnectH2lLastChange_Object = MibTableColumn
frPVCConnectH2lLastChange = _FrPVCConnectH2lLastChange_Object(
    (1, 3, 6, 1, 2, 1, 10, 44, 1, 5, 1, 10),
    _FrPVCConnectH2lLastChange_Type()
)
frPVCConnectH2lLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frPVCConnectH2lLastChange.setStatus("current")
_FrPVCConnectRowStatus_Type = RowStatus
_FrPVCConnectRowStatus_Object = MibTableColumn
frPVCConnectRowStatus = _FrPVCConnectRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 10, 44, 1, 5, 1, 11),
    _FrPVCConnectRowStatus_Type()
)
frPVCConnectRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    frPVCConnectRowStatus.setStatus("current")
_FrPVCConnectUserName_Type = SnmpAdminString
_FrPVCConnectUserName_Object = MibTableColumn
frPVCConnectUserName = _FrPVCConnectUserName_Object(
    (1, 3, 6, 1, 2, 1, 10, 44, 1, 5, 1, 12),
    _FrPVCConnectUserName_Type()
)
frPVCConnectUserName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    frPVCConnectUserName.setStatus("current")
_FrPVCConnectProviderName_Type = SnmpAdminString
_FrPVCConnectProviderName_Object = MibTableColumn
frPVCConnectProviderName = _FrPVCConnectProviderName_Object(
    (1, 3, 6, 1, 2, 1, 10, 44, 1, 5, 1, 13),
    _FrPVCConnectProviderName_Type()
)
frPVCConnectProviderName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    frPVCConnectProviderName.setStatus("current")
_FrAccountPVCTable_Object = MibTable
frAccountPVCTable = _FrAccountPVCTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 44, 1, 6)
)
if mibBuilder.loadTexts:
    frAccountPVCTable.setStatus("current")
_FrAccountPVCEntry_Object = MibTableRow
frAccountPVCEntry = _FrAccountPVCEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 44, 1, 6, 1)
)
frAccountPVCEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "FRNETSERV-MIB", "frAccountPVCDLCIIndex"),
)
if mibBuilder.loadTexts:
    frAccountPVCEntry.setStatus("current")


class _FrAccountPVCDLCIIndex_Type(Integer32):
    """Custom type frAccountPVCDLCIIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 4194303),
    )


_FrAccountPVCDLCIIndex_Type.__name__ = "Integer32"
_FrAccountPVCDLCIIndex_Object = MibTableColumn
frAccountPVCDLCIIndex = _FrAccountPVCDLCIIndex_Object(
    (1, 3, 6, 1, 2, 1, 10, 44, 1, 6, 1, 1),
    _FrAccountPVCDLCIIndex_Type()
)
frAccountPVCDLCIIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    frAccountPVCDLCIIndex.setStatus("current")
_FrAccountPVCSegmentSize_Type = Integer32
_FrAccountPVCSegmentSize_Object = MibTableColumn
frAccountPVCSegmentSize = _FrAccountPVCSegmentSize_Object(
    (1, 3, 6, 1, 2, 1, 10, 44, 1, 6, 1, 2),
    _FrAccountPVCSegmentSize_Type()
)
frAccountPVCSegmentSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frAccountPVCSegmentSize.setStatus("current")
if mibBuilder.loadTexts:
    frAccountPVCSegmentSize.setUnits("Octets")
_FrAccountPVCInSegments_Type = Counter32
_FrAccountPVCInSegments_Object = MibTableColumn
frAccountPVCInSegments = _FrAccountPVCInSegments_Object(
    (1, 3, 6, 1, 2, 1, 10, 44, 1, 6, 1, 3),
    _FrAccountPVCInSegments_Type()
)
frAccountPVCInSegments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frAccountPVCInSegments.setStatus("current")
if mibBuilder.loadTexts:
    frAccountPVCInSegments.setUnits("Segments")
_FrAccountPVCOutSegments_Type = Counter32
_FrAccountPVCOutSegments_Object = MibTableColumn
frAccountPVCOutSegments = _FrAccountPVCOutSegments_Object(
    (1, 3, 6, 1, 2, 1, 10, 44, 1, 6, 1, 4),
    _FrAccountPVCOutSegments_Type()
)
frAccountPVCOutSegments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frAccountPVCOutSegments.setStatus("current")
if mibBuilder.loadTexts:
    frAccountPVCOutSegments.setUnits("Segments")
_FrAccountLportTable_Object = MibTable
frAccountLportTable = _FrAccountLportTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 44, 1, 7)
)
if mibBuilder.loadTexts:
    frAccountLportTable.setStatus("current")
_FrAccountLportEntry_Object = MibTableRow
frAccountLportEntry = _FrAccountLportEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 44, 1, 7, 1)
)
frAccountLportEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    frAccountLportEntry.setStatus("current")
_FrAccountLportSegmentSize_Type = Integer32
_FrAccountLportSegmentSize_Object = MibTableColumn
frAccountLportSegmentSize = _FrAccountLportSegmentSize_Object(
    (1, 3, 6, 1, 2, 1, 10, 44, 1, 7, 1, 1),
    _FrAccountLportSegmentSize_Type()
)
frAccountLportSegmentSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frAccountLportSegmentSize.setStatus("current")
if mibBuilder.loadTexts:
    frAccountLportSegmentSize.setUnits("Octets")
_FrAccountLportInSegments_Type = Counter32
_FrAccountLportInSegments_Object = MibTableColumn
frAccountLportInSegments = _FrAccountLportInSegments_Object(
    (1, 3, 6, 1, 2, 1, 10, 44, 1, 7, 1, 2),
    _FrAccountLportInSegments_Type()
)
frAccountLportInSegments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frAccountLportInSegments.setStatus("current")
if mibBuilder.loadTexts:
    frAccountLportInSegments.setUnits("Segments")
_FrAccountLportOutSegments_Type = Counter32
_FrAccountLportOutSegments_Object = MibTableColumn
frAccountLportOutSegments = _FrAccountLportOutSegments_Object(
    (1, 3, 6, 1, 2, 1, 10, 44, 1, 7, 1, 3),
    _FrAccountLportOutSegments_Type()
)
frAccountLportOutSegments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frAccountLportOutSegments.setStatus("current")
if mibBuilder.loadTexts:
    frAccountLportOutSegments.setUnits("Segments")
_FrnetservTraps_ObjectIdentity = ObjectIdentity
frnetservTraps = _FrnetservTraps_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 44, 2)
)
_FrnetservTrapsPrefix_ObjectIdentity = ObjectIdentity
frnetservTrapsPrefix = _FrnetservTrapsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 44, 2, 0)
)
_FrnetservConformance_ObjectIdentity = ObjectIdentity
frnetservConformance = _FrnetservConformance_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 44, 3)
)
_FrnetservGroups_ObjectIdentity = ObjectIdentity
frnetservGroups = _FrnetservGroups_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 44, 3, 1)
)
_FrnetservCompliances_ObjectIdentity = ObjectIdentity
frnetservCompliances = _FrnetservCompliances_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 44, 3, 2)
)

# Managed Objects groups

frnetservLportGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 44, 3, 1, 1)
)
frnetservLportGroup.setObjects(
      *(("FRNETSERV-MIB", "frLportNumPlan"),
        ("FRNETSERV-MIB", "frLportContact"),
        ("FRNETSERV-MIB", "frLportLocation"),
        ("FRNETSERV-MIB", "frLportType"),
        ("FRNETSERV-MIB", "frLportAddrDLCILen"),
        ("FRNETSERV-MIB", "frLportVCSigProtocol"),
        ("FRNETSERV-MIB", "frLportVCSigPointer"))
)
if mibBuilder.loadTexts:
    frnetservLportGroup.setStatus("deprecated")

frnetservMgtVCSigGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 44, 3, 1, 2)
)
frnetservMgtVCSigGroup.setObjects(
      *(("FRNETSERV-MIB", "frMgtVCSigProced"),
        ("FRNETSERV-MIB", "frMgtVCSigUserN391"),
        ("FRNETSERV-MIB", "frMgtVCSigUserN392"),
        ("FRNETSERV-MIB", "frMgtVCSigUserN393"),
        ("FRNETSERV-MIB", "frMgtVCSigUserT391"),
        ("FRNETSERV-MIB", "frMgtVCSigNetN392"),
        ("FRNETSERV-MIB", "frMgtVCSigNetN393"),
        ("FRNETSERV-MIB", "frMgtVCSigNetT392"),
        ("FRNETSERV-MIB", "frMgtVCSigNetnN4"),
        ("FRNETSERV-MIB", "frMgtVCSigNetnT3"),
        ("FRNETSERV-MIB", "frMgtVCSigUserLinkRelErrors"),
        ("FRNETSERV-MIB", "frMgtVCSigUserProtErrors"),
        ("FRNETSERV-MIB", "frMgtVCSigUserChanInactive"),
        ("FRNETSERV-MIB", "frMgtVCSigNetLinkRelErrors"),
        ("FRNETSERV-MIB", "frMgtVCSigNetProtErrors"),
        ("FRNETSERV-MIB", "frMgtVCSigNetChanInactive"))
)
if mibBuilder.loadTexts:
    frnetservMgtVCSigGroup.setStatus("current")

frnetservPVCEndptGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 44, 3, 1, 3)
)
frnetservPVCEndptGroup.setObjects(
      *(("FRNETSERV-MIB", "frPVCConnectIndexValue"),
        ("FRNETSERV-MIB", "frPVCEndptInMaxFrameSize"),
        ("FRNETSERV-MIB", "frPVCEndptInBc"),
        ("FRNETSERV-MIB", "frPVCEndptInBe"),
        ("FRNETSERV-MIB", "frPVCEndptInCIR"),
        ("FRNETSERV-MIB", "frPVCEndptOutMaxFrameSize"),
        ("FRNETSERV-MIB", "frPVCEndptOutBc"),
        ("FRNETSERV-MIB", "frPVCEndptOutBe"),
        ("FRNETSERV-MIB", "frPVCEndptOutCIR"),
        ("FRNETSERV-MIB", "frPVCEndptConnectIdentifier"),
        ("FRNETSERV-MIB", "frPVCEndptRowStatus"),
        ("FRNETSERV-MIB", "frPVCEndptRcvdSigStatus"),
        ("FRNETSERV-MIB", "frPVCEndptInFrames"),
        ("FRNETSERV-MIB", "frPVCEndptOutFrames"),
        ("FRNETSERV-MIB", "frPVCEndptInDEFrames"),
        ("FRNETSERV-MIB", "frPVCEndptInExcessFrames"),
        ("FRNETSERV-MIB", "frPVCEndptOutExcessFrames"),
        ("FRNETSERV-MIB", "frPVCEndptInDiscards"),
        ("FRNETSERV-MIB", "frPVCEndptInOctets"),
        ("FRNETSERV-MIB", "frPVCEndptOutOctets"))
)
if mibBuilder.loadTexts:
    frnetservPVCEndptGroup.setStatus("current")

frnetservPVCConnectGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 44, 3, 1, 4)
)
frnetservPVCConnectGroup.setObjects(
      *(("FRNETSERV-MIB", "frPVCConnectAdminStatus"),
        ("FRNETSERV-MIB", "frPVCConnectL2hOperStatus"),
        ("FRNETSERV-MIB", "frPVCConnectH2lOperStatus"),
        ("FRNETSERV-MIB", "frPVCConnectL2hLastChange"),
        ("FRNETSERV-MIB", "frPVCConnectH2lLastChange"),
        ("FRNETSERV-MIB", "frPVCConnectRowStatus"))
)
if mibBuilder.loadTexts:
    frnetservPVCConnectGroup.setStatus("current")

frnetservAccountPVCGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 44, 3, 1, 5)
)
frnetservAccountPVCGroup.setObjects(
      *(("FRNETSERV-MIB", "frAccountPVCSegmentSize"),
        ("FRNETSERV-MIB", "frAccountPVCInSegments"),
        ("FRNETSERV-MIB", "frAccountPVCOutSegments"))
)
if mibBuilder.loadTexts:
    frnetservAccountPVCGroup.setStatus("current")

frnetservAccountLportGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 44, 3, 1, 6)
)
frnetservAccountLportGroup.setObjects(
      *(("FRNETSERV-MIB", "frAccountLportSegmentSize"),
        ("FRNETSERV-MIB", "frAccountLportInSegments"),
        ("FRNETSERV-MIB", "frAccountLportOutSegments"))
)
if mibBuilder.loadTexts:
    frnetservAccountLportGroup.setStatus("current")

frnetservLportGroup2 = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 44, 3, 1, 7)
)
frnetservLportGroup2.setObjects(
      *(("FRNETSERV-MIB", "frLportNumPlan"),
        ("FRNETSERV-MIB", "frLportContact"),
        ("FRNETSERV-MIB", "frLportLocation"),
        ("FRNETSERV-MIB", "frLportType"),
        ("FRNETSERV-MIB", "frLportAddrDLCILen"),
        ("FRNETSERV-MIB", "frLportVCSigProtocol"),
        ("FRNETSERV-MIB", "frLportFragControl"),
        ("FRNETSERV-MIB", "frLportFragSize"))
)
if mibBuilder.loadTexts:
    frnetservLportGroup2.setStatus("current")

frnetservPVCEndptGroup2 = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 44, 3, 1, 8)
)
frnetservPVCEndptGroup2.setObjects(
      *(("FRNETSERV-MIB", "frPVCEndptInDiscardsDESet"),
        ("FRNETSERV-MIB", "frPVCEndptInFramesFECNSet"),
        ("FRNETSERV-MIB", "frPVCEndptOutFramesFECNSet"),
        ("FRNETSERV-MIB", "frPVCEndptInFramesBECNSet"),
        ("FRNETSERV-MIB", "frPVCEndptOutFramesBECNSet"),
        ("FRNETSERV-MIB", "frPVCEndptInCongDiscards"),
        ("FRNETSERV-MIB", "frPVCEndptInDECongDiscards"),
        ("FRNETSERV-MIB", "frPVCEndptOutCongDiscards"),
        ("FRNETSERV-MIB", "frPVCEndptOutDECongDiscards"),
        ("FRNETSERV-MIB", "frPVCEndptOutDEFrames"),
        ("FRNETSERV-MIB", "frPVCEndptAtmIwfConnIndex"))
)
if mibBuilder.loadTexts:
    frnetservPVCEndptGroup2.setStatus("current")

frnetservPVCConnectNamesGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 44, 3, 1, 9)
)
frnetservPVCConnectNamesGroup.setObjects(
      *(("FRNETSERV-MIB", "frPVCConnectUserName"),
        ("FRNETSERV-MIB", "frPVCConnectProviderName"))
)
if mibBuilder.loadTexts:
    frnetservPVCConnectNamesGroup.setStatus("current")

frnetservLportAdminGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 44, 3, 1, 10)
)
frnetservLportAdminGroup.setObjects(
      *(("FRNETSERV-MIB", "frLportDLCIIndexValue"),
        ("FRNETSERV-MIB", "frLportTypeAdmin"),
        ("FRNETSERV-MIB", "frLportVCSigProtocolAdmin"))
)
if mibBuilder.loadTexts:
    frnetservLportAdminGroup.setStatus("current")

frnetservMgtVCSigAdminGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 44, 3, 1, 11)
)
frnetservMgtVCSigAdminGroup.setObjects(
      *(("FRNETSERV-MIB", "frMgtVCSigProcedAdmin"),
        ("FRNETSERV-MIB", "frMgtVCSigUserN391Admin"),
        ("FRNETSERV-MIB", "frMgtVCSigUserN392Admin"),
        ("FRNETSERV-MIB", "frMgtVCSigUserN393Admin"),
        ("FRNETSERV-MIB", "frMgtVCSigUserT391Admin"),
        ("FRNETSERV-MIB", "frMgtVCSigNetN392Admin"),
        ("FRNETSERV-MIB", "frMgtVCSigNetN393Admin"),
        ("FRNETSERV-MIB", "frMgtVCSigNetT392Admin"),
        ("FRNETSERV-MIB", "frMgtVCSigNetnT3Admin"))
)
if mibBuilder.loadTexts:
    frnetservMgtVCSigAdminGroup.setStatus("current")


# Notification objects

frPVCConnectStatusNotif = NotificationType(
    (1, 3, 6, 1, 2, 1, 10, 44, 2, 0, 2)
)
frPVCConnectStatusNotif.setObjects(
      *(("FRNETSERV-MIB", "frPVCConnectL2hOperStatus"),
        ("FRNETSERV-MIB", "frPVCConnectH2lOperStatus"),
        ("FRNETSERV-MIB", "frPVCEndptRcvdSigStatus"))
)
if mibBuilder.loadTexts:
    frPVCConnectStatusNotif.setStatus(
        "current"
    )

frPVCConnectStatusChange = NotificationType(
    (1, 3, 6, 1, 2, 1, 10, 44, 2, 1)
)
frPVCConnectStatusChange.setObjects(
      *(("FRNETSERV-MIB", "frPVCConnectIndex"),
        ("FRNETSERV-MIB", "frPVCConnectLowIfIndex"),
        ("FRNETSERV-MIB", "frPVCConnectLowDLCIIndex"),
        ("FRNETSERV-MIB", "frPVCConnectHighIfIndex"),
        ("FRNETSERV-MIB", "frPVCConnectHighDLCIIndex"),
        ("FRNETSERV-MIB", "frPVCConnectL2hOperStatus"),
        ("FRNETSERV-MIB", "frPVCConnectH2lOperStatus"),
        ("FRNETSERV-MIB", "frPVCEndptRcvdSigStatus"))
)
if mibBuilder.loadTexts:
    frPVCConnectStatusChange.setStatus(
        "deprecated"
    )


# Notifications groups

frnetservPVCNotifGroup = NotificationGroup(
    (1, 3, 6, 1, 2, 1, 10, 44, 3, 1, 12)
)
frnetservPVCNotifGroup.setObjects(
    ("FRNETSERV-MIB", "frPVCConnectStatusChange")
)
if mibBuilder.loadTexts:
    frnetservPVCNotifGroup.setStatus(
        "deprecated"
    )

frnetservPVCNotifGroup2 = NotificationGroup(
    (1, 3, 6, 1, 2, 1, 10, 44, 3, 1, 13)
)
frnetservPVCNotifGroup2.setObjects(
    ("FRNETSERV-MIB", "frPVCConnectStatusNotif")
)
if mibBuilder.loadTexts:
    frnetservPVCNotifGroup2.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

frnetservCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 10, 44, 3, 2, 1)
)
if mibBuilder.loadTexts:
    frnetservCompliance.setStatus(
        "deprecated"
    )

frnetservCompliance2 = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 10, 44, 3, 2, 2)
)
if mibBuilder.loadTexts:
    frnetservCompliance2.setStatus(
        "current"
    )

frnetSwitchCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 10, 44, 3, 2, 3)
)
if mibBuilder.loadTexts:
    frnetSwitchCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "FRNETSERV-MIB",
    **{"frnetservMIB": frnetservMIB,
       "frnetservObjects": frnetservObjects,
       "frLportTable": frLportTable,
       "frLportEntry": frLportEntry,
       "frLportNumPlan": frLportNumPlan,
       "frLportContact": frLportContact,
       "frLportLocation": frLportLocation,
       "frLportType": frLportType,
       "frLportAddrDLCILen": frLportAddrDLCILen,
       "frLportVCSigProtocol": frLportVCSigProtocol,
       "frLportVCSigPointer": frLportVCSigPointer,
       "frLportDLCIIndexValue": frLportDLCIIndexValue,
       "frLportTypeAdmin": frLportTypeAdmin,
       "frLportVCSigProtocolAdmin": frLportVCSigProtocolAdmin,
       "frLportFragControl": frLportFragControl,
       "frLportFragSize": frLportFragSize,
       "frMgtVCSigTable": frMgtVCSigTable,
       "frMgtVCSigEntry": frMgtVCSigEntry,
       "frMgtVCSigProced": frMgtVCSigProced,
       "frMgtVCSigUserN391": frMgtVCSigUserN391,
       "frMgtVCSigUserN392": frMgtVCSigUserN392,
       "frMgtVCSigUserN393": frMgtVCSigUserN393,
       "frMgtVCSigUserT391": frMgtVCSigUserT391,
       "frMgtVCSigNetN392": frMgtVCSigNetN392,
       "frMgtVCSigNetN393": frMgtVCSigNetN393,
       "frMgtVCSigNetT392": frMgtVCSigNetT392,
       "frMgtVCSigNetnN4": frMgtVCSigNetnN4,
       "frMgtVCSigNetnT3": frMgtVCSigNetnT3,
       "frMgtVCSigUserLinkRelErrors": frMgtVCSigUserLinkRelErrors,
       "frMgtVCSigUserProtErrors": frMgtVCSigUserProtErrors,
       "frMgtVCSigUserChanInactive": frMgtVCSigUserChanInactive,
       "frMgtVCSigNetLinkRelErrors": frMgtVCSigNetLinkRelErrors,
       "frMgtVCSigNetProtErrors": frMgtVCSigNetProtErrors,
       "frMgtVCSigNetChanInactive": frMgtVCSigNetChanInactive,
       "frMgtVCSigProcedAdmin": frMgtVCSigProcedAdmin,
       "frMgtVCSigUserN391Admin": frMgtVCSigUserN391Admin,
       "frMgtVCSigUserN392Admin": frMgtVCSigUserN392Admin,
       "frMgtVCSigUserN393Admin": frMgtVCSigUserN393Admin,
       "frMgtVCSigUserT391Admin": frMgtVCSigUserT391Admin,
       "frMgtVCSigNetN392Admin": frMgtVCSigNetN392Admin,
       "frMgtVCSigNetN393Admin": frMgtVCSigNetN393Admin,
       "frMgtVCSigNetT392Admin": frMgtVCSigNetT392Admin,
       "frMgtVCSigNetnT3Admin": frMgtVCSigNetnT3Admin,
       "frPVCEndptTable": frPVCEndptTable,
       "frPVCEndptEntry": frPVCEndptEntry,
       "frPVCEndptDLCIIndex": frPVCEndptDLCIIndex,
       "frPVCEndptInMaxFrameSize": frPVCEndptInMaxFrameSize,
       "frPVCEndptInBc": frPVCEndptInBc,
       "frPVCEndptInBe": frPVCEndptInBe,
       "frPVCEndptInCIR": frPVCEndptInCIR,
       "frPVCEndptOutMaxFrameSize": frPVCEndptOutMaxFrameSize,
       "frPVCEndptOutBc": frPVCEndptOutBc,
       "frPVCEndptOutBe": frPVCEndptOutBe,
       "frPVCEndptOutCIR": frPVCEndptOutCIR,
       "frPVCEndptConnectIdentifier": frPVCEndptConnectIdentifier,
       "frPVCEndptRowStatus": frPVCEndptRowStatus,
       "frPVCEndptRcvdSigStatus": frPVCEndptRcvdSigStatus,
       "frPVCEndptInFrames": frPVCEndptInFrames,
       "frPVCEndptOutFrames": frPVCEndptOutFrames,
       "frPVCEndptInDEFrames": frPVCEndptInDEFrames,
       "frPVCEndptInExcessFrames": frPVCEndptInExcessFrames,
       "frPVCEndptOutExcessFrames": frPVCEndptOutExcessFrames,
       "frPVCEndptInDiscards": frPVCEndptInDiscards,
       "frPVCEndptInOctets": frPVCEndptInOctets,
       "frPVCEndptOutOctets": frPVCEndptOutOctets,
       "frPVCEndptInDiscardsDESet": frPVCEndptInDiscardsDESet,
       "frPVCEndptInFramesFECNSet": frPVCEndptInFramesFECNSet,
       "frPVCEndptOutFramesFECNSet": frPVCEndptOutFramesFECNSet,
       "frPVCEndptInFramesBECNSet": frPVCEndptInFramesBECNSet,
       "frPVCEndptOutFramesBECNSet": frPVCEndptOutFramesBECNSet,
       "frPVCEndptInCongDiscards": frPVCEndptInCongDiscards,
       "frPVCEndptInDECongDiscards": frPVCEndptInDECongDiscards,
       "frPVCEndptOutCongDiscards": frPVCEndptOutCongDiscards,
       "frPVCEndptOutDECongDiscards": frPVCEndptOutDECongDiscards,
       "frPVCEndptOutDEFrames": frPVCEndptOutDEFrames,
       "frPVCEndptAtmIwfConnIndex": frPVCEndptAtmIwfConnIndex,
       "frPVCConnectIndexValue": frPVCConnectIndexValue,
       "frPVCConnectTable": frPVCConnectTable,
       "frPVCConnectEntry": frPVCConnectEntry,
       "frPVCConnectIndex": frPVCConnectIndex,
       "frPVCConnectLowIfIndex": frPVCConnectLowIfIndex,
       "frPVCConnectLowDLCIIndex": frPVCConnectLowDLCIIndex,
       "frPVCConnectHighIfIndex": frPVCConnectHighIfIndex,
       "frPVCConnectHighDLCIIndex": frPVCConnectHighDLCIIndex,
       "frPVCConnectAdminStatus": frPVCConnectAdminStatus,
       "frPVCConnectL2hOperStatus": frPVCConnectL2hOperStatus,
       "frPVCConnectH2lOperStatus": frPVCConnectH2lOperStatus,
       "frPVCConnectL2hLastChange": frPVCConnectL2hLastChange,
       "frPVCConnectH2lLastChange": frPVCConnectH2lLastChange,
       "frPVCConnectRowStatus": frPVCConnectRowStatus,
       "frPVCConnectUserName": frPVCConnectUserName,
       "frPVCConnectProviderName": frPVCConnectProviderName,
       "frAccountPVCTable": frAccountPVCTable,
       "frAccountPVCEntry": frAccountPVCEntry,
       "frAccountPVCDLCIIndex": frAccountPVCDLCIIndex,
       "frAccountPVCSegmentSize": frAccountPVCSegmentSize,
       "frAccountPVCInSegments": frAccountPVCInSegments,
       "frAccountPVCOutSegments": frAccountPVCOutSegments,
       "frAccountLportTable": frAccountLportTable,
       "frAccountLportEntry": frAccountLportEntry,
       "frAccountLportSegmentSize": frAccountLportSegmentSize,
       "frAccountLportInSegments": frAccountLportInSegments,
       "frAccountLportOutSegments": frAccountLportOutSegments,
       "frnetservTraps": frnetservTraps,
       "frnetservTrapsPrefix": frnetservTrapsPrefix,
       "frPVCConnectStatusNotif": frPVCConnectStatusNotif,
       "frPVCConnectStatusChange": frPVCConnectStatusChange,
       "frnetservConformance": frnetservConformance,
       "frnetservGroups": frnetservGroups,
       "frnetservLportGroup": frnetservLportGroup,
       "frnetservMgtVCSigGroup": frnetservMgtVCSigGroup,
       "frnetservPVCEndptGroup": frnetservPVCEndptGroup,
       "frnetservPVCConnectGroup": frnetservPVCConnectGroup,
       "frnetservAccountPVCGroup": frnetservAccountPVCGroup,
       "frnetservAccountLportGroup": frnetservAccountLportGroup,
       "frnetservLportGroup2": frnetservLportGroup2,
       "frnetservPVCEndptGroup2": frnetservPVCEndptGroup2,
       "frnetservPVCConnectNamesGroup": frnetservPVCConnectNamesGroup,
       "frnetservLportAdminGroup": frnetservLportAdminGroup,
       "frnetservMgtVCSigAdminGroup": frnetservMgtVCSigAdminGroup,
       "frnetservPVCNotifGroup": frnetservPVCNotifGroup,
       "frnetservPVCNotifGroup2": frnetservPVCNotifGroup2,
       "frnetservCompliances": frnetservCompliances,
       "frnetservCompliance": frnetservCompliance,
       "frnetservCompliance2": frnetservCompliance2,
       "frnetSwitchCompliance": frnetSwitchCompliance}
)
