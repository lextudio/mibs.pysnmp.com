# SNMP MIB module (CTRON-AP3000-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CTRON-AP3000-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:18:31 2024
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
 iso,
 mgmt) = mibBuilder.importSymbols(
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
    "iso",
    "mgmt")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

ctronAP3000 = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 13)
)
ctronAP3000.setRevisions(
        ("2007-10-30 18:45",)
)


# Types definitions



class MacAddress(OctetString):
    """Custom type MacAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )





class DisplayString(OctetString):
    """Custom type DisplayString based on OctetString"""




class TruthValue(Integer32):
    """Custom type TruthValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Cabletron_ObjectIdentity = ObjectIdentity
cabletron = _Cabletron_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52)
)
_Mibs_ObjectIdentity = ObjectIdentity
mibs = _Mibs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4)
)
_ComPortMgnt_ObjectIdentity = ObjectIdentity
comPortMgnt = _ComPortMgnt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 13, 1)
)


class _ComPortControl_Type(Integer32):
    """Custom type comPortControl based on Integer32"""
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


_ComPortControl_Type.__name__ = "Integer32"
_ComPortControl_Object = MibScalar
comPortControl = _ComPortControl_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 13, 1, 1),
    _ComPortControl_Type()
)
comPortControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    comPortControl.setStatus("current")
_MacFilterMgnt_ObjectIdentity = ObjectIdentity
macFilterMgnt = _MacFilterMgnt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 13, 2)
)
_MacFilterTable_Object = MibTable
macFilterTable = _MacFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 13, 2, 1)
)
if mibBuilder.loadTexts:
    macFilterTable.setStatus("deprecated")
_MacFilterEntry_Object = MibTableRow
macFilterEntry = _MacFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 13, 2, 1, 1)
)
macFilterEntry.setIndexNames(
    (0, "CTRON-AP3000-MIB", "macFilterIndex"),
)
if mibBuilder.loadTexts:
    macFilterEntry.setStatus("deprecated")


class _MacFilterIndex_Type(Integer32):
    """Custom type macFilterIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_MacFilterIndex_Type.__name__ = "Integer32"
_MacFilterIndex_Object = MibTableColumn
macFilterIndex = _MacFilterIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 13, 2, 1, 1, 1),
    _MacFilterIndex_Type()
)
macFilterIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    macFilterIndex.setStatus("deprecated")
_MacFilterAddress_Type = MacAddress
_MacFilterAddress_Object = MibTableColumn
macFilterAddress = _MacFilterAddress_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 13, 2, 1, 1, 2),
    _MacFilterAddress_Type()
)
macFilterAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    macFilterAddress.setStatus("deprecated")


class _MacFilterAllowedToGo_Type(Integer32):
    """Custom type macFilterAllowedToGo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("allow", 1),
          ("deny", 2))
    )


_MacFilterAllowedToGo_Type.__name__ = "Integer32"
_MacFilterAllowedToGo_Object = MibTableColumn
macFilterAllowedToGo = _MacFilterAllowedToGo_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 13, 2, 1, 1, 3),
    _MacFilterAllowedToGo_Type()
)
macFilterAllowedToGo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    macFilterAllowedToGo.setStatus("deprecated")


class _MacFilterOpeStatus_Type(Integer32):
    """Custom type macFilterOpeStatus based on Integer32"""
    defaultValue = 0

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
        *(("create", 3),
          ("invalid", 2),
          ("other", 0),
          ("valid", 1))
    )


_MacFilterOpeStatus_Type.__name__ = "Integer32"
_MacFilterOpeStatus_Object = MibTableColumn
macFilterOpeStatus = _MacFilterOpeStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 13, 2, 1, 1, 4),
    _MacFilterOpeStatus_Type()
)
macFilterOpeStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    macFilterOpeStatus.setStatus("deprecated")


class _ApMacFilterControl_Type(Integer32):
    """Custom type apMacFilterControl based on Integer32"""
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


_ApMacFilterControl_Type.__name__ = "Integer32"
_ApMacFilterControl_Object = MibScalar
apMacFilterControl = _ApMacFilterControl_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 13, 2, 2),
    _ApMacFilterControl_Type()
)
apMacFilterControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apMacFilterControl.setStatus("deprecated")
_ApvMacFilterOperateTable_Object = MibTable
apvMacFilterOperateTable = _ApvMacFilterOperateTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 13, 2, 3)
)
if mibBuilder.loadTexts:
    apvMacFilterOperateTable.setStatus("current")
_ApvMacFilterOperateEntry_Object = MibTableRow
apvMacFilterOperateEntry = _ApvMacFilterOperateEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 13, 2, 3, 1)
)
apvMacFilterOperateEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    apvMacFilterOperateEntry.setStatus("current")


class _ApvMacFilterPermission_Type(Integer32):
    """Custom type apvMacFilterPermission based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("allowed", 1),
          ("denied", 2))
    )


_ApvMacFilterPermission_Type.__name__ = "Integer32"
_ApvMacFilterPermission_Object = MibTableColumn
apvMacFilterPermission = _ApvMacFilterPermission_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 13, 2, 3, 1, 1),
    _ApvMacFilterPermission_Type()
)
apvMacFilterPermission.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apvMacFilterPermission.setStatus("current")
_ApvMacFilterAddressToAdd_Type = OctetString
_ApvMacFilterAddressToAdd_Object = MibTableColumn
apvMacFilterAddressToAdd = _ApvMacFilterAddressToAdd_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 13, 2, 3, 1, 2),
    _ApvMacFilterAddressToAdd_Type()
)
apvMacFilterAddressToAdd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apvMacFilterAddressToAdd.setStatus("current")
_ApvMacFilterTable_Object = MibTable
apvMacFilterTable = _ApvMacFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 13, 2, 4)
)
if mibBuilder.loadTexts:
    apvMacFilterTable.setStatus("current")
_ApvMacFilterEntry_Object = MibTableRow
apvMacFilterEntry = _ApvMacFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 13, 2, 4, 1)
)
apvMacFilterEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CTRON-AP3000-MIB", "apvMacFilterIndex"),
)
if mibBuilder.loadTexts:
    apvMacFilterEntry.setStatus("current")


class _ApvMacFilterIndex_Type(Integer32):
    """Custom type apvMacFilterIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_ApvMacFilterIndex_Type.__name__ = "Integer32"
_ApvMacFilterIndex_Object = MibTableColumn
apvMacFilterIndex = _ApvMacFilterIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 13, 2, 4, 1, 1),
    _ApvMacFilterIndex_Type()
)
apvMacFilterIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    apvMacFilterIndex.setStatus("current")
_ApvMacFilterAddress_Type = MacAddress
_ApvMacFilterAddress_Object = MibTableColumn
apvMacFilterAddress = _ApvMacFilterAddress_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 13, 2, 4, 1, 2),
    _ApvMacFilterAddress_Type()
)
apvMacFilterAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apvMacFilterAddress.setStatus("current")


class _ApvMacFilterActivity_Type(Integer32):
    """Custom type apvMacFilterActivity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("allow", 1),
          ("deleteEntry", 3),
          ("denied", 2))
    )


_ApvMacFilterActivity_Type.__name__ = "Integer32"
_ApvMacFilterActivity_Object = MibTableColumn
apvMacFilterActivity = _ApvMacFilterActivity_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 13, 2, 4, 1, 3),
    _ApvMacFilterActivity_Type()
)
apvMacFilterActivity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apvMacFilterActivity.setStatus("current")
_QosMgnt_ObjectIdentity = ObjectIdentity
qosMgnt = _QosMgnt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 13, 3)
)


class _QosModeControl_Type(Integer32):
    """Custom type qosModeControl based on Integer32"""
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
        *(("qos8021p", 5),
          ("qosda", 3),
          ("qosether", 4),
          ("qosoff", 1),
          ("qossa", 2))
    )


_QosModeControl_Type.__name__ = "Integer32"
_QosModeControl_Object = MibScalar
qosModeControl = _QosModeControl_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 13, 3, 1),
    _QosModeControl_Type()
)
qosModeControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosModeControl.setStatus("current")
_QosMACTypeTable_Object = MibTable
qosMACTypeTable = _QosMACTypeTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 13, 3, 2)
)
if mibBuilder.loadTexts:
    qosMACTypeTable.setStatus("current")
_QosMACTypeEntry_Object = MibTableRow
qosMACTypeEntry = _QosMACTypeEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 13, 3, 2, 1)
)
qosMACTypeEntry.setIndexNames(
    (0, "CTRON-AP3000-MIB", "qosMACTypeIndex"),
)
if mibBuilder.loadTexts:
    qosMACTypeEntry.setStatus("current")


class _QosMACTypeIndex_Type(Integer32):
    """Custom type qosMACTypeIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_QosMACTypeIndex_Type.__name__ = "Integer32"
_QosMACTypeIndex_Object = MibTableColumn
qosMACTypeIndex = _QosMACTypeIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 13, 3, 2, 1, 1),
    _QosMACTypeIndex_Type()
)
qosMACTypeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    qosMACTypeIndex.setStatus("current")
_QosMACTypeAddress_Type = MacAddress
_QosMACTypeAddress_Object = MibTableColumn
qosMACTypeAddress = _QosMACTypeAddress_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 13, 3, 2, 1, 2),
    _QosMACTypeAddress_Type()
)
qosMACTypeAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosMACTypeAddress.setStatus("current")


class _QosMACTypePriority_Type(Integer32):
    """Custom type qosMACTypePriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_QosMACTypePriority_Type.__name__ = "Integer32"
_QosMACTypePriority_Object = MibTableColumn
qosMACTypePriority = _QosMACTypePriority_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 13, 3, 2, 1, 3),
    _QosMACTypePriority_Type()
)
qosMACTypePriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosMACTypePriority.setStatus("current")


class _QosMACTypeOpeStatus_Type(Integer32):
    """Custom type qosMACTypeOpeStatus based on Integer32"""
    defaultValue = 0

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
        *(("create", 3),
          ("invalid", 2),
          ("other", 0),
          ("valid", 1))
    )


_QosMACTypeOpeStatus_Type.__name__ = "Integer32"
_QosMACTypeOpeStatus_Object = MibTableColumn
qosMACTypeOpeStatus = _QosMACTypeOpeStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 13, 3, 2, 1, 4),
    _QosMACTypeOpeStatus_Type()
)
qosMACTypeOpeStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qosMACTypeOpeStatus.setStatus("current")
_QosEtherTypeTable_Object = MibTable
qosEtherTypeTable = _QosEtherTypeTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 13, 3, 3)
)
if mibBuilder.loadTexts:
    qosEtherTypeTable.setStatus("current")
_QosEtherTypeEntry_Object = MibTableRow
qosEtherTypeEntry = _QosEtherTypeEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 13, 3, 3, 1)
)
qosEtherTypeEntry.setIndexNames(
    (0, "CTRON-AP3000-MIB", "qosMACTypeIndex"),
)
if mibBuilder.loadTexts:
    qosEtherTypeEntry.setStatus("current")
_QosEtherTypeIndex_Type = Integer32
_QosEtherTypeIndex_Object = MibTableColumn
qosEtherTypeIndex = _QosEtherTypeIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 13, 3, 3, 1, 1),
    _QosEtherTypeIndex_Type()
)
qosEtherTypeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    qosEtherTypeIndex.setStatus("current")


class _QosEtherTypeHexValue_Type(OctetString):
    """Custom type qosEtherTypeHexValue based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_QosEtherTypeHexValue_Type.__name__ = "OctetString"
_QosEtherTypeHexValue_Object = MibTableColumn
qosEtherTypeHexValue = _QosEtherTypeHexValue_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 13, 3, 3, 1, 2),
    _QosEtherTypeHexValue_Type()
)
qosEtherTypeHexValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosEtherTypeHexValue.setStatus("current")


class _QosEtherTypePriority_Type(Integer32):
    """Custom type qosEtherTypePriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_QosEtherTypePriority_Type.__name__ = "Integer32"
_QosEtherTypePriority_Object = MibTableColumn
qosEtherTypePriority = _QosEtherTypePriority_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 13, 3, 3, 1, 3),
    _QosEtherTypePriority_Type()
)
qosEtherTypePriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosEtherTypePriority.setStatus("current")


class _QosEtherTypeOpeStatus_Type(Integer32):
    """Custom type qosEtherTypeOpeStatus based on Integer32"""
    defaultValue = 0

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
        *(("create", 3),
          ("invalid", 2),
          ("other", 0),
          ("valid", 1))
    )


_QosEtherTypeOpeStatus_Type.__name__ = "Integer32"
_QosEtherTypeOpeStatus_Object = MibTableColumn
qosEtherTypeOpeStatus = _QosEtherTypeOpeStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 13, 3, 3, 1, 4),
    _QosEtherTypeOpeStatus_Type()
)
qosEtherTypeOpeStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qosEtherTypeOpeStatus.setStatus("current")


class _QosQueueingMode_Type(Integer32):
    """Custom type qosQueueingMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("strict-priority", 2),
          ("weighted-fair", 1))
    )


_QosQueueingMode_Type.__name__ = "Integer32"
_QosQueueingMode_Object = MibScalar
qosQueueingMode = _QosQueueingMode_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 13, 3, 4),
    _QosQueueingMode_Type()
)
qosQueueingMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosQueueingMode.setStatus("current")


class _QosSVPStatus_Type(Integer32):
    """Custom type qosSVPStatus based on Integer32"""
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


_QosSVPStatus_Type.__name__ = "Integer32"
_QosSVPStatus_Object = MibScalar
qosSVPStatus = _QosSVPStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 13, 3, 5),
    _QosSVPStatus_Type()
)
qosSVPStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosSVPStatus.setStatus("current")
_LinkQualityMgnt_ObjectIdentity = ObjectIdentity
linkQualityMgnt = _LinkQualityMgnt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 13, 4)
)
_LinkQualityTable_Object = MibTable
linkQualityTable = _LinkQualityTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 13, 4, 1)
)
if mibBuilder.loadTexts:
    linkQualityTable.setStatus("current")
_LinkQualityEntry_Object = MibTableRow
linkQualityEntry = _LinkQualityEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 13, 4, 1, 1)
)
linkQualityEntry.setIndexNames(
    (0, "CTRON-AP3000-MIB", "linkQualityRadioIndex"),
    (0, "CTRON-AP3000-MIB", "linkQualityStaIndex"),
)
if mibBuilder.loadTexts:
    linkQualityEntry.setStatus("current")


class _LinkQualityRadioIndex_Type(Integer32):
    """Custom type linkQualityRadioIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_LinkQualityRadioIndex_Type.__name__ = "Integer32"
_LinkQualityRadioIndex_Object = MibTableColumn
linkQualityRadioIndex = _LinkQualityRadioIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 13, 4, 1, 1, 1),
    _LinkQualityRadioIndex_Type()
)
linkQualityRadioIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    linkQualityRadioIndex.setStatus("current")


class _LinkQualityStaIndex_Type(Integer32):
    """Custom type linkQualityStaIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_LinkQualityStaIndex_Type.__name__ = "Integer32"
_LinkQualityStaIndex_Object = MibTableColumn
linkQualityStaIndex = _LinkQualityStaIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 13, 4, 1, 1, 2),
    _LinkQualityStaIndex_Type()
)
linkQualityStaIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    linkQualityStaIndex.setStatus("current")
_LinkQualityStaMacAddress_Type = MacAddress
_LinkQualityStaMacAddress_Object = MibTableColumn
linkQualityStaMacAddress = _LinkQualityStaMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 13, 4, 1, 1, 3),
    _LinkQualityStaMacAddress_Type()
)
linkQualityStaMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkQualityStaMacAddress.setStatus("current")


class _LinkQualityStaRssi_Type(Integer32):
    """Custom type linkQualityStaRssi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_LinkQualityStaRssi_Type.__name__ = "Integer32"
_LinkQualityStaRssi_Object = MibTableColumn
linkQualityStaRssi = _LinkQualityStaRssi_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 13, 4, 1, 1, 4),
    _LinkQualityStaRssi_Type()
)
linkQualityStaRssi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkQualityStaRssi.setStatus("current")
_ApSnmpMgnt_ObjectIdentity = ObjectIdentity
apSnmpMgnt = _ApSnmpMgnt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 13, 5)
)


class _TrapControl_Type(Integer32):
    """Custom type trapControl based on Integer32"""
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


_TrapControl_Type.__name__ = "Integer32"
_TrapControl_Object = MibScalar
trapControl = _TrapControl_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 13, 5, 1),
    _TrapControl_Type()
)
trapControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapControl.setStatus("current")
_TrapConfiguration_ObjectIdentity = ObjectIdentity
trapConfiguration = _TrapConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 13, 5, 2)
)


class _TrapSysSystemUp_Type(Integer32):
    """Custom type trapSysSystemUp based on Integer32"""
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


_TrapSysSystemUp_Type.__name__ = "Integer32"
_TrapSysSystemUp_Object = MibScalar
trapSysSystemUp = _TrapSysSystemUp_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 13, 5, 2, 1),
    _TrapSysSystemUp_Type()
)
trapSysSystemUp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapSysSystemUp.setStatus("current")


class _TrapSysSystemDown_Type(Integer32):
    """Custom type trapSysSystemDown based on Integer32"""
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


_TrapSysSystemDown_Type.__name__ = "Integer32"
_TrapSysSystemDown_Object = MibScalar
trapSysSystemDown = _TrapSysSystemDown_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 13, 5, 2, 2),
    _TrapSysSystemDown_Type()
)
trapSysSystemDown.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapSysSystemDown.setStatus("current")


class _TrapSysRadiusServerChanged_Type(Integer32):
    """Custom type trapSysRadiusServerChanged based on Integer32"""
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


_TrapSysRadiusServerChanged_Type.__name__ = "Integer32"
_TrapSysRadiusServerChanged_Object = MibScalar
trapSysRadiusServerChanged = _TrapSysRadiusServerChanged_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 13, 5, 2, 3),
    _TrapSysRadiusServerChanged_Type()
)
trapSysRadiusServerChanged.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapSysRadiusServerChanged.setStatus("current")


class _TrapDot11StationAssociation_Type(Integer32):
    """Custom type trapDot11StationAssociation based on Integer32"""
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


_TrapDot11StationAssociation_Type.__name__ = "Integer32"
_TrapDot11StationAssociation_Object = MibScalar
trapDot11StationAssociation = _TrapDot11StationAssociation_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 13, 5, 2, 4),
    _TrapDot11StationAssociation_Type()
)
trapDot11StationAssociation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapDot11StationAssociation.setStatus("current")


class _TrapDot11StationReAssociation_Type(Integer32):
    """Custom type trapDot11StationReAssociation based on Integer32"""
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


_TrapDot11StationReAssociation_Type.__name__ = "Integer32"
_TrapDot11StationReAssociation_Object = MibScalar
trapDot11StationReAssociation = _TrapDot11StationReAssociation_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 13, 5, 2, 5),
    _TrapDot11StationReAssociation_Type()
)
trapDot11StationReAssociation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapDot11StationReAssociation.setStatus("current")


class _TrapDot11StationAuthentication_Type(Integer32):
    """Custom type trapDot11StationAuthentication based on Integer32"""
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


_TrapDot11StationAuthentication_Type.__name__ = "Integer32"
_TrapDot11StationAuthentication_Object = MibScalar
trapDot11StationAuthentication = _TrapDot11StationAuthentication_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 13, 5, 2, 6),
    _TrapDot11StationAuthentication_Type()
)
trapDot11StationAuthentication.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapDot11StationAuthentication.setStatus("current")


class _TrapDot11StationRequestFail_Type(Integer32):
    """Custom type trapDot11StationRequestFail based on Integer32"""
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


_TrapDot11StationRequestFail_Type.__name__ = "Integer32"
_TrapDot11StationRequestFail_Object = MibScalar
trapDot11StationRequestFail = _TrapDot11StationRequestFail_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 13, 5, 2, 7),
    _TrapDot11StationRequestFail_Type()
)
trapDot11StationRequestFail.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapDot11StationRequestFail.setStatus("current")


class _TrapLocalMacAddrAuthFail_Type(Integer32):
    """Custom type trapLocalMacAddrAuthFail based on Integer32"""
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


_TrapLocalMacAddrAuthFail_Type.__name__ = "Integer32"
_TrapLocalMacAddrAuthFail_Object = MibScalar
trapLocalMacAddrAuthFail = _TrapLocalMacAddrAuthFail_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 13, 5, 2, 9),
    _TrapLocalMacAddrAuthFail_Type()
)
trapLocalMacAddrAuthFail.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapLocalMacAddrAuthFail.setStatus("current")


class _TrapLocalMacAddrAuthSuccess_Type(Integer32):
    """Custom type trapLocalMacAddrAuthSuccess based on Integer32"""
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


_TrapLocalMacAddrAuthSuccess_Type.__name__ = "Integer32"
_TrapLocalMacAddrAuthSuccess_Object = MibScalar
trapLocalMacAddrAuthSuccess = _TrapLocalMacAddrAuthSuccess_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 13, 5, 2, 10),
    _TrapLocalMacAddrAuthSuccess_Type()
)
trapLocalMacAddrAuthSuccess.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapLocalMacAddrAuthSuccess.setStatus("current")


class _TrapDot1xAuthNotInitiated_Type(Integer32):
    """Custom type trapDot1xAuthNotInitiated based on Integer32"""
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


_TrapDot1xAuthNotInitiated_Type.__name__ = "Integer32"
_TrapDot1xAuthNotInitiated_Object = MibScalar
trapDot1xAuthNotInitiated = _TrapDot1xAuthNotInitiated_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 13, 5, 2, 11),
    _TrapDot1xAuthNotInitiated_Type()
)
trapDot1xAuthNotInitiated.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapDot1xAuthNotInitiated.setStatus("current")


class _TrapDot1xAuthSuccess_Type(Integer32):
    """Custom type trapDot1xAuthSuccess based on Integer32"""
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


_TrapDot1xAuthSuccess_Type.__name__ = "Integer32"
_TrapDot1xAuthSuccess_Object = MibScalar
trapDot1xAuthSuccess = _TrapDot1xAuthSuccess_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 13, 5, 2, 12),
    _TrapDot1xAuthSuccess_Type()
)
trapDot1xAuthSuccess.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapDot1xAuthSuccess.setStatus("current")


class _TrapDot1xAuthFail_Type(Integer32):
    """Custom type trapDot1xAuthFail based on Integer32"""
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


_TrapDot1xAuthFail_Type.__name__ = "Integer32"
_TrapDot1xAuthFail_Object = MibScalar
trapDot1xAuthFail = _TrapDot1xAuthFail_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 13, 5, 2, 13),
    _TrapDot1xAuthFail_Type()
)
trapDot1xAuthFail.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapDot1xAuthFail.setStatus("current")


class _TrapDot1xMacAddrAuthSuccess_Type(Integer32):
    """Custom type trapDot1xMacAddrAuthSuccess based on Integer32"""
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


_TrapDot1xMacAddrAuthSuccess_Type.__name__ = "Integer32"
_TrapDot1xMacAddrAuthSuccess_Object = MibScalar
trapDot1xMacAddrAuthSuccess = _TrapDot1xMacAddrAuthSuccess_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 13, 5, 2, 14),
    _TrapDot1xMacAddrAuthSuccess_Type()
)
trapDot1xMacAddrAuthSuccess.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapDot1xMacAddrAuthSuccess.setStatus("current")


class _TrapDot1xMacAddrAuthFail_Type(Integer32):
    """Custom type trapDot1xMacAddrAuthFail based on Integer32"""
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


_TrapDot1xMacAddrAuthFail_Type.__name__ = "Integer32"
_TrapDot1xMacAddrAuthFail_Object = MibScalar
trapDot1xMacAddrAuthFail = _TrapDot1xMacAddrAuthFail_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 13, 5, 2, 15),
    _TrapDot1xMacAddrAuthFail_Type()
)
trapDot1xMacAddrAuthFail.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapDot1xMacAddrAuthFail.setStatus("current")


class _TrapPppLogonFail_Type(Integer32):
    """Custom type trapPppLogonFail based on Integer32"""
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


_TrapPppLogonFail_Type.__name__ = "Integer32"
_TrapPppLogonFail_Object = MibScalar
trapPppLogonFail = _TrapPppLogonFail_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 13, 5, 2, 16),
    _TrapPppLogonFail_Type()
)
trapPppLogonFail.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapPppLogonFail.setStatus("current")


class _TrapIappStationRoamedFrom_Type(Integer32):
    """Custom type trapIappStationRoamedFrom based on Integer32"""
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


_TrapIappStationRoamedFrom_Type.__name__ = "Integer32"
_TrapIappStationRoamedFrom_Object = MibScalar
trapIappStationRoamedFrom = _TrapIappStationRoamedFrom_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 13, 5, 2, 17),
    _TrapIappStationRoamedFrom_Type()
)
trapIappStationRoamedFrom.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapIappStationRoamedFrom.setStatus("current")


class _TrapIappStationRoamedTo_Type(Integer32):
    """Custom type trapIappStationRoamedTo based on Integer32"""
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


_TrapIappStationRoamedTo_Type.__name__ = "Integer32"
_TrapIappStationRoamedTo_Object = MibScalar
trapIappStationRoamedTo = _TrapIappStationRoamedTo_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 13, 5, 2, 18),
    _TrapIappStationRoamedTo_Type()
)
trapIappStationRoamedTo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapIappStationRoamedTo.setStatus("current")


class _TrapIappContextDataSent_Type(Integer32):
    """Custom type trapIappContextDataSent based on Integer32"""
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


_TrapIappContextDataSent_Type.__name__ = "Integer32"
_TrapIappContextDataSent_Object = MibScalar
trapIappContextDataSent = _TrapIappContextDataSent_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 13, 5, 2, 19),
    _TrapIappContextDataSent_Type()
)
trapIappContextDataSent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapIappContextDataSent.setStatus("current")


class _TrapSntpServerFail_Type(Integer32):
    """Custom type trapSntpServerFail based on Integer32"""
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


_TrapSntpServerFail_Type.__name__ = "Integer32"
_TrapSntpServerFail_Object = MibScalar
trapSntpServerFail = _TrapSntpServerFail_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 13, 5, 2, 20),
    _TrapSntpServerFail_Type()
)
trapSntpServerFail.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapSntpServerFail.setStatus("current")


class _TrapDot11InterfaceAFail_Type(Integer32):
    """Custom type trapDot11InterfaceAFail based on Integer32"""
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


_TrapDot11InterfaceAFail_Type.__name__ = "Integer32"
_TrapDot11InterfaceAFail_Object = MibScalar
trapDot11InterfaceAFail = _TrapDot11InterfaceAFail_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 13, 5, 2, 21),
    _TrapDot11InterfaceAFail_Type()
)
trapDot11InterfaceAFail.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapDot11InterfaceAFail.setStatus("current")


class _TrapDot11InterfaceGFail_Type(Integer32):
    """Custom type trapDot11InterfaceGFail based on Integer32"""
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


_TrapDot11InterfaceGFail_Type.__name__ = "Integer32"
_TrapDot11InterfaceGFail_Object = MibScalar
trapDot11InterfaceGFail = _TrapDot11InterfaceGFail_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 13, 5, 2, 22),
    _TrapDot11InterfaceGFail_Type()
)
trapDot11InterfaceGFail.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapDot11InterfaceGFail.setStatus("current")


class _TrapDot11WirelessSTPDetection_Type(Integer32):
    """Custom type trapDot11WirelessSTPDetection based on Integer32"""
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


_TrapDot11WirelessSTPDetection_Type.__name__ = "Integer32"
_TrapDot11WirelessSTPDetection_Object = MibScalar
trapDot11WirelessSTPDetection = _TrapDot11WirelessSTPDetection_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 13, 5, 2, 23),
    _TrapDot11WirelessSTPDetection_Type()
)
trapDot11WirelessSTPDetection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapDot11WirelessSTPDetection.setStatus("current")
_ApSnmpTrapDestinationTable_Object = MibTable
apSnmpTrapDestinationTable = _ApSnmpTrapDestinationTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 13, 5, 3)
)
if mibBuilder.loadTexts:
    apSnmpTrapDestinationTable.setStatus("current")
_ApSnmpTrapDestinationEntry_Object = MibTableRow
apSnmpTrapDestinationEntry = _ApSnmpTrapDestinationEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 13, 5, 3, 1)
)
apSnmpTrapDestinationEntry.setIndexNames(
    (0, "CTRON-AP3000-MIB", "apSnmpTrapDestinationIndex"),
)
if mibBuilder.loadTexts:
    apSnmpTrapDestinationEntry.setStatus("current")


class _ApSnmpTrapDestinationIndex_Type(Integer32):
    """Custom type apSnmpTrapDestinationIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_ApSnmpTrapDestinationIndex_Type.__name__ = "Integer32"
_ApSnmpTrapDestinationIndex_Object = MibTableColumn
apSnmpTrapDestinationIndex = _ApSnmpTrapDestinationIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 13, 5, 3, 1, 1),
    _ApSnmpTrapDestinationIndex_Type()
)
apSnmpTrapDestinationIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    apSnmpTrapDestinationIndex.setStatus("current")


class _ApSnmpTrapDestinationCommunity_Type(DisplayString):
    """Custom type apSnmpTrapDestinationCommunity based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ApSnmpTrapDestinationCommunity_Type.__name__ = "DisplayString"
_ApSnmpTrapDestinationCommunity_Object = MibTableColumn
apSnmpTrapDestinationCommunity = _ApSnmpTrapDestinationCommunity_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 13, 5, 3, 1, 2),
    _ApSnmpTrapDestinationCommunity_Type()
)
apSnmpTrapDestinationCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apSnmpTrapDestinationCommunity.setStatus("current")
_ApSnmpTrapDestinationIP_Type = IpAddress
_ApSnmpTrapDestinationIP_Object = MibTableColumn
apSnmpTrapDestinationIP = _ApSnmpTrapDestinationIP_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 13, 5, 3, 1, 3),
    _ApSnmpTrapDestinationIP_Type()
)
apSnmpTrapDestinationIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apSnmpTrapDestinationIP.setStatus("current")


class _ApSnmpTrapDestinationState_Type(Integer32):
    """Custom type apSnmpTrapDestinationState based on Integer32"""
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


_ApSnmpTrapDestinationState_Type.__name__ = "Integer32"
_ApSnmpTrapDestinationState_Object = MibTableColumn
apSnmpTrapDestinationState = _ApSnmpTrapDestinationState_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 13, 5, 3, 1, 4),
    _ApSnmpTrapDestinationState_Type()
)
apSnmpTrapDestinationState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apSnmpTrapDestinationState.setStatus("current")


class _ApSnmpCommunityReadOnly_Type(DisplayString):
    """Custom type apSnmpCommunityReadOnly based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ApSnmpCommunityReadOnly_Type.__name__ = "DisplayString"
_ApSnmpCommunityReadOnly_Object = MibScalar
apSnmpCommunityReadOnly = _ApSnmpCommunityReadOnly_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 13, 5, 4),
    _ApSnmpCommunityReadOnly_Type()
)
apSnmpCommunityReadOnly.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apSnmpCommunityReadOnly.setStatus("current")


class _ApSnmpCommunityReadWrite_Type(DisplayString):
    """Custom type apSnmpCommunityReadWrite based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ApSnmpCommunityReadWrite_Type.__name__ = "DisplayString"
_ApSnmpCommunityReadWrite_Object = MibScalar
apSnmpCommunityReadWrite = _ApSnmpCommunityReadWrite_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 13, 5, 5),
    _ApSnmpCommunityReadWrite_Type()
)
apSnmpCommunityReadWrite.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apSnmpCommunityReadWrite.setStatus("current")


class _ApSnmpVersionFilter_Type(Integer32):
    """Custom type apSnmpVersionFilter based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disableSNMPv1SNMPv2c", 2),
          ("enableSNMPv1SNMPv2c", 1))
    )


_ApSnmpVersionFilter_Type.__name__ = "Integer32"
_ApSnmpVersionFilter_Object = MibScalar
apSnmpVersionFilter = _ApSnmpVersionFilter_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 13, 5, 6),
    _ApSnmpVersionFilter_Type()
)
apSnmpVersionFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apSnmpVersionFilter.setStatus("current")
_SysEntity_ObjectIdentity = ObjectIdentity
sysEntity = _SysEntity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 13, 6)
)


class _SwHardwareVer_Type(DisplayString):
    """Custom type swHardwareVer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_SwHardwareVer_Type.__name__ = "DisplayString"
_SwHardwareVer_Object = MibScalar
swHardwareVer = _SwHardwareVer_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 13, 6, 1),
    _SwHardwareVer_Type()
)
swHardwareVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swHardwareVer.setStatus("current")


class _SwBootRomVer_Type(DisplayString):
    """Custom type swBootRomVer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_SwBootRomVer_Type.__name__ = "DisplayString"
_SwBootRomVer_Object = MibScalar
swBootRomVer = _SwBootRomVer_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 13, 6, 2),
    _SwBootRomVer_Type()
)
swBootRomVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swBootRomVer.setStatus("current")


class _SwOpCodeVer_Type(DisplayString):
    """Custom type swOpCodeVer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_SwOpCodeVer_Type.__name__ = "DisplayString"
_SwOpCodeVer_Object = MibScalar
swOpCodeVer = _SwOpCodeVer_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 13, 6, 3),
    _SwOpCodeVer_Type()
)
swOpCodeVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swOpCodeVer.setStatus("current")


class _SwSerialNumber_Type(DisplayString):
    """Custom type swSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_SwSerialNumber_Type.__name__ = "DisplayString"
_SwSerialNumber_Object = MibScalar
swSerialNumber = _SwSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 13, 6, 4),
    _SwSerialNumber_Type()
)
swSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSerialNumber.setStatus("current")


class _SwProductName_Type(DisplayString):
    """Custom type swProductName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_SwProductName_Type.__name__ = "DisplayString"
_SwProductName_Object = MibScalar
swProductName = _SwProductName_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 13, 6, 5),
    _SwProductName_Type()
)
swProductName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swProductName.setStatus("current")


class _SwCountrySetting_Type(DisplayString):
    """Custom type swCountrySetting based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SwCountrySetting_Type.__name__ = "DisplayString"
_SwCountrySetting_Object = MibScalar
swCountrySetting = _SwCountrySetting_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 13, 6, 6),
    _SwCountrySetting_Type()
)
swCountrySetting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swCountrySetting.setStatus("current")
_ApSecurityMgnt_ObjectIdentity = ObjectIdentity
apSecurityMgnt = _ApSecurityMgnt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 13, 7)
)
_ApRadioSecurityTable_Object = MibTable
apRadioSecurityTable = _ApRadioSecurityTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 13, 7, 1)
)
if mibBuilder.loadTexts:
    apRadioSecurityTable.setStatus("current")
_ApRadioSecurityEntry_Object = MibTableRow
apRadioSecurityEntry = _ApRadioSecurityEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 13, 7, 1, 1)
)
apRadioSecurityEntry.setIndexNames(
    (0, "CTRON-AP3000-MIB", "apRadioSecurityIndex"),
)
if mibBuilder.loadTexts:
    apRadioSecurityEntry.setStatus("current")


class _ApRadioSecurityIndex_Type(Integer32):
    """Custom type apRadioSecurityIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_ApRadioSecurityIndex_Type.__name__ = "Integer32"
_ApRadioSecurityIndex_Object = MibTableColumn
apRadioSecurityIndex = _ApRadioSecurityIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 13, 7, 1, 1, 1),
    _ApRadioSecurityIndex_Type()
)
apRadioSecurityIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    apRadioSecurityIndex.setStatus("current")


class _ApRadioSecurityWEPAuthType_Type(Integer32):
    """Custom type apRadioSecurityWEPAuthType based on Integer32"""
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
              7)
        )
    )
    namedValues = NamedValues(
        *(("opensystem", 0),
          ("sharedkey", 1),
          ("wpa", 2),
          ("wpa2", 6),
          ("wpa2psk", 7),
          ("wpapsk", 3),
          ("wpawpa2mixed", 4),
          ("wpawpa2pskmixed", 5))
    )


_ApRadioSecurityWEPAuthType_Type.__name__ = "Integer32"
_ApRadioSecurityWEPAuthType_Object = MibTableColumn
apRadioSecurityWEPAuthType = _ApRadioSecurityWEPAuthType_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 13, 7, 1, 1, 2),
    _ApRadioSecurityWEPAuthType_Type()
)
apRadioSecurityWEPAuthType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apRadioSecurityWEPAuthType.setStatus("current")


class _ApRadioSecuritySharedKeyLen_Type(Integer32):
    """Custom type apRadioSecuritySharedKeyLen based on Integer32"""
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
        *(("none", 0),
          ("oneHundredFiftyTwo", 3),
          ("oneHundredTwentyEight", 2),
          ("sixtyFour", 1))
    )


_ApRadioSecuritySharedKeyLen_Type.__name__ = "Integer32"
_ApRadioSecuritySharedKeyLen_Object = MibTableColumn
apRadioSecuritySharedKeyLen = _ApRadioSecuritySharedKeyLen_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 13, 7, 1, 1, 3),
    _ApRadioSecuritySharedKeyLen_Type()
)
apRadioSecuritySharedKeyLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apRadioSecuritySharedKeyLen.setStatus("current")


class _ApRadioSecurityWPAMode_Type(Integer32):
    """Custom type apRadioSecurityWPAMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notSupported", 2),
          ("required", 1),
          ("supported", 0))
    )


_ApRadioSecurityWPAMode_Type.__name__ = "Integer32"
_ApRadioSecurityWPAMode_Object = MibTableColumn
apRadioSecurityWPAMode = _ApRadioSecurityWPAMode_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 13, 7, 1, 1, 4),
    _ApRadioSecurityWPAMode_Type()
)
apRadioSecurityWPAMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apRadioSecurityWPAMode.setStatus("current")


class _ApRadioSecurityWPAKeyType_Type(Integer32):
    """Custom type apRadioSecurityWPAKeyType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("dot1x", 0),
          ("presharedkey", 1))
    )


_ApRadioSecurityWPAKeyType_Type.__name__ = "Integer32"
_ApRadioSecurityWPAKeyType_Object = MibTableColumn
apRadioSecurityWPAKeyType = _ApRadioSecurityWPAKeyType_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 13, 7, 1, 1, 5),
    _ApRadioSecurityWPAKeyType_Type()
)
apRadioSecurityWPAKeyType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apRadioSecurityWPAKeyType.setStatus("current")


class _ApRadioSecurityWPACipher_Type(Integer32):
    """Custom type apRadioSecurityWPACipher based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("aes", 2),
          ("tkip", 1),
          ("wep", 0))
    )


_ApRadioSecurityWPACipher_Type.__name__ = "Integer32"
_ApRadioSecurityWPACipher_Object = MibTableColumn
apRadioSecurityWPACipher = _ApRadioSecurityWPACipher_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 13, 7, 1, 1, 6),
    _ApRadioSecurityWPACipher_Type()
)
apRadioSecurityWPACipher.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apRadioSecurityWPACipher.setStatus("obsolete")


class _ApRadioSecurityWPAPSKType_Type(Integer32):
    """Custom type apRadioSecurityWPAPSKType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("alphanumeric", 1),
          ("hex", 0))
    )


_ApRadioSecurityWPAPSKType_Type.__name__ = "Integer32"
_ApRadioSecurityWPAPSKType_Object = MibTableColumn
apRadioSecurityWPAPSKType = _ApRadioSecurityWPAPSKType_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 13, 7, 1, 1, 7),
    _ApRadioSecurityWPAPSKType_Type()
)
apRadioSecurityWPAPSKType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apRadioSecurityWPAPSKType.setStatus("current")


class _ApRadioSecurityWPAPSK_Type(DisplayString):
    """Custom type apRadioSecurityWPAPSK based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_ApRadioSecurityWPAPSK_Type.__name__ = "DisplayString"
_ApRadioSecurityWPAPSK_Object = MibTableColumn
apRadioSecurityWPAPSK = _ApRadioSecurityWPAPSK_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 13, 7, 1, 1, 8),
    _ApRadioSecurityWPAPSK_Type()
)
apRadioSecurityWPAPSK.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apRadioSecurityWPAPSK.setStatus("current")


class _ApRadioSecurityWEPKeyType_Type(Integer32):
    """Custom type apRadioSecurityWEPKeyType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("alphanumeric", 1),
          ("hexadecimal", 0))
    )


_ApRadioSecurityWEPKeyType_Type.__name__ = "Integer32"
_ApRadioSecurityWEPKeyType_Object = MibTableColumn
apRadioSecurityWEPKeyType = _ApRadioSecurityWEPKeyType_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 13, 7, 1, 1, 9),
    _ApRadioSecurityWEPKeyType_Type()
)
apRadioSecurityWEPKeyType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apRadioSecurityWEPKeyType.setStatus("current")
_ApRadioSecurityWEPEnabled_Type = TruthValue
_ApRadioSecurityWEPEnabled_Object = MibTableColumn
apRadioSecurityWEPEnabled = _ApRadioSecurityWEPEnabled_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 13, 7, 1, 1, 10),
    _ApRadioSecurityWEPEnabled_Type()
)
apRadioSecurityWEPEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apRadioSecurityWEPEnabled.setStatus("current")


class _ApRadioSecurityWPACipherSuite_Type(Integer32):
    """Custom type apRadioSecurityWPACipherSuite based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("aesccmp", 0),
          ("tkip", 1),
          ("wep", 2))
    )


_ApRadioSecurityWPACipherSuite_Type.__name__ = "Integer32"
_ApRadioSecurityWPACipherSuite_Object = MibTableColumn
apRadioSecurityWPACipherSuite = _ApRadioSecurityWPACipherSuite_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 13, 7, 1, 1, 11),
    _ApRadioSecurityWPACipherSuite_Type()
)
apRadioSecurityWPACipherSuite.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apRadioSecurityWPACipherSuite.setStatus("current")


class _ApRadioApSecurityWPAPreAuthentication_Type(Integer32):
    """Custom type apRadioApSecurityWPAPreAuthentication based on Integer32"""
    defaultValue = 2

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


_ApRadioApSecurityWPAPreAuthentication_Type.__name__ = "Integer32"
_ApRadioApSecurityWPAPreAuthentication_Object = MibTableColumn
apRadioApSecurityWPAPreAuthentication = _ApRadioApSecurityWPAPreAuthentication_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 13, 7, 1, 1, 12),
    _ApRadioApSecurityWPAPreAuthentication_Type()
)
apRadioApSecurityWPAPreAuthentication.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apRadioApSecurityWPAPreAuthentication.setStatus("current")


class _ApRadioApSecurityWPAPmksaLifetime_Type(Integer32):
    """Custom type apRadioApSecurityWPAPmksaLifetime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 14400),
    )


_ApRadioApSecurityWPAPmksaLifetime_Type.__name__ = "Integer32"
_ApRadioApSecurityWPAPmksaLifetime_Object = MibTableColumn
apRadioApSecurityWPAPmksaLifetime = _ApRadioApSecurityWPAPmksaLifetime_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 13, 7, 1, 1, 13),
    _ApRadioApSecurityWPAPmksaLifetime_Type()
)
apRadioApSecurityWPAPmksaLifetime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apRadioApSecurityWPAPmksaLifetime.setStatus("current")
_ApSecuritySsh_ObjectIdentity = ObjectIdentity
apSecuritySsh = _ApSecuritySsh_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 13, 7, 2)
)
_ApSecuritySshServerEnabled_Type = TruthValue
_ApSecuritySshServerEnabled_Object = MibScalar
apSecuritySshServerEnabled = _ApSecuritySshServerEnabled_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 13, 7, 2, 1),
    _ApSecuritySshServerEnabled_Type()
)
apSecuritySshServerEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apSecuritySshServerEnabled.setStatus("current")


class _ApSecuritySshServerPort_Type(Integer32):
    """Custom type apSecuritySshServerPort based on Integer32"""
    defaultValue = 22


_ApSecuritySshServerPort_Object = MibScalar
apSecuritySshServerPort = _ApSecuritySshServerPort_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 13, 7, 2, 2),
    _ApSecuritySshServerPort_Type()
)
apSecuritySshServerPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apSecuritySshServerPort.setStatus("current")
_ApSecuritySshTelnetServerEnabled_Type = TruthValue
_ApSecuritySshTelnetServerEnabled_Object = MibScalar
apSecuritySshTelnetServerEnabled = _ApSecuritySshTelnetServerEnabled_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 13, 7, 2, 3),
    _ApSecuritySshTelnetServerEnabled_Type()
)
apSecuritySshTelnetServerEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apSecuritySshTelnetServerEnabled.setStatus("current")
_ApRadioInterfaceMgnt_ObjectIdentity = ObjectIdentity
apRadioInterfaceMgnt = _ApRadioInterfaceMgnt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 13, 8)
)
_EnterpriseApRadioTable_Object = MibTable
enterpriseApRadioTable = _EnterpriseApRadioTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 13, 8, 2)
)
if mibBuilder.loadTexts:
    enterpriseApRadioTable.setStatus("current")
_EnterpriseApRadioEntry_Object = MibTableRow
enterpriseApRadioEntry = _EnterpriseApRadioEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 13, 8, 2, 1)
)
enterpriseApRadioEntry.setIndexNames(
    (0, "CTRON-AP3000-MIB", "enterpriseApRadioIndex"),
)
if mibBuilder.loadTexts:
    enterpriseApRadioEntry.setStatus("current")


class _EnterpriseApRadioIndex_Type(Integer32):
    """Custom type enterpriseApRadioIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_EnterpriseApRadioIndex_Type.__name__ = "Integer32"
_EnterpriseApRadioIndex_Object = MibTableColumn
enterpriseApRadioIndex = _EnterpriseApRadioIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 13, 8, 2, 1, 1),
    _EnterpriseApRadioIndex_Type()
)
enterpriseApRadioIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    enterpriseApRadioIndex.setStatus("current")


class _EnterpriseApRadioAutoChannel_Type(Integer32):
    """Custom type enterpriseApRadioAutoChannel based on Integer32"""
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


_EnterpriseApRadioAutoChannel_Type.__name__ = "Integer32"
_EnterpriseApRadioAutoChannel_Object = MibTableColumn
enterpriseApRadioAutoChannel = _EnterpriseApRadioAutoChannel_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 13, 8, 2, 1, 2),
    _EnterpriseApRadioAutoChannel_Type()
)
enterpriseApRadioAutoChannel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enterpriseApRadioAutoChannel.setStatus("current")


class _EnterpriseApRadioTransmitPower_Type(Integer32):
    """Custom type enterpriseApRadioTransmitPower based on Integer32"""
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
        *(("eighth", 4),
          ("full", 1),
          ("half", 2),
          ("min", 5),
          ("quarter", 3))
    )


_EnterpriseApRadioTransmitPower_Type.__name__ = "Integer32"
_EnterpriseApRadioTransmitPower_Object = MibTableColumn
enterpriseApRadioTransmitPower = _EnterpriseApRadioTransmitPower_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 13, 8, 2, 1, 3),
    _EnterpriseApRadioTransmitPower_Type()
)
enterpriseApRadioTransmitPower.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enterpriseApRadioTransmitPower.setStatus("current")


class _EnterpriseApRadioTurboMode_Type(Integer32):
    """Custom type enterpriseApRadioTurboMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1),
          ("invalid", 3))
    )


_EnterpriseApRadioTurboMode_Type.__name__ = "Integer32"
_EnterpriseApRadioTurboMode_Object = MibTableColumn
enterpriseApRadioTurboMode = _EnterpriseApRadioTurboMode_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 13, 8, 2, 1, 4),
    _EnterpriseApRadioTurboMode_Type()
)
enterpriseApRadioTurboMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enterpriseApRadioTurboMode.setStatus("current")


class _EnterpriseApRadioDataRate_Type(Integer32):
    """Custom type enterpriseApRadioDataRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              5,
              6,
              9,
              11,
              12,
              18,
              24,
              36,
              48,
              54,
              255)
        )
    )
    namedValues = NamedValues(
        *(("auto", 255),
          ("eighteenMbps", 18),
          ("elevenMbps", 11),
          ("fiftyFourMbps", 54),
          ("fiveAndHalfMbps", 5),
          ("fourtyEightMbps", 48),
          ("nineMbps", 9),
          ("oneMbps", 1),
          ("sixMbps", 6),
          ("thirtySixMbps", 36),
          ("twelveMbps", 12),
          ("twentyFourMbps", 24),
          ("twoMbps", 2))
    )


_EnterpriseApRadioDataRate_Type.__name__ = "Integer32"
_EnterpriseApRadioDataRate_Object = MibTableColumn
enterpriseApRadioDataRate = _EnterpriseApRadioDataRate_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 13, 8, 2, 1, 5),
    _EnterpriseApRadioDataRate_Type()
)
enterpriseApRadioDataRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enterpriseApRadioDataRate.setStatus("current")


class _EnterpriseApRadioGMode_Type(Integer32):
    """Custom type enterpriseApRadioGMode based on Integer32"""
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
        *(("bOnly", 1),
          ("bg", 3),
          ("gOnly", 2),
          ("invalid", 4))
    )


_EnterpriseApRadioGMode_Type.__name__ = "Integer32"
_EnterpriseApRadioGMode_Object = MibTableColumn
enterpriseApRadioGMode = _EnterpriseApRadioGMode_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 13, 8, 2, 1, 6),
    _EnterpriseApRadioGMode_Type()
)
enterpriseApRadioGMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enterpriseApRadioGMode.setStatus("current")


class _EnterpriseApRadioAntennaMode_Type(Integer32):
    """Custom type enterpriseApRadioAntennaMode based on Integer32"""
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
        *(("both", 1),
          ("invalid", 4),
          ("left", 2),
          ("right", 3))
    )


_EnterpriseApRadioAntennaMode_Type.__name__ = "Integer32"
_EnterpriseApRadioAntennaMode_Object = MibTableColumn
enterpriseApRadioAntennaMode = _EnterpriseApRadioAntennaMode_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 13, 8, 2, 1, 7),
    _EnterpriseApRadioAntennaMode_Type()
)
enterpriseApRadioAntennaMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enterpriseApRadioAntennaMode.setStatus("current")


class _RogueApState_Type(Integer32):
    """Custom type rogueApState based on Integer32"""
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


_RogueApState_Type.__name__ = "Integer32"
_RogueApState_Object = MibTableColumn
rogueApState = _RogueApState_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 13, 8, 2, 1, 8),
    _RogueApState_Type()
)
rogueApState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rogueApState.setStatus("current")


class _RogueApInterval_Type(Integer32):
    """Custom type rogueApInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30, 10080),
    )


_RogueApInterval_Type.__name__ = "Integer32"
_RogueApInterval_Object = MibTableColumn
rogueApInterval = _RogueApInterval_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 13, 8, 2, 1, 9),
    _RogueApInterval_Type()
)
rogueApInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rogueApInterval.setStatus("current")


class _RogueApDuration_Type(Integer32):
    """Custom type rogueApDuration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(200, 1000),
    )


_RogueApDuration_Type.__name__ = "Integer32"
_RogueApDuration_Object = MibTableColumn
rogueApDuration = _RogueApDuration_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 13, 8, 2, 1, 10),
    _RogueApDuration_Type()
)
rogueApDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rogueApDuration.setStatus("current")


class _RogueApScanNow_Type(Integer32):
    """Custom type rogueApScanNow based on Integer32"""
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


_RogueApScanNow_Type.__name__ = "Integer32"
_RogueApScanNow_Object = MibTableColumn
rogueApScanNow = _RogueApScanNow_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 13, 8, 2, 1, 11),
    _RogueApScanNow_Type()
)
rogueApScanNow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rogueApScanNow.setStatus("current")


class _EnterpriseApRadioAntennaModeControl_Type(Integer32):
    """Custom type enterpriseApRadioAntennaModeControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("external", 2),
          ("fixed", 1))
    )


_EnterpriseApRadioAntennaModeControl_Type.__name__ = "Integer32"
_EnterpriseApRadioAntennaModeControl_Object = MibTableColumn
enterpriseApRadioAntennaModeControl = _EnterpriseApRadioAntennaModeControl_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 13, 8, 2, 1, 12),
    _EnterpriseApRadioAntennaModeControl_Type()
)
enterpriseApRadioAntennaModeControl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enterpriseApRadioAntennaModeControl.setStatus("current")


class _EnterpriseApRadioFixedAntennaType_Type(Integer32):
    """Custom type enterpriseApRadioFixedAntennaType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("diversity", 1),
          ("left", 2),
          ("right", 3))
    )


_EnterpriseApRadioFixedAntennaType_Type.__name__ = "Integer32"
_EnterpriseApRadioFixedAntennaType_Object = MibTableColumn
enterpriseApRadioFixedAntennaType = _EnterpriseApRadioFixedAntennaType_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 13, 8, 2, 1, 13),
    _EnterpriseApRadioFixedAntennaType_Type()
)
enterpriseApRadioFixedAntennaType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enterpriseApRadioFixedAntennaType.setStatus("current")
_EnterpriseApRadioAntennaID_Type = Integer32
_EnterpriseApRadioAntennaID_Object = MibTableColumn
enterpriseApRadioAntennaID = _EnterpriseApRadioAntennaID_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 13, 8, 2, 1, 14),
    _EnterpriseApRadioAntennaID_Type()
)
enterpriseApRadioAntennaID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enterpriseApRadioAntennaID.setStatus("current")


class _EnterpriseApRadioMulticastDataRate_Type(Integer32):
    """Custom type enterpriseApRadioMulticastDataRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              5,
              6,
              9,
              11,
              12,
              18,
              24,
              36,
              48,
              54)
        )
    )
    namedValues = NamedValues(
        *(("eighteenMbps", 18),
          ("elevenMbps", 11),
          ("fiftyFourMbps", 54),
          ("fiveAndHalfMbps", 5),
          ("fortyEightMbps", 48),
          ("nineMbps", 9),
          ("oneMbps", 1),
          ("sixMbps", 6),
          ("thirtySixMbps", 36),
          ("twelveMbps", 12),
          ("twentyFourMbps", 24),
          ("twoMbps", 2))
    )


_EnterpriseApRadioMulticastDataRate_Type.__name__ = "Integer32"
_EnterpriseApRadioMulticastDataRate_Object = MibTableColumn
enterpriseApRadioMulticastDataRate = _EnterpriseApRadioMulticastDataRate_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 13, 8, 2, 1, 15),
    _EnterpriseApRadioMulticastDataRate_Type()
)
enterpriseApRadioMulticastDataRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enterpriseApRadioMulticastDataRate.setStatus("current")


class _EnterpriseApRadioAutoDataRate_Type(Integer32):
    """Custom type enterpriseApRadioAutoDataRate based on Integer32"""
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


_EnterpriseApRadioAutoDataRate_Type.__name__ = "Integer32"
_EnterpriseApRadioAutoDataRate_Object = MibTableColumn
enterpriseApRadioAutoDataRate = _EnterpriseApRadioAutoDataRate_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 13, 8, 2, 1, 16),
    _EnterpriseApRadioAutoDataRate_Type()
)
enterpriseApRadioAutoDataRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enterpriseApRadioAutoDataRate.setStatus("current")


class _EnterpriseApRadioPreamble_Type(Integer32):
    """Custom type enterpriseApRadioPreamble based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 3),
          ("long", 1),
          ("short", 2))
    )


_EnterpriseApRadioPreamble_Type.__name__ = "Integer32"
_EnterpriseApRadioPreamble_Object = MibTableColumn
enterpriseApRadioPreamble = _EnterpriseApRadioPreamble_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 13, 8, 2, 1, 17),
    _EnterpriseApRadioPreamble_Type()
)
enterpriseApRadioPreamble.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enterpriseApRadioPreamble.setStatus("current")


class _EnterpriseApRadioSWRetryMode_Type(Integer32):
    """Custom type enterpriseApRadioSWRetryMode based on Integer32"""
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


_EnterpriseApRadioSWRetryMode_Type.__name__ = "Integer32"
_EnterpriseApRadioSWRetryMode_Object = MibTableColumn
enterpriseApRadioSWRetryMode = _EnterpriseApRadioSWRetryMode_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 13, 8, 2, 1, 18),
    _EnterpriseApRadioSWRetryMode_Type()
)
enterpriseApRadioSWRetryMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enterpriseApRadioSWRetryMode.setStatus("current")
_EnterpriseApVapRadioTable_Object = MibTable
enterpriseApVapRadioTable = _EnterpriseApVapRadioTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 13, 8, 3)
)
if mibBuilder.loadTexts:
    enterpriseApVapRadioTable.setStatus("current")
_EnterpriseApVapRadioEntry_Object = MibTableRow
enterpriseApVapRadioEntry = _EnterpriseApVapRadioEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 13, 8, 3, 1)
)
enterpriseApVapRadioEntry.setIndexNames(
    (0, "CTRON-AP3000-MIB", "enterpriseApVapRadioIndex"),
)
if mibBuilder.loadTexts:
    enterpriseApVapRadioEntry.setStatus("current")


class _EnterpriseApVapRadioIndex_Type(Integer32):
    """Custom type enterpriseApVapRadioIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_EnterpriseApVapRadioIndex_Type.__name__ = "Integer32"
_EnterpriseApVapRadioIndex_Object = MibTableColumn
enterpriseApVapRadioIndex = _EnterpriseApVapRadioIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 13, 8, 3, 1, 1),
    _EnterpriseApVapRadioIndex_Type()
)
enterpriseApVapRadioIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    enterpriseApVapRadioIndex.setStatus("current")


class _EnterpriseApVapRadioState_Type(Integer32):
    """Custom type enterpriseApVapRadioState based on Integer32"""
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


_EnterpriseApVapRadioState_Type.__name__ = "Integer32"
_EnterpriseApVapRadioState_Object = MibTableColumn
enterpriseApVapRadioState = _EnterpriseApVapRadioState_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 13, 8, 3, 1, 2),
    _EnterpriseApVapRadioState_Type()
)
enterpriseApVapRadioState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enterpriseApVapRadioState.setStatus("current")


class _EnterpriseApVapRadioSecureAccess_Type(Integer32):
    """Custom type enterpriseApVapRadioSecureAccess based on Integer32"""
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


_EnterpriseApVapRadioSecureAccess_Type.__name__ = "Integer32"
_EnterpriseApVapRadioSecureAccess_Object = MibTableColumn
enterpriseApVapRadioSecureAccess = _EnterpriseApVapRadioSecureAccess_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 13, 8, 3, 1, 3),
    _EnterpriseApVapRadioSecureAccess_Type()
)
enterpriseApVapRadioSecureAccess.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enterpriseApVapRadioSecureAccess.setStatus("current")


class _EnterpriseApVapRadioMaxAssoc_Type(Integer32):
    """Custom type enterpriseApVapRadioMaxAssoc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_EnterpriseApVapRadioMaxAssoc_Type.__name__ = "Integer32"
_EnterpriseApVapRadioMaxAssoc_Object = MibTableColumn
enterpriseApVapRadioMaxAssoc = _EnterpriseApVapRadioMaxAssoc_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 13, 8, 3, 1, 4),
    _EnterpriseApVapRadioMaxAssoc_Type()
)
enterpriseApVapRadioMaxAssoc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enterpriseApVapRadioMaxAssoc.setStatus("current")


class _EnterpriseApVapRadioTransmitKey_Type(Integer32):
    """Custom type enterpriseApVapRadioTransmitKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_EnterpriseApVapRadioTransmitKey_Type.__name__ = "Integer32"
_EnterpriseApVapRadioTransmitKey_Object = MibTableColumn
enterpriseApVapRadioTransmitKey = _EnterpriseApVapRadioTransmitKey_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 13, 8, 3, 1, 5),
    _EnterpriseApVapRadioTransmitKey_Type()
)
enterpriseApVapRadioTransmitKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enterpriseApVapRadioTransmitKey.setStatus("current")


class _EnterpriseApVapRadioDescription_Type(DisplayString):
    """Custom type enterpriseApVapRadioDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_EnterpriseApVapRadioDescription_Type.__name__ = "DisplayString"
_EnterpriseApVapRadioDescription_Object = MibTableColumn
enterpriseApVapRadioDescription = _EnterpriseApVapRadioDescription_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 13, 8, 3, 1, 6),
    _EnterpriseApVapRadioDescription_Type()
)
enterpriseApVapRadioDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enterpriseApVapRadioDescription.setStatus("current")


class _EnterpriseApVapRadioDefefaultPriority_Type(Integer32):
    """Custom type enterpriseApVapRadioDefefaultPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_EnterpriseApVapRadioDefefaultPriority_Type.__name__ = "Integer32"
_EnterpriseApVapRadioDefefaultPriority_Object = MibTableColumn
enterpriseApVapRadioDefefaultPriority = _EnterpriseApVapRadioDefefaultPriority_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 13, 8, 3, 1, 7),
    _EnterpriseApVapRadioDefefaultPriority_Type()
)
enterpriseApVapRadioDefefaultPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enterpriseApVapRadioDefefaultPriority.setStatus("current")
_EnterpriseApRadioWdsTable_Object = MibTable
enterpriseApRadioWdsTable = _EnterpriseApRadioWdsTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 13, 8, 4)
)
if mibBuilder.loadTexts:
    enterpriseApRadioWdsTable.setStatus("current")
_EnterpriseApRadioWdsEntry_Object = MibTableRow
enterpriseApRadioWdsEntry = _EnterpriseApRadioWdsEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 13, 8, 4, 1)
)
enterpriseApRadioWdsEntry.setIndexNames(
    (0, "CTRON-AP3000-MIB", "enterpriseApRadioIndex"),
)
if mibBuilder.loadTexts:
    enterpriseApRadioWdsEntry.setStatus("current")


class _WdsApRole_Type(Integer32):
    """Custom type wdsApRole based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("roleAp", 1),
          ("roleBridge", 3),
          ("roleBridgeMaster", 2))
    )


_WdsApRole_Type.__name__ = "Integer32"
_WdsApRole_Object = MibTableColumn
wdsApRole = _WdsApRole_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 13, 8, 4, 1, 1),
    _WdsApRole_Type()
)
wdsApRole.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wdsApRole.setStatus("current")
_WdsApAckTimeout_Type = Integer32
_WdsApAckTimeout_Object = MibTableColumn
wdsApAckTimeout = _WdsApAckTimeout_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 13, 8, 4, 1, 2),
    _WdsApAckTimeout_Type()
)
wdsApAckTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wdsApAckTimeout.setStatus("current")
_EnterpriseApRadioWdsPeerTable_Object = MibTable
enterpriseApRadioWdsPeerTable = _EnterpriseApRadioWdsPeerTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 13, 8, 5)
)
if mibBuilder.loadTexts:
    enterpriseApRadioWdsPeerTable.setStatus("current")
_EnterpriseApRadioWdsPeerEntry_Object = MibTableRow
enterpriseApRadioWdsPeerEntry = _EnterpriseApRadioWdsPeerEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 13, 8, 5, 1)
)
enterpriseApRadioWdsPeerEntry.setIndexNames(
    (0, "CTRON-AP3000-MIB", "enterpriseApRadioIndex"),
    (0, "CTRON-AP3000-MIB", "wdsPeerIndex"),
)
if mibBuilder.loadTexts:
    enterpriseApRadioWdsPeerEntry.setStatus("current")


class _WdsPeerIndex_Type(Integer32):
    """Custom type wdsPeerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_WdsPeerIndex_Type.__name__ = "Integer32"
_WdsPeerIndex_Object = MibTableColumn
wdsPeerIndex = _WdsPeerIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 13, 8, 5, 1, 1),
    _WdsPeerIndex_Type()
)
wdsPeerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wdsPeerIndex.setStatus("current")


class _WdsPeerBssid_Type(DisplayString):
    """Custom type wdsPeerBssid based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 17),
    )


_WdsPeerBssid_Type.__name__ = "DisplayString"
_WdsPeerBssid_Object = MibTableColumn
wdsPeerBssid = _WdsPeerBssid_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 13, 8, 5, 1, 2),
    _WdsPeerBssid_Type()
)
wdsPeerBssid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wdsPeerBssid.setStatus("current")
_WdsPeerRSSI_Type = Integer32
_WdsPeerRSSI_Object = MibTableColumn
wdsPeerRSSI = _WdsPeerRSSI_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 13, 8, 5, 1, 3),
    _WdsPeerRSSI_Type()
)
wdsPeerRSSI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wdsPeerRSSI.setStatus("current")
_EnterpriseApRadioWEPKeysTable_Object = MibTable
enterpriseApRadioWEPKeysTable = _EnterpriseApRadioWEPKeysTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 13, 8, 6)
)
if mibBuilder.loadTexts:
    enterpriseApRadioWEPKeysTable.setStatus("current")
_EnterpriseApRadioWEPKeysEntry_Object = MibTableRow
enterpriseApRadioWEPKeysEntry = _EnterpriseApRadioWEPKeysEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 13, 8, 6, 1)
)
enterpriseApRadioWEPKeysEntry.setIndexNames(
    (0, "CTRON-AP3000-MIB", "enterpriseApRadioIndex"),
    (0, "CTRON-AP3000-MIB", "enterpriseApRadioWEPKeysIndex"),
)
if mibBuilder.loadTexts:
    enterpriseApRadioWEPKeysEntry.setStatus("current")


class _EnterpriseApRadioWEPKeysIndex_Type(Integer32):
    """Custom type enterpriseApRadioWEPKeysIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_EnterpriseApRadioWEPKeysIndex_Type.__name__ = "Integer32"
_EnterpriseApRadioWEPKeysIndex_Object = MibTableColumn
enterpriseApRadioWEPKeysIndex = _EnterpriseApRadioWEPKeysIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 13, 8, 6, 1, 1),
    _EnterpriseApRadioWEPKeysIndex_Type()
)
enterpriseApRadioWEPKeysIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    enterpriseApRadioWEPKeysIndex.setStatus("current")


class _EnterpriseApRadioWEPKeyType_Type(Integer32):
    """Custom type enterpriseApRadioWEPKeyType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("alphanumericKey", 2),
          ("hexadecimalKey", 1),
          ("otherKey", 3))
    )


_EnterpriseApRadioWEPKeyType_Type.__name__ = "Integer32"
_EnterpriseApRadioWEPKeyType_Object = MibTableColumn
enterpriseApRadioWEPKeyType = _EnterpriseApRadioWEPKeyType_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 13, 8, 6, 1, 2),
    _EnterpriseApRadioWEPKeyType_Type()
)
enterpriseApRadioWEPKeyType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enterpriseApRadioWEPKeyType.setStatus("current")


class _EnterpriseApRadioWEPKeyLength_Type(Integer32):
    """Custom type enterpriseApRadioWEPKeyLength based on Integer32"""
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
        *(("keyLength128Bit", 2),
          ("keyLength152Bit", 3),
          ("keyLength64Bit", 1),
          ("keyLengthOther", 4))
    )


_EnterpriseApRadioWEPKeyLength_Type.__name__ = "Integer32"
_EnterpriseApRadioWEPKeyLength_Object = MibTableColumn
enterpriseApRadioWEPKeyLength = _EnterpriseApRadioWEPKeyLength_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 13, 8, 6, 1, 3),
    _EnterpriseApRadioWEPKeyLength_Type()
)
enterpriseApRadioWEPKeyLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enterpriseApRadioWEPKeyLength.setStatus("current")
_EnterpriseApRadioAvAntennaListTable_Object = MibTable
enterpriseApRadioAvAntennaListTable = _EnterpriseApRadioAvAntennaListTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 13, 8, 7)
)
if mibBuilder.loadTexts:
    enterpriseApRadioAvAntennaListTable.setStatus("current")
_EnterpriseApRadioAvAntennaListEntry_Object = MibTableRow
enterpriseApRadioAvAntennaListEntry = _EnterpriseApRadioAvAntennaListEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 13, 8, 7, 1)
)
enterpriseApRadioAvAntennaListEntry.setIndexNames(
    (0, "CTRON-AP3000-MIB", "enterpriseApRadioIndex"),
    (0, "CTRON-AP3000-MIB", "enterpriseApRadioAvAntennaIndex"),
)
if mibBuilder.loadTexts:
    enterpriseApRadioAvAntennaListEntry.setStatus("current")


class _EnterpriseApRadioAvAntennaIndex_Type(Integer32):
    """Custom type enterpriseApRadioAvAntennaIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_EnterpriseApRadioAvAntennaIndex_Type.__name__ = "Integer32"
_EnterpriseApRadioAvAntennaIndex_Object = MibTableColumn
enterpriseApRadioAvAntennaIndex = _EnterpriseApRadioAvAntennaIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 13, 8, 7, 1, 1),
    _EnterpriseApRadioAvAntennaIndex_Type()
)
enterpriseApRadioAvAntennaIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    enterpriseApRadioAvAntennaIndex.setStatus("current")
_EnterpriseApRadioAvAntennaId_Type = Integer32
_EnterpriseApRadioAvAntennaId_Object = MibTableColumn
enterpriseApRadioAvAntennaId = _EnterpriseApRadioAvAntennaId_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 13, 8, 7, 1, 2),
    _EnterpriseApRadioAvAntennaId_Type()
)
enterpriseApRadioAvAntennaId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enterpriseApRadioAvAntennaId.setStatus("current")


class _EnterpriseApRadioAvAntennaDesc_Type(DisplayString):
    """Custom type enterpriseApRadioAvAntennaDesc based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_EnterpriseApRadioAvAntennaDesc_Type.__name__ = "DisplayString"
_EnterpriseApRadioAvAntennaDesc_Object = MibTableColumn
enterpriseApRadioAvAntennaDesc = _EnterpriseApRadioAvAntennaDesc_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 13, 8, 7, 1, 3),
    _EnterpriseApRadioAvAntennaDesc_Type()
)
enterpriseApRadioAvAntennaDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enterpriseApRadioAvAntennaDesc.setStatus("current")
_EnterpriseApRadioAvChannelListTable_Object = MibTable
enterpriseApRadioAvChannelListTable = _EnterpriseApRadioAvChannelListTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 13, 8, 8)
)
if mibBuilder.loadTexts:
    enterpriseApRadioAvChannelListTable.setStatus("current")
_EnterpriseApRadioAvChannelListEntry_Object = MibTableRow
enterpriseApRadioAvChannelListEntry = _EnterpriseApRadioAvChannelListEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 13, 8, 8, 1)
)
enterpriseApRadioAvChannelListEntry.setIndexNames(
    (0, "CTRON-AP3000-MIB", "enterpriseApRadioIndex"),
    (0, "CTRON-AP3000-MIB", "enterpriseApRadioAvChannelIndex"),
)
if mibBuilder.loadTexts:
    enterpriseApRadioAvChannelListEntry.setStatus("current")


class _EnterpriseApRadioAvChannelIndex_Type(Integer32):
    """Custom type enterpriseApRadioAvChannelIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_EnterpriseApRadioAvChannelIndex_Type.__name__ = "Integer32"
_EnterpriseApRadioAvChannelIndex_Object = MibTableColumn
enterpriseApRadioAvChannelIndex = _EnterpriseApRadioAvChannelIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 13, 8, 8, 1, 1),
    _EnterpriseApRadioAvChannelIndex_Type()
)
enterpriseApRadioAvChannelIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    enterpriseApRadioAvChannelIndex.setStatus("current")
_EnterpriseApRadioAvChannelNo_Type = Integer32
_EnterpriseApRadioAvChannelNo_Object = MibTableColumn
enterpriseApRadioAvChannelNo = _EnterpriseApRadioAvChannelNo_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 13, 8, 8, 1, 2),
    _EnterpriseApRadioAvChannelNo_Type()
)
enterpriseApRadioAvChannelNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enterpriseApRadioAvChannelNo.setStatus("current")
_ApEtherInterfaceMgnt_ObjectIdentity = ObjectIdentity
apEtherInterfaceMgnt = _ApEtherInterfaceMgnt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 13, 9)
)
_ApEtherNetConfig_ObjectIdentity = ObjectIdentity
apEtherNetConfig = _ApEtherNetConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 13, 9, 1)
)
_NetConfigIPAddress_Type = IpAddress
_NetConfigIPAddress_Object = MibScalar
netConfigIPAddress = _NetConfigIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 13, 9, 1, 1),
    _NetConfigIPAddress_Type()
)
netConfigIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netConfigIPAddress.setStatus("current")
_NetConfigSubnetMask_Type = IpAddress
_NetConfigSubnetMask_Object = MibScalar
netConfigSubnetMask = _NetConfigSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 13, 9, 1, 2),
    _NetConfigSubnetMask_Type()
)
netConfigSubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netConfigSubnetMask.setStatus("current")
_NetConfigDefaultGateway_Type = IpAddress
_NetConfigDefaultGateway_Object = MibScalar
netConfigDefaultGateway = _NetConfigDefaultGateway_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 13, 9, 1, 3),
    _NetConfigDefaultGateway_Type()
)
netConfigDefaultGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netConfigDefaultGateway.setStatus("current")


class _NetConfigHttpState_Type(Integer32):
    """Custom type netConfigHttpState based on Integer32"""
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


_NetConfigHttpState_Type.__name__ = "Integer32"
_NetConfigHttpState_Object = MibScalar
netConfigHttpState = _NetConfigHttpState_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 13, 9, 1, 4),
    _NetConfigHttpState_Type()
)
netConfigHttpState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netConfigHttpState.setStatus("current")


class _NetConfigHttpPort_Type(Integer32):
    """Custom type netConfigHttpPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(514, 65535),
    )


_NetConfigHttpPort_Type.__name__ = "Integer32"
_NetConfigHttpPort_Object = MibScalar
netConfigHttpPort = _NetConfigHttpPort_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 13, 9, 1, 5),
    _NetConfigHttpPort_Type()
)
netConfigHttpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netConfigHttpPort.setStatus("current")


class _NetConfigHttpsState_Type(Integer32):
    """Custom type netConfigHttpsState based on Integer32"""
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


_NetConfigHttpsState_Type.__name__ = "Integer32"
_NetConfigHttpsState_Object = MibScalar
netConfigHttpsState = _NetConfigHttpsState_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 13, 9, 1, 6),
    _NetConfigHttpsState_Type()
)
netConfigHttpsState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netConfigHttpsState.setStatus("current")


class _NetConfigHttpsPort_Type(Integer32):
    """Custom type netConfigHttpsPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(514, 65535),
    )


_NetConfigHttpsPort_Type.__name__ = "Integer32"
_NetConfigHttpsPort_Object = MibScalar
netConfigHttpsPort = _NetConfigHttpsPort_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 13, 9, 1, 7),
    _NetConfigHttpsPort_Type()
)
netConfigHttpsPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netConfigHttpsPort.setStatus("current")


class _NetConfigDHCPState_Type(Integer32):
    """Custom type netConfigDHCPState based on Integer32"""
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


_NetConfigDHCPState_Type.__name__ = "Integer32"
_NetConfigDHCPState_Object = MibScalar
netConfigDHCPState = _NetConfigDHCPState_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 13, 9, 1, 8),
    _NetConfigDHCPState_Type()
)
netConfigDHCPState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netConfigDHCPState.setStatus("current")
_ApFilterControlMgnt_ObjectIdentity = ObjectIdentity
apFilterControlMgnt = _ApFilterControlMgnt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 13, 10)
)


class _ApFilterControlBridge_Type(Integer32):
    """Custom type apFilterControlBridge based on Integer32"""
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


_ApFilterControlBridge_Type.__name__ = "Integer32"
_ApFilterControlBridge_Object = MibScalar
apFilterControlBridge = _ApFilterControlBridge_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 13, 10, 1),
    _ApFilterControlBridge_Type()
)
apFilterControlBridge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apFilterControlBridge.setStatus("current")


class _EnterpriseApFilterControlAPManage_Type(Integer32):
    """Custom type enterpriseApFilterControlAPManage based on Integer32"""
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


_EnterpriseApFilterControlAPManage_Type.__name__ = "Integer32"
_EnterpriseApFilterControlAPManage_Object = MibScalar
enterpriseApFilterControlAPManage = _EnterpriseApFilterControlAPManage_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 13, 10, 2),
    _EnterpriseApFilterControlAPManage_Type()
)
enterpriseApFilterControlAPManage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enterpriseApFilterControlAPManage.setStatus("current")


class _EnterpriseApFilterControlEthernet_Type(Integer32):
    """Custom type enterpriseApFilterControlEthernet based on Integer32"""
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


_EnterpriseApFilterControlEthernet_Type.__name__ = "Integer32"
_EnterpriseApFilterControlEthernet_Object = MibScalar
enterpriseApFilterControlEthernet = _EnterpriseApFilterControlEthernet_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 13, 10, 3),
    _EnterpriseApFilterControlEthernet_Type()
)
enterpriseApFilterControlEthernet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enterpriseApFilterControlEthernet.setStatus("current")
_EnterpriseApFilterProtocolTable_Object = MibTable
enterpriseApFilterProtocolTable = _EnterpriseApFilterProtocolTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 13, 10, 4)
)
if mibBuilder.loadTexts:
    enterpriseApFilterProtocolTable.setStatus("current")
_EnterpriseApFilterProtocolEntry_Object = MibTableRow
enterpriseApFilterProtocolEntry = _EnterpriseApFilterProtocolEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 13, 10, 4, 1)
)
enterpriseApFilterProtocolEntry.setIndexNames(
    (0, "CTRON-AP3000-MIB", "enterpriseApFilterProtocolIndex"),
)
if mibBuilder.loadTexts:
    enterpriseApFilterProtocolEntry.setStatus("current")


class _EnterpriseApFilterProtocolIndex_Type(Integer32):
    """Custom type enterpriseApFilterProtocolIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_EnterpriseApFilterProtocolIndex_Type.__name__ = "Integer32"
_EnterpriseApFilterProtocolIndex_Object = MibTableColumn
enterpriseApFilterProtocolIndex = _EnterpriseApFilterProtocolIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 13, 10, 4, 1, 1),
    _EnterpriseApFilterProtocolIndex_Type()
)
enterpriseApFilterProtocolIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    enterpriseApFilterProtocolIndex.setStatus("current")
_EnterpriseApFilterProtocolName_Type = DisplayString
_EnterpriseApFilterProtocolName_Object = MibTableColumn
enterpriseApFilterProtocolName = _EnterpriseApFilterProtocolName_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 13, 10, 4, 1, 2),
    _EnterpriseApFilterProtocolName_Type()
)
enterpriseApFilterProtocolName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enterpriseApFilterProtocolName.setStatus("current")
_EnterpriseApFilterProtocolISODesignator_Type = DisplayString
_EnterpriseApFilterProtocolISODesignator_Object = MibTableColumn
enterpriseApFilterProtocolISODesignator = _EnterpriseApFilterProtocolISODesignator_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 13, 10, 4, 1, 3),
    _EnterpriseApFilterProtocolISODesignator_Type()
)
enterpriseApFilterProtocolISODesignator.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enterpriseApFilterProtocolISODesignator.setStatus("current")


class _EnterpriseApFilterProtocolState_Type(Integer32):
    """Custom type enterpriseApFilterProtocolState based on Integer32"""
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


_EnterpriseApFilterProtocolState_Type.__name__ = "Integer32"
_EnterpriseApFilterProtocolState_Object = MibTableColumn
enterpriseApFilterProtocolState = _EnterpriseApFilterProtocolState_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 13, 10, 4, 1, 4),
    _EnterpriseApFilterProtocolState_Type()
)
enterpriseApFilterProtocolState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enterpriseApFilterProtocolState.setStatus("current")


class _ApvGlobalIBSSRelayMode_Type(Integer32):
    """Custom type apvGlobalIBSSRelayMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("allVapModeEnable", 2),
          ("perVapModeEnable", 1))
    )


_ApvGlobalIBSSRelayMode_Type.__name__ = "Integer32"
_ApvGlobalIBSSRelayMode_Object = MibScalar
apvGlobalIBSSRelayMode = _ApvGlobalIBSSRelayMode_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 13, 10, 5),
    _ApvGlobalIBSSRelayMode_Type()
)
apvGlobalIBSSRelayMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apvGlobalIBSSRelayMode.setStatus("current")
_ApvFilterControlTable_Object = MibTable
apvFilterControlTable = _ApvFilterControlTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 13, 10, 6)
)
if mibBuilder.loadTexts:
    apvFilterControlTable.setStatus("current")
_ApvFilterControlEntry_Object = MibTableRow
apvFilterControlEntry = _ApvFilterControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 13, 10, 6, 1)
)
apvFilterControlEntry.setIndexNames(
    (0, "CTRON-AP3000-MIB", "apvFilterControlIndex"),
)
if mibBuilder.loadTexts:
    apvFilterControlEntry.setStatus("current")


class _ApvFilterControlIndex_Type(Integer32):
    """Custom type apvFilterControlIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_ApvFilterControlIndex_Type.__name__ = "Integer32"
_ApvFilterControlIndex_Object = MibTableColumn
apvFilterControlIndex = _ApvFilterControlIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 13, 10, 6, 1, 1),
    _ApvFilterControlIndex_Type()
)
apvFilterControlIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    apvFilterControlIndex.setStatus("current")


class _ApvIBSSFilterControl_Type(Integer32):
    """Custom type apvIBSSFilterControl based on Integer32"""
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


_ApvIBSSFilterControl_Type.__name__ = "Integer32"
_ApvIBSSFilterControl_Object = MibTableColumn
apvIBSSFilterControl = _ApvIBSSFilterControl_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 13, 10, 6, 1, 2),
    _ApvIBSSFilterControl_Type()
)
apvIBSSFilterControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apvIBSSFilterControl.setStatus("current")


class _ApvAPManageFilterControl_Type(Integer32):
    """Custom type apvAPManageFilterControl based on Integer32"""
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


_ApvAPManageFilterControl_Type.__name__ = "Integer32"
_ApvAPManageFilterControl_Object = MibTableColumn
apvAPManageFilterControl = _ApvAPManageFilterControl_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 13, 10, 6, 1, 3),
    _ApvAPManageFilterControl_Type()
)
apvAPManageFilterControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apvAPManageFilterControl.setStatus("current")
_ApVLANMgnt_ObjectIdentity = ObjectIdentity
apVLANMgnt = _ApVLANMgnt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 13, 11)
)
_ApVLANMgntNativeId_Type = Integer32
_ApVLANMgntNativeId_Object = MibScalar
apVLANMgntNativeId = _ApVLANMgntNativeId_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 13, 11, 1),
    _ApVLANMgntNativeId_Type()
)
apVLANMgntNativeId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apVLANMgntNativeId.setStatus("current")


class _ApVLANMgntState_Type(Integer32):
    """Custom type apVLANMgntState based on Integer32"""
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


_ApVLANMgntState_Type.__name__ = "Integer32"
_ApVLANMgntState_Object = MibScalar
apVLANMgntState = _ApVLANMgntState_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 13, 11, 2),
    _ApVLANMgntState_Type()
)
apVLANMgntState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apVLANMgntState.setStatus("current")


class _ApVLANMgntStateNextBoot_Type(Integer32):
    """Custom type apVLANMgntStateNextBoot based on Integer32"""
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


_ApVLANMgntStateNextBoot_Type.__name__ = "Integer32"
_ApVLANMgntStateNextBoot_Object = MibScalar
apVLANMgntStateNextBoot = _ApVLANMgntStateNextBoot_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 13, 11, 3),
    _ApVLANMgntStateNextBoot_Type()
)
apVLANMgntStateNextBoot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apVLANMgntStateNextBoot.setStatus("current")
_ApNativeVlanTable_Object = MibTable
apNativeVlanTable = _ApNativeVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 13, 11, 6)
)
if mibBuilder.loadTexts:
    apNativeVlanTable.setStatus("current")
_ApNativeVlanEntry_Object = MibTableRow
apNativeVlanEntry = _ApNativeVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 13, 11, 6, 1)
)
apNativeVlanEntry.setIndexNames(
    (0, "CTRON-AP3000-MIB", "apNativeVlanIfIndex"),
    (0, "CTRON-AP3000-MIB", "apNativeVlanSsidNumber"),
)
if mibBuilder.loadTexts:
    apNativeVlanEntry.setStatus("current")


class _ApNativeVlanIfIndex_Type(Integer32):
    """Custom type apNativeVlanIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_ApNativeVlanIfIndex_Type.__name__ = "Integer32"
_ApNativeVlanIfIndex_Object = MibTableColumn
apNativeVlanIfIndex = _ApNativeVlanIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 13, 11, 6, 1, 1),
    _ApNativeVlanIfIndex_Type()
)
apNativeVlanIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    apNativeVlanIfIndex.setStatus("current")


class _ApNativeVlanSsidNumber_Type(Integer32):
    """Custom type apNativeVlanSsidNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_ApNativeVlanSsidNumber_Type.__name__ = "Integer32"
_ApNativeVlanSsidNumber_Object = MibTableColumn
apNativeVlanSsidNumber = _ApNativeVlanSsidNumber_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 13, 11, 6, 1, 2),
    _ApNativeVlanSsidNumber_Type()
)
apNativeVlanSsidNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    apNativeVlanSsidNumber.setStatus("current")
_ApNativeVlanVlanId_Type = Integer32
_ApNativeVlanVlanId_Object = MibTableColumn
apNativeVlanVlanId = _ApNativeVlanVlanId_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 13, 11, 6, 1, 3),
    _ApNativeVlanVlanId_Type()
)
apNativeVlanVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apNativeVlanVlanId.setStatus("current")


class _ApNativeVlanState_Type(Integer32):
    """Custom type apNativeVlanState based on Integer32"""
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


_ApNativeVlanState_Type.__name__ = "Integer32"
_ApNativeVlanState_Object = MibTableColumn
apNativeVlanState = _ApNativeVlanState_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 13, 11, 6, 1, 4),
    _ApNativeVlanState_Type()
)
apNativeVlanState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apNativeVlanState.setStatus("current")
_ApVLANMgntEtherUntaggedVlanId_Type = Integer32
_ApVLANMgntEtherUntaggedVlanId_Object = MibScalar
apVLANMgntEtherUntaggedVlanId = _ApVLANMgntEtherUntaggedVlanId_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 13, 11, 7),
    _ApVLANMgntEtherUntaggedVlanId_Type()
)
apVLANMgntEtherUntaggedVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apVLANMgntEtherUntaggedVlanId.setStatus("current")
_ApAuthenticationMgnt_ObjectIdentity = ObjectIdentity
apAuthenticationMgnt = _ApAuthenticationMgnt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 13, 12)
)
_ApAuthenticationSetupEntry_ObjectIdentity = ObjectIdentity
apAuthenticationSetupEntry = _ApAuthenticationSetupEntry_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 13, 12, 1)
)


class _Ap8021xState_Type(Integer32):
    """Custom type ap8021xState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("required", 2),
          ("supported", 1))
    )


_Ap8021xState_Type.__name__ = "Integer32"
_Ap8021xState_Object = MibScalar
ap8021xState = _Ap8021xState_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 13, 12, 1, 1),
    _Ap8021xState_Type()
)
ap8021xState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ap8021xState.setStatus("current")


class _Ap8021xBroadcastKeyRefreshRate_Type(Integer32):
    """Custom type ap8021xBroadcastKeyRefreshRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1440),
    )


_Ap8021xBroadcastKeyRefreshRate_Type.__name__ = "Integer32"
_Ap8021xBroadcastKeyRefreshRate_Object = MibScalar
ap8021xBroadcastKeyRefreshRate = _Ap8021xBroadcastKeyRefreshRate_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 13, 12, 1, 2),
    _Ap8021xBroadcastKeyRefreshRate_Type()
)
ap8021xBroadcastKeyRefreshRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ap8021xBroadcastKeyRefreshRate.setStatus("current")


class _Ap8021xSessionKeyRefreshRate_Type(Integer32):
    """Custom type ap8021xSessionKeyRefreshRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1440),
    )


_Ap8021xSessionKeyRefreshRate_Type.__name__ = "Integer32"
_Ap8021xSessionKeyRefreshRate_Object = MibScalar
ap8021xSessionKeyRefreshRate = _Ap8021xSessionKeyRefreshRate_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 13, 12, 1, 3),
    _Ap8021xSessionKeyRefreshRate_Type()
)
ap8021xSessionKeyRefreshRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ap8021xSessionKeyRefreshRate.setStatus("current")


class _Ap8021xReauthenticationTimeout_Type(Integer32):
    """Custom type ap8021xReauthenticationTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1440),
    )


_Ap8021xReauthenticationTimeout_Type.__name__ = "Integer32"
_Ap8021xReauthenticationTimeout_Object = MibScalar
ap8021xReauthenticationTimeout = _Ap8021xReauthenticationTimeout_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 13, 12, 1, 4),
    _Ap8021xReauthenticationTimeout_Type()
)
ap8021xReauthenticationTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ap8021xReauthenticationTimeout.setStatus("current")


class _ApAuthenticationMode_Type(Integer32):
    """Custom type apAuthenticationMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("local", 1),
          ("radius", 2))
    )


_ApAuthenticationMode_Type.__name__ = "Integer32"
_ApAuthenticationMode_Object = MibScalar
apAuthenticationMode = _ApAuthenticationMode_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 13, 12, 1, 5),
    _ApAuthenticationMode_Type()
)
apAuthenticationMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apAuthenticationMode.setStatus("current")
_ApAuthenticationServerTable_Object = MibTable
apAuthenticationServerTable = _ApAuthenticationServerTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 13, 12, 2)
)
if mibBuilder.loadTexts:
    apAuthenticationServerTable.setStatus("current")
_ApAuthenticationServerEntry_Object = MibTableRow
apAuthenticationServerEntry = _ApAuthenticationServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 13, 12, 2, 1)
)
apAuthenticationServerEntry.setIndexNames(
    (0, "CTRON-AP3000-MIB", "apAuthenticationServerIndex"),
)
if mibBuilder.loadTexts:
    apAuthenticationServerEntry.setStatus("current")


class _ApAuthenticationServerIndex_Type(Integer32):
    """Custom type apAuthenticationServerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_ApAuthenticationServerIndex_Type.__name__ = "Integer32"
_ApAuthenticationServerIndex_Object = MibTableColumn
apAuthenticationServerIndex = _ApAuthenticationServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 13, 12, 2, 1, 1),
    _ApAuthenticationServerIndex_Type()
)
apAuthenticationServerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    apAuthenticationServerIndex.setStatus("current")


class _ApAuthenticationServer_Type(DisplayString):
    """Custom type apAuthenticationServer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_ApAuthenticationServer_Type.__name__ = "DisplayString"
_ApAuthenticationServer_Object = MibTableColumn
apAuthenticationServer = _ApAuthenticationServer_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 13, 12, 2, 1, 2),
    _ApAuthenticationServer_Type()
)
apAuthenticationServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apAuthenticationServer.setStatus("current")


class _ApAuthenticationPort_Type(Integer32):
    """Custom type apAuthenticationPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1024, 65535),
    )


_ApAuthenticationPort_Type.__name__ = "Integer32"
_ApAuthenticationPort_Object = MibTableColumn
apAuthenticationPort = _ApAuthenticationPort_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 13, 12, 2, 1, 3),
    _ApAuthenticationPort_Type()
)
apAuthenticationPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apAuthenticationPort.setStatus("current")


class _ApAuthenticationKey_Type(DisplayString):
    """Custom type apAuthenticationKey based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_ApAuthenticationKey_Type.__name__ = "DisplayString"
_ApAuthenticationKey_Object = MibTableColumn
apAuthenticationKey = _ApAuthenticationKey_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 13, 12, 2, 1, 4),
    _ApAuthenticationKey_Type()
)
apAuthenticationKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apAuthenticationKey.setStatus("current")


class _ApAuthenticationRetransmit_Type(Integer32):
    """Custom type apAuthenticationRetransmit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_ApAuthenticationRetransmit_Type.__name__ = "Integer32"
_ApAuthenticationRetransmit_Object = MibTableColumn
apAuthenticationRetransmit = _ApAuthenticationRetransmit_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 13, 12, 2, 1, 5),
    _ApAuthenticationRetransmit_Type()
)
apAuthenticationRetransmit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apAuthenticationRetransmit.setStatus("current")


class _ApAuthenticationTimeout_Type(Integer32):
    """Custom type apAuthenticationTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_ApAuthenticationTimeout_Type.__name__ = "Integer32"
_ApAuthenticationTimeout_Object = MibTableColumn
apAuthenticationTimeout = _ApAuthenticationTimeout_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 13, 12, 2, 1, 6),
    _ApAuthenticationTimeout_Type()
)
apAuthenticationTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apAuthenticationTimeout.setStatus("current")


class _ApAuthenticationAcctPort_Type(Integer32):
    """Custom type apAuthenticationAcctPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ApAuthenticationAcctPort_Type.__name__ = "Integer32"
_ApAuthenticationAcctPort_Object = MibTableColumn
apAuthenticationAcctPort = _ApAuthenticationAcctPort_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 13, 12, 2, 1, 7),
    _ApAuthenticationAcctPort_Type()
)
apAuthenticationAcctPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apAuthenticationAcctPort.setStatus("current")


class _ApAuthenticationAcctInterimUpdate_Type(Integer32):
    """Custom type apAuthenticationAcctInterimUpdate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 86400),
    )


_ApAuthenticationAcctInterimUpdate_Type.__name__ = "Integer32"
_ApAuthenticationAcctInterimUpdate_Object = MibTableColumn
apAuthenticationAcctInterimUpdate = _ApAuthenticationAcctInterimUpdate_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 13, 12, 2, 1, 8),
    _ApAuthenticationAcctInterimUpdate_Type()
)
apAuthenticationAcctInterimUpdate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apAuthenticationAcctInterimUpdate.setStatus("current")


class _ApAuthenticationAcctState_Type(Integer32):
    """Custom type apAuthenticationAcctState based on Integer32"""
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


_ApAuthenticationAcctState_Type.__name__ = "Integer32"
_ApAuthenticationAcctState_Object = MibTableColumn
apAuthenticationAcctState = _ApAuthenticationAcctState_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 13, 12, 2, 1, 9),
    _ApAuthenticationAcctState_Type()
)
apAuthenticationAcctState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apAuthenticationAcctState.setStatus("current")
_ApAuthenticationSupplicantTable_Object = MibTable
apAuthenticationSupplicantTable = _ApAuthenticationSupplicantTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 13, 12, 3)
)
if mibBuilder.loadTexts:
    apAuthenticationSupplicantTable.setStatus("current")
_ApAuthenticationSupplicantEntry_Object = MibTableRow
apAuthenticationSupplicantEntry = _ApAuthenticationSupplicantEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 13, 12, 3, 1)
)
apAuthenticationSupplicantEntry.setIndexNames(
    (0, "CTRON-AP3000-MIB", "ap8021xSuppIndex"),
)
if mibBuilder.loadTexts:
    apAuthenticationSupplicantEntry.setStatus("current")


class _Ap8021xSuppIndex_Type(Integer32):
    """Custom type ap8021xSuppIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Ap8021xSuppIndex_Type.__name__ = "Integer32"
_Ap8021xSuppIndex_Object = MibTableColumn
ap8021xSuppIndex = _Ap8021xSuppIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 13, 12, 3, 1, 1),
    _Ap8021xSuppIndex_Type()
)
ap8021xSuppIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ap8021xSuppIndex.setStatus("current")


class _Ap8021xSuppState_Type(Integer32):
    """Custom type ap8021xSuppState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_Ap8021xSuppState_Type.__name__ = "Integer32"
_Ap8021xSuppState_Object = MibTableColumn
ap8021xSuppState = _Ap8021xSuppState_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 13, 12, 3, 1, 2),
    _Ap8021xSuppState_Type()
)
ap8021xSuppState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ap8021xSuppState.setStatus("current")


class _Ap8021xSuppUser_Type(DisplayString):
    """Custom type ap8021xSuppUser based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_Ap8021xSuppUser_Type.__name__ = "DisplayString"
_Ap8021xSuppUser_Object = MibTableColumn
ap8021xSuppUser = _Ap8021xSuppUser_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 13, 12, 3, 1, 3),
    _Ap8021xSuppUser_Type()
)
ap8021xSuppUser.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ap8021xSuppUser.setStatus("current")


class _Ap8021xSuppPasswd_Type(DisplayString):
    """Custom type ap8021xSuppPasswd based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_Ap8021xSuppPasswd_Type.__name__ = "DisplayString"
_Ap8021xSuppPasswd_Object = MibTableColumn
ap8021xSuppPasswd = _Ap8021xSuppPasswd_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 13, 12, 3, 1, 4),
    _Ap8021xSuppPasswd_Type()
)
ap8021xSuppPasswd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ap8021xSuppPasswd.setStatus("current")
_ApvAuthenticationSetupTable_Object = MibTable
apvAuthenticationSetupTable = _ApvAuthenticationSetupTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 13, 12, 4)
)
if mibBuilder.loadTexts:
    apvAuthenticationSetupTable.setStatus("current")
_ApvAuthenticationSetupEntry_Object = MibTableRow
apvAuthenticationSetupEntry = _ApvAuthenticationSetupEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 13, 12, 4, 1)
)
apvAuthenticationSetupEntry.setIndexNames(
    (0, "CTRON-AP3000-MIB", "apv8021xIndex"),
)
if mibBuilder.loadTexts:
    apvAuthenticationSetupEntry.setStatus("current")


class _Apv8021xIndex_Type(Integer32):
    """Custom type apv8021xIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Apv8021xIndex_Type.__name__ = "Integer32"
_Apv8021xIndex_Object = MibTableColumn
apv8021xIndex = _Apv8021xIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 13, 12, 4, 1, 1),
    _Apv8021xIndex_Type()
)
apv8021xIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    apv8021xIndex.setStatus("current")


class _Apv8021xState_Type(Integer32):
    """Custom type apv8021xState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("required", 2),
          ("supported", 1))
    )


_Apv8021xState_Type.__name__ = "Integer32"
_Apv8021xState_Object = MibTableColumn
apv8021xState = _Apv8021xState_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 13, 12, 4, 1, 2),
    _Apv8021xState_Type()
)
apv8021xState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apv8021xState.setStatus("current")


class _Apv8021xBroadcastKeyRefreshRate_Type(Integer32):
    """Custom type apv8021xBroadcastKeyRefreshRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1440),
    )


_Apv8021xBroadcastKeyRefreshRate_Type.__name__ = "Integer32"
_Apv8021xBroadcastKeyRefreshRate_Object = MibTableColumn
apv8021xBroadcastKeyRefreshRate = _Apv8021xBroadcastKeyRefreshRate_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 13, 12, 4, 1, 3),
    _Apv8021xBroadcastKeyRefreshRate_Type()
)
apv8021xBroadcastKeyRefreshRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apv8021xBroadcastKeyRefreshRate.setStatus("current")


class _Apv8021xSessionKeyRefreshRate_Type(Integer32):
    """Custom type apv8021xSessionKeyRefreshRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1440),
    )


_Apv8021xSessionKeyRefreshRate_Type.__name__ = "Integer32"
_Apv8021xSessionKeyRefreshRate_Object = MibTableColumn
apv8021xSessionKeyRefreshRate = _Apv8021xSessionKeyRefreshRate_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 13, 12, 4, 1, 4),
    _Apv8021xSessionKeyRefreshRate_Type()
)
apv8021xSessionKeyRefreshRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apv8021xSessionKeyRefreshRate.setStatus("current")


class _Apv8021xReauthenticationTimeout_Type(Integer32):
    """Custom type apv8021xReauthenticationTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Apv8021xReauthenticationTimeout_Type.__name__ = "Integer32"
_Apv8021xReauthenticationTimeout_Object = MibTableColumn
apv8021xReauthenticationTimeout = _Apv8021xReauthenticationTimeout_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 13, 12, 4, 1, 5),
    _Apv8021xReauthenticationTimeout_Type()
)
apv8021xReauthenticationTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apv8021xReauthenticationTimeout.setStatus("current")


class _ApvMACAuthenticationMode_Type(Integer32):
    """Custom type apvMACAuthenticationMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("local", 1),
          ("remote", 2))
    )


_ApvMACAuthenticationMode_Type.__name__ = "Integer32"
_ApvMACAuthenticationMode_Object = MibTableColumn
apvMACAuthenticationMode = _ApvMACAuthenticationMode_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 13, 12, 4, 1, 6),
    _ApvMACAuthenticationMode_Type()
)
apvMACAuthenticationMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apvMACAuthenticationMode.setStatus("current")


class _ApvMACAuthenticationTimeout_Type(Integer32):
    """Custom type apvMACAuthenticationTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ApvMACAuthenticationTimeout_Type.__name__ = "Integer32"
_ApvMACAuthenticationTimeout_Object = MibTableColumn
apvMACAuthenticationTimeout = _ApvMACAuthenticationTimeout_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 13, 12, 4, 1, 7),
    _ApvMACAuthenticationTimeout_Type()
)
apvMACAuthenticationTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apvMACAuthenticationTimeout.setStatus("current")


class _ApvMACAuthenticationPasswd_Type(DisplayString):
    """Custom type apvMACAuthenticationPasswd based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_ApvMACAuthenticationPasswd_Type.__name__ = "DisplayString"
_ApvMACAuthenticationPasswd_Object = MibTableColumn
apvMACAuthenticationPasswd = _ApvMACAuthenticationPasswd_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 13, 12, 4, 1, 8),
    _ApvMACAuthenticationPasswd_Type()
)
apvMACAuthenticationPasswd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apvMACAuthenticationPasswd.setStatus("current")
_ApWStationSessionMgnt_ObjectIdentity = ObjectIdentity
apWStationSessionMgnt = _ApWStationSessionMgnt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 13, 13)
)
_ApWStationSessionTable_Object = MibTable
apWStationSessionTable = _ApWStationSessionTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 13, 13, 1)
)
if mibBuilder.loadTexts:
    apWStationSessionTable.setStatus("current")
_ApWStationSessionEntry_Object = MibTableRow
apWStationSessionEntry = _ApWStationSessionEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 13, 13, 1, 1)
)
apWStationSessionEntry.setIndexNames(
    (0, "CTRON-AP3000-MIB", "apWStationSessionIfIndex"),
    (0, "CTRON-AP3000-MIB", "apWStationSessionStationAddres"),
)
if mibBuilder.loadTexts:
    apWStationSessionEntry.setStatus("current")


class _ApWStationSessionIfIndex_Type(Integer32):
    """Custom type apWStationSessionIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_ApWStationSessionIfIndex_Type.__name__ = "Integer32"
_ApWStationSessionIfIndex_Object = MibTableColumn
apWStationSessionIfIndex = _ApWStationSessionIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 13, 13, 1, 1, 1),
    _ApWStationSessionIfIndex_Type()
)
apWStationSessionIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    apWStationSessionIfIndex.setStatus("current")
_ApWStationSessionStationAddres_Type = MacAddress
_ApWStationSessionStationAddres_Object = MibTableColumn
apWStationSessionStationAddres = _ApWStationSessionStationAddres_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 13, 13, 1, 1, 2),
    _ApWStationSessionStationAddres_Type()
)
apWStationSessionStationAddres.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    apWStationSessionStationAddres.setStatus("current")
_ApWStationSessionAuthenticated_Type = TruthValue
_ApWStationSessionAuthenticated_Object = MibTableColumn
apWStationSessionAuthenticated = _ApWStationSessionAuthenticated_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 13, 13, 1, 1, 3),
    _ApWStationSessionAuthenticated_Type()
)
apWStationSessionAuthenticated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apWStationSessionAuthenticated.setStatus("current")
_ApWStationSessionAssociated_Type = TruthValue
_ApWStationSessionAssociated_Object = MibTableColumn
apWStationSessionAssociated = _ApWStationSessionAssociated_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 13, 13, 1, 1, 4),
    _ApWStationSessionAssociated_Type()
)
apWStationSessionAssociated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apWStationSessionAssociated.setStatus("current")
_ApWStationSessionIsForwarding_Type = TruthValue
_ApWStationSessionIsForwarding_Object = MibTableColumn
apWStationSessionIsForwarding = _ApWStationSessionIsForwarding_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 13, 13, 1, 1, 5),
    _ApWStationSessionIsForwarding_Type()
)
apWStationSessionIsForwarding.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apWStationSessionIsForwarding.setStatus("current")


class _ApWStationSessionKeyType_Type(Integer32):
    """Custom type apWStationSessionKeyType based on Integer32"""
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
        *(("dynamicWep", 3),
          ("none", 1),
          ("staticWep", 2),
          ("wpaAes", 6),
          ("wpaTkip", 5),
          ("wpaWep", 4))
    )


_ApWStationSessionKeyType_Type.__name__ = "Integer32"
_ApWStationSessionKeyType_Object = MibTableColumn
apWStationSessionKeyType = _ApWStationSessionKeyType_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 13, 13, 1, 1, 6),
    _ApWStationSessionKeyType_Type()
)
apWStationSessionKeyType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apWStationSessionKeyType.setStatus("current")
_ApWStationSessionAssociationId_Type = Integer32
_ApWStationSessionAssociationId_Object = MibTableColumn
apWStationSessionAssociationId = _ApWStationSessionAssociationId_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 13, 13, 1, 1, 7),
    _ApWStationSessionAssociationId_Type()
)
apWStationSessionAssociationId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apWStationSessionAssociationId.setStatus("current")
_ApWStationSessionLastAuthenticatedTime_Type = TimeTicks
_ApWStationSessionLastAuthenticatedTime_Object = MibTableColumn
apWStationSessionLastAuthenticatedTime = _ApWStationSessionLastAuthenticatedTime_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 13, 13, 1, 1, 8),
    _ApWStationSessionLastAuthenticatedTime_Type()
)
apWStationSessionLastAuthenticatedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apWStationSessionLastAuthenticatedTime.setStatus("current")
_ApWStationSessionAssociatedTime_Type = TimeTicks
_ApWStationSessionAssociatedTime_Object = MibTableColumn
apWStationSessionAssociatedTime = _ApWStationSessionAssociatedTime_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 13, 13, 1, 1, 9),
    _ApWStationSessionAssociatedTime_Type()
)
apWStationSessionAssociatedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apWStationSessionAssociatedTime.setStatus("current")
_ApWStationSessionLastAssociatedTime_Type = TimeTicks
_ApWStationSessionLastAssociatedTime_Object = MibTableColumn
apWStationSessionLastAssociatedTime = _ApWStationSessionLastAssociatedTime_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 13, 13, 1, 1, 10),
    _ApWStationSessionLastAssociatedTime_Type()
)
apWStationSessionLastAssociatedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apWStationSessionLastAssociatedTime.setStatus("current")
_ApWStationSessionLastDisassociatedTime_Type = TimeTicks
_ApWStationSessionLastDisassociatedTime_Object = MibTableColumn
apWStationSessionLastDisassociatedTime = _ApWStationSessionLastDisassociatedTime_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 13, 13, 1, 1, 11),
    _ApWStationSessionLastDisassociatedTime_Type()
)
apWStationSessionLastDisassociatedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apWStationSessionLastDisassociatedTime.setStatus("current")
_ApWStationSessionTxPacketCount_Type = Counter32
_ApWStationSessionTxPacketCount_Object = MibTableColumn
apWStationSessionTxPacketCount = _ApWStationSessionTxPacketCount_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 13, 13, 1, 1, 12),
    _ApWStationSessionTxPacketCount_Type()
)
apWStationSessionTxPacketCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apWStationSessionTxPacketCount.setStatus("current")
_ApWStationSessionRxPacketCount_Type = Counter32
_ApWStationSessionRxPacketCount_Object = MibTableColumn
apWStationSessionRxPacketCount = _ApWStationSessionRxPacketCount_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 13, 13, 1, 1, 13),
    _ApWStationSessionRxPacketCount_Type()
)
apWStationSessionRxPacketCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apWStationSessionRxPacketCount.setStatus("current")
_ApWStationSessionTxByteCount_Type = Counter32
_ApWStationSessionTxByteCount_Object = MibTableColumn
apWStationSessionTxByteCount = _ApWStationSessionTxByteCount_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 13, 13, 1, 1, 14),
    _ApWStationSessionTxByteCount_Type()
)
apWStationSessionTxByteCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apWStationSessionTxByteCount.setStatus("current")
_ApWStationSessionRxByteCount_Type = Counter32
_ApWStationSessionRxByteCount_Object = MibTableColumn
apWStationSessionRxByteCount = _ApWStationSessionRxByteCount_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 13, 13, 1, 1, 15),
    _ApWStationSessionRxByteCount_Type()
)
apWStationSessionRxByteCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apWStationSessionRxByteCount.setStatus("current")
_ApWStationSessionVlanID_Type = Integer32
_ApWStationSessionVlanID_Object = MibTableColumn
apWStationSessionVlanID = _ApWStationSessionVlanID_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 13, 13, 1, 1, 16),
    _ApWStationSessionVlanID_Type()
)
apWStationSessionVlanID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apWStationSessionVlanID.setStatus("current")
_ApRogueApMgnt_ObjectIdentity = ObjectIdentity
apRogueApMgnt = _ApRogueApMgnt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 13, 14)
)
_RogueApDetectionTable_Object = MibTable
rogueApDetectionTable = _RogueApDetectionTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 13, 14, 1)
)
if mibBuilder.loadTexts:
    rogueApDetectionTable.setStatus("current")
_RogueApDetectionEntry_Object = MibTableRow
rogueApDetectionEntry = _RogueApDetectionEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 13, 14, 1, 1)
)
rogueApDetectionEntry.setIndexNames(
    (0, "CTRON-AP3000-MIB", "rogueApIndex"),
)
if mibBuilder.loadTexts:
    rogueApDetectionEntry.setStatus("current")


class _RogueApIndex_Type(Integer32):
    """Custom type rogueApIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_RogueApIndex_Type.__name__ = "Integer32"
_RogueApIndex_Object = MibTableColumn
rogueApIndex = _RogueApIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 13, 14, 1, 1, 1),
    _RogueApIndex_Type()
)
rogueApIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rogueApIndex.setStatus("current")


class _RogueApBssid_Type(DisplayString):
    """Custom type rogueApBssid based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 6),
    )


_RogueApBssid_Type.__name__ = "DisplayString"
_RogueApBssid_Object = MibTableColumn
rogueApBssid = _RogueApBssid_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 13, 14, 1, 1, 2),
    _RogueApBssid_Type()
)
rogueApBssid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rogueApBssid.setStatus("current")


class _RogueApSsid_Type(DisplayString):
    """Custom type rogueApSsid based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_RogueApSsid_Type.__name__ = "DisplayString"
_RogueApSsid_Object = MibTableColumn
rogueApSsid = _RogueApSsid_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 13, 14, 1, 1, 3),
    _RogueApSsid_Type()
)
rogueApSsid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rogueApSsid.setStatus("current")
_RogueApPortNumber_Type = Integer32
_RogueApPortNumber_Object = MibTableColumn
rogueApPortNumber = _RogueApPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 13, 14, 1, 1, 4),
    _RogueApPortNumber_Type()
)
rogueApPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rogueApPortNumber.setStatus("current")
_RogueApChannelNumber_Type = Integer32
_RogueApChannelNumber_Object = MibTableColumn
rogueApChannelNumber = _RogueApChannelNumber_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 13, 14, 1, 1, 5),
    _RogueApChannelNumber_Type()
)
rogueApChannelNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rogueApChannelNumber.setStatus("current")
_RogueApRSSIValue_Type = Integer32
_RogueApRSSIValue_Object = MibTableColumn
rogueApRSSIValue = _RogueApRSSIValue_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 13, 14, 1, 1, 6),
    _RogueApRSSIValue_Type()
)
rogueApRSSIValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rogueApRSSIValue.setStatus("current")
_ApRougeApControl_ObjectIdentity = ObjectIdentity
apRougeApControl = _ApRougeApControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 13, 14, 2)
)


class _RogueApRADIUSAuthenticate_Type(Integer32):
    """Custom type rogueApRADIUSAuthenticate based on Integer32"""
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


_RogueApRADIUSAuthenticate_Type.__name__ = "Integer32"
_RogueApRADIUSAuthenticate_Object = MibScalar
rogueApRADIUSAuthenticate = _RogueApRADIUSAuthenticate_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 13, 14, 2, 1),
    _RogueApRADIUSAuthenticate_Type()
)
rogueApRADIUSAuthenticate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rogueApRADIUSAuthenticate.setStatus("current")


class _RogueApClear_Type(Integer32):
    """Custom type rogueApClear based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("clear", 1)
    )


_RogueApClear_Type.__name__ = "Integer32"
_RogueApClear_Object = MibScalar
rogueApClear = _RogueApClear_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 13, 14, 2, 2),
    _RogueApClear_Type()
)
rogueApClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rogueApClear.setStatus("current")
_ApAdminMgnt_ObjectIdentity = ObjectIdentity
apAdminMgnt = _ApAdminMgnt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 13, 15)
)


class _ApAdminUsername_Type(DisplayString):
    """Custom type apAdminUsername based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_ApAdminUsername_Type.__name__ = "DisplayString"
_ApAdminUsername_Object = MibScalar
apAdminUsername = _ApAdminUsername_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 13, 15, 1),
    _ApAdminUsername_Type()
)
apAdminUsername.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apAdminUsername.setStatus("current")


class _AppAdminPassword_Type(DisplayString):
    """Custom type appAdminPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_AppAdminPassword_Type.__name__ = "DisplayString"
_AppAdminPassword_Object = MibScalar
appAdminPassword = _AppAdminPassword_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 13, 15, 2),
    _AppAdminPassword_Type()
)
appAdminPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    appAdminPassword.setStatus("current")
_ApResetMgt_ObjectIdentity = ObjectIdentity
apResetMgt = _ApResetMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 13, 16)
)


class _ApRestartOpCodeFile_Type(DisplayString):
    """Custom type apRestartOpCodeFile based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_ApRestartOpCodeFile_Type.__name__ = "DisplayString"
_ApRestartOpCodeFile_Object = MibScalar
apRestartOpCodeFile = _ApRestartOpCodeFile_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 13, 16, 1),
    _ApRestartOpCodeFile_Type()
)
apRestartOpCodeFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apRestartOpCodeFile.setStatus("current")


class _ApRestartControl_Type(Integer32):
    """Custom type apRestartControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("coldBoot", 3),
          ("running", 1),
          ("warmBoot", 2))
    )


_ApRestartControl_Type.__name__ = "Integer32"
_ApRestartControl_Object = MibScalar
apRestartControl = _ApRestartControl_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 13, 16, 2),
    _ApRestartControl_Type()
)
apRestartControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apRestartControl.setStatus("current")
_ApSNTPMgnt_ObjectIdentity = ObjectIdentity
apSNTPMgnt = _ApSNTPMgnt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 13, 17)
)


class _ApSNTPState_Type(Integer32):
    """Custom type apSNTPState based on Integer32"""
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


_ApSNTPState_Type.__name__ = "Integer32"
_ApSNTPState_Object = MibScalar
apSNTPState = _ApSNTPState_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 13, 17, 1),
    _ApSNTPState_Type()
)
apSNTPState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apSNTPState.setStatus("current")
_ApSNTPPrimaryServer_Type = IpAddress
_ApSNTPPrimaryServer_Object = MibScalar
apSNTPPrimaryServer = _ApSNTPPrimaryServer_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 13, 17, 2),
    _ApSNTPPrimaryServer_Type()
)
apSNTPPrimaryServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apSNTPPrimaryServer.setStatus("current")
_ApSNTPSecondaryServer_Type = IpAddress
_ApSNTPSecondaryServer_Object = MibScalar
apSNTPSecondaryServer = _ApSNTPSecondaryServer_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 13, 17, 3),
    _ApSNTPSecondaryServer_Type()
)
apSNTPSecondaryServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apSNTPSecondaryServer.setStatus("current")


class _ApSNTPTimezone_Type(Integer32):
    """Custom type apSNTPTimezone based on Integer32"""
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
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              34,
              35,
              36,
              37,
              38,
              39,
              40,
              41,
              42,
              43,
              44,
              45,
              46,
              47,
              48,
              49,
              50,
              51,
              52,
              53)
        )
    )
    namedValues = NamedValues(
        *(("abuDhabi", 39),
          ("alaska", 3),
          ("almaty", 42),
          ("amsterdam", 24),
          ("arizona", 5),
          ("athens", 30),
          ("atlantic", 13),
          ("azores", 20),
          ("baghdad", 36),
          ("bangkok", 43),
          ("beijing", 44),
          ("bogota", 10),
          ("brasilia", 17),
          ("bratislava", 26),
          ("brisbane", 47),
          ("bucharest", 31),
          ("buenos", 18),
          ("cairo", 32),
          ("canberra", 48),
          ("caracas", 14),
          ("casablanca", 21),
          ("central", 7),
          ("eastern", 11),
          ("enewetakKwajalein", 0),
          ("fiji", 52),
          ("greenwichMeanTimeDublin", 22),
          ("greenwichMeanTimeLisbon", 23),
          ("guam", 49),
          ("harare", 33),
          ("hawaii", 2),
          ("helsinki", 34),
          ("hobart", 50),
          ("indiana", 12),
          ("islamabad", 41),
          ("israel", 35),
          ("magadan", 51),
          ("mexicoCity", 8),
          ("midAtlantic", 19),
          ("midwayIsland", 1),
          ("moscow", 37),
          ("mountain", 6),
          ("newfoundland", 16),
          ("pacific", 4),
          ("paris", 28),
          ("prague", 27),
          ("santiago", 15),
          ("saskatchewan", 9),
          ("sofija", 29),
          ("stockholm", 25),
          ("taipei", 45),
          ("tehran", 38),
          ("tokyo", 46),
          ("vogograd", 40),
          ("wellington", 53))
    )


_ApSNTPTimezone_Type.__name__ = "Integer32"
_ApSNTPTimezone_Object = MibScalar
apSNTPTimezone = _ApSNTPTimezone_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 13, 17, 4),
    _ApSNTPTimezone_Type()
)
apSNTPTimezone.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apSNTPTimezone.setStatus("current")


class _ApSNTPDST_Type(Integer32):
    """Custom type apSNTPDST based on Integer32"""
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


_ApSNTPDST_Type.__name__ = "Integer32"
_ApSNTPDST_Object = MibScalar
apSNTPDST = _ApSNTPDST_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 13, 17, 5),
    _ApSNTPDST_Type()
)
apSNTPDST.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apSNTPDST.setStatus("current")


class _ApSNTPDSTStartMonth_Type(Integer32):
    """Custom type apSNTPDSTStartMonth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 12),
    )


_ApSNTPDSTStartMonth_Type.__name__ = "Integer32"
_ApSNTPDSTStartMonth_Object = MibScalar
apSNTPDSTStartMonth = _ApSNTPDSTStartMonth_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 13, 17, 6),
    _ApSNTPDSTStartMonth_Type()
)
apSNTPDSTStartMonth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apSNTPDSTStartMonth.setStatus("current")


class _ApSNTPDSTStartDay_Type(Integer32):
    """Custom type apSNTPDSTStartDay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 31),
    )


_ApSNTPDSTStartDay_Type.__name__ = "Integer32"
_ApSNTPDSTStartDay_Object = MibScalar
apSNTPDSTStartDay = _ApSNTPDSTStartDay_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 13, 17, 7),
    _ApSNTPDSTStartDay_Type()
)
apSNTPDSTStartDay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apSNTPDSTStartDay.setStatus("current")


class _ApSNTPDSTEndMonth_Type(Integer32):
    """Custom type apSNTPDSTEndMonth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 12),
    )


_ApSNTPDSTEndMonth_Type.__name__ = "Integer32"
_ApSNTPDSTEndMonth_Object = MibScalar
apSNTPDSTEndMonth = _ApSNTPDSTEndMonth_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 13, 17, 8),
    _ApSNTPDSTEndMonth_Type()
)
apSNTPDSTEndMonth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apSNTPDSTEndMonth.setStatus("current")


class _ApSNTPDSTEndDay_Type(Integer32):
    """Custom type apSNTPDSTEndDay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 31),
    )


_ApSNTPDSTEndDay_Type.__name__ = "Integer32"
_ApSNTPDSTEndDay_Object = MibScalar
apSNTPDSTEndDay = _ApSNTPDSTEndDay_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 13, 17, 9),
    _ApSNTPDSTEndDay_Type()
)
apSNTPDSTEndDay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apSNTPDSTEndDay.setStatus("current")
_ApDNSMgnt_ObjectIdentity = ObjectIdentity
apDNSMgnt = _ApDNSMgnt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 13, 18)
)
_ApDNSPrimaryServer_Type = IpAddress
_ApDNSPrimaryServer_Object = MibScalar
apDNSPrimaryServer = _ApDNSPrimaryServer_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 13, 18, 1),
    _ApDNSPrimaryServer_Type()
)
apDNSPrimaryServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apDNSPrimaryServer.setStatus("current")
_ApDNSSecondaryServer_Type = IpAddress
_ApDNSSecondaryServer_Object = MibScalar
apDNSSecondaryServer = _ApDNSSecondaryServer_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 13, 18, 2),
    _ApDNSSecondaryServer_Type()
)
apDNSSecondaryServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apDNSSecondaryServer.setStatus("current")
_ApIappMgnt_ObjectIdentity = ObjectIdentity
apIappMgnt = _ApIappMgnt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 13, 19)
)


class _ApIappEnabled_Type(Integer32):
    """Custom type apIappEnabled based on Integer32"""
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


_ApIappEnabled_Type.__name__ = "Integer32"
_ApIappEnabled_Object = MibScalar
apIappEnabled = _ApIappEnabled_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 13, 19, 1),
    _ApIappEnabled_Type()
)
apIappEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apIappEnabled.setStatus("current")
_ApSyslogConfigMgnt_ObjectIdentity = ObjectIdentity
apSyslogConfigMgnt = _ApSyslogConfigMgnt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 13, 20)
)


class _ApLogConfigState_Type(Integer32):
    """Custom type apLogConfigState based on Integer32"""
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


_ApLogConfigState_Type.__name__ = "Integer32"
_ApLogConfigState_Object = MibScalar
apLogConfigState = _ApLogConfigState_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 13, 20, 1),
    _ApLogConfigState_Type()
)
apLogConfigState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apLogConfigState.setStatus("current")


class _ApSyslogConsoleState_Type(Integer32):
    """Custom type apSyslogConsoleState based on Integer32"""
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


_ApSyslogConsoleState_Type.__name__ = "Integer32"
_ApSyslogConsoleState_Object = MibScalar
apSyslogConsoleState = _ApSyslogConsoleState_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 13, 20, 2),
    _ApSyslogConsoleState_Type()
)
apSyslogConsoleState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apSyslogConsoleState.setStatus("current")


class _ApSyslogLevel_Type(Integer32):
    """Custom type apSyslogLevel based on Integer32"""
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
              7)
        )
    )
    namedValues = NamedValues(
        *(("alert", 1),
          ("critical", 2),
          ("debug", 7),
          ("emergency", 0),
          ("error", 3),
          ("info", 6),
          ("notice", 5),
          ("warning", 4))
    )


_ApSyslogLevel_Type.__name__ = "Integer32"
_ApSyslogLevel_Object = MibScalar
apSyslogLevel = _ApSyslogLevel_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 13, 20, 3),
    _ApSyslogLevel_Type()
)
apSyslogLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apSyslogLevel.setStatus("current")
_ApSyslogServerTable_Object = MibTable
apSyslogServerTable = _ApSyslogServerTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 13, 20, 4)
)
if mibBuilder.loadTexts:
    apSyslogServerTable.setStatus("current")
_ApSyslogServerEntry_Object = MibTableRow
apSyslogServerEntry = _ApSyslogServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 13, 20, 4, 1)
)
apSyslogServerEntry.setIndexNames(
    (0, "CTRON-AP3000-MIB", "apSyslogServerIndex"),
)
if mibBuilder.loadTexts:
    apSyslogServerEntry.setStatus("current")


class _ApSyslogServerIndex_Type(Integer32):
    """Custom type apSyslogServerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_ApSyslogServerIndex_Type.__name__ = "Integer32"
_ApSyslogServerIndex_Object = MibTableColumn
apSyslogServerIndex = _ApSyslogServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 13, 20, 4, 1, 1),
    _ApSyslogServerIndex_Type()
)
apSyslogServerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    apSyslogServerIndex.setStatus("current")


class _ApSyslogServerState_Type(Integer32):
    """Custom type apSyslogServerState based on Integer32"""
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


_ApSyslogServerState_Type.__name__ = "Integer32"
_ApSyslogServerState_Object = MibTableColumn
apSyslogServerState = _ApSyslogServerState_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 13, 20, 4, 1, 2),
    _ApSyslogServerState_Type()
)
apSyslogServerState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apSyslogServerState.setStatus("current")


class _ApSyslogServerIPAddress_Type(DisplayString):
    """Custom type apSyslogServerIPAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_ApSyslogServerIPAddress_Type.__name__ = "DisplayString"
_ApSyslogServerIPAddress_Object = MibTableColumn
apSyslogServerIPAddress = _ApSyslogServerIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 13, 20, 4, 1, 3),
    _ApSyslogServerIPAddress_Type()
)
apSyslogServerIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apSyslogServerIPAddress.setStatus("current")


class _ApSyslogServerPort_Type(Integer32):
    """Custom type apSyslogServerPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1024, 65535),
    )


_ApSyslogServerPort_Type.__name__ = "Integer32"
_ApSyslogServerPort_Object = MibTableColumn
apSyslogServerPort = _ApSyslogServerPort_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 13, 20, 4, 1, 4),
    _ApSyslogServerPort_Type()
)
apSyslogServerPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apSyslogServerPort.setStatus("current")
_ApEventLogMgnt_ObjectIdentity = ObjectIdentity
apEventLogMgnt = _ApEventLogMgnt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 13, 21)
)
_ApEventLogTable_Object = MibTable
apEventLogTable = _ApEventLogTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 13, 21, 1)
)
if mibBuilder.loadTexts:
    apEventLogTable.setStatus("current")
_ApEventLogEntry_Object = MibTableRow
apEventLogEntry = _ApEventLogEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 13, 21, 1, 1)
)
apEventLogEntry.setIndexNames(
    (0, "CTRON-AP3000-MIB", "apEventLogIndex"),
)
if mibBuilder.loadTexts:
    apEventLogEntry.setStatus("current")


class _ApEventLogIndex_Type(Integer32):
    """Custom type apEventLogIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_ApEventLogIndex_Type.__name__ = "Integer32"
_ApEventLogIndex_Object = MibTableColumn
apEventLogIndex = _ApEventLogIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 13, 21, 1, 1, 1),
    _ApEventLogIndex_Type()
)
apEventLogIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    apEventLogIndex.setStatus("current")


class _ApEventLogMessage_Type(DisplayString):
    """Custom type apEventLogMessage based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_ApEventLogMessage_Type.__name__ = "DisplayString"
_ApEventLogMessage_Object = MibTableColumn
apEventLogMessage = _ApEventLogMessage_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 13, 21, 1, 1, 2),
    _ApEventLogMessage_Type()
)
apEventLogMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apEventLogMessage.setStatus("current")


class _ApEventLogClear_Type(Integer32):
    """Custom type apEventLogClear based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("clearLog", 1)
    )


_ApEventLogClear_Type.__name__ = "Integer32"
_ApEventLogClear_Object = MibScalar
apEventLogClear = _ApEventLogClear_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 13, 21, 2),
    _ApEventLogClear_Type()
)
apEventLogClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apEventLogClear.setStatus("current")
_ApWSLSupportMgnt_ObjectIdentity = ObjectIdentity
apWSLSupportMgnt = _ApWSLSupportMgnt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 13, 22)
)


class _ApWSLSupportControl_Type(Integer32):
    """Custom type apWSLSupportControl based on Integer32"""
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


_ApWSLSupportControl_Type.__name__ = "Integer32"
_ApWSLSupportControl_Object = MibScalar
apWSLSupportControl = _ApWSLSupportControl_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 13, 22, 1),
    _ApWSLSupportControl_Type()
)
apWSLSupportControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apWSLSupportControl.setStatus("current")


class _ApWSLSupportMasterAddress_Type(DisplayString):
    """Custom type apWSLSupportMasterAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_ApWSLSupportMasterAddress_Type.__name__ = "DisplayString"
_ApWSLSupportMasterAddress_Object = MibScalar
apWSLSupportMasterAddress = _ApWSLSupportMasterAddress_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 13, 22, 2),
    _ApWSLSupportMasterAddress_Type()
)
apWSLSupportMasterAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apWSLSupportMasterAddress.setStatus("current")


class _ApWSLSupportSecondaryAddress_Type(DisplayString):
    """Custom type apWSLSupportSecondaryAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_ApWSLSupportSecondaryAddress_Type.__name__ = "DisplayString"
_ApWSLSupportSecondaryAddress_Object = MibScalar
apWSLSupportSecondaryAddress = _ApWSLSupportSecondaryAddress_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 13, 22, 3),
    _ApWSLSupportSecondaryAddress_Type()
)
apWSLSupportSecondaryAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apWSLSupportSecondaryAddress.setStatus("current")


class _ApWSLSupportPort_Type(Integer32):
    """Custom type apWSLSupportPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1024, 65535),
    )


_ApWSLSupportPort_Type.__name__ = "Integer32"
_ApWSLSupportPort_Object = MibScalar
apWSLSupportPort = _ApWSLSupportPort_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 13, 22, 4),
    _ApWSLSupportPort_Type()
)
apWSLSupportPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apWSLSupportPort.setStatus("current")


class _ApWSLSupportHeartbeatInterval_Type(Integer32):
    """Custom type apWSLSupportHeartbeatInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_ApWSLSupportHeartbeatInterval_Type.__name__ = "Integer32"
_ApWSLSupportHeartbeatInterval_Object = MibScalar
apWSLSupportHeartbeatInterval = _ApWSLSupportHeartbeatInterval_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 13, 22, 5),
    _ApWSLSupportHeartbeatInterval_Type()
)
apWSLSupportHeartbeatInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apWSLSupportHeartbeatInterval.setStatus("current")


class _ApWSLSupportHeartbeatLastChange_Type(DisplayString):
    """Custom type apWSLSupportHeartbeatLastChange based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_ApWSLSupportHeartbeatLastChange_Type.__name__ = "DisplayString"
_ApWSLSupportHeartbeatLastChange_Object = MibScalar
apWSLSupportHeartbeatLastChange = _ApWSLSupportHeartbeatLastChange_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 13, 22, 6),
    _ApWSLSupportHeartbeatLastChange_Type()
)
apWSLSupportHeartbeatLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apWSLSupportHeartbeatLastChange.setStatus("current")


class _ApWSLSupportOperationMode_Type(Integer32):
    """Custom type apWSLSupportOperationMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("associated", 1),
          ("standalone", 0))
    )


_ApWSLSupportOperationMode_Type.__name__ = "Integer32"
_ApWSLSupportOperationMode_Object = MibScalar
apWSLSupportOperationMode = _ApWSLSupportOperationMode_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 13, 22, 7),
    _ApWSLSupportOperationMode_Type()
)
apWSLSupportOperationMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apWSLSupportOperationMode.setStatus("current")


class _ApWSLSupportRxThreshold_Type(Integer32):
    """Custom type apWSLSupportRxThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-128, 127),
    )


_ApWSLSupportRxThreshold_Type.__name__ = "Integer32"
_ApWSLSupportRxThreshold_Object = MibScalar
apWSLSupportRxThreshold = _ApWSLSupportRxThreshold_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 13, 22, 8),
    _ApWSLSupportRxThreshold_Type()
)
apWSLSupportRxThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apWSLSupportRxThreshold.setStatus("current")


class _ApWSLSupportControlStatus_Type(Integer32):
    """Custom type apWSLSupportControlStatus based on Integer32"""
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


_ApWSLSupportControlStatus_Type.__name__ = "Integer32"
_ApWSLSupportControlStatus_Object = MibScalar
apWSLSupportControlStatus = _ApWSLSupportControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 13, 22, 9),
    _ApWSLSupportControlStatus_Type()
)
apWSLSupportControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apWSLSupportControlStatus.setStatus("current")


class _ApWSLRFAreaPollControl_Type(Integer32):
    """Custom type apWSLRFAreaPollControl based on Integer32"""
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


_ApWSLRFAreaPollControl_Type.__name__ = "Integer32"
_ApWSLRFAreaPollControl_Object = MibScalar
apWSLRFAreaPollControl = _ApWSLRFAreaPollControl_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 13, 22, 10),
    _ApWSLRFAreaPollControl_Type()
)
apWSLRFAreaPollControl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apWSLRFAreaPollControl.setStatus("current")


class _ApWSLRFAreaPollControlStatus_Type(Integer32):
    """Custom type apWSLRFAreaPollControlStatus based on Integer32"""
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


_ApWSLRFAreaPollControlStatus_Type.__name__ = "Integer32"
_ApWSLRFAreaPollControlStatus_Object = MibScalar
apWSLRFAreaPollControlStatus = _ApWSLRFAreaPollControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 13, 22, 11),
    _ApWSLRFAreaPollControlStatus_Type()
)
apWSLRFAreaPollControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apWSLRFAreaPollControlStatus.setStatus("current")
_ApWMMMgnt_ObjectIdentity = ObjectIdentity
apWMMMgnt = _ApWMMMgnt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 13, 23)
)
_ApWMMControlTable_Object = MibTable
apWMMControlTable = _ApWMMControlTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 13, 23, 1)
)
if mibBuilder.loadTexts:
    apWMMControlTable.setStatus("current")
_ApWMMControlEntry_Object = MibTableRow
apWMMControlEntry = _ApWMMControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 13, 23, 1, 1)
)
apWMMControlEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    apWMMControlEntry.setStatus("current")


class _ApWMMState_Type(Integer32):
    """Custom type apWMMState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("required", 1),
          ("supported", 2))
    )


_ApWMMState_Type.__name__ = "Integer32"
_ApWMMState_Object = MibTableColumn
apWMMState = _ApWMMState_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 13, 23, 1, 1, 1),
    _ApWMMState_Type()
)
apWMMState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apWMMState.setStatus("current")
_ApWMMBssParamTable_Object = MibTable
apWMMBssParamTable = _ApWMMBssParamTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 13, 23, 2)
)
if mibBuilder.loadTexts:
    apWMMBssParamTable.setStatus("current")
_ApWMMBssParamEntry_Object = MibTableRow
apWMMBssParamEntry = _ApWMMBssParamEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 13, 23, 2, 1)
)
apWMMBssParamEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CTRON-AP3000-MIB", "apWMMBssParamIndex"),
)
if mibBuilder.loadTexts:
    apWMMBssParamEntry.setStatus("current")


class _ApWMMBssParamIndex_Type(Integer32):
    """Custom type apWMMBssParamIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_ApWMMBssParamIndex_Type.__name__ = "Integer32"
_ApWMMBssParamIndex_Object = MibTableColumn
apWMMBssParamIndex = _ApWMMBssParamIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 13, 23, 2, 1, 1),
    _ApWMMBssParamIndex_Type()
)
apWMMBssParamIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    apWMMBssParamIndex.setStatus("current")


class _ApWMMBssParamCWmin_Type(Integer32):
    """Custom type apWMMBssParamCWmin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_ApWMMBssParamCWmin_Type.__name__ = "Integer32"
_ApWMMBssParamCWmin_Object = MibTableColumn
apWMMBssParamCWmin = _ApWMMBssParamCWmin_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 13, 23, 2, 1, 2),
    _ApWMMBssParamCWmin_Type()
)
apWMMBssParamCWmin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apWMMBssParamCWmin.setStatus("current")


class _ApWMMBssParamCWmax_Type(Integer32):
    """Custom type apWMMBssParamCWmax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_ApWMMBssParamCWmax_Type.__name__ = "Integer32"
_ApWMMBssParamCWmax_Object = MibTableColumn
apWMMBssParamCWmax = _ApWMMBssParamCWmax_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 13, 23, 2, 1, 3),
    _ApWMMBssParamCWmax_Type()
)
apWMMBssParamCWmax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apWMMBssParamCWmax.setStatus("current")


class _ApWMMBssParamAIFSN_Type(Integer32):
    """Custom type apWMMBssParamAIFSN based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_ApWMMBssParamAIFSN_Type.__name__ = "Integer32"
_ApWMMBssParamAIFSN_Object = MibTableColumn
apWMMBssParamAIFSN = _ApWMMBssParamAIFSN_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 13, 23, 2, 1, 4),
    _ApWMMBssParamAIFSN_Type()
)
apWMMBssParamAIFSN.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apWMMBssParamAIFSN.setStatus("current")


class _ApWMMBssParamTXOPLimit_Type(Integer32):
    """Custom type apWMMBssParamTXOPLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ApWMMBssParamTXOPLimit_Type.__name__ = "Integer32"
_ApWMMBssParamTXOPLimit_Object = MibTableColumn
apWMMBssParamTXOPLimit = _ApWMMBssParamTXOPLimit_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 13, 23, 2, 1, 5),
    _ApWMMBssParamTXOPLimit_Type()
)
apWMMBssParamTXOPLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apWMMBssParamTXOPLimit.setStatus("current")
_ApWMMBssParamAdmissionControl_Type = TruthValue
_ApWMMBssParamAdmissionControl_Object = MibTableColumn
apWMMBssParamAdmissionControl = _ApWMMBssParamAdmissionControl_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 13, 23, 2, 1, 6),
    _ApWMMBssParamAdmissionControl_Type()
)
apWMMBssParamAdmissionControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apWMMBssParamAdmissionControl.setStatus("current")
_ApWMMApParamTable_Object = MibTable
apWMMApParamTable = _ApWMMApParamTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 13, 23, 3)
)
if mibBuilder.loadTexts:
    apWMMApParamTable.setStatus("current")
_ApWMMApParamEntry_Object = MibTableRow
apWMMApParamEntry = _ApWMMApParamEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 13, 23, 3, 1)
)
apWMMApParamEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CTRON-AP3000-MIB", "apWMMApParamIndex"),
)
if mibBuilder.loadTexts:
    apWMMApParamEntry.setStatus("current")


class _ApWMMApParamIndex_Type(Integer32):
    """Custom type apWMMApParamIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_ApWMMApParamIndex_Type.__name__ = "Integer32"
_ApWMMApParamIndex_Object = MibTableColumn
apWMMApParamIndex = _ApWMMApParamIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 13, 23, 3, 1, 1),
    _ApWMMApParamIndex_Type()
)
apWMMApParamIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    apWMMApParamIndex.setStatus("current")


class _ApWMMApParamCWmin_Type(Integer32):
    """Custom type apWMMApParamCWmin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_ApWMMApParamCWmin_Type.__name__ = "Integer32"
_ApWMMApParamCWmin_Object = MibTableColumn
apWMMApParamCWmin = _ApWMMApParamCWmin_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 13, 23, 3, 1, 2),
    _ApWMMApParamCWmin_Type()
)
apWMMApParamCWmin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apWMMApParamCWmin.setStatus("current")


class _ApWMMApParamCWmax_Type(Integer32):
    """Custom type apWMMApParamCWmax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_ApWMMApParamCWmax_Type.__name__ = "Integer32"
_ApWMMApParamCWmax_Object = MibTableColumn
apWMMApParamCWmax = _ApWMMApParamCWmax_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 13, 23, 3, 1, 3),
    _ApWMMApParamCWmax_Type()
)
apWMMApParamCWmax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apWMMApParamCWmax.setStatus("current")


class _ApWMMApParamAIFSN_Type(Integer32):
    """Custom type apWMMApParamAIFSN based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_ApWMMApParamAIFSN_Type.__name__ = "Integer32"
_ApWMMApParamAIFSN_Object = MibTableColumn
apWMMApParamAIFSN = _ApWMMApParamAIFSN_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 13, 23, 3, 1, 4),
    _ApWMMApParamAIFSN_Type()
)
apWMMApParamAIFSN.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apWMMApParamAIFSN.setStatus("current")


class _ApWMMApParamTXOPLimit_Type(Integer32):
    """Custom type apWMMApParamTXOPLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ApWMMApParamTXOPLimit_Type.__name__ = "Integer32"
_ApWMMApParamTXOPLimit_Object = MibTableColumn
apWMMApParamTXOPLimit = _ApWMMApParamTXOPLimit_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 13, 23, 3, 1, 5),
    _ApWMMApParamTXOPLimit_Type()
)
apWMMApParamTXOPLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apWMMApParamTXOPLimit.setStatus("current")
_ApWMMApParamAdmissionControl_Type = TruthValue
_ApWMMApParamAdmissionControl_Object = MibTableColumn
apWMMApParamAdmissionControl = _ApWMMApParamAdmissionControl_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 13, 23, 3, 1, 6),
    _ApWMMApParamAdmissionControl_Type()
)
apWMMApParamAdmissionControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apWMMApParamAdmissionControl.setStatus("current")
_ApNotificationTrapTree_ObjectIdentity = ObjectIdentity
apNotificationTrapTree = _ApNotificationTrapTree_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 13, 100)
)
_ApNotificationObjects_ObjectIdentity = ObjectIdentity
apNotificationObjects = _ApNotificationObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 13, 100, 1)
)
_ApNotificationDot11MacAddr_Type = MacAddress
_ApNotificationDot11MacAddr_Object = MibScalar
apNotificationDot11MacAddr = _ApNotificationDot11MacAddr_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 13, 100, 1, 1),
    _ApNotificationDot11MacAddr_Type()
)
apNotificationDot11MacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apNotificationDot11MacAddr.setStatus("current")
_ApNotificationDot11Station_Type = MacAddress
_ApNotificationDot11Station_Object = MibScalar
apNotificationDot11Station = _ApNotificationDot11Station_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 13, 100, 1, 2),
    _ApNotificationDot11Station_Type()
)
apNotificationDot11Station.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apNotificationDot11Station.setStatus("current")


class _ApNotificationDot11RequestType_Type(Integer32):
    """Custom type apNotificationDot11RequestType based on Integer32"""
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
        *(("association", 2),
          ("authentication", 4),
          ("reAssociation", 3),
          ("unknown", 1))
    )


_ApNotificationDot11RequestType_Type.__name__ = "Integer32"
_ApNotificationDot11RequestType_Object = MibScalar
apNotificationDot11RequestType = _ApNotificationDot11RequestType_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 13, 100, 1, 3),
    _ApNotificationDot11RequestType_Type()
)
apNotificationDot11RequestType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apNotificationDot11RequestType.setStatus("current")


class _ApNotificationDot11ReasonCode_Type(Integer32):
    """Custom type apNotificationDot11ReasonCode based on Integer32"""
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
        *(("challengeTextMismatch", 9),
          ("internalError", 3),
          ("invalidFrameLngth", 6),
          ("invalidModeOrState", 1),
          ("outOfSequenceFrame", 4),
          ("unAuthenticatedStation", 2),
          ("unsupportedAlgorithm", 5),
          ("wepNotAllowed", 8),
          ("wepRequiredOnAP", 7))
    )


_ApNotificationDot11ReasonCode_Type.__name__ = "Integer32"
_ApNotificationDot11ReasonCode_Object = MibScalar
apNotificationDot11ReasonCode = _ApNotificationDot11ReasonCode_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 13, 100, 1, 4),
    _ApNotificationDot11ReasonCode_Type()
)
apNotificationDot11ReasonCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apNotificationDot11ReasonCode.setStatus("current")
_ApNotificationDot11IpAddress_Type = IpAddress
_ApNotificationDot11IpAddress_Object = MibScalar
apNotificationDot11IpAddress = _ApNotificationDot11IpAddress_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 13, 100, 1, 5),
    _ApNotificationDot11IpAddress_Type()
)
apNotificationDot11IpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apNotificationDot11IpAddress.setStatus("current")
_ApNotificationDot11AuthenticatorMacAddr_Type = MacAddress
_ApNotificationDot11AuthenticatorMacAddr_Object = MibScalar
apNotificationDot11AuthenticatorMacAddr = _ApNotificationDot11AuthenticatorMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 13, 100, 1, 6),
    _ApNotificationDot11AuthenticatorMacAddr_Type()
)
apNotificationDot11AuthenticatorMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apNotificationDot11AuthenticatorMacAddr.setStatus("current")
_ApNotificationTrapObjects_ObjectIdentity = ObjectIdentity
apNotificationTrapObjects = _ApNotificationTrapObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 13, 100, 2)
)

# Managed Objects groups


# Notification objects

sysSystemUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 52, 4, 13, 100, 2, 1)
)
if mibBuilder.loadTexts:
    sysSystemUp.setStatus(
        "current"
    )

sysSystemDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 52, 4, 13, 100, 2, 2)
)
if mibBuilder.loadTexts:
    sysSystemDown.setStatus(
        "current"
    )

sysRadiusServerChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 52, 4, 13, 100, 2, 3)
)
if mibBuilder.loadTexts:
    sysRadiusServerChanged.setStatus(
        "current"
    )

dot11StationAssociation = NotificationType(
    (1, 3, 6, 1, 4, 1, 52, 4, 13, 100, 2, 4)
)
dot11StationAssociation.setObjects(
    ("CTRON-AP3000-MIB", "apNotificationDot11Station")
)
if mibBuilder.loadTexts:
    dot11StationAssociation.setStatus(
        "current"
    )

dot11StationReAssociation = NotificationType(
    (1, 3, 6, 1, 4, 1, 52, 4, 13, 100, 2, 5)
)
dot11StationReAssociation.setObjects(
    ("CTRON-AP3000-MIB", "apNotificationDot11Station")
)
if mibBuilder.loadTexts:
    dot11StationReAssociation.setStatus(
        "current"
    )

dot11StationAuthentication = NotificationType(
    (1, 3, 6, 1, 4, 1, 52, 4, 13, 100, 2, 6)
)
dot11StationAuthentication.setObjects(
    ("CTRON-AP3000-MIB", "apNotificationDot11Station")
)
if mibBuilder.loadTexts:
    dot11StationAuthentication.setStatus(
        "current"
    )

dot11StationRequestFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 52, 4, 13, 100, 2, 7)
)
dot11StationRequestFail.setObjects(
      *(("CTRON-AP3000-MIB", "apNotificationDot11Station"),
        ("CTRON-AP3000-MIB", "apNotificationDot11RequestType"),
        ("CTRON-AP3000-MIB", "apNotificationDot11ReasonCode"))
)
if mibBuilder.loadTexts:
    dot11StationRequestFail.setStatus(
        "current"
    )

dot1xMacAddrAuthSuccess = NotificationType(
    (1, 3, 6, 1, 4, 1, 52, 4, 13, 100, 2, 9)
)
dot1xMacAddrAuthSuccess.setObjects(
    ("CTRON-AP3000-MIB", "apNotificationDot11Station")
)
if mibBuilder.loadTexts:
    dot1xMacAddrAuthSuccess.setStatus(
        "current"
    )

dot1xMacAddrAuthFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 52, 4, 13, 100, 2, 10)
)
dot1xMacAddrAuthFail.setObjects(
    ("CTRON-AP3000-MIB", "apNotificationDot11Station")
)
if mibBuilder.loadTexts:
    dot1xMacAddrAuthFail.setStatus(
        "current"
    )

dot1xAuthNotInitiated = NotificationType(
    (1, 3, 6, 1, 4, 1, 52, 4, 13, 100, 2, 11)
)
dot1xAuthNotInitiated.setObjects(
    ("CTRON-AP3000-MIB", "apNotificationDot11Station")
)
if mibBuilder.loadTexts:
    dot1xAuthNotInitiated.setStatus(
        "current"
    )

dot1xAuthSuccess = NotificationType(
    (1, 3, 6, 1, 4, 1, 52, 4, 13, 100, 2, 12)
)
dot1xAuthSuccess.setObjects(
    ("CTRON-AP3000-MIB", "apNotificationDot11Station")
)
if mibBuilder.loadTexts:
    dot1xAuthSuccess.setStatus(
        "current"
    )

dot1xAuthFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 52, 4, 13, 100, 2, 13)
)
dot1xAuthFail.setObjects(
    ("CTRON-AP3000-MIB", "apNotificationDot11Station")
)
if mibBuilder.loadTexts:
    dot1xAuthFail.setStatus(
        "current"
    )

localMacAddrAuthSuccess = NotificationType(
    (1, 3, 6, 1, 4, 1, 52, 4, 13, 100, 2, 14)
)
localMacAddrAuthSuccess.setObjects(
    ("CTRON-AP3000-MIB", "apNotificationDot11Station")
)
if mibBuilder.loadTexts:
    localMacAddrAuthSuccess.setStatus(
        "current"
    )

localMacAddrAuthFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 52, 4, 13, 100, 2, 15)
)
localMacAddrAuthFail.setObjects(
    ("CTRON-AP3000-MIB", "apNotificationDot11Station")
)
if mibBuilder.loadTexts:
    localMacAddrAuthFail.setStatus(
        "current"
    )

pppLogonFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 52, 4, 13, 100, 2, 16)
)
if mibBuilder.loadTexts:
    pppLogonFail.setStatus(
        "current"
    )

iappStationRoamedFrom = NotificationType(
    (1, 3, 6, 1, 4, 1, 52, 4, 13, 100, 2, 17)
)
iappStationRoamedFrom.setObjects(
      *(("CTRON-AP3000-MIB", "apNotificationDot11Station"),
        ("CTRON-AP3000-MIB", "apNotificationDot11IpAddress"))
)
if mibBuilder.loadTexts:
    iappStationRoamedFrom.setStatus(
        "current"
    )

iappStationRoamedTo = NotificationType(
    (1, 3, 6, 1, 4, 1, 52, 4, 13, 100, 2, 18)
)
iappStationRoamedTo.setObjects(
      *(("CTRON-AP3000-MIB", "apNotificationDot11Station"),
        ("CTRON-AP3000-MIB", "apNotificationDot11IpAddress"))
)
if mibBuilder.loadTexts:
    iappStationRoamedTo.setStatus(
        "current"
    )

iappContextDataSent = NotificationType(
    (1, 3, 6, 1, 4, 1, 52, 4, 13, 100, 2, 19)
)
iappContextDataSent.setObjects(
      *(("CTRON-AP3000-MIB", "apNotificationDot11Station"),
        ("CTRON-AP3000-MIB", "apNotificationDot11IpAddress"))
)
if mibBuilder.loadTexts:
    iappContextDataSent.setStatus(
        "current"
    )

sntpServerFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 52, 4, 13, 100, 2, 20)
)
if mibBuilder.loadTexts:
    sntpServerFail.setStatus(
        "current"
    )

dot11InterfaceAFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 52, 4, 13, 100, 2, 21)
)
if mibBuilder.loadTexts:
    dot11InterfaceAFail.setStatus(
        "current"
    )

dot11InterfaceGFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 52, 4, 13, 100, 2, 22)
)
if mibBuilder.loadTexts:
    dot11InterfaceGFail.setStatus(
        "current"
    )

dot11WirelessSTPDetection = NotificationType(
    (1, 3, 6, 1, 4, 1, 52, 4, 13, 100, 2, 23)
)
if mibBuilder.loadTexts:
    dot11WirelessSTPDetection.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CTRON-AP3000-MIB",
    **{"MacAddress": MacAddress,
       "DisplayString": DisplayString,
       "TruthValue": TruthValue,
       "cabletron": cabletron,
       "mibs": mibs,
       "ctronAP3000": ctronAP3000,
       "comPortMgnt": comPortMgnt,
       "comPortControl": comPortControl,
       "macFilterMgnt": macFilterMgnt,
       "macFilterTable": macFilterTable,
       "macFilterEntry": macFilterEntry,
       "macFilterIndex": macFilterIndex,
       "macFilterAddress": macFilterAddress,
       "macFilterAllowedToGo": macFilterAllowedToGo,
       "macFilterOpeStatus": macFilterOpeStatus,
       "apMacFilterControl": apMacFilterControl,
       "apvMacFilterOperateTable": apvMacFilterOperateTable,
       "apvMacFilterOperateEntry": apvMacFilterOperateEntry,
       "apvMacFilterPermission": apvMacFilterPermission,
       "apvMacFilterAddressToAdd": apvMacFilterAddressToAdd,
       "apvMacFilterTable": apvMacFilterTable,
       "apvMacFilterEntry": apvMacFilterEntry,
       "apvMacFilterIndex": apvMacFilterIndex,
       "apvMacFilterAddress": apvMacFilterAddress,
       "apvMacFilterActivity": apvMacFilterActivity,
       "qosMgnt": qosMgnt,
       "qosModeControl": qosModeControl,
       "qosMACTypeTable": qosMACTypeTable,
       "qosMACTypeEntry": qosMACTypeEntry,
       "qosMACTypeIndex": qosMACTypeIndex,
       "qosMACTypeAddress": qosMACTypeAddress,
       "qosMACTypePriority": qosMACTypePriority,
       "qosMACTypeOpeStatus": qosMACTypeOpeStatus,
       "qosEtherTypeTable": qosEtherTypeTable,
       "qosEtherTypeEntry": qosEtherTypeEntry,
       "qosEtherTypeIndex": qosEtherTypeIndex,
       "qosEtherTypeHexValue": qosEtherTypeHexValue,
       "qosEtherTypePriority": qosEtherTypePriority,
       "qosEtherTypeOpeStatus": qosEtherTypeOpeStatus,
       "qosQueueingMode": qosQueueingMode,
       "qosSVPStatus": qosSVPStatus,
       "linkQualityMgnt": linkQualityMgnt,
       "linkQualityTable": linkQualityTable,
       "linkQualityEntry": linkQualityEntry,
       "linkQualityRadioIndex": linkQualityRadioIndex,
       "linkQualityStaIndex": linkQualityStaIndex,
       "linkQualityStaMacAddress": linkQualityStaMacAddress,
       "linkQualityStaRssi": linkQualityStaRssi,
       "apSnmpMgnt": apSnmpMgnt,
       "trapControl": trapControl,
       "trapConfiguration": trapConfiguration,
       "trapSysSystemUp": trapSysSystemUp,
       "trapSysSystemDown": trapSysSystemDown,
       "trapSysRadiusServerChanged": trapSysRadiusServerChanged,
       "trapDot11StationAssociation": trapDot11StationAssociation,
       "trapDot11StationReAssociation": trapDot11StationReAssociation,
       "trapDot11StationAuthentication": trapDot11StationAuthentication,
       "trapDot11StationRequestFail": trapDot11StationRequestFail,
       "trapLocalMacAddrAuthFail": trapLocalMacAddrAuthFail,
       "trapLocalMacAddrAuthSuccess": trapLocalMacAddrAuthSuccess,
       "trapDot1xAuthNotInitiated": trapDot1xAuthNotInitiated,
       "trapDot1xAuthSuccess": trapDot1xAuthSuccess,
       "trapDot1xAuthFail": trapDot1xAuthFail,
       "trapDot1xMacAddrAuthSuccess": trapDot1xMacAddrAuthSuccess,
       "trapDot1xMacAddrAuthFail": trapDot1xMacAddrAuthFail,
       "trapPppLogonFail": trapPppLogonFail,
       "trapIappStationRoamedFrom": trapIappStationRoamedFrom,
       "trapIappStationRoamedTo": trapIappStationRoamedTo,
       "trapIappContextDataSent": trapIappContextDataSent,
       "trapSntpServerFail": trapSntpServerFail,
       "trapDot11InterfaceAFail": trapDot11InterfaceAFail,
       "trapDot11InterfaceGFail": trapDot11InterfaceGFail,
       "trapDot11WirelessSTPDetection": trapDot11WirelessSTPDetection,
       "apSnmpTrapDestinationTable": apSnmpTrapDestinationTable,
       "apSnmpTrapDestinationEntry": apSnmpTrapDestinationEntry,
       "apSnmpTrapDestinationIndex": apSnmpTrapDestinationIndex,
       "apSnmpTrapDestinationCommunity": apSnmpTrapDestinationCommunity,
       "apSnmpTrapDestinationIP": apSnmpTrapDestinationIP,
       "apSnmpTrapDestinationState": apSnmpTrapDestinationState,
       "apSnmpCommunityReadOnly": apSnmpCommunityReadOnly,
       "apSnmpCommunityReadWrite": apSnmpCommunityReadWrite,
       "apSnmpVersionFilter": apSnmpVersionFilter,
       "sysEntity": sysEntity,
       "swHardwareVer": swHardwareVer,
       "swBootRomVer": swBootRomVer,
       "swOpCodeVer": swOpCodeVer,
       "swSerialNumber": swSerialNumber,
       "swProductName": swProductName,
       "swCountrySetting": swCountrySetting,
       "apSecurityMgnt": apSecurityMgnt,
       "apRadioSecurityTable": apRadioSecurityTable,
       "apRadioSecurityEntry": apRadioSecurityEntry,
       "apRadioSecurityIndex": apRadioSecurityIndex,
       "apRadioSecurityWEPAuthType": apRadioSecurityWEPAuthType,
       "apRadioSecuritySharedKeyLen": apRadioSecuritySharedKeyLen,
       "apRadioSecurityWPAMode": apRadioSecurityWPAMode,
       "apRadioSecurityWPAKeyType": apRadioSecurityWPAKeyType,
       "apRadioSecurityWPACipher": apRadioSecurityWPACipher,
       "apRadioSecurityWPAPSKType": apRadioSecurityWPAPSKType,
       "apRadioSecurityWPAPSK": apRadioSecurityWPAPSK,
       "apRadioSecurityWEPKeyType": apRadioSecurityWEPKeyType,
       "apRadioSecurityWEPEnabled": apRadioSecurityWEPEnabled,
       "apRadioSecurityWPACipherSuite": apRadioSecurityWPACipherSuite,
       "apRadioApSecurityWPAPreAuthentication": apRadioApSecurityWPAPreAuthentication,
       "apRadioApSecurityWPAPmksaLifetime": apRadioApSecurityWPAPmksaLifetime,
       "apSecuritySsh": apSecuritySsh,
       "apSecuritySshServerEnabled": apSecuritySshServerEnabled,
       "apSecuritySshServerPort": apSecuritySshServerPort,
       "apSecuritySshTelnetServerEnabled": apSecuritySshTelnetServerEnabled,
       "apRadioInterfaceMgnt": apRadioInterfaceMgnt,
       "enterpriseApRadioTable": enterpriseApRadioTable,
       "enterpriseApRadioEntry": enterpriseApRadioEntry,
       "enterpriseApRadioIndex": enterpriseApRadioIndex,
       "enterpriseApRadioAutoChannel": enterpriseApRadioAutoChannel,
       "enterpriseApRadioTransmitPower": enterpriseApRadioTransmitPower,
       "enterpriseApRadioTurboMode": enterpriseApRadioTurboMode,
       "enterpriseApRadioDataRate": enterpriseApRadioDataRate,
       "enterpriseApRadioGMode": enterpriseApRadioGMode,
       "enterpriseApRadioAntennaMode": enterpriseApRadioAntennaMode,
       "rogueApState": rogueApState,
       "rogueApInterval": rogueApInterval,
       "rogueApDuration": rogueApDuration,
       "rogueApScanNow": rogueApScanNow,
       "enterpriseApRadioAntennaModeControl": enterpriseApRadioAntennaModeControl,
       "enterpriseApRadioFixedAntennaType": enterpriseApRadioFixedAntennaType,
       "enterpriseApRadioAntennaID": enterpriseApRadioAntennaID,
       "enterpriseApRadioMulticastDataRate": enterpriseApRadioMulticastDataRate,
       "enterpriseApRadioAutoDataRate": enterpriseApRadioAutoDataRate,
       "enterpriseApRadioPreamble": enterpriseApRadioPreamble,
       "enterpriseApRadioSWRetryMode": enterpriseApRadioSWRetryMode,
       "enterpriseApVapRadioTable": enterpriseApVapRadioTable,
       "enterpriseApVapRadioEntry": enterpriseApVapRadioEntry,
       "enterpriseApVapRadioIndex": enterpriseApVapRadioIndex,
       "enterpriseApVapRadioState": enterpriseApVapRadioState,
       "enterpriseApVapRadioSecureAccess": enterpriseApVapRadioSecureAccess,
       "enterpriseApVapRadioMaxAssoc": enterpriseApVapRadioMaxAssoc,
       "enterpriseApVapRadioTransmitKey": enterpriseApVapRadioTransmitKey,
       "enterpriseApVapRadioDescription": enterpriseApVapRadioDescription,
       "enterpriseApVapRadioDefefaultPriority": enterpriseApVapRadioDefefaultPriority,
       "enterpriseApRadioWdsTable": enterpriseApRadioWdsTable,
       "enterpriseApRadioWdsEntry": enterpriseApRadioWdsEntry,
       "wdsApRole": wdsApRole,
       "wdsApAckTimeout": wdsApAckTimeout,
       "enterpriseApRadioWdsPeerTable": enterpriseApRadioWdsPeerTable,
       "enterpriseApRadioWdsPeerEntry": enterpriseApRadioWdsPeerEntry,
       "wdsPeerIndex": wdsPeerIndex,
       "wdsPeerBssid": wdsPeerBssid,
       "wdsPeerRSSI": wdsPeerRSSI,
       "enterpriseApRadioWEPKeysTable": enterpriseApRadioWEPKeysTable,
       "enterpriseApRadioWEPKeysEntry": enterpriseApRadioWEPKeysEntry,
       "enterpriseApRadioWEPKeysIndex": enterpriseApRadioWEPKeysIndex,
       "enterpriseApRadioWEPKeyType": enterpriseApRadioWEPKeyType,
       "enterpriseApRadioWEPKeyLength": enterpriseApRadioWEPKeyLength,
       "enterpriseApRadioAvAntennaListTable": enterpriseApRadioAvAntennaListTable,
       "enterpriseApRadioAvAntennaListEntry": enterpriseApRadioAvAntennaListEntry,
       "enterpriseApRadioAvAntennaIndex": enterpriseApRadioAvAntennaIndex,
       "enterpriseApRadioAvAntennaId": enterpriseApRadioAvAntennaId,
       "enterpriseApRadioAvAntennaDesc": enterpriseApRadioAvAntennaDesc,
       "enterpriseApRadioAvChannelListTable": enterpriseApRadioAvChannelListTable,
       "enterpriseApRadioAvChannelListEntry": enterpriseApRadioAvChannelListEntry,
       "enterpriseApRadioAvChannelIndex": enterpriseApRadioAvChannelIndex,
       "enterpriseApRadioAvChannelNo": enterpriseApRadioAvChannelNo,
       "apEtherInterfaceMgnt": apEtherInterfaceMgnt,
       "apEtherNetConfig": apEtherNetConfig,
       "netConfigIPAddress": netConfigIPAddress,
       "netConfigSubnetMask": netConfigSubnetMask,
       "netConfigDefaultGateway": netConfigDefaultGateway,
       "netConfigHttpState": netConfigHttpState,
       "netConfigHttpPort": netConfigHttpPort,
       "netConfigHttpsState": netConfigHttpsState,
       "netConfigHttpsPort": netConfigHttpsPort,
       "netConfigDHCPState": netConfigDHCPState,
       "apFilterControlMgnt": apFilterControlMgnt,
       "apFilterControlBridge": apFilterControlBridge,
       "enterpriseApFilterControlAPManage": enterpriseApFilterControlAPManage,
       "enterpriseApFilterControlEthernet": enterpriseApFilterControlEthernet,
       "enterpriseApFilterProtocolTable": enterpriseApFilterProtocolTable,
       "enterpriseApFilterProtocolEntry": enterpriseApFilterProtocolEntry,
       "enterpriseApFilterProtocolIndex": enterpriseApFilterProtocolIndex,
       "enterpriseApFilterProtocolName": enterpriseApFilterProtocolName,
       "enterpriseApFilterProtocolISODesignator": enterpriseApFilterProtocolISODesignator,
       "enterpriseApFilterProtocolState": enterpriseApFilterProtocolState,
       "apvGlobalIBSSRelayMode": apvGlobalIBSSRelayMode,
       "apvFilterControlTable": apvFilterControlTable,
       "apvFilterControlEntry": apvFilterControlEntry,
       "apvFilterControlIndex": apvFilterControlIndex,
       "apvIBSSFilterControl": apvIBSSFilterControl,
       "apvAPManageFilterControl": apvAPManageFilterControl,
       "apVLANMgnt": apVLANMgnt,
       "apVLANMgntNativeId": apVLANMgntNativeId,
       "apVLANMgntState": apVLANMgntState,
       "apVLANMgntStateNextBoot": apVLANMgntStateNextBoot,
       "apNativeVlanTable": apNativeVlanTable,
       "apNativeVlanEntry": apNativeVlanEntry,
       "apNativeVlanIfIndex": apNativeVlanIfIndex,
       "apNativeVlanSsidNumber": apNativeVlanSsidNumber,
       "apNativeVlanVlanId": apNativeVlanVlanId,
       "apNativeVlanState": apNativeVlanState,
       "apVLANMgntEtherUntaggedVlanId": apVLANMgntEtherUntaggedVlanId,
       "apAuthenticationMgnt": apAuthenticationMgnt,
       "apAuthenticationSetupEntry": apAuthenticationSetupEntry,
       "ap8021xState": ap8021xState,
       "ap8021xBroadcastKeyRefreshRate": ap8021xBroadcastKeyRefreshRate,
       "ap8021xSessionKeyRefreshRate": ap8021xSessionKeyRefreshRate,
       "ap8021xReauthenticationTimeout": ap8021xReauthenticationTimeout,
       "apAuthenticationMode": apAuthenticationMode,
       "apAuthenticationServerTable": apAuthenticationServerTable,
       "apAuthenticationServerEntry": apAuthenticationServerEntry,
       "apAuthenticationServerIndex": apAuthenticationServerIndex,
       "apAuthenticationServer": apAuthenticationServer,
       "apAuthenticationPort": apAuthenticationPort,
       "apAuthenticationKey": apAuthenticationKey,
       "apAuthenticationRetransmit": apAuthenticationRetransmit,
       "apAuthenticationTimeout": apAuthenticationTimeout,
       "apAuthenticationAcctPort": apAuthenticationAcctPort,
       "apAuthenticationAcctInterimUpdate": apAuthenticationAcctInterimUpdate,
       "apAuthenticationAcctState": apAuthenticationAcctState,
       "apAuthenticationSupplicantTable": apAuthenticationSupplicantTable,
       "apAuthenticationSupplicantEntry": apAuthenticationSupplicantEntry,
       "ap8021xSuppIndex": ap8021xSuppIndex,
       "ap8021xSuppState": ap8021xSuppState,
       "ap8021xSuppUser": ap8021xSuppUser,
       "ap8021xSuppPasswd": ap8021xSuppPasswd,
       "apvAuthenticationSetupTable": apvAuthenticationSetupTable,
       "apvAuthenticationSetupEntry": apvAuthenticationSetupEntry,
       "apv8021xIndex": apv8021xIndex,
       "apv8021xState": apv8021xState,
       "apv8021xBroadcastKeyRefreshRate": apv8021xBroadcastKeyRefreshRate,
       "apv8021xSessionKeyRefreshRate": apv8021xSessionKeyRefreshRate,
       "apv8021xReauthenticationTimeout": apv8021xReauthenticationTimeout,
       "apvMACAuthenticationMode": apvMACAuthenticationMode,
       "apvMACAuthenticationTimeout": apvMACAuthenticationTimeout,
       "apvMACAuthenticationPasswd": apvMACAuthenticationPasswd,
       "apWStationSessionMgnt": apWStationSessionMgnt,
       "apWStationSessionTable": apWStationSessionTable,
       "apWStationSessionEntry": apWStationSessionEntry,
       "apWStationSessionIfIndex": apWStationSessionIfIndex,
       "apWStationSessionStationAddres": apWStationSessionStationAddres,
       "apWStationSessionAuthenticated": apWStationSessionAuthenticated,
       "apWStationSessionAssociated": apWStationSessionAssociated,
       "apWStationSessionIsForwarding": apWStationSessionIsForwarding,
       "apWStationSessionKeyType": apWStationSessionKeyType,
       "apWStationSessionAssociationId": apWStationSessionAssociationId,
       "apWStationSessionLastAuthenticatedTime": apWStationSessionLastAuthenticatedTime,
       "apWStationSessionAssociatedTime": apWStationSessionAssociatedTime,
       "apWStationSessionLastAssociatedTime": apWStationSessionLastAssociatedTime,
       "apWStationSessionLastDisassociatedTime": apWStationSessionLastDisassociatedTime,
       "apWStationSessionTxPacketCount": apWStationSessionTxPacketCount,
       "apWStationSessionRxPacketCount": apWStationSessionRxPacketCount,
       "apWStationSessionTxByteCount": apWStationSessionTxByteCount,
       "apWStationSessionRxByteCount": apWStationSessionRxByteCount,
       "apWStationSessionVlanID": apWStationSessionVlanID,
       "apRogueApMgnt": apRogueApMgnt,
       "rogueApDetectionTable": rogueApDetectionTable,
       "rogueApDetectionEntry": rogueApDetectionEntry,
       "rogueApIndex": rogueApIndex,
       "rogueApBssid": rogueApBssid,
       "rogueApSsid": rogueApSsid,
       "rogueApPortNumber": rogueApPortNumber,
       "rogueApChannelNumber": rogueApChannelNumber,
       "rogueApRSSIValue": rogueApRSSIValue,
       "apRougeApControl": apRougeApControl,
       "rogueApRADIUSAuthenticate": rogueApRADIUSAuthenticate,
       "rogueApClear": rogueApClear,
       "apAdminMgnt": apAdminMgnt,
       "apAdminUsername": apAdminUsername,
       "appAdminPassword": appAdminPassword,
       "apResetMgt": apResetMgt,
       "apRestartOpCodeFile": apRestartOpCodeFile,
       "apRestartControl": apRestartControl,
       "apSNTPMgnt": apSNTPMgnt,
       "apSNTPState": apSNTPState,
       "apSNTPPrimaryServer": apSNTPPrimaryServer,
       "apSNTPSecondaryServer": apSNTPSecondaryServer,
       "apSNTPTimezone": apSNTPTimezone,
       "apSNTPDST": apSNTPDST,
       "apSNTPDSTStartMonth": apSNTPDSTStartMonth,
       "apSNTPDSTStartDay": apSNTPDSTStartDay,
       "apSNTPDSTEndMonth": apSNTPDSTEndMonth,
       "apSNTPDSTEndDay": apSNTPDSTEndDay,
       "apDNSMgnt": apDNSMgnt,
       "apDNSPrimaryServer": apDNSPrimaryServer,
       "apDNSSecondaryServer": apDNSSecondaryServer,
       "apIappMgnt": apIappMgnt,
       "apIappEnabled": apIappEnabled,
       "apSyslogConfigMgnt": apSyslogConfigMgnt,
       "apLogConfigState": apLogConfigState,
       "apSyslogConsoleState": apSyslogConsoleState,
       "apSyslogLevel": apSyslogLevel,
       "apSyslogServerTable": apSyslogServerTable,
       "apSyslogServerEntry": apSyslogServerEntry,
       "apSyslogServerIndex": apSyslogServerIndex,
       "apSyslogServerState": apSyslogServerState,
       "apSyslogServerIPAddress": apSyslogServerIPAddress,
       "apSyslogServerPort": apSyslogServerPort,
       "apEventLogMgnt": apEventLogMgnt,
       "apEventLogTable": apEventLogTable,
       "apEventLogEntry": apEventLogEntry,
       "apEventLogIndex": apEventLogIndex,
       "apEventLogMessage": apEventLogMessage,
       "apEventLogClear": apEventLogClear,
       "apWSLSupportMgnt": apWSLSupportMgnt,
       "apWSLSupportControl": apWSLSupportControl,
       "apWSLSupportMasterAddress": apWSLSupportMasterAddress,
       "apWSLSupportSecondaryAddress": apWSLSupportSecondaryAddress,
       "apWSLSupportPort": apWSLSupportPort,
       "apWSLSupportHeartbeatInterval": apWSLSupportHeartbeatInterval,
       "apWSLSupportHeartbeatLastChange": apWSLSupportHeartbeatLastChange,
       "apWSLSupportOperationMode": apWSLSupportOperationMode,
       "apWSLSupportRxThreshold": apWSLSupportRxThreshold,
       "apWSLSupportControlStatus": apWSLSupportControlStatus,
       "apWSLRFAreaPollControl": apWSLRFAreaPollControl,
       "apWSLRFAreaPollControlStatus": apWSLRFAreaPollControlStatus,
       "apWMMMgnt": apWMMMgnt,
       "apWMMControlTable": apWMMControlTable,
       "apWMMControlEntry": apWMMControlEntry,
       "apWMMState": apWMMState,
       "apWMMBssParamTable": apWMMBssParamTable,
       "apWMMBssParamEntry": apWMMBssParamEntry,
       "apWMMBssParamIndex": apWMMBssParamIndex,
       "apWMMBssParamCWmin": apWMMBssParamCWmin,
       "apWMMBssParamCWmax": apWMMBssParamCWmax,
       "apWMMBssParamAIFSN": apWMMBssParamAIFSN,
       "apWMMBssParamTXOPLimit": apWMMBssParamTXOPLimit,
       "apWMMBssParamAdmissionControl": apWMMBssParamAdmissionControl,
       "apWMMApParamTable": apWMMApParamTable,
       "apWMMApParamEntry": apWMMApParamEntry,
       "apWMMApParamIndex": apWMMApParamIndex,
       "apWMMApParamCWmin": apWMMApParamCWmin,
       "apWMMApParamCWmax": apWMMApParamCWmax,
       "apWMMApParamAIFSN": apWMMApParamAIFSN,
       "apWMMApParamTXOPLimit": apWMMApParamTXOPLimit,
       "apWMMApParamAdmissionControl": apWMMApParamAdmissionControl,
       "apNotificationTrapTree": apNotificationTrapTree,
       "apNotificationObjects": apNotificationObjects,
       "apNotificationDot11MacAddr": apNotificationDot11MacAddr,
       "apNotificationDot11Station": apNotificationDot11Station,
       "apNotificationDot11RequestType": apNotificationDot11RequestType,
       "apNotificationDot11ReasonCode": apNotificationDot11ReasonCode,
       "apNotificationDot11IpAddress": apNotificationDot11IpAddress,
       "apNotificationDot11AuthenticatorMacAddr": apNotificationDot11AuthenticatorMacAddr,
       "apNotificationTrapObjects": apNotificationTrapObjects,
       "sysSystemUp": sysSystemUp,
       "sysSystemDown": sysSystemDown,
       "sysRadiusServerChanged": sysRadiusServerChanged,
       "dot11StationAssociation": dot11StationAssociation,
       "dot11StationReAssociation": dot11StationReAssociation,
       "dot11StationAuthentication": dot11StationAuthentication,
       "dot11StationRequestFail": dot11StationRequestFail,
       "dot1xMacAddrAuthSuccess": dot1xMacAddrAuthSuccess,
       "dot1xMacAddrAuthFail": dot1xMacAddrAuthFail,
       "dot1xAuthNotInitiated": dot1xAuthNotInitiated,
       "dot1xAuthSuccess": dot1xAuthSuccess,
       "dot1xAuthFail": dot1xAuthFail,
       "localMacAddrAuthSuccess": localMacAddrAuthSuccess,
       "localMacAddrAuthFail": localMacAddrAuthFail,
       "pppLogonFail": pppLogonFail,
       "iappStationRoamedFrom": iappStationRoamedFrom,
       "iappStationRoamedTo": iappStationRoamedTo,
       "iappContextDataSent": iappContextDataSent,
       "sntpServerFail": sntpServerFail,
       "dot11InterfaceAFail": dot11InterfaceAFail,
       "dot11InterfaceGFail": dot11InterfaceGFail,
       "dot11WirelessSTPDetection": dot11WirelessSTPDetection}
)
