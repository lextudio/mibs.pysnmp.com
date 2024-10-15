# SNMP MIB module (CISCO-FC-MGMT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-FC-MGMT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:00:14 2024
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

(ciscoExperiment,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoExperiment")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

ciscoFcMgmtMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 999999)
)
ciscoFcMgmtMIB.setRevisions(
        ("2002-09-12 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class CfcmFcNameIdOrZero(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(8, 8),
        ValueSizeConstraint(16, 16),
    )



class CfcmFcAddressId(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(3, 3),
    )



class CfcmDomainIdOrZero(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 239),
    )



class CfcmFcPortType(Integer32, TextualConvention):
    status = "current"
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("bPort", 9),
          ("dynamic", 3),
          ("ePort", 8),
          ("fPort", 6),
          ("flPort", 7),
          ("nPort", 4),
          ("nlPort", 5),
          ("other", 2),
          ("unknown", 1))
    )



class CfcmFcClasses(Bits, TextualConvention):
    status = "current"


class CfcmFcBbCredit(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )



class CfcmFcBbCreditModel(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("alternate", 2),
          ("regular", 1))
    )



class CfcmFcDataFieldSize(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(128, 2112),
    )



class CfcmFcUnitFunctions(Bits, TextualConvention):
    status = "current"


class CfcmPhysicalIndexOrZero(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )



class CfcmHrSWInstalledIndexOrZero(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )



class CfcmMilliSeconds(Unsigned32, TextualConvention):
    status = "current"


class CfcmMicroSeconds(Unsigned32, TextualConvention):
    status = "current"


# MIB Managed Objects in the order of their OIDs

_CfcmgmtObjects_ObjectIdentity = ObjectIdentity
cfcmgmtObjects = _CfcmgmtObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 999999, 1)
)
_CfcmInstanceTable_Object = MibTable
cfcmInstanceTable = _CfcmInstanceTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 999999, 1, 1)
)
if mibBuilder.loadTexts:
    cfcmInstanceTable.setStatus("current")
_CfcmInstanceEntry_Object = MibTableRow
cfcmInstanceEntry = _CfcmInstanceEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 999999, 1, 1, 1)
)
cfcmInstanceEntry.setIndexNames(
    (0, "CISCO-FC-MGMT-MIB", "cfcmInstanceIndex"),
)
if mibBuilder.loadTexts:
    cfcmInstanceEntry.setStatus("current")


class _CfcmInstanceIndex_Type(Unsigned32):
    """Custom type cfcmInstanceIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_CfcmInstanceIndex_Type.__name__ = "Unsigned32"
_CfcmInstanceIndex_Object = MibTableColumn
cfcmInstanceIndex = _CfcmInstanceIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 999999, 1, 1, 1, 1),
    _CfcmInstanceIndex_Type()
)
cfcmInstanceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfcmInstanceIndex.setStatus("current")
_CfcmInstanceWwn_Type = CfcmFcNameIdOrZero
_CfcmInstanceWwn_Object = MibTableColumn
cfcmInstanceWwn = _CfcmInstanceWwn_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 999999, 1, 1, 1, 2),
    _CfcmInstanceWwn_Type()
)
cfcmInstanceWwn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfcmInstanceWwn.setStatus("current")
_CfcmInstanceFunctions_Type = CfcmFcUnitFunctions
_CfcmInstanceFunctions_Object = MibTableColumn
cfcmInstanceFunctions = _CfcmInstanceFunctions_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 999999, 1, 1, 1, 3),
    _CfcmInstanceFunctions_Type()
)
cfcmInstanceFunctions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfcmInstanceFunctions.setStatus("current")
_CfcmInstancePhysicalIndex_Type = CfcmPhysicalIndexOrZero
_CfcmInstancePhysicalIndex_Object = MibTableColumn
cfcmInstancePhysicalIndex = _CfcmInstancePhysicalIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 999999, 1, 1, 1, 4),
    _CfcmInstancePhysicalIndex_Type()
)
cfcmInstancePhysicalIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfcmInstancePhysicalIndex.setStatus("current")
_CfcmInstanceSoftwareIndex_Type = CfcmHrSWInstalledIndexOrZero
_CfcmInstanceSoftwareIndex_Object = MibTableColumn
cfcmInstanceSoftwareIndex = _CfcmInstanceSoftwareIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 999999, 1, 1, 1, 5),
    _CfcmInstanceSoftwareIndex_Type()
)
cfcmInstanceSoftwareIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfcmInstanceSoftwareIndex.setStatus("current")


class _CfcmInstanceStatus_Type(Integer32):
    """Custom type cfcmInstanceStatus based on Integer32"""
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
        *(("failed", 4),
          ("ok", 2),
          ("unknown", 1),
          ("warning", 3))
    )


_CfcmInstanceStatus_Type.__name__ = "Integer32"
_CfcmInstanceStatus_Object = MibTableColumn
cfcmInstanceStatus = _CfcmInstanceStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 999999, 1, 1, 1, 6),
    _CfcmInstanceStatus_Type()
)
cfcmInstanceStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfcmInstanceStatus.setStatus("current")


class _CfcmInstanceTextName_Type(SnmpAdminString):
    """Custom type cfcmInstanceTextName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 79),
    )


_CfcmInstanceTextName_Type.__name__ = "SnmpAdminString"
_CfcmInstanceTextName_Object = MibTableColumn
cfcmInstanceTextName = _CfcmInstanceTextName_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 999999, 1, 1, 1, 7),
    _CfcmInstanceTextName_Type()
)
cfcmInstanceTextName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfcmInstanceTextName.setStatus("current")
_CfcmInstanceDescr_Type = SnmpAdminString
_CfcmInstanceDescr_Object = MibTableColumn
cfcmInstanceDescr = _CfcmInstanceDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 999999, 1, 1, 1, 8),
    _CfcmInstanceDescr_Type()
)
cfcmInstanceDescr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfcmInstanceDescr.setStatus("current")
_CfcmInstanceFabricId_Type = CfcmFcNameIdOrZero
_CfcmInstanceFabricId_Object = MibTableColumn
cfcmInstanceFabricId = _CfcmInstanceFabricId_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 999999, 1, 1, 1, 9),
    _CfcmInstanceFabricId_Type()
)
cfcmInstanceFabricId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfcmInstanceFabricId.setStatus("current")
_CfcmSwitchTable_Object = MibTable
cfcmSwitchTable = _CfcmSwitchTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 999999, 1, 2)
)
if mibBuilder.loadTexts:
    cfcmSwitchTable.setStatus("current")
_CfcmSwitchEntry_Object = MibTableRow
cfcmSwitchEntry = _CfcmSwitchEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 999999, 1, 2, 1)
)
cfcmSwitchEntry.setIndexNames(
    (0, "CISCO-FC-MGMT-MIB", "cfcmInstanceIndex"),
    (0, "CISCO-FC-MGMT-MIB", "cfcmSwitchIndex"),
)
if mibBuilder.loadTexts:
    cfcmSwitchEntry.setStatus("current")


class _CfcmSwitchIndex_Type(Unsigned32):
    """Custom type cfcmSwitchIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_CfcmSwitchIndex_Type.__name__ = "Unsigned32"
_CfcmSwitchIndex_Object = MibTableColumn
cfcmSwitchIndex = _CfcmSwitchIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 999999, 1, 2, 1, 1),
    _CfcmSwitchIndex_Type()
)
cfcmSwitchIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfcmSwitchIndex.setStatus("current")
_CfcmSwitchDomainId_Type = CfcmDomainIdOrZero
_CfcmSwitchDomainId_Object = MibTableColumn
cfcmSwitchDomainId = _CfcmSwitchDomainId_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 999999, 1, 2, 1, 2),
    _CfcmSwitchDomainId_Type()
)
cfcmSwitchDomainId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfcmSwitchDomainId.setStatus("current")
_CfcmSwitchPrincipal_Type = TruthValue
_CfcmSwitchPrincipal_Object = MibTableColumn
cfcmSwitchPrincipal = _CfcmSwitchPrincipal_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 999999, 1, 2, 1, 3),
    _CfcmSwitchPrincipal_Type()
)
cfcmSwitchPrincipal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfcmSwitchPrincipal.setStatus("current")
_CfcmPortTable_Object = MibTable
cfcmPortTable = _CfcmPortTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 999999, 1, 3)
)
if mibBuilder.loadTexts:
    cfcmPortTable.setStatus("current")
_CfcmPortEntry_Object = MibTableRow
cfcmPortEntry = _CfcmPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 999999, 1, 3, 1)
)
cfcmPortEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    cfcmPortEntry.setStatus("current")


class _CfcmPortInstanceIndex_Type(Unsigned32):
    """Custom type cfcmPortInstanceIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_CfcmPortInstanceIndex_Type.__name__ = "Unsigned32"
_CfcmPortInstanceIndex_Object = MibTableColumn
cfcmPortInstanceIndex = _CfcmPortInstanceIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 999999, 1, 3, 1, 1),
    _CfcmPortInstanceIndex_Type()
)
cfcmPortInstanceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfcmPortInstanceIndex.setStatus("current")
_CfcmPortWwn_Type = CfcmFcNameIdOrZero
_CfcmPortWwn_Object = MibTableColumn
cfcmPortWwn = _CfcmPortWwn_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 999999, 1, 3, 1, 2),
    _CfcmPortWwn_Type()
)
cfcmPortWwn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfcmPortWwn.setStatus("current")
_CfcmPortNodeWwn_Type = CfcmFcNameIdOrZero
_CfcmPortNodeWwn_Object = MibTableColumn
cfcmPortNodeWwn = _CfcmPortNodeWwn_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 999999, 1, 3, 1, 3),
    _CfcmPortNodeWwn_Type()
)
cfcmPortNodeWwn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfcmPortNodeWwn.setStatus("current")
_CfcmPortAdminType_Type = CfcmFcPortType
_CfcmPortAdminType_Object = MibTableColumn
cfcmPortAdminType = _CfcmPortAdminType_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 999999, 1, 3, 1, 4),
    _CfcmPortAdminType_Type()
)
cfcmPortAdminType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfcmPortAdminType.setStatus("current")
_CfcmPortOperType_Type = CfcmFcPortType
_CfcmPortOperType_Object = MibTableColumn
cfcmPortOperType = _CfcmPortOperType_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 999999, 1, 3, 1, 5),
    _CfcmPortOperType_Type()
)
cfcmPortOperType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfcmPortOperType.setStatus("current")
_CfcmPortFcCapClass_Type = CfcmFcClasses
_CfcmPortFcCapClass_Object = MibTableColumn
cfcmPortFcCapClass = _CfcmPortFcCapClass_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 999999, 1, 3, 1, 6),
    _CfcmPortFcCapClass_Type()
)
cfcmPortFcCapClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfcmPortFcCapClass.setStatus("current")
_CfcmPortFcOperClass_Type = CfcmFcClasses
_CfcmPortFcOperClass_Object = MibTableColumn
cfcmPortFcOperClass = _CfcmPortFcOperClass_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 999999, 1, 3, 1, 7),
    _CfcmPortFcOperClass_Type()
)
cfcmPortFcOperClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfcmPortFcOperClass.setStatus("current")


class _CfcmPortTransmitterType_Type(Integer32):
    """Custom type cfcmPortTransmitterType based on Integer32"""
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
        *(("electrical", 6),
          ("longwave1310nm", 5),
          ("longwave1550nm", 4),
          ("other", 2),
          ("shortwave850nm", 3),
          ("unknown", 1))
    )


_CfcmPortTransmitterType_Type.__name__ = "Integer32"
_CfcmPortTransmitterType_Object = MibTableColumn
cfcmPortTransmitterType = _CfcmPortTransmitterType_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 999999, 1, 3, 1, 8),
    _CfcmPortTransmitterType_Type()
)
cfcmPortTransmitterType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfcmPortTransmitterType.setStatus("current")


class _CfcmPortConnectorType_Type(Integer32):
    """Custom type cfcmPortConnectorType based on Integer32"""
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("embedded", 4),
          ("gbic", 3),
          ("gbicNoSerialId", 7),
          ("gbicSerialId", 6),
          ("glm", 5),
          ("other", 2),
          ("sfpNoSerialId", 9),
          ("sfpSerialId", 8),
          ("unknown", 1))
    )


_CfcmPortConnectorType_Type.__name__ = "Integer32"
_CfcmPortConnectorType_Object = MibTableColumn
cfcmPortConnectorType = _CfcmPortConnectorType_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 999999, 1, 3, 1, 9),
    _CfcmPortConnectorType_Type()
)
cfcmPortConnectorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfcmPortConnectorType.setStatus("current")
_CfcmPortSerialNumber_Type = SnmpAdminString
_CfcmPortSerialNumber_Object = MibTableColumn
cfcmPortSerialNumber = _CfcmPortSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 999999, 1, 3, 1, 10),
    _CfcmPortSerialNumber_Type()
)
cfcmPortSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfcmPortSerialNumber.setStatus("current")
_CfcmPortPhysicalNumber_Type = Unsigned32
_CfcmPortPhysicalNumber_Object = MibTableColumn
cfcmPortPhysicalNumber = _CfcmPortPhysicalNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 999999, 1, 3, 1, 11),
    _CfcmPortPhysicalNumber_Type()
)
cfcmPortPhysicalNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfcmPortPhysicalNumber.setStatus("current")


class _CfcmPortAdminSpeed_Type(Integer32):
    """Custom type cfcmPortAdminSpeed based on Integer32"""
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
        *(("auto", 1),
          ("eighthGbs", 2),
          ("fourGbs", 7),
          ("halfGbs", 4),
          ("oneGbs", 5),
          ("quarterGbs", 3),
          ("tenGbs", 8),
          ("twoGbs", 6))
    )


_CfcmPortAdminSpeed_Type.__name__ = "Integer32"
_CfcmPortAdminSpeed_Object = MibTableColumn
cfcmPortAdminSpeed = _CfcmPortAdminSpeed_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 999999, 1, 3, 1, 12),
    _CfcmPortAdminSpeed_Type()
)
cfcmPortAdminSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfcmPortAdminSpeed.setStatus("current")


class _CfcmPortCapProtocols_Type(Bits):
    """Custom type cfcmPortCapProtocols based on Bits"""
    namedValues = NamedValues(
        *(("fabric", 2),
          ("ficon", 6),
          ("loop", 1),
          ("scsi", 3),
          ("tcpIp", 4),
          ("unknown", 0),
          ("vi", 5))
    )

_CfcmPortCapProtocols_Type.__name__ = "Bits"
_CfcmPortCapProtocols_Object = MibTableColumn
cfcmPortCapProtocols = _CfcmPortCapProtocols_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 999999, 1, 3, 1, 13),
    _CfcmPortCapProtocols_Type()
)
cfcmPortCapProtocols.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfcmPortCapProtocols.setStatus("current")


class _CfcmPortOperProtocols_Type(Bits):
    """Custom type cfcmPortOperProtocols based on Bits"""
    namedValues = NamedValues(
        *(("fabric", 2),
          ("ficon", 6),
          ("loop", 1),
          ("scsi", 3),
          ("tcpIp", 4),
          ("unknown", 0),
          ("vi", 5))
    )

_CfcmPortOperProtocols_Type.__name__ = "Bits"
_CfcmPortOperProtocols_Object = MibTableColumn
cfcmPortOperProtocols = _CfcmPortOperProtocols_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 999999, 1, 3, 1, 14),
    _CfcmPortOperProtocols_Type()
)
cfcmPortOperProtocols.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfcmPortOperProtocols.setStatus("current")
_CfcmPortStatsTable_Object = MibTable
cfcmPortStatsTable = _CfcmPortStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 999999, 1, 4)
)
if mibBuilder.loadTexts:
    cfcmPortStatsTable.setStatus("current")
_CfcmPortStatsEntry_Object = MibTableRow
cfcmPortStatsEntry = _CfcmPortStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 999999, 1, 4, 1)
)
if mibBuilder.loadTexts:
    cfcmPortStatsEntry.setStatus("current")
_CfcmPortBBCreditZeros_Type = Counter64
_CfcmPortBBCreditZeros_Object = MibTableColumn
cfcmPortBBCreditZeros = _CfcmPortBBCreditZeros_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 999999, 1, 4, 1, 1),
    _CfcmPortBBCreditZeros_Type()
)
cfcmPortBBCreditZeros.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfcmPortBBCreditZeros.setStatus("current")
_CfcmPortFullInputBuffers_Type = Counter64
_CfcmPortFullInputBuffers_Object = MibTableColumn
cfcmPortFullInputBuffers = _CfcmPortFullInputBuffers_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 999999, 1, 4, 1, 2),
    _CfcmPortFullInputBuffers_Type()
)
cfcmPortFullInputBuffers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfcmPortFullInputBuffers.setStatus("current")
_CfcmPortClass2RxFrames_Type = Counter64
_CfcmPortClass2RxFrames_Object = MibTableColumn
cfcmPortClass2RxFrames = _CfcmPortClass2RxFrames_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 999999, 1, 4, 1, 3),
    _CfcmPortClass2RxFrames_Type()
)
cfcmPortClass2RxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfcmPortClass2RxFrames.setStatus("current")
_CfcmPortClass2RxOctets_Type = Counter64
_CfcmPortClass2RxOctets_Object = MibTableColumn
cfcmPortClass2RxOctets = _CfcmPortClass2RxOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 999999, 1, 4, 1, 4),
    _CfcmPortClass2RxOctets_Type()
)
cfcmPortClass2RxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfcmPortClass2RxOctets.setStatus("current")
_CfcmPortClass2TxFrames_Type = Counter64
_CfcmPortClass2TxFrames_Object = MibTableColumn
cfcmPortClass2TxFrames = _CfcmPortClass2TxFrames_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 999999, 1, 4, 1, 5),
    _CfcmPortClass2TxFrames_Type()
)
cfcmPortClass2TxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfcmPortClass2TxFrames.setStatus("current")
_CfcmPortClass2TxOctets_Type = Counter64
_CfcmPortClass2TxOctets_Object = MibTableColumn
cfcmPortClass2TxOctets = _CfcmPortClass2TxOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 999999, 1, 4, 1, 6),
    _CfcmPortClass2TxOctets_Type()
)
cfcmPortClass2TxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfcmPortClass2TxOctets.setStatus("current")
_CfcmPortClass2Discards_Type = Counter64
_CfcmPortClass2Discards_Object = MibTableColumn
cfcmPortClass2Discards = _CfcmPortClass2Discards_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 999999, 1, 4, 1, 7),
    _CfcmPortClass2Discards_Type()
)
cfcmPortClass2Discards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfcmPortClass2Discards.setStatus("current")
_CfcmPortClass2RxFbsyFrames_Type = Counter64
_CfcmPortClass2RxFbsyFrames_Object = MibTableColumn
cfcmPortClass2RxFbsyFrames = _CfcmPortClass2RxFbsyFrames_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 999999, 1, 4, 1, 8),
    _CfcmPortClass2RxFbsyFrames_Type()
)
cfcmPortClass2RxFbsyFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfcmPortClass2RxFbsyFrames.setStatus("current")
_CfcmPortClass2RxPbsyFrames_Type = Counter64
_CfcmPortClass2RxPbsyFrames_Object = MibTableColumn
cfcmPortClass2RxPbsyFrames = _CfcmPortClass2RxPbsyFrames_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 999999, 1, 4, 1, 9),
    _CfcmPortClass2RxPbsyFrames_Type()
)
cfcmPortClass2RxPbsyFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfcmPortClass2RxPbsyFrames.setStatus("current")
_CfcmPortClass2RxFrjtFrames_Type = Counter64
_CfcmPortClass2RxFrjtFrames_Object = MibTableColumn
cfcmPortClass2RxFrjtFrames = _CfcmPortClass2RxFrjtFrames_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 999999, 1, 4, 1, 10),
    _CfcmPortClass2RxFrjtFrames_Type()
)
cfcmPortClass2RxFrjtFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfcmPortClass2RxFrjtFrames.setStatus("current")
_CfcmPortClass2RxPrjtFrames_Type = Counter64
_CfcmPortClass2RxPrjtFrames_Object = MibTableColumn
cfcmPortClass2RxPrjtFrames = _CfcmPortClass2RxPrjtFrames_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 999999, 1, 4, 1, 11),
    _CfcmPortClass2RxPrjtFrames_Type()
)
cfcmPortClass2RxPrjtFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfcmPortClass2RxPrjtFrames.setStatus("current")
_CfcmPortClass2TxFbsyFrames_Type = Counter64
_CfcmPortClass2TxFbsyFrames_Object = MibTableColumn
cfcmPortClass2TxFbsyFrames = _CfcmPortClass2TxFbsyFrames_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 999999, 1, 4, 1, 12),
    _CfcmPortClass2TxFbsyFrames_Type()
)
cfcmPortClass2TxFbsyFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfcmPortClass2TxFbsyFrames.setStatus("current")
_CfcmPortClass2TxPbsyFrames_Type = Counter64
_CfcmPortClass2TxPbsyFrames_Object = MibTableColumn
cfcmPortClass2TxPbsyFrames = _CfcmPortClass2TxPbsyFrames_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 999999, 1, 4, 1, 13),
    _CfcmPortClass2TxPbsyFrames_Type()
)
cfcmPortClass2TxPbsyFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfcmPortClass2TxPbsyFrames.setStatus("current")
_CfcmPortClass2TxFrjtFrames_Type = Counter64
_CfcmPortClass2TxFrjtFrames_Object = MibTableColumn
cfcmPortClass2TxFrjtFrames = _CfcmPortClass2TxFrjtFrames_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 999999, 1, 4, 1, 14),
    _CfcmPortClass2TxFrjtFrames_Type()
)
cfcmPortClass2TxFrjtFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfcmPortClass2TxFrjtFrames.setStatus("current")
_CfcmPortClass2TxPrjtFrames_Type = Counter64
_CfcmPortClass2TxPrjtFrames_Object = MibTableColumn
cfcmPortClass2TxPrjtFrames = _CfcmPortClass2TxPrjtFrames_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 999999, 1, 4, 1, 15),
    _CfcmPortClass2TxPrjtFrames_Type()
)
cfcmPortClass2TxPrjtFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfcmPortClass2TxPrjtFrames.setStatus("current")
_CfcmPortClass3RxFrames_Type = Counter64
_CfcmPortClass3RxFrames_Object = MibTableColumn
cfcmPortClass3RxFrames = _CfcmPortClass3RxFrames_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 999999, 1, 4, 1, 16),
    _CfcmPortClass3RxFrames_Type()
)
cfcmPortClass3RxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfcmPortClass3RxFrames.setStatus("current")
_CfcmPortClass3RxOctets_Type = Counter64
_CfcmPortClass3RxOctets_Object = MibTableColumn
cfcmPortClass3RxOctets = _CfcmPortClass3RxOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 999999, 1, 4, 1, 17),
    _CfcmPortClass3RxOctets_Type()
)
cfcmPortClass3RxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfcmPortClass3RxOctets.setStatus("current")
_CfcmPortClass3TxFrames_Type = Counter64
_CfcmPortClass3TxFrames_Object = MibTableColumn
cfcmPortClass3TxFrames = _CfcmPortClass3TxFrames_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 999999, 1, 4, 1, 18),
    _CfcmPortClass3TxFrames_Type()
)
cfcmPortClass3TxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfcmPortClass3TxFrames.setStatus("current")
_CfcmPortClass3TxOctets_Type = Counter64
_CfcmPortClass3TxOctets_Object = MibTableColumn
cfcmPortClass3TxOctets = _CfcmPortClass3TxOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 999999, 1, 4, 1, 19),
    _CfcmPortClass3TxOctets_Type()
)
cfcmPortClass3TxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfcmPortClass3TxOctets.setStatus("current")
_CfcmPortClass3Discards_Type = Counter64
_CfcmPortClass3Discards_Object = MibTableColumn
cfcmPortClass3Discards = _CfcmPortClass3Discards_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 999999, 1, 4, 1, 20),
    _CfcmPortClass3Discards_Type()
)
cfcmPortClass3Discards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfcmPortClass3Discards.setStatus("current")
_CfcmPortClassFRxFrames_Type = Counter32
_CfcmPortClassFRxFrames_Object = MibTableColumn
cfcmPortClassFRxFrames = _CfcmPortClassFRxFrames_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 999999, 1, 4, 1, 21),
    _CfcmPortClassFRxFrames_Type()
)
cfcmPortClassFRxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfcmPortClassFRxFrames.setStatus("current")
_CfcmPortClassFRxOctets_Type = Counter32
_CfcmPortClassFRxOctets_Object = MibTableColumn
cfcmPortClassFRxOctets = _CfcmPortClassFRxOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 999999, 1, 4, 1, 22),
    _CfcmPortClassFRxOctets_Type()
)
cfcmPortClassFRxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfcmPortClassFRxOctets.setStatus("current")
_CfcmPortClassFTxFrames_Type = Counter32
_CfcmPortClassFTxFrames_Object = MibTableColumn
cfcmPortClassFTxFrames = _CfcmPortClassFTxFrames_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 999999, 1, 4, 1, 23),
    _CfcmPortClassFTxFrames_Type()
)
cfcmPortClassFTxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfcmPortClassFTxFrames.setStatus("current")
_CfcmPortClassFTxOctets_Type = Counter32
_CfcmPortClassFTxOctets_Object = MibTableColumn
cfcmPortClassFTxOctets = _CfcmPortClassFTxOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 999999, 1, 4, 1, 24),
    _CfcmPortClassFTxOctets_Type()
)
cfcmPortClassFTxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfcmPortClassFTxOctets.setStatus("current")
_CfcmPortClassFDiscards_Type = Counter32
_CfcmPortClassFDiscards_Object = MibTableColumn
cfcmPortClassFDiscards = _CfcmPortClassFDiscards_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 999999, 1, 4, 1, 25),
    _CfcmPortClassFDiscards_Type()
)
cfcmPortClassFDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfcmPortClassFDiscards.setStatus("current")
_CfcmPortLcStatsTable_Object = MibTable
cfcmPortLcStatsTable = _CfcmPortLcStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 999999, 1, 5)
)
if mibBuilder.loadTexts:
    cfcmPortLcStatsTable.setStatus("current")
_CfcmPortLcStatsEntry_Object = MibTableRow
cfcmPortLcStatsEntry = _CfcmPortLcStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 999999, 1, 5, 1)
)
if mibBuilder.loadTexts:
    cfcmPortLcStatsEntry.setStatus("current")
_CfcmPortLcBBCreditZeros_Type = Counter32
_CfcmPortLcBBCreditZeros_Object = MibTableColumn
cfcmPortLcBBCreditZeros = _CfcmPortLcBBCreditZeros_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 999999, 1, 5, 1, 1),
    _CfcmPortLcBBCreditZeros_Type()
)
cfcmPortLcBBCreditZeros.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfcmPortLcBBCreditZeros.setStatus("current")
_CfcmPortLcFullInputBuffers_Type = Counter32
_CfcmPortLcFullInputBuffers_Object = MibTableColumn
cfcmPortLcFullInputBuffers = _CfcmPortLcFullInputBuffers_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 999999, 1, 5, 1, 2),
    _CfcmPortLcFullInputBuffers_Type()
)
cfcmPortLcFullInputBuffers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfcmPortLcFullInputBuffers.setStatus("current")
_CfcmPortLcClass2RxFrames_Type = Counter32
_CfcmPortLcClass2RxFrames_Object = MibTableColumn
cfcmPortLcClass2RxFrames = _CfcmPortLcClass2RxFrames_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 999999, 1, 5, 1, 3),
    _CfcmPortLcClass2RxFrames_Type()
)
cfcmPortLcClass2RxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfcmPortLcClass2RxFrames.setStatus("current")
_CfcmPortLcClass2RxOctets_Type = Counter32
_CfcmPortLcClass2RxOctets_Object = MibTableColumn
cfcmPortLcClass2RxOctets = _CfcmPortLcClass2RxOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 999999, 1, 5, 1, 4),
    _CfcmPortLcClass2RxOctets_Type()
)
cfcmPortLcClass2RxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfcmPortLcClass2RxOctets.setStatus("current")
_CfcmPortLcClass2TxFrames_Type = Counter32
_CfcmPortLcClass2TxFrames_Object = MibTableColumn
cfcmPortLcClass2TxFrames = _CfcmPortLcClass2TxFrames_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 999999, 1, 5, 1, 5),
    _CfcmPortLcClass2TxFrames_Type()
)
cfcmPortLcClass2TxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfcmPortLcClass2TxFrames.setStatus("current")
_CfcmPortLcClass2TxOctets_Type = Counter32
_CfcmPortLcClass2TxOctets_Object = MibTableColumn
cfcmPortLcClass2TxOctets = _CfcmPortLcClass2TxOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 999999, 1, 5, 1, 6),
    _CfcmPortLcClass2TxOctets_Type()
)
cfcmPortLcClass2TxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfcmPortLcClass2TxOctets.setStatus("current")
_CfcmPortLcClass2Discards_Type = Counter32
_CfcmPortLcClass2Discards_Object = MibTableColumn
cfcmPortLcClass2Discards = _CfcmPortLcClass2Discards_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 999999, 1, 5, 1, 7),
    _CfcmPortLcClass2Discards_Type()
)
cfcmPortLcClass2Discards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfcmPortLcClass2Discards.setStatus("current")
_CfcmPortLcClass2RxFbsyFrames_Type = Counter32
_CfcmPortLcClass2RxFbsyFrames_Object = MibTableColumn
cfcmPortLcClass2RxFbsyFrames = _CfcmPortLcClass2RxFbsyFrames_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 999999, 1, 5, 1, 8),
    _CfcmPortLcClass2RxFbsyFrames_Type()
)
cfcmPortLcClass2RxFbsyFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfcmPortLcClass2RxFbsyFrames.setStatus("current")
_CfcmPortLcClass2RxPbsyFrames_Type = Counter32
_CfcmPortLcClass2RxPbsyFrames_Object = MibTableColumn
cfcmPortLcClass2RxPbsyFrames = _CfcmPortLcClass2RxPbsyFrames_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 999999, 1, 5, 1, 9),
    _CfcmPortLcClass2RxPbsyFrames_Type()
)
cfcmPortLcClass2RxPbsyFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfcmPortLcClass2RxPbsyFrames.setStatus("current")
_CfcmPortLcClass2RxFrjtFrames_Type = Counter32
_CfcmPortLcClass2RxFrjtFrames_Object = MibTableColumn
cfcmPortLcClass2RxFrjtFrames = _CfcmPortLcClass2RxFrjtFrames_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 999999, 1, 5, 1, 10),
    _CfcmPortLcClass2RxFrjtFrames_Type()
)
cfcmPortLcClass2RxFrjtFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfcmPortLcClass2RxFrjtFrames.setStatus("current")
_CfcmPortLcClass2RxPrjtFrames_Type = Counter32
_CfcmPortLcClass2RxPrjtFrames_Object = MibTableColumn
cfcmPortLcClass2RxPrjtFrames = _CfcmPortLcClass2RxPrjtFrames_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 999999, 1, 5, 1, 11),
    _CfcmPortLcClass2RxPrjtFrames_Type()
)
cfcmPortLcClass2RxPrjtFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfcmPortLcClass2RxPrjtFrames.setStatus("current")
_CfcmPortLcClass2TxFbsyFrames_Type = Counter32
_CfcmPortLcClass2TxFbsyFrames_Object = MibTableColumn
cfcmPortLcClass2TxFbsyFrames = _CfcmPortLcClass2TxFbsyFrames_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 999999, 1, 5, 1, 12),
    _CfcmPortLcClass2TxFbsyFrames_Type()
)
cfcmPortLcClass2TxFbsyFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfcmPortLcClass2TxFbsyFrames.setStatus("current")
_CfcmPortLcClass2TxPbsyFrames_Type = Counter32
_CfcmPortLcClass2TxPbsyFrames_Object = MibTableColumn
cfcmPortLcClass2TxPbsyFrames = _CfcmPortLcClass2TxPbsyFrames_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 999999, 1, 5, 1, 13),
    _CfcmPortLcClass2TxPbsyFrames_Type()
)
cfcmPortLcClass2TxPbsyFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfcmPortLcClass2TxPbsyFrames.setStatus("current")
_CfcmPortLcClass2TxFrjtFrames_Type = Counter32
_CfcmPortLcClass2TxFrjtFrames_Object = MibTableColumn
cfcmPortLcClass2TxFrjtFrames = _CfcmPortLcClass2TxFrjtFrames_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 999999, 1, 5, 1, 14),
    _CfcmPortLcClass2TxFrjtFrames_Type()
)
cfcmPortLcClass2TxFrjtFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfcmPortLcClass2TxFrjtFrames.setStatus("current")
_CfcmPortLcClass2TxPrjtFrames_Type = Counter32
_CfcmPortLcClass2TxPrjtFrames_Object = MibTableColumn
cfcmPortLcClass2TxPrjtFrames = _CfcmPortLcClass2TxPrjtFrames_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 999999, 1, 5, 1, 15),
    _CfcmPortLcClass2TxPrjtFrames_Type()
)
cfcmPortLcClass2TxPrjtFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfcmPortLcClass2TxPrjtFrames.setStatus("current")
_CfcmPortLcClass3RxFrames_Type = Counter32
_CfcmPortLcClass3RxFrames_Object = MibTableColumn
cfcmPortLcClass3RxFrames = _CfcmPortLcClass3RxFrames_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 999999, 1, 5, 1, 16),
    _CfcmPortLcClass3RxFrames_Type()
)
cfcmPortLcClass3RxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfcmPortLcClass3RxFrames.setStatus("current")
_CfcmPortLcClass3RxOctets_Type = Counter32
_CfcmPortLcClass3RxOctets_Object = MibTableColumn
cfcmPortLcClass3RxOctets = _CfcmPortLcClass3RxOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 999999, 1, 5, 1, 17),
    _CfcmPortLcClass3RxOctets_Type()
)
cfcmPortLcClass3RxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfcmPortLcClass3RxOctets.setStatus("current")
_CfcmPortLcClass3TxFrames_Type = Counter32
_CfcmPortLcClass3TxFrames_Object = MibTableColumn
cfcmPortLcClass3TxFrames = _CfcmPortLcClass3TxFrames_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 999999, 1, 5, 1, 18),
    _CfcmPortLcClass3TxFrames_Type()
)
cfcmPortLcClass3TxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfcmPortLcClass3TxFrames.setStatus("current")
_CfcmPortLcClass3TxOctets_Type = Counter32
_CfcmPortLcClass3TxOctets_Object = MibTableColumn
cfcmPortLcClass3TxOctets = _CfcmPortLcClass3TxOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 999999, 1, 5, 1, 19),
    _CfcmPortLcClass3TxOctets_Type()
)
cfcmPortLcClass3TxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfcmPortLcClass3TxOctets.setStatus("current")
_CfcmPortLcClass3Discards_Type = Counter32
_CfcmPortLcClass3Discards_Object = MibTableColumn
cfcmPortLcClass3Discards = _CfcmPortLcClass3Discards_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 999999, 1, 5, 1, 20),
    _CfcmPortLcClass3Discards_Type()
)
cfcmPortLcClass3Discards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfcmPortLcClass3Discards.setStatus("current")
_CfcmPortErrorsTable_Object = MibTable
cfcmPortErrorsTable = _CfcmPortErrorsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 999999, 1, 6)
)
if mibBuilder.loadTexts:
    cfcmPortErrorsTable.setStatus("current")
_CfcmPortErrorsEntry_Object = MibTableRow
cfcmPortErrorsEntry = _CfcmPortErrorsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 999999, 1, 6, 1)
)
if mibBuilder.loadTexts:
    cfcmPortErrorsEntry.setStatus("current")
_CfcmPortRxLinkResets_Type = Counter32
_CfcmPortRxLinkResets_Object = MibTableColumn
cfcmPortRxLinkResets = _CfcmPortRxLinkResets_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 999999, 1, 6, 1, 1),
    _CfcmPortRxLinkResets_Type()
)
cfcmPortRxLinkResets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfcmPortRxLinkResets.setStatus("current")
_CfcmPortTxLinkResets_Type = Counter32
_CfcmPortTxLinkResets_Object = MibTableColumn
cfcmPortTxLinkResets = _CfcmPortTxLinkResets_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 999999, 1, 6, 1, 2),
    _CfcmPortTxLinkResets_Type()
)
cfcmPortTxLinkResets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfcmPortTxLinkResets.setStatus("current")
_CfcmPortLinkResets_Type = Counter32
_CfcmPortLinkResets_Object = MibTableColumn
cfcmPortLinkResets = _CfcmPortLinkResets_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 999999, 1, 6, 1, 3),
    _CfcmPortLinkResets_Type()
)
cfcmPortLinkResets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfcmPortLinkResets.setStatus("current")
_CfcmPortRxOfflineSequences_Type = Counter32
_CfcmPortRxOfflineSequences_Object = MibTableColumn
cfcmPortRxOfflineSequences = _CfcmPortRxOfflineSequences_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 999999, 1, 6, 1, 4),
    _CfcmPortRxOfflineSequences_Type()
)
cfcmPortRxOfflineSequences.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfcmPortRxOfflineSequences.setStatus("current")
_CfcmPortTxOfflineSequences_Type = Counter32
_CfcmPortTxOfflineSequences_Object = MibTableColumn
cfcmPortTxOfflineSequences = _CfcmPortTxOfflineSequences_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 999999, 1, 6, 1, 5),
    _CfcmPortTxOfflineSequences_Type()
)
cfcmPortTxOfflineSequences.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfcmPortTxOfflineSequences.setStatus("current")
_CfcmPortLinkFailures_Type = Counter32
_CfcmPortLinkFailures_Object = MibTableColumn
cfcmPortLinkFailures = _CfcmPortLinkFailures_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 999999, 1, 6, 1, 6),
    _CfcmPortLinkFailures_Type()
)
cfcmPortLinkFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfcmPortLinkFailures.setStatus("current")
_CfcmPortLossofSynchs_Type = Counter32
_CfcmPortLossofSynchs_Object = MibTableColumn
cfcmPortLossofSynchs = _CfcmPortLossofSynchs_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 999999, 1, 6, 1, 7),
    _CfcmPortLossofSynchs_Type()
)
cfcmPortLossofSynchs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfcmPortLossofSynchs.setStatus("current")
_CfcmPortLossofSignals_Type = Counter32
_CfcmPortLossofSignals_Object = MibTableColumn
cfcmPortLossofSignals = _CfcmPortLossofSignals_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 999999, 1, 6, 1, 8),
    _CfcmPortLossofSignals_Type()
)
cfcmPortLossofSignals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfcmPortLossofSignals.setStatus("current")
_CfcmPortPrimSeqProtocolErrors_Type = Counter32
_CfcmPortPrimSeqProtocolErrors_Object = MibTableColumn
cfcmPortPrimSeqProtocolErrors = _CfcmPortPrimSeqProtocolErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 999999, 1, 6, 1, 9),
    _CfcmPortPrimSeqProtocolErrors_Type()
)
cfcmPortPrimSeqProtocolErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfcmPortPrimSeqProtocolErrors.setStatus("current")
_CfcmPortInvalidTxWords_Type = Counter32
_CfcmPortInvalidTxWords_Object = MibTableColumn
cfcmPortInvalidTxWords = _CfcmPortInvalidTxWords_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 999999, 1, 6, 1, 10),
    _CfcmPortInvalidTxWords_Type()
)
cfcmPortInvalidTxWords.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfcmPortInvalidTxWords.setStatus("current")
_CfcmPortInvalidCRCs_Type = Counter32
_CfcmPortInvalidCRCs_Object = MibTableColumn
cfcmPortInvalidCRCs = _CfcmPortInvalidCRCs_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 999999, 1, 6, 1, 11),
    _CfcmPortInvalidCRCs_Type()
)
cfcmPortInvalidCRCs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfcmPortInvalidCRCs.setStatus("current")
_CfcmPortInvalidOrderedSets_Type = Counter32
_CfcmPortInvalidOrderedSets_Object = MibTableColumn
cfcmPortInvalidOrderedSets = _CfcmPortInvalidOrderedSets_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 999999, 1, 6, 1, 12),
    _CfcmPortInvalidOrderedSets_Type()
)
cfcmPortInvalidOrderedSets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfcmPortInvalidOrderedSets.setStatus("current")
_CfcmPortFrameTooLongs_Type = Counter32
_CfcmPortFrameTooLongs_Object = MibTableColumn
cfcmPortFrameTooLongs = _CfcmPortFrameTooLongs_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 999999, 1, 6, 1, 13),
    _CfcmPortFrameTooLongs_Type()
)
cfcmPortFrameTooLongs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfcmPortFrameTooLongs.setStatus("current")
_CfcmPortTruncatedFrames_Type = Counter32
_CfcmPortTruncatedFrames_Object = MibTableColumn
cfcmPortTruncatedFrames = _CfcmPortTruncatedFrames_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 999999, 1, 6, 1, 14),
    _CfcmPortTruncatedFrames_Type()
)
cfcmPortTruncatedFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfcmPortTruncatedFrames.setStatus("current")
_CfcmPortAddressErrors_Type = Counter32
_CfcmPortAddressErrors_Object = MibTableColumn
cfcmPortAddressErrors = _CfcmPortAddressErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 999999, 1, 6, 1, 15),
    _CfcmPortAddressErrors_Type()
)
cfcmPortAddressErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfcmPortAddressErrors.setStatus("current")
_CfcmPortDelimiterErrors_Type = Counter32
_CfcmPortDelimiterErrors_Object = MibTableColumn
cfcmPortDelimiterErrors = _CfcmPortDelimiterErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 999999, 1, 6, 1, 16),
    _CfcmPortDelimiterErrors_Type()
)
cfcmPortDelimiterErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfcmPortDelimiterErrors.setStatus("current")
_CfcmPortEncodingDisparityErrors_Type = Counter32
_CfcmPortEncodingDisparityErrors_Object = MibTableColumn
cfcmPortEncodingDisparityErrors = _CfcmPortEncodingDisparityErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 999999, 1, 6, 1, 17),
    _CfcmPortEncodingDisparityErrors_Type()
)
cfcmPortEncodingDisparityErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfcmPortEncodingDisparityErrors.setStatus("current")
_CfcmPortOtherErrors_Type = Counter32
_CfcmPortOtherErrors_Object = MibTableColumn
cfcmPortOtherErrors = _CfcmPortOtherErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 999999, 1, 6, 1, 18),
    _CfcmPortOtherErrors_Type()
)
cfcmPortOtherErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfcmPortOtherErrors.setStatus("current")
_CfcmFxPortTable_Object = MibTable
cfcmFxPortTable = _CfcmFxPortTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 999999, 1, 7)
)
if mibBuilder.loadTexts:
    cfcmFxPortTable.setStatus("current")
_CfcmFxPortEntry_Object = MibTableRow
cfcmFxPortEntry = _CfcmFxPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 999999, 1, 7, 1)
)
cfcmFxPortEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    cfcmFxPortEntry.setStatus("current")
_CfcmFxPortRatov_Type = CfcmMilliSeconds
_CfcmFxPortRatov_Object = MibTableColumn
cfcmFxPortRatov = _CfcmFxPortRatov_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 999999, 1, 7, 1, 1),
    _CfcmFxPortRatov_Type()
)
cfcmFxPortRatov.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfcmFxPortRatov.setStatus("current")
if mibBuilder.loadTexts:
    cfcmFxPortRatov.setUnits("milliseconds")
_CfcmFxPortEdtov_Type = CfcmMilliSeconds
_CfcmFxPortEdtov_Object = MibTableColumn
cfcmFxPortEdtov = _CfcmFxPortEdtov_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 999999, 1, 7, 1, 2),
    _CfcmFxPortEdtov_Type()
)
cfcmFxPortEdtov.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfcmFxPortEdtov.setStatus("current")
if mibBuilder.loadTexts:
    cfcmFxPortEdtov.setUnits("milliseconds")
_CfcmFxPortRttov_Type = CfcmMilliSeconds
_CfcmFxPortRttov_Object = MibTableColumn
cfcmFxPortRttov = _CfcmFxPortRttov_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 999999, 1, 7, 1, 3),
    _CfcmFxPortRttov_Type()
)
cfcmFxPortRttov.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfcmFxPortRttov.setStatus("current")
if mibBuilder.loadTexts:
    cfcmFxPortRttov.setUnits("milliseconds")
_CfcmFxPortHoldTime_Type = CfcmMicroSeconds
_CfcmFxPortHoldTime_Object = MibTableColumn
cfcmFxPortHoldTime = _CfcmFxPortHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 999999, 1, 7, 1, 4),
    _CfcmFxPortHoldTime_Type()
)
cfcmFxPortHoldTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfcmFxPortHoldTime.setStatus("current")
if mibBuilder.loadTexts:
    cfcmFxPortHoldTime.setUnits("microseconds")
_CfcmFxPortCapBbCreditMax_Type = CfcmFcBbCredit
_CfcmFxPortCapBbCreditMax_Object = MibTableColumn
cfcmFxPortCapBbCreditMax = _CfcmFxPortCapBbCreditMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 999999, 1, 7, 1, 5),
    _CfcmFxPortCapBbCreditMax_Type()
)
cfcmFxPortCapBbCreditMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfcmFxPortCapBbCreditMax.setStatus("current")
if mibBuilder.loadTexts:
    cfcmFxPortCapBbCreditMax.setUnits("buffers")
_CfcmFxPortCapBbCreditMin_Type = CfcmFcBbCredit
_CfcmFxPortCapBbCreditMin_Object = MibTableColumn
cfcmFxPortCapBbCreditMin = _CfcmFxPortCapBbCreditMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 999999, 1, 7, 1, 6),
    _CfcmFxPortCapBbCreditMin_Type()
)
cfcmFxPortCapBbCreditMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfcmFxPortCapBbCreditMin.setStatus("current")
if mibBuilder.loadTexts:
    cfcmFxPortCapBbCreditMin.setUnits("buffers")
_CfcmFxPortCapDataFieldSizeMax_Type = CfcmFcDataFieldSize
_CfcmFxPortCapDataFieldSizeMax_Object = MibTableColumn
cfcmFxPortCapDataFieldSizeMax = _CfcmFxPortCapDataFieldSizeMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 999999, 1, 7, 1, 7),
    _CfcmFxPortCapDataFieldSizeMax_Type()
)
cfcmFxPortCapDataFieldSizeMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfcmFxPortCapDataFieldSizeMax.setStatus("current")
if mibBuilder.loadTexts:
    cfcmFxPortCapDataFieldSizeMax.setUnits("bytes")
_CfcmFxPortCapDataFieldSizeMin_Type = CfcmFcDataFieldSize
_CfcmFxPortCapDataFieldSizeMin_Object = MibTableColumn
cfcmFxPortCapDataFieldSizeMin = _CfcmFxPortCapDataFieldSizeMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 999999, 1, 7, 1, 8),
    _CfcmFxPortCapDataFieldSizeMin_Type()
)
cfcmFxPortCapDataFieldSizeMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfcmFxPortCapDataFieldSizeMin.setStatus("current")
if mibBuilder.loadTexts:
    cfcmFxPortCapDataFieldSizeMin.setUnits("bytes")
_CfcmFxPortCapClass2SeqDeliv_Type = TruthValue
_CfcmFxPortCapClass2SeqDeliv_Object = MibTableColumn
cfcmFxPortCapClass2SeqDeliv = _CfcmFxPortCapClass2SeqDeliv_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 999999, 1, 7, 1, 9),
    _CfcmFxPortCapClass2SeqDeliv_Type()
)
cfcmFxPortCapClass2SeqDeliv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfcmFxPortCapClass2SeqDeliv.setStatus("current")
_CfcmFxPortCapClass3SeqDeliv_Type = TruthValue
_CfcmFxPortCapClass3SeqDeliv_Object = MibTableColumn
cfcmFxPortCapClass3SeqDeliv = _CfcmFxPortCapClass3SeqDeliv_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 999999, 1, 7, 1, 10),
    _CfcmFxPortCapClass3SeqDeliv_Type()
)
cfcmFxPortCapClass3SeqDeliv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfcmFxPortCapClass3SeqDeliv.setStatus("current")
_CfcmFxPortCapHoldTimeMax_Type = CfcmMicroSeconds
_CfcmFxPortCapHoldTimeMax_Object = MibTableColumn
cfcmFxPortCapHoldTimeMax = _CfcmFxPortCapHoldTimeMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 999999, 1, 7, 1, 11),
    _CfcmFxPortCapHoldTimeMax_Type()
)
cfcmFxPortCapHoldTimeMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfcmFxPortCapHoldTimeMax.setStatus("current")
if mibBuilder.loadTexts:
    cfcmFxPortCapHoldTimeMax.setUnits("microseconds")
_CfcmFxPortCapHoldTimeMin_Type = CfcmMicroSeconds
_CfcmFxPortCapHoldTimeMin_Object = MibTableColumn
cfcmFxPortCapHoldTimeMin = _CfcmFxPortCapHoldTimeMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 999999, 1, 7, 1, 12),
    _CfcmFxPortCapHoldTimeMin_Type()
)
cfcmFxPortCapHoldTimeMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfcmFxPortCapHoldTimeMin.setStatus("current")
if mibBuilder.loadTexts:
    cfcmFxPortCapHoldTimeMin.setUnits("microseconds")
_CfcmISPortTable_Object = MibTable
cfcmISPortTable = _CfcmISPortTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 999999, 1, 8)
)
if mibBuilder.loadTexts:
    cfcmISPortTable.setStatus("current")
_CfcmISPortEntry_Object = MibTableRow
cfcmISPortEntry = _CfcmISPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 999999, 1, 8, 1)
)
cfcmISPortEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    cfcmISPortEntry.setStatus("current")
_CfcmISPortClassFCredit_Type = CfcmFcBbCredit
_CfcmISPortClassFCredit_Object = MibTableColumn
cfcmISPortClassFCredit = _CfcmISPortClassFCredit_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 999999, 1, 8, 1, 1),
    _CfcmISPortClassFCredit_Type()
)
cfcmISPortClassFCredit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfcmISPortClassFCredit.setStatus("current")
_CfcmISPortClassFDataFieldSize_Type = CfcmFcDataFieldSize
_CfcmISPortClassFDataFieldSize_Object = MibTableColumn
cfcmISPortClassFDataFieldSize = _CfcmISPortClassFDataFieldSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 999999, 1, 8, 1, 2),
    _CfcmISPortClassFDataFieldSize_Type()
)
cfcmISPortClassFDataFieldSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfcmISPortClassFDataFieldSize.setStatus("current")
if mibBuilder.loadTexts:
    cfcmISPortClassFDataFieldSize.setUnits("bytes")
_CfcmFLoginTable_Object = MibTable
cfcmFLoginTable = _CfcmFLoginTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 999999, 1, 9)
)
if mibBuilder.loadTexts:
    cfcmFLoginTable.setStatus("current")
_CfcmFLoginEntry_Object = MibTableRow
cfcmFLoginEntry = _CfcmFLoginEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 999999, 1, 9, 1)
)
cfcmFLoginEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CISCO-FC-MGMT-MIB", "cfcmFLoginNxPortIndex"),
)
if mibBuilder.loadTexts:
    cfcmFLoginEntry.setStatus("current")


class _CfcmFLoginNxPortIndex_Type(Unsigned32):
    """Custom type cfcmFLoginNxPortIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_CfcmFLoginNxPortIndex_Type.__name__ = "Unsigned32"
_CfcmFLoginNxPortIndex_Object = MibTableColumn
cfcmFLoginNxPortIndex = _CfcmFLoginNxPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 999999, 1, 9, 1, 1),
    _CfcmFLoginNxPortIndex_Type()
)
cfcmFLoginNxPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfcmFLoginNxPortIndex.setStatus("current")
_CfcmFLoginPortWwn_Type = CfcmFcNameIdOrZero
_CfcmFLoginPortWwn_Object = MibTableColumn
cfcmFLoginPortWwn = _CfcmFLoginPortWwn_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 999999, 1, 9, 1, 2),
    _CfcmFLoginPortWwn_Type()
)
cfcmFLoginPortWwn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfcmFLoginPortWwn.setStatus("current")
_CfcmFLoginNodeWwn_Type = CfcmFcNameIdOrZero
_CfcmFLoginNodeWwn_Object = MibTableColumn
cfcmFLoginNodeWwn = _CfcmFLoginNodeWwn_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 999999, 1, 9, 1, 3),
    _CfcmFLoginNodeWwn_Type()
)
cfcmFLoginNodeWwn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfcmFLoginNodeWwn.setStatus("current")
_CfcmFLoginBbCreditModel_Type = CfcmFcBbCreditModel
_CfcmFLoginBbCreditModel_Object = MibTableColumn
cfcmFLoginBbCreditModel = _CfcmFLoginBbCreditModel_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 999999, 1, 9, 1, 4),
    _CfcmFLoginBbCreditModel_Type()
)
cfcmFLoginBbCreditModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfcmFLoginBbCreditModel.setStatus("current")
_CfcmFLoginBbCredit_Type = CfcmFcBbCredit
_CfcmFLoginBbCredit_Object = MibTableColumn
cfcmFLoginBbCredit = _CfcmFLoginBbCredit_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 999999, 1, 9, 1, 5),
    _CfcmFLoginBbCredit_Type()
)
cfcmFLoginBbCredit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfcmFLoginBbCredit.setStatus("current")
_CfcmFLoginClassesAgreed_Type = CfcmFcClasses
_CfcmFLoginClassesAgreed_Object = MibTableColumn
cfcmFLoginClassesAgreed = _CfcmFLoginClassesAgreed_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 999999, 1, 9, 1, 6),
    _CfcmFLoginClassesAgreed_Type()
)
cfcmFLoginClassesAgreed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfcmFLoginClassesAgreed.setStatus("current")
_CfcmFLoginClass2SeqDelivAgreed_Type = TruthValue
_CfcmFLoginClass2SeqDelivAgreed_Object = MibTableColumn
cfcmFLoginClass2SeqDelivAgreed = _CfcmFLoginClass2SeqDelivAgreed_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 999999, 1, 9, 1, 7),
    _CfcmFLoginClass2SeqDelivAgreed_Type()
)
cfcmFLoginClass2SeqDelivAgreed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfcmFLoginClass2SeqDelivAgreed.setStatus("current")
_CfcmFLoginClass2DataFieldSize_Type = CfcmFcDataFieldSize
_CfcmFLoginClass2DataFieldSize_Object = MibTableColumn
cfcmFLoginClass2DataFieldSize = _CfcmFLoginClass2DataFieldSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 999999, 1, 9, 1, 8),
    _CfcmFLoginClass2DataFieldSize_Type()
)
cfcmFLoginClass2DataFieldSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfcmFLoginClass2DataFieldSize.setStatus("current")
_CfcmFLoginClass3SeqDelivAgreed_Type = TruthValue
_CfcmFLoginClass3SeqDelivAgreed_Object = MibTableColumn
cfcmFLoginClass3SeqDelivAgreed = _CfcmFLoginClass3SeqDelivAgreed_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 999999, 1, 9, 1, 9),
    _CfcmFLoginClass3SeqDelivAgreed_Type()
)
cfcmFLoginClass3SeqDelivAgreed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfcmFLoginClass3SeqDelivAgreed.setStatus("current")
_CfcmFLoginClass3DataFieldSize_Type = CfcmFcDataFieldSize
_CfcmFLoginClass3DataFieldSize_Object = MibTableColumn
cfcmFLoginClass3DataFieldSize = _CfcmFLoginClass3DataFieldSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 999999, 1, 9, 1, 10),
    _CfcmFLoginClass3DataFieldSize_Type()
)
cfcmFLoginClass3DataFieldSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfcmFLoginClass3DataFieldSize.setStatus("current")
_CfcmLinkTable_Object = MibTable
cfcmLinkTable = _CfcmLinkTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 999999, 1, 10)
)
if mibBuilder.loadTexts:
    cfcmLinkTable.setStatus("current")
_CfcmLinkEntry_Object = MibTableRow
cfcmLinkEntry = _CfcmLinkEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 999999, 1, 10, 1)
)
cfcmLinkEntry.setIndexNames(
    (0, "CISCO-FC-MGMT-MIB", "cfcmInstanceIndex"),
    (0, "CISCO-FC-MGMT-MIB", "cfcmLinkIndex"),
)
if mibBuilder.loadTexts:
    cfcmLinkEntry.setStatus("current")
_CfcmLinkIndex_Type = Unsigned32
_CfcmLinkIndex_Object = MibTableColumn
cfcmLinkIndex = _CfcmLinkIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 999999, 1, 10, 1, 1),
    _CfcmLinkIndex_Type()
)
cfcmLinkIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfcmLinkIndex.setStatus("current")
_CfcmLinkEnd1NodeWwn_Type = CfcmFcNameIdOrZero
_CfcmLinkEnd1NodeWwn_Object = MibTableColumn
cfcmLinkEnd1NodeWwn = _CfcmLinkEnd1NodeWwn_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 999999, 1, 10, 1, 2),
    _CfcmLinkEnd1NodeWwn_Type()
)
cfcmLinkEnd1NodeWwn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfcmLinkEnd1NodeWwn.setStatus("current")
_CfcmLinkEnd1PhysPortNumber_Type = Unsigned32
_CfcmLinkEnd1PhysPortNumber_Object = MibTableColumn
cfcmLinkEnd1PhysPortNumber = _CfcmLinkEnd1PhysPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 999999, 1, 10, 1, 3),
    _CfcmLinkEnd1PhysPortNumber_Type()
)
cfcmLinkEnd1PhysPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfcmLinkEnd1PhysPortNumber.setStatus("current")
_CfcmLinkEnd1PortWwn_Type = CfcmFcNameIdOrZero
_CfcmLinkEnd1PortWwn_Object = MibTableColumn
cfcmLinkEnd1PortWwn = _CfcmLinkEnd1PortWwn_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 999999, 1, 10, 1, 4),
    _CfcmLinkEnd1PortWwn_Type()
)
cfcmLinkEnd1PortWwn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfcmLinkEnd1PortWwn.setStatus("current")
_CfcmLinkEnd2NodeWwn_Type = CfcmFcNameIdOrZero
_CfcmLinkEnd2NodeWwn_Object = MibTableColumn
cfcmLinkEnd2NodeWwn = _CfcmLinkEnd2NodeWwn_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 999999, 1, 10, 1, 5),
    _CfcmLinkEnd2NodeWwn_Type()
)
cfcmLinkEnd2NodeWwn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfcmLinkEnd2NodeWwn.setStatus("current")
_CfcmLinkEnd2PhysPortNumber_Type = Unsigned32
_CfcmLinkEnd2PhysPortNumber_Object = MibTableColumn
cfcmLinkEnd2PhysPortNumber = _CfcmLinkEnd2PhysPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 999999, 1, 10, 1, 6),
    _CfcmLinkEnd2PhysPortNumber_Type()
)
cfcmLinkEnd2PhysPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfcmLinkEnd2PhysPortNumber.setStatus("current")
_CfcmLinkEnd2PortWwn_Type = CfcmFcNameIdOrZero
_CfcmLinkEnd2PortWwn_Object = MibTableColumn
cfcmLinkEnd2PortWwn = _CfcmLinkEnd2PortWwn_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 999999, 1, 10, 1, 7),
    _CfcmLinkEnd2PortWwn_Type()
)
cfcmLinkEnd2PortWwn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfcmLinkEnd2PortWwn.setStatus("current")
_CfcmLinkEnd2AgentAddress_Type = SnmpAdminString
_CfcmLinkEnd2AgentAddress_Object = MibTableColumn
cfcmLinkEnd2AgentAddress = _CfcmLinkEnd2AgentAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 999999, 1, 10, 1, 8),
    _CfcmLinkEnd2AgentAddress_Type()
)
cfcmLinkEnd2AgentAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfcmLinkEnd2AgentAddress.setStatus("current")
_CfcmLinkEnd2PortType_Type = CfcmFcPortType
_CfcmLinkEnd2PortType_Object = MibTableColumn
cfcmLinkEnd2PortType = _CfcmLinkEnd2PortType_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 999999, 1, 10, 1, 9),
    _CfcmLinkEnd2PortType_Type()
)
cfcmLinkEnd2PortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfcmLinkEnd2PortType.setStatus("current")
_CfcmLinkEnd2UnitType_Type = CfcmFcUnitFunctions
_CfcmLinkEnd2UnitType_Object = MibTableColumn
cfcmLinkEnd2UnitType = _CfcmLinkEnd2UnitType_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 999999, 1, 10, 1, 10),
    _CfcmLinkEnd2UnitType_Type()
)
cfcmLinkEnd2UnitType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfcmLinkEnd2UnitType.setStatus("current")
_CfcmLinkEnd2FcAddressId_Type = CfcmFcAddressId
_CfcmLinkEnd2FcAddressId_Object = MibTableColumn
cfcmLinkEnd2FcAddressId = _CfcmLinkEnd2FcAddressId_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 999999, 1, 10, 1, 11),
    _CfcmLinkEnd2FcAddressId_Type()
)
cfcmLinkEnd2FcAddressId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfcmLinkEnd2FcAddressId.setStatus("current")
_CfcmgmtNotifications_ObjectIdentity = ObjectIdentity
cfcmgmtNotifications = _CfcmgmtNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 999999, 2)
)
_CfcmgmtNotifPrefix_ObjectIdentity = ObjectIdentity
cfcmgmtNotifPrefix = _CfcmgmtNotifPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 999999, 2, 0)
)
_CfcmgmtConformance_ObjectIdentity = ObjectIdentity
cfcmgmtConformance = _CfcmgmtConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 999999, 3)
)
_CfcmgmtCompliances_ObjectIdentity = ObjectIdentity
cfcmgmtCompliances = _CfcmgmtCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 999999, 3, 1)
)
_CfcmgmtGroups_ObjectIdentity = ObjectIdentity
cfcmgmtGroups = _CfcmgmtGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 999999, 3, 2)
)
cfcmPortEntry.registerAugmentions(
    ("CISCO-FC-MGMT-MIB",
     "cfcmPortStatsEntry")
)
cfcmPortStatsEntry.setIndexNames(*cfcmPortEntry.getIndexNames())
cfcmPortEntry.registerAugmentions(
    ("CISCO-FC-MGMT-MIB",
     "cfcmPortLcStatsEntry")
)
cfcmPortLcStatsEntry.setIndexNames(*cfcmPortEntry.getIndexNames())
cfcmPortEntry.registerAugmentions(
    ("CISCO-FC-MGMT-MIB",
     "cfcmPortErrorsEntry")
)
cfcmPortErrorsEntry.setIndexNames(*cfcmPortEntry.getIndexNames())

# Managed Objects groups

cfcmInstanceBasicGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 999999, 3, 2, 1)
)
cfcmInstanceBasicGroup.setObjects(
      *(("CISCO-FC-MGMT-MIB", "cfcmInstanceWwn"),
        ("CISCO-FC-MGMT-MIB", "cfcmInstanceFunctions"),
        ("CISCO-FC-MGMT-MIB", "cfcmInstancePhysicalIndex"),
        ("CISCO-FC-MGMT-MIB", "cfcmInstanceSoftwareIndex"),
        ("CISCO-FC-MGMT-MIB", "cfcmInstanceStatus"),
        ("CISCO-FC-MGMT-MIB", "cfcmInstanceTextName"),
        ("CISCO-FC-MGMT-MIB", "cfcmInstanceDescr"),
        ("CISCO-FC-MGMT-MIB", "cfcmInstanceFabricId"))
)
if mibBuilder.loadTexts:
    cfcmInstanceBasicGroup.setStatus("current")

cfcmSwitchBasicGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 999999, 3, 2, 2)
)
cfcmSwitchBasicGroup.setObjects(
      *(("CISCO-FC-MGMT-MIB", "cfcmSwitchDomainId"),
        ("CISCO-FC-MGMT-MIB", "cfcmSwitchPrincipal"))
)
if mibBuilder.loadTexts:
    cfcmSwitchBasicGroup.setStatus("current")

cfcmPortBasicGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 999999, 3, 2, 3)
)
cfcmPortBasicGroup.setObjects(
      *(("CISCO-FC-MGMT-MIB", "cfcmPortInstanceIndex"),
        ("CISCO-FC-MGMT-MIB", "cfcmPortWwn"),
        ("CISCO-FC-MGMT-MIB", "cfcmPortNodeWwn"),
        ("CISCO-FC-MGMT-MIB", "cfcmPortAdminType"),
        ("CISCO-FC-MGMT-MIB", "cfcmPortOperType"),
        ("CISCO-FC-MGMT-MIB", "cfcmPortFcCapClass"),
        ("CISCO-FC-MGMT-MIB", "cfcmPortFcOperClass"),
        ("CISCO-FC-MGMT-MIB", "cfcmPortTransmitterType"),
        ("CISCO-FC-MGMT-MIB", "cfcmPortConnectorType"),
        ("CISCO-FC-MGMT-MIB", "cfcmPortSerialNumber"),
        ("CISCO-FC-MGMT-MIB", "cfcmPortPhysicalNumber"),
        ("CISCO-FC-MGMT-MIB", "cfcmPortAdminSpeed"),
        ("CISCO-FC-MGMT-MIB", "cfcmPortCapProtocols"),
        ("CISCO-FC-MGMT-MIB", "cfcmPortOperProtocols"))
)
if mibBuilder.loadTexts:
    cfcmPortBasicGroup.setStatus("current")

cfcmPortStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 999999, 3, 2, 4)
)
cfcmPortStatsGroup.setObjects(
      *(("CISCO-FC-MGMT-MIB", "cfcmPortBBCreditZeros"),
        ("CISCO-FC-MGMT-MIB", "cfcmPortFullInputBuffers"))
)
if mibBuilder.loadTexts:
    cfcmPortStatsGroup.setStatus("current")

cfcmPortClass23StatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 999999, 3, 2, 5)
)
cfcmPortClass23StatsGroup.setObjects(
      *(("CISCO-FC-MGMT-MIB", "cfcmPortClass2RxFrames"),
        ("CISCO-FC-MGMT-MIB", "cfcmPortClass2RxOctets"),
        ("CISCO-FC-MGMT-MIB", "cfcmPortClass2TxFrames"),
        ("CISCO-FC-MGMT-MIB", "cfcmPortClass2TxOctets"),
        ("CISCO-FC-MGMT-MIB", "cfcmPortClass2Discards"),
        ("CISCO-FC-MGMT-MIB", "cfcmPortClass2RxFbsyFrames"),
        ("CISCO-FC-MGMT-MIB", "cfcmPortClass2RxPbsyFrames"),
        ("CISCO-FC-MGMT-MIB", "cfcmPortClass2RxFrjtFrames"),
        ("CISCO-FC-MGMT-MIB", "cfcmPortClass2RxPrjtFrames"),
        ("CISCO-FC-MGMT-MIB", "cfcmPortClass2TxFbsyFrames"),
        ("CISCO-FC-MGMT-MIB", "cfcmPortClass2TxPbsyFrames"),
        ("CISCO-FC-MGMT-MIB", "cfcmPortClass2TxFrjtFrames"),
        ("CISCO-FC-MGMT-MIB", "cfcmPortClass2TxPrjtFrames"),
        ("CISCO-FC-MGMT-MIB", "cfcmPortClass3RxFrames"),
        ("CISCO-FC-MGMT-MIB", "cfcmPortClass3RxOctets"),
        ("CISCO-FC-MGMT-MIB", "cfcmPortClass3TxFrames"),
        ("CISCO-FC-MGMT-MIB", "cfcmPortClass3TxOctets"),
        ("CISCO-FC-MGMT-MIB", "cfcmPortClass3Discards"))
)
if mibBuilder.loadTexts:
    cfcmPortClass23StatsGroup.setStatus("current")

cfcmPortClassFStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 999999, 3, 2, 6)
)
cfcmPortClassFStatsGroup.setObjects(
      *(("CISCO-FC-MGMT-MIB", "cfcmPortClassFRxFrames"),
        ("CISCO-FC-MGMT-MIB", "cfcmPortClassFRxOctets"),
        ("CISCO-FC-MGMT-MIB", "cfcmPortClassFTxFrames"),
        ("CISCO-FC-MGMT-MIB", "cfcmPortClassFTxOctets"),
        ("CISCO-FC-MGMT-MIB", "cfcmPortClassFDiscards"))
)
if mibBuilder.loadTexts:
    cfcmPortClassFStatsGroup.setStatus("current")

cfcmPortLcStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 999999, 3, 2, 7)
)
cfcmPortLcStatsGroup.setObjects(
      *(("CISCO-FC-MGMT-MIB", "cfcmPortLcBBCreditZeros"),
        ("CISCO-FC-MGMT-MIB", "cfcmPortLcFullInputBuffers"),
        ("CISCO-FC-MGMT-MIB", "cfcmPortLcClass2RxFrames"),
        ("CISCO-FC-MGMT-MIB", "cfcmPortLcClass2RxOctets"),
        ("CISCO-FC-MGMT-MIB", "cfcmPortLcClass2TxFrames"),
        ("CISCO-FC-MGMT-MIB", "cfcmPortLcClass2TxOctets"),
        ("CISCO-FC-MGMT-MIB", "cfcmPortLcClass2Discards"),
        ("CISCO-FC-MGMT-MIB", "cfcmPortLcClass3Discards"),
        ("CISCO-FC-MGMT-MIB", "cfcmPortLcClass3RxFrames"),
        ("CISCO-FC-MGMT-MIB", "cfcmPortLcClass3RxOctets"),
        ("CISCO-FC-MGMT-MIB", "cfcmPortLcClass3TxFrames"),
        ("CISCO-FC-MGMT-MIB", "cfcmPortLcClass3TxOctets"),
        ("CISCO-FC-MGMT-MIB", "cfcmPortLcClass2RxFbsyFrames"),
        ("CISCO-FC-MGMT-MIB", "cfcmPortLcClass2RxPbsyFrames"),
        ("CISCO-FC-MGMT-MIB", "cfcmPortLcClass2RxFrjtFrames"),
        ("CISCO-FC-MGMT-MIB", "cfcmPortLcClass2RxPrjtFrames"),
        ("CISCO-FC-MGMT-MIB", "cfcmPortLcClass2TxFbsyFrames"),
        ("CISCO-FC-MGMT-MIB", "cfcmPortLcClass2TxPbsyFrames"),
        ("CISCO-FC-MGMT-MIB", "cfcmPortLcClass2TxFrjtFrames"),
        ("CISCO-FC-MGMT-MIB", "cfcmPortLcClass2TxPrjtFrames"))
)
if mibBuilder.loadTexts:
    cfcmPortLcStatsGroup.setStatus("current")

cfcmPortErrorsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 999999, 3, 2, 8)
)
cfcmPortErrorsGroup.setObjects(
      *(("CISCO-FC-MGMT-MIB", "cfcmPortRxLinkResets"),
        ("CISCO-FC-MGMT-MIB", "cfcmPortTxLinkResets"),
        ("CISCO-FC-MGMT-MIB", "cfcmPortLinkResets"),
        ("CISCO-FC-MGMT-MIB", "cfcmPortRxOfflineSequences"),
        ("CISCO-FC-MGMT-MIB", "cfcmPortTxOfflineSequences"),
        ("CISCO-FC-MGMT-MIB", "cfcmPortLinkFailures"),
        ("CISCO-FC-MGMT-MIB", "cfcmPortLossofSynchs"),
        ("CISCO-FC-MGMT-MIB", "cfcmPortLossofSignals"),
        ("CISCO-FC-MGMT-MIB", "cfcmPortPrimSeqProtocolErrors"),
        ("CISCO-FC-MGMT-MIB", "cfcmPortInvalidTxWords"),
        ("CISCO-FC-MGMT-MIB", "cfcmPortInvalidCRCs"),
        ("CISCO-FC-MGMT-MIB", "cfcmPortInvalidOrderedSets"),
        ("CISCO-FC-MGMT-MIB", "cfcmPortFrameTooLongs"),
        ("CISCO-FC-MGMT-MIB", "cfcmPortTruncatedFrames"),
        ("CISCO-FC-MGMT-MIB", "cfcmPortAddressErrors"),
        ("CISCO-FC-MGMT-MIB", "cfcmPortDelimiterErrors"),
        ("CISCO-FC-MGMT-MIB", "cfcmPortEncodingDisparityErrors"),
        ("CISCO-FC-MGMT-MIB", "cfcmPortOtherErrors"))
)
if mibBuilder.loadTexts:
    cfcmPortErrorsGroup.setStatus("current")

cfcmSwitchPortGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 999999, 3, 2, 9)
)
cfcmSwitchPortGroup.setObjects(
      *(("CISCO-FC-MGMT-MIB", "cfcmFxPortRatov"),
        ("CISCO-FC-MGMT-MIB", "cfcmFxPortEdtov"),
        ("CISCO-FC-MGMT-MIB", "cfcmFxPortRttov"),
        ("CISCO-FC-MGMT-MIB", "cfcmFxPortHoldTime"),
        ("CISCO-FC-MGMT-MIB", "cfcmFxPortCapBbCreditMax"),
        ("CISCO-FC-MGMT-MIB", "cfcmFxPortCapBbCreditMin"),
        ("CISCO-FC-MGMT-MIB", "cfcmFxPortCapDataFieldSizeMax"),
        ("CISCO-FC-MGMT-MIB", "cfcmFxPortCapDataFieldSizeMin"),
        ("CISCO-FC-MGMT-MIB", "cfcmFxPortCapClass2SeqDeliv"),
        ("CISCO-FC-MGMT-MIB", "cfcmFxPortCapClass3SeqDeliv"),
        ("CISCO-FC-MGMT-MIB", "cfcmFxPortCapHoldTimeMax"),
        ("CISCO-FC-MGMT-MIB", "cfcmFxPortCapHoldTimeMin"),
        ("CISCO-FC-MGMT-MIB", "cfcmISPortClassFCredit"),
        ("CISCO-FC-MGMT-MIB", "cfcmISPortClassFDataFieldSize"))
)
if mibBuilder.loadTexts:
    cfcmSwitchPortGroup.setStatus("current")

cfcmSwitchLoginGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 999999, 3, 2, 10)
)
cfcmSwitchLoginGroup.setObjects(
      *(("CISCO-FC-MGMT-MIB", "cfcmFLoginPortWwn"),
        ("CISCO-FC-MGMT-MIB", "cfcmFLoginNodeWwn"),
        ("CISCO-FC-MGMT-MIB", "cfcmFLoginBbCreditModel"),
        ("CISCO-FC-MGMT-MIB", "cfcmFLoginBbCredit"),
        ("CISCO-FC-MGMT-MIB", "cfcmFLoginClassesAgreed"),
        ("CISCO-FC-MGMT-MIB", "cfcmFLoginClass2SeqDelivAgreed"),
        ("CISCO-FC-MGMT-MIB", "cfcmFLoginClass2DataFieldSize"),
        ("CISCO-FC-MGMT-MIB", "cfcmFLoginClass3SeqDelivAgreed"),
        ("CISCO-FC-MGMT-MIB", "cfcmFLoginClass3DataFieldSize"))
)
if mibBuilder.loadTexts:
    cfcmSwitchLoginGroup.setStatus("current")

cfcmLinkBasicGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 999999, 3, 2, 11)
)
cfcmLinkBasicGroup.setObjects(
      *(("CISCO-FC-MGMT-MIB", "cfcmLinkEnd1NodeWwn"),
        ("CISCO-FC-MGMT-MIB", "cfcmLinkEnd1PhysPortNumber"),
        ("CISCO-FC-MGMT-MIB", "cfcmLinkEnd1PortWwn"),
        ("CISCO-FC-MGMT-MIB", "cfcmLinkEnd2NodeWwn"),
        ("CISCO-FC-MGMT-MIB", "cfcmLinkEnd2PhysPortNumber"),
        ("CISCO-FC-MGMT-MIB", "cfcmLinkEnd2PortWwn"),
        ("CISCO-FC-MGMT-MIB", "cfcmLinkEnd2AgentAddress"),
        ("CISCO-FC-MGMT-MIB", "cfcmLinkEnd2PortType"),
        ("CISCO-FC-MGMT-MIB", "cfcmLinkEnd2UnitType"),
        ("CISCO-FC-MGMT-MIB", "cfcmLinkEnd2FcAddressId"))
)
if mibBuilder.loadTexts:
    cfcmLinkBasicGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

cfcmgmtCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 10, 999999, 3, 1, 1)
)
if mibBuilder.loadTexts:
    cfcmgmtCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-FC-MGMT-MIB",
    **{"CfcmFcNameIdOrZero": CfcmFcNameIdOrZero,
       "CfcmFcAddressId": CfcmFcAddressId,
       "CfcmDomainIdOrZero": CfcmDomainIdOrZero,
       "CfcmFcPortType": CfcmFcPortType,
       "CfcmFcClasses": CfcmFcClasses,
       "CfcmFcBbCredit": CfcmFcBbCredit,
       "CfcmFcBbCreditModel": CfcmFcBbCreditModel,
       "CfcmFcDataFieldSize": CfcmFcDataFieldSize,
       "CfcmFcUnitFunctions": CfcmFcUnitFunctions,
       "CfcmPhysicalIndexOrZero": CfcmPhysicalIndexOrZero,
       "CfcmHrSWInstalledIndexOrZero": CfcmHrSWInstalledIndexOrZero,
       "CfcmMilliSeconds": CfcmMilliSeconds,
       "CfcmMicroSeconds": CfcmMicroSeconds,
       "ciscoFcMgmtMIB": ciscoFcMgmtMIB,
       "cfcmgmtObjects": cfcmgmtObjects,
       "cfcmInstanceTable": cfcmInstanceTable,
       "cfcmInstanceEntry": cfcmInstanceEntry,
       "cfcmInstanceIndex": cfcmInstanceIndex,
       "cfcmInstanceWwn": cfcmInstanceWwn,
       "cfcmInstanceFunctions": cfcmInstanceFunctions,
       "cfcmInstancePhysicalIndex": cfcmInstancePhysicalIndex,
       "cfcmInstanceSoftwareIndex": cfcmInstanceSoftwareIndex,
       "cfcmInstanceStatus": cfcmInstanceStatus,
       "cfcmInstanceTextName": cfcmInstanceTextName,
       "cfcmInstanceDescr": cfcmInstanceDescr,
       "cfcmInstanceFabricId": cfcmInstanceFabricId,
       "cfcmSwitchTable": cfcmSwitchTable,
       "cfcmSwitchEntry": cfcmSwitchEntry,
       "cfcmSwitchIndex": cfcmSwitchIndex,
       "cfcmSwitchDomainId": cfcmSwitchDomainId,
       "cfcmSwitchPrincipal": cfcmSwitchPrincipal,
       "cfcmPortTable": cfcmPortTable,
       "cfcmPortEntry": cfcmPortEntry,
       "cfcmPortInstanceIndex": cfcmPortInstanceIndex,
       "cfcmPortWwn": cfcmPortWwn,
       "cfcmPortNodeWwn": cfcmPortNodeWwn,
       "cfcmPortAdminType": cfcmPortAdminType,
       "cfcmPortOperType": cfcmPortOperType,
       "cfcmPortFcCapClass": cfcmPortFcCapClass,
       "cfcmPortFcOperClass": cfcmPortFcOperClass,
       "cfcmPortTransmitterType": cfcmPortTransmitterType,
       "cfcmPortConnectorType": cfcmPortConnectorType,
       "cfcmPortSerialNumber": cfcmPortSerialNumber,
       "cfcmPortPhysicalNumber": cfcmPortPhysicalNumber,
       "cfcmPortAdminSpeed": cfcmPortAdminSpeed,
       "cfcmPortCapProtocols": cfcmPortCapProtocols,
       "cfcmPortOperProtocols": cfcmPortOperProtocols,
       "cfcmPortStatsTable": cfcmPortStatsTable,
       "cfcmPortStatsEntry": cfcmPortStatsEntry,
       "cfcmPortBBCreditZeros": cfcmPortBBCreditZeros,
       "cfcmPortFullInputBuffers": cfcmPortFullInputBuffers,
       "cfcmPortClass2RxFrames": cfcmPortClass2RxFrames,
       "cfcmPortClass2RxOctets": cfcmPortClass2RxOctets,
       "cfcmPortClass2TxFrames": cfcmPortClass2TxFrames,
       "cfcmPortClass2TxOctets": cfcmPortClass2TxOctets,
       "cfcmPortClass2Discards": cfcmPortClass2Discards,
       "cfcmPortClass2RxFbsyFrames": cfcmPortClass2RxFbsyFrames,
       "cfcmPortClass2RxPbsyFrames": cfcmPortClass2RxPbsyFrames,
       "cfcmPortClass2RxFrjtFrames": cfcmPortClass2RxFrjtFrames,
       "cfcmPortClass2RxPrjtFrames": cfcmPortClass2RxPrjtFrames,
       "cfcmPortClass2TxFbsyFrames": cfcmPortClass2TxFbsyFrames,
       "cfcmPortClass2TxPbsyFrames": cfcmPortClass2TxPbsyFrames,
       "cfcmPortClass2TxFrjtFrames": cfcmPortClass2TxFrjtFrames,
       "cfcmPortClass2TxPrjtFrames": cfcmPortClass2TxPrjtFrames,
       "cfcmPortClass3RxFrames": cfcmPortClass3RxFrames,
       "cfcmPortClass3RxOctets": cfcmPortClass3RxOctets,
       "cfcmPortClass3TxFrames": cfcmPortClass3TxFrames,
       "cfcmPortClass3TxOctets": cfcmPortClass3TxOctets,
       "cfcmPortClass3Discards": cfcmPortClass3Discards,
       "cfcmPortClassFRxFrames": cfcmPortClassFRxFrames,
       "cfcmPortClassFRxOctets": cfcmPortClassFRxOctets,
       "cfcmPortClassFTxFrames": cfcmPortClassFTxFrames,
       "cfcmPortClassFTxOctets": cfcmPortClassFTxOctets,
       "cfcmPortClassFDiscards": cfcmPortClassFDiscards,
       "cfcmPortLcStatsTable": cfcmPortLcStatsTable,
       "cfcmPortLcStatsEntry": cfcmPortLcStatsEntry,
       "cfcmPortLcBBCreditZeros": cfcmPortLcBBCreditZeros,
       "cfcmPortLcFullInputBuffers": cfcmPortLcFullInputBuffers,
       "cfcmPortLcClass2RxFrames": cfcmPortLcClass2RxFrames,
       "cfcmPortLcClass2RxOctets": cfcmPortLcClass2RxOctets,
       "cfcmPortLcClass2TxFrames": cfcmPortLcClass2TxFrames,
       "cfcmPortLcClass2TxOctets": cfcmPortLcClass2TxOctets,
       "cfcmPortLcClass2Discards": cfcmPortLcClass2Discards,
       "cfcmPortLcClass2RxFbsyFrames": cfcmPortLcClass2RxFbsyFrames,
       "cfcmPortLcClass2RxPbsyFrames": cfcmPortLcClass2RxPbsyFrames,
       "cfcmPortLcClass2RxFrjtFrames": cfcmPortLcClass2RxFrjtFrames,
       "cfcmPortLcClass2RxPrjtFrames": cfcmPortLcClass2RxPrjtFrames,
       "cfcmPortLcClass2TxFbsyFrames": cfcmPortLcClass2TxFbsyFrames,
       "cfcmPortLcClass2TxPbsyFrames": cfcmPortLcClass2TxPbsyFrames,
       "cfcmPortLcClass2TxFrjtFrames": cfcmPortLcClass2TxFrjtFrames,
       "cfcmPortLcClass2TxPrjtFrames": cfcmPortLcClass2TxPrjtFrames,
       "cfcmPortLcClass3RxFrames": cfcmPortLcClass3RxFrames,
       "cfcmPortLcClass3RxOctets": cfcmPortLcClass3RxOctets,
       "cfcmPortLcClass3TxFrames": cfcmPortLcClass3TxFrames,
       "cfcmPortLcClass3TxOctets": cfcmPortLcClass3TxOctets,
       "cfcmPortLcClass3Discards": cfcmPortLcClass3Discards,
       "cfcmPortErrorsTable": cfcmPortErrorsTable,
       "cfcmPortErrorsEntry": cfcmPortErrorsEntry,
       "cfcmPortRxLinkResets": cfcmPortRxLinkResets,
       "cfcmPortTxLinkResets": cfcmPortTxLinkResets,
       "cfcmPortLinkResets": cfcmPortLinkResets,
       "cfcmPortRxOfflineSequences": cfcmPortRxOfflineSequences,
       "cfcmPortTxOfflineSequences": cfcmPortTxOfflineSequences,
       "cfcmPortLinkFailures": cfcmPortLinkFailures,
       "cfcmPortLossofSynchs": cfcmPortLossofSynchs,
       "cfcmPortLossofSignals": cfcmPortLossofSignals,
       "cfcmPortPrimSeqProtocolErrors": cfcmPortPrimSeqProtocolErrors,
       "cfcmPortInvalidTxWords": cfcmPortInvalidTxWords,
       "cfcmPortInvalidCRCs": cfcmPortInvalidCRCs,
       "cfcmPortInvalidOrderedSets": cfcmPortInvalidOrderedSets,
       "cfcmPortFrameTooLongs": cfcmPortFrameTooLongs,
       "cfcmPortTruncatedFrames": cfcmPortTruncatedFrames,
       "cfcmPortAddressErrors": cfcmPortAddressErrors,
       "cfcmPortDelimiterErrors": cfcmPortDelimiterErrors,
       "cfcmPortEncodingDisparityErrors": cfcmPortEncodingDisparityErrors,
       "cfcmPortOtherErrors": cfcmPortOtherErrors,
       "cfcmFxPortTable": cfcmFxPortTable,
       "cfcmFxPortEntry": cfcmFxPortEntry,
       "cfcmFxPortRatov": cfcmFxPortRatov,
       "cfcmFxPortEdtov": cfcmFxPortEdtov,
       "cfcmFxPortRttov": cfcmFxPortRttov,
       "cfcmFxPortHoldTime": cfcmFxPortHoldTime,
       "cfcmFxPortCapBbCreditMax": cfcmFxPortCapBbCreditMax,
       "cfcmFxPortCapBbCreditMin": cfcmFxPortCapBbCreditMin,
       "cfcmFxPortCapDataFieldSizeMax": cfcmFxPortCapDataFieldSizeMax,
       "cfcmFxPortCapDataFieldSizeMin": cfcmFxPortCapDataFieldSizeMin,
       "cfcmFxPortCapClass2SeqDeliv": cfcmFxPortCapClass2SeqDeliv,
       "cfcmFxPortCapClass3SeqDeliv": cfcmFxPortCapClass3SeqDeliv,
       "cfcmFxPortCapHoldTimeMax": cfcmFxPortCapHoldTimeMax,
       "cfcmFxPortCapHoldTimeMin": cfcmFxPortCapHoldTimeMin,
       "cfcmISPortTable": cfcmISPortTable,
       "cfcmISPortEntry": cfcmISPortEntry,
       "cfcmISPortClassFCredit": cfcmISPortClassFCredit,
       "cfcmISPortClassFDataFieldSize": cfcmISPortClassFDataFieldSize,
       "cfcmFLoginTable": cfcmFLoginTable,
       "cfcmFLoginEntry": cfcmFLoginEntry,
       "cfcmFLoginNxPortIndex": cfcmFLoginNxPortIndex,
       "cfcmFLoginPortWwn": cfcmFLoginPortWwn,
       "cfcmFLoginNodeWwn": cfcmFLoginNodeWwn,
       "cfcmFLoginBbCreditModel": cfcmFLoginBbCreditModel,
       "cfcmFLoginBbCredit": cfcmFLoginBbCredit,
       "cfcmFLoginClassesAgreed": cfcmFLoginClassesAgreed,
       "cfcmFLoginClass2SeqDelivAgreed": cfcmFLoginClass2SeqDelivAgreed,
       "cfcmFLoginClass2DataFieldSize": cfcmFLoginClass2DataFieldSize,
       "cfcmFLoginClass3SeqDelivAgreed": cfcmFLoginClass3SeqDelivAgreed,
       "cfcmFLoginClass3DataFieldSize": cfcmFLoginClass3DataFieldSize,
       "cfcmLinkTable": cfcmLinkTable,
       "cfcmLinkEntry": cfcmLinkEntry,
       "cfcmLinkIndex": cfcmLinkIndex,
       "cfcmLinkEnd1NodeWwn": cfcmLinkEnd1NodeWwn,
       "cfcmLinkEnd1PhysPortNumber": cfcmLinkEnd1PhysPortNumber,
       "cfcmLinkEnd1PortWwn": cfcmLinkEnd1PortWwn,
       "cfcmLinkEnd2NodeWwn": cfcmLinkEnd2NodeWwn,
       "cfcmLinkEnd2PhysPortNumber": cfcmLinkEnd2PhysPortNumber,
       "cfcmLinkEnd2PortWwn": cfcmLinkEnd2PortWwn,
       "cfcmLinkEnd2AgentAddress": cfcmLinkEnd2AgentAddress,
       "cfcmLinkEnd2PortType": cfcmLinkEnd2PortType,
       "cfcmLinkEnd2UnitType": cfcmLinkEnd2UnitType,
       "cfcmLinkEnd2FcAddressId": cfcmLinkEnd2FcAddressId,
       "cfcmgmtNotifications": cfcmgmtNotifications,
       "cfcmgmtNotifPrefix": cfcmgmtNotifPrefix,
       "cfcmgmtConformance": cfcmgmtConformance,
       "cfcmgmtCompliances": cfcmgmtCompliances,
       "cfcmgmtCompliance": cfcmgmtCompliance,
       "cfcmgmtGroups": cfcmgmtGroups,
       "cfcmInstanceBasicGroup": cfcmInstanceBasicGroup,
       "cfcmSwitchBasicGroup": cfcmSwitchBasicGroup,
       "cfcmPortBasicGroup": cfcmPortBasicGroup,
       "cfcmPortStatsGroup": cfcmPortStatsGroup,
       "cfcmPortClass23StatsGroup": cfcmPortClass23StatsGroup,
       "cfcmPortClassFStatsGroup": cfcmPortClassFStatsGroup,
       "cfcmPortLcStatsGroup": cfcmPortLcStatsGroup,
       "cfcmPortErrorsGroup": cfcmPortErrorsGroup,
       "cfcmSwitchPortGroup": cfcmSwitchPortGroup,
       "cfcmSwitchLoginGroup": cfcmSwitchLoginGroup,
       "cfcmLinkBasicGroup": cfcmLinkBasicGroup}
)
