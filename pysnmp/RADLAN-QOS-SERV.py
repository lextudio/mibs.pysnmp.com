# SNMP MIB module (RADLAN-QOS-SERV) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/RADLAN-QOS-SERV
# Produced by pysmi-1.5.4 at Mon Oct 14 22:43:08 2024
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

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

(PortList,) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "PortList")

(rnd,) = mibBuilder.importSymbols(
    "RADLAN-MIB",
    "rnd")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

rlQosServ = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 89, 99)
)
rlQosServ.setRevisions(
        ("2006-02-12 00:00",
         "2003-10-28 00:24")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class RlQosServServiceStatus(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("suspended", 2))
    )



class RlQosServNamedTableId(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("fce", 2),
          ("fcl", 1),
          ("profile", 3))
    )



# MIB Managed Objects in the order of their OIDs

_RlQosServTemplateTable_Object = MibTable
rlQosServTemplateTable = _RlQosServTemplateTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 99, 1)
)
if mibBuilder.loadTexts:
    rlQosServTemplateTable.setStatus("current")
_RlQosServTemplateEntry_Object = MibTableRow
rlQosServTemplateEntry = _RlQosServTemplateEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 99, 1, 1)
)
rlQosServTemplateEntry.setIndexNames(
    (0, "RADLAN-QOS-SERV", "rlQosServTemplateIndex"),
)
if mibBuilder.loadTexts:
    rlQosServTemplateEntry.setStatus("current")
_RlQosServTemplateIndex_Type = Integer32
_RlQosServTemplateIndex_Object = MibTableColumn
rlQosServTemplateIndex = _RlQosServTemplateIndex_Object(
    (1, 3, 6, 1, 4, 1, 89, 99, 1, 1, 1),
    _RlQosServTemplateIndex_Type()
)
rlQosServTemplateIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlQosServTemplateIndex.setStatus("current")


class _RlQosServTemplateDestMac_Type(TruthValue):
    """Custom type rlQosServTemplateDestMac based on TruthValue"""


_RlQosServTemplateDestMac_Object = MibTableColumn
rlQosServTemplateDestMac = _RlQosServTemplateDestMac_Object(
    (1, 3, 6, 1, 4, 1, 89, 99, 1, 1, 2),
    _RlQosServTemplateDestMac_Type()
)
rlQosServTemplateDestMac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlQosServTemplateDestMac.setStatus("current")
_RlQosServTemplateDestMacMask_Type = MacAddress
_RlQosServTemplateDestMacMask_Object = MibTableColumn
rlQosServTemplateDestMacMask = _RlQosServTemplateDestMacMask_Object(
    (1, 3, 6, 1, 4, 1, 89, 99, 1, 1, 3),
    _RlQosServTemplateDestMacMask_Type()
)
rlQosServTemplateDestMacMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlQosServTemplateDestMacMask.setStatus("current")


class _RlQosServTemplateSrcMac_Type(TruthValue):
    """Custom type rlQosServTemplateSrcMac based on TruthValue"""


_RlQosServTemplateSrcMac_Object = MibTableColumn
rlQosServTemplateSrcMac = _RlQosServTemplateSrcMac_Object(
    (1, 3, 6, 1, 4, 1, 89, 99, 1, 1, 4),
    _RlQosServTemplateSrcMac_Type()
)
rlQosServTemplateSrcMac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlQosServTemplateSrcMac.setStatus("current")
_RlQosServTemplateSrcMacMask_Type = MacAddress
_RlQosServTemplateSrcMacMask_Object = MibTableColumn
rlQosServTemplateSrcMacMask = _RlQosServTemplateSrcMacMask_Object(
    (1, 3, 6, 1, 4, 1, 89, 99, 1, 1, 5),
    _RlQosServTemplateSrcMacMask_Type()
)
rlQosServTemplateSrcMacMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlQosServTemplateSrcMacMask.setStatus("current")


class _RlQosServTemplateVlan_Type(TruthValue):
    """Custom type rlQosServTemplateVlan based on TruthValue"""


_RlQosServTemplateVlan_Object = MibTableColumn
rlQosServTemplateVlan = _RlQosServTemplateVlan_Object(
    (1, 3, 6, 1, 4, 1, 89, 99, 1, 1, 6),
    _RlQosServTemplateVlan_Type()
)
rlQosServTemplateVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlQosServTemplateVlan.setStatus("current")


class _RlQosServTemplateDestIp_Type(TruthValue):
    """Custom type rlQosServTemplateDestIp based on TruthValue"""


_RlQosServTemplateDestIp_Object = MibTableColumn
rlQosServTemplateDestIp = _RlQosServTemplateDestIp_Object(
    (1, 3, 6, 1, 4, 1, 89, 99, 1, 1, 7),
    _RlQosServTemplateDestIp_Type()
)
rlQosServTemplateDestIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlQosServTemplateDestIp.setStatus("current")


class _RlQosServTemplateDestIpMask_Type(IpAddress):
    """Custom type rlQosServTemplateDestIpMask based on IpAddress"""
    defaultHexValue = "00000000"


_RlQosServTemplateDestIpMask_Object = MibTableColumn
rlQosServTemplateDestIpMask = _RlQosServTemplateDestIpMask_Object(
    (1, 3, 6, 1, 4, 1, 89, 99, 1, 1, 8),
    _RlQosServTemplateDestIpMask_Type()
)
rlQosServTemplateDestIpMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlQosServTemplateDestIpMask.setStatus("current")


class _RlQosServTemplateSrcIp_Type(TruthValue):
    """Custom type rlQosServTemplateSrcIp based on TruthValue"""


_RlQosServTemplateSrcIp_Object = MibTableColumn
rlQosServTemplateSrcIp = _RlQosServTemplateSrcIp_Object(
    (1, 3, 6, 1, 4, 1, 89, 99, 1, 1, 9),
    _RlQosServTemplateSrcIp_Type()
)
rlQosServTemplateSrcIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlQosServTemplateSrcIp.setStatus("current")


class _RlQosServTemplateSrcIpMask_Type(IpAddress):
    """Custom type rlQosServTemplateSrcIpMask based on IpAddress"""
    defaultHexValue = "00000000"


_RlQosServTemplateSrcIpMask_Object = MibTableColumn
rlQosServTemplateSrcIpMask = _RlQosServTemplateSrcIpMask_Object(
    (1, 3, 6, 1, 4, 1, 89, 99, 1, 1, 10),
    _RlQosServTemplateSrcIpMask_Type()
)
rlQosServTemplateSrcIpMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlQosServTemplateSrcIpMask.setStatus("current")


class _RlQosServTemplateIpProtocol_Type(TruthValue):
    """Custom type rlQosServTemplateIpProtocol based on TruthValue"""


_RlQosServTemplateIpProtocol_Object = MibTableColumn
rlQosServTemplateIpProtocol = _RlQosServTemplateIpProtocol_Object(
    (1, 3, 6, 1, 4, 1, 89, 99, 1, 1, 11),
    _RlQosServTemplateIpProtocol_Type()
)
rlQosServTemplateIpProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlQosServTemplateIpProtocol.setStatus("current")


class _RlQosServTemplateSrcPort_Type(TruthValue):
    """Custom type rlQosServTemplateSrcPort based on TruthValue"""


_RlQosServTemplateSrcPort_Object = MibTableColumn
rlQosServTemplateSrcPort = _RlQosServTemplateSrcPort_Object(
    (1, 3, 6, 1, 4, 1, 89, 99, 1, 1, 12),
    _RlQosServTemplateSrcPort_Type()
)
rlQosServTemplateSrcPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlQosServTemplateSrcPort.setStatus("current")


class _RlQosServTemplateDestPort_Type(TruthValue):
    """Custom type rlQosServTemplateDestPort based on TruthValue"""


_RlQosServTemplateDestPort_Object = MibTableColumn
rlQosServTemplateDestPort = _RlQosServTemplateDestPort_Object(
    (1, 3, 6, 1, 4, 1, 89, 99, 1, 1, 13),
    _RlQosServTemplateDestPort_Type()
)
rlQosServTemplateDestPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlQosServTemplateDestPort.setStatus("current")


class _RlQosServTemplateTos_Type(TruthValue):
    """Custom type rlQosServTemplateTos based on TruthValue"""


_RlQosServTemplateTos_Object = MibTableColumn
rlQosServTemplateTos = _RlQosServTemplateTos_Object(
    (1, 3, 6, 1, 4, 1, 89, 99, 1, 1, 14),
    _RlQosServTemplateTos_Type()
)
rlQosServTemplateTos.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlQosServTemplateTos.setStatus("current")


class _RlQosServTemplateVpt_Type(TruthValue):
    """Custom type rlQosServTemplateVpt based on TruthValue"""


_RlQosServTemplateVpt_Object = MibTableColumn
rlQosServTemplateVpt = _RlQosServTemplateVpt_Object(
    (1, 3, 6, 1, 4, 1, 89, 99, 1, 1, 15),
    _RlQosServTemplateVpt_Type()
)
rlQosServTemplateVpt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlQosServTemplateVpt.setStatus("current")


class _RlQosServTemplateEtherType_Type(TruthValue):
    """Custom type rlQosServTemplateEtherType based on TruthValue"""


_RlQosServTemplateEtherType_Object = MibTableColumn
rlQosServTemplateEtherType = _RlQosServTemplateEtherType_Object(
    (1, 3, 6, 1, 4, 1, 89, 99, 1, 1, 16),
    _RlQosServTemplateEtherType_Type()
)
rlQosServTemplateEtherType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlQosServTemplateEtherType.setStatus("current")


class _RlQosServTemplateTcpFlags_Type(TruthValue):
    """Custom type rlQosServTemplateTcpFlags based on TruthValue"""


_RlQosServTemplateTcpFlags_Object = MibTableColumn
rlQosServTemplateTcpFlags = _RlQosServTemplateTcpFlags_Object(
    (1, 3, 6, 1, 4, 1, 89, 99, 1, 1, 17),
    _RlQosServTemplateTcpFlags_Type()
)
rlQosServTemplateTcpFlags.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlQosServTemplateTcpFlags.setStatus("current")


class _RlQosServTemplateIcmpType_Type(TruthValue):
    """Custom type rlQosServTemplateIcmpType based on TruthValue"""


_RlQosServTemplateIcmpType_Object = MibTableColumn
rlQosServTemplateIcmpType = _RlQosServTemplateIcmpType_Object(
    (1, 3, 6, 1, 4, 1, 89, 99, 1, 1, 18),
    _RlQosServTemplateIcmpType_Type()
)
rlQosServTemplateIcmpType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlQosServTemplateIcmpType.setStatus("current")


class _RlQosServTemplateIcmpCode_Type(TruthValue):
    """Custom type rlQosServTemplateIcmpCode based on TruthValue"""


_RlQosServTemplateIcmpCode_Object = MibTableColumn
rlQosServTemplateIcmpCode = _RlQosServTemplateIcmpCode_Object(
    (1, 3, 6, 1, 4, 1, 89, 99, 1, 1, 19),
    _RlQosServTemplateIcmpCode_Type()
)
rlQosServTemplateIcmpCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlQosServTemplateIcmpCode.setStatus("current")


class _RlQosServTemplateIgmpType_Type(TruthValue):
    """Custom type rlQosServTemplateIgmpType based on TruthValue"""


_RlQosServTemplateIgmpType_Object = MibTableColumn
rlQosServTemplateIgmpType = _RlQosServTemplateIgmpType_Object(
    (1, 3, 6, 1, 4, 1, 89, 99, 1, 1, 20),
    _RlQosServTemplateIgmpType_Type()
)
rlQosServTemplateIgmpType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlQosServTemplateIgmpType.setStatus("current")
_RlQosServFclTable_Object = MibTable
rlQosServFclTable = _RlQosServFclTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 99, 2)
)
if mibBuilder.loadTexts:
    rlQosServFclTable.setStatus("current")
_RlQosServFclEntry_Object = MibTableRow
rlQosServFclEntry = _RlQosServFclEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 99, 2, 1)
)
rlQosServFclEntry.setIndexNames(
    (0, "RADLAN-QOS-SERV", "rlQosServFclIndex"),
    (0, "RADLAN-QOS-SERV", "rlQosServFclFcePriority"),
)
if mibBuilder.loadTexts:
    rlQosServFclEntry.setStatus("current")
_RlQosServFclIndex_Type = Integer32
_RlQosServFclIndex_Object = MibTableColumn
rlQosServFclIndex = _RlQosServFclIndex_Object(
    (1, 3, 6, 1, 4, 1, 89, 99, 2, 1, 1),
    _RlQosServFclIndex_Type()
)
rlQosServFclIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlQosServFclIndex.setStatus("current")
_RlQosServFclFcePriority_Type = Integer32
_RlQosServFclFcePriority_Object = MibTableColumn
rlQosServFclFcePriority = _RlQosServFclFcePriority_Object(
    (1, 3, 6, 1, 4, 1, 89, 99, 2, 1, 2),
    _RlQosServFclFcePriority_Type()
)
rlQosServFclFcePriority.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlQosServFclFcePriority.setStatus("current")
_RlQosServFclFceIndex_Type = Integer32
_RlQosServFclFceIndex_Object = MibTableColumn
rlQosServFclFceIndex = _RlQosServFclFceIndex_Object(
    (1, 3, 6, 1, 4, 1, 89, 99, 2, 1, 3),
    _RlQosServFclFceIndex_Type()
)
rlQosServFclFceIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlQosServFclFceIndex.setStatus("current")
_RlQosServFclStatus_Type = RowStatus
_RlQosServFclStatus_Object = MibTableColumn
rlQosServFclStatus = _RlQosServFclStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 99, 2, 1, 4),
    _RlQosServFclStatus_Type()
)
rlQosServFclStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlQosServFclStatus.setStatus("current")
_RlQosServFceTable_Object = MibTable
rlQosServFceTable = _RlQosServFceTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 99, 3)
)
if mibBuilder.loadTexts:
    rlQosServFceTable.setStatus("current")
_RlQosServFceEntry_Object = MibTableRow
rlQosServFceEntry = _RlQosServFceEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 99, 3, 1)
)
rlQosServFceEntry.setIndexNames(
    (0, "RADLAN-QOS-SERV", "rlQosServFceIndex"),
)
if mibBuilder.loadTexts:
    rlQosServFceEntry.setStatus("current")
_RlQosServFceIndex_Type = Integer32
_RlQosServFceIndex_Object = MibTableColumn
rlQosServFceIndex = _RlQosServFceIndex_Object(
    (1, 3, 6, 1, 4, 1, 89, 99, 3, 1, 1),
    _RlQosServFceIndex_Type()
)
rlQosServFceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlQosServFceIndex.setStatus("current")


class _RlQosServFceErrorCode_Type(Integer32):
    """Custom type rlQosServFceErrorCode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noError", 1),
          ("noTemplate", 2))
    )


_RlQosServFceErrorCode_Type.__name__ = "Integer32"
_RlQosServFceErrorCode_Object = MibTableColumn
rlQosServFceErrorCode = _RlQosServFceErrorCode_Object(
    (1, 3, 6, 1, 4, 1, 89, 99, 3, 1, 2),
    _RlQosServFceErrorCode_Type()
)
rlQosServFceErrorCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlQosServFceErrorCode.setStatus("current")


class _RlQosServFceSelection_Type(Bits):
    """Custom type rlQosServFceSelection based on Bits"""
    namedValues = NamedValues(
        *(("destPort", 6),
          ("dscp", 8),
          ("etherType", 11),
          ("icmpCode", 14),
          ("icmpType", 13),
          ("igmpType", 15),
          ("ipDestAddr", 3),
          ("ipPrecedence", 9),
          ("ipProtocol", 5),
          ("ipSrcAddr", 4),
          ("macDestAddr", 0),
          ("macSrcAddr", 1),
          ("srcPort", 7),
          ("tcpFlags", 12),
          ("vlan", 2),
          ("vpt", 10))
    )

_RlQosServFceSelection_Type.__name__ = "Bits"
_RlQosServFceSelection_Object = MibTableColumn
rlQosServFceSelection = _RlQosServFceSelection_Object(
    (1, 3, 6, 1, 4, 1, 89, 99, 3, 1, 3),
    _RlQosServFceSelection_Type()
)
rlQosServFceSelection.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlQosServFceSelection.setStatus("current")
_RlQosServFceDestMac_Type = MacAddress
_RlQosServFceDestMac_Object = MibTableColumn
rlQosServFceDestMac = _RlQosServFceDestMac_Object(
    (1, 3, 6, 1, 4, 1, 89, 99, 3, 1, 4),
    _RlQosServFceDestMac_Type()
)
rlQosServFceDestMac.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlQosServFceDestMac.setStatus("current")
_RlQosServFceDestMacMask_Type = MacAddress
_RlQosServFceDestMacMask_Object = MibTableColumn
rlQosServFceDestMacMask = _RlQosServFceDestMacMask_Object(
    (1, 3, 6, 1, 4, 1, 89, 99, 3, 1, 5),
    _RlQosServFceDestMacMask_Type()
)
rlQosServFceDestMacMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlQosServFceDestMacMask.setStatus("current")
_RlQosServFceSrcMac_Type = MacAddress
_RlQosServFceSrcMac_Object = MibTableColumn
rlQosServFceSrcMac = _RlQosServFceSrcMac_Object(
    (1, 3, 6, 1, 4, 1, 89, 99, 3, 1, 6),
    _RlQosServFceSrcMac_Type()
)
rlQosServFceSrcMac.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlQosServFceSrcMac.setStatus("current")
_RlQosServFceSrcMacMask_Type = MacAddress
_RlQosServFceSrcMacMask_Object = MibTableColumn
rlQosServFceSrcMacMask = _RlQosServFceSrcMacMask_Object(
    (1, 3, 6, 1, 4, 1, 89, 99, 3, 1, 7),
    _RlQosServFceSrcMacMask_Type()
)
rlQosServFceSrcMacMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlQosServFceSrcMacMask.setStatus("current")


class _RlQosServFceVlan_Type(Integer32):
    """Custom type rlQosServFceVlan based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_RlQosServFceVlan_Type.__name__ = "Integer32"
_RlQosServFceVlan_Object = MibTableColumn
rlQosServFceVlan = _RlQosServFceVlan_Object(
    (1, 3, 6, 1, 4, 1, 89, 99, 3, 1, 8),
    _RlQosServFceVlan_Type()
)
rlQosServFceVlan.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlQosServFceVlan.setStatus("current")


class _RlQosServFceVlanMask_Type(Integer32):
    """Custom type rlQosServFceVlanMask based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_RlQosServFceVlanMask_Type.__name__ = "Integer32"
_RlQosServFceVlanMask_Object = MibTableColumn
rlQosServFceVlanMask = _RlQosServFceVlanMask_Object(
    (1, 3, 6, 1, 4, 1, 89, 99, 3, 1, 9),
    _RlQosServFceVlanMask_Type()
)
rlQosServFceVlanMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlQosServFceVlanMask.setStatus("current")


class _RlQosServFceDestIp_Type(IpAddress):
    """Custom type rlQosServFceDestIp based on IpAddress"""
    defaultHexValue = "00000000"


_RlQosServFceDestIp_Object = MibTableColumn
rlQosServFceDestIp = _RlQosServFceDestIp_Object(
    (1, 3, 6, 1, 4, 1, 89, 99, 3, 1, 10),
    _RlQosServFceDestIp_Type()
)
rlQosServFceDestIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlQosServFceDestIp.setStatus("current")


class _RlQosServFceDestIpMask_Type(IpAddress):
    """Custom type rlQosServFceDestIpMask based on IpAddress"""
    defaultHexValue = "00000000"


_RlQosServFceDestIpMask_Object = MibTableColumn
rlQosServFceDestIpMask = _RlQosServFceDestIpMask_Object(
    (1, 3, 6, 1, 4, 1, 89, 99, 3, 1, 11),
    _RlQosServFceDestIpMask_Type()
)
rlQosServFceDestIpMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlQosServFceDestIpMask.setStatus("current")


class _RlQosServFceSrcIp_Type(IpAddress):
    """Custom type rlQosServFceSrcIp based on IpAddress"""
    defaultHexValue = "00000000"


_RlQosServFceSrcIp_Object = MibTableColumn
rlQosServFceSrcIp = _RlQosServFceSrcIp_Object(
    (1, 3, 6, 1, 4, 1, 89, 99, 3, 1, 12),
    _RlQosServFceSrcIp_Type()
)
rlQosServFceSrcIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlQosServFceSrcIp.setStatus("current")


class _RlQosServFceSrcIpMask_Type(IpAddress):
    """Custom type rlQosServFceSrcIpMask based on IpAddress"""
    defaultHexValue = "00000000"


_RlQosServFceSrcIpMask_Object = MibTableColumn
rlQosServFceSrcIpMask = _RlQosServFceSrcIpMask_Object(
    (1, 3, 6, 1, 4, 1, 89, 99, 3, 1, 13),
    _RlQosServFceSrcIpMask_Type()
)
rlQosServFceSrcIpMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlQosServFceSrcIpMask.setStatus("current")


class _RlQosServFceIpProtocol_Type(Integer32):
    """Custom type rlQosServFceIpProtocol based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_RlQosServFceIpProtocol_Type.__name__ = "Integer32"
_RlQosServFceIpProtocol_Object = MibTableColumn
rlQosServFceIpProtocol = _RlQosServFceIpProtocol_Object(
    (1, 3, 6, 1, 4, 1, 89, 99, 3, 1, 14),
    _RlQosServFceIpProtocol_Type()
)
rlQosServFceIpProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlQosServFceIpProtocol.setStatus("current")


class _RlQosServFceDestPort_Type(Integer32):
    """Custom type rlQosServFceDestPort based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RlQosServFceDestPort_Type.__name__ = "Integer32"
_RlQosServFceDestPort_Object = MibTableColumn
rlQosServFceDestPort = _RlQosServFceDestPort_Object(
    (1, 3, 6, 1, 4, 1, 89, 99, 3, 1, 15),
    _RlQosServFceDestPort_Type()
)
rlQosServFceDestPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlQosServFceDestPort.setStatus("current")


class _RlQosServFceDestPortMask_Type(Integer32):
    """Custom type rlQosServFceDestPortMask based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RlQosServFceDestPortMask_Type.__name__ = "Integer32"
_RlQosServFceDestPortMask_Object = MibTableColumn
rlQosServFceDestPortMask = _RlQosServFceDestPortMask_Object(
    (1, 3, 6, 1, 4, 1, 89, 99, 3, 1, 16),
    _RlQosServFceDestPortMask_Type()
)
rlQosServFceDestPortMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlQosServFceDestPortMask.setStatus("current")


class _RlQosServFceSrcPort_Type(Integer32):
    """Custom type rlQosServFceSrcPort based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RlQosServFceSrcPort_Type.__name__ = "Integer32"
_RlQosServFceSrcPort_Object = MibTableColumn
rlQosServFceSrcPort = _RlQosServFceSrcPort_Object(
    (1, 3, 6, 1, 4, 1, 89, 99, 3, 1, 17),
    _RlQosServFceSrcPort_Type()
)
rlQosServFceSrcPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlQosServFceSrcPort.setStatus("current")


class _RlQosServFceSrcPortMask_Type(Integer32):
    """Custom type rlQosServFceSrcPortMask based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RlQosServFceSrcPortMask_Type.__name__ = "Integer32"
_RlQosServFceSrcPortMask_Object = MibTableColumn
rlQosServFceSrcPortMask = _RlQosServFceSrcPortMask_Object(
    (1, 3, 6, 1, 4, 1, 89, 99, 3, 1, 18),
    _RlQosServFceSrcPortMask_Type()
)
rlQosServFceSrcPortMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlQosServFceSrcPortMask.setStatus("current")


class _RlQosServFceDscp_Type(Integer32):
    """Custom type rlQosServFceDscp based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_RlQosServFceDscp_Type.__name__ = "Integer32"
_RlQosServFceDscp_Object = MibTableColumn
rlQosServFceDscp = _RlQosServFceDscp_Object(
    (1, 3, 6, 1, 4, 1, 89, 99, 3, 1, 19),
    _RlQosServFceDscp_Type()
)
rlQosServFceDscp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlQosServFceDscp.setStatus("current")


class _RlQosServFceIpPrecedence_Type(Integer32):
    """Custom type rlQosServFceIpPrecedence based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_RlQosServFceIpPrecedence_Type.__name__ = "Integer32"
_RlQosServFceIpPrecedence_Object = MibTableColumn
rlQosServFceIpPrecedence = _RlQosServFceIpPrecedence_Object(
    (1, 3, 6, 1, 4, 1, 89, 99, 3, 1, 20),
    _RlQosServFceIpPrecedence_Type()
)
rlQosServFceIpPrecedence.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlQosServFceIpPrecedence.setStatus("current")


class _RlQosServFceVpt_Type(Integer32):
    """Custom type rlQosServFceVpt based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_RlQosServFceVpt_Type.__name__ = "Integer32"
_RlQosServFceVpt_Object = MibTableColumn
rlQosServFceVpt = _RlQosServFceVpt_Object(
    (1, 3, 6, 1, 4, 1, 89, 99, 3, 1, 21),
    _RlQosServFceVpt_Type()
)
rlQosServFceVpt.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlQosServFceVpt.setStatus("current")
_RlQosServFceVptMask_Type = Integer32
_RlQosServFceVptMask_Object = MibTableColumn
rlQosServFceVptMask = _RlQosServFceVptMask_Object(
    (1, 3, 6, 1, 4, 1, 89, 99, 3, 1, 22),
    _RlQosServFceVptMask_Type()
)
rlQosServFceVptMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlQosServFceVptMask.setStatus("current")


class _RlQosServFceEtherType_Type(Integer32):
    """Custom type rlQosServFceEtherType based on Integer32"""
    defaultValue = 1501

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1501, 65536),
    )


_RlQosServFceEtherType_Type.__name__ = "Integer32"
_RlQosServFceEtherType_Object = MibTableColumn
rlQosServFceEtherType = _RlQosServFceEtherType_Object(
    (1, 3, 6, 1, 4, 1, 89, 99, 3, 1, 23),
    _RlQosServFceEtherType_Type()
)
rlQosServFceEtherType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlQosServFceEtherType.setStatus("current")


class _RlQosServFceTcpFlags_Type(Integer32):
    """Custom type rlQosServFceTcpFlags based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_RlQosServFceTcpFlags_Type.__name__ = "Integer32"
_RlQosServFceTcpFlags_Object = MibTableColumn
rlQosServFceTcpFlags = _RlQosServFceTcpFlags_Object(
    (1, 3, 6, 1, 4, 1, 89, 99, 3, 1, 24),
    _RlQosServFceTcpFlags_Type()
)
rlQosServFceTcpFlags.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlQosServFceTcpFlags.setStatus("current")


class _RlQosServFceTcpFlagsMask_Type(Integer32):
    """Custom type rlQosServFceTcpFlagsMask based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_RlQosServFceTcpFlagsMask_Type.__name__ = "Integer32"
_RlQosServFceTcpFlagsMask_Object = MibTableColumn
rlQosServFceTcpFlagsMask = _RlQosServFceTcpFlagsMask_Object(
    (1, 3, 6, 1, 4, 1, 89, 99, 3, 1, 25),
    _RlQosServFceTcpFlagsMask_Type()
)
rlQosServFceTcpFlagsMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlQosServFceTcpFlagsMask.setStatus("current")


class _RlQosServFceIcmpType_Type(Integer32):
    """Custom type rlQosServFceIcmpType based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_RlQosServFceIcmpType_Type.__name__ = "Integer32"
_RlQosServFceIcmpType_Object = MibTableColumn
rlQosServFceIcmpType = _RlQosServFceIcmpType_Object(
    (1, 3, 6, 1, 4, 1, 89, 99, 3, 1, 26),
    _RlQosServFceIcmpType_Type()
)
rlQosServFceIcmpType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlQosServFceIcmpType.setStatus("current")


class _RlQosServFceIcmpCode_Type(Integer32):
    """Custom type rlQosServFceIcmpCode based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_RlQosServFceIcmpCode_Type.__name__ = "Integer32"
_RlQosServFceIcmpCode_Object = MibTableColumn
rlQosServFceIcmpCode = _RlQosServFceIcmpCode_Object(
    (1, 3, 6, 1, 4, 1, 89, 99, 3, 1, 27),
    _RlQosServFceIcmpCode_Type()
)
rlQosServFceIcmpCode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlQosServFceIcmpCode.setStatus("current")


class _RlQosServFceIgmpType_Type(Integer32):
    """Custom type rlQosServFceIgmpType based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_RlQosServFceIgmpType_Type.__name__ = "Integer32"
_RlQosServFceIgmpType_Object = MibTableColumn
rlQosServFceIgmpType = _RlQosServFceIgmpType_Object(
    (1, 3, 6, 1, 4, 1, 89, 99, 3, 1, 28),
    _RlQosServFceIgmpType_Type()
)
rlQosServFceIgmpType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlQosServFceIgmpType.setStatus("current")
_RlQosServFceStatus_Type = RowStatus
_RlQosServFceStatus_Object = MibTableColumn
rlQosServFceStatus = _RlQosServFceStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 99, 3, 1, 29),
    _RlQosServFceStatus_Type()
)
rlQosServFceStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlQosServFceStatus.setStatus("current")
_RlQosServProfileTable_Object = MibTable
rlQosServProfileTable = _RlQosServProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 99, 4)
)
if mibBuilder.loadTexts:
    rlQosServProfileTable.setStatus("current")
_RlQosServProfileEntry_Object = MibTableRow
rlQosServProfileEntry = _RlQosServProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 99, 4, 1)
)
rlQosServProfileEntry.setIndexNames(
    (0, "RADLAN-QOS-SERV", "rlQosServProfileIndex"),
)
if mibBuilder.loadTexts:
    rlQosServProfileEntry.setStatus("current")
_RlQosServProfileIndex_Type = Integer32
_RlQosServProfileIndex_Object = MibTableColumn
rlQosServProfileIndex = _RlQosServProfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 89, 99, 4, 1, 1),
    _RlQosServProfileIndex_Type()
)
rlQosServProfileIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlQosServProfileIndex.setStatus("current")


class _RlQosServProfileType_Type(Integer32):
    """Custom type rlQosServProfileType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("aggregate", 2),
          ("regular", 1))
    )


_RlQosServProfileType_Type.__name__ = "Integer32"
_RlQosServProfileType_Object = MibTableColumn
rlQosServProfileType = _RlQosServProfileType_Object(
    (1, 3, 6, 1, 4, 1, 89, 99, 4, 1, 2),
    _RlQosServProfileType_Type()
)
rlQosServProfileType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlQosServProfileType.setStatus("current")


class _RlQosServProfileServiceType_Type(Integer32):
    """Custom type rlQosServProfileServiceType based on Integer32"""
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
              7,
              8,
              9,
              10,
              11)
        )
    )
    namedValues = NamedValues(
        *(("bestEffort", 1),
          ("committedBoundBandwidth", 5),
          ("committedDelay", 3),
          ("drop", 10),
          ("dropAndDisablePort", 11),
          ("minDelay", 2),
          ("minMaxBandwidth", 4),
          ("rateLimit", 6),
          ("trust", 9),
          ("trustCos", 7),
          ("trustDscp", 8))
    )


_RlQosServProfileServiceType_Type.__name__ = "Integer32"
_RlQosServProfileServiceType_Object = MibTableColumn
rlQosServProfileServiceType = _RlQosServProfileServiceType_Object(
    (1, 3, 6, 1, 4, 1, 89, 99, 4, 1, 3),
    _RlQosServProfileServiceType_Type()
)
rlQosServProfileServiceType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlQosServProfileServiceType.setStatus("current")


class _RlQosServProfileIngressBurstSize_Type(Unsigned32):
    """Custom type rlQosServProfileIngressBurstSize based on Unsigned32"""
    defaultValue = 3000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000000),
    )


_RlQosServProfileIngressBurstSize_Type.__name__ = "Unsigned32"
_RlQosServProfileIngressBurstSize_Object = MibTableColumn
rlQosServProfileIngressBurstSize = _RlQosServProfileIngressBurstSize_Object(
    (1, 3, 6, 1, 4, 1, 89, 99, 4, 1, 4),
    _RlQosServProfileIngressBurstSize_Type()
)
rlQosServProfileIngressBurstSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlQosServProfileIngressBurstSize.setStatus("current")
if mibBuilder.loadTexts:
    rlQosServProfileIngressBurstSize.setUnits("bytes")


class _RlQosServProfileMaxBandwidth_Type(Unsigned32):
    """Custom type rlQosServProfileMaxBandwidth based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000000),
    )


_RlQosServProfileMaxBandwidth_Type.__name__ = "Unsigned32"
_RlQosServProfileMaxBandwidth_Object = MibTableColumn
rlQosServProfileMaxBandwidth = _RlQosServProfileMaxBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 89, 99, 4, 1, 5),
    _RlQosServProfileMaxBandwidth_Type()
)
rlQosServProfileMaxBandwidth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlQosServProfileMaxBandwidth.setStatus("current")
if mibBuilder.loadTexts:
    rlQosServProfileMaxBandwidth.setUnits("bytes")


class _RlQosServProfileMinBandwidth_Type(Unsigned32):
    """Custom type rlQosServProfileMinBandwidth based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000000),
    )


_RlQosServProfileMinBandwidth_Type.__name__ = "Unsigned32"
_RlQosServProfileMinBandwidth_Object = MibTableColumn
rlQosServProfileMinBandwidth = _RlQosServProfileMinBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 89, 99, 4, 1, 6),
    _RlQosServProfileMinBandwidth_Type()
)
rlQosServProfileMinBandwidth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlQosServProfileMinBandwidth.setStatus("current")
if mibBuilder.loadTexts:
    rlQosServProfileMinBandwidth.setUnits("bytes")


class _RlQosServProfileMaxDelay_Type(Unsigned32):
    """Custom type rlQosServProfileMaxDelay based on Unsigned32"""
    defaultValue = 0


_RlQosServProfileMaxDelay_Object = MibTableColumn
rlQosServProfileMaxDelay = _RlQosServProfileMaxDelay_Object(
    (1, 3, 6, 1, 4, 1, 89, 99, 4, 1, 7),
    _RlQosServProfileMaxDelay_Type()
)
rlQosServProfileMaxDelay.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlQosServProfileMaxDelay.setStatus("current")
if mibBuilder.loadTexts:
    rlQosServProfileMaxDelay.setUnits("milliseconds")
_RlQosServProfileStatus_Type = RowStatus
_RlQosServProfileStatus_Object = MibTableColumn
rlQosServProfileStatus = _RlQosServProfileStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 99, 4, 1, 8),
    _RlQosServProfileStatus_Type()
)
rlQosServProfileStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlQosServProfileStatus.setStatus("current")
_RlQosServServiceTable_Object = MibTable
rlQosServServiceTable = _RlQosServServiceTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 99, 5)
)
if mibBuilder.loadTexts:
    rlQosServServiceTable.setStatus("current")
_RlQosServServiceEntry_Object = MibTableRow
rlQosServServiceEntry = _RlQosServServiceEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 99, 5, 1)
)
rlQosServServiceEntry.setIndexNames(
    (0, "RADLAN-QOS-SERV", "rlQosServServiceIndex"),
)
if mibBuilder.loadTexts:
    rlQosServServiceEntry.setStatus("current")
_RlQosServServiceIndex_Type = Integer32
_RlQosServServiceIndex_Object = MibTableColumn
rlQosServServiceIndex = _RlQosServServiceIndex_Object(
    (1, 3, 6, 1, 4, 1, 89, 99, 5, 1, 1),
    _RlQosServServiceIndex_Type()
)
rlQosServServiceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlQosServServiceIndex.setStatus("current")


class _RlQosServServicePriority_Type(Unsigned32):
    """Custom type rlQosServServicePriority based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_RlQosServServicePriority_Type.__name__ = "Unsigned32"
_RlQosServServicePriority_Object = MibTableColumn
rlQosServServicePriority = _RlQosServServicePriority_Object(
    (1, 3, 6, 1, 4, 1, 89, 99, 5, 1, 2),
    _RlQosServServicePriority_Type()
)
rlQosServServicePriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlQosServServicePriority.setStatus("current")
_RlQosServServiceProfilePointer_Type = Integer32
_RlQosServServiceProfilePointer_Object = MibTableColumn
rlQosServServiceProfilePointer = _RlQosServServiceProfilePointer_Object(
    (1, 3, 6, 1, 4, 1, 89, 99, 5, 1, 3),
    _RlQosServServiceProfilePointer_Type()
)
rlQosServServiceProfilePointer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlQosServServiceProfilePointer.setStatus("current")
_RlQosServServiceFclPointer_Type = Integer32
_RlQosServServiceFclPointer_Object = MibTableColumn
rlQosServServiceFclPointer = _RlQosServServiceFclPointer_Object(
    (1, 3, 6, 1, 4, 1, 89, 99, 5, 1, 4),
    _RlQosServServiceFclPointer_Type()
)
rlQosServServiceFclPointer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlQosServServiceFclPointer.setStatus("current")
_RlQosServServiceInIfList_Type = PortList
_RlQosServServiceInIfList_Object = MibTableColumn
rlQosServServiceInIfList = _RlQosServServiceInIfList_Object(
    (1, 3, 6, 1, 4, 1, 89, 99, 5, 1, 5),
    _RlQosServServiceInIfList_Type()
)
rlQosServServiceInIfList.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlQosServServiceInIfList.setStatus("current")
_RlQosServServiceOutIfList_Type = PortList
_RlQosServServiceOutIfList_Object = MibTableColumn
rlQosServServiceOutIfList = _RlQosServServiceOutIfList_Object(
    (1, 3, 6, 1, 4, 1, 89, 99, 5, 1, 6),
    _RlQosServServiceOutIfList_Type()
)
rlQosServServiceOutIfList.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlQosServServiceOutIfList.setStatus("current")
_RlQosServServiceScaledOutIfList_Type = PortList
_RlQosServServiceScaledOutIfList_Object = MibTableColumn
rlQosServServiceScaledOutIfList = _RlQosServServiceScaledOutIfList_Object(
    (1, 3, 6, 1, 4, 1, 89, 99, 5, 1, 7),
    _RlQosServServiceScaledOutIfList_Type()
)
rlQosServServiceScaledOutIfList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlQosServServiceScaledOutIfList.setStatus("current")
_RlQosServServiceProfileParamOper_Type = Unsigned32
_RlQosServServiceProfileParamOper_Object = MibTableColumn
rlQosServServiceProfileParamOper = _RlQosServServiceProfileParamOper_Object(
    (1, 3, 6, 1, 4, 1, 89, 99, 5, 1, 8),
    _RlQosServServiceProfileParamOper_Type()
)
rlQosServServiceProfileParamOper.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlQosServServiceProfileParamOper.setStatus("current")
_RlQosServServiceStatusOper_Type = RlQosServServiceStatus
_RlQosServServiceStatusOper_Object = MibTableColumn
rlQosServServiceStatusOper = _RlQosServServiceStatusOper_Object(
    (1, 3, 6, 1, 4, 1, 89, 99, 5, 1, 9),
    _RlQosServServiceStatusOper_Type()
)
rlQosServServiceStatusOper.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlQosServServiceStatusOper.setStatus("current")


class _RlQosServServiceStatusAdmin_Type(RlQosServServiceStatus):
    """Custom type rlQosServServiceStatusAdmin based on RlQosServServiceStatus"""


_RlQosServServiceStatusAdmin_Object = MibTableColumn
rlQosServServiceStatusAdmin = _RlQosServServiceStatusAdmin_Object(
    (1, 3, 6, 1, 4, 1, 89, 99, 5, 1, 10),
    _RlQosServServiceStatusAdmin_Type()
)
rlQosServServiceStatusAdmin.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlQosServServiceStatusAdmin.setStatus("current")
_RlQosServServiceStatus_Type = RowStatus
_RlQosServServiceStatus_Object = MibTableColumn
rlQosServServiceStatus = _RlQosServServiceStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 99, 5, 1, 11),
    _RlQosServServiceStatus_Type()
)
rlQosServServiceStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlQosServServiceStatus.setStatus("current")
_RlQosServServicePriorityTable_Object = MibTable
rlQosServServicePriorityTable = _RlQosServServicePriorityTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 99, 6)
)
if mibBuilder.loadTexts:
    rlQosServServicePriorityTable.setStatus("current")
_RlQosServServicePriorityEntry_Object = MibTableRow
rlQosServServicePriorityEntry = _RlQosServServicePriorityEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 99, 6, 1)
)
rlQosServServicePriorityEntry.setIndexNames(
    (0, "RADLAN-QOS-SERV", "rlQosServServicePriorityIndex"),
)
if mibBuilder.loadTexts:
    rlQosServServicePriorityEntry.setStatus("current")


class _RlQosServServicePriorityIndex_Type(Integer32):
    """Custom type rlQosServServicePriorityIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_RlQosServServicePriorityIndex_Type.__name__ = "Integer32"
_RlQosServServicePriorityIndex_Object = MibTableColumn
rlQosServServicePriorityIndex = _RlQosServServicePriorityIndex_Object(
    (1, 3, 6, 1, 4, 1, 89, 99, 6, 1, 1),
    _RlQosServServicePriorityIndex_Type()
)
rlQosServServicePriorityIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlQosServServicePriorityIndex.setStatus("current")
_RlQosServServicePriorityPointer_Type = Integer32
_RlQosServServicePriorityPointer_Object = MibTableColumn
rlQosServServicePriorityPointer = _RlQosServServicePriorityPointer_Object(
    (1, 3, 6, 1, 4, 1, 89, 99, 6, 1, 2),
    _RlQosServServicePriorityPointer_Type()
)
rlQosServServicePriorityPointer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlQosServServicePriorityPointer.setStatus("current")
_RlQosServServiceDefaultMappingTable_Object = MibTable
rlQosServServiceDefaultMappingTable = _RlQosServServiceDefaultMappingTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 99, 7)
)
if mibBuilder.loadTexts:
    rlQosServServiceDefaultMappingTable.setStatus("current")
_RlQosServServiceDefaultMappingEntry_Object = MibTableRow
rlQosServServiceDefaultMappingEntry = _RlQosServServiceDefaultMappingEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 99, 7, 1)
)
rlQosServServiceDefaultMappingEntry.setIndexNames(
    (0, "RADLAN-QOS-SERV", "rlQosServServiceDefaultMappingType"),
)
if mibBuilder.loadTexts:
    rlQosServServiceDefaultMappingEntry.setStatus("current")


class _RlQosServServiceDefaultMappingType_Type(Integer32):
    """Custom type rlQosServServiceDefaultMappingType based on Integer32"""
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
        *(("bestEffort", 1),
          ("committedBoundBandwidth", 5),
          ("committedDelay", 3),
          ("minDelay", 2),
          ("minMaxBandwidth", 4),
          ("rateLimit", 6),
          ("trustDscp", 7))
    )


_RlQosServServiceDefaultMappingType_Type.__name__ = "Integer32"
_RlQosServServiceDefaultMappingType_Object = MibTableColumn
rlQosServServiceDefaultMappingType = _RlQosServServiceDefaultMappingType_Object(
    (1, 3, 6, 1, 4, 1, 89, 99, 7, 1, 1),
    _RlQosServServiceDefaultMappingType_Type()
)
rlQosServServiceDefaultMappingType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlQosServServiceDefaultMappingType.setStatus("current")


class _RlQosServServiceDefaultMappingDscp_Type(Integer32):
    """Custom type rlQosServServiceDefaultMappingDscp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 64),
    )


_RlQosServServiceDefaultMappingDscp_Type.__name__ = "Integer32"
_RlQosServServiceDefaultMappingDscp_Object = MibTableColumn
rlQosServServiceDefaultMappingDscp = _RlQosServServiceDefaultMappingDscp_Object(
    (1, 3, 6, 1, 4, 1, 89, 99, 7, 1, 2),
    _RlQosServServiceDefaultMappingDscp_Type()
)
rlQosServServiceDefaultMappingDscp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlQosServServiceDefaultMappingDscp.setStatus("current")


class _RlQosServServiceDefaultMappingVpt_Type(Integer32):
    """Custom type rlQosServServiceDefaultMappingVpt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_RlQosServServiceDefaultMappingVpt_Type.__name__ = "Integer32"
_RlQosServServiceDefaultMappingVpt_Object = MibTableColumn
rlQosServServiceDefaultMappingVpt = _RlQosServServiceDefaultMappingVpt_Object(
    (1, 3, 6, 1, 4, 1, 89, 99, 7, 1, 3),
    _RlQosServServiceDefaultMappingVpt_Type()
)
rlQosServServiceDefaultMappingVpt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlQosServServiceDefaultMappingVpt.setStatus("current")
_RlQosServScalingErrorTable_Object = MibTable
rlQosServScalingErrorTable = _RlQosServScalingErrorTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 99, 8)
)
if mibBuilder.loadTexts:
    rlQosServScalingErrorTable.setStatus("current")
_RlQosServScalingErrorEntry_Object = MibTableRow
rlQosServScalingErrorEntry = _RlQosServScalingErrorEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 99, 8, 1)
)
rlQosServScalingErrorEntry.setIndexNames(
    (0, "RADLAN-QOS-SERV", "rlQosServScalingErrorIfIndex"),
)
if mibBuilder.loadTexts:
    rlQosServScalingErrorEntry.setStatus("current")
_RlQosServScalingErrorIfIndex_Type = InterfaceIndex
_RlQosServScalingErrorIfIndex_Object = MibTableColumn
rlQosServScalingErrorIfIndex = _RlQosServScalingErrorIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 89, 99, 8, 1, 1),
    _RlQosServScalingErrorIfIndex_Type()
)
rlQosServScalingErrorIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlQosServScalingErrorIfIndex.setStatus("current")


class _RlQosServScalingErrorReason_Type(Integer32):
    """Custom type rlQosServScalingErrorReason based on Integer32"""
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
              10,
              11,
              12)
        )
    )
    namedValues = NamedValues(
        *(("changeSpeed-10000to10", 3),
          ("changeSpeed-10000to100", 2),
          ("changeSpeed-10000to1000", 1),
          ("changeSpeed-1000to10", 5),
          ("changeSpeed-1000to100", 4),
          ("changeSpeed-1000to10000", 12),
          ("changeSpeed-100to10", 6),
          ("changeSpeed-100to1000", 10),
          ("changeSpeed-100to10000", 11),
          ("changeSpeed-10to100", 7),
          ("changeSpeed-10to1000", 8),
          ("changeSpeed-10to10000", 9))
    )


_RlQosServScalingErrorReason_Type.__name__ = "Integer32"
_RlQosServScalingErrorReason_Object = MibTableColumn
rlQosServScalingErrorReason = _RlQosServScalingErrorReason_Object(
    (1, 3, 6, 1, 4, 1, 89, 99, 8, 1, 2),
    _RlQosServScalingErrorReason_Type()
)
rlQosServScalingErrorReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlQosServScalingErrorReason.setStatus("current")
_RlQosServFreeSequentialTable_Object = MibTable
rlQosServFreeSequentialTable = _RlQosServFreeSequentialTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 99, 9)
)
if mibBuilder.loadTexts:
    rlQosServFreeSequentialTable.setStatus("current")
_RlQosServFreeSequentialEntry_Object = MibTableRow
rlQosServFreeSequentialEntry = _RlQosServFreeSequentialEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 99, 9, 1)
)
rlQosServFreeSequentialEntry.setIndexNames(
    (0, "RADLAN-QOS-SERV", "rlQosServFreeSequentialId"),
)
if mibBuilder.loadTexts:
    rlQosServFreeSequentialEntry.setStatus("current")


class _RlQosServFreeSequentialId_Type(Integer32):
    """Custom type rlQosServFreeSequentialId based on Integer32"""
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
        *(("fce", 2),
          ("fcl", 1),
          ("priorityService", 5),
          ("profile", 3),
          ("service", 4))
    )


_RlQosServFreeSequentialId_Type.__name__ = "Integer32"
_RlQosServFreeSequentialId_Object = MibTableColumn
rlQosServFreeSequentialId = _RlQosServFreeSequentialId_Object(
    (1, 3, 6, 1, 4, 1, 89, 99, 9, 1, 1),
    _RlQosServFreeSequentialId_Type()
)
rlQosServFreeSequentialId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlQosServFreeSequentialId.setStatus("current")
_RlQosServFreeSequentialValue_Type = Integer32
_RlQosServFreeSequentialValue_Object = MibTableColumn
rlQosServFreeSequentialValue = _RlQosServFreeSequentialValue_Object(
    (1, 3, 6, 1, 4, 1, 89, 99, 9, 1, 2),
    _RlQosServFreeSequentialValue_Type()
)
rlQosServFreeSequentialValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlQosServFreeSequentialValue.setStatus("current")
_RlQosServNameToIndexTable_Object = MibTable
rlQosServNameToIndexTable = _RlQosServNameToIndexTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 99, 10)
)
if mibBuilder.loadTexts:
    rlQosServNameToIndexTable.setStatus("current")
_RlQosServNameToIndexEntry_Object = MibTableRow
rlQosServNameToIndexEntry = _RlQosServNameToIndexEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 99, 10, 1)
)
rlQosServNameToIndexEntry.setIndexNames(
    (0, "RADLAN-QOS-SERV", "rlQosServNameToIndexTableId"),
    (0, "RADLAN-QOS-SERV", "rlQosServNameToIndexName"),
)
if mibBuilder.loadTexts:
    rlQosServNameToIndexEntry.setStatus("current")
_RlQosServNameToIndexTableId_Type = RlQosServNamedTableId
_RlQosServNameToIndexTableId_Object = MibTableColumn
rlQosServNameToIndexTableId = _RlQosServNameToIndexTableId_Object(
    (1, 3, 6, 1, 4, 1, 89, 99, 10, 1, 1),
    _RlQosServNameToIndexTableId_Type()
)
rlQosServNameToIndexTableId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlQosServNameToIndexTableId.setStatus("current")


class _RlQosServNameToIndexName_Type(DisplayString):
    """Custom type rlQosServNameToIndexName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_RlQosServNameToIndexName_Type.__name__ = "DisplayString"
_RlQosServNameToIndexName_Object = MibTableColumn
rlQosServNameToIndexName = _RlQosServNameToIndexName_Object(
    (1, 3, 6, 1, 4, 1, 89, 99, 10, 1, 2),
    _RlQosServNameToIndexName_Type()
)
rlQosServNameToIndexName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlQosServNameToIndexName.setStatus("current")
_RlQosServNameToIndexValue_Type = Integer32
_RlQosServNameToIndexValue_Object = MibTableColumn
rlQosServNameToIndexValue = _RlQosServNameToIndexValue_Object(
    (1, 3, 6, 1, 4, 1, 89, 99, 10, 1, 3),
    _RlQosServNameToIndexValue_Type()
)
rlQosServNameToIndexValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlQosServNameToIndexValue.setStatus("current")
_RlQosServNameToIndexStatus_Type = RowStatus
_RlQosServNameToIndexStatus_Object = MibTableColumn
rlQosServNameToIndexStatus = _RlQosServNameToIndexStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 99, 10, 1, 4),
    _RlQosServNameToIndexStatus_Type()
)
rlQosServNameToIndexStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlQosServNameToIndexStatus.setStatus("current")
_RlQosServIndexToNameTable_Object = MibTable
rlQosServIndexToNameTable = _RlQosServIndexToNameTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 99, 11)
)
if mibBuilder.loadTexts:
    rlQosServIndexToNameTable.setStatus("current")
_RlQosServIndexToNameEntry_Object = MibTableRow
rlQosServIndexToNameEntry = _RlQosServIndexToNameEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 99, 11, 1)
)
rlQosServIndexToNameEntry.setIndexNames(
    (0, "RADLAN-QOS-SERV", "rlQosServIndexToNameTableId"),
    (0, "RADLAN-QOS-SERV", "rlQosServIndexToNameIndex"),
)
if mibBuilder.loadTexts:
    rlQosServIndexToNameEntry.setStatus("current")
_RlQosServIndexToNameTableId_Type = RlQosServNamedTableId
_RlQosServIndexToNameTableId_Object = MibTableColumn
rlQosServIndexToNameTableId = _RlQosServIndexToNameTableId_Object(
    (1, 3, 6, 1, 4, 1, 89, 99, 11, 1, 1),
    _RlQosServIndexToNameTableId_Type()
)
rlQosServIndexToNameTableId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlQosServIndexToNameTableId.setStatus("current")
_RlQosServIndexToNameIndex_Type = Integer32
_RlQosServIndexToNameIndex_Object = MibTableColumn
rlQosServIndexToNameIndex = _RlQosServIndexToNameIndex_Object(
    (1, 3, 6, 1, 4, 1, 89, 99, 11, 1, 2),
    _RlQosServIndexToNameIndex_Type()
)
rlQosServIndexToNameIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlQosServIndexToNameIndex.setStatus("current")


class _RlQosServIndexToNameValue_Type(DisplayString):
    """Custom type rlQosServIndexToNameValue based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_RlQosServIndexToNameValue_Type.__name__ = "DisplayString"
_RlQosServIndexToNameValue_Object = MibTableColumn
rlQosServIndexToNameValue = _RlQosServIndexToNameValue_Object(
    (1, 3, 6, 1, 4, 1, 89, 99, 11, 1, 3),
    _RlQosServIndexToNameValue_Type()
)
rlQosServIndexToNameValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlQosServIndexToNameValue.setStatus("current")
_RlQosServMibVersion_Type = Integer32
_RlQosServMibVersion_Object = MibScalar
rlQosServMibVersion = _RlQosServMibVersion_Object(
    (1, 3, 6, 1, 4, 1, 89, 99, 12),
    _RlQosServMibVersion_Type()
)
rlQosServMibVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlQosServMibVersion.setStatus("current")


class _RlQosServMibAction_Type(Integer32):
    """Custom type rlQosServMibAction based on Integer32"""
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
        *(("flatServicePriorities", 4),
          ("importPolicy", 2),
          ("noImportPolicy", 3),
          ("none", 1))
    )


_RlQosServMibAction_Type.__name__ = "Integer32"
_RlQosServMibAction_Object = MibScalar
rlQosServMibAction = _RlQosServMibAction_Object(
    (1, 3, 6, 1, 4, 1, 89, 99, 13),
    _RlQosServMibAction_Type()
)
rlQosServMibAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlQosServMibAction.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RADLAN-QOS-SERV",
    **{"RlQosServServiceStatus": RlQosServServiceStatus,
       "RlQosServNamedTableId": RlQosServNamedTableId,
       "rlQosServ": rlQosServ,
       "rlQosServTemplateTable": rlQosServTemplateTable,
       "rlQosServTemplateEntry": rlQosServTemplateEntry,
       "rlQosServTemplateIndex": rlQosServTemplateIndex,
       "rlQosServTemplateDestMac": rlQosServTemplateDestMac,
       "rlQosServTemplateDestMacMask": rlQosServTemplateDestMacMask,
       "rlQosServTemplateSrcMac": rlQosServTemplateSrcMac,
       "rlQosServTemplateSrcMacMask": rlQosServTemplateSrcMacMask,
       "rlQosServTemplateVlan": rlQosServTemplateVlan,
       "rlQosServTemplateDestIp": rlQosServTemplateDestIp,
       "rlQosServTemplateDestIpMask": rlQosServTemplateDestIpMask,
       "rlQosServTemplateSrcIp": rlQosServTemplateSrcIp,
       "rlQosServTemplateSrcIpMask": rlQosServTemplateSrcIpMask,
       "rlQosServTemplateIpProtocol": rlQosServTemplateIpProtocol,
       "rlQosServTemplateSrcPort": rlQosServTemplateSrcPort,
       "rlQosServTemplateDestPort": rlQosServTemplateDestPort,
       "rlQosServTemplateTos": rlQosServTemplateTos,
       "rlQosServTemplateVpt": rlQosServTemplateVpt,
       "rlQosServTemplateEtherType": rlQosServTemplateEtherType,
       "rlQosServTemplateTcpFlags": rlQosServTemplateTcpFlags,
       "rlQosServTemplateIcmpType": rlQosServTemplateIcmpType,
       "rlQosServTemplateIcmpCode": rlQosServTemplateIcmpCode,
       "rlQosServTemplateIgmpType": rlQosServTemplateIgmpType,
       "rlQosServFclTable": rlQosServFclTable,
       "rlQosServFclEntry": rlQosServFclEntry,
       "rlQosServFclIndex": rlQosServFclIndex,
       "rlQosServFclFcePriority": rlQosServFclFcePriority,
       "rlQosServFclFceIndex": rlQosServFclFceIndex,
       "rlQosServFclStatus": rlQosServFclStatus,
       "rlQosServFceTable": rlQosServFceTable,
       "rlQosServFceEntry": rlQosServFceEntry,
       "rlQosServFceIndex": rlQosServFceIndex,
       "rlQosServFceErrorCode": rlQosServFceErrorCode,
       "rlQosServFceSelection": rlQosServFceSelection,
       "rlQosServFceDestMac": rlQosServFceDestMac,
       "rlQosServFceDestMacMask": rlQosServFceDestMacMask,
       "rlQosServFceSrcMac": rlQosServFceSrcMac,
       "rlQosServFceSrcMacMask": rlQosServFceSrcMacMask,
       "rlQosServFceVlan": rlQosServFceVlan,
       "rlQosServFceVlanMask": rlQosServFceVlanMask,
       "rlQosServFceDestIp": rlQosServFceDestIp,
       "rlQosServFceDestIpMask": rlQosServFceDestIpMask,
       "rlQosServFceSrcIp": rlQosServFceSrcIp,
       "rlQosServFceSrcIpMask": rlQosServFceSrcIpMask,
       "rlQosServFceIpProtocol": rlQosServFceIpProtocol,
       "rlQosServFceDestPort": rlQosServFceDestPort,
       "rlQosServFceDestPortMask": rlQosServFceDestPortMask,
       "rlQosServFceSrcPort": rlQosServFceSrcPort,
       "rlQosServFceSrcPortMask": rlQosServFceSrcPortMask,
       "rlQosServFceDscp": rlQosServFceDscp,
       "rlQosServFceIpPrecedence": rlQosServFceIpPrecedence,
       "rlQosServFceVpt": rlQosServFceVpt,
       "rlQosServFceVptMask": rlQosServFceVptMask,
       "rlQosServFceEtherType": rlQosServFceEtherType,
       "rlQosServFceTcpFlags": rlQosServFceTcpFlags,
       "rlQosServFceTcpFlagsMask": rlQosServFceTcpFlagsMask,
       "rlQosServFceIcmpType": rlQosServFceIcmpType,
       "rlQosServFceIcmpCode": rlQosServFceIcmpCode,
       "rlQosServFceIgmpType": rlQosServFceIgmpType,
       "rlQosServFceStatus": rlQosServFceStatus,
       "rlQosServProfileTable": rlQosServProfileTable,
       "rlQosServProfileEntry": rlQosServProfileEntry,
       "rlQosServProfileIndex": rlQosServProfileIndex,
       "rlQosServProfileType": rlQosServProfileType,
       "rlQosServProfileServiceType": rlQosServProfileServiceType,
       "rlQosServProfileIngressBurstSize": rlQosServProfileIngressBurstSize,
       "rlQosServProfileMaxBandwidth": rlQosServProfileMaxBandwidth,
       "rlQosServProfileMinBandwidth": rlQosServProfileMinBandwidth,
       "rlQosServProfileMaxDelay": rlQosServProfileMaxDelay,
       "rlQosServProfileStatus": rlQosServProfileStatus,
       "rlQosServServiceTable": rlQosServServiceTable,
       "rlQosServServiceEntry": rlQosServServiceEntry,
       "rlQosServServiceIndex": rlQosServServiceIndex,
       "rlQosServServicePriority": rlQosServServicePriority,
       "rlQosServServiceProfilePointer": rlQosServServiceProfilePointer,
       "rlQosServServiceFclPointer": rlQosServServiceFclPointer,
       "rlQosServServiceInIfList": rlQosServServiceInIfList,
       "rlQosServServiceOutIfList": rlQosServServiceOutIfList,
       "rlQosServServiceScaledOutIfList": rlQosServServiceScaledOutIfList,
       "rlQosServServiceProfileParamOper": rlQosServServiceProfileParamOper,
       "rlQosServServiceStatusOper": rlQosServServiceStatusOper,
       "rlQosServServiceStatusAdmin": rlQosServServiceStatusAdmin,
       "rlQosServServiceStatus": rlQosServServiceStatus,
       "rlQosServServicePriorityTable": rlQosServServicePriorityTable,
       "rlQosServServicePriorityEntry": rlQosServServicePriorityEntry,
       "rlQosServServicePriorityIndex": rlQosServServicePriorityIndex,
       "rlQosServServicePriorityPointer": rlQosServServicePriorityPointer,
       "rlQosServServiceDefaultMappingTable": rlQosServServiceDefaultMappingTable,
       "rlQosServServiceDefaultMappingEntry": rlQosServServiceDefaultMappingEntry,
       "rlQosServServiceDefaultMappingType": rlQosServServiceDefaultMappingType,
       "rlQosServServiceDefaultMappingDscp": rlQosServServiceDefaultMappingDscp,
       "rlQosServServiceDefaultMappingVpt": rlQosServServiceDefaultMappingVpt,
       "rlQosServScalingErrorTable": rlQosServScalingErrorTable,
       "rlQosServScalingErrorEntry": rlQosServScalingErrorEntry,
       "rlQosServScalingErrorIfIndex": rlQosServScalingErrorIfIndex,
       "rlQosServScalingErrorReason": rlQosServScalingErrorReason,
       "rlQosServFreeSequentialTable": rlQosServFreeSequentialTable,
       "rlQosServFreeSequentialEntry": rlQosServFreeSequentialEntry,
       "rlQosServFreeSequentialId": rlQosServFreeSequentialId,
       "rlQosServFreeSequentialValue": rlQosServFreeSequentialValue,
       "rlQosServNameToIndexTable": rlQosServNameToIndexTable,
       "rlQosServNameToIndexEntry": rlQosServNameToIndexEntry,
       "rlQosServNameToIndexTableId": rlQosServNameToIndexTableId,
       "rlQosServNameToIndexName": rlQosServNameToIndexName,
       "rlQosServNameToIndexValue": rlQosServNameToIndexValue,
       "rlQosServNameToIndexStatus": rlQosServNameToIndexStatus,
       "rlQosServIndexToNameTable": rlQosServIndexToNameTable,
       "rlQosServIndexToNameEntry": rlQosServIndexToNameEntry,
       "rlQosServIndexToNameTableId": rlQosServIndexToNameTableId,
       "rlQosServIndexToNameIndex": rlQosServIndexToNameIndex,
       "rlQosServIndexToNameValue": rlQosServIndexToNameValue,
       "rlQosServMibVersion": rlQosServMibVersion,
       "rlQosServMibAction": rlQosServMibAction}
)
