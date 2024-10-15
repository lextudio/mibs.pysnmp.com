# SNMP MIB module (NBS-EUSM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/NBS-EUSM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:24:47 2024
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

(nbs,
 nbsCmmcPortEntry,
 nbsCmmcSlotEntry) = mibBuilder.importSymbols(
    "NBS-CMMC-MIB",
    "nbs",
    "nbsCmmcPortEntry",
    "nbsCmmcSlotEntry")

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
 RowStatus,
 StorageType,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "StorageType",
    "TextualConvention")


# MODULE-IDENTITY

nbsEusmMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 629, 202)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_NbsEusmSlotGrp_ObjectIdentity = ObjectIdentity
nbsEusmSlotGrp = _NbsEusmSlotGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 202, 1)
)
if mibBuilder.loadTexts:
    nbsEusmSlotGrp.setStatus("current")
_NbsEusmSlotTable_Object = MibTable
nbsEusmSlotTable = _NbsEusmSlotTable_Object(
    (1, 3, 6, 1, 4, 1, 629, 202, 1, 1)
)
if mibBuilder.loadTexts:
    nbsEusmSlotTable.setStatus("current")
_NbsEusmSlotEntry_Object = MibTableRow
nbsEusmSlotEntry = _NbsEusmSlotEntry_Object(
    (1, 3, 6, 1, 4, 1, 629, 202, 1, 1, 1)
)
if mibBuilder.loadTexts:
    nbsEusmSlotEntry.setStatus("current")


class _NbsEusmSlotSupportsEusm_Type(Integer32):
    """Custom type nbsEusmSlotSupportsEusm based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notSupported", 1),
          ("supported", 2))
    )


_NbsEusmSlotSupportsEusm_Type.__name__ = "Integer32"
_NbsEusmSlotSupportsEusm_Object = MibTableColumn
nbsEusmSlotSupportsEusm = _NbsEusmSlotSupportsEusm_Object(
    (1, 3, 6, 1, 4, 1, 629, 202, 1, 1, 1, 1),
    _NbsEusmSlotSupportsEusm_Type()
)
nbsEusmSlotSupportsEusm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsEusmSlotSupportsEusm.setStatus("current")


class _NbsEusmSlotAccControlActionUntag_Type(Integer32):
    """Custom type nbsEusmSlotAccControlActionUntag based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("deny", 3),
          ("notSupported", 1),
          ("permit", 2))
    )


_NbsEusmSlotAccControlActionUntag_Type.__name__ = "Integer32"
_NbsEusmSlotAccControlActionUntag_Object = MibTableColumn
nbsEusmSlotAccControlActionUntag = _NbsEusmSlotAccControlActionUntag_Object(
    (1, 3, 6, 1, 4, 1, 629, 202, 1, 1, 1, 2),
    _NbsEusmSlotAccControlActionUntag_Type()
)
nbsEusmSlotAccControlActionUntag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsEusmSlotAccControlActionUntag.setStatus("current")


class _NbsEusmSlotAccControlActionTag_Type(Integer32):
    """Custom type nbsEusmSlotAccControlActionTag based on Integer32"""
    defaultValue = 5

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
        *(("denyAll", 2),
          ("denyVlan", 3),
          ("notSupported", 1),
          ("permitAll", 5),
          ("permitVlan", 4))
    )


_NbsEusmSlotAccControlActionTag_Type.__name__ = "Integer32"
_NbsEusmSlotAccControlActionTag_Object = MibTableColumn
nbsEusmSlotAccControlActionTag = _NbsEusmSlotAccControlActionTag_Object(
    (1, 3, 6, 1, 4, 1, 629, 202, 1, 1, 1, 3),
    _NbsEusmSlotAccControlActionTag_Type()
)
nbsEusmSlotAccControlActionTag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsEusmSlotAccControlActionTag.setStatus("current")
_NbsEusmSlotAccControlVidList_Type = DisplayString
_NbsEusmSlotAccControlVidList_Object = MibTableColumn
nbsEusmSlotAccControlVidList = _NbsEusmSlotAccControlVidList_Object(
    (1, 3, 6, 1, 4, 1, 629, 202, 1, 1, 1, 4),
    _NbsEusmSlotAccControlVidList_Type()
)
nbsEusmSlotAccControlVidList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsEusmSlotAccControlVidList.setStatus("current")


class _NbsEusmSlotLinkAggrAdmin_Type(Integer32):
    """Custom type nbsEusmSlotLinkAggrAdmin based on Integer32"""
    defaultValue = 2

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
        *(("deprecatedonSmac", 5),
          ("notSupported", 1),
          ("off", 2),
          ("onDmac", 6),
          ("onIp", 8),
          ("onRandom", 3),
          ("onXorAll", 4),
          ("onXorSd", 7))
    )


_NbsEusmSlotLinkAggrAdmin_Type.__name__ = "Integer32"
_NbsEusmSlotLinkAggrAdmin_Object = MibTableColumn
nbsEusmSlotLinkAggrAdmin = _NbsEusmSlotLinkAggrAdmin_Object(
    (1, 3, 6, 1, 4, 1, 629, 202, 1, 1, 1, 5),
    _NbsEusmSlotLinkAggrAdmin_Type()
)
nbsEusmSlotLinkAggrAdmin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsEusmSlotLinkAggrAdmin.setStatus("current")


class _NbsEusmSlotLinkAggrOper_Type(Integer32):
    """Custom type nbsEusmSlotLinkAggrOper based on Integer32"""
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
        *(("notSupported", 1),
          ("off", 2),
          ("onDmac", 6),
          ("onIp", 8),
          ("onRandom", 3),
          ("onSmac", 5),
          ("onXorAll", 4),
          ("onXorSd", 7))
    )


_NbsEusmSlotLinkAggrOper_Type.__name__ = "Integer32"
_NbsEusmSlotLinkAggrOper_Object = MibTableColumn
nbsEusmSlotLinkAggrOper = _NbsEusmSlotLinkAggrOper_Object(
    (1, 3, 6, 1, 4, 1, 629, 202, 1, 1, 1, 6),
    _NbsEusmSlotLinkAggrOper_Type()
)
nbsEusmSlotLinkAggrOper.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsEusmSlotLinkAggrOper.setStatus("current")


class _NbsEusmSlotStormControlBroadcast_Type(Integer32):
    """Custom type nbsEusmSlotStormControlBroadcast based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_NbsEusmSlotStormControlBroadcast_Type.__name__ = "Integer32"
_NbsEusmSlotStormControlBroadcast_Object = MibTableColumn
nbsEusmSlotStormControlBroadcast = _NbsEusmSlotStormControlBroadcast_Object(
    (1, 3, 6, 1, 4, 1, 629, 202, 1, 1, 1, 7),
    _NbsEusmSlotStormControlBroadcast_Type()
)
nbsEusmSlotStormControlBroadcast.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsEusmSlotStormControlBroadcast.setStatus("current")


class _NbsEusmSlotStormControlMulticast_Type(Integer32):
    """Custom type nbsEusmSlotStormControlMulticast based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_NbsEusmSlotStormControlMulticast_Type.__name__ = "Integer32"
_NbsEusmSlotStormControlMulticast_Object = MibTableColumn
nbsEusmSlotStormControlMulticast = _NbsEusmSlotStormControlMulticast_Object(
    (1, 3, 6, 1, 4, 1, 629, 202, 1, 1, 1, 8),
    _NbsEusmSlotStormControlMulticast_Type()
)
nbsEusmSlotStormControlMulticast.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsEusmSlotStormControlMulticast.setStatus("current")


class _NbsEusmSlotStormControlUnicast_Type(Integer32):
    """Custom type nbsEusmSlotStormControlUnicast based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_NbsEusmSlotStormControlUnicast_Type.__name__ = "Integer32"
_NbsEusmSlotStormControlUnicast_Object = MibTableColumn
nbsEusmSlotStormControlUnicast = _NbsEusmSlotStormControlUnicast_Object(
    (1, 3, 6, 1, 4, 1, 629, 202, 1, 1, 1, 9),
    _NbsEusmSlotStormControlUnicast_Type()
)
nbsEusmSlotStormControlUnicast.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsEusmSlotStormControlUnicast.setStatus("current")


class _NbsEusmSlotStormBurstSize_Type(Integer32):
    """Custom type nbsEusmSlotStormBurstSize based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_NbsEusmSlotStormBurstSize_Type.__name__ = "Integer32"
_NbsEusmSlotStormBurstSize_Object = MibTableColumn
nbsEusmSlotStormBurstSize = _NbsEusmSlotStormBurstSize_Object(
    (1, 3, 6, 1, 4, 1, 629, 202, 1, 1, 1, 10),
    _NbsEusmSlotStormBurstSize_Type()
)
nbsEusmSlotStormBurstSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsEusmSlotStormBurstSize.setStatus("deprecated")


class _NbsEusmSlotCoSMode_Type(Integer32):
    """Custom type nbsEusmSlotCoSMode based on Integer32"""
    defaultValue = 5

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
        *(("bothTagDscp", 4),
          ("dscpOnly", 2),
          ("none", 5),
          ("notSupported", 1),
          ("tagOnly", 3))
    )


_NbsEusmSlotCoSMode_Type.__name__ = "Integer32"
_NbsEusmSlotCoSMode_Object = MibTableColumn
nbsEusmSlotCoSMode = _NbsEusmSlotCoSMode_Object(
    (1, 3, 6, 1, 4, 1, 629, 202, 1, 1, 1, 11),
    _NbsEusmSlotCoSMode_Type()
)
nbsEusmSlotCoSMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsEusmSlotCoSMode.setStatus("current")


class _NbsEusmSlotDscpRemark_Type(Integer32):
    """Custom type nbsEusmSlotDscpRemark based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 3),
          ("enable", 2),
          ("notSupported", 1))
    )


_NbsEusmSlotDscpRemark_Type.__name__ = "Integer32"
_NbsEusmSlotDscpRemark_Object = MibTableColumn
nbsEusmSlotDscpRemark = _NbsEusmSlotDscpRemark_Object(
    (1, 3, 6, 1, 4, 1, 629, 202, 1, 1, 1, 12),
    _NbsEusmSlotDscpRemark_Type()
)
nbsEusmSlotDscpRemark.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsEusmSlotDscpRemark.setStatus("current")


class _NbsEusmSlotDscpEgressMode_Type(Integer32):
    """Custom type nbsEusmSlotDscpEgressMode based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("afMode", 2),
          ("csMode", 3),
          ("notSupported", 1))
    )


_NbsEusmSlotDscpEgressMode_Type.__name__ = "Integer32"
_NbsEusmSlotDscpEgressMode_Object = MibTableColumn
nbsEusmSlotDscpEgressMode = _NbsEusmSlotDscpEgressMode_Object(
    (1, 3, 6, 1, 4, 1, 629, 202, 1, 1, 1, 13),
    _NbsEusmSlotDscpEgressMode_Type()
)
nbsEusmSlotDscpEgressMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsEusmSlotDscpEgressMode.setStatus("current")


class _NbsEusmSlotDscpIngressEf_Type(Integer32):
    """Custom type nbsEusmSlotDscpIngressEf based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 3),
          ("enable", 2),
          ("notSupported", 1))
    )


_NbsEusmSlotDscpIngressEf_Type.__name__ = "Integer32"
_NbsEusmSlotDscpIngressEf_Object = MibTableColumn
nbsEusmSlotDscpIngressEf = _NbsEusmSlotDscpIngressEf_Object(
    (1, 3, 6, 1, 4, 1, 629, 202, 1, 1, 1, 14),
    _NbsEusmSlotDscpIngressEf_Type()
)
nbsEusmSlotDscpIngressEf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsEusmSlotDscpIngressEf.setStatus("current")


class _NbsEusmSlotDscpIngressAf_Type(Integer32):
    """Custom type nbsEusmSlotDscpIngressAf based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 3),
          ("enable", 2),
          ("notSupported", 1))
    )


_NbsEusmSlotDscpIngressAf_Type.__name__ = "Integer32"
_NbsEusmSlotDscpIngressAf_Object = MibTableColumn
nbsEusmSlotDscpIngressAf = _NbsEusmSlotDscpIngressAf_Object(
    (1, 3, 6, 1, 4, 1, 629, 202, 1, 1, 1, 15),
    _NbsEusmSlotDscpIngressAf_Type()
)
nbsEusmSlotDscpIngressAf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsEusmSlotDscpIngressAf.setStatus("current")


class _NbsEusmSlotDscpIngressCs_Type(Integer32):
    """Custom type nbsEusmSlotDscpIngressCs based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 3),
          ("enable", 2),
          ("notSupported", 1))
    )


_NbsEusmSlotDscpIngressCs_Type.__name__ = "Integer32"
_NbsEusmSlotDscpIngressCs_Object = MibTableColumn
nbsEusmSlotDscpIngressCs = _NbsEusmSlotDscpIngressCs_Object(
    (1, 3, 6, 1, 4, 1, 629, 202, 1, 1, 1, 16),
    _NbsEusmSlotDscpIngressCs_Type()
)
nbsEusmSlotDscpIngressCs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsEusmSlotDscpIngressCs.setStatus("current")


class _NbsEusmSlotDscpIngressZeroDscp_Type(Integer32):
    """Custom type nbsEusmSlotDscpIngressZeroDscp based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 3),
          ("enable", 2),
          ("notSupported", 1))
    )


_NbsEusmSlotDscpIngressZeroDscp_Type.__name__ = "Integer32"
_NbsEusmSlotDscpIngressZeroDscp_Object = MibTableColumn
nbsEusmSlotDscpIngressZeroDscp = _NbsEusmSlotDscpIngressZeroDscp_Object(
    (1, 3, 6, 1, 4, 1, 629, 202, 1, 1, 1, 17),
    _NbsEusmSlotDscpIngressZeroDscp_Type()
)
nbsEusmSlotDscpIngressZeroDscp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsEusmSlotDscpIngressZeroDscp.setStatus("current")


class _NbsEusmSlotDscpIngressAllOther_Type(Integer32):
    """Custom type nbsEusmSlotDscpIngressAllOther based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 3),
          ("enable", 2),
          ("notSupported", 1))
    )


_NbsEusmSlotDscpIngressAllOther_Type.__name__ = "Integer32"
_NbsEusmSlotDscpIngressAllOther_Object = MibTableColumn
nbsEusmSlotDscpIngressAllOther = _NbsEusmSlotDscpIngressAllOther_Object(
    (1, 3, 6, 1, 4, 1, 629, 202, 1, 1, 1, 18),
    _NbsEusmSlotDscpIngressAllOther_Type()
)
nbsEusmSlotDscpIngressAllOther.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsEusmSlotDscpIngressAllOther.setStatus("current")


class _NbsEusmSlotIometrix_Type(Integer32):
    """Custom type nbsEusmSlotIometrix based on Integer32"""
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
        *(("notSupported", 1),
          ("off", 2),
          ("on", 3))
    )


_NbsEusmSlotIometrix_Type.__name__ = "Integer32"
_NbsEusmSlotIometrix_Object = MibTableColumn
nbsEusmSlotIometrix = _NbsEusmSlotIometrix_Object(
    (1, 3, 6, 1, 4, 1, 629, 202, 1, 1, 1, 19),
    _NbsEusmSlotIometrix_Type()
)
nbsEusmSlotIometrix.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsEusmSlotIometrix.setStatus("current")


class _NbsEusmSlotManagementVid_Type(Integer32):
    """Custom type nbsEusmSlotManagementVid based on Integer32"""
    defaultValue = 4094

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_NbsEusmSlotManagementVid_Type.__name__ = "Integer32"
_NbsEusmSlotManagementVid_Object = MibTableColumn
nbsEusmSlotManagementVid = _NbsEusmSlotManagementVid_Object(
    (1, 3, 6, 1, 4, 1, 629, 202, 1, 1, 1, 20),
    _NbsEusmSlotManagementVid_Type()
)
nbsEusmSlotManagementVid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsEusmSlotManagementVid.setStatus("current")


class _NbsEusmSlotUserPortIRAdmin_Type(Unsigned32):
    """Custom type nbsEusmSlotUserPortIRAdmin based on Unsigned32"""
    defaultValue = 1000000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000000),
    )


_NbsEusmSlotUserPortIRAdmin_Type.__name__ = "Unsigned32"
_NbsEusmSlotUserPortIRAdmin_Object = MibTableColumn
nbsEusmSlotUserPortIRAdmin = _NbsEusmSlotUserPortIRAdmin_Object(
    (1, 3, 6, 1, 4, 1, 629, 202, 1, 1, 1, 21),
    _NbsEusmSlotUserPortIRAdmin_Type()
)
nbsEusmSlotUserPortIRAdmin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsEusmSlotUserPortIRAdmin.setStatus("current")
_NbsEusmSlotUserPortIROper_Type = Unsigned32
_NbsEusmSlotUserPortIROper_Object = MibTableColumn
nbsEusmSlotUserPortIROper = _NbsEusmSlotUserPortIROper_Object(
    (1, 3, 6, 1, 4, 1, 629, 202, 1, 1, 1, 22),
    _NbsEusmSlotUserPortIROper_Type()
)
nbsEusmSlotUserPortIROper.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsEusmSlotUserPortIROper.setStatus("current")


class _NbsEusmSlotMaxFlowCfgSize_Type(Integer32):
    """Custom type nbsEusmSlotMaxFlowCfgSize based on Integer32"""
    defaultValue = 32


_NbsEusmSlotMaxFlowCfgSize_Object = MibTableColumn
nbsEusmSlotMaxFlowCfgSize = _NbsEusmSlotMaxFlowCfgSize_Object(
    (1, 3, 6, 1, 4, 1, 629, 202, 1, 1, 1, 23),
    _NbsEusmSlotMaxFlowCfgSize_Type()
)
nbsEusmSlotMaxFlowCfgSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsEusmSlotMaxFlowCfgSize.setStatus("current")


class _NbsEusmSlotMaxVlanTranSize_Type(Integer32):
    """Custom type nbsEusmSlotMaxVlanTranSize based on Integer32"""
    defaultValue = 4


_NbsEusmSlotMaxVlanTranSize_Object = MibTableColumn
nbsEusmSlotMaxVlanTranSize = _NbsEusmSlotMaxVlanTranSize_Object(
    (1, 3, 6, 1, 4, 1, 629, 202, 1, 1, 1, 24),
    _NbsEusmSlotMaxVlanTranSize_Type()
)
nbsEusmSlotMaxVlanTranSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsEusmSlotMaxVlanTranSize.setStatus("current")


class _NbsEusmSlotMaxDscpMapSize_Type(Integer32):
    """Custom type nbsEusmSlotMaxDscpMapSize based on Integer32"""
    defaultValue = 7


_NbsEusmSlotMaxDscpMapSize_Object = MibTableColumn
nbsEusmSlotMaxDscpMapSize = _NbsEusmSlotMaxDscpMapSize_Object(
    (1, 3, 6, 1, 4, 1, 629, 202, 1, 1, 1, 25),
    _NbsEusmSlotMaxDscpMapSize_Type()
)
nbsEusmSlotMaxDscpMapSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsEusmSlotMaxDscpMapSize.setStatus("current")


class _NbsEusmSlotMaxCosPrioSize_Type(Integer32):
    """Custom type nbsEusmSlotMaxCosPrioSize based on Integer32"""
    defaultValue = 8


_NbsEusmSlotMaxCosPrioSize_Object = MibTableColumn
nbsEusmSlotMaxCosPrioSize = _NbsEusmSlotMaxCosPrioSize_Object(
    (1, 3, 6, 1, 4, 1, 629, 202, 1, 1, 1, 26),
    _NbsEusmSlotMaxCosPrioSize_Type()
)
nbsEusmSlotMaxCosPrioSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsEusmSlotMaxCosPrioSize.setStatus("current")
_NbsEusmFlowCfgTable_Object = MibTable
nbsEusmFlowCfgTable = _NbsEusmFlowCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 629, 202, 1, 2)
)
if mibBuilder.loadTexts:
    nbsEusmFlowCfgTable.setStatus("current")
_NbsEusmFlowCfgEntry_Object = MibTableRow
nbsEusmFlowCfgEntry = _NbsEusmFlowCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 629, 202, 1, 2, 1)
)
nbsEusmFlowCfgEntry.setIndexNames(
    (0, "NBS-EUSM-MIB", "nbsEusmFlowCfgChassis"),
    (0, "NBS-EUSM-MIB", "nbsEusmFlowCfgSlot"),
    (0, "NBS-EUSM-MIB", "nbsEusmFlowCfgVid"),
    (0, "NBS-EUSM-MIB", "nbsEusmFlowCfgPriority"),
)
if mibBuilder.loadTexts:
    nbsEusmFlowCfgEntry.setStatus("current")
_NbsEusmFlowCfgChassis_Type = Integer32
_NbsEusmFlowCfgChassis_Object = MibTableColumn
nbsEusmFlowCfgChassis = _NbsEusmFlowCfgChassis_Object(
    (1, 3, 6, 1, 4, 1, 629, 202, 1, 2, 1, 1),
    _NbsEusmFlowCfgChassis_Type()
)
nbsEusmFlowCfgChassis.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsEusmFlowCfgChassis.setStatus("current")
_NbsEusmFlowCfgSlot_Type = Integer32
_NbsEusmFlowCfgSlot_Object = MibTableColumn
nbsEusmFlowCfgSlot = _NbsEusmFlowCfgSlot_Object(
    (1, 3, 6, 1, 4, 1, 629, 202, 1, 2, 1, 2),
    _NbsEusmFlowCfgSlot_Type()
)
nbsEusmFlowCfgSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsEusmFlowCfgSlot.setStatus("current")


class _NbsEusmFlowCfgVid_Type(Integer32):
    """Custom type nbsEusmFlowCfgVid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_NbsEusmFlowCfgVid_Type.__name__ = "Integer32"
_NbsEusmFlowCfgVid_Object = MibTableColumn
nbsEusmFlowCfgVid = _NbsEusmFlowCfgVid_Object(
    (1, 3, 6, 1, 4, 1, 629, 202, 1, 2, 1, 3),
    _NbsEusmFlowCfgVid_Type()
)
nbsEusmFlowCfgVid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsEusmFlowCfgVid.setStatus("current")


class _NbsEusmFlowCfgPriority_Type(Integer32):
    """Custom type nbsEusmFlowCfgPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_NbsEusmFlowCfgPriority_Type.__name__ = "Integer32"
_NbsEusmFlowCfgPriority_Object = MibTableColumn
nbsEusmFlowCfgPriority = _NbsEusmFlowCfgPriority_Object(
    (1, 3, 6, 1, 4, 1, 629, 202, 1, 2, 1, 4),
    _NbsEusmFlowCfgPriority_Type()
)
nbsEusmFlowCfgPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsEusmFlowCfgPriority.setStatus("current")
_NbsEusmFlowCfgRowStatus_Type = RowStatus
_NbsEusmFlowCfgRowStatus_Object = MibTableColumn
nbsEusmFlowCfgRowStatus = _NbsEusmFlowCfgRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 629, 202, 1, 2, 1, 5),
    _NbsEusmFlowCfgRowStatus_Type()
)
nbsEusmFlowCfgRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nbsEusmFlowCfgRowStatus.setStatus("current")


class _NbsEusmFlowCfgStorageType_Type(StorageType):
    """Custom type nbsEusmFlowCfgStorageType based on StorageType"""


_NbsEusmFlowCfgStorageType_Object = MibTableColumn
nbsEusmFlowCfgStorageType = _NbsEusmFlowCfgStorageType_Object(
    (1, 3, 6, 1, 4, 1, 629, 202, 1, 2, 1, 6),
    _NbsEusmFlowCfgStorageType_Type()
)
nbsEusmFlowCfgStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nbsEusmFlowCfgStorageType.setStatus("current")


class _NbsEusmFlowCfgIRAdmin_Type(Unsigned32):
    """Custom type nbsEusmFlowCfgIRAdmin based on Unsigned32"""
    defaultValue = 1000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000000),
    )


_NbsEusmFlowCfgIRAdmin_Type.__name__ = "Unsigned32"
_NbsEusmFlowCfgIRAdmin_Object = MibTableColumn
nbsEusmFlowCfgIRAdmin = _NbsEusmFlowCfgIRAdmin_Object(
    (1, 3, 6, 1, 4, 1, 629, 202, 1, 2, 1, 7),
    _NbsEusmFlowCfgIRAdmin_Type()
)
nbsEusmFlowCfgIRAdmin.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nbsEusmFlowCfgIRAdmin.setStatus("current")
_NbsEusmFlowCfgIROper_Type = Unsigned32
_NbsEusmFlowCfgIROper_Object = MibTableColumn
nbsEusmFlowCfgIROper = _NbsEusmFlowCfgIROper_Object(
    (1, 3, 6, 1, 4, 1, 629, 202, 1, 2, 1, 8),
    _NbsEusmFlowCfgIROper_Type()
)
nbsEusmFlowCfgIROper.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsEusmFlowCfgIROper.setStatus("current")


class _NbsEusmFlowCfgClearCounter_Type(Integer32):
    """Custom type nbsEusmFlowCfgClearCounter based on Integer32"""
    defaultValue = 2

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
        *(("clear", 4),
          ("idle", 2),
          ("inProgress", 3),
          ("notSupported", 1))
    )


_NbsEusmFlowCfgClearCounter_Type.__name__ = "Integer32"
_NbsEusmFlowCfgClearCounter_Object = MibTableColumn
nbsEusmFlowCfgClearCounter = _NbsEusmFlowCfgClearCounter_Object(
    (1, 3, 6, 1, 4, 1, 629, 202, 1, 2, 1, 9),
    _NbsEusmFlowCfgClearCounter_Type()
)
nbsEusmFlowCfgClearCounter.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nbsEusmFlowCfgClearCounter.setStatus("current")
_NbsEusmFlowStatusTable_Object = MibTable
nbsEusmFlowStatusTable = _NbsEusmFlowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 629, 202, 1, 3)
)
if mibBuilder.loadTexts:
    nbsEusmFlowStatusTable.setStatus("current")
_NbsEusmFlowStatusEntry_Object = MibTableRow
nbsEusmFlowStatusEntry = _NbsEusmFlowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 629, 202, 1, 3, 1)
)
if mibBuilder.loadTexts:
    nbsEusmFlowStatusEntry.setStatus("current")
_NbsEusmFlowStatusRxFrames_Type = Counter64
_NbsEusmFlowStatusRxFrames_Object = MibTableColumn
nbsEusmFlowStatusRxFrames = _NbsEusmFlowStatusRxFrames_Object(
    (1, 3, 6, 1, 4, 1, 629, 202, 1, 3, 1, 1),
    _NbsEusmFlowStatusRxFrames_Type()
)
nbsEusmFlowStatusRxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsEusmFlowStatusRxFrames.setStatus("current")
_NbsEusmFlowStatusRxOctets_Type = Counter64
_NbsEusmFlowStatusRxOctets_Object = MibTableColumn
nbsEusmFlowStatusRxOctets = _NbsEusmFlowStatusRxOctets_Object(
    (1, 3, 6, 1, 4, 1, 629, 202, 1, 3, 1, 2),
    _NbsEusmFlowStatusRxOctets_Type()
)
nbsEusmFlowStatusRxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsEusmFlowStatusRxOctets.setStatus("current")
_NbsEusmVidMapTable_Object = MibTable
nbsEusmVidMapTable = _NbsEusmVidMapTable_Object(
    (1, 3, 6, 1, 4, 1, 629, 202, 1, 4)
)
if mibBuilder.loadTexts:
    nbsEusmVidMapTable.setStatus("current")
_NbsEusmVidMapEntry_Object = MibTableRow
nbsEusmVidMapEntry = _NbsEusmVidMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 629, 202, 1, 4, 1)
)
nbsEusmVidMapEntry.setIndexNames(
    (0, "NBS-EUSM-MIB", "nbsEusmVidMapChassis"),
    (0, "NBS-EUSM-MIB", "nbsEusmVidMapSlot"),
    (0, "NBS-EUSM-MIB", "nbsEusmVidMapFromVid"),
)
if mibBuilder.loadTexts:
    nbsEusmVidMapEntry.setStatus("current")
_NbsEusmVidMapChassis_Type = Integer32
_NbsEusmVidMapChassis_Object = MibTableColumn
nbsEusmVidMapChassis = _NbsEusmVidMapChassis_Object(
    (1, 3, 6, 1, 4, 1, 629, 202, 1, 4, 1, 1),
    _NbsEusmVidMapChassis_Type()
)
nbsEusmVidMapChassis.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsEusmVidMapChassis.setStatus("current")
_NbsEusmVidMapSlot_Type = Integer32
_NbsEusmVidMapSlot_Object = MibTableColumn
nbsEusmVidMapSlot = _NbsEusmVidMapSlot_Object(
    (1, 3, 6, 1, 4, 1, 629, 202, 1, 4, 1, 2),
    _NbsEusmVidMapSlot_Type()
)
nbsEusmVidMapSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsEusmVidMapSlot.setStatus("current")


class _NbsEusmVidMapFromVid_Type(Integer32):
    """Custom type nbsEusmVidMapFromVid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_NbsEusmVidMapFromVid_Type.__name__ = "Integer32"
_NbsEusmVidMapFromVid_Object = MibTableColumn
nbsEusmVidMapFromVid = _NbsEusmVidMapFromVid_Object(
    (1, 3, 6, 1, 4, 1, 629, 202, 1, 4, 1, 3),
    _NbsEusmVidMapFromVid_Type()
)
nbsEusmVidMapFromVid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsEusmVidMapFromVid.setStatus("current")


class _NbsEusmVidMapToVid_Type(Integer32):
    """Custom type nbsEusmVidMapToVid based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_NbsEusmVidMapToVid_Type.__name__ = "Integer32"
_NbsEusmVidMapToVid_Object = MibTableColumn
nbsEusmVidMapToVid = _NbsEusmVidMapToVid_Object(
    (1, 3, 6, 1, 4, 1, 629, 202, 1, 4, 1, 4),
    _NbsEusmVidMapToVid_Type()
)
nbsEusmVidMapToVid.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nbsEusmVidMapToVid.setStatus("current")
_NbsEusmVidMapRowStatus_Type = RowStatus
_NbsEusmVidMapRowStatus_Object = MibTableColumn
nbsEusmVidMapRowStatus = _NbsEusmVidMapRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 629, 202, 1, 4, 1, 5),
    _NbsEusmVidMapRowStatus_Type()
)
nbsEusmVidMapRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nbsEusmVidMapRowStatus.setStatus("current")


class _NbsEusmVidMapStorageType_Type(StorageType):
    """Custom type nbsEusmVidMapStorageType based on StorageType"""


_NbsEusmVidMapStorageType_Object = MibTableColumn
nbsEusmVidMapStorageType = _NbsEusmVidMapStorageType_Object(
    (1, 3, 6, 1, 4, 1, 629, 202, 1, 4, 1, 6),
    _NbsEusmVidMapStorageType_Type()
)
nbsEusmVidMapStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nbsEusmVidMapStorageType.setStatus("current")
_NbsEusmCoSDscpMapTable_Object = MibTable
nbsEusmCoSDscpMapTable = _NbsEusmCoSDscpMapTable_Object(
    (1, 3, 6, 1, 4, 1, 629, 202, 1, 5)
)
if mibBuilder.loadTexts:
    nbsEusmCoSDscpMapTable.setStatus("current")
_NbsEusmCoSDscpMapEntry_Object = MibTableRow
nbsEusmCoSDscpMapEntry = _NbsEusmCoSDscpMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 629, 202, 1, 5, 1)
)
nbsEusmCoSDscpMapEntry.setIndexNames(
    (0, "NBS-EUSM-MIB", "nbsEusmCoSDscpMapChassis"),
    (0, "NBS-EUSM-MIB", "nbsEusmCoSDscpMapSlot"),
    (0, "NBS-EUSM-MIB", "nbsEusmCoSDscpMapDscp"),
)
if mibBuilder.loadTexts:
    nbsEusmCoSDscpMapEntry.setStatus("current")
_NbsEusmCoSDscpMapChassis_Type = Integer32
_NbsEusmCoSDscpMapChassis_Object = MibTableColumn
nbsEusmCoSDscpMapChassis = _NbsEusmCoSDscpMapChassis_Object(
    (1, 3, 6, 1, 4, 1, 629, 202, 1, 5, 1, 1),
    _NbsEusmCoSDscpMapChassis_Type()
)
nbsEusmCoSDscpMapChassis.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsEusmCoSDscpMapChassis.setStatus("current")
_NbsEusmCoSDscpMapSlot_Type = Integer32
_NbsEusmCoSDscpMapSlot_Object = MibTableColumn
nbsEusmCoSDscpMapSlot = _NbsEusmCoSDscpMapSlot_Object(
    (1, 3, 6, 1, 4, 1, 629, 202, 1, 5, 1, 2),
    _NbsEusmCoSDscpMapSlot_Type()
)
nbsEusmCoSDscpMapSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsEusmCoSDscpMapSlot.setStatus("current")


class _NbsEusmCoSDscpMapDscp_Type(Integer32):
    """Custom type nbsEusmCoSDscpMapDscp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_NbsEusmCoSDscpMapDscp_Type.__name__ = "Integer32"
_NbsEusmCoSDscpMapDscp_Object = MibTableColumn
nbsEusmCoSDscpMapDscp = _NbsEusmCoSDscpMapDscp_Object(
    (1, 3, 6, 1, 4, 1, 629, 202, 1, 5, 1, 3),
    _NbsEusmCoSDscpMapDscp_Type()
)
nbsEusmCoSDscpMapDscp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsEusmCoSDscpMapDscp.setStatus("current")


class _NbsEusmCoSDscpMapSlcPrio_Type(Integer32):
    """Custom type nbsEusmCoSDscpMapSlcPrio based on Integer32"""
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
        *(("high", 4),
          ("low", 1),
          ("medium", 3),
          ("normal", 2))
    )


_NbsEusmCoSDscpMapSlcPrio_Type.__name__ = "Integer32"
_NbsEusmCoSDscpMapSlcPrio_Object = MibTableColumn
nbsEusmCoSDscpMapSlcPrio = _NbsEusmCoSDscpMapSlcPrio_Object(
    (1, 3, 6, 1, 4, 1, 629, 202, 1, 5, 1, 4),
    _NbsEusmCoSDscpMapSlcPrio_Type()
)
nbsEusmCoSDscpMapSlcPrio.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nbsEusmCoSDscpMapSlcPrio.setStatus("current")
_NbsEusmCoSDscpMapRowStatus_Type = RowStatus
_NbsEusmCoSDscpMapRowStatus_Object = MibTableColumn
nbsEusmCoSDscpMapRowStatus = _NbsEusmCoSDscpMapRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 629, 202, 1, 5, 1, 5),
    _NbsEusmCoSDscpMapRowStatus_Type()
)
nbsEusmCoSDscpMapRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nbsEusmCoSDscpMapRowStatus.setStatus("current")


class _NbsEusmCoSDscpMapStorageType_Type(StorageType):
    """Custom type nbsEusmCoSDscpMapStorageType based on StorageType"""


_NbsEusmCoSDscpMapStorageType_Object = MibTableColumn
nbsEusmCoSDscpMapStorageType = _NbsEusmCoSDscpMapStorageType_Object(
    (1, 3, 6, 1, 4, 1, 629, 202, 1, 5, 1, 6),
    _NbsEusmCoSDscpMapStorageType_Type()
)
nbsEusmCoSDscpMapStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nbsEusmCoSDscpMapStorageType.setStatus("current")
_NbsEusmCoSTagPrioMapTable_Object = MibTable
nbsEusmCoSTagPrioMapTable = _NbsEusmCoSTagPrioMapTable_Object(
    (1, 3, 6, 1, 4, 1, 629, 202, 1, 6)
)
if mibBuilder.loadTexts:
    nbsEusmCoSTagPrioMapTable.setStatus("current")
_NbsEusmCoSTagPrioMapEntry_Object = MibTableRow
nbsEusmCoSTagPrioMapEntry = _NbsEusmCoSTagPrioMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 629, 202, 1, 6, 1)
)
nbsEusmCoSTagPrioMapEntry.setIndexNames(
    (0, "NBS-EUSM-MIB", "nbsEusmCoSTagPrioMapChassis"),
    (0, "NBS-EUSM-MIB", "nbsEusmCoSTagPrioMapSlot"),
    (0, "NBS-EUSM-MIB", "nbsEusmCoSTagPrioMapPriority"),
)
if mibBuilder.loadTexts:
    nbsEusmCoSTagPrioMapEntry.setStatus("current")
_NbsEusmCoSTagPrioMapChassis_Type = Integer32
_NbsEusmCoSTagPrioMapChassis_Object = MibTableColumn
nbsEusmCoSTagPrioMapChassis = _NbsEusmCoSTagPrioMapChassis_Object(
    (1, 3, 6, 1, 4, 1, 629, 202, 1, 6, 1, 1),
    _NbsEusmCoSTagPrioMapChassis_Type()
)
nbsEusmCoSTagPrioMapChassis.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsEusmCoSTagPrioMapChassis.setStatus("current")
_NbsEusmCoSTagPrioMapSlot_Type = Integer32
_NbsEusmCoSTagPrioMapSlot_Object = MibTableColumn
nbsEusmCoSTagPrioMapSlot = _NbsEusmCoSTagPrioMapSlot_Object(
    (1, 3, 6, 1, 4, 1, 629, 202, 1, 6, 1, 2),
    _NbsEusmCoSTagPrioMapSlot_Type()
)
nbsEusmCoSTagPrioMapSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsEusmCoSTagPrioMapSlot.setStatus("current")


class _NbsEusmCoSTagPrioMapPriority_Type(Integer32):
    """Custom type nbsEusmCoSTagPrioMapPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_NbsEusmCoSTagPrioMapPriority_Type.__name__ = "Integer32"
_NbsEusmCoSTagPrioMapPriority_Object = MibTableColumn
nbsEusmCoSTagPrioMapPriority = _NbsEusmCoSTagPrioMapPriority_Object(
    (1, 3, 6, 1, 4, 1, 629, 202, 1, 6, 1, 3),
    _NbsEusmCoSTagPrioMapPriority_Type()
)
nbsEusmCoSTagPrioMapPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsEusmCoSTagPrioMapPriority.setStatus("current")


class _NbsEusmCoSTagPrioMapSlcPrio_Type(Integer32):
    """Custom type nbsEusmCoSTagPrioMapSlcPrio based on Integer32"""
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
        *(("high", 4),
          ("low", 1),
          ("medium", 3),
          ("normal", 2))
    )


_NbsEusmCoSTagPrioMapSlcPrio_Type.__name__ = "Integer32"
_NbsEusmCoSTagPrioMapSlcPrio_Object = MibTableColumn
nbsEusmCoSTagPrioMapSlcPrio = _NbsEusmCoSTagPrioMapSlcPrio_Object(
    (1, 3, 6, 1, 4, 1, 629, 202, 1, 6, 1, 4),
    _NbsEusmCoSTagPrioMapSlcPrio_Type()
)
nbsEusmCoSTagPrioMapSlcPrio.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nbsEusmCoSTagPrioMapSlcPrio.setStatus("current")
_NbsEusmPortGrp_ObjectIdentity = ObjectIdentity
nbsEusmPortGrp = _NbsEusmPortGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 202, 2)
)
if mibBuilder.loadTexts:
    nbsEusmPortGrp.setStatus("current")
_NbsEusmPortTable_Object = MibTable
nbsEusmPortTable = _NbsEusmPortTable_Object(
    (1, 3, 6, 1, 4, 1, 629, 202, 2, 1)
)
if mibBuilder.loadTexts:
    nbsEusmPortTable.setStatus("current")
_NbsEusmPortEntry_Object = MibTableRow
nbsEusmPortEntry = _NbsEusmPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 629, 202, 2, 1, 1)
)
if mibBuilder.loadTexts:
    nbsEusmPortEntry.setStatus("current")


class _NbsEusmPortSupportsEusm_Type(Integer32):
    """Custom type nbsEusmPortSupportsEusm based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notSupported", 1),
          ("supported", 2))
    )


_NbsEusmPortSupportsEusm_Type.__name__ = "Integer32"
_NbsEusmPortSupportsEusm_Object = MibTableColumn
nbsEusmPortSupportsEusm = _NbsEusmPortSupportsEusm_Object(
    (1, 3, 6, 1, 4, 1, 629, 202, 2, 1, 1, 1),
    _NbsEusmPortSupportsEusm_Type()
)
nbsEusmPortSupportsEusm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsEusmPortSupportsEusm.setStatus("current")


class _NbsEusmPortSmartLoopbackAction_Type(Integer32):
    """Custom type nbsEusmPortSmartLoopbackAction based on Integer32"""
    defaultValue = 2

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
        *(("all", 3),
          ("mac", 7),
          ("notSupported", 1),
          ("off", 2),
          ("onBoth", 6),
          ("onDA", 4),
          ("onVid", 5))
    )


_NbsEusmPortSmartLoopbackAction_Type.__name__ = "Integer32"
_NbsEusmPortSmartLoopbackAction_Object = MibTableColumn
nbsEusmPortSmartLoopbackAction = _NbsEusmPortSmartLoopbackAction_Object(
    (1, 3, 6, 1, 4, 1, 629, 202, 2, 1, 1, 2),
    _NbsEusmPortSmartLoopbackAction_Type()
)
nbsEusmPortSmartLoopbackAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsEusmPortSmartLoopbackAction.setStatus("current")


class _NbsEusmPortSmartLoopbackSwap_Type(Integer32):
    """Custom type nbsEusmPortSmartLoopbackSwap based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notSupported", 1),
          ("off", 2),
          ("on", 3))
    )


_NbsEusmPortSmartLoopbackSwap_Type.__name__ = "Integer32"
_NbsEusmPortSmartLoopbackSwap_Object = MibTableColumn
nbsEusmPortSmartLoopbackSwap = _NbsEusmPortSmartLoopbackSwap_Object(
    (1, 3, 6, 1, 4, 1, 629, 202, 2, 1, 1, 3),
    _NbsEusmPortSmartLoopbackSwap_Type()
)
nbsEusmPortSmartLoopbackSwap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsEusmPortSmartLoopbackSwap.setStatus("current")


class _NbsEusmPortSmartLoopbackMac_Type(OctetString):
    """Custom type nbsEusmPortSmartLoopbackMac based on OctetString"""
    defaultHexValue = "000000000000"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_NbsEusmPortSmartLoopbackMac_Type.__name__ = "OctetString"
_NbsEusmPortSmartLoopbackMac_Object = MibTableColumn
nbsEusmPortSmartLoopbackMac = _NbsEusmPortSmartLoopbackMac_Object(
    (1, 3, 6, 1, 4, 1, 629, 202, 2, 1, 1, 4),
    _NbsEusmPortSmartLoopbackMac_Type()
)
nbsEusmPortSmartLoopbackMac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsEusmPortSmartLoopbackMac.setStatus("current")


class _NbsEusmPortSmartLoopbackVid_Type(Integer32):
    """Custom type nbsEusmPortSmartLoopbackVid based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_NbsEusmPortSmartLoopbackVid_Type.__name__ = "Integer32"
_NbsEusmPortSmartLoopbackVid_Object = MibTableColumn
nbsEusmPortSmartLoopbackVid = _NbsEusmPortSmartLoopbackVid_Object(
    (1, 3, 6, 1, 4, 1, 629, 202, 2, 1, 1, 5),
    _NbsEusmPortSmartLoopbackVid_Type()
)
nbsEusmPortSmartLoopbackVid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsEusmPortSmartLoopbackVid.setStatus("current")


class _NbsEusmPortVlanTagAction_Type(Integer32):
    """Custom type nbsEusmPortVlanTagAction based on Integer32"""
    defaultValue = 4

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
        *(("add", 2),
          ("ignore", 4),
          ("notSupported", 1),
          ("strip", 3))
    )


_NbsEusmPortVlanTagAction_Type.__name__ = "Integer32"
_NbsEusmPortVlanTagAction_Object = MibTableColumn
nbsEusmPortVlanTagAction = _NbsEusmPortVlanTagAction_Object(
    (1, 3, 6, 1, 4, 1, 629, 202, 2, 1, 1, 6),
    _NbsEusmPortVlanTagAction_Type()
)
nbsEusmPortVlanTagAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsEusmPortVlanTagAction.setStatus("current")


class _NbsEusmPortVlanTagVid_Type(Integer32):
    """Custom type nbsEusmPortVlanTagVid based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_NbsEusmPortVlanTagVid_Type.__name__ = "Integer32"
_NbsEusmPortVlanTagVid_Object = MibTableColumn
nbsEusmPortVlanTagVid = _NbsEusmPortVlanTagVid_Object(
    (1, 3, 6, 1, 4, 1, 629, 202, 2, 1, 1, 7),
    _NbsEusmPortVlanTagVid_Type()
)
nbsEusmPortVlanTagVid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsEusmPortVlanTagVid.setStatus("current")


class _NbsEusmPortVlanTagPriority_Type(Integer32):
    """Custom type nbsEusmPortVlanTagPriority based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_NbsEusmPortVlanTagPriority_Type.__name__ = "Integer32"
_NbsEusmPortVlanTagPriority_Object = MibTableColumn
nbsEusmPortVlanTagPriority = _NbsEusmPortVlanTagPriority_Object(
    (1, 3, 6, 1, 4, 1, 629, 202, 2, 1, 1, 8),
    _NbsEusmPortVlanTagPriority_Type()
)
nbsEusmPortVlanTagPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsEusmPortVlanTagPriority.setStatus("current")
_NbsEusmTestGrp_ObjectIdentity = ObjectIdentity
nbsEusmTestGrp = _NbsEusmTestGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 202, 3)
)
if mibBuilder.loadTexts:
    nbsEusmTestGrp.setStatus("current")
_NbsEusmTgaTable_Object = MibTable
nbsEusmTgaTable = _NbsEusmTgaTable_Object(
    (1, 3, 6, 1, 4, 1, 629, 202, 3, 1)
)
if mibBuilder.loadTexts:
    nbsEusmTgaTable.setStatus("current")
_NbsEusmTgaEntry_Object = MibTableRow
nbsEusmTgaEntry = _NbsEusmTgaEntry_Object(
    (1, 3, 6, 1, 4, 1, 629, 202, 3, 1, 1)
)
if mibBuilder.loadTexts:
    nbsEusmTgaEntry.setStatus("current")


class _NbsEusmTgaDa_Type(OctetString):
    """Custom type nbsEusmTgaDa based on OctetString"""
    defaultHexValue = "000000000000"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_NbsEusmTgaDa_Type.__name__ = "OctetString"
_NbsEusmTgaDa_Object = MibTableColumn
nbsEusmTgaDa = _NbsEusmTgaDa_Object(
    (1, 3, 6, 1, 4, 1, 629, 202, 3, 1, 1, 1),
    _NbsEusmTgaDa_Type()
)
nbsEusmTgaDa.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsEusmTgaDa.setStatus("current")


class _NbsEusmTgaDaType_Type(Integer32):
    """Custom type nbsEusmTgaDaType based on Integer32"""
    defaultValue = 2

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
        *(("fixed", 3),
          ("increment", 4),
          ("notSupported", 1),
          ("random", 2))
    )


_NbsEusmTgaDaType_Type.__name__ = "Integer32"
_NbsEusmTgaDaType_Object = MibTableColumn
nbsEusmTgaDaType = _NbsEusmTgaDaType_Object(
    (1, 3, 6, 1, 4, 1, 629, 202, 3, 1, 1, 2),
    _NbsEusmTgaDaType_Type()
)
nbsEusmTgaDaType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsEusmTgaDaType.setStatus("current")


class _NbsEusmTgaSa_Type(OctetString):
    """Custom type nbsEusmTgaSa based on OctetString"""
    defaultHexValue = "000000000000"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_NbsEusmTgaSa_Type.__name__ = "OctetString"
_NbsEusmTgaSa_Object = MibTableColumn
nbsEusmTgaSa = _NbsEusmTgaSa_Object(
    (1, 3, 6, 1, 4, 1, 629, 202, 3, 1, 1, 3),
    _NbsEusmTgaSa_Type()
)
nbsEusmTgaSa.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsEusmTgaSa.setStatus("current")


class _NbsEusmTgaSaType_Type(Integer32):
    """Custom type nbsEusmTgaSaType based on Integer32"""
    defaultValue = 2

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
        *(("fixed", 3),
          ("increment", 4),
          ("notSupported", 1),
          ("random", 2))
    )


_NbsEusmTgaSaType_Type.__name__ = "Integer32"
_NbsEusmTgaSaType_Object = MibTableColumn
nbsEusmTgaSaType = _NbsEusmTgaSaType_Object(
    (1, 3, 6, 1, 4, 1, 629, 202, 3, 1, 1, 4),
    _NbsEusmTgaSaType_Type()
)
nbsEusmTgaSaType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsEusmTgaSaType.setStatus("current")


class _NbsEusmTgaTag_Type(OctetString):
    """Custom type nbsEusmTgaTag based on OctetString"""
    defaultHexValue = "00000000"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_NbsEusmTgaTag_Type.__name__ = "OctetString"
_NbsEusmTgaTag_Object = MibTableColumn
nbsEusmTgaTag = _NbsEusmTgaTag_Object(
    (1, 3, 6, 1, 4, 1, 629, 202, 3, 1, 1, 5),
    _NbsEusmTgaTag_Type()
)
nbsEusmTgaTag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsEusmTgaTag.setStatus("current")


class _NbsEusmTgaTagType_Type(Integer32):
    """Custom type nbsEusmTgaTagType based on Integer32"""
    defaultValue = 2

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
        *(("fixed", 3),
          ("increment", 4),
          ("notSupported", 1),
          ("random", 2))
    )


_NbsEusmTgaTagType_Type.__name__ = "Integer32"
_NbsEusmTgaTagType_Object = MibTableColumn
nbsEusmTgaTagType = _NbsEusmTgaTagType_Object(
    (1, 3, 6, 1, 4, 1, 629, 202, 3, 1, 1, 6),
    _NbsEusmTgaTagType_Type()
)
nbsEusmTgaTagType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsEusmTgaTagType.setStatus("current")


class _NbsEusmTgaPattern_Type(OctetString):
    """Custom type nbsEusmTgaPattern based on OctetString"""
    defaultHexValue = "0000"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_NbsEusmTgaPattern_Type.__name__ = "OctetString"
_NbsEusmTgaPattern_Object = MibTableColumn
nbsEusmTgaPattern = _NbsEusmTgaPattern_Object(
    (1, 3, 6, 1, 4, 1, 629, 202, 3, 1, 1, 7),
    _NbsEusmTgaPattern_Type()
)
nbsEusmTgaPattern.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsEusmTgaPattern.setStatus("current")


class _NbsEusmTgaPatternType_Type(Integer32):
    """Custom type nbsEusmTgaPatternType based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("fixed", 3),
          ("notSupported", 1),
          ("random", 2))
    )


_NbsEusmTgaPatternType_Type.__name__ = "Integer32"
_NbsEusmTgaPatternType_Object = MibTableColumn
nbsEusmTgaPatternType = _NbsEusmTgaPatternType_Object(
    (1, 3, 6, 1, 4, 1, 629, 202, 3, 1, 1, 8),
    _NbsEusmTgaPatternType_Type()
)
nbsEusmTgaPatternType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsEusmTgaPatternType.setStatus("current")


class _NbsEusmTgaFrameSize_Type(Integer32):
    """Custom type nbsEusmTgaFrameSize based on Integer32"""
    defaultValue = 64

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(64, 9600),
    )


_NbsEusmTgaFrameSize_Type.__name__ = "Integer32"
_NbsEusmTgaFrameSize_Object = MibTableColumn
nbsEusmTgaFrameSize = _NbsEusmTgaFrameSize_Object(
    (1, 3, 6, 1, 4, 1, 629, 202, 3, 1, 1, 9),
    _NbsEusmTgaFrameSize_Type()
)
nbsEusmTgaFrameSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsEusmTgaFrameSize.setStatus("current")


class _NbsEusmTgaFrameSizeType_Type(Integer32):
    """Custom type nbsEusmTgaFrameSizeType based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("fixed", 3),
          ("notSupported", 1),
          ("random", 2))
    )


_NbsEusmTgaFrameSizeType_Type.__name__ = "Integer32"
_NbsEusmTgaFrameSizeType_Object = MibTableColumn
nbsEusmTgaFrameSizeType = _NbsEusmTgaFrameSizeType_Object(
    (1, 3, 6, 1, 4, 1, 629, 202, 3, 1, 1, 10),
    _NbsEusmTgaFrameSizeType_Type()
)
nbsEusmTgaFrameSizeType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsEusmTgaFrameSizeType.setStatus("current")


class _NbsEusmTgaFrameCount_Type(Unsigned32):
    """Custom type nbsEusmTgaFrameCount based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967294),
    )


_NbsEusmTgaFrameCount_Type.__name__ = "Unsigned32"
_NbsEusmTgaFrameCount_Object = MibTableColumn
nbsEusmTgaFrameCount = _NbsEusmTgaFrameCount_Object(
    (1, 3, 6, 1, 4, 1, 629, 202, 3, 1, 1, 11),
    _NbsEusmTgaFrameCount_Type()
)
nbsEusmTgaFrameCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsEusmTgaFrameCount.setStatus("current")


class _NbsEusmTgaFrameCountType_Type(Integer32):
    """Custom type nbsEusmTgaFrameCountType based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("continuous", 2),
          ("fixed", 3),
          ("notSupported", 1))
    )


_NbsEusmTgaFrameCountType_Type.__name__ = "Integer32"
_NbsEusmTgaFrameCountType_Object = MibTableColumn
nbsEusmTgaFrameCountType = _NbsEusmTgaFrameCountType_Object(
    (1, 3, 6, 1, 4, 1, 629, 202, 3, 1, 1, 12),
    _NbsEusmTgaFrameCountType_Type()
)
nbsEusmTgaFrameCountType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsEusmTgaFrameCountType.setStatus("current")


class _NbsEusmTgaInterPacketGap_Type(Integer32):
    """Custom type nbsEusmTgaInterPacketGap based on Integer32"""
    defaultValue = 1249928

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(12, 134217727),
    )


_NbsEusmTgaInterPacketGap_Type.__name__ = "Integer32"
_NbsEusmTgaInterPacketGap_Object = MibTableColumn
nbsEusmTgaInterPacketGap = _NbsEusmTgaInterPacketGap_Object(
    (1, 3, 6, 1, 4, 1, 629, 202, 3, 1, 1, 13),
    _NbsEusmTgaInterPacketGap_Type()
)
nbsEusmTgaInterPacketGap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsEusmTgaInterPacketGap.setStatus("current")


class _NbsEusmTgaAction_Type(Integer32):
    """Custom type nbsEusmTgaAction based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notSupported", 1),
          ("start", 2),
          ("stop", 3))
    )


_NbsEusmTgaAction_Type.__name__ = "Integer32"
_NbsEusmTgaAction_Object = MibTableColumn
nbsEusmTgaAction = _NbsEusmTgaAction_Object(
    (1, 3, 6, 1, 4, 1, 629, 202, 3, 1, 1, 14),
    _NbsEusmTgaAction_Type()
)
nbsEusmTgaAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsEusmTgaAction.setStatus("current")
_NbsEusmCableTestTable_Object = MibTable
nbsEusmCableTestTable = _NbsEusmCableTestTable_Object(
    (1, 3, 6, 1, 4, 1, 629, 202, 3, 2)
)
if mibBuilder.loadTexts:
    nbsEusmCableTestTable.setStatus("current")
_NbsEusmCableTestEntry_Object = MibTableRow
nbsEusmCableTestEntry = _NbsEusmCableTestEntry_Object(
    (1, 3, 6, 1, 4, 1, 629, 202, 3, 2, 1)
)
if mibBuilder.loadTexts:
    nbsEusmCableTestEntry.setStatus("current")


class _NbsEusmCableTestStatus_Type(Integer32):
    """Custom type nbsEusmCableTestStatus based on Integer32"""
    defaultValue = 5

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
        *(("notSupported", 1),
          ("testCompleted", 4),
          ("testIdle", 5),
          ("testInProgress", 3),
          ("testStart", 2))
    )


_NbsEusmCableTestStatus_Type.__name__ = "Integer32"
_NbsEusmCableTestStatus_Object = MibTableColumn
nbsEusmCableTestStatus = _NbsEusmCableTestStatus_Object(
    (1, 3, 6, 1, 4, 1, 629, 202, 3, 2, 1, 1),
    _NbsEusmCableTestStatus_Type()
)
nbsEusmCableTestStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsEusmCableTestStatus.setStatus("current")
_NbsEusmCableTestResult_Type = DisplayString
_NbsEusmCableTestResult_Object = MibTableColumn
nbsEusmCableTestResult = _NbsEusmCableTestResult_Object(
    (1, 3, 6, 1, 4, 1, 629, 202, 3, 2, 1, 2),
    _NbsEusmCableTestResult_Type()
)
nbsEusmCableTestResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsEusmCableTestResult.setStatus("current")
_NbsEusmLgaTable_Object = MibTable
nbsEusmLgaTable = _NbsEusmLgaTable_Object(
    (1, 3, 6, 1, 4, 1, 629, 202, 3, 3)
)
if mibBuilder.loadTexts:
    nbsEusmLgaTable.setStatus("current")
_NbsEusmLgaEntry_Object = MibTableRow
nbsEusmLgaEntry = _NbsEusmLgaEntry_Object(
    (1, 3, 6, 1, 4, 1, 629, 202, 3, 3, 1)
)
if mibBuilder.loadTexts:
    nbsEusmLgaEntry.setStatus("current")


class _NbsEusmLgaRdAllFrames_Type(Integer32):
    """Custom type nbsEusmLgaRdAllFrames based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_NbsEusmLgaRdAllFrames_Type.__name__ = "Integer32"
_NbsEusmLgaRdAllFrames_Object = MibTableColumn
nbsEusmLgaRdAllFrames = _NbsEusmLgaRdAllFrames_Object(
    (1, 3, 6, 1, 4, 1, 629, 202, 3, 3, 1, 1),
    _NbsEusmLgaRdAllFrames_Type()
)
nbsEusmLgaRdAllFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsEusmLgaRdAllFrames.setStatus("current")


class _NbsEusmLgaRducFrames_Type(Integer32):
    """Custom type nbsEusmLgaRducFrames based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_NbsEusmLgaRducFrames_Type.__name__ = "Integer32"
_NbsEusmLgaRducFrames_Object = MibTableColumn
nbsEusmLgaRducFrames = _NbsEusmLgaRducFrames_Object(
    (1, 3, 6, 1, 4, 1, 629, 202, 3, 3, 1, 2),
    _NbsEusmLgaRducFrames_Type()
)
nbsEusmLgaRducFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsEusmLgaRducFrames.setStatus("current")


class _NbsEusmLgaRdmcFrames_Type(Integer32):
    """Custom type nbsEusmLgaRdmcFrames based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_NbsEusmLgaRdmcFrames_Type.__name__ = "Integer32"
_NbsEusmLgaRdmcFrames_Object = MibTableColumn
nbsEusmLgaRdmcFrames = _NbsEusmLgaRdmcFrames_Object(
    (1, 3, 6, 1, 4, 1, 629, 202, 3, 3, 1, 3),
    _NbsEusmLgaRdmcFrames_Type()
)
nbsEusmLgaRdmcFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsEusmLgaRdmcFrames.setStatus("current")


class _NbsEusmLgaRdbcFrames_Type(Integer32):
    """Custom type nbsEusmLgaRdbcFrames based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_NbsEusmLgaRdbcFrames_Type.__name__ = "Integer32"
_NbsEusmLgaRdbcFrames_Object = MibTableColumn
nbsEusmLgaRdbcFrames = _NbsEusmLgaRdbcFrames_Object(
    (1, 3, 6, 1, 4, 1, 629, 202, 3, 3, 1, 4),
    _NbsEusmLgaRdbcFrames_Type()
)
nbsEusmLgaRdbcFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsEusmLgaRdbcFrames.setStatus("current")


class _NbsEusmLgaRdSize64_Type(Integer32):
    """Custom type nbsEusmLgaRdSize64 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_NbsEusmLgaRdSize64_Type.__name__ = "Integer32"
_NbsEusmLgaRdSize64_Object = MibTableColumn
nbsEusmLgaRdSize64 = _NbsEusmLgaRdSize64_Object(
    (1, 3, 6, 1, 4, 1, 629, 202, 3, 3, 1, 5),
    _NbsEusmLgaRdSize64_Type()
)
nbsEusmLgaRdSize64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsEusmLgaRdSize64.setStatus("current")


class _NbsEusmLgaRdSizeMax127_Type(Integer32):
    """Custom type nbsEusmLgaRdSizeMax127 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_NbsEusmLgaRdSizeMax127_Type.__name__ = "Integer32"
_NbsEusmLgaRdSizeMax127_Object = MibTableColumn
nbsEusmLgaRdSizeMax127 = _NbsEusmLgaRdSizeMax127_Object(
    (1, 3, 6, 1, 4, 1, 629, 202, 3, 3, 1, 6),
    _NbsEusmLgaRdSizeMax127_Type()
)
nbsEusmLgaRdSizeMax127.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsEusmLgaRdSizeMax127.setStatus("current")


class _NbsEusmLgaRdSizeMax255_Type(Integer32):
    """Custom type nbsEusmLgaRdSizeMax255 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_NbsEusmLgaRdSizeMax255_Type.__name__ = "Integer32"
_NbsEusmLgaRdSizeMax255_Object = MibTableColumn
nbsEusmLgaRdSizeMax255 = _NbsEusmLgaRdSizeMax255_Object(
    (1, 3, 6, 1, 4, 1, 629, 202, 3, 3, 1, 7),
    _NbsEusmLgaRdSizeMax255_Type()
)
nbsEusmLgaRdSizeMax255.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsEusmLgaRdSizeMax255.setStatus("current")


class _NbsEusmLgaRdSizeMax511_Type(Integer32):
    """Custom type nbsEusmLgaRdSizeMax511 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_NbsEusmLgaRdSizeMax511_Type.__name__ = "Integer32"
_NbsEusmLgaRdSizeMax511_Object = MibTableColumn
nbsEusmLgaRdSizeMax511 = _NbsEusmLgaRdSizeMax511_Object(
    (1, 3, 6, 1, 4, 1, 629, 202, 3, 3, 1, 8),
    _NbsEusmLgaRdSizeMax511_Type()
)
nbsEusmLgaRdSizeMax511.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsEusmLgaRdSizeMax511.setStatus("current")


class _NbsEusmLgaRdSizeMax1023_Type(Integer32):
    """Custom type nbsEusmLgaRdSizeMax1023 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_NbsEusmLgaRdSizeMax1023_Type.__name__ = "Integer32"
_NbsEusmLgaRdSizeMax1023_Object = MibTableColumn
nbsEusmLgaRdSizeMax1023 = _NbsEusmLgaRdSizeMax1023_Object(
    (1, 3, 6, 1, 4, 1, 629, 202, 3, 3, 1, 9),
    _NbsEusmLgaRdSizeMax1023_Type()
)
nbsEusmLgaRdSizeMax1023.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsEusmLgaRdSizeMax1023.setStatus("current")


class _NbsEusmLgaRdSizeMax1518_Type(Integer32):
    """Custom type nbsEusmLgaRdSizeMax1518 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_NbsEusmLgaRdSizeMax1518_Type.__name__ = "Integer32"
_NbsEusmLgaRdSizeMax1518_Object = MibTableColumn
nbsEusmLgaRdSizeMax1518 = _NbsEusmLgaRdSizeMax1518_Object(
    (1, 3, 6, 1, 4, 1, 629, 202, 3, 3, 1, 10),
    _NbsEusmLgaRdSizeMax1518_Type()
)
nbsEusmLgaRdSizeMax1518.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsEusmLgaRdSizeMax1518.setStatus("current")


class _NbsEusmLgaRdSizeMax2047_Type(Integer32):
    """Custom type nbsEusmLgaRdSizeMax2047 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_NbsEusmLgaRdSizeMax2047_Type.__name__ = "Integer32"
_NbsEusmLgaRdSizeMax2047_Object = MibTableColumn
nbsEusmLgaRdSizeMax2047 = _NbsEusmLgaRdSizeMax2047_Object(
    (1, 3, 6, 1, 4, 1, 629, 202, 3, 3, 1, 11),
    _NbsEusmLgaRdSizeMax2047_Type()
)
nbsEusmLgaRdSizeMax2047.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsEusmLgaRdSizeMax2047.setStatus("current")


class _NbsEusmLgaRdSizeOvr2047_Type(Integer32):
    """Custom type nbsEusmLgaRdSizeOvr2047 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_NbsEusmLgaRdSizeOvr2047_Type.__name__ = "Integer32"
_NbsEusmLgaRdSizeOvr2047_Object = MibTableColumn
nbsEusmLgaRdSizeOvr2047 = _NbsEusmLgaRdSizeOvr2047_Object(
    (1, 3, 6, 1, 4, 1, 629, 202, 3, 3, 1, 12),
    _NbsEusmLgaRdSizeOvr2047_Type()
)
nbsEusmLgaRdSizeOvr2047.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsEusmLgaRdSizeOvr2047.setStatus("current")
_NbsEusmLgaRdFrameDivisor_Type = Unsigned32
_NbsEusmLgaRdFrameDivisor_Object = MibTableColumn
nbsEusmLgaRdFrameDivisor = _NbsEusmLgaRdFrameDivisor_Object(
    (1, 3, 6, 1, 4, 1, 629, 202, 3, 3, 1, 13),
    _NbsEusmLgaRdFrameDivisor_Type()
)
nbsEusmLgaRdFrameDivisor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsEusmLgaRdFrameDivisor.setStatus("current")


class _NbsEusmLgaRdAllOctets_Type(Integer32):
    """Custom type nbsEusmLgaRdAllOctets based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_NbsEusmLgaRdAllOctets_Type.__name__ = "Integer32"
_NbsEusmLgaRdAllOctets_Object = MibTableColumn
nbsEusmLgaRdAllOctets = _NbsEusmLgaRdAllOctets_Object(
    (1, 3, 6, 1, 4, 1, 629, 202, 3, 3, 1, 14),
    _NbsEusmLgaRdAllOctets_Type()
)
nbsEusmLgaRdAllOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsEusmLgaRdAllOctets.setStatus("current")
_NbsEusmLgaRdOctetDivisor_Type = Unsigned32
_NbsEusmLgaRdOctetDivisor_Object = MibTableColumn
nbsEusmLgaRdOctetDivisor = _NbsEusmLgaRdOctetDivisor_Object(
    (1, 3, 6, 1, 4, 1, 629, 202, 3, 3, 1, 15),
    _NbsEusmLgaRdOctetDivisor_Type()
)
nbsEusmLgaRdOctetDivisor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsEusmLgaRdOctetDivisor.setStatus("current")
_NbsEusmLgaRdTimeSpan_Type = Unsigned32
_NbsEusmLgaRdTimeSpan_Object = MibTableColumn
nbsEusmLgaRdTimeSpan = _NbsEusmLgaRdTimeSpan_Object(
    (1, 3, 6, 1, 4, 1, 629, 202, 3, 3, 1, 16),
    _NbsEusmLgaRdTimeSpan_Type()
)
nbsEusmLgaRdTimeSpan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsEusmLgaRdTimeSpan.setStatus("current")


class _NbsEusmLgaAdAllFrames_Type(Integer32):
    """Custom type nbsEusmLgaAdAllFrames based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_NbsEusmLgaAdAllFrames_Type.__name__ = "Integer32"
_NbsEusmLgaAdAllFrames_Object = MibTableColumn
nbsEusmLgaAdAllFrames = _NbsEusmLgaAdAllFrames_Object(
    (1, 3, 6, 1, 4, 1, 629, 202, 3, 3, 1, 17),
    _NbsEusmLgaAdAllFrames_Type()
)
nbsEusmLgaAdAllFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsEusmLgaAdAllFrames.setStatus("current")


class _NbsEusmLgaAducFrames_Type(Integer32):
    """Custom type nbsEusmLgaAducFrames based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_NbsEusmLgaAducFrames_Type.__name__ = "Integer32"
_NbsEusmLgaAducFrames_Object = MibTableColumn
nbsEusmLgaAducFrames = _NbsEusmLgaAducFrames_Object(
    (1, 3, 6, 1, 4, 1, 629, 202, 3, 3, 1, 18),
    _NbsEusmLgaAducFrames_Type()
)
nbsEusmLgaAducFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsEusmLgaAducFrames.setStatus("current")


class _NbsEusmLgaAdmcFrames_Type(Integer32):
    """Custom type nbsEusmLgaAdmcFrames based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_NbsEusmLgaAdmcFrames_Type.__name__ = "Integer32"
_NbsEusmLgaAdmcFrames_Object = MibTableColumn
nbsEusmLgaAdmcFrames = _NbsEusmLgaAdmcFrames_Object(
    (1, 3, 6, 1, 4, 1, 629, 202, 3, 3, 1, 19),
    _NbsEusmLgaAdmcFrames_Type()
)
nbsEusmLgaAdmcFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsEusmLgaAdmcFrames.setStatus("current")


class _NbsEusmLgaAdbcFrames_Type(Integer32):
    """Custom type nbsEusmLgaAdbcFrames based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_NbsEusmLgaAdbcFrames_Type.__name__ = "Integer32"
_NbsEusmLgaAdbcFrames_Object = MibTableColumn
nbsEusmLgaAdbcFrames = _NbsEusmLgaAdbcFrames_Object(
    (1, 3, 6, 1, 4, 1, 629, 202, 3, 3, 1, 20),
    _NbsEusmLgaAdbcFrames_Type()
)
nbsEusmLgaAdbcFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsEusmLgaAdbcFrames.setStatus("current")


class _NbsEusmLgaAdSize64_Type(Integer32):
    """Custom type nbsEusmLgaAdSize64 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_NbsEusmLgaAdSize64_Type.__name__ = "Integer32"
_NbsEusmLgaAdSize64_Object = MibTableColumn
nbsEusmLgaAdSize64 = _NbsEusmLgaAdSize64_Object(
    (1, 3, 6, 1, 4, 1, 629, 202, 3, 3, 1, 21),
    _NbsEusmLgaAdSize64_Type()
)
nbsEusmLgaAdSize64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsEusmLgaAdSize64.setStatus("current")


class _NbsEusmLgaAdSizeMax127_Type(Integer32):
    """Custom type nbsEusmLgaAdSizeMax127 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_NbsEusmLgaAdSizeMax127_Type.__name__ = "Integer32"
_NbsEusmLgaAdSizeMax127_Object = MibTableColumn
nbsEusmLgaAdSizeMax127 = _NbsEusmLgaAdSizeMax127_Object(
    (1, 3, 6, 1, 4, 1, 629, 202, 3, 3, 1, 22),
    _NbsEusmLgaAdSizeMax127_Type()
)
nbsEusmLgaAdSizeMax127.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsEusmLgaAdSizeMax127.setStatus("current")


class _NbsEusmLgaAdSizeMax255_Type(Integer32):
    """Custom type nbsEusmLgaAdSizeMax255 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_NbsEusmLgaAdSizeMax255_Type.__name__ = "Integer32"
_NbsEusmLgaAdSizeMax255_Object = MibTableColumn
nbsEusmLgaAdSizeMax255 = _NbsEusmLgaAdSizeMax255_Object(
    (1, 3, 6, 1, 4, 1, 629, 202, 3, 3, 1, 23),
    _NbsEusmLgaAdSizeMax255_Type()
)
nbsEusmLgaAdSizeMax255.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsEusmLgaAdSizeMax255.setStatus("current")


class _NbsEusmLgaAdSizeMax511_Type(Integer32):
    """Custom type nbsEusmLgaAdSizeMax511 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_NbsEusmLgaAdSizeMax511_Type.__name__ = "Integer32"
_NbsEusmLgaAdSizeMax511_Object = MibTableColumn
nbsEusmLgaAdSizeMax511 = _NbsEusmLgaAdSizeMax511_Object(
    (1, 3, 6, 1, 4, 1, 629, 202, 3, 3, 1, 24),
    _NbsEusmLgaAdSizeMax511_Type()
)
nbsEusmLgaAdSizeMax511.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsEusmLgaAdSizeMax511.setStatus("current")


class _NbsEusmLgaAdSizeMax1023_Type(Integer32):
    """Custom type nbsEusmLgaAdSizeMax1023 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_NbsEusmLgaAdSizeMax1023_Type.__name__ = "Integer32"
_NbsEusmLgaAdSizeMax1023_Object = MibTableColumn
nbsEusmLgaAdSizeMax1023 = _NbsEusmLgaAdSizeMax1023_Object(
    (1, 3, 6, 1, 4, 1, 629, 202, 3, 3, 1, 25),
    _NbsEusmLgaAdSizeMax1023_Type()
)
nbsEusmLgaAdSizeMax1023.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsEusmLgaAdSizeMax1023.setStatus("current")


class _NbsEusmLgaAdSizeMax1518_Type(Integer32):
    """Custom type nbsEusmLgaAdSizeMax1518 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_NbsEusmLgaAdSizeMax1518_Type.__name__ = "Integer32"
_NbsEusmLgaAdSizeMax1518_Object = MibTableColumn
nbsEusmLgaAdSizeMax1518 = _NbsEusmLgaAdSizeMax1518_Object(
    (1, 3, 6, 1, 4, 1, 629, 202, 3, 3, 1, 26),
    _NbsEusmLgaAdSizeMax1518_Type()
)
nbsEusmLgaAdSizeMax1518.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsEusmLgaAdSizeMax1518.setStatus("current")


class _NbsEusmLgaAdSizeMax2047_Type(Integer32):
    """Custom type nbsEusmLgaAdSizeMax2047 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_NbsEusmLgaAdSizeMax2047_Type.__name__ = "Integer32"
_NbsEusmLgaAdSizeMax2047_Object = MibTableColumn
nbsEusmLgaAdSizeMax2047 = _NbsEusmLgaAdSizeMax2047_Object(
    (1, 3, 6, 1, 4, 1, 629, 202, 3, 3, 1, 27),
    _NbsEusmLgaAdSizeMax2047_Type()
)
nbsEusmLgaAdSizeMax2047.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsEusmLgaAdSizeMax2047.setStatus("current")


class _NbsEusmLgaAdSizeOvr2047_Type(Integer32):
    """Custom type nbsEusmLgaAdSizeOvr2047 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_NbsEusmLgaAdSizeOvr2047_Type.__name__ = "Integer32"
_NbsEusmLgaAdSizeOvr2047_Object = MibTableColumn
nbsEusmLgaAdSizeOvr2047 = _NbsEusmLgaAdSizeOvr2047_Object(
    (1, 3, 6, 1, 4, 1, 629, 202, 3, 3, 1, 28),
    _NbsEusmLgaAdSizeOvr2047_Type()
)
nbsEusmLgaAdSizeOvr2047.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsEusmLgaAdSizeOvr2047.setStatus("current")
_NbsEusmLgaAdFrameDivisor_Type = Unsigned32
_NbsEusmLgaAdFrameDivisor_Object = MibTableColumn
nbsEusmLgaAdFrameDivisor = _NbsEusmLgaAdFrameDivisor_Object(
    (1, 3, 6, 1, 4, 1, 629, 202, 3, 3, 1, 29),
    _NbsEusmLgaAdFrameDivisor_Type()
)
nbsEusmLgaAdFrameDivisor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsEusmLgaAdFrameDivisor.setStatus("current")


class _NbsEusmLgaAdAllOctets_Type(Integer32):
    """Custom type nbsEusmLgaAdAllOctets based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_NbsEusmLgaAdAllOctets_Type.__name__ = "Integer32"
_NbsEusmLgaAdAllOctets_Object = MibTableColumn
nbsEusmLgaAdAllOctets = _NbsEusmLgaAdAllOctets_Object(
    (1, 3, 6, 1, 4, 1, 629, 202, 3, 3, 1, 30),
    _NbsEusmLgaAdAllOctets_Type()
)
nbsEusmLgaAdAllOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsEusmLgaAdAllOctets.setStatus("current")
_NbsEusmLgaAdOctetDivisor_Type = Unsigned32
_NbsEusmLgaAdOctetDivisor_Object = MibTableColumn
nbsEusmLgaAdOctetDivisor = _NbsEusmLgaAdOctetDivisor_Object(
    (1, 3, 6, 1, 4, 1, 629, 202, 3, 3, 1, 31),
    _NbsEusmLgaAdOctetDivisor_Type()
)
nbsEusmLgaAdOctetDivisor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsEusmLgaAdOctetDivisor.setStatus("current")
_NbsEusmLgaAdTimeSpan_Type = Unsigned32
_NbsEusmLgaAdTimeSpan_Object = MibTableColumn
nbsEusmLgaAdTimeSpan = _NbsEusmLgaAdTimeSpan_Object(
    (1, 3, 6, 1, 4, 1, 629, 202, 3, 3, 1, 32),
    _NbsEusmLgaAdTimeSpan_Type()
)
nbsEusmLgaAdTimeSpan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsEusmLgaAdTimeSpan.setStatus("current")


class _NbsEusmSlotLgaInterval_Type(Integer32):
    """Custom type nbsEusmSlotLgaInterval based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 86400),
    )


_NbsEusmSlotLgaInterval_Type.__name__ = "Integer32"
_NbsEusmSlotLgaInterval_Object = MibTableColumn
nbsEusmSlotLgaInterval = _NbsEusmSlotLgaInterval_Object(
    (1, 3, 6, 1, 4, 1, 629, 202, 3, 3, 1, 33),
    _NbsEusmSlotLgaInterval_Type()
)
nbsEusmSlotLgaInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsEusmSlotLgaInterval.setStatus("current")


class _NbsEusmSlotLgaAction_Type(Integer32):
    """Custom type nbsEusmSlotLgaAction based on Integer32"""
    defaultValue = 1

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
        *(("inProgress", 5),
          ("inactive", 2),
          ("notSupported", 1),
          ("start", 3),
          ("stop", 4))
    )


_NbsEusmSlotLgaAction_Type.__name__ = "Integer32"
_NbsEusmSlotLgaAction_Object = MibTableColumn
nbsEusmSlotLgaAction = _NbsEusmSlotLgaAction_Object(
    (1, 3, 6, 1, 4, 1, 629, 202, 3, 3, 1, 34),
    _NbsEusmSlotLgaAction_Type()
)
nbsEusmSlotLgaAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsEusmSlotLgaAction.setStatus("current")
_NbsEusmPmTable_Object = MibTable
nbsEusmPmTable = _NbsEusmPmTable_Object(
    (1, 3, 6, 1, 4, 1, 629, 202, 3, 4)
)
if mibBuilder.loadTexts:
    nbsEusmPmTable.setStatus("current")
_NbsEusmPmEntry_Object = MibTableRow
nbsEusmPmEntry = _NbsEusmPmEntry_Object(
    (1, 3, 6, 1, 4, 1, 629, 202, 3, 4, 1)
)
if mibBuilder.loadTexts:
    nbsEusmPmEntry.setStatus("current")
_NbsEusmPmAvgAllSizes_Type = Counter32
_NbsEusmPmAvgAllSizes_Object = MibTableColumn
nbsEusmPmAvgAllSizes = _NbsEusmPmAvgAllSizes_Object(
    (1, 3, 6, 1, 4, 1, 629, 202, 3, 4, 1, 1),
    _NbsEusmPmAvgAllSizes_Type()
)
nbsEusmPmAvgAllSizes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsEusmPmAvgAllSizes.setStatus("current")
_NbsEusmPmAvg64_Type = Counter32
_NbsEusmPmAvg64_Object = MibTableColumn
nbsEusmPmAvg64 = _NbsEusmPmAvg64_Object(
    (1, 3, 6, 1, 4, 1, 629, 202, 3, 4, 1, 2),
    _NbsEusmPmAvg64_Type()
)
nbsEusmPmAvg64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsEusmPmAvg64.setStatus("current")
_NbsEusmPmAvg127_Type = Counter32
_NbsEusmPmAvg127_Object = MibTableColumn
nbsEusmPmAvg127 = _NbsEusmPmAvg127_Object(
    (1, 3, 6, 1, 4, 1, 629, 202, 3, 4, 1, 3),
    _NbsEusmPmAvg127_Type()
)
nbsEusmPmAvg127.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsEusmPmAvg127.setStatus("current")
_NbsEusmPmAvg255_Type = Counter32
_NbsEusmPmAvg255_Object = MibTableColumn
nbsEusmPmAvg255 = _NbsEusmPmAvg255_Object(
    (1, 3, 6, 1, 4, 1, 629, 202, 3, 4, 1, 4),
    _NbsEusmPmAvg255_Type()
)
nbsEusmPmAvg255.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsEusmPmAvg255.setStatus("current")
_NbsEusmPmAvg511_Type = Counter32
_NbsEusmPmAvg511_Object = MibTableColumn
nbsEusmPmAvg511 = _NbsEusmPmAvg511_Object(
    (1, 3, 6, 1, 4, 1, 629, 202, 3, 4, 1, 5),
    _NbsEusmPmAvg511_Type()
)
nbsEusmPmAvg511.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsEusmPmAvg511.setStatus("current")
_NbsEusmPmAvg1023_Type = Counter32
_NbsEusmPmAvg1023_Object = MibTableColumn
nbsEusmPmAvg1023 = _NbsEusmPmAvg1023_Object(
    (1, 3, 6, 1, 4, 1, 629, 202, 3, 4, 1, 6),
    _NbsEusmPmAvg1023_Type()
)
nbsEusmPmAvg1023.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsEusmPmAvg1023.setStatus("current")
_NbsEusmPmAvg1518_Type = Counter32
_NbsEusmPmAvg1518_Object = MibTableColumn
nbsEusmPmAvg1518 = _NbsEusmPmAvg1518_Object(
    (1, 3, 6, 1, 4, 1, 629, 202, 3, 4, 1, 7),
    _NbsEusmPmAvg1518_Type()
)
nbsEusmPmAvg1518.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsEusmPmAvg1518.setStatus("current")
_NbsEusmPmAvg2047_Type = Counter32
_NbsEusmPmAvg2047_Object = MibTableColumn
nbsEusmPmAvg2047 = _NbsEusmPmAvg2047_Object(
    (1, 3, 6, 1, 4, 1, 629, 202, 3, 4, 1, 8),
    _NbsEusmPmAvg2047_Type()
)
nbsEusmPmAvg2047.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsEusmPmAvg2047.setStatus("current")
_NbsEusmPmAvgOvr2047_Type = Counter32
_NbsEusmPmAvgOvr2047_Object = MibTableColumn
nbsEusmPmAvgOvr2047 = _NbsEusmPmAvgOvr2047_Object(
    (1, 3, 6, 1, 4, 1, 629, 202, 3, 4, 1, 9),
    _NbsEusmPmAvgOvr2047_Type()
)
nbsEusmPmAvgOvr2047.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsEusmPmAvgOvr2047.setStatus("current")
_NbsEusmPmMinAllSizes_Type = Counter32
_NbsEusmPmMinAllSizes_Object = MibTableColumn
nbsEusmPmMinAllSizes = _NbsEusmPmMinAllSizes_Object(
    (1, 3, 6, 1, 4, 1, 629, 202, 3, 4, 1, 10),
    _NbsEusmPmMinAllSizes_Type()
)
nbsEusmPmMinAllSizes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsEusmPmMinAllSizes.setStatus("current")
_NbsEusmPmMin64_Type = Counter32
_NbsEusmPmMin64_Object = MibTableColumn
nbsEusmPmMin64 = _NbsEusmPmMin64_Object(
    (1, 3, 6, 1, 4, 1, 629, 202, 3, 4, 1, 11),
    _NbsEusmPmMin64_Type()
)
nbsEusmPmMin64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsEusmPmMin64.setStatus("current")
_NbsEusmPmMin127_Type = Counter32
_NbsEusmPmMin127_Object = MibTableColumn
nbsEusmPmMin127 = _NbsEusmPmMin127_Object(
    (1, 3, 6, 1, 4, 1, 629, 202, 3, 4, 1, 12),
    _NbsEusmPmMin127_Type()
)
nbsEusmPmMin127.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsEusmPmMin127.setStatus("current")
_NbsEusmPmMin255_Type = Counter32
_NbsEusmPmMin255_Object = MibTableColumn
nbsEusmPmMin255 = _NbsEusmPmMin255_Object(
    (1, 3, 6, 1, 4, 1, 629, 202, 3, 4, 1, 13),
    _NbsEusmPmMin255_Type()
)
nbsEusmPmMin255.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsEusmPmMin255.setStatus("current")
_NbsEusmPmMin511_Type = Counter32
_NbsEusmPmMin511_Object = MibTableColumn
nbsEusmPmMin511 = _NbsEusmPmMin511_Object(
    (1, 3, 6, 1, 4, 1, 629, 202, 3, 4, 1, 14),
    _NbsEusmPmMin511_Type()
)
nbsEusmPmMin511.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsEusmPmMin511.setStatus("current")
_NbsEusmPmMin1023_Type = Counter32
_NbsEusmPmMin1023_Object = MibTableColumn
nbsEusmPmMin1023 = _NbsEusmPmMin1023_Object(
    (1, 3, 6, 1, 4, 1, 629, 202, 3, 4, 1, 15),
    _NbsEusmPmMin1023_Type()
)
nbsEusmPmMin1023.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsEusmPmMin1023.setStatus("current")
_NbsEusmPmMin1518_Type = Counter32
_NbsEusmPmMin1518_Object = MibTableColumn
nbsEusmPmMin1518 = _NbsEusmPmMin1518_Object(
    (1, 3, 6, 1, 4, 1, 629, 202, 3, 4, 1, 16),
    _NbsEusmPmMin1518_Type()
)
nbsEusmPmMin1518.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsEusmPmMin1518.setStatus("current")
_NbsEusmPmMin2047_Type = Counter32
_NbsEusmPmMin2047_Object = MibTableColumn
nbsEusmPmMin2047 = _NbsEusmPmMin2047_Object(
    (1, 3, 6, 1, 4, 1, 629, 202, 3, 4, 1, 17),
    _NbsEusmPmMin2047_Type()
)
nbsEusmPmMin2047.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsEusmPmMin2047.setStatus("current")
_NbsEusmPmMinOvr2047_Type = Counter32
_NbsEusmPmMinOvr2047_Object = MibTableColumn
nbsEusmPmMinOvr2047 = _NbsEusmPmMinOvr2047_Object(
    (1, 3, 6, 1, 4, 1, 629, 202, 3, 4, 1, 18),
    _NbsEusmPmMinOvr2047_Type()
)
nbsEusmPmMinOvr2047.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsEusmPmMinOvr2047.setStatus("current")
_NbsEusmPmMaxAllSizes_Type = Counter32
_NbsEusmPmMaxAllSizes_Object = MibTableColumn
nbsEusmPmMaxAllSizes = _NbsEusmPmMaxAllSizes_Object(
    (1, 3, 6, 1, 4, 1, 629, 202, 3, 4, 1, 19),
    _NbsEusmPmMaxAllSizes_Type()
)
nbsEusmPmMaxAllSizes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsEusmPmMaxAllSizes.setStatus("current")
_NbsEusmPmMax64_Type = Counter32
_NbsEusmPmMax64_Object = MibTableColumn
nbsEusmPmMax64 = _NbsEusmPmMax64_Object(
    (1, 3, 6, 1, 4, 1, 629, 202, 3, 4, 1, 20),
    _NbsEusmPmMax64_Type()
)
nbsEusmPmMax64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsEusmPmMax64.setStatus("current")
_NbsEusmPmMax127_Type = Counter32
_NbsEusmPmMax127_Object = MibTableColumn
nbsEusmPmMax127 = _NbsEusmPmMax127_Object(
    (1, 3, 6, 1, 4, 1, 629, 202, 3, 4, 1, 21),
    _NbsEusmPmMax127_Type()
)
nbsEusmPmMax127.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsEusmPmMax127.setStatus("current")
_NbsEusmPmMax255_Type = Counter32
_NbsEusmPmMax255_Object = MibTableColumn
nbsEusmPmMax255 = _NbsEusmPmMax255_Object(
    (1, 3, 6, 1, 4, 1, 629, 202, 3, 4, 1, 22),
    _NbsEusmPmMax255_Type()
)
nbsEusmPmMax255.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsEusmPmMax255.setStatus("current")
_NbsEusmPmMax511_Type = Counter32
_NbsEusmPmMax511_Object = MibTableColumn
nbsEusmPmMax511 = _NbsEusmPmMax511_Object(
    (1, 3, 6, 1, 4, 1, 629, 202, 3, 4, 1, 23),
    _NbsEusmPmMax511_Type()
)
nbsEusmPmMax511.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsEusmPmMax511.setStatus("current")
_NbsEusmPmMax1023_Type = Counter32
_NbsEusmPmMax1023_Object = MibTableColumn
nbsEusmPmMax1023 = _NbsEusmPmMax1023_Object(
    (1, 3, 6, 1, 4, 1, 629, 202, 3, 4, 1, 24),
    _NbsEusmPmMax1023_Type()
)
nbsEusmPmMax1023.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsEusmPmMax1023.setStatus("current")
_NbsEusmPmMax1518_Type = Counter32
_NbsEusmPmMax1518_Object = MibTableColumn
nbsEusmPmMax1518 = _NbsEusmPmMax1518_Object(
    (1, 3, 6, 1, 4, 1, 629, 202, 3, 4, 1, 25),
    _NbsEusmPmMax1518_Type()
)
nbsEusmPmMax1518.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsEusmPmMax1518.setStatus("current")
_NbsEusmPmMax2047_Type = Counter32
_NbsEusmPmMax2047_Object = MibTableColumn
nbsEusmPmMax2047 = _NbsEusmPmMax2047_Object(
    (1, 3, 6, 1, 4, 1, 629, 202, 3, 4, 1, 26),
    _NbsEusmPmMax2047_Type()
)
nbsEusmPmMax2047.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsEusmPmMax2047.setStatus("current")
_NbsEusmPmMaxOvr2047_Type = Counter32
_NbsEusmPmMaxOvr2047_Object = MibTableColumn
nbsEusmPmMaxOvr2047 = _NbsEusmPmMaxOvr2047_Object(
    (1, 3, 6, 1, 4, 1, 629, 202, 3, 4, 1, 27),
    _NbsEusmPmMaxOvr2047_Type()
)
nbsEusmPmMaxOvr2047.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsEusmPmMaxOvr2047.setStatus("current")
_NbsEusmPmFramesAllSizes_Type = Counter64
_NbsEusmPmFramesAllSizes_Object = MibTableColumn
nbsEusmPmFramesAllSizes = _NbsEusmPmFramesAllSizes_Object(
    (1, 3, 6, 1, 4, 1, 629, 202, 3, 4, 1, 28),
    _NbsEusmPmFramesAllSizes_Type()
)
nbsEusmPmFramesAllSizes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsEusmPmFramesAllSizes.setStatus("current")
_NbsEusmPmFrames64_Type = Counter64
_NbsEusmPmFrames64_Object = MibTableColumn
nbsEusmPmFrames64 = _NbsEusmPmFrames64_Object(
    (1, 3, 6, 1, 4, 1, 629, 202, 3, 4, 1, 29),
    _NbsEusmPmFrames64_Type()
)
nbsEusmPmFrames64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsEusmPmFrames64.setStatus("current")
_NbsEusmPmFrames127_Type = Counter64
_NbsEusmPmFrames127_Object = MibTableColumn
nbsEusmPmFrames127 = _NbsEusmPmFrames127_Object(
    (1, 3, 6, 1, 4, 1, 629, 202, 3, 4, 1, 30),
    _NbsEusmPmFrames127_Type()
)
nbsEusmPmFrames127.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsEusmPmFrames127.setStatus("current")
_NbsEusmPmFrames255_Type = Counter64
_NbsEusmPmFrames255_Object = MibTableColumn
nbsEusmPmFrames255 = _NbsEusmPmFrames255_Object(
    (1, 3, 6, 1, 4, 1, 629, 202, 3, 4, 1, 31),
    _NbsEusmPmFrames255_Type()
)
nbsEusmPmFrames255.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsEusmPmFrames255.setStatus("current")
_NbsEusmPmFrames511_Type = Counter64
_NbsEusmPmFrames511_Object = MibTableColumn
nbsEusmPmFrames511 = _NbsEusmPmFrames511_Object(
    (1, 3, 6, 1, 4, 1, 629, 202, 3, 4, 1, 32),
    _NbsEusmPmFrames511_Type()
)
nbsEusmPmFrames511.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsEusmPmFrames511.setStatus("current")
_NbsEusmPmFrames1023_Type = Counter64
_NbsEusmPmFrames1023_Object = MibTableColumn
nbsEusmPmFrames1023 = _NbsEusmPmFrames1023_Object(
    (1, 3, 6, 1, 4, 1, 629, 202, 3, 4, 1, 33),
    _NbsEusmPmFrames1023_Type()
)
nbsEusmPmFrames1023.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsEusmPmFrames1023.setStatus("current")
_NbsEusmPmFrames1518_Type = Counter64
_NbsEusmPmFrames1518_Object = MibTableColumn
nbsEusmPmFrames1518 = _NbsEusmPmFrames1518_Object(
    (1, 3, 6, 1, 4, 1, 629, 202, 3, 4, 1, 34),
    _NbsEusmPmFrames1518_Type()
)
nbsEusmPmFrames1518.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsEusmPmFrames1518.setStatus("current")
_NbsEusmPmFrames2047_Type = Counter64
_NbsEusmPmFrames2047_Object = MibTableColumn
nbsEusmPmFrames2047 = _NbsEusmPmFrames2047_Object(
    (1, 3, 6, 1, 4, 1, 629, 202, 3, 4, 1, 35),
    _NbsEusmPmFrames2047_Type()
)
nbsEusmPmFrames2047.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsEusmPmFrames2047.setStatus("current")
_NbsEusmPmFramesOvr2047_Type = Counter64
_NbsEusmPmFramesOvr2047_Object = MibTableColumn
nbsEusmPmFramesOvr2047 = _NbsEusmPmFramesOvr2047_Object(
    (1, 3, 6, 1, 4, 1, 629, 202, 3, 4, 1, 36),
    _NbsEusmPmFramesOvr2047_Type()
)
nbsEusmPmFramesOvr2047.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsEusmPmFramesOvr2047.setStatus("current")
_NbsEusmPmOctetsAllSizes_Type = Counter64
_NbsEusmPmOctetsAllSizes_Object = MibTableColumn
nbsEusmPmOctetsAllSizes = _NbsEusmPmOctetsAllSizes_Object(
    (1, 3, 6, 1, 4, 1, 629, 202, 3, 4, 1, 37),
    _NbsEusmPmOctetsAllSizes_Type()
)
nbsEusmPmOctetsAllSizes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsEusmPmOctetsAllSizes.setStatus("current")
_NbsEusmPmOctets64_Type = Counter64
_NbsEusmPmOctets64_Object = MibTableColumn
nbsEusmPmOctets64 = _NbsEusmPmOctets64_Object(
    (1, 3, 6, 1, 4, 1, 629, 202, 3, 4, 1, 38),
    _NbsEusmPmOctets64_Type()
)
nbsEusmPmOctets64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsEusmPmOctets64.setStatus("current")
_NbsEusmPmOctets127_Type = Counter64
_NbsEusmPmOctets127_Object = MibTableColumn
nbsEusmPmOctets127 = _NbsEusmPmOctets127_Object(
    (1, 3, 6, 1, 4, 1, 629, 202, 3, 4, 1, 39),
    _NbsEusmPmOctets127_Type()
)
nbsEusmPmOctets127.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsEusmPmOctets127.setStatus("current")
_NbsEusmPmOctets255_Type = Counter64
_NbsEusmPmOctets255_Object = MibTableColumn
nbsEusmPmOctets255 = _NbsEusmPmOctets255_Object(
    (1, 3, 6, 1, 4, 1, 629, 202, 3, 4, 1, 40),
    _NbsEusmPmOctets255_Type()
)
nbsEusmPmOctets255.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsEusmPmOctets255.setStatus("current")
_NbsEusmPmOctets511_Type = Counter64
_NbsEusmPmOctets511_Object = MibTableColumn
nbsEusmPmOctets511 = _NbsEusmPmOctets511_Object(
    (1, 3, 6, 1, 4, 1, 629, 202, 3, 4, 1, 41),
    _NbsEusmPmOctets511_Type()
)
nbsEusmPmOctets511.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsEusmPmOctets511.setStatus("current")
_NbsEusmPmOctets1023_Type = Counter64
_NbsEusmPmOctets1023_Object = MibTableColumn
nbsEusmPmOctets1023 = _NbsEusmPmOctets1023_Object(
    (1, 3, 6, 1, 4, 1, 629, 202, 3, 4, 1, 42),
    _NbsEusmPmOctets1023_Type()
)
nbsEusmPmOctets1023.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsEusmPmOctets1023.setStatus("current")
_NbsEusmPmOctets1518_Type = Counter64
_NbsEusmPmOctets1518_Object = MibTableColumn
nbsEusmPmOctets1518 = _NbsEusmPmOctets1518_Object(
    (1, 3, 6, 1, 4, 1, 629, 202, 3, 4, 1, 43),
    _NbsEusmPmOctets1518_Type()
)
nbsEusmPmOctets1518.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsEusmPmOctets1518.setStatus("current")
_NbsEusmPmOctets2047_Type = Counter64
_NbsEusmPmOctets2047_Object = MibTableColumn
nbsEusmPmOctets2047 = _NbsEusmPmOctets2047_Object(
    (1, 3, 6, 1, 4, 1, 629, 202, 3, 4, 1, 44),
    _NbsEusmPmOctets2047_Type()
)
nbsEusmPmOctets2047.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsEusmPmOctets2047.setStatus("current")
_NbsEusmPmOctetsOvr2047_Type = Counter64
_NbsEusmPmOctetsOvr2047_Object = MibTableColumn
nbsEusmPmOctetsOvr2047 = _NbsEusmPmOctetsOvr2047_Object(
    (1, 3, 6, 1, 4, 1, 629, 202, 3, 4, 1, 45),
    _NbsEusmPmOctetsOvr2047_Type()
)
nbsEusmPmOctetsOvr2047.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsEusmPmOctetsOvr2047.setStatus("current")


class _NbsEusmSlotPmInterval_Type(Integer32):
    """Custom type nbsEusmSlotPmInterval based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 604800),
    )


_NbsEusmSlotPmInterval_Type.__name__ = "Integer32"
_NbsEusmSlotPmInterval_Object = MibTableColumn
nbsEusmSlotPmInterval = _NbsEusmSlotPmInterval_Object(
    (1, 3, 6, 1, 4, 1, 629, 202, 3, 4, 1, 46),
    _NbsEusmSlotPmInterval_Type()
)
nbsEusmSlotPmInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsEusmSlotPmInterval.setStatus("current")


class _NbsEusmSlotPmSelector_Type(Integer32):
    """Custom type nbsEusmSlotPmSelector based on Integer32"""
    defaultValue = 1

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
        *(("coToCpe", 2),
          ("cpeRx", 5),
          ("cpeToCo", 3),
          ("cpeTx", 4),
          ("notSupported", 1))
    )


_NbsEusmSlotPmSelector_Type.__name__ = "Integer32"
_NbsEusmSlotPmSelector_Object = MibTableColumn
nbsEusmSlotPmSelector = _NbsEusmSlotPmSelector_Object(
    (1, 3, 6, 1, 4, 1, 629, 202, 3, 4, 1, 47),
    _NbsEusmSlotPmSelector_Type()
)
nbsEusmSlotPmSelector.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsEusmSlotPmSelector.setStatus("current")


class _NbsEusmSlotPmAction_Type(Integer32):
    """Custom type nbsEusmSlotPmAction based on Integer32"""
    defaultValue = 1

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
        *(("complete", 6),
          ("inProgress", 5),
          ("inactive", 2),
          ("notSupported", 1),
          ("start", 3),
          ("stop", 4),
          ("stopping", 7))
    )


_NbsEusmSlotPmAction_Type.__name__ = "Integer32"
_NbsEusmSlotPmAction_Object = MibTableColumn
nbsEusmSlotPmAction = _NbsEusmSlotPmAction_Object(
    (1, 3, 6, 1, 4, 1, 629, 202, 3, 4, 1, 48),
    _NbsEusmSlotPmAction_Type()
)
nbsEusmSlotPmAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsEusmSlotPmAction.setStatus("current")


class _NbsEusmSlotPmCapabilities_Type(OctetString):
    """Custom type nbsEusmSlotPmCapabilities based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_NbsEusmSlotPmCapabilities_Type.__name__ = "OctetString"
_NbsEusmSlotPmCapabilities_Object = MibTableColumn
nbsEusmSlotPmCapabilities = _NbsEusmSlotPmCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 629, 202, 3, 4, 1, 49),
    _NbsEusmSlotPmCapabilities_Type()
)
nbsEusmSlotPmCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsEusmSlotPmCapabilities.setStatus("current")
nbsCmmcSlotEntry.registerAugmentions(
    ("NBS-EUSM-MIB",
     "nbsEusmSlotEntry")
)
nbsEusmSlotEntry.setIndexNames(*nbsCmmcSlotEntry.getIndexNames())
nbsEusmFlowCfgEntry.registerAugmentions(
    ("NBS-EUSM-MIB",
     "nbsEusmFlowStatusEntry")
)
nbsEusmFlowStatusEntry.setIndexNames(*nbsEusmFlowCfgEntry.getIndexNames())
nbsCmmcPortEntry.registerAugmentions(
    ("NBS-EUSM-MIB",
     "nbsEusmPortEntry")
)
nbsEusmPortEntry.setIndexNames(*nbsCmmcPortEntry.getIndexNames())
nbsCmmcPortEntry.registerAugmentions(
    ("NBS-EUSM-MIB",
     "nbsEusmTgaEntry")
)
nbsEusmTgaEntry.setIndexNames(*nbsCmmcPortEntry.getIndexNames())
nbsCmmcPortEntry.registerAugmentions(
    ("NBS-EUSM-MIB",
     "nbsEusmCableTestEntry")
)
nbsEusmCableTestEntry.setIndexNames(*nbsCmmcPortEntry.getIndexNames())
nbsCmmcSlotEntry.registerAugmentions(
    ("NBS-EUSM-MIB",
     "nbsEusmLgaEntry")
)
nbsEusmLgaEntry.setIndexNames(*nbsCmmcSlotEntry.getIndexNames())
nbsCmmcSlotEntry.registerAugmentions(
    ("NBS-EUSM-MIB",
     "nbsEusmPmEntry")
)
nbsEusmPmEntry.setIndexNames(*nbsCmmcSlotEntry.getIndexNames())

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NBS-EUSM-MIB",
    **{"nbsEusmMib": nbsEusmMib,
       "nbsEusmSlotGrp": nbsEusmSlotGrp,
       "nbsEusmSlotTable": nbsEusmSlotTable,
       "nbsEusmSlotEntry": nbsEusmSlotEntry,
       "nbsEusmSlotSupportsEusm": nbsEusmSlotSupportsEusm,
       "nbsEusmSlotAccControlActionUntag": nbsEusmSlotAccControlActionUntag,
       "nbsEusmSlotAccControlActionTag": nbsEusmSlotAccControlActionTag,
       "nbsEusmSlotAccControlVidList": nbsEusmSlotAccControlVidList,
       "nbsEusmSlotLinkAggrAdmin": nbsEusmSlotLinkAggrAdmin,
       "nbsEusmSlotLinkAggrOper": nbsEusmSlotLinkAggrOper,
       "nbsEusmSlotStormControlBroadcast": nbsEusmSlotStormControlBroadcast,
       "nbsEusmSlotStormControlMulticast": nbsEusmSlotStormControlMulticast,
       "nbsEusmSlotStormControlUnicast": nbsEusmSlotStormControlUnicast,
       "nbsEusmSlotStormBurstSize": nbsEusmSlotStormBurstSize,
       "nbsEusmSlotCoSMode": nbsEusmSlotCoSMode,
       "nbsEusmSlotDscpRemark": nbsEusmSlotDscpRemark,
       "nbsEusmSlotDscpEgressMode": nbsEusmSlotDscpEgressMode,
       "nbsEusmSlotDscpIngressEf": nbsEusmSlotDscpIngressEf,
       "nbsEusmSlotDscpIngressAf": nbsEusmSlotDscpIngressAf,
       "nbsEusmSlotDscpIngressCs": nbsEusmSlotDscpIngressCs,
       "nbsEusmSlotDscpIngressZeroDscp": nbsEusmSlotDscpIngressZeroDscp,
       "nbsEusmSlotDscpIngressAllOther": nbsEusmSlotDscpIngressAllOther,
       "nbsEusmSlotIometrix": nbsEusmSlotIometrix,
       "nbsEusmSlotManagementVid": nbsEusmSlotManagementVid,
       "nbsEusmSlotUserPortIRAdmin": nbsEusmSlotUserPortIRAdmin,
       "nbsEusmSlotUserPortIROper": nbsEusmSlotUserPortIROper,
       "nbsEusmSlotMaxFlowCfgSize": nbsEusmSlotMaxFlowCfgSize,
       "nbsEusmSlotMaxVlanTranSize": nbsEusmSlotMaxVlanTranSize,
       "nbsEusmSlotMaxDscpMapSize": nbsEusmSlotMaxDscpMapSize,
       "nbsEusmSlotMaxCosPrioSize": nbsEusmSlotMaxCosPrioSize,
       "nbsEusmFlowCfgTable": nbsEusmFlowCfgTable,
       "nbsEusmFlowCfgEntry": nbsEusmFlowCfgEntry,
       "nbsEusmFlowCfgChassis": nbsEusmFlowCfgChassis,
       "nbsEusmFlowCfgSlot": nbsEusmFlowCfgSlot,
       "nbsEusmFlowCfgVid": nbsEusmFlowCfgVid,
       "nbsEusmFlowCfgPriority": nbsEusmFlowCfgPriority,
       "nbsEusmFlowCfgRowStatus": nbsEusmFlowCfgRowStatus,
       "nbsEusmFlowCfgStorageType": nbsEusmFlowCfgStorageType,
       "nbsEusmFlowCfgIRAdmin": nbsEusmFlowCfgIRAdmin,
       "nbsEusmFlowCfgIROper": nbsEusmFlowCfgIROper,
       "nbsEusmFlowCfgClearCounter": nbsEusmFlowCfgClearCounter,
       "nbsEusmFlowStatusTable": nbsEusmFlowStatusTable,
       "nbsEusmFlowStatusEntry": nbsEusmFlowStatusEntry,
       "nbsEusmFlowStatusRxFrames": nbsEusmFlowStatusRxFrames,
       "nbsEusmFlowStatusRxOctets": nbsEusmFlowStatusRxOctets,
       "nbsEusmVidMapTable": nbsEusmVidMapTable,
       "nbsEusmVidMapEntry": nbsEusmVidMapEntry,
       "nbsEusmVidMapChassis": nbsEusmVidMapChassis,
       "nbsEusmVidMapSlot": nbsEusmVidMapSlot,
       "nbsEusmVidMapFromVid": nbsEusmVidMapFromVid,
       "nbsEusmVidMapToVid": nbsEusmVidMapToVid,
       "nbsEusmVidMapRowStatus": nbsEusmVidMapRowStatus,
       "nbsEusmVidMapStorageType": nbsEusmVidMapStorageType,
       "nbsEusmCoSDscpMapTable": nbsEusmCoSDscpMapTable,
       "nbsEusmCoSDscpMapEntry": nbsEusmCoSDscpMapEntry,
       "nbsEusmCoSDscpMapChassis": nbsEusmCoSDscpMapChassis,
       "nbsEusmCoSDscpMapSlot": nbsEusmCoSDscpMapSlot,
       "nbsEusmCoSDscpMapDscp": nbsEusmCoSDscpMapDscp,
       "nbsEusmCoSDscpMapSlcPrio": nbsEusmCoSDscpMapSlcPrio,
       "nbsEusmCoSDscpMapRowStatus": nbsEusmCoSDscpMapRowStatus,
       "nbsEusmCoSDscpMapStorageType": nbsEusmCoSDscpMapStorageType,
       "nbsEusmCoSTagPrioMapTable": nbsEusmCoSTagPrioMapTable,
       "nbsEusmCoSTagPrioMapEntry": nbsEusmCoSTagPrioMapEntry,
       "nbsEusmCoSTagPrioMapChassis": nbsEusmCoSTagPrioMapChassis,
       "nbsEusmCoSTagPrioMapSlot": nbsEusmCoSTagPrioMapSlot,
       "nbsEusmCoSTagPrioMapPriority": nbsEusmCoSTagPrioMapPriority,
       "nbsEusmCoSTagPrioMapSlcPrio": nbsEusmCoSTagPrioMapSlcPrio,
       "nbsEusmPortGrp": nbsEusmPortGrp,
       "nbsEusmPortTable": nbsEusmPortTable,
       "nbsEusmPortEntry": nbsEusmPortEntry,
       "nbsEusmPortSupportsEusm": nbsEusmPortSupportsEusm,
       "nbsEusmPortSmartLoopbackAction": nbsEusmPortSmartLoopbackAction,
       "nbsEusmPortSmartLoopbackSwap": nbsEusmPortSmartLoopbackSwap,
       "nbsEusmPortSmartLoopbackMac": nbsEusmPortSmartLoopbackMac,
       "nbsEusmPortSmartLoopbackVid": nbsEusmPortSmartLoopbackVid,
       "nbsEusmPortVlanTagAction": nbsEusmPortVlanTagAction,
       "nbsEusmPortVlanTagVid": nbsEusmPortVlanTagVid,
       "nbsEusmPortVlanTagPriority": nbsEusmPortVlanTagPriority,
       "nbsEusmTestGrp": nbsEusmTestGrp,
       "nbsEusmTgaTable": nbsEusmTgaTable,
       "nbsEusmTgaEntry": nbsEusmTgaEntry,
       "nbsEusmTgaDa": nbsEusmTgaDa,
       "nbsEusmTgaDaType": nbsEusmTgaDaType,
       "nbsEusmTgaSa": nbsEusmTgaSa,
       "nbsEusmTgaSaType": nbsEusmTgaSaType,
       "nbsEusmTgaTag": nbsEusmTgaTag,
       "nbsEusmTgaTagType": nbsEusmTgaTagType,
       "nbsEusmTgaPattern": nbsEusmTgaPattern,
       "nbsEusmTgaPatternType": nbsEusmTgaPatternType,
       "nbsEusmTgaFrameSize": nbsEusmTgaFrameSize,
       "nbsEusmTgaFrameSizeType": nbsEusmTgaFrameSizeType,
       "nbsEusmTgaFrameCount": nbsEusmTgaFrameCount,
       "nbsEusmTgaFrameCountType": nbsEusmTgaFrameCountType,
       "nbsEusmTgaInterPacketGap": nbsEusmTgaInterPacketGap,
       "nbsEusmTgaAction": nbsEusmTgaAction,
       "nbsEusmCableTestTable": nbsEusmCableTestTable,
       "nbsEusmCableTestEntry": nbsEusmCableTestEntry,
       "nbsEusmCableTestStatus": nbsEusmCableTestStatus,
       "nbsEusmCableTestResult": nbsEusmCableTestResult,
       "nbsEusmLgaTable": nbsEusmLgaTable,
       "nbsEusmLgaEntry": nbsEusmLgaEntry,
       "nbsEusmLgaRdAllFrames": nbsEusmLgaRdAllFrames,
       "nbsEusmLgaRducFrames": nbsEusmLgaRducFrames,
       "nbsEusmLgaRdmcFrames": nbsEusmLgaRdmcFrames,
       "nbsEusmLgaRdbcFrames": nbsEusmLgaRdbcFrames,
       "nbsEusmLgaRdSize64": nbsEusmLgaRdSize64,
       "nbsEusmLgaRdSizeMax127": nbsEusmLgaRdSizeMax127,
       "nbsEusmLgaRdSizeMax255": nbsEusmLgaRdSizeMax255,
       "nbsEusmLgaRdSizeMax511": nbsEusmLgaRdSizeMax511,
       "nbsEusmLgaRdSizeMax1023": nbsEusmLgaRdSizeMax1023,
       "nbsEusmLgaRdSizeMax1518": nbsEusmLgaRdSizeMax1518,
       "nbsEusmLgaRdSizeMax2047": nbsEusmLgaRdSizeMax2047,
       "nbsEusmLgaRdSizeOvr2047": nbsEusmLgaRdSizeOvr2047,
       "nbsEusmLgaRdFrameDivisor": nbsEusmLgaRdFrameDivisor,
       "nbsEusmLgaRdAllOctets": nbsEusmLgaRdAllOctets,
       "nbsEusmLgaRdOctetDivisor": nbsEusmLgaRdOctetDivisor,
       "nbsEusmLgaRdTimeSpan": nbsEusmLgaRdTimeSpan,
       "nbsEusmLgaAdAllFrames": nbsEusmLgaAdAllFrames,
       "nbsEusmLgaAducFrames": nbsEusmLgaAducFrames,
       "nbsEusmLgaAdmcFrames": nbsEusmLgaAdmcFrames,
       "nbsEusmLgaAdbcFrames": nbsEusmLgaAdbcFrames,
       "nbsEusmLgaAdSize64": nbsEusmLgaAdSize64,
       "nbsEusmLgaAdSizeMax127": nbsEusmLgaAdSizeMax127,
       "nbsEusmLgaAdSizeMax255": nbsEusmLgaAdSizeMax255,
       "nbsEusmLgaAdSizeMax511": nbsEusmLgaAdSizeMax511,
       "nbsEusmLgaAdSizeMax1023": nbsEusmLgaAdSizeMax1023,
       "nbsEusmLgaAdSizeMax1518": nbsEusmLgaAdSizeMax1518,
       "nbsEusmLgaAdSizeMax2047": nbsEusmLgaAdSizeMax2047,
       "nbsEusmLgaAdSizeOvr2047": nbsEusmLgaAdSizeOvr2047,
       "nbsEusmLgaAdFrameDivisor": nbsEusmLgaAdFrameDivisor,
       "nbsEusmLgaAdAllOctets": nbsEusmLgaAdAllOctets,
       "nbsEusmLgaAdOctetDivisor": nbsEusmLgaAdOctetDivisor,
       "nbsEusmLgaAdTimeSpan": nbsEusmLgaAdTimeSpan,
       "nbsEusmSlotLgaInterval": nbsEusmSlotLgaInterval,
       "nbsEusmSlotLgaAction": nbsEusmSlotLgaAction,
       "nbsEusmPmTable": nbsEusmPmTable,
       "nbsEusmPmEntry": nbsEusmPmEntry,
       "nbsEusmPmAvgAllSizes": nbsEusmPmAvgAllSizes,
       "nbsEusmPmAvg64": nbsEusmPmAvg64,
       "nbsEusmPmAvg127": nbsEusmPmAvg127,
       "nbsEusmPmAvg255": nbsEusmPmAvg255,
       "nbsEusmPmAvg511": nbsEusmPmAvg511,
       "nbsEusmPmAvg1023": nbsEusmPmAvg1023,
       "nbsEusmPmAvg1518": nbsEusmPmAvg1518,
       "nbsEusmPmAvg2047": nbsEusmPmAvg2047,
       "nbsEusmPmAvgOvr2047": nbsEusmPmAvgOvr2047,
       "nbsEusmPmMinAllSizes": nbsEusmPmMinAllSizes,
       "nbsEusmPmMin64": nbsEusmPmMin64,
       "nbsEusmPmMin127": nbsEusmPmMin127,
       "nbsEusmPmMin255": nbsEusmPmMin255,
       "nbsEusmPmMin511": nbsEusmPmMin511,
       "nbsEusmPmMin1023": nbsEusmPmMin1023,
       "nbsEusmPmMin1518": nbsEusmPmMin1518,
       "nbsEusmPmMin2047": nbsEusmPmMin2047,
       "nbsEusmPmMinOvr2047": nbsEusmPmMinOvr2047,
       "nbsEusmPmMaxAllSizes": nbsEusmPmMaxAllSizes,
       "nbsEusmPmMax64": nbsEusmPmMax64,
       "nbsEusmPmMax127": nbsEusmPmMax127,
       "nbsEusmPmMax255": nbsEusmPmMax255,
       "nbsEusmPmMax511": nbsEusmPmMax511,
       "nbsEusmPmMax1023": nbsEusmPmMax1023,
       "nbsEusmPmMax1518": nbsEusmPmMax1518,
       "nbsEusmPmMax2047": nbsEusmPmMax2047,
       "nbsEusmPmMaxOvr2047": nbsEusmPmMaxOvr2047,
       "nbsEusmPmFramesAllSizes": nbsEusmPmFramesAllSizes,
       "nbsEusmPmFrames64": nbsEusmPmFrames64,
       "nbsEusmPmFrames127": nbsEusmPmFrames127,
       "nbsEusmPmFrames255": nbsEusmPmFrames255,
       "nbsEusmPmFrames511": nbsEusmPmFrames511,
       "nbsEusmPmFrames1023": nbsEusmPmFrames1023,
       "nbsEusmPmFrames1518": nbsEusmPmFrames1518,
       "nbsEusmPmFrames2047": nbsEusmPmFrames2047,
       "nbsEusmPmFramesOvr2047": nbsEusmPmFramesOvr2047,
       "nbsEusmPmOctetsAllSizes": nbsEusmPmOctetsAllSizes,
       "nbsEusmPmOctets64": nbsEusmPmOctets64,
       "nbsEusmPmOctets127": nbsEusmPmOctets127,
       "nbsEusmPmOctets255": nbsEusmPmOctets255,
       "nbsEusmPmOctets511": nbsEusmPmOctets511,
       "nbsEusmPmOctets1023": nbsEusmPmOctets1023,
       "nbsEusmPmOctets1518": nbsEusmPmOctets1518,
       "nbsEusmPmOctets2047": nbsEusmPmOctets2047,
       "nbsEusmPmOctetsOvr2047": nbsEusmPmOctetsOvr2047,
       "nbsEusmSlotPmInterval": nbsEusmSlotPmInterval,
       "nbsEusmSlotPmSelector": nbsEusmSlotPmSelector,
       "nbsEusmSlotPmAction": nbsEusmSlotPmAction,
       "nbsEusmSlotPmCapabilities": nbsEusmSlotPmCapabilities}
)
