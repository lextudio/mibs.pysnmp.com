# SNMP MIB module (LBHUB-REPEATER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/LBHUB-REPEATER-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:17:30 2024
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
 NotificationType,
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
    "NotificationType",
    "TimeTicks",
    "Unsigned32",
    "enterprises",
    "iso",
    "mgmt")

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions



class DisplayString(OctetString):
    """Custom type DisplayString based on OctetString"""




class PhysAddress(OctetString):
    """Custom type PhysAddress based on OctetString"""




class MacAddress(OctetString):
    """Custom type MacAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Mib_2_ObjectIdentity = ObjectIdentity
mib_2 = _Mib_2_ObjectIdentity(
    (1, 3, 6, 1, 2, 1)
)
_System_ObjectIdentity = ObjectIdentity
system = _System_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 1)
)
_Interfaces_ObjectIdentity = ObjectIdentity
interfaces = _Interfaces_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 2)
)
_At_ObjectIdentity = ObjectIdentity
at = _At_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 3)
)
_Ip_ObjectIdentity = ObjectIdentity
ip = _Ip_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 4)
)
_Icmp_ObjectIdentity = ObjectIdentity
icmp = _Icmp_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 5)
)
_Tcp_ObjectIdentity = ObjectIdentity
tcp = _Tcp_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 6)
)
_Udp_ObjectIdentity = ObjectIdentity
udp = _Udp_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 7)
)
_Egp_ObjectIdentity = ObjectIdentity
egp = _Egp_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 8)
)
_Transmission_ObjectIdentity = ObjectIdentity
transmission = _Transmission_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10)
)
_Snmp_ObjectIdentity = ObjectIdentity
snmp = _Snmp_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 11)
)
_Dot1dBridge_ObjectIdentity = ObjectIdentity
dot1dBridge = _Dot1dBridge_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 17)
)
_SnmpDot3RptrMgt_ObjectIdentity = ObjectIdentity
snmpDot3RptrMgt = _SnmpDot3RptrMgt_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 22)
)
_RptrBasicPackage_ObjectIdentity = ObjectIdentity
rptrBasicPackage = _RptrBasicPackage_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 22, 1)
)
_RptrRptrInfo_ObjectIdentity = ObjectIdentity
rptrRptrInfo = _RptrRptrInfo_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 22, 1, 1)
)


class _RptrGroupCapacity_Type(Integer32):
    """Custom type rptrGroupCapacity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_RptrGroupCapacity_Type.__name__ = "Integer32"
_RptrGroupCapacity_Object = MibScalar
rptrGroupCapacity = _RptrGroupCapacity_Object(
    (1, 3, 6, 1, 2, 1, 22, 1, 1, 1),
    _RptrGroupCapacity_Type()
)
rptrGroupCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrGroupCapacity.setStatus("mandatory")


class _RptrOperSTATUS_Type(Integer32):
    """Custom type rptrOperSTATUS based on Integer32"""
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
        *(("generalFailure", 6),
          ("groupFailure", 4),
          ("ok", 2),
          ("other", 1),
          ("portFailure", 5),
          ("rptrFailure", 3))
    )


_RptrOperSTATUS_Type.__name__ = "Integer32"
_RptrOperSTATUS_Object = MibScalar
rptrOperSTATUS = _RptrOperSTATUS_Object(
    (1, 3, 6, 1, 2, 1, 22, 1, 1, 2),
    _RptrOperSTATUS_Type()
)
rptrOperSTATUS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrOperSTATUS.setStatus("mandatory")


class _RptrHealthText_Type(DisplayString):
    """Custom type rptrHealthText based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_RptrHealthText_Type.__name__ = "DisplayString"
_RptrHealthText_Object = MibScalar
rptrHealthText = _RptrHealthText_Object(
    (1, 3, 6, 1, 2, 1, 22, 1, 1, 3),
    _RptrHealthText_Type()
)
rptrHealthText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrHealthText.setStatus("mandatory")


class _RptrReset_Type(Integer32):
    """Custom type rptrReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noReset", 1),
          ("reset", 2))
    )


_RptrReset_Type.__name__ = "Integer32"
_RptrReset_Object = MibScalar
rptrReset = _RptrReset_Object(
    (1, 3, 6, 1, 2, 1, 22, 1, 1, 4),
    _RptrReset_Type()
)
rptrReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rptrReset.setStatus("mandatory")


class _RptrNonDisruptTest_Type(Integer32):
    """Custom type rptrNonDisruptTest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noSelfTest", 1),
          ("selfTest", 2))
    )


_RptrNonDisruptTest_Type.__name__ = "Integer32"
_RptrNonDisruptTest_Object = MibScalar
rptrNonDisruptTest = _RptrNonDisruptTest_Object(
    (1, 3, 6, 1, 2, 1, 22, 1, 1, 5),
    _RptrNonDisruptTest_Type()
)
rptrNonDisruptTest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rptrNonDisruptTest.setStatus("mandatory")
_RptrTotalPartitionedPorts_Type = Gauge32
_RptrTotalPartitionedPorts_Object = MibScalar
rptrTotalPartitionedPorts = _RptrTotalPartitionedPorts_Object(
    (1, 3, 6, 1, 2, 1, 22, 1, 1, 6),
    _RptrTotalPartitionedPorts_Type()
)
rptrTotalPartitionedPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrTotalPartitionedPorts.setStatus("mandatory")
_RptrGroupInfo_ObjectIdentity = ObjectIdentity
rptrGroupInfo = _RptrGroupInfo_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 22, 1, 2)
)
_RptrGroupTable_Object = MibTable
rptrGroupTable = _RptrGroupTable_Object(
    (1, 3, 6, 1, 2, 1, 22, 1, 2, 1)
)
if mibBuilder.loadTexts:
    rptrGroupTable.setStatus("mandatory")
_RptrGroupEntry_Object = MibTableRow
rptrGroupEntry = _RptrGroupEntry_Object(
    (1, 3, 6, 1, 2, 1, 22, 1, 2, 1, 1)
)
rptrGroupEntry.setIndexNames(
    (0, "LBHUB-REPEATER-MIB", "rptrGroupIndex"),
)
if mibBuilder.loadTexts:
    rptrGroupEntry.setStatus("mandatory")


class _RptrGroupIndex_Type(Integer32):
    """Custom type rptrGroupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_RptrGroupIndex_Type.__name__ = "Integer32"
_RptrGroupIndex_Object = MibTableColumn
rptrGroupIndex = _RptrGroupIndex_Object(
    (1, 3, 6, 1, 2, 1, 22, 1, 2, 1, 1, 1),
    _RptrGroupIndex_Type()
)
rptrGroupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrGroupIndex.setStatus("mandatory")


class _RptrGroupDescr_Type(DisplayString):
    """Custom type rptrGroupDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_RptrGroupDescr_Type.__name__ = "DisplayString"
_RptrGroupDescr_Object = MibTableColumn
rptrGroupDescr = _RptrGroupDescr_Object(
    (1, 3, 6, 1, 2, 1, 22, 1, 2, 1, 1, 2),
    _RptrGroupDescr_Type()
)
rptrGroupDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrGroupDescr.setStatus("mandatory")
_RptrGroupObjectID_Type = ObjectIdentifier
_RptrGroupObjectID_Object = MibTableColumn
rptrGroupObjectID = _RptrGroupObjectID_Object(
    (1, 3, 6, 1, 2, 1, 22, 1, 2, 1, 1, 3),
    _RptrGroupObjectID_Type()
)
rptrGroupObjectID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrGroupObjectID.setStatus("mandatory")


class _RptrGroupOperSTATUS_Type(Integer32):
    """Custom type rptrGroupOperSTATUS based on Integer32"""
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
        *(("malfunctioning", 3),
          ("notPresent", 4),
          ("operational", 2),
          ("other", 1),
          ("resetInProgress", 6),
          ("underTest", 5))
    )


_RptrGroupOperSTATUS_Type.__name__ = "Integer32"
_RptrGroupOperSTATUS_Object = MibTableColumn
rptrGroupOperSTATUS = _RptrGroupOperSTATUS_Object(
    (1, 3, 6, 1, 2, 1, 22, 1, 2, 1, 1, 4),
    _RptrGroupOperSTATUS_Type()
)
rptrGroupOperSTATUS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrGroupOperSTATUS.setStatus("mandatory")
_RptrGroupLastOperSTATUSChange_Type = TimeTicks
_RptrGroupLastOperSTATUSChange_Object = MibTableColumn
rptrGroupLastOperSTATUSChange = _RptrGroupLastOperSTATUSChange_Object(
    (1, 3, 6, 1, 2, 1, 22, 1, 2, 1, 1, 5),
    _RptrGroupLastOperSTATUSChange_Type()
)
rptrGroupLastOperSTATUSChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrGroupLastOperSTATUSChange.setStatus("mandatory")


class _RptrGroupPortCapacity_Type(Integer32):
    """Custom type rptrGroupPortCapacity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_RptrGroupPortCapacity_Type.__name__ = "Integer32"
_RptrGroupPortCapacity_Object = MibTableColumn
rptrGroupPortCapacity = _RptrGroupPortCapacity_Object(
    (1, 3, 6, 1, 2, 1, 22, 1, 2, 1, 1, 6),
    _RptrGroupPortCapacity_Type()
)
rptrGroupPortCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrGroupPortCapacity.setStatus("mandatory")
_RptrPortInfo_ObjectIdentity = ObjectIdentity
rptrPortInfo = _RptrPortInfo_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 22, 1, 3)
)
_RptrPortTable_Object = MibTable
rptrPortTable = _RptrPortTable_Object(
    (1, 3, 6, 1, 2, 1, 22, 1, 3, 1)
)
if mibBuilder.loadTexts:
    rptrPortTable.setStatus("mandatory")
_RptrPortEntry_Object = MibTableRow
rptrPortEntry = _RptrPortEntry_Object(
    (1, 3, 6, 1, 2, 1, 22, 1, 3, 1, 1)
)
rptrPortEntry.setIndexNames(
    (0, "LBHUB-REPEATER-MIB", "rptrPortGroupIndex"),
    (0, "LBHUB-REPEATER-MIB", "rptrPortIndex"),
)
if mibBuilder.loadTexts:
    rptrPortEntry.setStatus("mandatory")


class _RptrPortGroupIndex_Type(Integer32):
    """Custom type rptrPortGroupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_RptrPortGroupIndex_Type.__name__ = "Integer32"
_RptrPortGroupIndex_Object = MibTableColumn
rptrPortGroupIndex = _RptrPortGroupIndex_Object(
    (1, 3, 6, 1, 2, 1, 22, 1, 3, 1, 1, 1),
    _RptrPortGroupIndex_Type()
)
rptrPortGroupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrPortGroupIndex.setStatus("mandatory")


class _RptrPortIndex_Type(Integer32):
    """Custom type rptrPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_RptrPortIndex_Type.__name__ = "Integer32"
_RptrPortIndex_Object = MibTableColumn
rptrPortIndex = _RptrPortIndex_Object(
    (1, 3, 6, 1, 2, 1, 22, 1, 3, 1, 1, 2),
    _RptrPortIndex_Type()
)
rptrPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrPortIndex.setStatus("mandatory")


class _RptrPortAdminSTATUS_Type(Integer32):
    """Custom type rptrPortAdminSTATUS based on Integer32"""
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


_RptrPortAdminSTATUS_Type.__name__ = "Integer32"
_RptrPortAdminSTATUS_Object = MibTableColumn
rptrPortAdminSTATUS = _RptrPortAdminSTATUS_Object(
    (1, 3, 6, 1, 2, 1, 22, 1, 3, 1, 1, 3),
    _RptrPortAdminSTATUS_Type()
)
rptrPortAdminSTATUS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rptrPortAdminSTATUS.setStatus("mandatory")


class _RptrPortAutoPartitionState_Type(Integer32):
    """Custom type rptrPortAutoPartitionState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("autoPartitioned", 2),
          ("notAutoPartitioned", 1))
    )


_RptrPortAutoPartitionState_Type.__name__ = "Integer32"
_RptrPortAutoPartitionState_Object = MibTableColumn
rptrPortAutoPartitionState = _RptrPortAutoPartitionState_Object(
    (1, 3, 6, 1, 2, 1, 22, 1, 3, 1, 1, 4),
    _RptrPortAutoPartitionState_Type()
)
rptrPortAutoPartitionState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrPortAutoPartitionState.setStatus("mandatory")


class _RptrPortOperSTATUS_Type(Integer32):
    """Custom type rptrPortOperSTATUS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notOperational", 2),
          ("notPresent", 3),
          ("operational", 1))
    )


_RptrPortOperSTATUS_Type.__name__ = "Integer32"
_RptrPortOperSTATUS_Object = MibTableColumn
rptrPortOperSTATUS = _RptrPortOperSTATUS_Object(
    (1, 3, 6, 1, 2, 1, 22, 1, 3, 1, 1, 5),
    _RptrPortOperSTATUS_Type()
)
rptrPortOperSTATUS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrPortOperSTATUS.setStatus("mandatory")
_RptrMonitorPackage_ObjectIdentity = ObjectIdentity
rptrMonitorPackage = _RptrMonitorPackage_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 22, 2)
)
_RptrMonitorRptrInfo_ObjectIdentity = ObjectIdentity
rptrMonitorRptrInfo = _RptrMonitorRptrInfo_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 22, 2, 1)
)
_RptrMonitorTransmitCollisions_Type = Counter32
_RptrMonitorTransmitCollisions_Object = MibScalar
rptrMonitorTransmitCollisions = _RptrMonitorTransmitCollisions_Object(
    (1, 3, 6, 1, 2, 1, 22, 2, 1, 1),
    _RptrMonitorTransmitCollisions_Type()
)
rptrMonitorTransmitCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrMonitorTransmitCollisions.setStatus("mandatory")
_RptrMonitorGroupInfo_ObjectIdentity = ObjectIdentity
rptrMonitorGroupInfo = _RptrMonitorGroupInfo_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 22, 2, 2)
)
_RptrMonitorGroupTable_Object = MibTable
rptrMonitorGroupTable = _RptrMonitorGroupTable_Object(
    (1, 3, 6, 1, 2, 1, 22, 2, 2, 1)
)
if mibBuilder.loadTexts:
    rptrMonitorGroupTable.setStatus("mandatory")
_RptrMonitorGroupEntry_Object = MibTableRow
rptrMonitorGroupEntry = _RptrMonitorGroupEntry_Object(
    (1, 3, 6, 1, 2, 1, 22, 2, 2, 1, 1)
)
rptrMonitorGroupEntry.setIndexNames(
    (0, "LBHUB-REPEATER-MIB", "rptrMonitorGroupIndex"),
)
if mibBuilder.loadTexts:
    rptrMonitorGroupEntry.setStatus("mandatory")


class _RptrMonitorGroupIndex_Type(Integer32):
    """Custom type rptrMonitorGroupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_RptrMonitorGroupIndex_Type.__name__ = "Integer32"
_RptrMonitorGroupIndex_Object = MibTableColumn
rptrMonitorGroupIndex = _RptrMonitorGroupIndex_Object(
    (1, 3, 6, 1, 2, 1, 22, 2, 2, 1, 1, 1),
    _RptrMonitorGroupIndex_Type()
)
rptrMonitorGroupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrMonitorGroupIndex.setStatus("mandatory")
_RptrMonitorGroupTotalFrames_Type = Counter32
_RptrMonitorGroupTotalFrames_Object = MibTableColumn
rptrMonitorGroupTotalFrames = _RptrMonitorGroupTotalFrames_Object(
    (1, 3, 6, 1, 2, 1, 22, 2, 2, 1, 1, 2),
    _RptrMonitorGroupTotalFrames_Type()
)
rptrMonitorGroupTotalFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrMonitorGroupTotalFrames.setStatus("mandatory")
_RptrMonitorGroupTotalOctets_Type = Counter32
_RptrMonitorGroupTotalOctets_Object = MibTableColumn
rptrMonitorGroupTotalOctets = _RptrMonitorGroupTotalOctets_Object(
    (1, 3, 6, 1, 2, 1, 22, 2, 2, 1, 1, 3),
    _RptrMonitorGroupTotalOctets_Type()
)
rptrMonitorGroupTotalOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrMonitorGroupTotalOctets.setStatus("mandatory")
_RptrMonitorGroupTotalErrors_Type = Counter32
_RptrMonitorGroupTotalErrors_Object = MibTableColumn
rptrMonitorGroupTotalErrors = _RptrMonitorGroupTotalErrors_Object(
    (1, 3, 6, 1, 2, 1, 22, 2, 2, 1, 1, 4),
    _RptrMonitorGroupTotalErrors_Type()
)
rptrMonitorGroupTotalErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrMonitorGroupTotalErrors.setStatus("mandatory")
_RptrMonitorPortInfo_ObjectIdentity = ObjectIdentity
rptrMonitorPortInfo = _RptrMonitorPortInfo_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 22, 2, 3)
)
_RptrMonitorPortTable_Object = MibTable
rptrMonitorPortTable = _RptrMonitorPortTable_Object(
    (1, 3, 6, 1, 2, 1, 22, 2, 3, 1)
)
if mibBuilder.loadTexts:
    rptrMonitorPortTable.setStatus("mandatory")
_RptrMonitorPortEntry_Object = MibTableRow
rptrMonitorPortEntry = _RptrMonitorPortEntry_Object(
    (1, 3, 6, 1, 2, 1, 22, 2, 3, 1, 1)
)
rptrMonitorPortEntry.setIndexNames(
    (0, "LBHUB-REPEATER-MIB", "rptrMonitorPortGroupIndex"),
    (0, "LBHUB-REPEATER-MIB", "rptrMonitorPortIndex"),
)
if mibBuilder.loadTexts:
    rptrMonitorPortEntry.setStatus("mandatory")


class _RptrMonitorPortGroupIndex_Type(Integer32):
    """Custom type rptrMonitorPortGroupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_RptrMonitorPortGroupIndex_Type.__name__ = "Integer32"
_RptrMonitorPortGroupIndex_Object = MibTableColumn
rptrMonitorPortGroupIndex = _RptrMonitorPortGroupIndex_Object(
    (1, 3, 6, 1, 2, 1, 22, 2, 3, 1, 1, 1),
    _RptrMonitorPortGroupIndex_Type()
)
rptrMonitorPortGroupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrMonitorPortGroupIndex.setStatus("mandatory")


class _RptrMonitorPortIndex_Type(Integer32):
    """Custom type rptrMonitorPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_RptrMonitorPortIndex_Type.__name__ = "Integer32"
_RptrMonitorPortIndex_Object = MibTableColumn
rptrMonitorPortIndex = _RptrMonitorPortIndex_Object(
    (1, 3, 6, 1, 2, 1, 22, 2, 3, 1, 1, 2),
    _RptrMonitorPortIndex_Type()
)
rptrMonitorPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrMonitorPortIndex.setStatus("mandatory")
_RptrMonitorPortReadableFrames_Type = Counter32
_RptrMonitorPortReadableFrames_Object = MibTableColumn
rptrMonitorPortReadableFrames = _RptrMonitorPortReadableFrames_Object(
    (1, 3, 6, 1, 2, 1, 22, 2, 3, 1, 1, 3),
    _RptrMonitorPortReadableFrames_Type()
)
rptrMonitorPortReadableFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrMonitorPortReadableFrames.setStatus("mandatory")
_RptrMonitorPortReadableOctets_Type = Counter32
_RptrMonitorPortReadableOctets_Object = MibTableColumn
rptrMonitorPortReadableOctets = _RptrMonitorPortReadableOctets_Object(
    (1, 3, 6, 1, 2, 1, 22, 2, 3, 1, 1, 4),
    _RptrMonitorPortReadableOctets_Type()
)
rptrMonitorPortReadableOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrMonitorPortReadableOctets.setStatus("mandatory")
_RptrMonitorPortFCSErrors_Type = Counter32
_RptrMonitorPortFCSErrors_Object = MibTableColumn
rptrMonitorPortFCSErrors = _RptrMonitorPortFCSErrors_Object(
    (1, 3, 6, 1, 2, 1, 22, 2, 3, 1, 1, 5),
    _RptrMonitorPortFCSErrors_Type()
)
rptrMonitorPortFCSErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrMonitorPortFCSErrors.setStatus("mandatory")
_RptrMonitorPortAlignmentErrors_Type = Counter32
_RptrMonitorPortAlignmentErrors_Object = MibTableColumn
rptrMonitorPortAlignmentErrors = _RptrMonitorPortAlignmentErrors_Object(
    (1, 3, 6, 1, 2, 1, 22, 2, 3, 1, 1, 6),
    _RptrMonitorPortAlignmentErrors_Type()
)
rptrMonitorPortAlignmentErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrMonitorPortAlignmentErrors.setStatus("mandatory")
_RptrMonitorPortFrameTooLongs_Type = Counter32
_RptrMonitorPortFrameTooLongs_Object = MibTableColumn
rptrMonitorPortFrameTooLongs = _RptrMonitorPortFrameTooLongs_Object(
    (1, 3, 6, 1, 2, 1, 22, 2, 3, 1, 1, 7),
    _RptrMonitorPortFrameTooLongs_Type()
)
rptrMonitorPortFrameTooLongs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrMonitorPortFrameTooLongs.setStatus("mandatory")
_RptrMonitorPortShortEvents_Type = Counter32
_RptrMonitorPortShortEvents_Object = MibTableColumn
rptrMonitorPortShortEvents = _RptrMonitorPortShortEvents_Object(
    (1, 3, 6, 1, 2, 1, 22, 2, 3, 1, 1, 8),
    _RptrMonitorPortShortEvents_Type()
)
rptrMonitorPortShortEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrMonitorPortShortEvents.setStatus("mandatory")
_RptrMonitorPortRunts_Type = Counter32
_RptrMonitorPortRunts_Object = MibTableColumn
rptrMonitorPortRunts = _RptrMonitorPortRunts_Object(
    (1, 3, 6, 1, 2, 1, 22, 2, 3, 1, 1, 9),
    _RptrMonitorPortRunts_Type()
)
rptrMonitorPortRunts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrMonitorPortRunts.setStatus("mandatory")
_RptrMonitorPortCollisions_Type = Counter32
_RptrMonitorPortCollisions_Object = MibTableColumn
rptrMonitorPortCollisions = _RptrMonitorPortCollisions_Object(
    (1, 3, 6, 1, 2, 1, 22, 2, 3, 1, 1, 10),
    _RptrMonitorPortCollisions_Type()
)
rptrMonitorPortCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrMonitorPortCollisions.setStatus("mandatory")
_RptrMonitorPortLateEvents_Type = Counter32
_RptrMonitorPortLateEvents_Object = MibTableColumn
rptrMonitorPortLateEvents = _RptrMonitorPortLateEvents_Object(
    (1, 3, 6, 1, 2, 1, 22, 2, 3, 1, 1, 11),
    _RptrMonitorPortLateEvents_Type()
)
rptrMonitorPortLateEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrMonitorPortLateEvents.setStatus("mandatory")
_RptrMonitorPortVeryLongEvents_Type = Counter32
_RptrMonitorPortVeryLongEvents_Object = MibTableColumn
rptrMonitorPortVeryLongEvents = _RptrMonitorPortVeryLongEvents_Object(
    (1, 3, 6, 1, 2, 1, 22, 2, 3, 1, 1, 12),
    _RptrMonitorPortVeryLongEvents_Type()
)
rptrMonitorPortVeryLongEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrMonitorPortVeryLongEvents.setStatus("mandatory")
_RptrMonitorPortDataRateMismatches_Type = Counter32
_RptrMonitorPortDataRateMismatches_Object = MibTableColumn
rptrMonitorPortDataRateMismatches = _RptrMonitorPortDataRateMismatches_Object(
    (1, 3, 6, 1, 2, 1, 22, 2, 3, 1, 1, 13),
    _RptrMonitorPortDataRateMismatches_Type()
)
rptrMonitorPortDataRateMismatches.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrMonitorPortDataRateMismatches.setStatus("mandatory")
_RptrMonitorPortAutoPartitions_Type = Counter32
_RptrMonitorPortAutoPartitions_Object = MibTableColumn
rptrMonitorPortAutoPartitions = _RptrMonitorPortAutoPartitions_Object(
    (1, 3, 6, 1, 2, 1, 22, 2, 3, 1, 1, 14),
    _RptrMonitorPortAutoPartitions_Type()
)
rptrMonitorPortAutoPartitions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrMonitorPortAutoPartitions.setStatus("mandatory")
_RptrMonitorPortTotalErrors_Type = Counter32
_RptrMonitorPortTotalErrors_Object = MibTableColumn
rptrMonitorPortTotalErrors = _RptrMonitorPortTotalErrors_Object(
    (1, 3, 6, 1, 2, 1, 22, 2, 3, 1, 1, 15),
    _RptrMonitorPortTotalErrors_Type()
)
rptrMonitorPortTotalErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrMonitorPortTotalErrors.setStatus("mandatory")
_RptrAddrTrackPackage_ObjectIdentity = ObjectIdentity
rptrAddrTrackPackage = _RptrAddrTrackPackage_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 22, 3)
)
_RptrAddrTrackRptrInfo_ObjectIdentity = ObjectIdentity
rptrAddrTrackRptrInfo = _RptrAddrTrackRptrInfo_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 22, 3, 1)
)
_RptrAddrTrackGroupInfo_ObjectIdentity = ObjectIdentity
rptrAddrTrackGroupInfo = _RptrAddrTrackGroupInfo_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 22, 3, 2)
)
_RptrAddrTrackPortInfo_ObjectIdentity = ObjectIdentity
rptrAddrTrackPortInfo = _RptrAddrTrackPortInfo_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 22, 3, 3)
)
_RptrAddrTrackTable_Object = MibTable
rptrAddrTrackTable = _RptrAddrTrackTable_Object(
    (1, 3, 6, 1, 2, 1, 22, 3, 3, 1)
)
if mibBuilder.loadTexts:
    rptrAddrTrackTable.setStatus("mandatory")
_RptrAddrTrackEntry_Object = MibTableRow
rptrAddrTrackEntry = _RptrAddrTrackEntry_Object(
    (1, 3, 6, 1, 2, 1, 22, 3, 3, 1, 1)
)
rptrAddrTrackEntry.setIndexNames(
    (0, "LBHUB-REPEATER-MIB", "rptrAddrTrackGroupIndex"),
    (0, "LBHUB-REPEATER-MIB", "rptrAddrTrackPortIndex"),
)
if mibBuilder.loadTexts:
    rptrAddrTrackEntry.setStatus("mandatory")


class _RptrAddrTrackGroupIndex_Type(Integer32):
    """Custom type rptrAddrTrackGroupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_RptrAddrTrackGroupIndex_Type.__name__ = "Integer32"
_RptrAddrTrackGroupIndex_Object = MibTableColumn
rptrAddrTrackGroupIndex = _RptrAddrTrackGroupIndex_Object(
    (1, 3, 6, 1, 2, 1, 22, 3, 3, 1, 1, 1),
    _RptrAddrTrackGroupIndex_Type()
)
rptrAddrTrackGroupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrAddrTrackGroupIndex.setStatus("mandatory")


class _RptrAddrTrackPortIndex_Type(Integer32):
    """Custom type rptrAddrTrackPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_RptrAddrTrackPortIndex_Type.__name__ = "Integer32"
_RptrAddrTrackPortIndex_Object = MibTableColumn
rptrAddrTrackPortIndex = _RptrAddrTrackPortIndex_Object(
    (1, 3, 6, 1, 2, 1, 22, 3, 3, 1, 1, 2),
    _RptrAddrTrackPortIndex_Type()
)
rptrAddrTrackPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrAddrTrackPortIndex.setStatus("mandatory")
_RptrAddrTrackLastSourceAddress_Type = MacAddress
_RptrAddrTrackLastSourceAddress_Object = MibTableColumn
rptrAddrTrackLastSourceAddress = _RptrAddrTrackLastSourceAddress_Object(
    (1, 3, 6, 1, 2, 1, 22, 3, 3, 1, 1, 3),
    _RptrAddrTrackLastSourceAddress_Type()
)
rptrAddrTrackLastSourceAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrAddrTrackLastSourceAddress.setStatus("deprecated")
_RptrAddrTrackSourceAddrChanges_Type = Counter32
_RptrAddrTrackSourceAddrChanges_Object = MibTableColumn
rptrAddrTrackSourceAddrChanges = _RptrAddrTrackSourceAddrChanges_Object(
    (1, 3, 6, 1, 2, 1, 22, 3, 3, 1, 1, 4),
    _RptrAddrTrackSourceAddrChanges_Type()
)
rptrAddrTrackSourceAddrChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrAddrTrackSourceAddrChanges.setStatus("mandatory")


class _RptrAddrTrackNewLastSrcAddress_Type(OctetString):
    """Custom type rptrAddrTrackNewLastSrcAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 6),
    )


_RptrAddrTrackNewLastSrcAddress_Type.__name__ = "OctetString"
_RptrAddrTrackNewLastSrcAddress_Object = MibTableColumn
rptrAddrTrackNewLastSrcAddress = _RptrAddrTrackNewLastSrcAddress_Object(
    (1, 3, 6, 1, 2, 1, 22, 3, 3, 1, 1, 5),
    _RptrAddrTrackNewLastSrcAddress_Type()
)
rptrAddrTrackNewLastSrcAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrAddrTrackNewLastSrcAddress.setStatus("mandatory")
_SnmpDot3MauMgt_ObjectIdentity = ObjectIdentity
snmpDot3MauMgt = _SnmpDot3MauMgt_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 26)
)
_Dot3RpMauBasicGroup_ObjectIdentity = ObjectIdentity
dot3RpMauBasicGroup = _Dot3RpMauBasicGroup_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 26, 1)
)
_RpMauTable_Object = MibTable
rpMauTable = _RpMauTable_Object(
    (1, 3, 6, 1, 2, 1, 26, 1, 1)
)
if mibBuilder.loadTexts:
    rpMauTable.setStatus("mandatory")
_RpMauEntry_Object = MibTableRow
rpMauEntry = _RpMauEntry_Object(
    (1, 3, 6, 1, 2, 1, 26, 1, 1, 1)
)
rpMauEntry.setIndexNames(
    (0, "LBHUB-REPEATER-MIB", "rpMauGroupIndex"),
    (0, "LBHUB-REPEATER-MIB", "rpMauPortIndex"),
    (0, "LBHUB-REPEATER-MIB", "rpMauIndex"),
)
if mibBuilder.loadTexts:
    rpMauEntry.setStatus("mandatory")


class _RpMauGroupIndex_Type(Integer32):
    """Custom type rpMauGroupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_RpMauGroupIndex_Type.__name__ = "Integer32"
_RpMauGroupIndex_Object = MibTableColumn
rpMauGroupIndex = _RpMauGroupIndex_Object(
    (1, 3, 6, 1, 2, 1, 26, 1, 1, 1, 1),
    _RpMauGroupIndex_Type()
)
rpMauGroupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpMauGroupIndex.setStatus("mandatory")


class _RpMauPortIndex_Type(Integer32):
    """Custom type rpMauPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_RpMauPortIndex_Type.__name__ = "Integer32"
_RpMauPortIndex_Object = MibTableColumn
rpMauPortIndex = _RpMauPortIndex_Object(
    (1, 3, 6, 1, 2, 1, 26, 1, 1, 1, 2),
    _RpMauPortIndex_Type()
)
rpMauPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpMauPortIndex.setStatus("mandatory")


class _RpMauIndex_Type(Integer32):
    """Custom type rpMauIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_RpMauIndex_Type.__name__ = "Integer32"
_RpMauIndex_Object = MibTableColumn
rpMauIndex = _RpMauIndex_Object(
    (1, 3, 6, 1, 2, 1, 26, 1, 1, 1, 3),
    _RpMauIndex_Type()
)
rpMauIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpMauIndex.setStatus("mandatory")
_RpMauType_Type = ObjectIdentifier
_RpMauType_Object = MibTableColumn
rpMauType = _RpMauType_Object(
    (1, 3, 6, 1, 2, 1, 26, 1, 1, 1, 4),
    _RpMauType_Type()
)
rpMauType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpMauType.setStatus("mandatory")


class _RpMauStatus_Type(Integer32):
    """Custom type rpMauStatus based on Integer32"""
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
        *(("operational", 3),
          ("other", 1),
          ("reset", 6),
          ("shutdown", 5),
          ("standby", 4),
          ("unknown", 2))
    )


_RpMauStatus_Type.__name__ = "Integer32"
_RpMauStatus_Object = MibTableColumn
rpMauStatus = _RpMauStatus_Object(
    (1, 3, 6, 1, 2, 1, 26, 1, 1, 1, 5),
    _RpMauStatus_Type()
)
rpMauStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rpMauStatus.setStatus("mandatory")


class _RpMauMediaAvailable_Type(Integer32):
    """Custom type rpMauMediaAvailable based on Integer32"""
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
        *(("available", 3),
          ("invalidSignal", 6),
          ("notAvailable", 4),
          ("other", 1),
          ("remoteFault", 5),
          ("unknown", 2))
    )


_RpMauMediaAvailable_Type.__name__ = "Integer32"
_RpMauMediaAvailable_Object = MibTableColumn
rpMauMediaAvailable = _RpMauMediaAvailable_Object(
    (1, 3, 6, 1, 2, 1, 26, 1, 1, 1, 6),
    _RpMauMediaAvailable_Type()
)
rpMauMediaAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpMauMediaAvailable.setStatus("mandatory")
_RpMauMediaAvailableStateExits_Type = Counter32
_RpMauMediaAvailableStateExits_Object = MibTableColumn
rpMauMediaAvailableStateExits = _RpMauMediaAvailableStateExits_Object(
    (1, 3, 6, 1, 2, 1, 26, 1, 1, 1, 7),
    _RpMauMediaAvailableStateExits_Type()
)
rpMauMediaAvailableStateExits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpMauMediaAvailableStateExits.setStatus("mandatory")


class _RpMauJabberState_Type(Integer32):
    """Custom type rpMauJabberState based on Integer32"""
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
        *(("jabbering", 4),
          ("noJabber", 3),
          ("other", 1),
          ("unknown", 2))
    )


_RpMauJabberState_Type.__name__ = "Integer32"
_RpMauJabberState_Object = MibTableColumn
rpMauJabberState = _RpMauJabberState_Object(
    (1, 3, 6, 1, 2, 1, 26, 1, 1, 1, 8),
    _RpMauJabberState_Type()
)
rpMauJabberState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpMauJabberState.setStatus("mandatory")
_RpMauJabberingStateEnters_Type = Counter32
_RpMauJabberingStateEnters_Object = MibTableColumn
rpMauJabberingStateEnters = _RpMauJabberingStateEnters_Object(
    (1, 3, 6, 1, 2, 1, 26, 1, 1, 1, 9),
    _RpMauJabberingStateEnters_Type()
)
rpMauJabberingStateEnters.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpMauJabberingStateEnters.setStatus("mandatory")
_Dot3IfMauBasicGroup_ObjectIdentity = ObjectIdentity
dot3IfMauBasicGroup = _Dot3IfMauBasicGroup_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 26, 2)
)
_Dot3BroadMauBasicGroup_ObjectIdentity = ObjectIdentity
dot3BroadMauBasicGroup = _Dot3BroadMauBasicGroup_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 26, 3)
)
_Dot3MauType_ObjectIdentity = ObjectIdentity
dot3MauType = _Dot3MauType_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 26, 4)
)
_Dot3MauTypeAUI_ObjectIdentity = ObjectIdentity
dot3MauTypeAUI = _Dot3MauTypeAUI_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 26, 4, 1)
)
_Dot3MauType10Base5_ObjectIdentity = ObjectIdentity
dot3MauType10Base5 = _Dot3MauType10Base5_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 26, 4, 2)
)
_Dot3MauTypeFoirl_ObjectIdentity = ObjectIdentity
dot3MauTypeFoirl = _Dot3MauTypeFoirl_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 26, 4, 3)
)
_Dot3MauType10Base2_ObjectIdentity = ObjectIdentity
dot3MauType10Base2 = _Dot3MauType10Base2_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 26, 4, 4)
)
_Dot3MauType10BaseT_ObjectIdentity = ObjectIdentity
dot3MauType10BaseT = _Dot3MauType10BaseT_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 26, 4, 5)
)
_Dot3MauType10BaseFP_ObjectIdentity = ObjectIdentity
dot3MauType10BaseFP = _Dot3MauType10BaseFP_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 26, 4, 6)
)
_Dot3MauType10BaseFB_ObjectIdentity = ObjectIdentity
dot3MauType10BaseFB = _Dot3MauType10BaseFB_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 26, 4, 7)
)
_Dot3MauType10BaseFL_ObjectIdentity = ObjectIdentity
dot3MauType10BaseFL = _Dot3MauType10BaseFL_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 26, 4, 8)
)
_Dot3MauType10Broad36_ObjectIdentity = ObjectIdentity
dot3MauType10Broad36 = _Dot3MauType10Broad36_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 26, 4, 9)
)
_A3Com_ObjectIdentity = ObjectIdentity
a3Com = _A3Com_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43)
)
_Products_ObjectIdentity = ObjectIdentity
products = _Products_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1)
)
_TerminalServer_ObjectIdentity = ObjectIdentity
terminalServer = _TerminalServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 1)
)
_DedicatedBridgeServer_ObjectIdentity = ObjectIdentity
dedicatedBridgeServer = _DedicatedBridgeServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 2)
)
_DedicatedRouteServer_ObjectIdentity = ObjectIdentity
dedicatedRouteServer = _DedicatedRouteServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 3)
)
_Brouter_ObjectIdentity = ObjectIdentity
brouter = _Brouter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4)
)
_GenericMSWorkstation_ObjectIdentity = ObjectIdentity
genericMSWorkstation = _GenericMSWorkstation_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 5)
)
_GenericMSServer_ObjectIdentity = ObjectIdentity
genericMSServer = _GenericMSServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 6)
)
_GenericUnixServer_ObjectIdentity = ObjectIdentity
genericUnixServer = _GenericUnixServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 7)
)
_Hub_ObjectIdentity = ObjectIdentity
hub = _Hub_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 8)
)
_LinkBuilder3GH_ObjectIdentity = ObjectIdentity
linkBuilder3GH = _LinkBuilder3GH_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 8, 1)
)
_LinkBuilder10BTi_ObjectIdentity = ObjectIdentity
linkBuilder10BTi = _LinkBuilder10BTi_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 8, 2)
)
_LinkBuilderECS_ObjectIdentity = ObjectIdentity
linkBuilderECS = _LinkBuilderECS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 8, 3)
)
_LinkBuilderMSH_ObjectIdentity = ObjectIdentity
linkBuilderMSH = _LinkBuilderMSH_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 8, 4)
)
_LinkBuilderFMS_ObjectIdentity = ObjectIdentity
linkBuilderFMS = _LinkBuilderFMS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 8, 5)
)
_LinkBuilderFDDIwg_ObjectIdentity = ObjectIdentity
linkBuilderFDDIwg = _LinkBuilderFDDIwg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 8, 6)
)
_LinkBuilderFMSII_ObjectIdentity = ObjectIdentity
linkBuilderFMSII = _LinkBuilderFMSII_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 8, 7)
)
_LinkSwitchFMS_ObjectIdentity = ObjectIdentity
linkSwitchFMS = _LinkSwitchFMS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 8, 8)
)
_LinkSwitchMSH_ObjectIdentity = ObjectIdentity
linkSwitchMSH = _LinkSwitchMSH_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 8, 9)
)
_LinkBuilderFMSLBridge_ObjectIdentity = ObjectIdentity
linkBuilderFMSLBridge = _LinkBuilderFMSLBridge_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 8, 10)
)
_Cards_ObjectIdentity = ObjectIdentity
cards = _Cards_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 9)
)
_LinkBuilder3GH_cards_ObjectIdentity = ObjectIdentity
linkBuilder3GH_cards = _LinkBuilder3GH_cards_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 9, 1)
)
_LinkBuilder10BTi_cards_ObjectIdentity = ObjectIdentity
linkBuilder10BTi_cards = _LinkBuilder10BTi_cards_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 9, 2)
)
_LinkBuilder10BTi_cards_utp_ObjectIdentity = ObjectIdentity
linkBuilder10BTi_cards_utp = _LinkBuilder10BTi_cards_utp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 9, 2, 1)
)
_LinkBuilder10BT_cards_utp_ObjectIdentity = ObjectIdentity
linkBuilder10BT_cards_utp = _LinkBuilder10BT_cards_utp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 9, 2, 2)
)
_LinkBuilderECS_cards_ObjectIdentity = ObjectIdentity
linkBuilderECS_cards = _LinkBuilderECS_cards_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 9, 3)
)
_LinkBuilderMSH_cards_ObjectIdentity = ObjectIdentity
linkBuilderMSH_cards = _LinkBuilderMSH_cards_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 9, 4)
)
_LinkBuilderFMS_cards_ObjectIdentity = ObjectIdentity
linkBuilderFMS_cards = _LinkBuilderFMS_cards_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 9, 5)
)
_LinkBuilderFMS_cards_utp_ObjectIdentity = ObjectIdentity
linkBuilderFMS_cards_utp = _LinkBuilderFMS_cards_utp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 9, 5, 1)
)
_LinkBuilderFMS_cards_coax_ObjectIdentity = ObjectIdentity
linkBuilderFMS_cards_coax = _LinkBuilderFMS_cards_coax_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 9, 5, 2)
)
_LinkBuilderFMS_cards_fiber_ObjectIdentity = ObjectIdentity
linkBuilderFMS_cards_fiber = _LinkBuilderFMS_cards_fiber_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 9, 5, 3)
)
_LinkBuilderFMS_cards_12fiber_ObjectIdentity = ObjectIdentity
linkBuilderFMS_cards_12fiber = _LinkBuilderFMS_cards_12fiber_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 9, 5, 4)
)
_LinkBuilderFMS_cards_24utp_ObjectIdentity = ObjectIdentity
linkBuilderFMS_cards_24utp = _LinkBuilderFMS_cards_24utp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 9, 5, 5)
)
_LinkBuilderFMSII_cards_ObjectIdentity = ObjectIdentity
linkBuilderFMSII_cards = _LinkBuilderFMSII_cards_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 9, 6)
)
_LinkBuilderFMSII_cards_12tp_rj45_ObjectIdentity = ObjectIdentity
linkBuilderFMSII_cards_12tp_rj45 = _LinkBuilderFMSII_cards_12tp_rj45_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 9, 6, 1)
)
_LinkBuilderFMSII_cards_10coax_bnc_ObjectIdentity = ObjectIdentity
linkBuilderFMSII_cards_10coax_bnc = _LinkBuilderFMSII_cards_10coax_bnc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 9, 6, 2)
)
_LinkBuilderFMSII_cards_6fiber_st_ObjectIdentity = ObjectIdentity
linkBuilderFMSII_cards_6fiber_st = _LinkBuilderFMSII_cards_6fiber_st_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 9, 6, 3)
)
_LinkBuilderFMSII_cards_12fiber_st_ObjectIdentity = ObjectIdentity
linkBuilderFMSII_cards_12fiber_st = _LinkBuilderFMSII_cards_12fiber_st_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 9, 6, 4)
)
_LinkBuilderFMSII_cards_24tp_rj45_ObjectIdentity = ObjectIdentity
linkBuilderFMSII_cards_24tp_rj45 = _LinkBuilderFMSII_cards_24tp_rj45_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 9, 6, 5)
)
_LinkBuilderFMSII_cards_24tp_telco_ObjectIdentity = ObjectIdentity
linkBuilderFMSII_cards_24tp_telco = _LinkBuilderFMSII_cards_24tp_telco_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 9, 6, 6)
)
_Chipsets_ObjectIdentity = ObjectIdentity
chipsets = _Chipsets_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 10)
)
_Amp_mib_ObjectIdentity = ObjectIdentity
amp_mib = _Amp_mib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 3)
)
_GenericTrap_ObjectIdentity = ObjectIdentity
genericTrap = _GenericTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 4)
)
_ViewBuilderApps_ObjectIdentity = ObjectIdentity
viewBuilderApps = _ViewBuilderApps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 5)
)
_SpecificTrap_ObjectIdentity = ObjectIdentity
specificTrap = _SpecificTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 6)
)
_LinkBuilder3GH_mib_ObjectIdentity = ObjectIdentity
linkBuilder3GH_mib = _LinkBuilder3GH_mib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 7)
)
_LinkBuilder10BTi_mib_ObjectIdentity = ObjectIdentity
linkBuilder10BTi_mib = _LinkBuilder10BTi_mib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 8)
)
_LinkBuilderECS_mib_ObjectIdentity = ObjectIdentity
linkBuilderECS_mib = _LinkBuilderECS_mib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 9)
)
_Generic_ObjectIdentity = ObjectIdentity
generic = _Generic_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 10)
)
_GenExperimental_ObjectIdentity = ObjectIdentity
genExperimental = _GenExperimental_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 10, 1)
)
_TestData_ObjectIdentity = ObjectIdentity
testData = _TestData_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 10, 1, 1)
)
_IfExtensions_ObjectIdentity = ObjectIdentity
ifExtensions = _IfExtensions_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 10, 1, 2)
)
_Setup_ObjectIdentity = ObjectIdentity
setup = _Setup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 10, 2)
)
_SysLoader_ObjectIdentity = ObjectIdentity
sysLoader = _SysLoader_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 10, 3)
)
_Security_ObjectIdentity = ObjectIdentity
security = _Security_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 10, 4)
)
_Gauges_ObjectIdentity = ObjectIdentity
gauges = _Gauges_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 10, 5)
)
_AsciiAgent_ObjectIdentity = ObjectIdentity
asciiAgent = _AsciiAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 10, 6)
)
_SerialIf_ObjectIdentity = ObjectIdentity
serialIf = _SerialIf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 10, 7)
)
_RepeaterMgmt_ObjectIdentity = ObjectIdentity
repeaterMgmt = _RepeaterMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 10, 8)
)
_EndStation_ObjectIdentity = ObjectIdentity
endStation = _EndStation_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 10, 9)
)
_LocalSnmp_ObjectIdentity = ObjectIdentity
localSnmp = _LocalSnmp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 10, 10)
)
_Manager_ObjectIdentity = ObjectIdentity
manager = _Manager_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 10, 11)
)
_UnusedGeneric12_ObjectIdentity = ObjectIdentity
unusedGeneric12 = _UnusedGeneric12_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 10, 12)
)
_Chassis_ObjectIdentity = ObjectIdentity
chassis = _Chassis_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 10, 14)
)
_MrmResilience_ObjectIdentity = ObjectIdentity
mrmResilience = _MrmResilience_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 10, 15)
)
_TokenRing_ObjectIdentity = ObjectIdentity
tokenRing = _TokenRing_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 10, 16)
)
_MultiRepeater_ObjectIdentity = ObjectIdentity
multiRepeater = _MultiRepeater_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 10, 17)
)
_BridgeMgmt_ObjectIdentity = ObjectIdentity
bridgeMgmt = _BridgeMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 10, 18)
)
_Fault_ObjectIdentity = ObjectIdentity
fault = _Fault_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 10, 19)
)
_Poll_ObjectIdentity = ObjectIdentity
poll = _Poll_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 10, 20)
)
_PowerSupply_ObjectIdentity = ObjectIdentity
powerSupply = _PowerSupply_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 10, 21)
)
_NetBuilder_mib_ObjectIdentity = ObjectIdentity
netBuilder_mib = _NetBuilder_mib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 11)
)
_LBridgeECS_mib_ObjectIdentity = ObjectIdentity
lBridgeECS_mib = _LBridgeECS_mib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 12)
)
_DeskMan_mib_ObjectIdentity = ObjectIdentity
deskMan_mib = _DeskMan_mib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 13)
)
_LinkBuilderMSH_mib_ObjectIdentity = ObjectIdentity
linkBuilderMSH_mib = _LinkBuilderMSH_mib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 14)
)
_LinkBuilderFMS_mib_ObjectIdentity = ObjectIdentity
linkBuilderFMS_mib = _LinkBuilderFMS_mib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 15)
)
_LinkBuilderFDDI_wghub_mib_ObjectIdentity = ObjectIdentity
linkBuilderFDDI_wghub_mib = _LinkBuilderFDDI_wghub_mib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 16)
)
_LinkSwitch_mib_ObjectIdentity = ObjectIdentity
linkSwitch_mib = _LinkSwitch_mib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 17)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "LBHUB-REPEATER-MIB",
    **{"DisplayString": DisplayString,
       "PhysAddress": PhysAddress,
       "MacAddress": MacAddress,
       "mib-2": mib_2,
       "system": system,
       "interfaces": interfaces,
       "at": at,
       "ip": ip,
       "icmp": icmp,
       "tcp": tcp,
       "udp": udp,
       "egp": egp,
       "transmission": transmission,
       "snmp": snmp,
       "dot1dBridge": dot1dBridge,
       "snmpDot3RptrMgt": snmpDot3RptrMgt,
       "rptrBasicPackage": rptrBasicPackage,
       "rptrRptrInfo": rptrRptrInfo,
       "rptrGroupCapacity": rptrGroupCapacity,
       "rptrOperSTATUS": rptrOperSTATUS,
       "rptrHealthText": rptrHealthText,
       "rptrReset": rptrReset,
       "rptrNonDisruptTest": rptrNonDisruptTest,
       "rptrTotalPartitionedPorts": rptrTotalPartitionedPorts,
       "rptrGroupInfo": rptrGroupInfo,
       "rptrGroupTable": rptrGroupTable,
       "rptrGroupEntry": rptrGroupEntry,
       "rptrGroupIndex": rptrGroupIndex,
       "rptrGroupDescr": rptrGroupDescr,
       "rptrGroupObjectID": rptrGroupObjectID,
       "rptrGroupOperSTATUS": rptrGroupOperSTATUS,
       "rptrGroupLastOperSTATUSChange": rptrGroupLastOperSTATUSChange,
       "rptrGroupPortCapacity": rptrGroupPortCapacity,
       "rptrPortInfo": rptrPortInfo,
       "rptrPortTable": rptrPortTable,
       "rptrPortEntry": rptrPortEntry,
       "rptrPortGroupIndex": rptrPortGroupIndex,
       "rptrPortIndex": rptrPortIndex,
       "rptrPortAdminSTATUS": rptrPortAdminSTATUS,
       "rptrPortAutoPartitionState": rptrPortAutoPartitionState,
       "rptrPortOperSTATUS": rptrPortOperSTATUS,
       "rptrMonitorPackage": rptrMonitorPackage,
       "rptrMonitorRptrInfo": rptrMonitorRptrInfo,
       "rptrMonitorTransmitCollisions": rptrMonitorTransmitCollisions,
       "rptrMonitorGroupInfo": rptrMonitorGroupInfo,
       "rptrMonitorGroupTable": rptrMonitorGroupTable,
       "rptrMonitorGroupEntry": rptrMonitorGroupEntry,
       "rptrMonitorGroupIndex": rptrMonitorGroupIndex,
       "rptrMonitorGroupTotalFrames": rptrMonitorGroupTotalFrames,
       "rptrMonitorGroupTotalOctets": rptrMonitorGroupTotalOctets,
       "rptrMonitorGroupTotalErrors": rptrMonitorGroupTotalErrors,
       "rptrMonitorPortInfo": rptrMonitorPortInfo,
       "rptrMonitorPortTable": rptrMonitorPortTable,
       "rptrMonitorPortEntry": rptrMonitorPortEntry,
       "rptrMonitorPortGroupIndex": rptrMonitorPortGroupIndex,
       "rptrMonitorPortIndex": rptrMonitorPortIndex,
       "rptrMonitorPortReadableFrames": rptrMonitorPortReadableFrames,
       "rptrMonitorPortReadableOctets": rptrMonitorPortReadableOctets,
       "rptrMonitorPortFCSErrors": rptrMonitorPortFCSErrors,
       "rptrMonitorPortAlignmentErrors": rptrMonitorPortAlignmentErrors,
       "rptrMonitorPortFrameTooLongs": rptrMonitorPortFrameTooLongs,
       "rptrMonitorPortShortEvents": rptrMonitorPortShortEvents,
       "rptrMonitorPortRunts": rptrMonitorPortRunts,
       "rptrMonitorPortCollisions": rptrMonitorPortCollisions,
       "rptrMonitorPortLateEvents": rptrMonitorPortLateEvents,
       "rptrMonitorPortVeryLongEvents": rptrMonitorPortVeryLongEvents,
       "rptrMonitorPortDataRateMismatches": rptrMonitorPortDataRateMismatches,
       "rptrMonitorPortAutoPartitions": rptrMonitorPortAutoPartitions,
       "rptrMonitorPortTotalErrors": rptrMonitorPortTotalErrors,
       "rptrAddrTrackPackage": rptrAddrTrackPackage,
       "rptrAddrTrackRptrInfo": rptrAddrTrackRptrInfo,
       "rptrAddrTrackGroupInfo": rptrAddrTrackGroupInfo,
       "rptrAddrTrackPortInfo": rptrAddrTrackPortInfo,
       "rptrAddrTrackTable": rptrAddrTrackTable,
       "rptrAddrTrackEntry": rptrAddrTrackEntry,
       "rptrAddrTrackGroupIndex": rptrAddrTrackGroupIndex,
       "rptrAddrTrackPortIndex": rptrAddrTrackPortIndex,
       "rptrAddrTrackLastSourceAddress": rptrAddrTrackLastSourceAddress,
       "rptrAddrTrackSourceAddrChanges": rptrAddrTrackSourceAddrChanges,
       "rptrAddrTrackNewLastSrcAddress": rptrAddrTrackNewLastSrcAddress,
       "snmpDot3MauMgt": snmpDot3MauMgt,
       "dot3RpMauBasicGroup": dot3RpMauBasicGroup,
       "rpMauTable": rpMauTable,
       "rpMauEntry": rpMauEntry,
       "rpMauGroupIndex": rpMauGroupIndex,
       "rpMauPortIndex": rpMauPortIndex,
       "rpMauIndex": rpMauIndex,
       "rpMauType": rpMauType,
       "rpMauStatus": rpMauStatus,
       "rpMauMediaAvailable": rpMauMediaAvailable,
       "rpMauMediaAvailableStateExits": rpMauMediaAvailableStateExits,
       "rpMauJabberState": rpMauJabberState,
       "rpMauJabberingStateEnters": rpMauJabberingStateEnters,
       "dot3IfMauBasicGroup": dot3IfMauBasicGroup,
       "dot3BroadMauBasicGroup": dot3BroadMauBasicGroup,
       "dot3MauType": dot3MauType,
       "dot3MauTypeAUI": dot3MauTypeAUI,
       "dot3MauType10Base5": dot3MauType10Base5,
       "dot3MauTypeFoirl": dot3MauTypeFoirl,
       "dot3MauType10Base2": dot3MauType10Base2,
       "dot3MauType10BaseT": dot3MauType10BaseT,
       "dot3MauType10BaseFP": dot3MauType10BaseFP,
       "dot3MauType10BaseFB": dot3MauType10BaseFB,
       "dot3MauType10BaseFL": dot3MauType10BaseFL,
       "dot3MauType10Broad36": dot3MauType10Broad36,
       "a3Com": a3Com,
       "products": products,
       "terminalServer": terminalServer,
       "dedicatedBridgeServer": dedicatedBridgeServer,
       "dedicatedRouteServer": dedicatedRouteServer,
       "brouter": brouter,
       "genericMSWorkstation": genericMSWorkstation,
       "genericMSServer": genericMSServer,
       "genericUnixServer": genericUnixServer,
       "hub": hub,
       "linkBuilder3GH": linkBuilder3GH,
       "linkBuilder10BTi": linkBuilder10BTi,
       "linkBuilderECS": linkBuilderECS,
       "linkBuilderMSH": linkBuilderMSH,
       "linkBuilderFMS": linkBuilderFMS,
       "linkBuilderFDDIwg": linkBuilderFDDIwg,
       "linkBuilderFMSII": linkBuilderFMSII,
       "linkSwitchFMS": linkSwitchFMS,
       "linkSwitchMSH": linkSwitchMSH,
       "linkBuilderFMSLBridge": linkBuilderFMSLBridge,
       "cards": cards,
       "linkBuilder3GH-cards": linkBuilder3GH_cards,
       "linkBuilder10BTi-cards": linkBuilder10BTi_cards,
       "linkBuilder10BTi-cards-utp": linkBuilder10BTi_cards_utp,
       "linkBuilder10BT-cards-utp": linkBuilder10BT_cards_utp,
       "linkBuilderECS-cards": linkBuilderECS_cards,
       "linkBuilderMSH-cards": linkBuilderMSH_cards,
       "linkBuilderFMS-cards": linkBuilderFMS_cards,
       "linkBuilderFMS-cards-utp": linkBuilderFMS_cards_utp,
       "linkBuilderFMS-cards-coax": linkBuilderFMS_cards_coax,
       "linkBuilderFMS-cards-fiber": linkBuilderFMS_cards_fiber,
       "linkBuilderFMS-cards-12fiber": linkBuilderFMS_cards_12fiber,
       "linkBuilderFMS-cards-24utp": linkBuilderFMS_cards_24utp,
       "linkBuilderFMSII-cards": linkBuilderFMSII_cards,
       "linkBuilderFMSII-cards-12tp-rj45": linkBuilderFMSII_cards_12tp_rj45,
       "linkBuilderFMSII-cards-10coax-bnc": linkBuilderFMSII_cards_10coax_bnc,
       "linkBuilderFMSII-cards-6fiber-st": linkBuilderFMSII_cards_6fiber_st,
       "linkBuilderFMSII-cards-12fiber-st": linkBuilderFMSII_cards_12fiber_st,
       "linkBuilderFMSII-cards-24tp-rj45": linkBuilderFMSII_cards_24tp_rj45,
       "linkBuilderFMSII-cards-24tp-telco": linkBuilderFMSII_cards_24tp_telco,
       "chipsets": chipsets,
       "amp-mib": amp_mib,
       "genericTrap": genericTrap,
       "viewBuilderApps": viewBuilderApps,
       "specificTrap": specificTrap,
       "linkBuilder3GH-mib": linkBuilder3GH_mib,
       "linkBuilder10BTi-mib": linkBuilder10BTi_mib,
       "linkBuilderECS-mib": linkBuilderECS_mib,
       "generic": generic,
       "genExperimental": genExperimental,
       "testData": testData,
       "ifExtensions": ifExtensions,
       "setup": setup,
       "sysLoader": sysLoader,
       "security": security,
       "gauges": gauges,
       "asciiAgent": asciiAgent,
       "serialIf": serialIf,
       "repeaterMgmt": repeaterMgmt,
       "endStation": endStation,
       "localSnmp": localSnmp,
       "manager": manager,
       "unusedGeneric12": unusedGeneric12,
       "chassis": chassis,
       "mrmResilience": mrmResilience,
       "tokenRing": tokenRing,
       "multiRepeater": multiRepeater,
       "bridgeMgmt": bridgeMgmt,
       "fault": fault,
       "poll": poll,
       "powerSupply": powerSupply,
       "netBuilder-mib": netBuilder_mib,
       "lBridgeECS-mib": lBridgeECS_mib,
       "deskMan-mib": deskMan_mib,
       "linkBuilderMSH-mib": linkBuilderMSH_mib,
       "linkBuilderFMS-mib": linkBuilderFMS_mib,
       "linkBuilderFDDI-wghub-mib": linkBuilderFDDI_wghub_mib,
       "linkSwitch-mib": linkSwitch_mib}
)
