# SNMP MIB module (ZXR10-PING-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ZXR10-PING-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:21:03 2024
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
 enterprises,
 experimental,
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
    "experimental",
    "iso",
    "mgmt")

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

(zxr10L2vpn,) = mibBuilder.importSymbols(
    "ZXR10-SMI",
    "zxr10L2vpn")


# MODULE-IDENTITY


# Types definitions



class DisplayString(OctetString):
    """Custom type DisplayString based on OctetString"""



# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Zxr10PingMIB_ObjectIdentity = ObjectIdentity
zxr10PingMIB = _Zxr10PingMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 3, 104, 2)
)
_Zxr10PingTable_Object = MibTable
zxr10PingTable = _Zxr10PingTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 104, 2, 1)
)
if mibBuilder.loadTexts:
    zxr10PingTable.setStatus("current")
_Zxr10pingCommonEntry_Object = MibTableRow
zxr10pingCommonEntry = _Zxr10pingCommonEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 104, 2, 1, 1)
)
zxr10pingCommonEntry.setIndexNames(
    (0, "ZXR10-PING-MIB", "zxr10PingCommonSerial"),
)
if mibBuilder.loadTexts:
    zxr10pingCommonEntry.setStatus("current")
_Zxr10PingCommonSerial_Type = Integer32
_Zxr10PingCommonSerial_Object = MibTableColumn
zxr10PingCommonSerial = _Zxr10PingCommonSerial_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 104, 2, 1, 1, 1),
    _Zxr10PingCommonSerial_Type()
)
zxr10PingCommonSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10PingCommonSerial.setStatus("current")


class _Zxr10PingCommonPingType_Type(Integer32):
    """Custom type zxr10PingCommonPingType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("common", 0),
          ("mng", 1),
          ("vrf", 2))
    )


_Zxr10PingCommonPingType_Type.__name__ = "Integer32"
_Zxr10PingCommonPingType_Object = MibTableColumn
zxr10PingCommonPingType = _Zxr10PingCommonPingType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 104, 2, 1, 1, 2),
    _Zxr10PingCommonPingType_Type()
)
zxr10PingCommonPingType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxr10PingCommonPingType.setStatus("current")
_Zxr10PingCommonDestAddr_Type = IpAddress
_Zxr10PingCommonDestAddr_Object = MibTableColumn
zxr10PingCommonDestAddr = _Zxr10PingCommonDestAddr_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 104, 2, 1, 1, 3),
    _Zxr10PingCommonDestAddr_Type()
)
zxr10PingCommonDestAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxr10PingCommonDestAddr.setStatus("current")


class _Zxr10PingCommonVrfName_Type(DisplayString):
    """Custom type zxr10PingCommonVrfName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_Zxr10PingCommonVrfName_Type.__name__ = "DisplayString"
_Zxr10PingCommonVrfName_Object = MibTableColumn
zxr10PingCommonVrfName = _Zxr10PingCommonVrfName_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 104, 2, 1, 1, 4),
    _Zxr10PingCommonVrfName_Type()
)
zxr10PingCommonVrfName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxr10PingCommonVrfName.setStatus("current")


class _Zxr10PingCommonIfOption_Type(Integer32):
    """Custom type zxr10PingCommonIfOption based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("option", 1))
    )


_Zxr10PingCommonIfOption_Type.__name__ = "Integer32"
_Zxr10PingCommonIfOption_Object = MibTableColumn
zxr10PingCommonIfOption = _Zxr10PingCommonIfOption_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 104, 2, 1, 1, 5),
    _Zxr10PingCommonIfOption_Type()
)
zxr10PingCommonIfOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxr10PingCommonIfOption.setStatus("current")
_Zxr10PingCommonPacketCount_Type = Integer32
_Zxr10PingCommonPacketCount_Object = MibTableColumn
zxr10PingCommonPacketCount = _Zxr10PingCommonPacketCount_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 104, 2, 1, 1, 6),
    _Zxr10PingCommonPacketCount_Type()
)
zxr10PingCommonPacketCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxr10PingCommonPacketCount.setStatus("current")


class _Zxr10PingCommonTimeOut_Type(Integer32):
    """Custom type zxr10PingCommonTimeOut based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_Zxr10PingCommonTimeOut_Type.__name__ = "Integer32"
_Zxr10PingCommonTimeOut_Object = MibTableColumn
zxr10PingCommonTimeOut = _Zxr10PingCommonTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 104, 2, 1, 1, 7),
    _Zxr10PingCommonTimeOut_Type()
)
zxr10PingCommonTimeOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxr10PingCommonTimeOut.setStatus("current")


class _Zxr10PingCommonDataLen_Type(Integer32):
    """Custom type zxr10PingCommonDataLen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(36, 8192),
    )


_Zxr10PingCommonDataLen_Type.__name__ = "Integer32"
_Zxr10PingCommonDataLen_Object = MibTableColumn
zxr10PingCommonDataLen = _Zxr10PingCommonDataLen_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 104, 2, 1, 1, 8),
    _Zxr10PingCommonDataLen_Type()
)
zxr10PingCommonDataLen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxr10PingCommonDataLen.setStatus("current")


class _Zxr10PingCommonIfExtOption_Type(Integer32):
    """Custom type zxr10PingCommonIfExtOption based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("extcom", 1),
          ("none", 0))
    )


_Zxr10PingCommonIfExtOption_Type.__name__ = "Integer32"
_Zxr10PingCommonIfExtOption_Object = MibTableColumn
zxr10PingCommonIfExtOption = _Zxr10PingCommonIfExtOption_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 104, 2, 1, 1, 9),
    _Zxr10PingCommonIfExtOption_Type()
)
zxr10PingCommonIfExtOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxr10PingCommonIfExtOption.setStatus("current")
_Zxr10PingCommonExtSourceAddr_Type = IpAddress
_Zxr10PingCommonExtSourceAddr_Object = MibTableColumn
zxr10PingCommonExtSourceAddr = _Zxr10PingCommonExtSourceAddr_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 104, 2, 1, 1, 10),
    _Zxr10PingCommonExtSourceAddr_Type()
)
zxr10PingCommonExtSourceAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxr10PingCommonExtSourceAddr.setStatus("current")


class _Zxr10PingCommonExtTos_Type(Integer32):
    """Custom type zxr10PingCommonExtTos based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Zxr10PingCommonExtTos_Type.__name__ = "Integer32"
_Zxr10PingCommonExtTos_Object = MibTableColumn
zxr10PingCommonExtTos = _Zxr10PingCommonExtTos_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 104, 2, 1, 1, 11),
    _Zxr10PingCommonExtTos_Type()
)
zxr10PingCommonExtTos.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxr10PingCommonExtTos.setStatus("current")


class _Zxr10PingCommonExtTTL_Type(Integer32):
    """Custom type zxr10PingCommonExtTTL based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_Zxr10PingCommonExtTTL_Type.__name__ = "Integer32"
_Zxr10PingCommonExtTTL_Object = MibTableColumn
zxr10PingCommonExtTTL = _Zxr10PingCommonExtTTL_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 104, 2, 1, 1, 12),
    _Zxr10PingCommonExtTTL_Type()
)
zxr10PingCommonExtTTL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxr10PingCommonExtTTL.setStatus("current")


class _Zxr10PingCommonExtFragement_Type(Integer32):
    """Custom type zxr10PingCommonExtFragement based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Zxr10PingCommonExtFragement_Type.__name__ = "Integer32"
_Zxr10PingCommonExtFragement_Object = MibTableColumn
zxr10PingCommonExtFragement = _Zxr10PingCommonExtFragement_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 104, 2, 1, 1, 13),
    _Zxr10PingCommonExtFragement_Type()
)
zxr10PingCommonExtFragement.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxr10PingCommonExtFragement.setStatus("current")


class _Zxr10PingCommonExtOpType_Type(Integer32):
    """Custom type zxr10PingCommonExtOpType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("loose", 1),
          ("none", 0),
          ("record", 2),
          ("strict", 3),
          ("timestamp", 4))
    )


_Zxr10PingCommonExtOpType_Type.__name__ = "Integer32"
_Zxr10PingCommonExtOpType_Object = MibTableColumn
zxr10PingCommonExtOpType = _Zxr10PingCommonExtOpType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 104, 2, 1, 1, 14),
    _Zxr10PingCommonExtOpType_Type()
)
zxr10PingCommonExtOpType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxr10PingCommonExtOpType.setStatus("current")
_Zxr10PingCommonExtOpIpAddr1_Type = IpAddress
_Zxr10PingCommonExtOpIpAddr1_Object = MibTableColumn
zxr10PingCommonExtOpIpAddr1 = _Zxr10PingCommonExtOpIpAddr1_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 104, 2, 1, 1, 15),
    _Zxr10PingCommonExtOpIpAddr1_Type()
)
zxr10PingCommonExtOpIpAddr1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxr10PingCommonExtOpIpAddr1.setStatus("current")
_Zxr10PingCommonExtOpIpAddr2_Type = IpAddress
_Zxr10PingCommonExtOpIpAddr2_Object = MibTableColumn
zxr10PingCommonExtOpIpAddr2 = _Zxr10PingCommonExtOpIpAddr2_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 104, 2, 1, 1, 16),
    _Zxr10PingCommonExtOpIpAddr2_Type()
)
zxr10PingCommonExtOpIpAddr2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxr10PingCommonExtOpIpAddr2.setStatus("current")
_Zxr10PingCommonExtOpIpAddr3_Type = IpAddress
_Zxr10PingCommonExtOpIpAddr3_Object = MibTableColumn
zxr10PingCommonExtOpIpAddr3 = _Zxr10PingCommonExtOpIpAddr3_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 104, 2, 1, 1, 17),
    _Zxr10PingCommonExtOpIpAddr3_Type()
)
zxr10PingCommonExtOpIpAddr3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxr10PingCommonExtOpIpAddr3.setStatus("current")
_Zxr10PingCommonExtOpIpAddr4_Type = IpAddress
_Zxr10PingCommonExtOpIpAddr4_Object = MibTableColumn
zxr10PingCommonExtOpIpAddr4 = _Zxr10PingCommonExtOpIpAddr4_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 104, 2, 1, 1, 18),
    _Zxr10PingCommonExtOpIpAddr4_Type()
)
zxr10PingCommonExtOpIpAddr4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxr10PingCommonExtOpIpAddr4.setStatus("current")
_Zxr10PingCommonExtOpIpAddr5_Type = IpAddress
_Zxr10PingCommonExtOpIpAddr5_Object = MibTableColumn
zxr10PingCommonExtOpIpAddr5 = _Zxr10PingCommonExtOpIpAddr5_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 104, 2, 1, 1, 19),
    _Zxr10PingCommonExtOpIpAddr5_Type()
)
zxr10PingCommonExtOpIpAddr5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxr10PingCommonExtOpIpAddr5.setStatus("current")
_Zxr10PingCommonExtOpIpAddr6_Type = IpAddress
_Zxr10PingCommonExtOpIpAddr6_Object = MibTableColumn
zxr10PingCommonExtOpIpAddr6 = _Zxr10PingCommonExtOpIpAddr6_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 104, 2, 1, 1, 20),
    _Zxr10PingCommonExtOpIpAddr6_Type()
)
zxr10PingCommonExtOpIpAddr6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxr10PingCommonExtOpIpAddr6.setStatus("current")
_Zxr10PingCommonExtOpIpAddr7_Type = IpAddress
_Zxr10PingCommonExtOpIpAddr7_Object = MibTableColumn
zxr10PingCommonExtOpIpAddr7 = _Zxr10PingCommonExtOpIpAddr7_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 104, 2, 1, 1, 21),
    _Zxr10PingCommonExtOpIpAddr7_Type()
)
zxr10PingCommonExtOpIpAddr7.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxr10PingCommonExtOpIpAddr7.setStatus("current")
_Zxr10PingCommonExtOpIpAddr8_Type = IpAddress
_Zxr10PingCommonExtOpIpAddr8_Object = MibTableColumn
zxr10PingCommonExtOpIpAddr8 = _Zxr10PingCommonExtOpIpAddr8_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 104, 2, 1, 1, 22),
    _Zxr10PingCommonExtOpIpAddr8_Type()
)
zxr10PingCommonExtOpIpAddr8.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxr10PingCommonExtOpIpAddr8.setStatus("current")
_Zxr10PingCommonExtOpIpAddr9_Type = IpAddress
_Zxr10PingCommonExtOpIpAddr9_Object = MibTableColumn
zxr10PingCommonExtOpIpAddr9 = _Zxr10PingCommonExtOpIpAddr9_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 104, 2, 1, 1, 23),
    _Zxr10PingCommonExtOpIpAddr9_Type()
)
zxr10PingCommonExtOpIpAddr9.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxr10PingCommonExtOpIpAddr9.setStatus("current")


class _Zxr10PingCommonExtOpRecordNum_Type(Integer32):
    """Custom type zxr10PingCommonExtOpRecordNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 9),
    )


_Zxr10PingCommonExtOpRecordNum_Type.__name__ = "Integer32"
_Zxr10PingCommonExtOpRecordNum_Object = MibTableColumn
zxr10PingCommonExtOpRecordNum = _Zxr10PingCommonExtOpRecordNum_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 104, 2, 1, 1, 24),
    _Zxr10PingCommonExtOpRecordNum_Type()
)
zxr10PingCommonExtOpRecordNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxr10PingCommonExtOpRecordNum.setStatus("current")


class _Zxr10PingCommonExtOpTimestampNum_Type(Integer32):
    """Custom type zxr10PingCommonExtOpTimestampNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 9),
    )


_Zxr10PingCommonExtOpTimestampNum_Type.__name__ = "Integer32"
_Zxr10PingCommonExtOpTimestampNum_Object = MibTableColumn
zxr10PingCommonExtOpTimestampNum = _Zxr10PingCommonExtOpTimestampNum_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 104, 2, 1, 1, 25),
    _Zxr10PingCommonExtOpTimestampNum_Type()
)
zxr10PingCommonExtOpTimestampNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxr10PingCommonExtOpTimestampNum.setStatus("current")


class _Zxr10PingCommonRosStatus_Type(Integer32):
    """Custom type zxr10PingCommonRosStatus based on Integer32"""
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
        *(("not-active", 1),
          ("ping-completed", 4),
          ("ping-processing", 3),
          ("start-ping", 2))
    )


_Zxr10PingCommonRosStatus_Type.__name__ = "Integer32"
_Zxr10PingCommonRosStatus_Object = MibTableColumn
zxr10PingCommonRosStatus = _Zxr10PingCommonRosStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 104, 2, 1, 1, 26),
    _Zxr10PingCommonRosStatus_Type()
)
zxr10PingCommonRosStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxr10PingCommonRosStatus.setStatus("current")
_Zxr10PingCommonEntryOwner_Type = DisplayString
_Zxr10PingCommonEntryOwner_Object = MibTableColumn
zxr10PingCommonEntryOwner = _Zxr10PingCommonEntryOwner_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 104, 2, 1, 1, 27),
    _Zxr10PingCommonEntryOwner_Type()
)
zxr10PingCommonEntryOwner.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxr10PingCommonEntryOwner.setStatus("current")


class _Zxr10PingCommonTrapOncompletion_Type(TruthValue):
    """Custom type zxr10PingCommonTrapOncompletion based on TruthValue"""


_Zxr10PingCommonTrapOncompletion_Object = MibTableColumn
zxr10PingCommonTrapOncompletion = _Zxr10PingCommonTrapOncompletion_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 104, 2, 1, 1, 28),
    _Zxr10PingCommonTrapOncompletion_Type()
)
zxr10PingCommonTrapOncompletion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxr10PingCommonTrapOncompletion.setStatus("current")
_Zxr10PingResultTable_Object = MibTable
zxr10PingResultTable = _Zxr10PingResultTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 104, 2, 2)
)
if mibBuilder.loadTexts:
    zxr10PingResultTable.setStatus("current")
_Zxr10pingResultEntry_Object = MibTableRow
zxr10pingResultEntry = _Zxr10pingResultEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 104, 2, 2, 1)
)
zxr10pingResultEntry.setIndexNames(
    (0, "ZXR10-PING-MIB", "zxr10PingCommResultSerial"),
)
if mibBuilder.loadTexts:
    zxr10pingResultEntry.setStatus("current")
_Zxr10PingCommResultSerial_Type = Integer32
_Zxr10PingCommResultSerial_Object = MibTableColumn
zxr10PingCommResultSerial = _Zxr10PingCommResultSerial_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 104, 2, 2, 1, 1),
    _Zxr10PingCommResultSerial_Type()
)
zxr10PingCommResultSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10PingCommResultSerial.setStatus("current")
_Zxr10PingCommResultSentPkts_Type = Integer32
_Zxr10PingCommResultSentPkts_Object = MibTableColumn
zxr10PingCommResultSentPkts = _Zxr10PingCommResultSentPkts_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 104, 2, 2, 1, 2),
    _Zxr10PingCommResultSentPkts_Type()
)
zxr10PingCommResultSentPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10PingCommResultSentPkts.setStatus("current")
_Zxr10PingCommResultRcvPkts_Type = Integer32
_Zxr10PingCommResultRcvPkts_Object = MibTableColumn
zxr10PingCommResultRcvPkts = _Zxr10PingCommResultRcvPkts_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 104, 2, 2, 1, 3),
    _Zxr10PingCommResultRcvPkts_Type()
)
zxr10PingCommResultRcvPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10PingCommResultRcvPkts.setStatus("current")
_Zxr10PingCommResultRoundTripMinTime_Type = Integer32
_Zxr10PingCommResultRoundTripMinTime_Object = MibTableColumn
zxr10PingCommResultRoundTripMinTime = _Zxr10PingCommResultRoundTripMinTime_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 104, 2, 2, 1, 4),
    _Zxr10PingCommResultRoundTripMinTime_Type()
)
zxr10PingCommResultRoundTripMinTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10PingCommResultRoundTripMinTime.setStatus("current")
_Zxr10PingCommResultRoundTripMaxTime_Type = Integer32
_Zxr10PingCommResultRoundTripMaxTime_Object = MibTableColumn
zxr10PingCommResultRoundTripMaxTime = _Zxr10PingCommResultRoundTripMaxTime_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 104, 2, 2, 1, 5),
    _Zxr10PingCommResultRoundTripMaxTime_Type()
)
zxr10PingCommResultRoundTripMaxTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10PingCommResultRoundTripMaxTime.setStatus("current")
_Zxr10PingCommResultRoundTripAvgTime_Type = Integer32
_Zxr10PingCommResultRoundTripAvgTime_Object = MibTableColumn
zxr10PingCommResultRoundTripAvgTime = _Zxr10PingCommResultRoundTripAvgTime_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 104, 2, 2, 1, 6),
    _Zxr10PingCommResultRoundTripAvgTime_Type()
)
zxr10PingCommResultRoundTripAvgTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10PingCommResultRoundTripAvgTime.setStatus("current")
_Zxr10PingCommExtResultTimeStampInfo_Type = DisplayString
_Zxr10PingCommExtResultTimeStampInfo_Object = MibTableColumn
zxr10PingCommExtResultTimeStampInfo = _Zxr10PingCommExtResultTimeStampInfo_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 104, 2, 2, 1, 7),
    _Zxr10PingCommExtResultTimeStampInfo_Type()
)
zxr10PingCommExtResultTimeStampInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10PingCommExtResultTimeStampInfo.setStatus("current")
_Zxr10PingCommExtResultIpAddrInfo_Type = DisplayString
_Zxr10PingCommExtResultIpAddrInfo_Object = MibTableColumn
zxr10PingCommExtResultIpAddrInfo = _Zxr10PingCommExtResultIpAddrInfo_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 104, 2, 2, 1, 8),
    _Zxr10PingCommExtResultIpAddrInfo_Type()
)
zxr10PingCommExtResultIpAddrInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10PingCommExtResultIpAddrInfo.setStatus("current")
_Zxr10PingCommResultEntryOwner_Type = DisplayString
_Zxr10PingCommResultEntryOwner_Object = MibTableColumn
zxr10PingCommResultEntryOwner = _Zxr10PingCommResultEntryOwner_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 104, 2, 2, 1, 9),
    _Zxr10PingCommResultEntryOwner_Type()
)
zxr10PingCommResultEntryOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10PingCommResultEntryOwner.setStatus("current")
_Zxr10PingCommResultRoundWobbleMinTime_Type = Integer32
_Zxr10PingCommResultRoundWobbleMinTime_Object = MibTableColumn
zxr10PingCommResultRoundWobbleMinTime = _Zxr10PingCommResultRoundWobbleMinTime_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 104, 2, 2, 1, 10),
    _Zxr10PingCommResultRoundWobbleMinTime_Type()
)
zxr10PingCommResultRoundWobbleMinTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10PingCommResultRoundWobbleMinTime.setStatus("current")
_Zxr10PingCommResultRoundWobbleMaxTime_Type = Integer32
_Zxr10PingCommResultRoundWobbleMaxTime_Object = MibTableColumn
zxr10PingCommResultRoundWobbleMaxTime = _Zxr10PingCommResultRoundWobbleMaxTime_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 104, 2, 2, 1, 11),
    _Zxr10PingCommResultRoundWobbleMaxTime_Type()
)
zxr10PingCommResultRoundWobbleMaxTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10PingCommResultRoundWobbleMaxTime.setStatus("current")
_Zxr10PingCommResultRoundWobbleAvgTime_Type = Integer32
_Zxr10PingCommResultRoundWobbleAvgTime_Object = MibTableColumn
zxr10PingCommResultRoundWobbleAvgTime = _Zxr10PingCommResultRoundWobbleAvgTime_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 104, 2, 2, 1, 12),
    _Zxr10PingCommResultRoundWobbleAvgTime_Type()
)
zxr10PingCommResultRoundWobbleAvgTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10PingCommResultRoundWobbleAvgTime.setStatus("current")
_PingNotifications_ObjectIdentity = ObjectIdentity
pingNotifications = _PingNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 3, 104, 2, 3)
)

# Managed Objects groups


# Notification objects

pingTrapResult = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 3, 104, 2, 3, 1)
)
pingTrapResult.setObjects(
      *(("ZXR10-PING-MIB", "zxr10PingCommResultSerial"),
        ("ZXR10-PING-MIB", "zxr10PingCommResultSentPkts"),
        ("ZXR10-PING-MIB", "zxr10PingCommResultRcvPkts"),
        ("ZXR10-PING-MIB", "zxr10PingCommResultRoundTripMinTime"),
        ("ZXR10-PING-MIB", "zxr10PingCommResultRoundTripMaxTime"),
        ("ZXR10-PING-MIB", "zxr10PingCommResultRoundTripAvgTime"))
)
if mibBuilder.loadTexts:
    pingTrapResult.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZXR10-PING-MIB",
    **{"DisplayString": DisplayString,
       "zxr10PingMIB": zxr10PingMIB,
       "zxr10PingTable": zxr10PingTable,
       "zxr10pingCommonEntry": zxr10pingCommonEntry,
       "zxr10PingCommonSerial": zxr10PingCommonSerial,
       "zxr10PingCommonPingType": zxr10PingCommonPingType,
       "zxr10PingCommonDestAddr": zxr10PingCommonDestAddr,
       "zxr10PingCommonVrfName": zxr10PingCommonVrfName,
       "zxr10PingCommonIfOption": zxr10PingCommonIfOption,
       "zxr10PingCommonPacketCount": zxr10PingCommonPacketCount,
       "zxr10PingCommonTimeOut": zxr10PingCommonTimeOut,
       "zxr10PingCommonDataLen": zxr10PingCommonDataLen,
       "zxr10PingCommonIfExtOption": zxr10PingCommonIfExtOption,
       "zxr10PingCommonExtSourceAddr": zxr10PingCommonExtSourceAddr,
       "zxr10PingCommonExtTos": zxr10PingCommonExtTos,
       "zxr10PingCommonExtTTL": zxr10PingCommonExtTTL,
       "zxr10PingCommonExtFragement": zxr10PingCommonExtFragement,
       "zxr10PingCommonExtOpType": zxr10PingCommonExtOpType,
       "zxr10PingCommonExtOpIpAddr1": zxr10PingCommonExtOpIpAddr1,
       "zxr10PingCommonExtOpIpAddr2": zxr10PingCommonExtOpIpAddr2,
       "zxr10PingCommonExtOpIpAddr3": zxr10PingCommonExtOpIpAddr3,
       "zxr10PingCommonExtOpIpAddr4": zxr10PingCommonExtOpIpAddr4,
       "zxr10PingCommonExtOpIpAddr5": zxr10PingCommonExtOpIpAddr5,
       "zxr10PingCommonExtOpIpAddr6": zxr10PingCommonExtOpIpAddr6,
       "zxr10PingCommonExtOpIpAddr7": zxr10PingCommonExtOpIpAddr7,
       "zxr10PingCommonExtOpIpAddr8": zxr10PingCommonExtOpIpAddr8,
       "zxr10PingCommonExtOpIpAddr9": zxr10PingCommonExtOpIpAddr9,
       "zxr10PingCommonExtOpRecordNum": zxr10PingCommonExtOpRecordNum,
       "zxr10PingCommonExtOpTimestampNum": zxr10PingCommonExtOpTimestampNum,
       "zxr10PingCommonRosStatus": zxr10PingCommonRosStatus,
       "zxr10PingCommonEntryOwner": zxr10PingCommonEntryOwner,
       "zxr10PingCommonTrapOncompletion": zxr10PingCommonTrapOncompletion,
       "zxr10PingResultTable": zxr10PingResultTable,
       "zxr10pingResultEntry": zxr10pingResultEntry,
       "zxr10PingCommResultSerial": zxr10PingCommResultSerial,
       "zxr10PingCommResultSentPkts": zxr10PingCommResultSentPkts,
       "zxr10PingCommResultRcvPkts": zxr10PingCommResultRcvPkts,
       "zxr10PingCommResultRoundTripMinTime": zxr10PingCommResultRoundTripMinTime,
       "zxr10PingCommResultRoundTripMaxTime": zxr10PingCommResultRoundTripMaxTime,
       "zxr10PingCommResultRoundTripAvgTime": zxr10PingCommResultRoundTripAvgTime,
       "zxr10PingCommExtResultTimeStampInfo": zxr10PingCommExtResultTimeStampInfo,
       "zxr10PingCommExtResultIpAddrInfo": zxr10PingCommExtResultIpAddrInfo,
       "zxr10PingCommResultEntryOwner": zxr10PingCommResultEntryOwner,
       "zxr10PingCommResultRoundWobbleMinTime": zxr10PingCommResultRoundWobbleMinTime,
       "zxr10PingCommResultRoundWobbleMaxTime": zxr10PingCommResultRoundWobbleMaxTime,
       "zxr10PingCommResultRoundWobbleAvgTime": zxr10PingCommResultRoundWobbleAvgTime,
       "pingNotifications": pingNotifications,
       "pingTrapResult": pingTrapResult}
)
