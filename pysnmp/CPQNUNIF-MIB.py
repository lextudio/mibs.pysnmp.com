# SNMP MIB module (CPQNUNIF-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CPQNUNIF-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:17:33 2024
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
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions



class CpqnRowStatus(Integer32):
    """Custom type CpqnRowStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("row-invalid", 2),
          ("row-valid", 1))
    )





class IpxAddress(OctetString):
    """Custom type IpxAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(10, 10),
    )





class CpqnVersionType(Integer32):
    """Custom type CpqnVersionType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("hardware", 2),
          ("other", 1),
          ("software", 3))
    )





class CpqnVersionStep(Integer32):
    """Custom type CpqnVersionStep based on Integer32"""
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
        *(("alpha", 3),
          ("beta", 4),
          ("engineering", 2),
          ("other", 1),
          ("pilot", 6),
          ("post-production", 9),
          ("pre-production", 7),
          ("production", 8),
          ("prototype", 5),
          ("simple-revision", 10))
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Compaq_ObjectIdentity = ObjectIdentity
compaq = _Compaq_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232)
)
_CpqnCommon_ObjectIdentity = ObjectIdentity
cpqnCommon = _CpqnCommon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 121)
)
_CpqnMibModules_ObjectIdentity = ObjectIdentity
cpqnMibModules = _CpqnMibModules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 121, 1)
)
_CpqnMibModuleTable_Object = MibTable
cpqnMibModuleTable = _CpqnMibModuleTable_Object(
    (1, 3, 6, 1, 4, 1, 232, 121, 1, 1)
)
if mibBuilder.loadTexts:
    cpqnMibModuleTable.setStatus("mandatory")
_CpqnMibModuleEntry_Object = MibTableRow
cpqnMibModuleEntry = _CpqnMibModuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 232, 121, 1, 1, 1)
)
cpqnMibModuleEntry.setIndexNames(
    (0, "CPQNUNIF-MIB", "cpqnMibModuleIndex"),
)
if mibBuilder.loadTexts:
    cpqnMibModuleEntry.setStatus("mandatory")
_CpqnMibModuleIndex_Type = Integer32
_CpqnMibModuleIndex_Object = MibTableColumn
cpqnMibModuleIndex = _CpqnMibModuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 121, 1, 1, 1, 1),
    _CpqnMibModuleIndex_Type()
)
cpqnMibModuleIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqnMibModuleIndex.setStatus("mandatory")
_CpqnMibModuleDescr_Type = DisplayString
_CpqnMibModuleDescr_Object = MibTableColumn
cpqnMibModuleDescr = _CpqnMibModuleDescr_Object(
    (1, 3, 6, 1, 4, 1, 232, 121, 1, 1, 1, 2),
    _CpqnMibModuleDescr_Type()
)
cpqnMibModuleDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqnMibModuleDescr.setStatus("mandatory")
_CpqnMibModuleOid_Type = ObjectIdentifier
_CpqnMibModuleOid_Object = MibTableColumn
cpqnMibModuleOid = _CpqnMibModuleOid_Object(
    (1, 3, 6, 1, 4, 1, 232, 121, 1, 1, 1, 3),
    _CpqnMibModuleOid_Type()
)
cpqnMibModuleOid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqnMibModuleOid.setStatus("mandatory")
_CpqnUnitControl_ObjectIdentity = ObjectIdentity
cpqnUnitControl = _CpqnUnitControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 121, 2)
)


class _CpqnUnitReset_Type(Integer32):
    """Custom type cpqnUnitReset based on Integer32"""
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
        *(("reset", 2),
          ("reset-to-factory-values", 4),
          ("running", 1),
          ("warm-start", 3))
    )


_CpqnUnitReset_Type.__name__ = "Integer32"
_CpqnUnitReset_Object = MibScalar
cpqnUnitReset = _CpqnUnitReset_Object(
    (1, 3, 6, 1, 4, 1, 232, 121, 2, 1),
    _CpqnUnitReset_Type()
)
cpqnUnitReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqnUnitReset.setStatus("mandatory")
_CpqnPrimarySerialPort_Type = Integer32
_CpqnPrimarySerialPort_Object = MibScalar
cpqnPrimarySerialPort = _CpqnPrimarySerialPort_Object(
    (1, 3, 6, 1, 4, 1, 232, 121, 2, 2),
    _CpqnPrimarySerialPort_Type()
)
cpqnPrimarySerialPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqnPrimarySerialPort.setStatus("mandatory")
_CpqnSerialPortTable_Object = MibTable
cpqnSerialPortTable = _CpqnSerialPortTable_Object(
    (1, 3, 6, 1, 4, 1, 232, 121, 2, 3)
)
if mibBuilder.loadTexts:
    cpqnSerialPortTable.setStatus("mandatory")
_CpqnSerialPortEntry_Object = MibTableRow
cpqnSerialPortEntry = _CpqnSerialPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 232, 121, 2, 3, 1)
)
cpqnSerialPortEntry.setIndexNames(
    (0, "CPQNUNIF-MIB", "cpqnSPortIndex"),
)
if mibBuilder.loadTexts:
    cpqnSerialPortEntry.setStatus("mandatory")
_CpqnSPortIndex_Type = Integer32
_CpqnSPortIndex_Object = MibTableColumn
cpqnSPortIndex = _CpqnSPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 121, 2, 3, 1, 1),
    _CpqnSPortIndex_Type()
)
cpqnSPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqnSPortIndex.setStatus("mandatory")
_CpqnSPortIfIndex_Type = Integer32
_CpqnSPortIfIndex_Object = MibTableColumn
cpqnSPortIfIndex = _CpqnSPortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 121, 2, 3, 1, 2),
    _CpqnSPortIfIndex_Type()
)
cpqnSPortIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqnSPortIfIndex.setStatus("mandatory")


class _CpqnSPortModemInitStringEnable_Type(Integer32):
    """Custom type cpqnSPortModemInitStringEnable based on Integer32"""
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


_CpqnSPortModemInitStringEnable_Type.__name__ = "Integer32"
_CpqnSPortModemInitStringEnable_Object = MibTableColumn
cpqnSPortModemInitStringEnable = _CpqnSPortModemInitStringEnable_Object(
    (1, 3, 6, 1, 4, 1, 232, 121, 2, 3, 1, 3),
    _CpqnSPortModemInitStringEnable_Type()
)
cpqnSPortModemInitStringEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqnSPortModemInitStringEnable.setStatus("mandatory")


class _CpqnSPortModemInitString_Type(DisplayString):
    """Custom type cpqnSPortModemInitString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 40),
    )


_CpqnSPortModemInitString_Type.__name__ = "DisplayString"
_CpqnSPortModemInitString_Object = MibTableColumn
cpqnSPortModemInitString = _CpqnSPortModemInitString_Object(
    (1, 3, 6, 1, 4, 1, 232, 121, 2, 3, 1, 4),
    _CpqnSPortModemInitString_Type()
)
cpqnSPortModemInitString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqnSPortModemInitString.setStatus("mandatory")


class _CpqnSPortModemAutoNegotiateState_Type(Integer32):
    """Custom type cpqnSPortModemAutoNegotiateState based on Integer32"""
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


_CpqnSPortModemAutoNegotiateState_Type.__name__ = "Integer32"
_CpqnSPortModemAutoNegotiateState_Object = MibTableColumn
cpqnSPortModemAutoNegotiateState = _CpqnSPortModemAutoNegotiateState_Object(
    (1, 3, 6, 1, 4, 1, 232, 121, 2, 3, 1, 5),
    _CpqnSPortModemAutoNegotiateState_Type()
)
cpqnSPortModemAutoNegotiateState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqnSPortModemAutoNegotiateState.setStatus("mandatory")
_CpqnSPortBaudRate_Type = Integer32
_CpqnSPortBaudRate_Object = MibTableColumn
cpqnSPortBaudRate = _CpqnSPortBaudRate_Object(
    (1, 3, 6, 1, 4, 1, 232, 121, 2, 3, 1, 6),
    _CpqnSPortBaudRate_Type()
)
cpqnSPortBaudRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqnSPortBaudRate.setStatus("mandatory")
_CpqnSupportedBaudRateTable_Object = MibTable
cpqnSupportedBaudRateTable = _CpqnSupportedBaudRateTable_Object(
    (1, 3, 6, 1, 4, 1, 232, 121, 2, 4)
)
if mibBuilder.loadTexts:
    cpqnSupportedBaudRateTable.setStatus("mandatory")
_CpqnSupportedBaudRateEntry_Object = MibTableRow
cpqnSupportedBaudRateEntry = _CpqnSupportedBaudRateEntry_Object(
    (1, 3, 6, 1, 4, 1, 232, 121, 2, 4, 1)
)
cpqnSupportedBaudRateEntry.setIndexNames(
    (0, "CPQNUNIF-MIB", "cpqnBaudRatePortIndex"),
    (0, "CPQNUNIF-MIB", "cpqnBaudRateIndex"),
)
if mibBuilder.loadTexts:
    cpqnSupportedBaudRateEntry.setStatus("mandatory")
_CpqnBaudRatePortIndex_Type = Integer32
_CpqnBaudRatePortIndex_Object = MibTableColumn
cpqnBaudRatePortIndex = _CpqnBaudRatePortIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 121, 2, 4, 1, 1),
    _CpqnBaudRatePortIndex_Type()
)
cpqnBaudRatePortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqnBaudRatePortIndex.setStatus("mandatory")
_CpqnBaudRateIndex_Type = Integer32
_CpqnBaudRateIndex_Object = MibTableColumn
cpqnBaudRateIndex = _CpqnBaudRateIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 121, 2, 4, 1, 2),
    _CpqnBaudRateIndex_Type()
)
cpqnBaudRateIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqnBaudRateIndex.setStatus("mandatory")
_CpqnBaudRate_Type = Integer32
_CpqnBaudRate_Object = MibTableColumn
cpqnBaudRate = _CpqnBaudRate_Object(
    (1, 3, 6, 1, 4, 1, 232, 121, 2, 4, 1, 3),
    _CpqnBaudRate_Type()
)
cpqnBaudRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqnBaudRate.setStatus("mandatory")
_CpqnVersionInformation_ObjectIdentity = ObjectIdentity
cpqnVersionInformation = _CpqnVersionInformation_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 121, 3)
)
_CpqnVersionTable_Object = MibTable
cpqnVersionTable = _CpqnVersionTable_Object(
    (1, 3, 6, 1, 4, 1, 232, 121, 3, 1)
)
if mibBuilder.loadTexts:
    cpqnVersionTable.setStatus("mandatory")
_CpqnVersionEntry_Object = MibTableRow
cpqnVersionEntry = _CpqnVersionEntry_Object(
    (1, 3, 6, 1, 4, 1, 232, 121, 3, 1, 1)
)
cpqnVersionEntry.setIndexNames(
    (0, "CPQNUNIF-MIB", "cpqnVersionIndex"),
)
if mibBuilder.loadTexts:
    cpqnVersionEntry.setStatus("mandatory")
_CpqnVersionIndex_Type = Integer32
_CpqnVersionIndex_Object = MibTableColumn
cpqnVersionIndex = _CpqnVersionIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 121, 3, 1, 1, 1),
    _CpqnVersionIndex_Type()
)
cpqnVersionIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqnVersionIndex.setStatus("mandatory")
_CpqnVersionType_Type = CpqnVersionType
_CpqnVersionType_Object = MibTableColumn
cpqnVersionType = _CpqnVersionType_Object(
    (1, 3, 6, 1, 4, 1, 232, 121, 3, 1, 1, 2),
    _CpqnVersionType_Type()
)
cpqnVersionType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqnVersionType.setStatus("mandatory")
_CpqnVersionDesc_Type = DisplayString
_CpqnVersionDesc_Object = MibTableColumn
cpqnVersionDesc = _CpqnVersionDesc_Object(
    (1, 3, 6, 1, 4, 1, 232, 121, 3, 1, 1, 3),
    _CpqnVersionDesc_Type()
)
cpqnVersionDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqnVersionDesc.setStatus("mandatory")
_CpqnVersionMajor_Type = Integer32
_CpqnVersionMajor_Object = MibTableColumn
cpqnVersionMajor = _CpqnVersionMajor_Object(
    (1, 3, 6, 1, 4, 1, 232, 121, 3, 1, 1, 4),
    _CpqnVersionMajor_Type()
)
cpqnVersionMajor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqnVersionMajor.setStatus("mandatory")
_CpqnVersionMinor_Type = Integer32
_CpqnVersionMinor_Object = MibTableColumn
cpqnVersionMinor = _CpqnVersionMinor_Object(
    (1, 3, 6, 1, 4, 1, 232, 121, 3, 1, 1, 5),
    _CpqnVersionMinor_Type()
)
cpqnVersionMinor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqnVersionMinor.setStatus("mandatory")
_CpqnVersionStep_Type = CpqnVersionStep
_CpqnVersionStep_Object = MibTableColumn
cpqnVersionStep = _CpqnVersionStep_Object(
    (1, 3, 6, 1, 4, 1, 232, 121, 3, 1, 1, 6),
    _CpqnVersionStep_Type()
)
cpqnVersionStep.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqnVersionStep.setStatus("mandatory")
_CpqnVersionRev_Type = Integer32
_CpqnVersionRev_Object = MibTableColumn
cpqnVersionRev = _CpqnVersionRev_Object(
    (1, 3, 6, 1, 4, 1, 232, 121, 3, 1, 1, 7),
    _CpqnVersionRev_Type()
)
cpqnVersionRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqnVersionRev.setStatus("mandatory")
_CpqnVersionSerialNumber_Type = DisplayString
_CpqnVersionSerialNumber_Object = MibTableColumn
cpqnVersionSerialNumber = _CpqnVersionSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 232, 121, 3, 1, 1, 8),
    _CpqnVersionSerialNumber_Type()
)
cpqnVersionSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqnVersionSerialNumber.setStatus("mandatory")
_CpqnVersionUnitId_Type = Integer32
_CpqnVersionUnitId_Object = MibTableColumn
cpqnVersionUnitId = _CpqnVersionUnitId_Object(
    (1, 3, 6, 1, 4, 1, 232, 121, 3, 1, 1, 9),
    _CpqnVersionUnitId_Type()
)
cpqnVersionUnitId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqnVersionUnitId.setStatus("mandatory")
_CpqnVersionParentIndex_Type = Integer32
_CpqnVersionParentIndex_Object = MibTableColumn
cpqnVersionParentIndex = _CpqnVersionParentIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 121, 3, 1, 1, 10),
    _CpqnVersionParentIndex_Type()
)
cpqnVersionParentIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqnVersionParentIndex.setStatus("mandatory")
_CpqnAccessControl_ObjectIdentity = ObjectIdentity
cpqnAccessControl = _CpqnAccessControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 121, 4)
)


class _CpqnAclTelnetControl_Type(Integer32):
    """Custom type cpqnAclTelnetControl based on Integer32"""
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


_CpqnAclTelnetControl_Type.__name__ = "Integer32"
_CpqnAclTelnetControl_Object = MibScalar
cpqnAclTelnetControl = _CpqnAclTelnetControl_Object(
    (1, 3, 6, 1, 4, 1, 232, 121, 4, 1),
    _CpqnAclTelnetControl_Type()
)
cpqnAclTelnetControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqnAclTelnetControl.setStatus("mandatory")
_CpqnCommunityAccessIPTable_Object = MibTable
cpqnCommunityAccessIPTable = _CpqnCommunityAccessIPTable_Object(
    (1, 3, 6, 1, 4, 1, 232, 121, 4, 2)
)
if mibBuilder.loadTexts:
    cpqnCommunityAccessIPTable.setStatus("mandatory")
_CpqnCommAccessIPEntry_Object = MibTableRow
cpqnCommAccessIPEntry = _CpqnCommAccessIPEntry_Object(
    (1, 3, 6, 1, 4, 1, 232, 121, 4, 2, 1)
)
cpqnCommAccessIPEntry.setIndexNames(
    (0, "CPQNUNIF-MIB", "cpqnAclIPIndex"),
)
if mibBuilder.loadTexts:
    cpqnCommAccessIPEntry.setStatus("mandatory")
_CpqnAclIPIndex_Type = Integer32
_CpqnAclIPIndex_Object = MibTableColumn
cpqnAclIPIndex = _CpqnAclIPIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 121, 4, 2, 1, 1),
    _CpqnAclIPIndex_Type()
)
cpqnAclIPIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqnAclIPIndex.setStatus("mandatory")
_CpqnAclIPRowStatus_Type = CpqnRowStatus
_CpqnAclIPRowStatus_Object = MibTableColumn
cpqnAclIPRowStatus = _CpqnAclIPRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 232, 121, 4, 2, 1, 2),
    _CpqnAclIPRowStatus_Type()
)
cpqnAclIPRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqnAclIPRowStatus.setStatus("mandatory")
_CpqnAclIPAddrMask_Type = IpAddress
_CpqnAclIPAddrMask_Object = MibTableColumn
cpqnAclIPAddrMask = _CpqnAclIPAddrMask_Object(
    (1, 3, 6, 1, 4, 1, 232, 121, 4, 2, 1, 3),
    _CpqnAclIPAddrMask_Type()
)
cpqnAclIPAddrMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqnAclIPAddrMask.setStatus("mandatory")
_CpqnAclIPAddrMatch_Type = IpAddress
_CpqnAclIPAddrMatch_Object = MibTableColumn
cpqnAclIPAddrMatch = _CpqnAclIPAddrMatch_Object(
    (1, 3, 6, 1, 4, 1, 232, 121, 4, 2, 1, 4),
    _CpqnAclIPAddrMatch_Type()
)
cpqnAclIPAddrMatch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqnAclIPAddrMatch.setStatus("mandatory")


class _CpqnAclIPCommunity_Type(DisplayString):
    """Custom type cpqnAclIPCommunity based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_CpqnAclIPCommunity_Type.__name__ = "DisplayString"
_CpqnAclIPCommunity_Object = MibTableColumn
cpqnAclIPCommunity = _CpqnAclIPCommunity_Object(
    (1, 3, 6, 1, 4, 1, 232, 121, 4, 2, 1, 5),
    _CpqnAclIPCommunity_Type()
)
cpqnAclIPCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqnAclIPCommunity.setStatus("mandatory")


class _CpqnAclIPRights_Type(Integer32):
    """Custom type cpqnAclIPRights based on Integer32"""
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
        *(("no-access", 1),
          ("read-only-allow-telnet", 3),
          ("read-only-prevent-telnet", 2),
          ("read-write-allow-telnet", 4))
    )


_CpqnAclIPRights_Type.__name__ = "Integer32"
_CpqnAclIPRights_Object = MibTableColumn
cpqnAclIPRights = _CpqnAclIPRights_Object(
    (1, 3, 6, 1, 4, 1, 232, 121, 4, 2, 1, 6),
    _CpqnAclIPRights_Type()
)
cpqnAclIPRights.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqnAclIPRights.setStatus("mandatory")
_CpqnCommunityAccessIPXTable_Object = MibTable
cpqnCommunityAccessIPXTable = _CpqnCommunityAccessIPXTable_Object(
    (1, 3, 6, 1, 4, 1, 232, 121, 4, 3)
)
if mibBuilder.loadTexts:
    cpqnCommunityAccessIPXTable.setStatus("mandatory")
_CpqnCommAccessIPXEntry_Object = MibTableRow
cpqnCommAccessIPXEntry = _CpqnCommAccessIPXEntry_Object(
    (1, 3, 6, 1, 4, 1, 232, 121, 4, 3, 1)
)
cpqnCommAccessIPXEntry.setIndexNames(
    (0, "CPQNUNIF-MIB", "cpqnAclIPXIndex"),
)
if mibBuilder.loadTexts:
    cpqnCommAccessIPXEntry.setStatus("mandatory")
_CpqnAclIPXIndex_Type = Integer32
_CpqnAclIPXIndex_Object = MibTableColumn
cpqnAclIPXIndex = _CpqnAclIPXIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 121, 4, 3, 1, 1),
    _CpqnAclIPXIndex_Type()
)
cpqnAclIPXIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqnAclIPXIndex.setStatus("mandatory")
_CpqnAclIPXRowStatus_Type = CpqnRowStatus
_CpqnAclIPXRowStatus_Object = MibTableColumn
cpqnAclIPXRowStatus = _CpqnAclIPXRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 232, 121, 4, 3, 1, 2),
    _CpqnAclIPXRowStatus_Type()
)
cpqnAclIPXRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqnAclIPXRowStatus.setStatus("mandatory")
_CpqnAclIPXAddrMask_Type = IpxAddress
_CpqnAclIPXAddrMask_Object = MibTableColumn
cpqnAclIPXAddrMask = _CpqnAclIPXAddrMask_Object(
    (1, 3, 6, 1, 4, 1, 232, 121, 4, 3, 1, 3),
    _CpqnAclIPXAddrMask_Type()
)
cpqnAclIPXAddrMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqnAclIPXAddrMask.setStatus("mandatory")
_CpqnAclIPXAddrMatch_Type = IpxAddress
_CpqnAclIPXAddrMatch_Object = MibTableColumn
cpqnAclIPXAddrMatch = _CpqnAclIPXAddrMatch_Object(
    (1, 3, 6, 1, 4, 1, 232, 121, 4, 3, 1, 4),
    _CpqnAclIPXAddrMatch_Type()
)
cpqnAclIPXAddrMatch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqnAclIPXAddrMatch.setStatus("mandatory")


class _CpqnAclIPXCommunity_Type(DisplayString):
    """Custom type cpqnAclIPXCommunity based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_CpqnAclIPXCommunity_Type.__name__ = "DisplayString"
_CpqnAclIPXCommunity_Object = MibTableColumn
cpqnAclIPXCommunity = _CpqnAclIPXCommunity_Object(
    (1, 3, 6, 1, 4, 1, 232, 121, 4, 3, 1, 5),
    _CpqnAclIPXCommunity_Type()
)
cpqnAclIPXCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqnAclIPXCommunity.setStatus("mandatory")


class _CpqnAclIPXRights_Type(Integer32):
    """Custom type cpqnAclIPXRights based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("no-access", 1),
          ("read-only-access", 2),
          ("read-write-access", 3))
    )


_CpqnAclIPXRights_Type.__name__ = "Integer32"
_CpqnAclIPXRights_Object = MibTableColumn
cpqnAclIPXRights = _CpqnAclIPXRights_Object(
    (1, 3, 6, 1, 4, 1, 232, 121, 4, 3, 1, 6),
    _CpqnAclIPXRights_Type()
)
cpqnAclIPXRights.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqnAclIPXRights.setStatus("mandatory")
_CpqnTrapDestinations_ObjectIdentity = ObjectIdentity
cpqnTrapDestinations = _CpqnTrapDestinations_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 121, 5)
)
_CpqnIPTrapDestTable_Object = MibTable
cpqnIPTrapDestTable = _CpqnIPTrapDestTable_Object(
    (1, 3, 6, 1, 4, 1, 232, 121, 5, 1)
)
if mibBuilder.loadTexts:
    cpqnIPTrapDestTable.setStatus("mandatory")
_CpqnIPTrapDestEntry_Object = MibTableRow
cpqnIPTrapDestEntry = _CpqnIPTrapDestEntry_Object(
    (1, 3, 6, 1, 4, 1, 232, 121, 5, 1, 1)
)
cpqnIPTrapDestEntry.setIndexNames(
    (0, "CPQNUNIF-MIB", "cpqnIPTrapDestIndex"),
)
if mibBuilder.loadTexts:
    cpqnIPTrapDestEntry.setStatus("mandatory")
_CpqnIPTrapDestIndex_Type = Integer32
_CpqnIPTrapDestIndex_Object = MibTableColumn
cpqnIPTrapDestIndex = _CpqnIPTrapDestIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 121, 5, 1, 1, 1),
    _CpqnIPTrapDestIndex_Type()
)
cpqnIPTrapDestIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqnIPTrapDestIndex.setStatus("mandatory")
_CpqnIPTrapDestRowStatus_Type = CpqnRowStatus
_CpqnIPTrapDestRowStatus_Object = MibTableColumn
cpqnIPTrapDestRowStatus = _CpqnIPTrapDestRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 232, 121, 5, 1, 1, 2),
    _CpqnIPTrapDestRowStatus_Type()
)
cpqnIPTrapDestRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqnIPTrapDestRowStatus.setStatus("mandatory")


class _CpqnIPTrapDestCommunity_Type(DisplayString):
    """Custom type cpqnIPTrapDestCommunity based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_CpqnIPTrapDestCommunity_Type.__name__ = "DisplayString"
_CpqnIPTrapDestCommunity_Object = MibTableColumn
cpqnIPTrapDestCommunity = _CpqnIPTrapDestCommunity_Object(
    (1, 3, 6, 1, 4, 1, 232, 121, 5, 1, 1, 3),
    _CpqnIPTrapDestCommunity_Type()
)
cpqnIPTrapDestCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqnIPTrapDestCommunity.setStatus("mandatory")
_CpqnIPTrapDestAddress_Type = IpAddress
_CpqnIPTrapDestAddress_Object = MibTableColumn
cpqnIPTrapDestAddress = _CpqnIPTrapDestAddress_Object(
    (1, 3, 6, 1, 4, 1, 232, 121, 5, 1, 1, 4),
    _CpqnIPTrapDestAddress_Type()
)
cpqnIPTrapDestAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqnIPTrapDestAddress.setStatus("mandatory")
_CpqnIPXTrapDestTable_Object = MibTable
cpqnIPXTrapDestTable = _CpqnIPXTrapDestTable_Object(
    (1, 3, 6, 1, 4, 1, 232, 121, 5, 2)
)
if mibBuilder.loadTexts:
    cpqnIPXTrapDestTable.setStatus("mandatory")
_CpqnIPXTrapDestEntry_Object = MibTableRow
cpqnIPXTrapDestEntry = _CpqnIPXTrapDestEntry_Object(
    (1, 3, 6, 1, 4, 1, 232, 121, 5, 2, 1)
)
cpqnIPXTrapDestEntry.setIndexNames(
    (0, "CPQNUNIF-MIB", "cpqnIPXTrapDestIndex"),
)
if mibBuilder.loadTexts:
    cpqnIPXTrapDestEntry.setStatus("mandatory")
_CpqnIPXTrapDestIndex_Type = Integer32
_CpqnIPXTrapDestIndex_Object = MibTableColumn
cpqnIPXTrapDestIndex = _CpqnIPXTrapDestIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 121, 5, 2, 1, 1),
    _CpqnIPXTrapDestIndex_Type()
)
cpqnIPXTrapDestIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqnIPXTrapDestIndex.setStatus("mandatory")
_CpqnIPXTrapDestRowStatus_Type = CpqnRowStatus
_CpqnIPXTrapDestRowStatus_Object = MibTableColumn
cpqnIPXTrapDestRowStatus = _CpqnIPXTrapDestRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 232, 121, 5, 2, 1, 2),
    _CpqnIPXTrapDestRowStatus_Type()
)
cpqnIPXTrapDestRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqnIPXTrapDestRowStatus.setStatus("mandatory")


class _CpqnIPXTrapDestCommunity_Type(DisplayString):
    """Custom type cpqnIPXTrapDestCommunity based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_CpqnIPXTrapDestCommunity_Type.__name__ = "DisplayString"
_CpqnIPXTrapDestCommunity_Object = MibTableColumn
cpqnIPXTrapDestCommunity = _CpqnIPXTrapDestCommunity_Object(
    (1, 3, 6, 1, 4, 1, 232, 121, 5, 2, 1, 3),
    _CpqnIPXTrapDestCommunity_Type()
)
cpqnIPXTrapDestCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqnIPXTrapDestCommunity.setStatus("mandatory")
_CpqnIPXTrapDestAddress_Type = IpxAddress
_CpqnIPXTrapDestAddress_Object = MibTableColumn
cpqnIPXTrapDestAddress = _CpqnIPXTrapDestAddress_Object(
    (1, 3, 6, 1, 4, 1, 232, 121, 5, 2, 1, 4),
    _CpqnIPXTrapDestAddress_Type()
)
cpqnIPXTrapDestAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqnIPXTrapDestAddress.setStatus("mandatory")
_CpqnNetworkInfo_ObjectIdentity = ObjectIdentity
cpqnNetworkInfo = _CpqnNetworkInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 121, 6)
)
_CpqnIpNetworkTable_Object = MibTable
cpqnIpNetworkTable = _CpqnIpNetworkTable_Object(
    (1, 3, 6, 1, 4, 1, 232, 121, 6, 1)
)
if mibBuilder.loadTexts:
    cpqnIpNetworkTable.setStatus("mandatory")
_CpqnIpNetworkEntry_Object = MibTableRow
cpqnIpNetworkEntry = _CpqnIpNetworkEntry_Object(
    (1, 3, 6, 1, 4, 1, 232, 121, 6, 1, 1)
)
cpqnIpNetworkEntry.setIndexNames(
    (0, "CPQNUNIF-MIB", "cpqnIpIfIndex"),
)
if mibBuilder.loadTexts:
    cpqnIpNetworkEntry.setStatus("mandatory")
_CpqnIpIfIndex_Type = Integer32
_CpqnIpIfIndex_Object = MibTableColumn
cpqnIpIfIndex = _CpqnIpIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 121, 6, 1, 1, 1),
    _CpqnIpIfIndex_Type()
)
cpqnIpIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqnIpIfIndex.setStatus("mandatory")
_CpqnIpPhysAddr_Type = PhysAddress
_CpqnIpPhysAddr_Object = MibTableColumn
cpqnIpPhysAddr = _CpqnIpPhysAddr_Object(
    (1, 3, 6, 1, 4, 1, 232, 121, 6, 1, 1, 2),
    _CpqnIpPhysAddr_Type()
)
cpqnIpPhysAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqnIpPhysAddr.setStatus("mandatory")
_CpqnIpAddr_Type = IpAddress
_CpqnIpAddr_Object = MibTableColumn
cpqnIpAddr = _CpqnIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 232, 121, 6, 1, 1, 3),
    _CpqnIpAddr_Type()
)
cpqnIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqnIpAddr.setStatus("mandatory")
_CpqnIpNetMask_Type = IpAddress
_CpqnIpNetMask_Object = MibTableColumn
cpqnIpNetMask = _CpqnIpNetMask_Object(
    (1, 3, 6, 1, 4, 1, 232, 121, 6, 1, 1, 4),
    _CpqnIpNetMask_Type()
)
cpqnIpNetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqnIpNetMask.setStatus("mandatory")
_CpqnIpRouter_Type = IpAddress
_CpqnIpRouter_Object = MibTableColumn
cpqnIpRouter = _CpqnIpRouter_Object(
    (1, 3, 6, 1, 4, 1, 232, 121, 6, 1, 1, 5),
    _CpqnIpRouter_Type()
)
cpqnIpRouter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqnIpRouter.setStatus("mandatory")


class _CpqnIpFrameType_Type(Integer32):
    """Custom type cpqnIpFrameType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ethernet-ii", 2),
          ("ieee-802-2-snap", 3),
          ("not-applicable", 1))
    )


_CpqnIpFrameType_Type.__name__ = "Integer32"
_CpqnIpFrameType_Object = MibTableColumn
cpqnIpFrameType = _CpqnIpFrameType_Object(
    (1, 3, 6, 1, 4, 1, 232, 121, 6, 1, 1, 6),
    _CpqnIpFrameType_Type()
)
cpqnIpFrameType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqnIpFrameType.setStatus("mandatory")


class _CpqnIpAutoDiscoveryStatus_Type(Integer32):
    """Custom type cpqnIpAutoDiscoveryStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("discover", 1),
          ("do-not-discover", 2))
    )


_CpqnIpAutoDiscoveryStatus_Type.__name__ = "Integer32"
_CpqnIpAutoDiscoveryStatus_Object = MibTableColumn
cpqnIpAutoDiscoveryStatus = _CpqnIpAutoDiscoveryStatus_Object(
    (1, 3, 6, 1, 4, 1, 232, 121, 6, 1, 1, 7),
    _CpqnIpAutoDiscoveryStatus_Type()
)
cpqnIpAutoDiscoveryStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqnIpAutoDiscoveryStatus.setStatus("mandatory")


class _CpqnIpPingPktRate_Type(Integer32):
    """Custom type cpqnIpPingPktRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(55, 65535),
    )


_CpqnIpPingPktRate_Type.__name__ = "Integer32"
_CpqnIpPingPktRate_Object = MibTableColumn
cpqnIpPingPktRate = _CpqnIpPingPktRate_Object(
    (1, 3, 6, 1, 4, 1, 232, 121, 6, 1, 1, 8),
    _CpqnIpPingPktRate_Type()
)
cpqnIpPingPktRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqnIpPingPktRate.setStatus("mandatory")


class _CpqnIpInfoSave_Type(Integer32):
    """Custom type cpqnIpInfoSave based on Integer32"""
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
        *(("ignore-changes", 1),
          ("values-changed", 3),
          ("values-valid", 4),
          ("write-changes-to-nvram", 2))
    )


_CpqnIpInfoSave_Type.__name__ = "Integer32"
_CpqnIpInfoSave_Object = MibTableColumn
cpqnIpInfoSave = _CpqnIpInfoSave_Object(
    (1, 3, 6, 1, 4, 1, 232, 121, 6, 1, 1, 9),
    _CpqnIpInfoSave_Type()
)
cpqnIpInfoSave.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqnIpInfoSave.setStatus("mandatory")
_CpqnIpxNetworkTable_Object = MibTable
cpqnIpxNetworkTable = _CpqnIpxNetworkTable_Object(
    (1, 3, 6, 1, 4, 1, 232, 121, 6, 2)
)
if mibBuilder.loadTexts:
    cpqnIpxNetworkTable.setStatus("mandatory")
_CpqnIpxNetworkEntry_Object = MibTableRow
cpqnIpxNetworkEntry = _CpqnIpxNetworkEntry_Object(
    (1, 3, 6, 1, 4, 1, 232, 121, 6, 2, 1)
)
cpqnIpxNetworkEntry.setIndexNames(
    (0, "CPQNUNIF-MIB", "cpqnIpxIfIndex"),
)
if mibBuilder.loadTexts:
    cpqnIpxNetworkEntry.setStatus("mandatory")
_CpqnIpxIfIndex_Type = Integer32
_CpqnIpxIfIndex_Object = MibTableColumn
cpqnIpxIfIndex = _CpqnIpxIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 121, 6, 2, 1, 1),
    _CpqnIpxIfIndex_Type()
)
cpqnIpxIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqnIpxIfIndex.setStatus("mandatory")
_CpqnIpxPhysAddr_Type = PhysAddress
_CpqnIpxPhysAddr_Object = MibTableColumn
cpqnIpxPhysAddr = _CpqnIpxPhysAddr_Object(
    (1, 3, 6, 1, 4, 1, 232, 121, 6, 2, 1, 2),
    _CpqnIpxPhysAddr_Type()
)
cpqnIpxPhysAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqnIpxPhysAddr.setStatus("mandatory")


class _CpqnIpxFrameType_Type(Integer32):
    """Custom type cpqnIpxFrameType based on Integer32"""
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
        *(("ethernet-802-3-raw", 3),
          ("ethernet-ii", 2),
          ("ieee-802-2", 4),
          ("ieee-802-2-snap", 5),
          ("not-applicable", 1))
    )


_CpqnIpxFrameType_Type.__name__ = "Integer32"
_CpqnIpxFrameType_Object = MibTableColumn
cpqnIpxFrameType = _CpqnIpxFrameType_Object(
    (1, 3, 6, 1, 4, 1, 232, 121, 6, 2, 1, 3),
    _CpqnIpxFrameType_Type()
)
cpqnIpxFrameType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqnIpxFrameType.setStatus("mandatory")


class _CpqnIpxNetworkNumber_Type(OctetString):
    """Custom type cpqnIpxNetworkNumber based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_CpqnIpxNetworkNumber_Type.__name__ = "OctetString"
_CpqnIpxNetworkNumber_Object = MibTableColumn
cpqnIpxNetworkNumber = _CpqnIpxNetworkNumber_Object(
    (1, 3, 6, 1, 4, 1, 232, 121, 6, 2, 1, 4),
    _CpqnIpxNetworkNumber_Type()
)
cpqnIpxNetworkNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqnIpxNetworkNumber.setStatus("mandatory")


class _CpqnIpxSAPBcastStatus_Type(Integer32):
    """Custom type cpqnIpxSAPBcastStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("do-ipx-SAPs", 1),
          ("no-ipx-SAPs", 2))
    )


_CpqnIpxSAPBcastStatus_Type.__name__ = "Integer32"
_CpqnIpxSAPBcastStatus_Object = MibTableColumn
cpqnIpxSAPBcastStatus = _CpqnIpxSAPBcastStatus_Object(
    (1, 3, 6, 1, 4, 1, 232, 121, 6, 2, 1, 5),
    _CpqnIpxSAPBcastStatus_Type()
)
cpqnIpxSAPBcastStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqnIpxSAPBcastStatus.setStatus("mandatory")
_CpqnBootpConfig_ObjectIdentity = ObjectIdentity
cpqnBootpConfig = _CpqnBootpConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 121, 7)
)
_CpqnBootpTable_Object = MibTable
cpqnBootpTable = _CpqnBootpTable_Object(
    (1, 3, 6, 1, 4, 1, 232, 121, 7, 1)
)
if mibBuilder.loadTexts:
    cpqnBootpTable.setStatus("mandatory")
_CpqnBootpEntry_Object = MibTableRow
cpqnBootpEntry = _CpqnBootpEntry_Object(
    (1, 3, 6, 1, 4, 1, 232, 121, 7, 1, 1)
)
cpqnBootpEntry.setIndexNames(
    (0, "CPQNUNIF-MIB", "cpqnBootpIfIndex"),
)
if mibBuilder.loadTexts:
    cpqnBootpEntry.setStatus("mandatory")
_CpqnBootpIfIndex_Type = Integer32
_CpqnBootpIfIndex_Object = MibTableColumn
cpqnBootpIfIndex = _CpqnBootpIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 121, 7, 1, 1, 1),
    _CpqnBootpIfIndex_Type()
)
cpqnBootpIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqnBootpIfIndex.setStatus("mandatory")


class _CpqnBootpEnable_Type(Integer32):
    """Custom type cpqnBootpEnable based on Integer32"""
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
        *(("disable-bootp", 1),
          ("enable-bootp-both", 4),
          ("enable-bootp-ethernet-ii", 2),
          ("enable-bootp-ieee-802-2-snap", 3))
    )


_CpqnBootpEnable_Type.__name__ = "Integer32"
_CpqnBootpEnable_Object = MibTableColumn
cpqnBootpEnable = _CpqnBootpEnable_Object(
    (1, 3, 6, 1, 4, 1, 232, 121, 7, 1, 1, 2),
    _CpqnBootpEnable_Type()
)
cpqnBootpEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqnBootpEnable.setStatus("mandatory")


class _CpqnBootpRetries_Type(Integer32):
    """Custom type cpqnBootpRetries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CpqnBootpRetries_Type.__name__ = "Integer32"
_CpqnBootpRetries_Object = MibTableColumn
cpqnBootpRetries = _CpqnBootpRetries_Object(
    (1, 3, 6, 1, 4, 1, 232, 121, 7, 1, 1, 3),
    _CpqnBootpRetries_Type()
)
cpqnBootpRetries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqnBootpRetries.setStatus("mandatory")


class _CpqnBootpRetryInterval_Type(Integer32):
    """Custom type cpqnBootpRetryInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 255),
    )


_CpqnBootpRetryInterval_Type.__name__ = "Integer32"
_CpqnBootpRetryInterval_Object = MibTableColumn
cpqnBootpRetryInterval = _CpqnBootpRetryInterval_Object(
    (1, 3, 6, 1, 4, 1, 232, 121, 7, 1, 1, 4),
    _CpqnBootpRetryInterval_Type()
)
cpqnBootpRetryInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqnBootpRetryInterval.setStatus("mandatory")
_CpqnBootpServerIpAddr_Type = IpAddress
_CpqnBootpServerIpAddr_Object = MibTableColumn
cpqnBootpServerIpAddr = _CpqnBootpServerIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 232, 121, 7, 1, 1, 5),
    _CpqnBootpServerIpAddr_Type()
)
cpqnBootpServerIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqnBootpServerIpAddr.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CPQNUNIF-MIB",
    **{"CpqnRowStatus": CpqnRowStatus,
       "IpxAddress": IpxAddress,
       "CpqnVersionType": CpqnVersionType,
       "CpqnVersionStep": CpqnVersionStep,
       "compaq": compaq,
       "cpqnCommon": cpqnCommon,
       "cpqnMibModules": cpqnMibModules,
       "cpqnMibModuleTable": cpqnMibModuleTable,
       "cpqnMibModuleEntry": cpqnMibModuleEntry,
       "cpqnMibModuleIndex": cpqnMibModuleIndex,
       "cpqnMibModuleDescr": cpqnMibModuleDescr,
       "cpqnMibModuleOid": cpqnMibModuleOid,
       "cpqnUnitControl": cpqnUnitControl,
       "cpqnUnitReset": cpqnUnitReset,
       "cpqnPrimarySerialPort": cpqnPrimarySerialPort,
       "cpqnSerialPortTable": cpqnSerialPortTable,
       "cpqnSerialPortEntry": cpqnSerialPortEntry,
       "cpqnSPortIndex": cpqnSPortIndex,
       "cpqnSPortIfIndex": cpqnSPortIfIndex,
       "cpqnSPortModemInitStringEnable": cpqnSPortModemInitStringEnable,
       "cpqnSPortModemInitString": cpqnSPortModemInitString,
       "cpqnSPortModemAutoNegotiateState": cpqnSPortModemAutoNegotiateState,
       "cpqnSPortBaudRate": cpqnSPortBaudRate,
       "cpqnSupportedBaudRateTable": cpqnSupportedBaudRateTable,
       "cpqnSupportedBaudRateEntry": cpqnSupportedBaudRateEntry,
       "cpqnBaudRatePortIndex": cpqnBaudRatePortIndex,
       "cpqnBaudRateIndex": cpqnBaudRateIndex,
       "cpqnBaudRate": cpqnBaudRate,
       "cpqnVersionInformation": cpqnVersionInformation,
       "cpqnVersionTable": cpqnVersionTable,
       "cpqnVersionEntry": cpqnVersionEntry,
       "cpqnVersionIndex": cpqnVersionIndex,
       "cpqnVersionType": cpqnVersionType,
       "cpqnVersionDesc": cpqnVersionDesc,
       "cpqnVersionMajor": cpqnVersionMajor,
       "cpqnVersionMinor": cpqnVersionMinor,
       "cpqnVersionStep": cpqnVersionStep,
       "cpqnVersionRev": cpqnVersionRev,
       "cpqnVersionSerialNumber": cpqnVersionSerialNumber,
       "cpqnVersionUnitId": cpqnVersionUnitId,
       "cpqnVersionParentIndex": cpqnVersionParentIndex,
       "cpqnAccessControl": cpqnAccessControl,
       "cpqnAclTelnetControl": cpqnAclTelnetControl,
       "cpqnCommunityAccessIPTable": cpqnCommunityAccessIPTable,
       "cpqnCommAccessIPEntry": cpqnCommAccessIPEntry,
       "cpqnAclIPIndex": cpqnAclIPIndex,
       "cpqnAclIPRowStatus": cpqnAclIPRowStatus,
       "cpqnAclIPAddrMask": cpqnAclIPAddrMask,
       "cpqnAclIPAddrMatch": cpqnAclIPAddrMatch,
       "cpqnAclIPCommunity": cpqnAclIPCommunity,
       "cpqnAclIPRights": cpqnAclIPRights,
       "cpqnCommunityAccessIPXTable": cpqnCommunityAccessIPXTable,
       "cpqnCommAccessIPXEntry": cpqnCommAccessIPXEntry,
       "cpqnAclIPXIndex": cpqnAclIPXIndex,
       "cpqnAclIPXRowStatus": cpqnAclIPXRowStatus,
       "cpqnAclIPXAddrMask": cpqnAclIPXAddrMask,
       "cpqnAclIPXAddrMatch": cpqnAclIPXAddrMatch,
       "cpqnAclIPXCommunity": cpqnAclIPXCommunity,
       "cpqnAclIPXRights": cpqnAclIPXRights,
       "cpqnTrapDestinations": cpqnTrapDestinations,
       "cpqnIPTrapDestTable": cpqnIPTrapDestTable,
       "cpqnIPTrapDestEntry": cpqnIPTrapDestEntry,
       "cpqnIPTrapDestIndex": cpqnIPTrapDestIndex,
       "cpqnIPTrapDestRowStatus": cpqnIPTrapDestRowStatus,
       "cpqnIPTrapDestCommunity": cpqnIPTrapDestCommunity,
       "cpqnIPTrapDestAddress": cpqnIPTrapDestAddress,
       "cpqnIPXTrapDestTable": cpqnIPXTrapDestTable,
       "cpqnIPXTrapDestEntry": cpqnIPXTrapDestEntry,
       "cpqnIPXTrapDestIndex": cpqnIPXTrapDestIndex,
       "cpqnIPXTrapDestRowStatus": cpqnIPXTrapDestRowStatus,
       "cpqnIPXTrapDestCommunity": cpqnIPXTrapDestCommunity,
       "cpqnIPXTrapDestAddress": cpqnIPXTrapDestAddress,
       "cpqnNetworkInfo": cpqnNetworkInfo,
       "cpqnIpNetworkTable": cpqnIpNetworkTable,
       "cpqnIpNetworkEntry": cpqnIpNetworkEntry,
       "cpqnIpIfIndex": cpqnIpIfIndex,
       "cpqnIpPhysAddr": cpqnIpPhysAddr,
       "cpqnIpAddr": cpqnIpAddr,
       "cpqnIpNetMask": cpqnIpNetMask,
       "cpqnIpRouter": cpqnIpRouter,
       "cpqnIpFrameType": cpqnIpFrameType,
       "cpqnIpAutoDiscoveryStatus": cpqnIpAutoDiscoveryStatus,
       "cpqnIpPingPktRate": cpqnIpPingPktRate,
       "cpqnIpInfoSave": cpqnIpInfoSave,
       "cpqnIpxNetworkTable": cpqnIpxNetworkTable,
       "cpqnIpxNetworkEntry": cpqnIpxNetworkEntry,
       "cpqnIpxIfIndex": cpqnIpxIfIndex,
       "cpqnIpxPhysAddr": cpqnIpxPhysAddr,
       "cpqnIpxFrameType": cpqnIpxFrameType,
       "cpqnIpxNetworkNumber": cpqnIpxNetworkNumber,
       "cpqnIpxSAPBcastStatus": cpqnIpxSAPBcastStatus,
       "cpqnBootpConfig": cpqnBootpConfig,
       "cpqnBootpTable": cpqnBootpTable,
       "cpqnBootpEntry": cpqnBootpEntry,
       "cpqnBootpIfIndex": cpqnBootpIfIndex,
       "cpqnBootpEnable": cpqnBootpEnable,
       "cpqnBootpRetries": cpqnBootpRetries,
       "cpqnBootpRetryInterval": cpqnBootpRetryInterval,
       "cpqnBootpServerIpAddr": cpqnBootpServerIpAddr}
)
