# SNMP MIB module (FC-MGMT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/FC-MGMT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:27:58 2024
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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

fcMgmtMIB = ModuleIdentity(
    (1, 3, 6, 1, 2, 1, 10, 56)
)
fcMgmtMIB.setRevisions(
        ("2005-04-26 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class FcNameIdOrZero(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(8, 8),
        ValueSizeConstraint(16, 16),
    )



class FcAddressIdOrZero(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(3, 3),
    )



class FcDomainIdOrZero(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 239),
    )



class FcPortType(Unsigned32, TextualConvention):
    status = "current"


class FcClasses(Bits, TextualConvention):
    status = "current"


class FcBbCredit(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )



class FcBbCreditModel(Integer32, TextualConvention):
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



class FcDataFieldSize(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(128, 2112),
    )



class FcUnitFunctions(Bits, TextualConvention):
    status = "current"


# MIB Managed Objects in the order of their OIDs

_FcmgmtObjects_ObjectIdentity = ObjectIdentity
fcmgmtObjects = _FcmgmtObjects_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 56, 1)
)
_FcmInstanceTable_Object = MibTable
fcmInstanceTable = _FcmInstanceTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 56, 1, 1)
)
if mibBuilder.loadTexts:
    fcmInstanceTable.setStatus("current")
_FcmInstanceEntry_Object = MibTableRow
fcmInstanceEntry = _FcmInstanceEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 56, 1, 1, 1)
)
fcmInstanceEntry.setIndexNames(
    (0, "FC-MGMT-MIB", "fcmInstanceIndex"),
)
if mibBuilder.loadTexts:
    fcmInstanceEntry.setStatus("current")


class _FcmInstanceIndex_Type(Unsigned32):
    """Custom type fcmInstanceIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_FcmInstanceIndex_Type.__name__ = "Unsigned32"
_FcmInstanceIndex_Object = MibTableColumn
fcmInstanceIndex = _FcmInstanceIndex_Object(
    (1, 3, 6, 1, 2, 1, 10, 56, 1, 1, 1, 1),
    _FcmInstanceIndex_Type()
)
fcmInstanceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fcmInstanceIndex.setStatus("current")
_FcmInstanceWwn_Type = FcNameIdOrZero
_FcmInstanceWwn_Object = MibTableColumn
fcmInstanceWwn = _FcmInstanceWwn_Object(
    (1, 3, 6, 1, 2, 1, 10, 56, 1, 1, 1, 2),
    _FcmInstanceWwn_Type()
)
fcmInstanceWwn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcmInstanceWwn.setStatus("current")
_FcmInstanceFunctions_Type = FcUnitFunctions
_FcmInstanceFunctions_Object = MibTableColumn
fcmInstanceFunctions = _FcmInstanceFunctions_Object(
    (1, 3, 6, 1, 2, 1, 10, 56, 1, 1, 1, 3),
    _FcmInstanceFunctions_Type()
)
fcmInstanceFunctions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcmInstanceFunctions.setStatus("current")


class _FcmInstancePhysicalIndex_Type(Integer32):
    """Custom type fcmInstancePhysicalIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FcmInstancePhysicalIndex_Type.__name__ = "Integer32"
_FcmInstancePhysicalIndex_Object = MibTableColumn
fcmInstancePhysicalIndex = _FcmInstancePhysicalIndex_Object(
    (1, 3, 6, 1, 2, 1, 10, 56, 1, 1, 1, 4),
    _FcmInstancePhysicalIndex_Type()
)
fcmInstancePhysicalIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcmInstancePhysicalIndex.setStatus("current")


class _FcmInstanceSoftwareIndex_Type(Integer32):
    """Custom type fcmInstanceSoftwareIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FcmInstanceSoftwareIndex_Type.__name__ = "Integer32"
_FcmInstanceSoftwareIndex_Object = MibTableColumn
fcmInstanceSoftwareIndex = _FcmInstanceSoftwareIndex_Object(
    (1, 3, 6, 1, 2, 1, 10, 56, 1, 1, 1, 5),
    _FcmInstanceSoftwareIndex_Type()
)
fcmInstanceSoftwareIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcmInstanceSoftwareIndex.setStatus("current")


class _FcmInstanceStatus_Type(Integer32):
    """Custom type fcmInstanceStatus based on Integer32"""
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


_FcmInstanceStatus_Type.__name__ = "Integer32"
_FcmInstanceStatus_Object = MibTableColumn
fcmInstanceStatus = _FcmInstanceStatus_Object(
    (1, 3, 6, 1, 2, 1, 10, 56, 1, 1, 1, 6),
    _FcmInstanceStatus_Type()
)
fcmInstanceStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcmInstanceStatus.setStatus("current")


class _FcmInstanceTextName_Type(SnmpAdminString):
    """Custom type fcmInstanceTextName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 79),
    )


_FcmInstanceTextName_Type.__name__ = "SnmpAdminString"
_FcmInstanceTextName_Object = MibTableColumn
fcmInstanceTextName = _FcmInstanceTextName_Object(
    (1, 3, 6, 1, 2, 1, 10, 56, 1, 1, 1, 7),
    _FcmInstanceTextName_Type()
)
fcmInstanceTextName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fcmInstanceTextName.setStatus("current")
_FcmInstanceDescr_Type = SnmpAdminString
_FcmInstanceDescr_Object = MibTableColumn
fcmInstanceDescr = _FcmInstanceDescr_Object(
    (1, 3, 6, 1, 2, 1, 10, 56, 1, 1, 1, 8),
    _FcmInstanceDescr_Type()
)
fcmInstanceDescr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fcmInstanceDescr.setStatus("current")
_FcmInstanceFabricId_Type = FcNameIdOrZero
_FcmInstanceFabricId_Object = MibTableColumn
fcmInstanceFabricId = _FcmInstanceFabricId_Object(
    (1, 3, 6, 1, 2, 1, 10, 56, 1, 1, 1, 9),
    _FcmInstanceFabricId_Type()
)
fcmInstanceFabricId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcmInstanceFabricId.setStatus("current")
_FcmSwitchTable_Object = MibTable
fcmSwitchTable = _FcmSwitchTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 56, 1, 2)
)
if mibBuilder.loadTexts:
    fcmSwitchTable.setStatus("current")
_FcmSwitchEntry_Object = MibTableRow
fcmSwitchEntry = _FcmSwitchEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 56, 1, 2, 1)
)
fcmSwitchEntry.setIndexNames(
    (0, "FC-MGMT-MIB", "fcmInstanceIndex"),
    (0, "FC-MGMT-MIB", "fcmSwitchIndex"),
)
if mibBuilder.loadTexts:
    fcmSwitchEntry.setStatus("current")


class _FcmSwitchIndex_Type(Unsigned32):
    """Custom type fcmSwitchIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_FcmSwitchIndex_Type.__name__ = "Unsigned32"
_FcmSwitchIndex_Object = MibTableColumn
fcmSwitchIndex = _FcmSwitchIndex_Object(
    (1, 3, 6, 1, 2, 1, 10, 56, 1, 2, 1, 1),
    _FcmSwitchIndex_Type()
)
fcmSwitchIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fcmSwitchIndex.setStatus("current")
_FcmSwitchDomainId_Type = FcDomainIdOrZero
_FcmSwitchDomainId_Object = MibTableColumn
fcmSwitchDomainId = _FcmSwitchDomainId_Object(
    (1, 3, 6, 1, 2, 1, 10, 56, 1, 2, 1, 2),
    _FcmSwitchDomainId_Type()
)
fcmSwitchDomainId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fcmSwitchDomainId.setStatus("current")
_FcmSwitchPrincipal_Type = TruthValue
_FcmSwitchPrincipal_Object = MibTableColumn
fcmSwitchPrincipal = _FcmSwitchPrincipal_Object(
    (1, 3, 6, 1, 2, 1, 10, 56, 1, 2, 1, 3),
    _FcmSwitchPrincipal_Type()
)
fcmSwitchPrincipal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcmSwitchPrincipal.setStatus("current")
_FcmSwitchWWN_Type = FcNameIdOrZero
_FcmSwitchWWN_Object = MibTableColumn
fcmSwitchWWN = _FcmSwitchWWN_Object(
    (1, 3, 6, 1, 2, 1, 10, 56, 1, 2, 1, 4),
    _FcmSwitchWWN_Type()
)
fcmSwitchWWN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcmSwitchWWN.setStatus("current")
_FcmPortTable_Object = MibTable
fcmPortTable = _FcmPortTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 56, 1, 3)
)
if mibBuilder.loadTexts:
    fcmPortTable.setStatus("current")
_FcmPortEntry_Object = MibTableRow
fcmPortEntry = _FcmPortEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 56, 1, 3, 1)
)
fcmPortEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    fcmPortEntry.setStatus("current")


class _FcmPortInstanceIndex_Type(Unsigned32):
    """Custom type fcmPortInstanceIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_FcmPortInstanceIndex_Type.__name__ = "Unsigned32"
_FcmPortInstanceIndex_Object = MibTableColumn
fcmPortInstanceIndex = _FcmPortInstanceIndex_Object(
    (1, 3, 6, 1, 2, 1, 10, 56, 1, 3, 1, 1),
    _FcmPortInstanceIndex_Type()
)
fcmPortInstanceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcmPortInstanceIndex.setStatus("current")
_FcmPortWwn_Type = FcNameIdOrZero
_FcmPortWwn_Object = MibTableColumn
fcmPortWwn = _FcmPortWwn_Object(
    (1, 3, 6, 1, 2, 1, 10, 56, 1, 3, 1, 2),
    _FcmPortWwn_Type()
)
fcmPortWwn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcmPortWwn.setStatus("current")
_FcmPortNodeWwn_Type = FcNameIdOrZero
_FcmPortNodeWwn_Object = MibTableColumn
fcmPortNodeWwn = _FcmPortNodeWwn_Object(
    (1, 3, 6, 1, 2, 1, 10, 56, 1, 3, 1, 3),
    _FcmPortNodeWwn_Type()
)
fcmPortNodeWwn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcmPortNodeWwn.setStatus("current")
_FcmPortAdminType_Type = FcPortType
_FcmPortAdminType_Object = MibTableColumn
fcmPortAdminType = _FcmPortAdminType_Object(
    (1, 3, 6, 1, 2, 1, 10, 56, 1, 3, 1, 4),
    _FcmPortAdminType_Type()
)
fcmPortAdminType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fcmPortAdminType.setStatus("current")
_FcmPortOperType_Type = FcPortType
_FcmPortOperType_Object = MibTableColumn
fcmPortOperType = _FcmPortOperType_Object(
    (1, 3, 6, 1, 2, 1, 10, 56, 1, 3, 1, 5),
    _FcmPortOperType_Type()
)
fcmPortOperType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcmPortOperType.setStatus("current")
_FcmPortFcCapClass_Type = FcClasses
_FcmPortFcCapClass_Object = MibTableColumn
fcmPortFcCapClass = _FcmPortFcCapClass_Object(
    (1, 3, 6, 1, 2, 1, 10, 56, 1, 3, 1, 6),
    _FcmPortFcCapClass_Type()
)
fcmPortFcCapClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcmPortFcCapClass.setStatus("current")
_FcmPortFcOperClass_Type = FcClasses
_FcmPortFcOperClass_Object = MibTableColumn
fcmPortFcOperClass = _FcmPortFcOperClass_Object(
    (1, 3, 6, 1, 2, 1, 10, 56, 1, 3, 1, 7),
    _FcmPortFcOperClass_Type()
)
fcmPortFcOperClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcmPortFcOperClass.setStatus("current")


class _FcmPortTransmitterType_Type(Integer32):
    """Custom type fcmPortTransmitterType based on Integer32"""
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


_FcmPortTransmitterType_Type.__name__ = "Integer32"
_FcmPortTransmitterType_Object = MibTableColumn
fcmPortTransmitterType = _FcmPortTransmitterType_Object(
    (1, 3, 6, 1, 2, 1, 10, 56, 1, 3, 1, 8),
    _FcmPortTransmitterType_Type()
)
fcmPortTransmitterType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcmPortTransmitterType.setStatus("current")


class _FcmPortConnectorType_Type(Integer32):
    """Custom type fcmPortConnectorType based on Integer32"""
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


_FcmPortConnectorType_Type.__name__ = "Integer32"
_FcmPortConnectorType_Object = MibTableColumn
fcmPortConnectorType = _FcmPortConnectorType_Object(
    (1, 3, 6, 1, 2, 1, 10, 56, 1, 3, 1, 9),
    _FcmPortConnectorType_Type()
)
fcmPortConnectorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcmPortConnectorType.setStatus("current")
_FcmPortSerialNumber_Type = SnmpAdminString
_FcmPortSerialNumber_Object = MibTableColumn
fcmPortSerialNumber = _FcmPortSerialNumber_Object(
    (1, 3, 6, 1, 2, 1, 10, 56, 1, 3, 1, 10),
    _FcmPortSerialNumber_Type()
)
fcmPortSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcmPortSerialNumber.setStatus("current")
_FcmPortPhysicalNumber_Type = Unsigned32
_FcmPortPhysicalNumber_Object = MibTableColumn
fcmPortPhysicalNumber = _FcmPortPhysicalNumber_Object(
    (1, 3, 6, 1, 2, 1, 10, 56, 1, 3, 1, 11),
    _FcmPortPhysicalNumber_Type()
)
fcmPortPhysicalNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcmPortPhysicalNumber.setStatus("current")


class _FcmPortAdminSpeed_Type(Integer32):
    """Custom type fcmPortAdminSpeed based on Integer32"""
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


_FcmPortAdminSpeed_Type.__name__ = "Integer32"
_FcmPortAdminSpeed_Object = MibTableColumn
fcmPortAdminSpeed = _FcmPortAdminSpeed_Object(
    (1, 3, 6, 1, 2, 1, 10, 56, 1, 3, 1, 12),
    _FcmPortAdminSpeed_Type()
)
fcmPortAdminSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fcmPortAdminSpeed.setStatus("current")


class _FcmPortCapProtocols_Type(Bits):
    """Custom type fcmPortCapProtocols based on Bits"""
    namedValues = NamedValues(
        *(("fabric", 2),
          ("ficon", 6),
          ("loop", 1),
          ("scsi", 3),
          ("tcpIp", 4),
          ("unknown", 0),
          ("vi", 5))
    )

_FcmPortCapProtocols_Type.__name__ = "Bits"
_FcmPortCapProtocols_Object = MibTableColumn
fcmPortCapProtocols = _FcmPortCapProtocols_Object(
    (1, 3, 6, 1, 2, 1, 10, 56, 1, 3, 1, 13),
    _FcmPortCapProtocols_Type()
)
fcmPortCapProtocols.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcmPortCapProtocols.setStatus("current")


class _FcmPortOperProtocols_Type(Bits):
    """Custom type fcmPortOperProtocols based on Bits"""
    namedValues = NamedValues(
        *(("fabric", 2),
          ("ficon", 6),
          ("loop", 1),
          ("scsi", 3),
          ("tcpIp", 4),
          ("unknown", 0),
          ("vi", 5))
    )

_FcmPortOperProtocols_Type.__name__ = "Bits"
_FcmPortOperProtocols_Object = MibTableColumn
fcmPortOperProtocols = _FcmPortOperProtocols_Object(
    (1, 3, 6, 1, 2, 1, 10, 56, 1, 3, 1, 14),
    _FcmPortOperProtocols_Type()
)
fcmPortOperProtocols.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcmPortOperProtocols.setStatus("current")
_FcmPortStatsTable_Object = MibTable
fcmPortStatsTable = _FcmPortStatsTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 56, 1, 4)
)
if mibBuilder.loadTexts:
    fcmPortStatsTable.setStatus("current")
_FcmPortStatsEntry_Object = MibTableRow
fcmPortStatsEntry = _FcmPortStatsEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 56, 1, 4, 1)
)
if mibBuilder.loadTexts:
    fcmPortStatsEntry.setStatus("current")
_FcmPortBBCreditZeros_Type = Counter64
_FcmPortBBCreditZeros_Object = MibTableColumn
fcmPortBBCreditZeros = _FcmPortBBCreditZeros_Object(
    (1, 3, 6, 1, 2, 1, 10, 56, 1, 4, 1, 1),
    _FcmPortBBCreditZeros_Type()
)
fcmPortBBCreditZeros.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcmPortBBCreditZeros.setStatus("current")
_FcmPortFullInputBuffers_Type = Counter64
_FcmPortFullInputBuffers_Object = MibTableColumn
fcmPortFullInputBuffers = _FcmPortFullInputBuffers_Object(
    (1, 3, 6, 1, 2, 1, 10, 56, 1, 4, 1, 2),
    _FcmPortFullInputBuffers_Type()
)
fcmPortFullInputBuffers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcmPortFullInputBuffers.setStatus("current")
_FcmPortClass2RxFrames_Type = Counter64
_FcmPortClass2RxFrames_Object = MibTableColumn
fcmPortClass2RxFrames = _FcmPortClass2RxFrames_Object(
    (1, 3, 6, 1, 2, 1, 10, 56, 1, 4, 1, 3),
    _FcmPortClass2RxFrames_Type()
)
fcmPortClass2RxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcmPortClass2RxFrames.setStatus("current")
_FcmPortClass2RxOctets_Type = Counter64
_FcmPortClass2RxOctets_Object = MibTableColumn
fcmPortClass2RxOctets = _FcmPortClass2RxOctets_Object(
    (1, 3, 6, 1, 2, 1, 10, 56, 1, 4, 1, 4),
    _FcmPortClass2RxOctets_Type()
)
fcmPortClass2RxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcmPortClass2RxOctets.setStatus("current")
_FcmPortClass2TxFrames_Type = Counter64
_FcmPortClass2TxFrames_Object = MibTableColumn
fcmPortClass2TxFrames = _FcmPortClass2TxFrames_Object(
    (1, 3, 6, 1, 2, 1, 10, 56, 1, 4, 1, 5),
    _FcmPortClass2TxFrames_Type()
)
fcmPortClass2TxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcmPortClass2TxFrames.setStatus("current")
_FcmPortClass2TxOctets_Type = Counter64
_FcmPortClass2TxOctets_Object = MibTableColumn
fcmPortClass2TxOctets = _FcmPortClass2TxOctets_Object(
    (1, 3, 6, 1, 2, 1, 10, 56, 1, 4, 1, 6),
    _FcmPortClass2TxOctets_Type()
)
fcmPortClass2TxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcmPortClass2TxOctets.setStatus("current")
_FcmPortClass2Discards_Type = Counter64
_FcmPortClass2Discards_Object = MibTableColumn
fcmPortClass2Discards = _FcmPortClass2Discards_Object(
    (1, 3, 6, 1, 2, 1, 10, 56, 1, 4, 1, 7),
    _FcmPortClass2Discards_Type()
)
fcmPortClass2Discards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcmPortClass2Discards.setStatus("current")
_FcmPortClass2RxFbsyFrames_Type = Counter64
_FcmPortClass2RxFbsyFrames_Object = MibTableColumn
fcmPortClass2RxFbsyFrames = _FcmPortClass2RxFbsyFrames_Object(
    (1, 3, 6, 1, 2, 1, 10, 56, 1, 4, 1, 8),
    _FcmPortClass2RxFbsyFrames_Type()
)
fcmPortClass2RxFbsyFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcmPortClass2RxFbsyFrames.setStatus("current")
_FcmPortClass2RxPbsyFrames_Type = Counter64
_FcmPortClass2RxPbsyFrames_Object = MibTableColumn
fcmPortClass2RxPbsyFrames = _FcmPortClass2RxPbsyFrames_Object(
    (1, 3, 6, 1, 2, 1, 10, 56, 1, 4, 1, 9),
    _FcmPortClass2RxPbsyFrames_Type()
)
fcmPortClass2RxPbsyFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcmPortClass2RxPbsyFrames.setStatus("current")
_FcmPortClass2RxFrjtFrames_Type = Counter64
_FcmPortClass2RxFrjtFrames_Object = MibTableColumn
fcmPortClass2RxFrjtFrames = _FcmPortClass2RxFrjtFrames_Object(
    (1, 3, 6, 1, 2, 1, 10, 56, 1, 4, 1, 10),
    _FcmPortClass2RxFrjtFrames_Type()
)
fcmPortClass2RxFrjtFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcmPortClass2RxFrjtFrames.setStatus("current")
_FcmPortClass2RxPrjtFrames_Type = Counter64
_FcmPortClass2RxPrjtFrames_Object = MibTableColumn
fcmPortClass2RxPrjtFrames = _FcmPortClass2RxPrjtFrames_Object(
    (1, 3, 6, 1, 2, 1, 10, 56, 1, 4, 1, 11),
    _FcmPortClass2RxPrjtFrames_Type()
)
fcmPortClass2RxPrjtFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcmPortClass2RxPrjtFrames.setStatus("current")
_FcmPortClass2TxFbsyFrames_Type = Counter64
_FcmPortClass2TxFbsyFrames_Object = MibTableColumn
fcmPortClass2TxFbsyFrames = _FcmPortClass2TxFbsyFrames_Object(
    (1, 3, 6, 1, 2, 1, 10, 56, 1, 4, 1, 12),
    _FcmPortClass2TxFbsyFrames_Type()
)
fcmPortClass2TxFbsyFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcmPortClass2TxFbsyFrames.setStatus("current")
_FcmPortClass2TxPbsyFrames_Type = Counter64
_FcmPortClass2TxPbsyFrames_Object = MibTableColumn
fcmPortClass2TxPbsyFrames = _FcmPortClass2TxPbsyFrames_Object(
    (1, 3, 6, 1, 2, 1, 10, 56, 1, 4, 1, 13),
    _FcmPortClass2TxPbsyFrames_Type()
)
fcmPortClass2TxPbsyFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcmPortClass2TxPbsyFrames.setStatus("current")
_FcmPortClass2TxFrjtFrames_Type = Counter64
_FcmPortClass2TxFrjtFrames_Object = MibTableColumn
fcmPortClass2TxFrjtFrames = _FcmPortClass2TxFrjtFrames_Object(
    (1, 3, 6, 1, 2, 1, 10, 56, 1, 4, 1, 14),
    _FcmPortClass2TxFrjtFrames_Type()
)
fcmPortClass2TxFrjtFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcmPortClass2TxFrjtFrames.setStatus("current")
_FcmPortClass2TxPrjtFrames_Type = Counter64
_FcmPortClass2TxPrjtFrames_Object = MibTableColumn
fcmPortClass2TxPrjtFrames = _FcmPortClass2TxPrjtFrames_Object(
    (1, 3, 6, 1, 2, 1, 10, 56, 1, 4, 1, 15),
    _FcmPortClass2TxPrjtFrames_Type()
)
fcmPortClass2TxPrjtFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcmPortClass2TxPrjtFrames.setStatus("current")
_FcmPortClass3RxFrames_Type = Counter64
_FcmPortClass3RxFrames_Object = MibTableColumn
fcmPortClass3RxFrames = _FcmPortClass3RxFrames_Object(
    (1, 3, 6, 1, 2, 1, 10, 56, 1, 4, 1, 16),
    _FcmPortClass3RxFrames_Type()
)
fcmPortClass3RxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcmPortClass3RxFrames.setStatus("current")
_FcmPortClass3RxOctets_Type = Counter64
_FcmPortClass3RxOctets_Object = MibTableColumn
fcmPortClass3RxOctets = _FcmPortClass3RxOctets_Object(
    (1, 3, 6, 1, 2, 1, 10, 56, 1, 4, 1, 17),
    _FcmPortClass3RxOctets_Type()
)
fcmPortClass3RxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcmPortClass3RxOctets.setStatus("current")
_FcmPortClass3TxFrames_Type = Counter64
_FcmPortClass3TxFrames_Object = MibTableColumn
fcmPortClass3TxFrames = _FcmPortClass3TxFrames_Object(
    (1, 3, 6, 1, 2, 1, 10, 56, 1, 4, 1, 18),
    _FcmPortClass3TxFrames_Type()
)
fcmPortClass3TxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcmPortClass3TxFrames.setStatus("current")
_FcmPortClass3TxOctets_Type = Counter64
_FcmPortClass3TxOctets_Object = MibTableColumn
fcmPortClass3TxOctets = _FcmPortClass3TxOctets_Object(
    (1, 3, 6, 1, 2, 1, 10, 56, 1, 4, 1, 19),
    _FcmPortClass3TxOctets_Type()
)
fcmPortClass3TxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcmPortClass3TxOctets.setStatus("current")
_FcmPortClass3Discards_Type = Counter64
_FcmPortClass3Discards_Object = MibTableColumn
fcmPortClass3Discards = _FcmPortClass3Discards_Object(
    (1, 3, 6, 1, 2, 1, 10, 56, 1, 4, 1, 20),
    _FcmPortClass3Discards_Type()
)
fcmPortClass3Discards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcmPortClass3Discards.setStatus("current")
_FcmPortClassFRxFrames_Type = Counter32
_FcmPortClassFRxFrames_Object = MibTableColumn
fcmPortClassFRxFrames = _FcmPortClassFRxFrames_Object(
    (1, 3, 6, 1, 2, 1, 10, 56, 1, 4, 1, 21),
    _FcmPortClassFRxFrames_Type()
)
fcmPortClassFRxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcmPortClassFRxFrames.setStatus("current")
_FcmPortClassFRxOctets_Type = Counter32
_FcmPortClassFRxOctets_Object = MibTableColumn
fcmPortClassFRxOctets = _FcmPortClassFRxOctets_Object(
    (1, 3, 6, 1, 2, 1, 10, 56, 1, 4, 1, 22),
    _FcmPortClassFRxOctets_Type()
)
fcmPortClassFRxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcmPortClassFRxOctets.setStatus("current")
_FcmPortClassFTxFrames_Type = Counter32
_FcmPortClassFTxFrames_Object = MibTableColumn
fcmPortClassFTxFrames = _FcmPortClassFTxFrames_Object(
    (1, 3, 6, 1, 2, 1, 10, 56, 1, 4, 1, 23),
    _FcmPortClassFTxFrames_Type()
)
fcmPortClassFTxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcmPortClassFTxFrames.setStatus("current")
_FcmPortClassFTxOctets_Type = Counter32
_FcmPortClassFTxOctets_Object = MibTableColumn
fcmPortClassFTxOctets = _FcmPortClassFTxOctets_Object(
    (1, 3, 6, 1, 2, 1, 10, 56, 1, 4, 1, 24),
    _FcmPortClassFTxOctets_Type()
)
fcmPortClassFTxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcmPortClassFTxOctets.setStatus("current")
_FcmPortClassFDiscards_Type = Counter32
_FcmPortClassFDiscards_Object = MibTableColumn
fcmPortClassFDiscards = _FcmPortClassFDiscards_Object(
    (1, 3, 6, 1, 2, 1, 10, 56, 1, 4, 1, 25),
    _FcmPortClassFDiscards_Type()
)
fcmPortClassFDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcmPortClassFDiscards.setStatus("current")
_FcmPortLcStatsTable_Object = MibTable
fcmPortLcStatsTable = _FcmPortLcStatsTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 56, 1, 5)
)
if mibBuilder.loadTexts:
    fcmPortLcStatsTable.setStatus("current")
_FcmPortLcStatsEntry_Object = MibTableRow
fcmPortLcStatsEntry = _FcmPortLcStatsEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 56, 1, 5, 1)
)
if mibBuilder.loadTexts:
    fcmPortLcStatsEntry.setStatus("current")
_FcmPortLcBBCreditZeros_Type = Counter32
_FcmPortLcBBCreditZeros_Object = MibTableColumn
fcmPortLcBBCreditZeros = _FcmPortLcBBCreditZeros_Object(
    (1, 3, 6, 1, 2, 1, 10, 56, 1, 5, 1, 1),
    _FcmPortLcBBCreditZeros_Type()
)
fcmPortLcBBCreditZeros.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcmPortLcBBCreditZeros.setStatus("current")
_FcmPortLcFullInputBuffers_Type = Counter32
_FcmPortLcFullInputBuffers_Object = MibTableColumn
fcmPortLcFullInputBuffers = _FcmPortLcFullInputBuffers_Object(
    (1, 3, 6, 1, 2, 1, 10, 56, 1, 5, 1, 2),
    _FcmPortLcFullInputBuffers_Type()
)
fcmPortLcFullInputBuffers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcmPortLcFullInputBuffers.setStatus("current")
_FcmPortLcClass2RxFrames_Type = Counter32
_FcmPortLcClass2RxFrames_Object = MibTableColumn
fcmPortLcClass2RxFrames = _FcmPortLcClass2RxFrames_Object(
    (1, 3, 6, 1, 2, 1, 10, 56, 1, 5, 1, 3),
    _FcmPortLcClass2RxFrames_Type()
)
fcmPortLcClass2RxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcmPortLcClass2RxFrames.setStatus("current")
_FcmPortLcClass2RxOctets_Type = Counter32
_FcmPortLcClass2RxOctets_Object = MibTableColumn
fcmPortLcClass2RxOctets = _FcmPortLcClass2RxOctets_Object(
    (1, 3, 6, 1, 2, 1, 10, 56, 1, 5, 1, 4),
    _FcmPortLcClass2RxOctets_Type()
)
fcmPortLcClass2RxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcmPortLcClass2RxOctets.setStatus("current")
_FcmPortLcClass2TxFrames_Type = Counter32
_FcmPortLcClass2TxFrames_Object = MibTableColumn
fcmPortLcClass2TxFrames = _FcmPortLcClass2TxFrames_Object(
    (1, 3, 6, 1, 2, 1, 10, 56, 1, 5, 1, 5),
    _FcmPortLcClass2TxFrames_Type()
)
fcmPortLcClass2TxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcmPortLcClass2TxFrames.setStatus("current")
_FcmPortLcClass2TxOctets_Type = Counter32
_FcmPortLcClass2TxOctets_Object = MibTableColumn
fcmPortLcClass2TxOctets = _FcmPortLcClass2TxOctets_Object(
    (1, 3, 6, 1, 2, 1, 10, 56, 1, 5, 1, 6),
    _FcmPortLcClass2TxOctets_Type()
)
fcmPortLcClass2TxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcmPortLcClass2TxOctets.setStatus("current")
_FcmPortLcClass2Discards_Type = Counter32
_FcmPortLcClass2Discards_Object = MibTableColumn
fcmPortLcClass2Discards = _FcmPortLcClass2Discards_Object(
    (1, 3, 6, 1, 2, 1, 10, 56, 1, 5, 1, 7),
    _FcmPortLcClass2Discards_Type()
)
fcmPortLcClass2Discards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcmPortLcClass2Discards.setStatus("current")
_FcmPortLcClass2RxFbsyFrames_Type = Counter32
_FcmPortLcClass2RxFbsyFrames_Object = MibTableColumn
fcmPortLcClass2RxFbsyFrames = _FcmPortLcClass2RxFbsyFrames_Object(
    (1, 3, 6, 1, 2, 1, 10, 56, 1, 5, 1, 8),
    _FcmPortLcClass2RxFbsyFrames_Type()
)
fcmPortLcClass2RxFbsyFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcmPortLcClass2RxFbsyFrames.setStatus("current")
_FcmPortLcClass2RxPbsyFrames_Type = Counter32
_FcmPortLcClass2RxPbsyFrames_Object = MibTableColumn
fcmPortLcClass2RxPbsyFrames = _FcmPortLcClass2RxPbsyFrames_Object(
    (1, 3, 6, 1, 2, 1, 10, 56, 1, 5, 1, 9),
    _FcmPortLcClass2RxPbsyFrames_Type()
)
fcmPortLcClass2RxPbsyFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcmPortLcClass2RxPbsyFrames.setStatus("current")
_FcmPortLcClass2RxFrjtFrames_Type = Counter32
_FcmPortLcClass2RxFrjtFrames_Object = MibTableColumn
fcmPortLcClass2RxFrjtFrames = _FcmPortLcClass2RxFrjtFrames_Object(
    (1, 3, 6, 1, 2, 1, 10, 56, 1, 5, 1, 10),
    _FcmPortLcClass2RxFrjtFrames_Type()
)
fcmPortLcClass2RxFrjtFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcmPortLcClass2RxFrjtFrames.setStatus("current")
_FcmPortLcClass2RxPrjtFrames_Type = Counter32
_FcmPortLcClass2RxPrjtFrames_Object = MibTableColumn
fcmPortLcClass2RxPrjtFrames = _FcmPortLcClass2RxPrjtFrames_Object(
    (1, 3, 6, 1, 2, 1, 10, 56, 1, 5, 1, 11),
    _FcmPortLcClass2RxPrjtFrames_Type()
)
fcmPortLcClass2RxPrjtFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcmPortLcClass2RxPrjtFrames.setStatus("current")
_FcmPortLcClass2TxFbsyFrames_Type = Counter32
_FcmPortLcClass2TxFbsyFrames_Object = MibTableColumn
fcmPortLcClass2TxFbsyFrames = _FcmPortLcClass2TxFbsyFrames_Object(
    (1, 3, 6, 1, 2, 1, 10, 56, 1, 5, 1, 12),
    _FcmPortLcClass2TxFbsyFrames_Type()
)
fcmPortLcClass2TxFbsyFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcmPortLcClass2TxFbsyFrames.setStatus("current")
_FcmPortLcClass2TxPbsyFrames_Type = Counter32
_FcmPortLcClass2TxPbsyFrames_Object = MibTableColumn
fcmPortLcClass2TxPbsyFrames = _FcmPortLcClass2TxPbsyFrames_Object(
    (1, 3, 6, 1, 2, 1, 10, 56, 1, 5, 1, 13),
    _FcmPortLcClass2TxPbsyFrames_Type()
)
fcmPortLcClass2TxPbsyFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcmPortLcClass2TxPbsyFrames.setStatus("current")
_FcmPortLcClass2TxFrjtFrames_Type = Counter32
_FcmPortLcClass2TxFrjtFrames_Object = MibTableColumn
fcmPortLcClass2TxFrjtFrames = _FcmPortLcClass2TxFrjtFrames_Object(
    (1, 3, 6, 1, 2, 1, 10, 56, 1, 5, 1, 14),
    _FcmPortLcClass2TxFrjtFrames_Type()
)
fcmPortLcClass2TxFrjtFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcmPortLcClass2TxFrjtFrames.setStatus("current")
_FcmPortLcClass2TxPrjtFrames_Type = Counter32
_FcmPortLcClass2TxPrjtFrames_Object = MibTableColumn
fcmPortLcClass2TxPrjtFrames = _FcmPortLcClass2TxPrjtFrames_Object(
    (1, 3, 6, 1, 2, 1, 10, 56, 1, 5, 1, 15),
    _FcmPortLcClass2TxPrjtFrames_Type()
)
fcmPortLcClass2TxPrjtFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcmPortLcClass2TxPrjtFrames.setStatus("current")
_FcmPortLcClass3RxFrames_Type = Counter32
_FcmPortLcClass3RxFrames_Object = MibTableColumn
fcmPortLcClass3RxFrames = _FcmPortLcClass3RxFrames_Object(
    (1, 3, 6, 1, 2, 1, 10, 56, 1, 5, 1, 16),
    _FcmPortLcClass3RxFrames_Type()
)
fcmPortLcClass3RxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcmPortLcClass3RxFrames.setStatus("current")
_FcmPortLcClass3RxOctets_Type = Counter32
_FcmPortLcClass3RxOctets_Object = MibTableColumn
fcmPortLcClass3RxOctets = _FcmPortLcClass3RxOctets_Object(
    (1, 3, 6, 1, 2, 1, 10, 56, 1, 5, 1, 17),
    _FcmPortLcClass3RxOctets_Type()
)
fcmPortLcClass3RxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcmPortLcClass3RxOctets.setStatus("current")
_FcmPortLcClass3TxFrames_Type = Counter32
_FcmPortLcClass3TxFrames_Object = MibTableColumn
fcmPortLcClass3TxFrames = _FcmPortLcClass3TxFrames_Object(
    (1, 3, 6, 1, 2, 1, 10, 56, 1, 5, 1, 18),
    _FcmPortLcClass3TxFrames_Type()
)
fcmPortLcClass3TxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcmPortLcClass3TxFrames.setStatus("current")
_FcmPortLcClass3TxOctets_Type = Counter32
_FcmPortLcClass3TxOctets_Object = MibTableColumn
fcmPortLcClass3TxOctets = _FcmPortLcClass3TxOctets_Object(
    (1, 3, 6, 1, 2, 1, 10, 56, 1, 5, 1, 19),
    _FcmPortLcClass3TxOctets_Type()
)
fcmPortLcClass3TxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcmPortLcClass3TxOctets.setStatus("current")
_FcmPortLcClass3Discards_Type = Counter32
_FcmPortLcClass3Discards_Object = MibTableColumn
fcmPortLcClass3Discards = _FcmPortLcClass3Discards_Object(
    (1, 3, 6, 1, 2, 1, 10, 56, 1, 5, 1, 20),
    _FcmPortLcClass3Discards_Type()
)
fcmPortLcClass3Discards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcmPortLcClass3Discards.setStatus("current")
_FcmPortErrorsTable_Object = MibTable
fcmPortErrorsTable = _FcmPortErrorsTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 56, 1, 6)
)
if mibBuilder.loadTexts:
    fcmPortErrorsTable.setStatus("current")
_FcmPortErrorsEntry_Object = MibTableRow
fcmPortErrorsEntry = _FcmPortErrorsEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 56, 1, 6, 1)
)
if mibBuilder.loadTexts:
    fcmPortErrorsEntry.setStatus("current")
_FcmPortRxLinkResets_Type = Counter32
_FcmPortRxLinkResets_Object = MibTableColumn
fcmPortRxLinkResets = _FcmPortRxLinkResets_Object(
    (1, 3, 6, 1, 2, 1, 10, 56, 1, 6, 1, 1),
    _FcmPortRxLinkResets_Type()
)
fcmPortRxLinkResets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcmPortRxLinkResets.setStatus("current")
_FcmPortTxLinkResets_Type = Counter32
_FcmPortTxLinkResets_Object = MibTableColumn
fcmPortTxLinkResets = _FcmPortTxLinkResets_Object(
    (1, 3, 6, 1, 2, 1, 10, 56, 1, 6, 1, 2),
    _FcmPortTxLinkResets_Type()
)
fcmPortTxLinkResets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcmPortTxLinkResets.setStatus("current")
_FcmPortLinkResets_Type = Counter32
_FcmPortLinkResets_Object = MibTableColumn
fcmPortLinkResets = _FcmPortLinkResets_Object(
    (1, 3, 6, 1, 2, 1, 10, 56, 1, 6, 1, 3),
    _FcmPortLinkResets_Type()
)
fcmPortLinkResets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcmPortLinkResets.setStatus("current")
_FcmPortRxOfflineSequences_Type = Counter32
_FcmPortRxOfflineSequences_Object = MibTableColumn
fcmPortRxOfflineSequences = _FcmPortRxOfflineSequences_Object(
    (1, 3, 6, 1, 2, 1, 10, 56, 1, 6, 1, 4),
    _FcmPortRxOfflineSequences_Type()
)
fcmPortRxOfflineSequences.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcmPortRxOfflineSequences.setStatus("current")
_FcmPortTxOfflineSequences_Type = Counter32
_FcmPortTxOfflineSequences_Object = MibTableColumn
fcmPortTxOfflineSequences = _FcmPortTxOfflineSequences_Object(
    (1, 3, 6, 1, 2, 1, 10, 56, 1, 6, 1, 5),
    _FcmPortTxOfflineSequences_Type()
)
fcmPortTxOfflineSequences.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcmPortTxOfflineSequences.setStatus("current")
_FcmPortLinkFailures_Type = Counter32
_FcmPortLinkFailures_Object = MibTableColumn
fcmPortLinkFailures = _FcmPortLinkFailures_Object(
    (1, 3, 6, 1, 2, 1, 10, 56, 1, 6, 1, 6),
    _FcmPortLinkFailures_Type()
)
fcmPortLinkFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcmPortLinkFailures.setStatus("current")
_FcmPortLossofSynchs_Type = Counter32
_FcmPortLossofSynchs_Object = MibTableColumn
fcmPortLossofSynchs = _FcmPortLossofSynchs_Object(
    (1, 3, 6, 1, 2, 1, 10, 56, 1, 6, 1, 7),
    _FcmPortLossofSynchs_Type()
)
fcmPortLossofSynchs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcmPortLossofSynchs.setStatus("current")
_FcmPortLossofSignals_Type = Counter32
_FcmPortLossofSignals_Object = MibTableColumn
fcmPortLossofSignals = _FcmPortLossofSignals_Object(
    (1, 3, 6, 1, 2, 1, 10, 56, 1, 6, 1, 8),
    _FcmPortLossofSignals_Type()
)
fcmPortLossofSignals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcmPortLossofSignals.setStatus("current")
_FcmPortPrimSeqProtocolErrors_Type = Counter32
_FcmPortPrimSeqProtocolErrors_Object = MibTableColumn
fcmPortPrimSeqProtocolErrors = _FcmPortPrimSeqProtocolErrors_Object(
    (1, 3, 6, 1, 2, 1, 10, 56, 1, 6, 1, 9),
    _FcmPortPrimSeqProtocolErrors_Type()
)
fcmPortPrimSeqProtocolErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcmPortPrimSeqProtocolErrors.setStatus("current")
_FcmPortInvalidTxWords_Type = Counter32
_FcmPortInvalidTxWords_Object = MibTableColumn
fcmPortInvalidTxWords = _FcmPortInvalidTxWords_Object(
    (1, 3, 6, 1, 2, 1, 10, 56, 1, 6, 1, 10),
    _FcmPortInvalidTxWords_Type()
)
fcmPortInvalidTxWords.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcmPortInvalidTxWords.setStatus("current")
_FcmPortInvalidCRCs_Type = Counter32
_FcmPortInvalidCRCs_Object = MibTableColumn
fcmPortInvalidCRCs = _FcmPortInvalidCRCs_Object(
    (1, 3, 6, 1, 2, 1, 10, 56, 1, 6, 1, 11),
    _FcmPortInvalidCRCs_Type()
)
fcmPortInvalidCRCs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcmPortInvalidCRCs.setStatus("current")
_FcmPortInvalidOrderedSets_Type = Counter32
_FcmPortInvalidOrderedSets_Object = MibTableColumn
fcmPortInvalidOrderedSets = _FcmPortInvalidOrderedSets_Object(
    (1, 3, 6, 1, 2, 1, 10, 56, 1, 6, 1, 12),
    _FcmPortInvalidOrderedSets_Type()
)
fcmPortInvalidOrderedSets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcmPortInvalidOrderedSets.setStatus("current")
_FcmPortFrameTooLongs_Type = Counter32
_FcmPortFrameTooLongs_Object = MibTableColumn
fcmPortFrameTooLongs = _FcmPortFrameTooLongs_Object(
    (1, 3, 6, 1, 2, 1, 10, 56, 1, 6, 1, 13),
    _FcmPortFrameTooLongs_Type()
)
fcmPortFrameTooLongs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcmPortFrameTooLongs.setStatus("current")
_FcmPortTruncatedFrames_Type = Counter32
_FcmPortTruncatedFrames_Object = MibTableColumn
fcmPortTruncatedFrames = _FcmPortTruncatedFrames_Object(
    (1, 3, 6, 1, 2, 1, 10, 56, 1, 6, 1, 14),
    _FcmPortTruncatedFrames_Type()
)
fcmPortTruncatedFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcmPortTruncatedFrames.setStatus("current")
_FcmPortAddressErrors_Type = Counter32
_FcmPortAddressErrors_Object = MibTableColumn
fcmPortAddressErrors = _FcmPortAddressErrors_Object(
    (1, 3, 6, 1, 2, 1, 10, 56, 1, 6, 1, 15),
    _FcmPortAddressErrors_Type()
)
fcmPortAddressErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcmPortAddressErrors.setStatus("current")
_FcmPortDelimiterErrors_Type = Counter32
_FcmPortDelimiterErrors_Object = MibTableColumn
fcmPortDelimiterErrors = _FcmPortDelimiterErrors_Object(
    (1, 3, 6, 1, 2, 1, 10, 56, 1, 6, 1, 16),
    _FcmPortDelimiterErrors_Type()
)
fcmPortDelimiterErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcmPortDelimiterErrors.setStatus("current")
_FcmPortEncodingDisparityErrors_Type = Counter32
_FcmPortEncodingDisparityErrors_Object = MibTableColumn
fcmPortEncodingDisparityErrors = _FcmPortEncodingDisparityErrors_Object(
    (1, 3, 6, 1, 2, 1, 10, 56, 1, 6, 1, 17),
    _FcmPortEncodingDisparityErrors_Type()
)
fcmPortEncodingDisparityErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcmPortEncodingDisparityErrors.setStatus("current")
_FcmPortOtherErrors_Type = Counter32
_FcmPortOtherErrors_Object = MibTableColumn
fcmPortOtherErrors = _FcmPortOtherErrors_Object(
    (1, 3, 6, 1, 2, 1, 10, 56, 1, 6, 1, 18),
    _FcmPortOtherErrors_Type()
)
fcmPortOtherErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcmPortOtherErrors.setStatus("current")
_FcmFxPortTable_Object = MibTable
fcmFxPortTable = _FcmFxPortTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 56, 1, 7)
)
if mibBuilder.loadTexts:
    fcmFxPortTable.setStatus("current")
_FcmFxPortEntry_Object = MibTableRow
fcmFxPortEntry = _FcmFxPortEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 56, 1, 7, 1)
)
fcmFxPortEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    fcmFxPortEntry.setStatus("current")
_FcmFxPortRatov_Type = Unsigned32
_FcmFxPortRatov_Object = MibTableColumn
fcmFxPortRatov = _FcmFxPortRatov_Object(
    (1, 3, 6, 1, 2, 1, 10, 56, 1, 7, 1, 1),
    _FcmFxPortRatov_Type()
)
fcmFxPortRatov.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcmFxPortRatov.setStatus("current")
if mibBuilder.loadTexts:
    fcmFxPortRatov.setUnits("milliseconds")
_FcmFxPortEdtov_Type = Unsigned32
_FcmFxPortEdtov_Object = MibTableColumn
fcmFxPortEdtov = _FcmFxPortEdtov_Object(
    (1, 3, 6, 1, 2, 1, 10, 56, 1, 7, 1, 2),
    _FcmFxPortEdtov_Type()
)
fcmFxPortEdtov.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcmFxPortEdtov.setStatus("current")
if mibBuilder.loadTexts:
    fcmFxPortEdtov.setUnits("milliseconds")
_FcmFxPortRttov_Type = Unsigned32
_FcmFxPortRttov_Object = MibTableColumn
fcmFxPortRttov = _FcmFxPortRttov_Object(
    (1, 3, 6, 1, 2, 1, 10, 56, 1, 7, 1, 3),
    _FcmFxPortRttov_Type()
)
fcmFxPortRttov.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcmFxPortRttov.setStatus("current")
if mibBuilder.loadTexts:
    fcmFxPortRttov.setUnits("milliseconds")
_FcmFxPortHoldTime_Type = Unsigned32
_FcmFxPortHoldTime_Object = MibTableColumn
fcmFxPortHoldTime = _FcmFxPortHoldTime_Object(
    (1, 3, 6, 1, 2, 1, 10, 56, 1, 7, 1, 4),
    _FcmFxPortHoldTime_Type()
)
fcmFxPortHoldTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcmFxPortHoldTime.setStatus("current")
if mibBuilder.loadTexts:
    fcmFxPortHoldTime.setUnits("microseconds")
_FcmFxPortCapBbCreditMax_Type = FcBbCredit
_FcmFxPortCapBbCreditMax_Object = MibTableColumn
fcmFxPortCapBbCreditMax = _FcmFxPortCapBbCreditMax_Object(
    (1, 3, 6, 1, 2, 1, 10, 56, 1, 7, 1, 5),
    _FcmFxPortCapBbCreditMax_Type()
)
fcmFxPortCapBbCreditMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcmFxPortCapBbCreditMax.setStatus("current")
if mibBuilder.loadTexts:
    fcmFxPortCapBbCreditMax.setUnits("buffers")
_FcmFxPortCapBbCreditMin_Type = FcBbCredit
_FcmFxPortCapBbCreditMin_Object = MibTableColumn
fcmFxPortCapBbCreditMin = _FcmFxPortCapBbCreditMin_Object(
    (1, 3, 6, 1, 2, 1, 10, 56, 1, 7, 1, 6),
    _FcmFxPortCapBbCreditMin_Type()
)
fcmFxPortCapBbCreditMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcmFxPortCapBbCreditMin.setStatus("current")
if mibBuilder.loadTexts:
    fcmFxPortCapBbCreditMin.setUnits("buffers")
_FcmFxPortCapDataFieldSizeMax_Type = FcDataFieldSize
_FcmFxPortCapDataFieldSizeMax_Object = MibTableColumn
fcmFxPortCapDataFieldSizeMax = _FcmFxPortCapDataFieldSizeMax_Object(
    (1, 3, 6, 1, 2, 1, 10, 56, 1, 7, 1, 7),
    _FcmFxPortCapDataFieldSizeMax_Type()
)
fcmFxPortCapDataFieldSizeMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcmFxPortCapDataFieldSizeMax.setStatus("current")
if mibBuilder.loadTexts:
    fcmFxPortCapDataFieldSizeMax.setUnits("bytes")
_FcmFxPortCapDataFieldSizeMin_Type = FcDataFieldSize
_FcmFxPortCapDataFieldSizeMin_Object = MibTableColumn
fcmFxPortCapDataFieldSizeMin = _FcmFxPortCapDataFieldSizeMin_Object(
    (1, 3, 6, 1, 2, 1, 10, 56, 1, 7, 1, 8),
    _FcmFxPortCapDataFieldSizeMin_Type()
)
fcmFxPortCapDataFieldSizeMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcmFxPortCapDataFieldSizeMin.setStatus("current")
if mibBuilder.loadTexts:
    fcmFxPortCapDataFieldSizeMin.setUnits("bytes")
_FcmFxPortCapClass2SeqDeliv_Type = TruthValue
_FcmFxPortCapClass2SeqDeliv_Object = MibTableColumn
fcmFxPortCapClass2SeqDeliv = _FcmFxPortCapClass2SeqDeliv_Object(
    (1, 3, 6, 1, 2, 1, 10, 56, 1, 7, 1, 9),
    _FcmFxPortCapClass2SeqDeliv_Type()
)
fcmFxPortCapClass2SeqDeliv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcmFxPortCapClass2SeqDeliv.setStatus("current")
_FcmFxPortCapClass3SeqDeliv_Type = TruthValue
_FcmFxPortCapClass3SeqDeliv_Object = MibTableColumn
fcmFxPortCapClass3SeqDeliv = _FcmFxPortCapClass3SeqDeliv_Object(
    (1, 3, 6, 1, 2, 1, 10, 56, 1, 7, 1, 10),
    _FcmFxPortCapClass3SeqDeliv_Type()
)
fcmFxPortCapClass3SeqDeliv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcmFxPortCapClass3SeqDeliv.setStatus("current")
_FcmFxPortCapHoldTimeMax_Type = Unsigned32
_FcmFxPortCapHoldTimeMax_Object = MibTableColumn
fcmFxPortCapHoldTimeMax = _FcmFxPortCapHoldTimeMax_Object(
    (1, 3, 6, 1, 2, 1, 10, 56, 1, 7, 1, 11),
    _FcmFxPortCapHoldTimeMax_Type()
)
fcmFxPortCapHoldTimeMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcmFxPortCapHoldTimeMax.setStatus("current")
if mibBuilder.loadTexts:
    fcmFxPortCapHoldTimeMax.setUnits("microseconds")
_FcmFxPortCapHoldTimeMin_Type = Unsigned32
_FcmFxPortCapHoldTimeMin_Object = MibTableColumn
fcmFxPortCapHoldTimeMin = _FcmFxPortCapHoldTimeMin_Object(
    (1, 3, 6, 1, 2, 1, 10, 56, 1, 7, 1, 12),
    _FcmFxPortCapHoldTimeMin_Type()
)
fcmFxPortCapHoldTimeMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcmFxPortCapHoldTimeMin.setStatus("current")
if mibBuilder.loadTexts:
    fcmFxPortCapHoldTimeMin.setUnits("microseconds")
_FcmISPortTable_Object = MibTable
fcmISPortTable = _FcmISPortTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 56, 1, 8)
)
if mibBuilder.loadTexts:
    fcmISPortTable.setStatus("current")
_FcmISPortEntry_Object = MibTableRow
fcmISPortEntry = _FcmISPortEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 56, 1, 8, 1)
)
fcmISPortEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    fcmISPortEntry.setStatus("current")
_FcmISPortClassFCredit_Type = FcBbCredit
_FcmISPortClassFCredit_Object = MibTableColumn
fcmISPortClassFCredit = _FcmISPortClassFCredit_Object(
    (1, 3, 6, 1, 2, 1, 10, 56, 1, 8, 1, 1),
    _FcmISPortClassFCredit_Type()
)
fcmISPortClassFCredit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fcmISPortClassFCredit.setStatus("current")
_FcmISPortClassFDataFieldSize_Type = FcDataFieldSize
_FcmISPortClassFDataFieldSize_Object = MibTableColumn
fcmISPortClassFDataFieldSize = _FcmISPortClassFDataFieldSize_Object(
    (1, 3, 6, 1, 2, 1, 10, 56, 1, 8, 1, 2),
    _FcmISPortClassFDataFieldSize_Type()
)
fcmISPortClassFDataFieldSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcmISPortClassFDataFieldSize.setStatus("current")
if mibBuilder.loadTexts:
    fcmISPortClassFDataFieldSize.setUnits("bytes")
_FcmFLoginTable_Object = MibTable
fcmFLoginTable = _FcmFLoginTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 56, 1, 9)
)
if mibBuilder.loadTexts:
    fcmFLoginTable.setStatus("current")
_FcmFLoginEntry_Object = MibTableRow
fcmFLoginEntry = _FcmFLoginEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 56, 1, 9, 1)
)
fcmFLoginEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "FC-MGMT-MIB", "fcmFLoginNxPortIndex"),
)
if mibBuilder.loadTexts:
    fcmFLoginEntry.setStatus("current")


class _FcmFLoginNxPortIndex_Type(Unsigned32):
    """Custom type fcmFLoginNxPortIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_FcmFLoginNxPortIndex_Type.__name__ = "Unsigned32"
_FcmFLoginNxPortIndex_Object = MibTableColumn
fcmFLoginNxPortIndex = _FcmFLoginNxPortIndex_Object(
    (1, 3, 6, 1, 2, 1, 10, 56, 1, 9, 1, 1),
    _FcmFLoginNxPortIndex_Type()
)
fcmFLoginNxPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fcmFLoginNxPortIndex.setStatus("current")
_FcmFLoginPortWwn_Type = FcNameIdOrZero
_FcmFLoginPortWwn_Object = MibTableColumn
fcmFLoginPortWwn = _FcmFLoginPortWwn_Object(
    (1, 3, 6, 1, 2, 1, 10, 56, 1, 9, 1, 2),
    _FcmFLoginPortWwn_Type()
)
fcmFLoginPortWwn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcmFLoginPortWwn.setStatus("current")
_FcmFLoginNodeWwn_Type = FcNameIdOrZero
_FcmFLoginNodeWwn_Object = MibTableColumn
fcmFLoginNodeWwn = _FcmFLoginNodeWwn_Object(
    (1, 3, 6, 1, 2, 1, 10, 56, 1, 9, 1, 3),
    _FcmFLoginNodeWwn_Type()
)
fcmFLoginNodeWwn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcmFLoginNodeWwn.setStatus("current")
_FcmFLoginBbCreditModel_Type = FcBbCreditModel
_FcmFLoginBbCreditModel_Object = MibTableColumn
fcmFLoginBbCreditModel = _FcmFLoginBbCreditModel_Object(
    (1, 3, 6, 1, 2, 1, 10, 56, 1, 9, 1, 4),
    _FcmFLoginBbCreditModel_Type()
)
fcmFLoginBbCreditModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcmFLoginBbCreditModel.setStatus("current")
_FcmFLoginBbCredit_Type = FcBbCredit
_FcmFLoginBbCredit_Object = MibTableColumn
fcmFLoginBbCredit = _FcmFLoginBbCredit_Object(
    (1, 3, 6, 1, 2, 1, 10, 56, 1, 9, 1, 5),
    _FcmFLoginBbCredit_Type()
)
fcmFLoginBbCredit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcmFLoginBbCredit.setStatus("current")
_FcmFLoginClassesAgreed_Type = FcClasses
_FcmFLoginClassesAgreed_Object = MibTableColumn
fcmFLoginClassesAgreed = _FcmFLoginClassesAgreed_Object(
    (1, 3, 6, 1, 2, 1, 10, 56, 1, 9, 1, 6),
    _FcmFLoginClassesAgreed_Type()
)
fcmFLoginClassesAgreed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcmFLoginClassesAgreed.setStatus("current")
_FcmFLoginClass2SeqDelivAgreed_Type = TruthValue
_FcmFLoginClass2SeqDelivAgreed_Object = MibTableColumn
fcmFLoginClass2SeqDelivAgreed = _FcmFLoginClass2SeqDelivAgreed_Object(
    (1, 3, 6, 1, 2, 1, 10, 56, 1, 9, 1, 7),
    _FcmFLoginClass2SeqDelivAgreed_Type()
)
fcmFLoginClass2SeqDelivAgreed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcmFLoginClass2SeqDelivAgreed.setStatus("current")
_FcmFLoginClass2DataFieldSize_Type = FcDataFieldSize
_FcmFLoginClass2DataFieldSize_Object = MibTableColumn
fcmFLoginClass2DataFieldSize = _FcmFLoginClass2DataFieldSize_Object(
    (1, 3, 6, 1, 2, 1, 10, 56, 1, 9, 1, 8),
    _FcmFLoginClass2DataFieldSize_Type()
)
fcmFLoginClass2DataFieldSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcmFLoginClass2DataFieldSize.setStatus("current")
_FcmFLoginClass3SeqDelivAgreed_Type = TruthValue
_FcmFLoginClass3SeqDelivAgreed_Object = MibTableColumn
fcmFLoginClass3SeqDelivAgreed = _FcmFLoginClass3SeqDelivAgreed_Object(
    (1, 3, 6, 1, 2, 1, 10, 56, 1, 9, 1, 9),
    _FcmFLoginClass3SeqDelivAgreed_Type()
)
fcmFLoginClass3SeqDelivAgreed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcmFLoginClass3SeqDelivAgreed.setStatus("current")
_FcmFLoginClass3DataFieldSize_Type = FcDataFieldSize
_FcmFLoginClass3DataFieldSize_Object = MibTableColumn
fcmFLoginClass3DataFieldSize = _FcmFLoginClass3DataFieldSize_Object(
    (1, 3, 6, 1, 2, 1, 10, 56, 1, 9, 1, 10),
    _FcmFLoginClass3DataFieldSize_Type()
)
fcmFLoginClass3DataFieldSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcmFLoginClass3DataFieldSize.setStatus("current")
_FcmLinkTable_Object = MibTable
fcmLinkTable = _FcmLinkTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 56, 1, 10)
)
if mibBuilder.loadTexts:
    fcmLinkTable.setStatus("current")
_FcmLinkEntry_Object = MibTableRow
fcmLinkEntry = _FcmLinkEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 56, 1, 10, 1)
)
fcmLinkEntry.setIndexNames(
    (0, "FC-MGMT-MIB", "fcmInstanceIndex"),
    (0, "FC-MGMT-MIB", "fcmLinkIndex"),
)
if mibBuilder.loadTexts:
    fcmLinkEntry.setStatus("current")


class _FcmLinkIndex_Type(Unsigned32):
    """Custom type fcmLinkIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_FcmLinkIndex_Type.__name__ = "Unsigned32"
_FcmLinkIndex_Object = MibTableColumn
fcmLinkIndex = _FcmLinkIndex_Object(
    (1, 3, 6, 1, 2, 1, 10, 56, 1, 10, 1, 1),
    _FcmLinkIndex_Type()
)
fcmLinkIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fcmLinkIndex.setStatus("current")
_FcmLinkEnd1NodeWwn_Type = FcNameIdOrZero
_FcmLinkEnd1NodeWwn_Object = MibTableColumn
fcmLinkEnd1NodeWwn = _FcmLinkEnd1NodeWwn_Object(
    (1, 3, 6, 1, 2, 1, 10, 56, 1, 10, 1, 2),
    _FcmLinkEnd1NodeWwn_Type()
)
fcmLinkEnd1NodeWwn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcmLinkEnd1NodeWwn.setStatus("current")
_FcmLinkEnd1PhysPortNumber_Type = Unsigned32
_FcmLinkEnd1PhysPortNumber_Object = MibTableColumn
fcmLinkEnd1PhysPortNumber = _FcmLinkEnd1PhysPortNumber_Object(
    (1, 3, 6, 1, 2, 1, 10, 56, 1, 10, 1, 3),
    _FcmLinkEnd1PhysPortNumber_Type()
)
fcmLinkEnd1PhysPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcmLinkEnd1PhysPortNumber.setStatus("current")
_FcmLinkEnd1PortWwn_Type = FcNameIdOrZero
_FcmLinkEnd1PortWwn_Object = MibTableColumn
fcmLinkEnd1PortWwn = _FcmLinkEnd1PortWwn_Object(
    (1, 3, 6, 1, 2, 1, 10, 56, 1, 10, 1, 4),
    _FcmLinkEnd1PortWwn_Type()
)
fcmLinkEnd1PortWwn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcmLinkEnd1PortWwn.setStatus("current")
_FcmLinkEnd2NodeWwn_Type = FcNameIdOrZero
_FcmLinkEnd2NodeWwn_Object = MibTableColumn
fcmLinkEnd2NodeWwn = _FcmLinkEnd2NodeWwn_Object(
    (1, 3, 6, 1, 2, 1, 10, 56, 1, 10, 1, 5),
    _FcmLinkEnd2NodeWwn_Type()
)
fcmLinkEnd2NodeWwn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcmLinkEnd2NodeWwn.setStatus("current")
_FcmLinkEnd2PhysPortNumber_Type = Unsigned32
_FcmLinkEnd2PhysPortNumber_Object = MibTableColumn
fcmLinkEnd2PhysPortNumber = _FcmLinkEnd2PhysPortNumber_Object(
    (1, 3, 6, 1, 2, 1, 10, 56, 1, 10, 1, 6),
    _FcmLinkEnd2PhysPortNumber_Type()
)
fcmLinkEnd2PhysPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcmLinkEnd2PhysPortNumber.setStatus("current")
_FcmLinkEnd2PortWwn_Type = FcNameIdOrZero
_FcmLinkEnd2PortWwn_Object = MibTableColumn
fcmLinkEnd2PortWwn = _FcmLinkEnd2PortWwn_Object(
    (1, 3, 6, 1, 2, 1, 10, 56, 1, 10, 1, 7),
    _FcmLinkEnd2PortWwn_Type()
)
fcmLinkEnd2PortWwn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcmLinkEnd2PortWwn.setStatus("current")
_FcmLinkEnd2AgentAddress_Type = SnmpAdminString
_FcmLinkEnd2AgentAddress_Object = MibTableColumn
fcmLinkEnd2AgentAddress = _FcmLinkEnd2AgentAddress_Object(
    (1, 3, 6, 1, 2, 1, 10, 56, 1, 10, 1, 8),
    _FcmLinkEnd2AgentAddress_Type()
)
fcmLinkEnd2AgentAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcmLinkEnd2AgentAddress.setStatus("current")
_FcmLinkEnd2PortType_Type = FcPortType
_FcmLinkEnd2PortType_Object = MibTableColumn
fcmLinkEnd2PortType = _FcmLinkEnd2PortType_Object(
    (1, 3, 6, 1, 2, 1, 10, 56, 1, 10, 1, 9),
    _FcmLinkEnd2PortType_Type()
)
fcmLinkEnd2PortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcmLinkEnd2PortType.setStatus("current")
_FcmLinkEnd2UnitType_Type = FcUnitFunctions
_FcmLinkEnd2UnitType_Object = MibTableColumn
fcmLinkEnd2UnitType = _FcmLinkEnd2UnitType_Object(
    (1, 3, 6, 1, 2, 1, 10, 56, 1, 10, 1, 10),
    _FcmLinkEnd2UnitType_Type()
)
fcmLinkEnd2UnitType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcmLinkEnd2UnitType.setStatus("current")
_FcmLinkEnd2FcAddressId_Type = FcAddressIdOrZero
_FcmLinkEnd2FcAddressId_Object = MibTableColumn
fcmLinkEnd2FcAddressId = _FcmLinkEnd2FcAddressId_Object(
    (1, 3, 6, 1, 2, 1, 10, 56, 1, 10, 1, 11),
    _FcmLinkEnd2FcAddressId_Type()
)
fcmLinkEnd2FcAddressId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcmLinkEnd2FcAddressId.setStatus("current")
_FcmgmtNotifications_ObjectIdentity = ObjectIdentity
fcmgmtNotifications = _FcmgmtNotifications_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 56, 2)
)
_FcmgmtNotifPrefix_ObjectIdentity = ObjectIdentity
fcmgmtNotifPrefix = _FcmgmtNotifPrefix_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 56, 2, 0)
)
_FcmgmtConformance_ObjectIdentity = ObjectIdentity
fcmgmtConformance = _FcmgmtConformance_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 56, 3)
)
_FcmgmtCompliances_ObjectIdentity = ObjectIdentity
fcmgmtCompliances = _FcmgmtCompliances_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 56, 3, 1)
)
_FcmgmtGroups_ObjectIdentity = ObjectIdentity
fcmgmtGroups = _FcmgmtGroups_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 56, 3, 2)
)
fcmPortEntry.registerAugmentions(
    ("FC-MGMT-MIB",
     "fcmPortStatsEntry")
)
fcmPortStatsEntry.setIndexNames(*fcmPortEntry.getIndexNames())
fcmPortEntry.registerAugmentions(
    ("FC-MGMT-MIB",
     "fcmPortLcStatsEntry")
)
fcmPortLcStatsEntry.setIndexNames(*fcmPortEntry.getIndexNames())
fcmPortEntry.registerAugmentions(
    ("FC-MGMT-MIB",
     "fcmPortErrorsEntry")
)
fcmPortErrorsEntry.setIndexNames(*fcmPortEntry.getIndexNames())

# Managed Objects groups

fcmInstanceBasicGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 56, 3, 2, 1)
)
fcmInstanceBasicGroup.setObjects(
      *(("FC-MGMT-MIB", "fcmInstanceWwn"),
        ("FC-MGMT-MIB", "fcmInstanceFunctions"),
        ("FC-MGMT-MIB", "fcmInstancePhysicalIndex"),
        ("FC-MGMT-MIB", "fcmInstanceSoftwareIndex"),
        ("FC-MGMT-MIB", "fcmInstanceStatus"),
        ("FC-MGMT-MIB", "fcmInstanceTextName"),
        ("FC-MGMT-MIB", "fcmInstanceDescr"),
        ("FC-MGMT-MIB", "fcmInstanceFabricId"))
)
if mibBuilder.loadTexts:
    fcmInstanceBasicGroup.setStatus("current")

fcmSwitchBasicGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 56, 3, 2, 2)
)
fcmSwitchBasicGroup.setObjects(
      *(("FC-MGMT-MIB", "fcmSwitchDomainId"),
        ("FC-MGMT-MIB", "fcmSwitchPrincipal"),
        ("FC-MGMT-MIB", "fcmSwitchWWN"))
)
if mibBuilder.loadTexts:
    fcmSwitchBasicGroup.setStatus("current")

fcmPortBasicGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 56, 3, 2, 3)
)
fcmPortBasicGroup.setObjects(
      *(("FC-MGMT-MIB", "fcmPortInstanceIndex"),
        ("FC-MGMT-MIB", "fcmPortWwn"),
        ("FC-MGMT-MIB", "fcmPortNodeWwn"),
        ("FC-MGMT-MIB", "fcmPortAdminType"),
        ("FC-MGMT-MIB", "fcmPortOperType"),
        ("FC-MGMT-MIB", "fcmPortFcCapClass"),
        ("FC-MGMT-MIB", "fcmPortFcOperClass"),
        ("FC-MGMT-MIB", "fcmPortTransmitterType"),
        ("FC-MGMT-MIB", "fcmPortConnectorType"),
        ("FC-MGMT-MIB", "fcmPortSerialNumber"),
        ("FC-MGMT-MIB", "fcmPortPhysicalNumber"),
        ("FC-MGMT-MIB", "fcmPortAdminSpeed"),
        ("FC-MGMT-MIB", "fcmPortCapProtocols"),
        ("FC-MGMT-MIB", "fcmPortOperProtocols"))
)
if mibBuilder.loadTexts:
    fcmPortBasicGroup.setStatus("current")

fcmPortStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 56, 3, 2, 4)
)
fcmPortStatsGroup.setObjects(
      *(("FC-MGMT-MIB", "fcmPortBBCreditZeros"),
        ("FC-MGMT-MIB", "fcmPortFullInputBuffers"))
)
if mibBuilder.loadTexts:
    fcmPortStatsGroup.setStatus("current")

fcmPortClass23StatsGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 56, 3, 2, 5)
)
fcmPortClass23StatsGroup.setObjects(
      *(("FC-MGMT-MIB", "fcmPortClass2RxFrames"),
        ("FC-MGMT-MIB", "fcmPortClass2RxOctets"),
        ("FC-MGMT-MIB", "fcmPortClass2TxFrames"),
        ("FC-MGMT-MIB", "fcmPortClass2TxOctets"),
        ("FC-MGMT-MIB", "fcmPortClass2Discards"),
        ("FC-MGMT-MIB", "fcmPortClass2RxFbsyFrames"),
        ("FC-MGMT-MIB", "fcmPortClass2RxPbsyFrames"),
        ("FC-MGMT-MIB", "fcmPortClass2RxFrjtFrames"),
        ("FC-MGMT-MIB", "fcmPortClass2RxPrjtFrames"),
        ("FC-MGMT-MIB", "fcmPortClass2TxFbsyFrames"),
        ("FC-MGMT-MIB", "fcmPortClass2TxPbsyFrames"),
        ("FC-MGMT-MIB", "fcmPortClass2TxFrjtFrames"),
        ("FC-MGMT-MIB", "fcmPortClass2TxPrjtFrames"),
        ("FC-MGMT-MIB", "fcmPortClass3RxFrames"),
        ("FC-MGMT-MIB", "fcmPortClass3RxOctets"),
        ("FC-MGMT-MIB", "fcmPortClass3TxFrames"),
        ("FC-MGMT-MIB", "fcmPortClass3TxOctets"),
        ("FC-MGMT-MIB", "fcmPortClass3Discards"))
)
if mibBuilder.loadTexts:
    fcmPortClass23StatsGroup.setStatus("current")

fcmPortClassFStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 56, 3, 2, 6)
)
fcmPortClassFStatsGroup.setObjects(
      *(("FC-MGMT-MIB", "fcmPortClassFRxFrames"),
        ("FC-MGMT-MIB", "fcmPortClassFRxOctets"),
        ("FC-MGMT-MIB", "fcmPortClassFTxFrames"),
        ("FC-MGMT-MIB", "fcmPortClassFTxOctets"),
        ("FC-MGMT-MIB", "fcmPortClassFDiscards"))
)
if mibBuilder.loadTexts:
    fcmPortClassFStatsGroup.setStatus("current")

fcmPortLcStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 56, 3, 2, 7)
)
fcmPortLcStatsGroup.setObjects(
      *(("FC-MGMT-MIB", "fcmPortLcBBCreditZeros"),
        ("FC-MGMT-MIB", "fcmPortLcFullInputBuffers"),
        ("FC-MGMT-MIB", "fcmPortLcClass2RxFrames"),
        ("FC-MGMT-MIB", "fcmPortLcClass2RxOctets"),
        ("FC-MGMT-MIB", "fcmPortLcClass2TxFrames"),
        ("FC-MGMT-MIB", "fcmPortLcClass2TxOctets"),
        ("FC-MGMT-MIB", "fcmPortLcClass2Discards"),
        ("FC-MGMT-MIB", "fcmPortLcClass3Discards"),
        ("FC-MGMT-MIB", "fcmPortLcClass3RxFrames"),
        ("FC-MGMT-MIB", "fcmPortLcClass3RxOctets"),
        ("FC-MGMT-MIB", "fcmPortLcClass3TxFrames"),
        ("FC-MGMT-MIB", "fcmPortLcClass3TxOctets"),
        ("FC-MGMT-MIB", "fcmPortLcClass2RxFbsyFrames"),
        ("FC-MGMT-MIB", "fcmPortLcClass2RxPbsyFrames"),
        ("FC-MGMT-MIB", "fcmPortLcClass2RxFrjtFrames"),
        ("FC-MGMT-MIB", "fcmPortLcClass2RxPrjtFrames"),
        ("FC-MGMT-MIB", "fcmPortLcClass2TxFbsyFrames"),
        ("FC-MGMT-MIB", "fcmPortLcClass2TxPbsyFrames"),
        ("FC-MGMT-MIB", "fcmPortLcClass2TxFrjtFrames"),
        ("FC-MGMT-MIB", "fcmPortLcClass2TxPrjtFrames"))
)
if mibBuilder.loadTexts:
    fcmPortLcStatsGroup.setStatus("current")

fcmPortErrorsGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 56, 3, 2, 8)
)
fcmPortErrorsGroup.setObjects(
      *(("FC-MGMT-MIB", "fcmPortRxLinkResets"),
        ("FC-MGMT-MIB", "fcmPortTxLinkResets"),
        ("FC-MGMT-MIB", "fcmPortLinkResets"),
        ("FC-MGMT-MIB", "fcmPortRxOfflineSequences"),
        ("FC-MGMT-MIB", "fcmPortTxOfflineSequences"),
        ("FC-MGMT-MIB", "fcmPortLinkFailures"),
        ("FC-MGMT-MIB", "fcmPortLossofSynchs"),
        ("FC-MGMT-MIB", "fcmPortLossofSignals"),
        ("FC-MGMT-MIB", "fcmPortPrimSeqProtocolErrors"),
        ("FC-MGMT-MIB", "fcmPortInvalidTxWords"),
        ("FC-MGMT-MIB", "fcmPortInvalidCRCs"),
        ("FC-MGMT-MIB", "fcmPortInvalidOrderedSets"),
        ("FC-MGMT-MIB", "fcmPortFrameTooLongs"),
        ("FC-MGMT-MIB", "fcmPortTruncatedFrames"),
        ("FC-MGMT-MIB", "fcmPortAddressErrors"),
        ("FC-MGMT-MIB", "fcmPortDelimiterErrors"),
        ("FC-MGMT-MIB", "fcmPortEncodingDisparityErrors"),
        ("FC-MGMT-MIB", "fcmPortOtherErrors"))
)
if mibBuilder.loadTexts:
    fcmPortErrorsGroup.setStatus("current")

fcmSwitchPortGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 56, 3, 2, 9)
)
fcmSwitchPortGroup.setObjects(
      *(("FC-MGMT-MIB", "fcmFxPortRatov"),
        ("FC-MGMT-MIB", "fcmFxPortEdtov"),
        ("FC-MGMT-MIB", "fcmFxPortRttov"),
        ("FC-MGMT-MIB", "fcmFxPortHoldTime"),
        ("FC-MGMT-MIB", "fcmFxPortCapBbCreditMax"),
        ("FC-MGMT-MIB", "fcmFxPortCapBbCreditMin"),
        ("FC-MGMT-MIB", "fcmFxPortCapDataFieldSizeMax"),
        ("FC-MGMT-MIB", "fcmFxPortCapDataFieldSizeMin"),
        ("FC-MGMT-MIB", "fcmFxPortCapClass2SeqDeliv"),
        ("FC-MGMT-MIB", "fcmFxPortCapClass3SeqDeliv"),
        ("FC-MGMT-MIB", "fcmFxPortCapHoldTimeMax"),
        ("FC-MGMT-MIB", "fcmFxPortCapHoldTimeMin"),
        ("FC-MGMT-MIB", "fcmISPortClassFCredit"),
        ("FC-MGMT-MIB", "fcmISPortClassFDataFieldSize"))
)
if mibBuilder.loadTexts:
    fcmSwitchPortGroup.setStatus("current")

fcmSwitchLoginGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 56, 3, 2, 10)
)
fcmSwitchLoginGroup.setObjects(
      *(("FC-MGMT-MIB", "fcmFLoginPortWwn"),
        ("FC-MGMT-MIB", "fcmFLoginNodeWwn"),
        ("FC-MGMT-MIB", "fcmFLoginBbCreditModel"),
        ("FC-MGMT-MIB", "fcmFLoginBbCredit"),
        ("FC-MGMT-MIB", "fcmFLoginClassesAgreed"),
        ("FC-MGMT-MIB", "fcmFLoginClass2SeqDelivAgreed"),
        ("FC-MGMT-MIB", "fcmFLoginClass2DataFieldSize"),
        ("FC-MGMT-MIB", "fcmFLoginClass3SeqDelivAgreed"),
        ("FC-MGMT-MIB", "fcmFLoginClass3DataFieldSize"))
)
if mibBuilder.loadTexts:
    fcmSwitchLoginGroup.setStatus("current")

fcmLinkBasicGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 56, 3, 2, 11)
)
fcmLinkBasicGroup.setObjects(
      *(("FC-MGMT-MIB", "fcmLinkEnd1NodeWwn"),
        ("FC-MGMT-MIB", "fcmLinkEnd1PhysPortNumber"),
        ("FC-MGMT-MIB", "fcmLinkEnd1PortWwn"),
        ("FC-MGMT-MIB", "fcmLinkEnd2NodeWwn"),
        ("FC-MGMT-MIB", "fcmLinkEnd2PhysPortNumber"),
        ("FC-MGMT-MIB", "fcmLinkEnd2PortWwn"),
        ("FC-MGMT-MIB", "fcmLinkEnd2AgentAddress"),
        ("FC-MGMT-MIB", "fcmLinkEnd2PortType"),
        ("FC-MGMT-MIB", "fcmLinkEnd2UnitType"),
        ("FC-MGMT-MIB", "fcmLinkEnd2FcAddressId"))
)
if mibBuilder.loadTexts:
    fcmLinkBasicGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

fcmgmtCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 10, 56, 3, 1, 1)
)
if mibBuilder.loadTexts:
    fcmgmtCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "FC-MGMT-MIB",
    **{"FcNameIdOrZero": FcNameIdOrZero,
       "FcAddressIdOrZero": FcAddressIdOrZero,
       "FcDomainIdOrZero": FcDomainIdOrZero,
       "FcPortType": FcPortType,
       "FcClasses": FcClasses,
       "FcBbCredit": FcBbCredit,
       "FcBbCreditModel": FcBbCreditModel,
       "FcDataFieldSize": FcDataFieldSize,
       "FcUnitFunctions": FcUnitFunctions,
       "fcMgmtMIB": fcMgmtMIB,
       "fcmgmtObjects": fcmgmtObjects,
       "fcmInstanceTable": fcmInstanceTable,
       "fcmInstanceEntry": fcmInstanceEntry,
       "fcmInstanceIndex": fcmInstanceIndex,
       "fcmInstanceWwn": fcmInstanceWwn,
       "fcmInstanceFunctions": fcmInstanceFunctions,
       "fcmInstancePhysicalIndex": fcmInstancePhysicalIndex,
       "fcmInstanceSoftwareIndex": fcmInstanceSoftwareIndex,
       "fcmInstanceStatus": fcmInstanceStatus,
       "fcmInstanceTextName": fcmInstanceTextName,
       "fcmInstanceDescr": fcmInstanceDescr,
       "fcmInstanceFabricId": fcmInstanceFabricId,
       "fcmSwitchTable": fcmSwitchTable,
       "fcmSwitchEntry": fcmSwitchEntry,
       "fcmSwitchIndex": fcmSwitchIndex,
       "fcmSwitchDomainId": fcmSwitchDomainId,
       "fcmSwitchPrincipal": fcmSwitchPrincipal,
       "fcmSwitchWWN": fcmSwitchWWN,
       "fcmPortTable": fcmPortTable,
       "fcmPortEntry": fcmPortEntry,
       "fcmPortInstanceIndex": fcmPortInstanceIndex,
       "fcmPortWwn": fcmPortWwn,
       "fcmPortNodeWwn": fcmPortNodeWwn,
       "fcmPortAdminType": fcmPortAdminType,
       "fcmPortOperType": fcmPortOperType,
       "fcmPortFcCapClass": fcmPortFcCapClass,
       "fcmPortFcOperClass": fcmPortFcOperClass,
       "fcmPortTransmitterType": fcmPortTransmitterType,
       "fcmPortConnectorType": fcmPortConnectorType,
       "fcmPortSerialNumber": fcmPortSerialNumber,
       "fcmPortPhysicalNumber": fcmPortPhysicalNumber,
       "fcmPortAdminSpeed": fcmPortAdminSpeed,
       "fcmPortCapProtocols": fcmPortCapProtocols,
       "fcmPortOperProtocols": fcmPortOperProtocols,
       "fcmPortStatsTable": fcmPortStatsTable,
       "fcmPortStatsEntry": fcmPortStatsEntry,
       "fcmPortBBCreditZeros": fcmPortBBCreditZeros,
       "fcmPortFullInputBuffers": fcmPortFullInputBuffers,
       "fcmPortClass2RxFrames": fcmPortClass2RxFrames,
       "fcmPortClass2RxOctets": fcmPortClass2RxOctets,
       "fcmPortClass2TxFrames": fcmPortClass2TxFrames,
       "fcmPortClass2TxOctets": fcmPortClass2TxOctets,
       "fcmPortClass2Discards": fcmPortClass2Discards,
       "fcmPortClass2RxFbsyFrames": fcmPortClass2RxFbsyFrames,
       "fcmPortClass2RxPbsyFrames": fcmPortClass2RxPbsyFrames,
       "fcmPortClass2RxFrjtFrames": fcmPortClass2RxFrjtFrames,
       "fcmPortClass2RxPrjtFrames": fcmPortClass2RxPrjtFrames,
       "fcmPortClass2TxFbsyFrames": fcmPortClass2TxFbsyFrames,
       "fcmPortClass2TxPbsyFrames": fcmPortClass2TxPbsyFrames,
       "fcmPortClass2TxFrjtFrames": fcmPortClass2TxFrjtFrames,
       "fcmPortClass2TxPrjtFrames": fcmPortClass2TxPrjtFrames,
       "fcmPortClass3RxFrames": fcmPortClass3RxFrames,
       "fcmPortClass3RxOctets": fcmPortClass3RxOctets,
       "fcmPortClass3TxFrames": fcmPortClass3TxFrames,
       "fcmPortClass3TxOctets": fcmPortClass3TxOctets,
       "fcmPortClass3Discards": fcmPortClass3Discards,
       "fcmPortClassFRxFrames": fcmPortClassFRxFrames,
       "fcmPortClassFRxOctets": fcmPortClassFRxOctets,
       "fcmPortClassFTxFrames": fcmPortClassFTxFrames,
       "fcmPortClassFTxOctets": fcmPortClassFTxOctets,
       "fcmPortClassFDiscards": fcmPortClassFDiscards,
       "fcmPortLcStatsTable": fcmPortLcStatsTable,
       "fcmPortLcStatsEntry": fcmPortLcStatsEntry,
       "fcmPortLcBBCreditZeros": fcmPortLcBBCreditZeros,
       "fcmPortLcFullInputBuffers": fcmPortLcFullInputBuffers,
       "fcmPortLcClass2RxFrames": fcmPortLcClass2RxFrames,
       "fcmPortLcClass2RxOctets": fcmPortLcClass2RxOctets,
       "fcmPortLcClass2TxFrames": fcmPortLcClass2TxFrames,
       "fcmPortLcClass2TxOctets": fcmPortLcClass2TxOctets,
       "fcmPortLcClass2Discards": fcmPortLcClass2Discards,
       "fcmPortLcClass2RxFbsyFrames": fcmPortLcClass2RxFbsyFrames,
       "fcmPortLcClass2RxPbsyFrames": fcmPortLcClass2RxPbsyFrames,
       "fcmPortLcClass2RxFrjtFrames": fcmPortLcClass2RxFrjtFrames,
       "fcmPortLcClass2RxPrjtFrames": fcmPortLcClass2RxPrjtFrames,
       "fcmPortLcClass2TxFbsyFrames": fcmPortLcClass2TxFbsyFrames,
       "fcmPortLcClass2TxPbsyFrames": fcmPortLcClass2TxPbsyFrames,
       "fcmPortLcClass2TxFrjtFrames": fcmPortLcClass2TxFrjtFrames,
       "fcmPortLcClass2TxPrjtFrames": fcmPortLcClass2TxPrjtFrames,
       "fcmPortLcClass3RxFrames": fcmPortLcClass3RxFrames,
       "fcmPortLcClass3RxOctets": fcmPortLcClass3RxOctets,
       "fcmPortLcClass3TxFrames": fcmPortLcClass3TxFrames,
       "fcmPortLcClass3TxOctets": fcmPortLcClass3TxOctets,
       "fcmPortLcClass3Discards": fcmPortLcClass3Discards,
       "fcmPortErrorsTable": fcmPortErrorsTable,
       "fcmPortErrorsEntry": fcmPortErrorsEntry,
       "fcmPortRxLinkResets": fcmPortRxLinkResets,
       "fcmPortTxLinkResets": fcmPortTxLinkResets,
       "fcmPortLinkResets": fcmPortLinkResets,
       "fcmPortRxOfflineSequences": fcmPortRxOfflineSequences,
       "fcmPortTxOfflineSequences": fcmPortTxOfflineSequences,
       "fcmPortLinkFailures": fcmPortLinkFailures,
       "fcmPortLossofSynchs": fcmPortLossofSynchs,
       "fcmPortLossofSignals": fcmPortLossofSignals,
       "fcmPortPrimSeqProtocolErrors": fcmPortPrimSeqProtocolErrors,
       "fcmPortInvalidTxWords": fcmPortInvalidTxWords,
       "fcmPortInvalidCRCs": fcmPortInvalidCRCs,
       "fcmPortInvalidOrderedSets": fcmPortInvalidOrderedSets,
       "fcmPortFrameTooLongs": fcmPortFrameTooLongs,
       "fcmPortTruncatedFrames": fcmPortTruncatedFrames,
       "fcmPortAddressErrors": fcmPortAddressErrors,
       "fcmPortDelimiterErrors": fcmPortDelimiterErrors,
       "fcmPortEncodingDisparityErrors": fcmPortEncodingDisparityErrors,
       "fcmPortOtherErrors": fcmPortOtherErrors,
       "fcmFxPortTable": fcmFxPortTable,
       "fcmFxPortEntry": fcmFxPortEntry,
       "fcmFxPortRatov": fcmFxPortRatov,
       "fcmFxPortEdtov": fcmFxPortEdtov,
       "fcmFxPortRttov": fcmFxPortRttov,
       "fcmFxPortHoldTime": fcmFxPortHoldTime,
       "fcmFxPortCapBbCreditMax": fcmFxPortCapBbCreditMax,
       "fcmFxPortCapBbCreditMin": fcmFxPortCapBbCreditMin,
       "fcmFxPortCapDataFieldSizeMax": fcmFxPortCapDataFieldSizeMax,
       "fcmFxPortCapDataFieldSizeMin": fcmFxPortCapDataFieldSizeMin,
       "fcmFxPortCapClass2SeqDeliv": fcmFxPortCapClass2SeqDeliv,
       "fcmFxPortCapClass3SeqDeliv": fcmFxPortCapClass3SeqDeliv,
       "fcmFxPortCapHoldTimeMax": fcmFxPortCapHoldTimeMax,
       "fcmFxPortCapHoldTimeMin": fcmFxPortCapHoldTimeMin,
       "fcmISPortTable": fcmISPortTable,
       "fcmISPortEntry": fcmISPortEntry,
       "fcmISPortClassFCredit": fcmISPortClassFCredit,
       "fcmISPortClassFDataFieldSize": fcmISPortClassFDataFieldSize,
       "fcmFLoginTable": fcmFLoginTable,
       "fcmFLoginEntry": fcmFLoginEntry,
       "fcmFLoginNxPortIndex": fcmFLoginNxPortIndex,
       "fcmFLoginPortWwn": fcmFLoginPortWwn,
       "fcmFLoginNodeWwn": fcmFLoginNodeWwn,
       "fcmFLoginBbCreditModel": fcmFLoginBbCreditModel,
       "fcmFLoginBbCredit": fcmFLoginBbCredit,
       "fcmFLoginClassesAgreed": fcmFLoginClassesAgreed,
       "fcmFLoginClass2SeqDelivAgreed": fcmFLoginClass2SeqDelivAgreed,
       "fcmFLoginClass2DataFieldSize": fcmFLoginClass2DataFieldSize,
       "fcmFLoginClass3SeqDelivAgreed": fcmFLoginClass3SeqDelivAgreed,
       "fcmFLoginClass3DataFieldSize": fcmFLoginClass3DataFieldSize,
       "fcmLinkTable": fcmLinkTable,
       "fcmLinkEntry": fcmLinkEntry,
       "fcmLinkIndex": fcmLinkIndex,
       "fcmLinkEnd1NodeWwn": fcmLinkEnd1NodeWwn,
       "fcmLinkEnd1PhysPortNumber": fcmLinkEnd1PhysPortNumber,
       "fcmLinkEnd1PortWwn": fcmLinkEnd1PortWwn,
       "fcmLinkEnd2NodeWwn": fcmLinkEnd2NodeWwn,
       "fcmLinkEnd2PhysPortNumber": fcmLinkEnd2PhysPortNumber,
       "fcmLinkEnd2PortWwn": fcmLinkEnd2PortWwn,
       "fcmLinkEnd2AgentAddress": fcmLinkEnd2AgentAddress,
       "fcmLinkEnd2PortType": fcmLinkEnd2PortType,
       "fcmLinkEnd2UnitType": fcmLinkEnd2UnitType,
       "fcmLinkEnd2FcAddressId": fcmLinkEnd2FcAddressId,
       "fcmgmtNotifications": fcmgmtNotifications,
       "fcmgmtNotifPrefix": fcmgmtNotifPrefix,
       "fcmgmtConformance": fcmgmtConformance,
       "fcmgmtCompliances": fcmgmtCompliances,
       "fcmgmtCompliance": fcmgmtCompliance,
       "fcmgmtGroups": fcmgmtGroups,
       "fcmInstanceBasicGroup": fcmInstanceBasicGroup,
       "fcmSwitchBasicGroup": fcmSwitchBasicGroup,
       "fcmPortBasicGroup": fcmPortBasicGroup,
       "fcmPortStatsGroup": fcmPortStatsGroup,
       "fcmPortClass23StatsGroup": fcmPortClass23StatsGroup,
       "fcmPortClassFStatsGroup": fcmPortClassFStatsGroup,
       "fcmPortLcStatsGroup": fcmPortLcStatsGroup,
       "fcmPortErrorsGroup": fcmPortErrorsGroup,
       "fcmSwitchPortGroup": fcmSwitchPortGroup,
       "fcmSwitchLoginGroup": fcmSwitchLoginGroup,
       "fcmLinkBasicGroup": fcmLinkBasicGroup}
)
