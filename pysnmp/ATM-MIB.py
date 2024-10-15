# SNMP MIB module (ATM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ATM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:33:29 2024
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

atmMIB = ModuleIdentity(
    (1, 3, 6, 1, 2, 1, 37)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class IfIndex(Integer32, TextualConvention):
    status = "current"


class AtmTrafficDescrParamIndex(Integer32, TextualConvention):
    status = "current"


# MIB Managed Objects in the order of their OIDs

_AtmMIBObjects_ObjectIdentity = ObjectIdentity
atmMIBObjects = _AtmMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 37, 1)
)
_AtmTrafficDescriptorTypes_ObjectIdentity = ObjectIdentity
atmTrafficDescriptorTypes = _AtmTrafficDescriptorTypes_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 37, 1, 1)
)
_AtmNoTrafficDescriptor_ObjectIdentity = ObjectIdentity
atmNoTrafficDescriptor = _AtmNoTrafficDescriptor_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 37, 1, 1, 1)
)
if mibBuilder.loadTexts:
    atmNoTrafficDescriptor.setStatus("current")
_AtmNoClpNoScr_ObjectIdentity = ObjectIdentity
atmNoClpNoScr = _AtmNoClpNoScr_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 37, 1, 1, 2)
)
if mibBuilder.loadTexts:
    atmNoClpNoScr.setStatus("current")
_AtmClpNoTaggingNoScr_ObjectIdentity = ObjectIdentity
atmClpNoTaggingNoScr = _AtmClpNoTaggingNoScr_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 37, 1, 1, 3)
)
if mibBuilder.loadTexts:
    atmClpNoTaggingNoScr.setStatus("current")
_AtmClpTaggingNoScr_ObjectIdentity = ObjectIdentity
atmClpTaggingNoScr = _AtmClpTaggingNoScr_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 37, 1, 1, 4)
)
if mibBuilder.loadTexts:
    atmClpTaggingNoScr.setStatus("current")
_AtmNoClpScr_ObjectIdentity = ObjectIdentity
atmNoClpScr = _AtmNoClpScr_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 37, 1, 1, 5)
)
if mibBuilder.loadTexts:
    atmNoClpScr.setStatus("current")
_AtmClpNoTaggingScr_ObjectIdentity = ObjectIdentity
atmClpNoTaggingScr = _AtmClpNoTaggingScr_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 37, 1, 1, 6)
)
if mibBuilder.loadTexts:
    atmClpNoTaggingScr.setStatus("current")
_AtmClpTaggingScr_ObjectIdentity = ObjectIdentity
atmClpTaggingScr = _AtmClpTaggingScr_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 37, 1, 1, 7)
)
if mibBuilder.loadTexts:
    atmClpTaggingScr.setStatus("current")
_AtmInterfaceConfTable_Object = MibTable
atmInterfaceConfTable = _AtmInterfaceConfTable_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 2)
)
if mibBuilder.loadTexts:
    atmInterfaceConfTable.setStatus("current")
_AtmInterfaceConfEntry_Object = MibTableRow
atmInterfaceConfEntry = _AtmInterfaceConfEntry_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 2, 1)
)
atmInterfaceConfEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    atmInterfaceConfEntry.setStatus("current")


class _AtmInterfaceMaxVpcs_Type(Integer32):
    """Custom type atmInterfaceMaxVpcs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4096),
    )


_AtmInterfaceMaxVpcs_Type.__name__ = "Integer32"
_AtmInterfaceMaxVpcs_Object = MibTableColumn
atmInterfaceMaxVpcs = _AtmInterfaceMaxVpcs_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 2, 1, 1),
    _AtmInterfaceMaxVpcs_Type()
)
atmInterfaceMaxVpcs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmInterfaceMaxVpcs.setStatus("current")


class _AtmInterfaceMaxVccs_Type(Integer32):
    """Custom type atmInterfaceMaxVccs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_AtmInterfaceMaxVccs_Type.__name__ = "Integer32"
_AtmInterfaceMaxVccs_Object = MibTableColumn
atmInterfaceMaxVccs = _AtmInterfaceMaxVccs_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 2, 1, 2),
    _AtmInterfaceMaxVccs_Type()
)
atmInterfaceMaxVccs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmInterfaceMaxVccs.setStatus("current")


class _AtmInterfaceConfVpcs_Type(Integer32):
    """Custom type atmInterfaceConfVpcs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4096),
    )


_AtmInterfaceConfVpcs_Type.__name__ = "Integer32"
_AtmInterfaceConfVpcs_Object = MibTableColumn
atmInterfaceConfVpcs = _AtmInterfaceConfVpcs_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 2, 1, 3),
    _AtmInterfaceConfVpcs_Type()
)
atmInterfaceConfVpcs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmInterfaceConfVpcs.setStatus("current")


class _AtmInterfaceConfVccs_Type(Integer32):
    """Custom type atmInterfaceConfVccs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_AtmInterfaceConfVccs_Type.__name__ = "Integer32"
_AtmInterfaceConfVccs_Object = MibTableColumn
atmInterfaceConfVccs = _AtmInterfaceConfVccs_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 2, 1, 4),
    _AtmInterfaceConfVccs_Type()
)
atmInterfaceConfVccs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmInterfaceConfVccs.setStatus("current")


class _AtmInterfaceMaxActiveVpiBits_Type(Integer32):
    """Custom type atmInterfaceMaxActiveVpiBits based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 12),
    )


_AtmInterfaceMaxActiveVpiBits_Type.__name__ = "Integer32"
_AtmInterfaceMaxActiveVpiBits_Object = MibTableColumn
atmInterfaceMaxActiveVpiBits = _AtmInterfaceMaxActiveVpiBits_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 2, 1, 5),
    _AtmInterfaceMaxActiveVpiBits_Type()
)
atmInterfaceMaxActiveVpiBits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmInterfaceMaxActiveVpiBits.setStatus("current")


class _AtmInterfaceMaxActiveVciBits_Type(Integer32):
    """Custom type atmInterfaceMaxActiveVciBits based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_AtmInterfaceMaxActiveVciBits_Type.__name__ = "Integer32"
_AtmInterfaceMaxActiveVciBits_Object = MibTableColumn
atmInterfaceMaxActiveVciBits = _AtmInterfaceMaxActiveVciBits_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 2, 1, 6),
    _AtmInterfaceMaxActiveVciBits_Type()
)
atmInterfaceMaxActiveVciBits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmInterfaceMaxActiveVciBits.setStatus("current")


class _AtmInterfaceIlmiVpi_Type(Integer32):
    """Custom type atmInterfaceIlmiVpi based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AtmInterfaceIlmiVpi_Type.__name__ = "Integer32"
_AtmInterfaceIlmiVpi_Object = MibTableColumn
atmInterfaceIlmiVpi = _AtmInterfaceIlmiVpi_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 2, 1, 7),
    _AtmInterfaceIlmiVpi_Type()
)
atmInterfaceIlmiVpi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmInterfaceIlmiVpi.setStatus("current")


class _AtmInterfaceIlmiVci_Type(Integer32):
    """Custom type atmInterfaceIlmiVci based on Integer32"""
    defaultValue = 16

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AtmInterfaceIlmiVci_Type.__name__ = "Integer32"
_AtmInterfaceIlmiVci_Object = MibTableColumn
atmInterfaceIlmiVci = _AtmInterfaceIlmiVci_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 2, 1, 8),
    _AtmInterfaceIlmiVci_Type()
)
atmInterfaceIlmiVci.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmInterfaceIlmiVci.setStatus("current")


class _AtmInterfaceAddressType_Type(Integer32):
    """Custom type atmInterfaceAddressType based on Integer32"""
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
        *(("nativeE164", 3),
          ("nsapE164", 2),
          ("other", 4),
          ("private", 1))
    )


_AtmInterfaceAddressType_Type.__name__ = "Integer32"
_AtmInterfaceAddressType_Object = MibTableColumn
atmInterfaceAddressType = _AtmInterfaceAddressType_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 2, 1, 9),
    _AtmInterfaceAddressType_Type()
)
atmInterfaceAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmInterfaceAddressType.setStatus("current")


class _AtmInterfaceAdminAddress_Type(OctetString):
    """Custom type atmInterfaceAdminAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AtmInterfaceAdminAddress_Type.__name__ = "OctetString"
_AtmInterfaceAdminAddress_Object = MibTableColumn
atmInterfaceAdminAddress = _AtmInterfaceAdminAddress_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 2, 1, 10),
    _AtmInterfaceAdminAddress_Type()
)
atmInterfaceAdminAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmInterfaceAdminAddress.setStatus("current")
_AtmInterfaceMyNeighborIpAddress_Type = IpAddress
_AtmInterfaceMyNeighborIpAddress_Object = MibTableColumn
atmInterfaceMyNeighborIpAddress = _AtmInterfaceMyNeighborIpAddress_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 2, 1, 11),
    _AtmInterfaceMyNeighborIpAddress_Type()
)
atmInterfaceMyNeighborIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmInterfaceMyNeighborIpAddress.setStatus("current")
_AtmInterfaceMyNeighborIfName_Type = DisplayString
_AtmInterfaceMyNeighborIfName_Object = MibTableColumn
atmInterfaceMyNeighborIfName = _AtmInterfaceMyNeighborIfName_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 2, 1, 12),
    _AtmInterfaceMyNeighborIfName_Type()
)
atmInterfaceMyNeighborIfName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmInterfaceMyNeighborIfName.setStatus("current")
_AtmInterfaceDs3PlcpTable_Object = MibTable
atmInterfaceDs3PlcpTable = _AtmInterfaceDs3PlcpTable_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 3)
)
if mibBuilder.loadTexts:
    atmInterfaceDs3PlcpTable.setStatus("current")
_AtmInterfaceDs3PlcpEntry_Object = MibTableRow
atmInterfaceDs3PlcpEntry = _AtmInterfaceDs3PlcpEntry_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 3, 1)
)
atmInterfaceDs3PlcpEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    atmInterfaceDs3PlcpEntry.setStatus("current")
_AtmInterfaceDs3PlcpSEFSs_Type = Counter32
_AtmInterfaceDs3PlcpSEFSs_Object = MibTableColumn
atmInterfaceDs3PlcpSEFSs = _AtmInterfaceDs3PlcpSEFSs_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 3, 1, 1),
    _AtmInterfaceDs3PlcpSEFSs_Type()
)
atmInterfaceDs3PlcpSEFSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmInterfaceDs3PlcpSEFSs.setStatus("current")


class _AtmInterfaceDs3PlcpAlarmState_Type(Integer32):
    """Custom type atmInterfaceDs3PlcpAlarmState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("incomingLOF", 3),
          ("noAlarm", 1),
          ("receivedFarEndAlarm", 2))
    )


_AtmInterfaceDs3PlcpAlarmState_Type.__name__ = "Integer32"
_AtmInterfaceDs3PlcpAlarmState_Object = MibTableColumn
atmInterfaceDs3PlcpAlarmState = _AtmInterfaceDs3PlcpAlarmState_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 3, 1, 2),
    _AtmInterfaceDs3PlcpAlarmState_Type()
)
atmInterfaceDs3PlcpAlarmState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmInterfaceDs3PlcpAlarmState.setStatus("current")
_AtmInterfaceDs3PlcpUASs_Type = Counter32
_AtmInterfaceDs3PlcpUASs_Object = MibTableColumn
atmInterfaceDs3PlcpUASs = _AtmInterfaceDs3PlcpUASs_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 3, 1, 3),
    _AtmInterfaceDs3PlcpUASs_Type()
)
atmInterfaceDs3PlcpUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmInterfaceDs3PlcpUASs.setStatus("current")
_AtmInterfaceTCTable_Object = MibTable
atmInterfaceTCTable = _AtmInterfaceTCTable_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 4)
)
if mibBuilder.loadTexts:
    atmInterfaceTCTable.setStatus("current")
_AtmInterfaceTCEntry_Object = MibTableRow
atmInterfaceTCEntry = _AtmInterfaceTCEntry_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 4, 1)
)
atmInterfaceTCEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    atmInterfaceTCEntry.setStatus("current")
_AtmInterfaceOCDEvents_Type = Counter32
_AtmInterfaceOCDEvents_Object = MibTableColumn
atmInterfaceOCDEvents = _AtmInterfaceOCDEvents_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 4, 1, 1),
    _AtmInterfaceOCDEvents_Type()
)
atmInterfaceOCDEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmInterfaceOCDEvents.setStatus("current")


class _AtmInterfaceTCAlarmState_Type(Integer32):
    """Custom type atmInterfaceTCAlarmState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("lcdFailure", 2),
          ("noAlarm", 1))
    )


_AtmInterfaceTCAlarmState_Type.__name__ = "Integer32"
_AtmInterfaceTCAlarmState_Object = MibTableColumn
atmInterfaceTCAlarmState = _AtmInterfaceTCAlarmState_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 4, 1, 2),
    _AtmInterfaceTCAlarmState_Type()
)
atmInterfaceTCAlarmState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmInterfaceTCAlarmState.setStatus("current")
_AtmTrafficDescrParamTable_Object = MibTable
atmTrafficDescrParamTable = _AtmTrafficDescrParamTable_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 5)
)
if mibBuilder.loadTexts:
    atmTrafficDescrParamTable.setStatus("current")
_AtmTrafficDescrParamEntry_Object = MibTableRow
atmTrafficDescrParamEntry = _AtmTrafficDescrParamEntry_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 5, 1)
)
atmTrafficDescrParamEntry.setIndexNames(
    (0, "ATM-MIB", "atmTrafficDescrParamIndex"),
)
if mibBuilder.loadTexts:
    atmTrafficDescrParamEntry.setStatus("current")
_AtmTrafficDescrParamIndex_Type = AtmTrafficDescrParamIndex
_AtmTrafficDescrParamIndex_Object = MibTableColumn
atmTrafficDescrParamIndex = _AtmTrafficDescrParamIndex_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 5, 1, 1),
    _AtmTrafficDescrParamIndex_Type()
)
atmTrafficDescrParamIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    atmTrafficDescrParamIndex.setStatus("current")


class _AtmTrafficDescrType_Type(ObjectIdentifier):
    """Custom type atmTrafficDescrType based on ObjectIdentifier"""
    defaultValue = (1, 3, 6, 1, 2, 1, 37, 1, 1, 1)


_AtmTrafficDescrType_Object = MibTableColumn
atmTrafficDescrType = _AtmTrafficDescrType_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 5, 1, 2),
    _AtmTrafficDescrType_Type()
)
atmTrafficDescrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmTrafficDescrType.setStatus("current")


class _AtmTrafficDescrParam1_Type(Integer32):
    """Custom type atmTrafficDescrParam1 based on Integer32"""
    defaultValue = 0


_AtmTrafficDescrParam1_Object = MibTableColumn
atmTrafficDescrParam1 = _AtmTrafficDescrParam1_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 5, 1, 3),
    _AtmTrafficDescrParam1_Type()
)
atmTrafficDescrParam1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmTrafficDescrParam1.setStatus("current")


class _AtmTrafficDescrParam2_Type(Integer32):
    """Custom type atmTrafficDescrParam2 based on Integer32"""
    defaultValue = 0


_AtmTrafficDescrParam2_Object = MibTableColumn
atmTrafficDescrParam2 = _AtmTrafficDescrParam2_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 5, 1, 4),
    _AtmTrafficDescrParam2_Type()
)
atmTrafficDescrParam2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmTrafficDescrParam2.setStatus("current")


class _AtmTrafficDescrParam3_Type(Integer32):
    """Custom type atmTrafficDescrParam3 based on Integer32"""
    defaultValue = 0


_AtmTrafficDescrParam3_Object = MibTableColumn
atmTrafficDescrParam3 = _AtmTrafficDescrParam3_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 5, 1, 5),
    _AtmTrafficDescrParam3_Type()
)
atmTrafficDescrParam3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmTrafficDescrParam3.setStatus("current")


class _AtmTrafficDescrParam4_Type(Integer32):
    """Custom type atmTrafficDescrParam4 based on Integer32"""
    defaultValue = 0


_AtmTrafficDescrParam4_Object = MibTableColumn
atmTrafficDescrParam4 = _AtmTrafficDescrParam4_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 5, 1, 6),
    _AtmTrafficDescrParam4_Type()
)
atmTrafficDescrParam4.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmTrafficDescrParam4.setStatus("current")


class _AtmTrafficDescrParam5_Type(Integer32):
    """Custom type atmTrafficDescrParam5 based on Integer32"""
    defaultValue = 0


_AtmTrafficDescrParam5_Object = MibTableColumn
atmTrafficDescrParam5 = _AtmTrafficDescrParam5_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 5, 1, 7),
    _AtmTrafficDescrParam5_Type()
)
atmTrafficDescrParam5.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmTrafficDescrParam5.setStatus("current")


class _AtmTrafficQoSClass_Type(Integer32):
    """Custom type atmTrafficQoSClass based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AtmTrafficQoSClass_Type.__name__ = "Integer32"
_AtmTrafficQoSClass_Object = MibTableColumn
atmTrafficQoSClass = _AtmTrafficQoSClass_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 5, 1, 8),
    _AtmTrafficQoSClass_Type()
)
atmTrafficQoSClass.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmTrafficQoSClass.setStatus("current")


class _AtmTrafficDescrRowStatus_Type(RowStatus):
    """Custom type atmTrafficDescrRowStatus based on RowStatus"""


_AtmTrafficDescrRowStatus_Object = MibTableColumn
atmTrafficDescrRowStatus = _AtmTrafficDescrRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 5, 1, 9),
    _AtmTrafficDescrRowStatus_Type()
)
atmTrafficDescrRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmTrafficDescrRowStatus.setStatus("current")
_AtmVplTable_Object = MibTable
atmVplTable = _AtmVplTable_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 6)
)
if mibBuilder.loadTexts:
    atmVplTable.setStatus("current")
_AtmVplEntry_Object = MibTableRow
atmVplEntry = _AtmVplEntry_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 6, 1)
)
atmVplEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ATM-MIB", "atmVplVpi"),
)
if mibBuilder.loadTexts:
    atmVplEntry.setStatus("current")


class _AtmVplVpi_Type(Integer32):
    """Custom type atmVplVpi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_AtmVplVpi_Type.__name__ = "Integer32"
_AtmVplVpi_Object = MibTableColumn
atmVplVpi = _AtmVplVpi_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 6, 1, 1),
    _AtmVplVpi_Type()
)
atmVplVpi.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    atmVplVpi.setStatus("current")


class _AtmVplAdminStatus_Type(Integer32):
    """Custom type atmVplAdminStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_AtmVplAdminStatus_Type.__name__ = "Integer32"
_AtmVplAdminStatus_Object = MibTableColumn
atmVplAdminStatus = _AtmVplAdminStatus_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 6, 1, 2),
    _AtmVplAdminStatus_Type()
)
atmVplAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmVplAdminStatus.setStatus("current")


class _AtmVplOperStatus_Type(Integer32):
    """Custom type atmVplOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("unknown", 3),
          ("up", 1))
    )


_AtmVplOperStatus_Type.__name__ = "Integer32"
_AtmVplOperStatus_Object = MibTableColumn
atmVplOperStatus = _AtmVplOperStatus_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 6, 1, 3),
    _AtmVplOperStatus_Type()
)
atmVplOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmVplOperStatus.setStatus("current")
_AtmVplLastChange_Type = TimeStamp
_AtmVplLastChange_Object = MibTableColumn
atmVplLastChange = _AtmVplLastChange_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 6, 1, 4),
    _AtmVplLastChange_Type()
)
atmVplLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmVplLastChange.setStatus("current")
_AtmVplReceiveTrafficDescrIndex_Type = AtmTrafficDescrParamIndex
_AtmVplReceiveTrafficDescrIndex_Object = MibTableColumn
atmVplReceiveTrafficDescrIndex = _AtmVplReceiveTrafficDescrIndex_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 6, 1, 5),
    _AtmVplReceiveTrafficDescrIndex_Type()
)
atmVplReceiveTrafficDescrIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmVplReceiveTrafficDescrIndex.setStatus("current")
_AtmVplTransmitTrafficDescrIndex_Type = AtmTrafficDescrParamIndex
_AtmVplTransmitTrafficDescrIndex_Object = MibTableColumn
atmVplTransmitTrafficDescrIndex = _AtmVplTransmitTrafficDescrIndex_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 6, 1, 6),
    _AtmVplTransmitTrafficDescrIndex_Type()
)
atmVplTransmitTrafficDescrIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmVplTransmitTrafficDescrIndex.setStatus("current")


class _AtmVplCrossConnectIdentifier_Type(Integer32):
    """Custom type atmVplCrossConnectIdentifier based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AtmVplCrossConnectIdentifier_Type.__name__ = "Integer32"
_AtmVplCrossConnectIdentifier_Object = MibTableColumn
atmVplCrossConnectIdentifier = _AtmVplCrossConnectIdentifier_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 6, 1, 7),
    _AtmVplCrossConnectIdentifier_Type()
)
atmVplCrossConnectIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmVplCrossConnectIdentifier.setStatus("current")


class _AtmVplRowStatus_Type(RowStatus):
    """Custom type atmVplRowStatus based on RowStatus"""


_AtmVplRowStatus_Object = MibTableColumn
atmVplRowStatus = _AtmVplRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 6, 1, 8),
    _AtmVplRowStatus_Type()
)
atmVplRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmVplRowStatus.setStatus("current")
_AtmVclTable_Object = MibTable
atmVclTable = _AtmVclTable_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 7)
)
if mibBuilder.loadTexts:
    atmVclTable.setStatus("current")
_AtmVclEntry_Object = MibTableRow
atmVclEntry = _AtmVclEntry_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 7, 1)
)
atmVclEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ATM-MIB", "atmVclVpi"),
    (0, "ATM-MIB", "atmVclVci"),
)
if mibBuilder.loadTexts:
    atmVclEntry.setStatus("current")


class _AtmVclVpi_Type(Integer32):
    """Custom type atmVclVpi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_AtmVclVpi_Type.__name__ = "Integer32"
_AtmVclVpi_Object = MibTableColumn
atmVclVpi = _AtmVclVpi_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 7, 1, 1),
    _AtmVclVpi_Type()
)
atmVclVpi.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    atmVclVpi.setStatus("current")


class _AtmVclVci_Type(Integer32):
    """Custom type atmVclVci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AtmVclVci_Type.__name__ = "Integer32"
_AtmVclVci_Object = MibTableColumn
atmVclVci = _AtmVclVci_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 7, 1, 2),
    _AtmVclVci_Type()
)
atmVclVci.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    atmVclVci.setStatus("current")


class _AtmVclAdminStatus_Type(Integer32):
    """Custom type atmVclAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_AtmVclAdminStatus_Type.__name__ = "Integer32"
_AtmVclAdminStatus_Object = MibTableColumn
atmVclAdminStatus = _AtmVclAdminStatus_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 7, 1, 3),
    _AtmVclAdminStatus_Type()
)
atmVclAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmVclAdminStatus.setStatus("current")


class _AtmVclOperStatus_Type(Integer32):
    """Custom type atmVclOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("unknown", 3),
          ("up", 1))
    )


_AtmVclOperStatus_Type.__name__ = "Integer32"
_AtmVclOperStatus_Object = MibTableColumn
atmVclOperStatus = _AtmVclOperStatus_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 7, 1, 4),
    _AtmVclOperStatus_Type()
)
atmVclOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmVclOperStatus.setStatus("current")
_AtmVclLastChange_Type = TimeStamp
_AtmVclLastChange_Object = MibTableColumn
atmVclLastChange = _AtmVclLastChange_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 7, 1, 5),
    _AtmVclLastChange_Type()
)
atmVclLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmVclLastChange.setStatus("current")
_AtmVclReceiveTrafficDescrIndex_Type = AtmTrafficDescrParamIndex
_AtmVclReceiveTrafficDescrIndex_Object = MibTableColumn
atmVclReceiveTrafficDescrIndex = _AtmVclReceiveTrafficDescrIndex_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 7, 1, 6),
    _AtmVclReceiveTrafficDescrIndex_Type()
)
atmVclReceiveTrafficDescrIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmVclReceiveTrafficDescrIndex.setStatus("current")
_AtmVclTransmitTrafficDescrIndex_Type = AtmTrafficDescrParamIndex
_AtmVclTransmitTrafficDescrIndex_Object = MibTableColumn
atmVclTransmitTrafficDescrIndex = _AtmVclTransmitTrafficDescrIndex_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 7, 1, 7),
    _AtmVclTransmitTrafficDescrIndex_Type()
)
atmVclTransmitTrafficDescrIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmVclTransmitTrafficDescrIndex.setStatus("current")


class _AtmVccAalType_Type(Integer32):
    """Custom type atmVccAalType based on Integer32"""
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
        *(("aal1", 1),
          ("aal34", 2),
          ("aal5", 3),
          ("other", 4),
          ("unknown", 5))
    )


_AtmVccAalType_Type.__name__ = "Integer32"
_AtmVccAalType_Object = MibTableColumn
atmVccAalType = _AtmVccAalType_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 7, 1, 8),
    _AtmVccAalType_Type()
)
atmVccAalType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmVccAalType.setStatus("current")


class _AtmVccAal5CpcsTransmitSduSize_Type(Integer32):
    """Custom type atmVccAal5CpcsTransmitSduSize based on Integer32"""
    defaultValue = 9188

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_AtmVccAal5CpcsTransmitSduSize_Type.__name__ = "Integer32"
_AtmVccAal5CpcsTransmitSduSize_Object = MibTableColumn
atmVccAal5CpcsTransmitSduSize = _AtmVccAal5CpcsTransmitSduSize_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 7, 1, 9),
    _AtmVccAal5CpcsTransmitSduSize_Type()
)
atmVccAal5CpcsTransmitSduSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmVccAal5CpcsTransmitSduSize.setStatus("current")


class _AtmVccAal5CpcsReceiveSduSize_Type(Integer32):
    """Custom type atmVccAal5CpcsReceiveSduSize based on Integer32"""
    defaultValue = 9188

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_AtmVccAal5CpcsReceiveSduSize_Type.__name__ = "Integer32"
_AtmVccAal5CpcsReceiveSduSize_Object = MibTableColumn
atmVccAal5CpcsReceiveSduSize = _AtmVccAal5CpcsReceiveSduSize_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 7, 1, 10),
    _AtmVccAal5CpcsReceiveSduSize_Type()
)
atmVccAal5CpcsReceiveSduSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmVccAal5CpcsReceiveSduSize.setStatus("current")


class _AtmVccAal5EncapsType_Type(Integer32):
    """Custom type atmVccAal5EncapsType based on Integer32"""
    defaultValue = 7

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
        *(("llcEncapsulation", 7),
          ("multiprotocolFrameRelaySscs", 8),
          ("other", 9),
          ("unknown", 10),
          ("vcMultiplexBridgedProtocol8023", 2),
          ("vcMultiplexBridgedProtocol8025", 3),
          ("vcMultiplexBridgedProtocol8026", 4),
          ("vcMultiplexLANemulation8023", 5),
          ("vcMultiplexLANemulation8025", 6),
          ("vcMultiplexRoutedProtocol", 1))
    )


_AtmVccAal5EncapsType_Type.__name__ = "Integer32"
_AtmVccAal5EncapsType_Object = MibTableColumn
atmVccAal5EncapsType = _AtmVccAal5EncapsType_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 7, 1, 11),
    _AtmVccAal5EncapsType_Type()
)
atmVccAal5EncapsType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmVccAal5EncapsType.setStatus("current")


class _AtmVclCrossConnectIdentifier_Type(Integer32):
    """Custom type atmVclCrossConnectIdentifier based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AtmVclCrossConnectIdentifier_Type.__name__ = "Integer32"
_AtmVclCrossConnectIdentifier_Object = MibTableColumn
atmVclCrossConnectIdentifier = _AtmVclCrossConnectIdentifier_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 7, 1, 12),
    _AtmVclCrossConnectIdentifier_Type()
)
atmVclCrossConnectIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmVclCrossConnectIdentifier.setStatus("current")


class _AtmVclRowStatus_Type(RowStatus):
    """Custom type atmVclRowStatus based on RowStatus"""


_AtmVclRowStatus_Object = MibTableColumn
atmVclRowStatus = _AtmVclRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 7, 1, 13),
    _AtmVclRowStatus_Type()
)
atmVclRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmVclRowStatus.setStatus("current")


class _AtmVpCrossConnectIndexNext_Type(Integer32):
    """Custom type atmVpCrossConnectIndexNext based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AtmVpCrossConnectIndexNext_Type.__name__ = "Integer32"
_AtmVpCrossConnectIndexNext_Object = MibScalar
atmVpCrossConnectIndexNext = _AtmVpCrossConnectIndexNext_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 8),
    _AtmVpCrossConnectIndexNext_Type()
)
atmVpCrossConnectIndexNext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmVpCrossConnectIndexNext.setStatus("current")
_AtmVpCrossConnectTable_Object = MibTable
atmVpCrossConnectTable = _AtmVpCrossConnectTable_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 9)
)
if mibBuilder.loadTexts:
    atmVpCrossConnectTable.setStatus("current")
_AtmVpCrossConnectEntry_Object = MibTableRow
atmVpCrossConnectEntry = _AtmVpCrossConnectEntry_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 9, 1)
)
atmVpCrossConnectEntry.setIndexNames(
    (0, "ATM-MIB", "atmVpCrossConnectIndex"),
    (0, "ATM-MIB", "atmVpCrossConnectLowIfIndex"),
    (0, "ATM-MIB", "atmVpCrossConnectLowVpi"),
    (0, "ATM-MIB", "atmVpCrossConnectHighIfIndex"),
    (0, "ATM-MIB", "atmVpCrossConnectHighVpi"),
)
if mibBuilder.loadTexts:
    atmVpCrossConnectEntry.setStatus("current")


class _AtmVpCrossConnectIndex_Type(Integer32):
    """Custom type atmVpCrossConnectIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_AtmVpCrossConnectIndex_Type.__name__ = "Integer32"
_AtmVpCrossConnectIndex_Object = MibTableColumn
atmVpCrossConnectIndex = _AtmVpCrossConnectIndex_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 9, 1, 1),
    _AtmVpCrossConnectIndex_Type()
)
atmVpCrossConnectIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    atmVpCrossConnectIndex.setStatus("current")
_AtmVpCrossConnectLowIfIndex_Type = IfIndex
_AtmVpCrossConnectLowIfIndex_Object = MibTableColumn
atmVpCrossConnectLowIfIndex = _AtmVpCrossConnectLowIfIndex_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 9, 1, 2),
    _AtmVpCrossConnectLowIfIndex_Type()
)
atmVpCrossConnectLowIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    atmVpCrossConnectLowIfIndex.setStatus("current")


class _AtmVpCrossConnectLowVpi_Type(Integer32):
    """Custom type atmVpCrossConnectLowVpi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_AtmVpCrossConnectLowVpi_Type.__name__ = "Integer32"
_AtmVpCrossConnectLowVpi_Object = MibTableColumn
atmVpCrossConnectLowVpi = _AtmVpCrossConnectLowVpi_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 9, 1, 3),
    _AtmVpCrossConnectLowVpi_Type()
)
atmVpCrossConnectLowVpi.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    atmVpCrossConnectLowVpi.setStatus("current")
_AtmVpCrossConnectHighIfIndex_Type = IfIndex
_AtmVpCrossConnectHighIfIndex_Object = MibTableColumn
atmVpCrossConnectHighIfIndex = _AtmVpCrossConnectHighIfIndex_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 9, 1, 4),
    _AtmVpCrossConnectHighIfIndex_Type()
)
atmVpCrossConnectHighIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    atmVpCrossConnectHighIfIndex.setStatus("current")


class _AtmVpCrossConnectHighVpi_Type(Integer32):
    """Custom type atmVpCrossConnectHighVpi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_AtmVpCrossConnectHighVpi_Type.__name__ = "Integer32"
_AtmVpCrossConnectHighVpi_Object = MibTableColumn
atmVpCrossConnectHighVpi = _AtmVpCrossConnectHighVpi_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 9, 1, 5),
    _AtmVpCrossConnectHighVpi_Type()
)
atmVpCrossConnectHighVpi.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    atmVpCrossConnectHighVpi.setStatus("current")


class _AtmVpCrossConnectAdminStatus_Type(Integer32):
    """Custom type atmVpCrossConnectAdminStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_AtmVpCrossConnectAdminStatus_Type.__name__ = "Integer32"
_AtmVpCrossConnectAdminStatus_Object = MibTableColumn
atmVpCrossConnectAdminStatus = _AtmVpCrossConnectAdminStatus_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 9, 1, 6),
    _AtmVpCrossConnectAdminStatus_Type()
)
atmVpCrossConnectAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmVpCrossConnectAdminStatus.setStatus("current")


class _AtmVpCrossConnectL2HOperStatus_Type(Integer32):
    """Custom type atmVpCrossConnectL2HOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("unknown", 3),
          ("up", 1))
    )


_AtmVpCrossConnectL2HOperStatus_Type.__name__ = "Integer32"
_AtmVpCrossConnectL2HOperStatus_Object = MibTableColumn
atmVpCrossConnectL2HOperStatus = _AtmVpCrossConnectL2HOperStatus_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 9, 1, 7),
    _AtmVpCrossConnectL2HOperStatus_Type()
)
atmVpCrossConnectL2HOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmVpCrossConnectL2HOperStatus.setStatus("current")


class _AtmVpCrossConnectH2LOperStatus_Type(Integer32):
    """Custom type atmVpCrossConnectH2LOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("unknown", 3),
          ("up", 1))
    )


_AtmVpCrossConnectH2LOperStatus_Type.__name__ = "Integer32"
_AtmVpCrossConnectH2LOperStatus_Object = MibTableColumn
atmVpCrossConnectH2LOperStatus = _AtmVpCrossConnectH2LOperStatus_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 9, 1, 8),
    _AtmVpCrossConnectH2LOperStatus_Type()
)
atmVpCrossConnectH2LOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmVpCrossConnectH2LOperStatus.setStatus("current")
_AtmVpCrossConnectL2HLastChange_Type = TimeStamp
_AtmVpCrossConnectL2HLastChange_Object = MibTableColumn
atmVpCrossConnectL2HLastChange = _AtmVpCrossConnectL2HLastChange_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 9, 1, 9),
    _AtmVpCrossConnectL2HLastChange_Type()
)
atmVpCrossConnectL2HLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmVpCrossConnectL2HLastChange.setStatus("current")
_AtmVpCrossConnectH2LLastChange_Type = TimeStamp
_AtmVpCrossConnectH2LLastChange_Object = MibTableColumn
atmVpCrossConnectH2LLastChange = _AtmVpCrossConnectH2LLastChange_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 9, 1, 10),
    _AtmVpCrossConnectH2LLastChange_Type()
)
atmVpCrossConnectH2LLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmVpCrossConnectH2LLastChange.setStatus("current")


class _AtmVpCrossConnectRowStatus_Type(RowStatus):
    """Custom type atmVpCrossConnectRowStatus based on RowStatus"""


_AtmVpCrossConnectRowStatus_Object = MibTableColumn
atmVpCrossConnectRowStatus = _AtmVpCrossConnectRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 9, 1, 11),
    _AtmVpCrossConnectRowStatus_Type()
)
atmVpCrossConnectRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmVpCrossConnectRowStatus.setStatus("current")


class _AtmVcCrossConnectIndexNext_Type(Integer32):
    """Custom type atmVcCrossConnectIndexNext based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AtmVcCrossConnectIndexNext_Type.__name__ = "Integer32"
_AtmVcCrossConnectIndexNext_Object = MibScalar
atmVcCrossConnectIndexNext = _AtmVcCrossConnectIndexNext_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 10),
    _AtmVcCrossConnectIndexNext_Type()
)
atmVcCrossConnectIndexNext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmVcCrossConnectIndexNext.setStatus("current")
_AtmVcCrossConnectTable_Object = MibTable
atmVcCrossConnectTable = _AtmVcCrossConnectTable_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 11)
)
if mibBuilder.loadTexts:
    atmVcCrossConnectTable.setStatus("current")
_AtmVcCrossConnectEntry_Object = MibTableRow
atmVcCrossConnectEntry = _AtmVcCrossConnectEntry_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 11, 1)
)
atmVcCrossConnectEntry.setIndexNames(
    (0, "ATM-MIB", "atmVcCrossConnectIndex"),
    (0, "ATM-MIB", "atmVcCrossConnectLowIfIndex"),
    (0, "ATM-MIB", "atmVcCrossConnectLowVpi"),
    (0, "ATM-MIB", "atmVcCrossConnectLowVci"),
    (0, "ATM-MIB", "atmVcCrossConnectHighIfIndex"),
    (0, "ATM-MIB", "atmVcCrossConnectHighVpi"),
    (0, "ATM-MIB", "atmVcCrossConnectHighVci"),
)
if mibBuilder.loadTexts:
    atmVcCrossConnectEntry.setStatus("current")


class _AtmVcCrossConnectIndex_Type(Integer32):
    """Custom type atmVcCrossConnectIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_AtmVcCrossConnectIndex_Type.__name__ = "Integer32"
_AtmVcCrossConnectIndex_Object = MibTableColumn
atmVcCrossConnectIndex = _AtmVcCrossConnectIndex_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 11, 1, 1),
    _AtmVcCrossConnectIndex_Type()
)
atmVcCrossConnectIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    atmVcCrossConnectIndex.setStatus("current")
_AtmVcCrossConnectLowIfIndex_Type = IfIndex
_AtmVcCrossConnectLowIfIndex_Object = MibTableColumn
atmVcCrossConnectLowIfIndex = _AtmVcCrossConnectLowIfIndex_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 11, 1, 2),
    _AtmVcCrossConnectLowIfIndex_Type()
)
atmVcCrossConnectLowIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    atmVcCrossConnectLowIfIndex.setStatus("current")


class _AtmVcCrossConnectLowVpi_Type(Integer32):
    """Custom type atmVcCrossConnectLowVpi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_AtmVcCrossConnectLowVpi_Type.__name__ = "Integer32"
_AtmVcCrossConnectLowVpi_Object = MibTableColumn
atmVcCrossConnectLowVpi = _AtmVcCrossConnectLowVpi_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 11, 1, 3),
    _AtmVcCrossConnectLowVpi_Type()
)
atmVcCrossConnectLowVpi.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    atmVcCrossConnectLowVpi.setStatus("current")


class _AtmVcCrossConnectLowVci_Type(Integer32):
    """Custom type atmVcCrossConnectLowVci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AtmVcCrossConnectLowVci_Type.__name__ = "Integer32"
_AtmVcCrossConnectLowVci_Object = MibTableColumn
atmVcCrossConnectLowVci = _AtmVcCrossConnectLowVci_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 11, 1, 4),
    _AtmVcCrossConnectLowVci_Type()
)
atmVcCrossConnectLowVci.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    atmVcCrossConnectLowVci.setStatus("current")
_AtmVcCrossConnectHighIfIndex_Type = IfIndex
_AtmVcCrossConnectHighIfIndex_Object = MibTableColumn
atmVcCrossConnectHighIfIndex = _AtmVcCrossConnectHighIfIndex_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 11, 1, 5),
    _AtmVcCrossConnectHighIfIndex_Type()
)
atmVcCrossConnectHighIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    atmVcCrossConnectHighIfIndex.setStatus("current")


class _AtmVcCrossConnectHighVpi_Type(Integer32):
    """Custom type atmVcCrossConnectHighVpi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_AtmVcCrossConnectHighVpi_Type.__name__ = "Integer32"
_AtmVcCrossConnectHighVpi_Object = MibTableColumn
atmVcCrossConnectHighVpi = _AtmVcCrossConnectHighVpi_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 11, 1, 6),
    _AtmVcCrossConnectHighVpi_Type()
)
atmVcCrossConnectHighVpi.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    atmVcCrossConnectHighVpi.setStatus("current")


class _AtmVcCrossConnectHighVci_Type(Integer32):
    """Custom type atmVcCrossConnectHighVci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AtmVcCrossConnectHighVci_Type.__name__ = "Integer32"
_AtmVcCrossConnectHighVci_Object = MibTableColumn
atmVcCrossConnectHighVci = _AtmVcCrossConnectHighVci_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 11, 1, 7),
    _AtmVcCrossConnectHighVci_Type()
)
atmVcCrossConnectHighVci.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    atmVcCrossConnectHighVci.setStatus("current")


class _AtmVcCrossConnectAdminStatus_Type(Integer32):
    """Custom type atmVcCrossConnectAdminStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_AtmVcCrossConnectAdminStatus_Type.__name__ = "Integer32"
_AtmVcCrossConnectAdminStatus_Object = MibTableColumn
atmVcCrossConnectAdminStatus = _AtmVcCrossConnectAdminStatus_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 11, 1, 8),
    _AtmVcCrossConnectAdminStatus_Type()
)
atmVcCrossConnectAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmVcCrossConnectAdminStatus.setStatus("current")


class _AtmVcCrossConnectL2HOperStatus_Type(Integer32):
    """Custom type atmVcCrossConnectL2HOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("unknown", 3),
          ("up", 1))
    )


_AtmVcCrossConnectL2HOperStatus_Type.__name__ = "Integer32"
_AtmVcCrossConnectL2HOperStatus_Object = MibTableColumn
atmVcCrossConnectL2HOperStatus = _AtmVcCrossConnectL2HOperStatus_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 11, 1, 9),
    _AtmVcCrossConnectL2HOperStatus_Type()
)
atmVcCrossConnectL2HOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmVcCrossConnectL2HOperStatus.setStatus("current")


class _AtmVcCrossConnectH2LOperStatus_Type(Integer32):
    """Custom type atmVcCrossConnectH2LOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("unknown", 3),
          ("up", 1))
    )


_AtmVcCrossConnectH2LOperStatus_Type.__name__ = "Integer32"
_AtmVcCrossConnectH2LOperStatus_Object = MibTableColumn
atmVcCrossConnectH2LOperStatus = _AtmVcCrossConnectH2LOperStatus_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 11, 1, 10),
    _AtmVcCrossConnectH2LOperStatus_Type()
)
atmVcCrossConnectH2LOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmVcCrossConnectH2LOperStatus.setStatus("current")
_AtmVcCrossConnectL2HLastChange_Type = TimeStamp
_AtmVcCrossConnectL2HLastChange_Object = MibTableColumn
atmVcCrossConnectL2HLastChange = _AtmVcCrossConnectL2HLastChange_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 11, 1, 11),
    _AtmVcCrossConnectL2HLastChange_Type()
)
atmVcCrossConnectL2HLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmVcCrossConnectL2HLastChange.setStatus("current")
_AtmVcCrossConnectH2LLastChange_Type = TimeStamp
_AtmVcCrossConnectH2LLastChange_Object = MibTableColumn
atmVcCrossConnectH2LLastChange = _AtmVcCrossConnectH2LLastChange_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 11, 1, 12),
    _AtmVcCrossConnectH2LLastChange_Type()
)
atmVcCrossConnectH2LLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmVcCrossConnectH2LLastChange.setStatus("current")
_AtmVcCrossConnectRowStatus_Type = RowStatus
_AtmVcCrossConnectRowStatus_Object = MibTableColumn
atmVcCrossConnectRowStatus = _AtmVcCrossConnectRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 11, 1, 13),
    _AtmVcCrossConnectRowStatus_Type()
)
atmVcCrossConnectRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmVcCrossConnectRowStatus.setStatus("current")
_Aal5VccTable_Object = MibTable
aal5VccTable = _Aal5VccTable_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 12)
)
if mibBuilder.loadTexts:
    aal5VccTable.setStatus("current")
_Aal5VccEntry_Object = MibTableRow
aal5VccEntry = _Aal5VccEntry_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 12, 1)
)
aal5VccEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ATM-MIB", "aal5VccVpi"),
    (0, "ATM-MIB", "aal5VccVci"),
)
if mibBuilder.loadTexts:
    aal5VccEntry.setStatus("current")


class _Aal5VccVpi_Type(Integer32):
    """Custom type aal5VccVpi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_Aal5VccVpi_Type.__name__ = "Integer32"
_Aal5VccVpi_Object = MibTableColumn
aal5VccVpi = _Aal5VccVpi_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 12, 1, 1),
    _Aal5VccVpi_Type()
)
aal5VccVpi.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aal5VccVpi.setStatus("current")


class _Aal5VccVci_Type(Integer32):
    """Custom type aal5VccVci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Aal5VccVci_Type.__name__ = "Integer32"
_Aal5VccVci_Object = MibTableColumn
aal5VccVci = _Aal5VccVci_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 12, 1, 2),
    _Aal5VccVci_Type()
)
aal5VccVci.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aal5VccVci.setStatus("current")
_Aal5VccCrcErrors_Type = Counter32
_Aal5VccCrcErrors_Object = MibTableColumn
aal5VccCrcErrors = _Aal5VccCrcErrors_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 12, 1, 3),
    _Aal5VccCrcErrors_Type()
)
aal5VccCrcErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aal5VccCrcErrors.setStatus("current")
_Aal5VccSarTimeOuts_Type = Counter32
_Aal5VccSarTimeOuts_Object = MibTableColumn
aal5VccSarTimeOuts = _Aal5VccSarTimeOuts_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 12, 1, 4),
    _Aal5VccSarTimeOuts_Type()
)
aal5VccSarTimeOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aal5VccSarTimeOuts.setStatus("current")
_Aal5VccOverSizedSDUs_Type = Counter32
_Aal5VccOverSizedSDUs_Object = MibTableColumn
aal5VccOverSizedSDUs = _Aal5VccOverSizedSDUs_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 12, 1, 5),
    _Aal5VccOverSizedSDUs_Type()
)
aal5VccOverSizedSDUs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aal5VccOverSizedSDUs.setStatus("current")
_AtmMIBConformance_ObjectIdentity = ObjectIdentity
atmMIBConformance = _AtmMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 37, 2)
)
_AtmMIBGroups_ObjectIdentity = ObjectIdentity
atmMIBGroups = _AtmMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 37, 2, 1)
)
_AtmMIBCompliances_ObjectIdentity = ObjectIdentity
atmMIBCompliances = _AtmMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 37, 2, 2)
)

# Managed Objects groups

atmInterfaceConfGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 37, 2, 1, 1)
)
atmInterfaceConfGroup.setObjects(
      *(("ATM-MIB", "atmInterfaceMaxVpcs"),
        ("ATM-MIB", "atmInterfaceMaxVccs"),
        ("ATM-MIB", "atmInterfaceConfVpcs"),
        ("ATM-MIB", "atmInterfaceConfVccs"),
        ("ATM-MIB", "atmInterfaceMaxActiveVpiBits"),
        ("ATM-MIB", "atmInterfaceMaxActiveVciBits"),
        ("ATM-MIB", "atmInterfaceIlmiVpi"),
        ("ATM-MIB", "atmInterfaceIlmiVci"),
        ("ATM-MIB", "atmInterfaceAddressType"),
        ("ATM-MIB", "atmInterfaceAdminAddress"),
        ("ATM-MIB", "atmInterfaceMyNeighborIpAddress"),
        ("ATM-MIB", "atmInterfaceMyNeighborIfName"))
)
if mibBuilder.loadTexts:
    atmInterfaceConfGroup.setStatus("current")

atmTrafficDescrGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 37, 2, 1, 2)
)
atmTrafficDescrGroup.setObjects(
      *(("ATM-MIB", "atmTrafficDescrType"),
        ("ATM-MIB", "atmTrafficDescrParam1"),
        ("ATM-MIB", "atmTrafficDescrParam2"),
        ("ATM-MIB", "atmTrafficDescrParam3"),
        ("ATM-MIB", "atmTrafficDescrParam4"),
        ("ATM-MIB", "atmTrafficDescrParam5"),
        ("ATM-MIB", "atmTrafficQoSClass"),
        ("ATM-MIB", "atmTrafficDescrRowStatus"))
)
if mibBuilder.loadTexts:
    atmTrafficDescrGroup.setStatus("current")

atmInterfaceDs3PlcpGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 37, 2, 1, 3)
)
atmInterfaceDs3PlcpGroup.setObjects(
      *(("ATM-MIB", "atmInterfaceDs3PlcpSEFSs"),
        ("ATM-MIB", "atmInterfaceDs3PlcpAlarmState"),
        ("ATM-MIB", "atmInterfaceDs3PlcpUASs"))
)
if mibBuilder.loadTexts:
    atmInterfaceDs3PlcpGroup.setStatus("current")

atmInterfaceTCGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 37, 2, 1, 4)
)
atmInterfaceTCGroup.setObjects(
      *(("ATM-MIB", "atmInterfaceOCDEvents"),
        ("ATM-MIB", "atmInterfaceTCAlarmState"))
)
if mibBuilder.loadTexts:
    atmInterfaceTCGroup.setStatus("current")

atmVpcTerminationGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 37, 2, 1, 5)
)
atmVpcTerminationGroup.setObjects(
      *(("ATM-MIB", "atmVplOperStatus"),
        ("ATM-MIB", "atmVplAdminStatus"),
        ("ATM-MIB", "atmVplLastChange"),
        ("ATM-MIB", "atmVplReceiveTrafficDescrIndex"),
        ("ATM-MIB", "atmVplTransmitTrafficDescrIndex"),
        ("ATM-MIB", "atmVplRowStatus"))
)
if mibBuilder.loadTexts:
    atmVpcTerminationGroup.setStatus("current")

atmVccTerminationGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 37, 2, 1, 6)
)
atmVccTerminationGroup.setObjects(
      *(("ATM-MIB", "atmVclOperStatus"),
        ("ATM-MIB", "atmVclAdminStatus"),
        ("ATM-MIB", "atmVclLastChange"),
        ("ATM-MIB", "atmVclReceiveTrafficDescrIndex"),
        ("ATM-MIB", "atmVclTransmitTrafficDescrIndex"),
        ("ATM-MIB", "atmVccAalType"),
        ("ATM-MIB", "atmVclRowStatus"))
)
if mibBuilder.loadTexts:
    atmVccTerminationGroup.setStatus("current")

atmVpCrossConnectGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 37, 2, 1, 7)
)
atmVpCrossConnectGroup.setObjects(
      *(("ATM-MIB", "atmVplReceiveTrafficDescrIndex"),
        ("ATM-MIB", "atmVplTransmitTrafficDescrIndex"),
        ("ATM-MIB", "atmVplOperStatus"),
        ("ATM-MIB", "atmVplRowStatus"),
        ("ATM-MIB", "atmVpCrossConnectAdminStatus"),
        ("ATM-MIB", "atmVpCrossConnectL2HOperStatus"),
        ("ATM-MIB", "atmVpCrossConnectH2LOperStatus"),
        ("ATM-MIB", "atmVpCrossConnectL2HLastChange"),
        ("ATM-MIB", "atmVpCrossConnectH2LLastChange"),
        ("ATM-MIB", "atmVpCrossConnectRowStatus"),
        ("ATM-MIB", "atmVplCrossConnectIdentifier"),
        ("ATM-MIB", "atmVpCrossConnectIndexNext"))
)
if mibBuilder.loadTexts:
    atmVpCrossConnectGroup.setStatus("current")

atmVcCrossConnectGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 37, 2, 1, 8)
)
atmVcCrossConnectGroup.setObjects(
      *(("ATM-MIB", "atmVclReceiveTrafficDescrIndex"),
        ("ATM-MIB", "atmVclTransmitTrafficDescrIndex"),
        ("ATM-MIB", "atmVclOperStatus"),
        ("ATM-MIB", "atmVclRowStatus"),
        ("ATM-MIB", "atmVcCrossConnectAdminStatus"),
        ("ATM-MIB", "atmVcCrossConnectL2HOperStatus"),
        ("ATM-MIB", "atmVcCrossConnectH2LOperStatus"),
        ("ATM-MIB", "atmVcCrossConnectL2HLastChange"),
        ("ATM-MIB", "atmVcCrossConnectH2LLastChange"),
        ("ATM-MIB", "atmVcCrossConnectRowStatus"),
        ("ATM-MIB", "atmVclCrossConnectIdentifier"),
        ("ATM-MIB", "atmVcCrossConnectIndexNext"))
)
if mibBuilder.loadTexts:
    atmVcCrossConnectGroup.setStatus("current")

aal5VccGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 37, 2, 1, 9)
)
aal5VccGroup.setObjects(
      *(("ATM-MIB", "atmVccAal5CpcsTransmitSduSize"),
        ("ATM-MIB", "atmVccAal5CpcsReceiveSduSize"),
        ("ATM-MIB", "atmVccAal5EncapsType"),
        ("ATM-MIB", "aal5VccCrcErrors"),
        ("ATM-MIB", "aal5VccSarTimeOuts"),
        ("ATM-MIB", "aal5VccOverSizedSDUs"))
)
if mibBuilder.loadTexts:
    aal5VccGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

atmMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 37, 2, 2, 1)
)
if mibBuilder.loadTexts:
    atmMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ATM-MIB",
    **{"IfIndex": IfIndex,
       "AtmTrafficDescrParamIndex": AtmTrafficDescrParamIndex,
       "atmMIB": atmMIB,
       "atmMIBObjects": atmMIBObjects,
       "atmTrafficDescriptorTypes": atmTrafficDescriptorTypes,
       "atmNoTrafficDescriptor": atmNoTrafficDescriptor,
       "atmNoClpNoScr": atmNoClpNoScr,
       "atmClpNoTaggingNoScr": atmClpNoTaggingNoScr,
       "atmClpTaggingNoScr": atmClpTaggingNoScr,
       "atmNoClpScr": atmNoClpScr,
       "atmClpNoTaggingScr": atmClpNoTaggingScr,
       "atmClpTaggingScr": atmClpTaggingScr,
       "atmInterfaceConfTable": atmInterfaceConfTable,
       "atmInterfaceConfEntry": atmInterfaceConfEntry,
       "atmInterfaceMaxVpcs": atmInterfaceMaxVpcs,
       "atmInterfaceMaxVccs": atmInterfaceMaxVccs,
       "atmInterfaceConfVpcs": atmInterfaceConfVpcs,
       "atmInterfaceConfVccs": atmInterfaceConfVccs,
       "atmInterfaceMaxActiveVpiBits": atmInterfaceMaxActiveVpiBits,
       "atmInterfaceMaxActiveVciBits": atmInterfaceMaxActiveVciBits,
       "atmInterfaceIlmiVpi": atmInterfaceIlmiVpi,
       "atmInterfaceIlmiVci": atmInterfaceIlmiVci,
       "atmInterfaceAddressType": atmInterfaceAddressType,
       "atmInterfaceAdminAddress": atmInterfaceAdminAddress,
       "atmInterfaceMyNeighborIpAddress": atmInterfaceMyNeighborIpAddress,
       "atmInterfaceMyNeighborIfName": atmInterfaceMyNeighborIfName,
       "atmInterfaceDs3PlcpTable": atmInterfaceDs3PlcpTable,
       "atmInterfaceDs3PlcpEntry": atmInterfaceDs3PlcpEntry,
       "atmInterfaceDs3PlcpSEFSs": atmInterfaceDs3PlcpSEFSs,
       "atmInterfaceDs3PlcpAlarmState": atmInterfaceDs3PlcpAlarmState,
       "atmInterfaceDs3PlcpUASs": atmInterfaceDs3PlcpUASs,
       "atmInterfaceTCTable": atmInterfaceTCTable,
       "atmInterfaceTCEntry": atmInterfaceTCEntry,
       "atmInterfaceOCDEvents": atmInterfaceOCDEvents,
       "atmInterfaceTCAlarmState": atmInterfaceTCAlarmState,
       "atmTrafficDescrParamTable": atmTrafficDescrParamTable,
       "atmTrafficDescrParamEntry": atmTrafficDescrParamEntry,
       "atmTrafficDescrParamIndex": atmTrafficDescrParamIndex,
       "atmTrafficDescrType": atmTrafficDescrType,
       "atmTrafficDescrParam1": atmTrafficDescrParam1,
       "atmTrafficDescrParam2": atmTrafficDescrParam2,
       "atmTrafficDescrParam3": atmTrafficDescrParam3,
       "atmTrafficDescrParam4": atmTrafficDescrParam4,
       "atmTrafficDescrParam5": atmTrafficDescrParam5,
       "atmTrafficQoSClass": atmTrafficQoSClass,
       "atmTrafficDescrRowStatus": atmTrafficDescrRowStatus,
       "atmVplTable": atmVplTable,
       "atmVplEntry": atmVplEntry,
       "atmVplVpi": atmVplVpi,
       "atmVplAdminStatus": atmVplAdminStatus,
       "atmVplOperStatus": atmVplOperStatus,
       "atmVplLastChange": atmVplLastChange,
       "atmVplReceiveTrafficDescrIndex": atmVplReceiveTrafficDescrIndex,
       "atmVplTransmitTrafficDescrIndex": atmVplTransmitTrafficDescrIndex,
       "atmVplCrossConnectIdentifier": atmVplCrossConnectIdentifier,
       "atmVplRowStatus": atmVplRowStatus,
       "atmVclTable": atmVclTable,
       "atmVclEntry": atmVclEntry,
       "atmVclVpi": atmVclVpi,
       "atmVclVci": atmVclVci,
       "atmVclAdminStatus": atmVclAdminStatus,
       "atmVclOperStatus": atmVclOperStatus,
       "atmVclLastChange": atmVclLastChange,
       "atmVclReceiveTrafficDescrIndex": atmVclReceiveTrafficDescrIndex,
       "atmVclTransmitTrafficDescrIndex": atmVclTransmitTrafficDescrIndex,
       "atmVccAalType": atmVccAalType,
       "atmVccAal5CpcsTransmitSduSize": atmVccAal5CpcsTransmitSduSize,
       "atmVccAal5CpcsReceiveSduSize": atmVccAal5CpcsReceiveSduSize,
       "atmVccAal5EncapsType": atmVccAal5EncapsType,
       "atmVclCrossConnectIdentifier": atmVclCrossConnectIdentifier,
       "atmVclRowStatus": atmVclRowStatus,
       "atmVpCrossConnectIndexNext": atmVpCrossConnectIndexNext,
       "atmVpCrossConnectTable": atmVpCrossConnectTable,
       "atmVpCrossConnectEntry": atmVpCrossConnectEntry,
       "atmVpCrossConnectIndex": atmVpCrossConnectIndex,
       "atmVpCrossConnectLowIfIndex": atmVpCrossConnectLowIfIndex,
       "atmVpCrossConnectLowVpi": atmVpCrossConnectLowVpi,
       "atmVpCrossConnectHighIfIndex": atmVpCrossConnectHighIfIndex,
       "atmVpCrossConnectHighVpi": atmVpCrossConnectHighVpi,
       "atmVpCrossConnectAdminStatus": atmVpCrossConnectAdminStatus,
       "atmVpCrossConnectL2HOperStatus": atmVpCrossConnectL2HOperStatus,
       "atmVpCrossConnectH2LOperStatus": atmVpCrossConnectH2LOperStatus,
       "atmVpCrossConnectL2HLastChange": atmVpCrossConnectL2HLastChange,
       "atmVpCrossConnectH2LLastChange": atmVpCrossConnectH2LLastChange,
       "atmVpCrossConnectRowStatus": atmVpCrossConnectRowStatus,
       "atmVcCrossConnectIndexNext": atmVcCrossConnectIndexNext,
       "atmVcCrossConnectTable": atmVcCrossConnectTable,
       "atmVcCrossConnectEntry": atmVcCrossConnectEntry,
       "atmVcCrossConnectIndex": atmVcCrossConnectIndex,
       "atmVcCrossConnectLowIfIndex": atmVcCrossConnectLowIfIndex,
       "atmVcCrossConnectLowVpi": atmVcCrossConnectLowVpi,
       "atmVcCrossConnectLowVci": atmVcCrossConnectLowVci,
       "atmVcCrossConnectHighIfIndex": atmVcCrossConnectHighIfIndex,
       "atmVcCrossConnectHighVpi": atmVcCrossConnectHighVpi,
       "atmVcCrossConnectHighVci": atmVcCrossConnectHighVci,
       "atmVcCrossConnectAdminStatus": atmVcCrossConnectAdminStatus,
       "atmVcCrossConnectL2HOperStatus": atmVcCrossConnectL2HOperStatus,
       "atmVcCrossConnectH2LOperStatus": atmVcCrossConnectH2LOperStatus,
       "atmVcCrossConnectL2HLastChange": atmVcCrossConnectL2HLastChange,
       "atmVcCrossConnectH2LLastChange": atmVcCrossConnectH2LLastChange,
       "atmVcCrossConnectRowStatus": atmVcCrossConnectRowStatus,
       "aal5VccTable": aal5VccTable,
       "aal5VccEntry": aal5VccEntry,
       "aal5VccVpi": aal5VccVpi,
       "aal5VccVci": aal5VccVci,
       "aal5VccCrcErrors": aal5VccCrcErrors,
       "aal5VccSarTimeOuts": aal5VccSarTimeOuts,
       "aal5VccOverSizedSDUs": aal5VccOverSizedSDUs,
       "atmMIBConformance": atmMIBConformance,
       "atmMIBGroups": atmMIBGroups,
       "atmInterfaceConfGroup": atmInterfaceConfGroup,
       "atmTrafficDescrGroup": atmTrafficDescrGroup,
       "atmInterfaceDs3PlcpGroup": atmInterfaceDs3PlcpGroup,
       "atmInterfaceTCGroup": atmInterfaceTCGroup,
       "atmVpcTerminationGroup": atmVpcTerminationGroup,
       "atmVccTerminationGroup": atmVccTerminationGroup,
       "atmVpCrossConnectGroup": atmVpCrossConnectGroup,
       "atmVcCrossConnectGroup": atmVcCrossConnectGroup,
       "aal5VccGroup": aal5VccGroup,
       "atmMIBCompliances": atmMIBCompliances,
       "atmMIBCompliance": atmMIBCompliance}
)
