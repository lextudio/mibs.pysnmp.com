# SNMP MIB module (CTIF-EXT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CTIF-EXT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:18:25 2024
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

(ctronMib2,) = mibBuilder.importSymbols(
    "CTRON-MIB-NAMES",
    "ctronMib2")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CommonDev_ObjectIdentity = ObjectIdentity
commonDev = _CommonDev_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 3, 3, 1)
)


class _ComDeviceTime_Type(DisplayString):
    """Custom type comDeviceTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
        ValueSizeConstraint(8, 8),
    )


_ComDeviceTime_Type.__name__ = "DisplayString"
_ComDeviceTime_Object = MibScalar
comDeviceTime = _ComDeviceTime_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 3, 3, 1, 1),
    _ComDeviceTime_Type()
)
comDeviceTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    comDeviceTime.setStatus("mandatory")


class _ComDeviceDate_Type(DisplayString):
    """Custom type comDeviceDate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_ComDeviceDate_Type.__name__ = "DisplayString"
_ComDeviceDate_Object = MibScalar
comDeviceDate = _ComDeviceDate_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 3, 3, 1, 2),
    _ComDeviceDate_Type()
)
comDeviceDate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    comDeviceDate.setStatus("mandatory")
_ComDeviceBoardMap_Type = Integer32
_ComDeviceBoardMap_Object = MibScalar
comDeviceBoardMap = _ComDeviceBoardMap_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 3, 3, 1, 3),
    _ComDeviceBoardMap_Type()
)
comDeviceBoardMap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    comDeviceBoardMap.setStatus("mandatory")
_CtIf_ObjectIdentity = ObjectIdentity
ctIf = _CtIf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 3, 3, 2)
)
_CtIfTable_Object = MibTable
ctIfTable = _CtIfTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 3, 3, 2, 1)
)
if mibBuilder.loadTexts:
    ctIfTable.setStatus("mandatory")
_CtIfEntry_Object = MibTableRow
ctIfEntry = _CtIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 3, 3, 2, 1, 1)
)
ctIfEntry.setIndexNames(
    (0, "CTIF-EXT-MIB", "ctIfNumber"),
)
if mibBuilder.loadTexts:
    ctIfEntry.setStatus("mandatory")
_CtIfNumber_Type = Integer32
_CtIfNumber_Object = MibTableColumn
ctIfNumber = _CtIfNumber_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 3, 3, 2, 1, 1, 1),
    _CtIfNumber_Type()
)
ctIfNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctIfNumber.setStatus("mandatory")
_CtIfPortCnt_Type = Integer32
_CtIfPortCnt_Object = MibTableColumn
ctIfPortCnt = _CtIfPortCnt_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 3, 3, 2, 1, 1, 2),
    _CtIfPortCnt_Type()
)
ctIfPortCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctIfPortCnt.setStatus("mandatory")
_CtIfConnectionType_Type = ObjectIdentifier
_CtIfConnectionType_Object = MibTableColumn
ctIfConnectionType = _CtIfConnectionType_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 3, 3, 2, 1, 1, 3),
    _CtIfConnectionType_Type()
)
ctIfConnectionType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctIfConnectionType.setStatus("mandatory")


class _CtIfLAA_Type(OctetString):
    """Custom type ctIfLAA based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_CtIfLAA_Type.__name__ = "OctetString"
_CtIfLAA_Object = MibTableColumn
ctIfLAA = _CtIfLAA_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 3, 3, 2, 1, 1, 4),
    _CtIfLAA_Type()
)
ctIfLAA.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctIfLAA.setStatus("mandatory")


class _CtIfDuplex_Type(Integer32):
    """Custom type ctIfDuplex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("full", 3),
          ("other", 1),
          ("standard", 2))
    )


_CtIfDuplex_Type.__name__ = "Integer32"
_CtIfDuplex_Object = MibTableColumn
ctIfDuplex = _CtIfDuplex_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 3, 3, 2, 1, 1, 5),
    _CtIfDuplex_Type()
)
ctIfDuplex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctIfDuplex.setStatus("mandatory")


class _CtIfCapability_Type(Integer32):
    """Custom type ctIfCapability based on Integer32"""
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
        *(("ethernetBased", 5),
          ("fastEthernet", 4),
          ("fullDuplex", 3),
          ("other", 1),
          ("standard", 2))
    )


_CtIfCapability_Type.__name__ = "Integer32"
_CtIfCapability_Object = MibTableColumn
ctIfCapability = _CtIfCapability_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 3, 3, 2, 1, 1, 6),
    _CtIfCapability_Type()
)
ctIfCapability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctIfCapability.setStatus("mandatory")


class _CtIfRedundancy_Type(Integer32):
    """Custom type ctIfRedundancy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("not-redundant", 2),
          ("redundant", 1))
    )


_CtIfRedundancy_Type.__name__ = "Integer32"
_CtIfRedundancy_Object = MibTableColumn
ctIfRedundancy = _CtIfRedundancy_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 3, 3, 2, 1, 1, 7),
    _CtIfRedundancy_Type()
)
ctIfRedundancy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctIfRedundancy.setStatus("mandatory")
_CtIfPort_ObjectIdentity = ObjectIdentity
ctIfPort = _CtIfPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 3, 3, 3)
)
_CtIfPortTable_Object = MibTable
ctIfPortTable = _CtIfPortTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 3, 3, 3, 1)
)
if mibBuilder.loadTexts:
    ctIfPortTable.setStatus("mandatory")
_CtIfPortEntry_Object = MibTableRow
ctIfPortEntry = _CtIfPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 3, 3, 3, 1, 1)
)
ctIfPortEntry.setIndexNames(
    (0, "CTIF-EXT-MIB", "ctIfPortIfNumber"),
    (0, "CTIF-EXT-MIB", "ctIfPortPortNumber"),
)
if mibBuilder.loadTexts:
    ctIfPortEntry.setStatus("mandatory")
_CtIfPortPortNumber_Type = Integer32
_CtIfPortPortNumber_Object = MibTableColumn
ctIfPortPortNumber = _CtIfPortPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 3, 3, 3, 1, 1, 1),
    _CtIfPortPortNumber_Type()
)
ctIfPortPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctIfPortPortNumber.setStatus("mandatory")
_CtIfPortIfNumber_Type = Integer32
_CtIfPortIfNumber_Object = MibTableColumn
ctIfPortIfNumber = _CtIfPortIfNumber_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 3, 3, 3, 1, 1, 2),
    _CtIfPortIfNumber_Type()
)
ctIfPortIfNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctIfPortIfNumber.setStatus("mandatory")
_CtIfPortType_Type = ObjectIdentifier
_CtIfPortType_Object = MibTableColumn
ctIfPortType = _CtIfPortType_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 3, 3, 3, 1, 1, 3),
    _CtIfPortType_Type()
)
ctIfPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctIfPortType.setStatus("mandatory")


class _CtIfPortLinkStatus_Type(Integer32):
    """Custom type ctIfPortLinkStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("linked", 2),
          ("notApplicable", 3),
          ("notLinked", 1))
    )


_CtIfPortLinkStatus_Type.__name__ = "Integer32"
_CtIfPortLinkStatus_Object = MibTableColumn
ctIfPortLinkStatus = _CtIfPortLinkStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 3, 3, 3, 1, 1, 4),
    _CtIfPortLinkStatus_Type()
)
ctIfPortLinkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctIfPortLinkStatus.setStatus("mandatory")


class _CtIfPortTrapStatus_Type(Integer32):
    """Custom type ctIfPortTrapStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_CtIfPortTrapStatus_Type.__name__ = "Integer32"
_CtIfPortTrapStatus_Object = MibTableColumn
ctIfPortTrapStatus = _CtIfPortTrapStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 3, 3, 3, 1, 1, 5),
    _CtIfPortTrapStatus_Type()
)
ctIfPortTrapStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctIfPortTrapStatus.setStatus("mandatory")
_CtIfCp_ObjectIdentity = ObjectIdentity
ctIfCp = _CtIfCp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 3, 3, 4)
)
_CtCpTable_Object = MibTable
ctCpTable = _CtCpTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 3, 3, 4, 1)
)
if mibBuilder.loadTexts:
    ctCpTable.setStatus("mandatory")
_CtCpEntry_Object = MibTableRow
ctCpEntry = _CtCpEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 3, 3, 4, 1, 1)
)
ctCpEntry.setIndexNames(
    (0, "CTIF-EXT-MIB", "ctComPort"),
)
if mibBuilder.loadTexts:
    ctCpEntry.setStatus("mandatory")
_CtComPort_Type = Integer32
_CtComPort_Object = MibTableColumn
ctComPort = _CtComPort_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 3, 3, 4, 1, 1, 1),
    _CtComPort_Type()
)
ctComPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctComPort.setStatus("mandatory")


class _CtCpFunction_Type(Integer32):
    """Custom type ctCpFunction based on Integer32"""
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
        *(("lm", 1),
          ("ppp", 4),
          ("slip", 3),
          ("ups", 2))
    )


_CtCpFunction_Type.__name__ = "Integer32"
_CtCpFunction_Object = MibTableColumn
ctCpFunction = _CtCpFunction_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 3, 3, 4, 1, 1, 2),
    _CtCpFunction_Type()
)
ctCpFunction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctCpFunction.setStatus("mandatory")
_CtIfNum_Type = Integer32
_CtIfNum_Object = MibTableColumn
ctIfNum = _CtIfNum_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 3, 3, 4, 1, 1, 3),
    _CtIfNum_Type()
)
ctIfNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctIfNum.setStatus("mandatory")


class _CtCpAdminStatus_Type(Integer32):
    """Custom type ctCpAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_CtCpAdminStatus_Type.__name__ = "Integer32"
_CtCpAdminStatus_Object = MibTableColumn
ctCpAdminStatus = _CtCpAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 3, 3, 4, 1, 1, 4),
    _CtCpAdminStatus_Type()
)
ctCpAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctCpAdminStatus.setStatus("mandatory")
_CtSNMP_ObjectIdentity = ObjectIdentity
ctSNMP = _CtSNMP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 3, 3, 5)
)


class _EnableSNMPv1_Type(Integer32):
    """Custom type enableSNMPv1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_EnableSNMPv1_Type.__name__ = "Integer32"
_EnableSNMPv1_Object = MibScalar
enableSNMPv1 = _EnableSNMPv1_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 3, 3, 5, 1),
    _EnableSNMPv1_Type()
)
enableSNMPv1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enableSNMPv1.setStatus("mandatory")


class _EnableSNMPv2_Type(Integer32):
    """Custom type enableSNMPv2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_EnableSNMPv2_Type.__name__ = "Integer32"
_EnableSNMPv2_Object = MibScalar
enableSNMPv2 = _EnableSNMPv2_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 3, 3, 5, 2),
    _EnableSNMPv2_Type()
)
enableSNMPv2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enableSNMPv2.setStatus("mandatory")


class _EnableSNMPv1Counter64_Type(Integer32):
    """Custom type enableSNMPv1Counter64 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_EnableSNMPv1Counter64_Type.__name__ = "Integer32"
_EnableSNMPv1Counter64_Object = MibScalar
enableSNMPv1Counter64 = _EnableSNMPv1Counter64_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 3, 3, 5, 3),
    _EnableSNMPv1Counter64_Type()
)
enableSNMPv1Counter64.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enableSNMPv1Counter64.setStatus("mandatory")
_CtSonet_ObjectIdentity = ObjectIdentity
ctSonet = _CtSonet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 3, 3, 6)
)
_CtSonetTable_Object = MibTable
ctSonetTable = _CtSonetTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 3, 3, 6, 1)
)
if mibBuilder.loadTexts:
    ctSonetTable.setStatus("deprecated")
_CtSonetEntry_Object = MibTableRow
ctSonetEntry = _CtSonetEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 3, 3, 6, 1, 1)
)
ctSonetEntry.setIndexNames(
    (0, "CTIF-EXT-MIB", "ctSonetIfIndex"),
)
if mibBuilder.loadTexts:
    ctSonetEntry.setStatus("deprecated")
_CtSonetIfIndex_Type = Integer32
_CtSonetIfIndex_Object = MibTableColumn
ctSonetIfIndex = _CtSonetIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 3, 3, 6, 1, 1, 1),
    _CtSonetIfIndex_Type()
)
ctSonetIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctSonetIfIndex.setStatus("deprecated")


class _CtSonetMediumType_Type(Integer32):
    """Custom type ctSonetMediumType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("sdh", 2),
          ("sonet", 1))
    )


_CtSonetMediumType_Type.__name__ = "Integer32"
_CtSonetMediumType_Object = MibTableColumn
ctSonetMediumType = _CtSonetMediumType_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 3, 3, 6, 1, 1, 2),
    _CtSonetMediumType_Type()
)
ctSonetMediumType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctSonetMediumType.setStatus("deprecated")
_CtVirtual_ObjectIdentity = ObjectIdentity
ctVirtual = _CtVirtual_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 3, 3, 7)
)
_CtVirtualIfTable_Object = MibTable
ctVirtualIfTable = _CtVirtualIfTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 3, 3, 7, 1)
)
if mibBuilder.loadTexts:
    ctVirtualIfTable.setStatus("mandatory")
_CtVirtualIfEntry_Object = MibTableRow
ctVirtualIfEntry = _CtVirtualIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 3, 3, 7, 1, 1)
)
ctVirtualIfEntry.setIndexNames(
    (0, "CTIF-EXT-MIB", "ctVirtualIfIndex"),
)
if mibBuilder.loadTexts:
    ctVirtualIfEntry.setStatus("mandatory")
_CtVirtualIfIndex_Type = Integer32
_CtVirtualIfIndex_Object = MibTableColumn
ctVirtualIfIndex = _CtVirtualIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 3, 3, 7, 1, 1, 1),
    _CtVirtualIfIndex_Type()
)
ctVirtualIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctVirtualIfIndex.setStatus("mandatory")
_CtVirtualIfPhysicalInterface_Type = Integer32
_CtVirtualIfPhysicalInterface_Object = MibTableColumn
ctVirtualIfPhysicalInterface = _CtVirtualIfPhysicalInterface_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 3, 3, 7, 1, 1, 2),
    _CtVirtualIfPhysicalInterface_Type()
)
ctVirtualIfPhysicalInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctVirtualIfPhysicalInterface.setStatus("mandatory")
_CtVirtualIfType_Type = ObjectIdentifier
_CtVirtualIfType_Object = MibTableColumn
ctVirtualIfType = _CtVirtualIfType_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 3, 3, 7, 1, 1, 3),
    _CtVirtualIfType_Type()
)
ctVirtualIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctVirtualIfType.setStatus("mandatory")
_CtVirtualIfNumPorts_Type = Integer32
_CtVirtualIfNumPorts_Object = MibTableColumn
ctVirtualIfNumPorts = _CtVirtualIfNumPorts_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 3, 3, 7, 1, 1, 4),
    _CtVirtualIfNumPorts_Type()
)
ctVirtualIfNumPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctVirtualIfNumPorts.setStatus("mandatory")
_CtVirtualIfPortTable_Object = MibTable
ctVirtualIfPortTable = _CtVirtualIfPortTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 3, 3, 7, 2)
)
if mibBuilder.loadTexts:
    ctVirtualIfPortTable.setStatus("mandatory")
_CtVirtualIfPortEntry_Object = MibTableRow
ctVirtualIfPortEntry = _CtVirtualIfPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 3, 3, 7, 2, 1)
)
ctVirtualIfPortEntry.setIndexNames(
    (0, "CTIF-EXT-MIB", "ctVirtualIfPortIfIndex"),
    (0, "CTIF-EXT-MIB", "ctVirtualIfPortNumber"),
)
if mibBuilder.loadTexts:
    ctVirtualIfPortEntry.setStatus("mandatory")
_CtVirtualIfPortIfIndex_Type = Integer32
_CtVirtualIfPortIfIndex_Object = MibTableColumn
ctVirtualIfPortIfIndex = _CtVirtualIfPortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 3, 3, 7, 2, 1, 1),
    _CtVirtualIfPortIfIndex_Type()
)
ctVirtualIfPortIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctVirtualIfPortIfIndex.setStatus("mandatory")
_CtVirtualIfPortNumber_Type = Integer32
_CtVirtualIfPortNumber_Object = MibTableColumn
ctVirtualIfPortNumber = _CtVirtualIfPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 3, 3, 7, 2, 1, 2),
    _CtVirtualIfPortNumber_Type()
)
ctVirtualIfPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctVirtualIfPortNumber.setStatus("mandatory")


class _CtVirtualIfPortType_Type(Integer32):
    """Custom type ctVirtualIfPortType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("portVirtualTypePvcLlc", 2),
          ("portVirtualTypePvcVcmux", 3),
          ("portVirtualTypeSvc", 1))
    )


_CtVirtualIfPortType_Type.__name__ = "Integer32"
_CtVirtualIfPortType_Object = MibTableColumn
ctVirtualIfPortType = _CtVirtualIfPortType_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 3, 3, 7, 2, 1, 3),
    _CtVirtualIfPortType_Type()
)
ctVirtualIfPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctVirtualIfPortType.setStatus("mandatory")
_CtVirtualIfPortVPI_Type = Integer32
_CtVirtualIfPortVPI_Object = MibTableColumn
ctVirtualIfPortVPI = _CtVirtualIfPortVPI_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 3, 3, 7, 2, 1, 4),
    _CtVirtualIfPortVPI_Type()
)
ctVirtualIfPortVPI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctVirtualIfPortVPI.setStatus("mandatory")
_CtVirtualIfPortVCI_Type = Integer32
_CtVirtualIfPortVCI_Object = MibTableColumn
ctVirtualIfPortVCI = _CtVirtualIfPortVCI_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 3, 3, 7, 2, 1, 5),
    _CtVirtualIfPortVCI_Type()
)
ctVirtualIfPortVCI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctVirtualIfPortVCI.setStatus("mandatory")
_CtStats_ObjectIdentity = ObjectIdentity
ctStats = _CtStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 3, 3, 8)
)
_CtStatsTable_Object = MibTable
ctStatsTable = _CtStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 3, 3, 8, 1)
)
if mibBuilder.loadTexts:
    ctStatsTable.setStatus("mandatory")
_CtStatsEntry_Object = MibTableRow
ctStatsEntry = _CtStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 3, 3, 8, 1, 1)
)
ctStatsEntry.setIndexNames(
    (0, "CTIF-EXT-MIB", "ctStatsIfIndex"),
)
if mibBuilder.loadTexts:
    ctStatsEntry.setStatus("mandatory")
_CtStatsIfIndex_Type = Integer32
_CtStatsIfIndex_Object = MibTableColumn
ctStatsIfIndex = _CtStatsIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 3, 3, 8, 1, 1, 1),
    _CtStatsIfIndex_Type()
)
ctStatsIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctStatsIfIndex.setStatus("mandatory")


class _CtStatsIfEnable_Type(Integer32):
    """Custom type ctStatsIfEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_CtStatsIfEnable_Type.__name__ = "Integer32"
_CtStatsIfEnable_Object = MibTableColumn
ctStatsIfEnable = _CtStatsIfEnable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 3, 3, 8, 1, 1, 2),
    _CtStatsIfEnable_Type()
)
ctStatsIfEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctStatsIfEnable.setStatus("mandatory")
_CtFramerConfig_ObjectIdentity = ObjectIdentity
ctFramerConfig = _CtFramerConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 3, 3, 9)
)
_CtIfHC_ObjectIdentity = ObjectIdentity
ctIfHC = _CtIfHC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 3, 3, 10)
)
_CtIfHCStatsTable_Object = MibTable
ctIfHCStatsTable = _CtIfHCStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 3, 3, 10, 1)
)
if mibBuilder.loadTexts:
    ctIfHCStatsTable.setStatus("mandatory")
_CtIfHCStatsEntry_Object = MibTableRow
ctIfHCStatsEntry = _CtIfHCStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 3, 3, 10, 1, 1)
)
ctIfHCStatsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    ctIfHCStatsEntry.setStatus("mandatory")
_CtIfInOctets_Type = Counter32
_CtIfInOctets_Object = MibTableColumn
ctIfInOctets = _CtIfInOctets_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 3, 3, 10, 1, 1, 1),
    _CtIfInOctets_Type()
)
ctIfInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctIfInOctets.setStatus("mandatory")
_CtIfInOctetsOverflows_Type = Counter32
_CtIfInOctetsOverflows_Object = MibTableColumn
ctIfInOctetsOverflows = _CtIfInOctetsOverflows_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 3, 3, 10, 1, 1, 2),
    _CtIfInOctetsOverflows_Type()
)
ctIfInOctetsOverflows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctIfInOctetsOverflows.setStatus("mandatory")
_CtIfInUcastPkts_Type = Counter32
_CtIfInUcastPkts_Object = MibTableColumn
ctIfInUcastPkts = _CtIfInUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 3, 3, 10, 1, 1, 3),
    _CtIfInUcastPkts_Type()
)
ctIfInUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctIfInUcastPkts.setStatus("mandatory")
_CtIfInUcastPktsOverflows_Type = Counter32
_CtIfInUcastPktsOverflows_Object = MibTableColumn
ctIfInUcastPktsOverflows = _CtIfInUcastPktsOverflows_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 3, 3, 10, 1, 1, 4),
    _CtIfInUcastPktsOverflows_Type()
)
ctIfInUcastPktsOverflows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctIfInUcastPktsOverflows.setStatus("mandatory")
_CtIfInMulticastPkts_Type = Counter32
_CtIfInMulticastPkts_Object = MibTableColumn
ctIfInMulticastPkts = _CtIfInMulticastPkts_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 3, 3, 10, 1, 1, 5),
    _CtIfInMulticastPkts_Type()
)
ctIfInMulticastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctIfInMulticastPkts.setStatus("mandatory")
_CtIfInMulticastPktsOverflows_Type = Counter32
_CtIfInMulticastPktsOverflows_Object = MibTableColumn
ctIfInMulticastPktsOverflows = _CtIfInMulticastPktsOverflows_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 3, 3, 10, 1, 1, 6),
    _CtIfInMulticastPktsOverflows_Type()
)
ctIfInMulticastPktsOverflows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctIfInMulticastPktsOverflows.setStatus("mandatory")
_CtIfInBroadcastPkts_Type = Counter32
_CtIfInBroadcastPkts_Object = MibTableColumn
ctIfInBroadcastPkts = _CtIfInBroadcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 3, 3, 10, 1, 1, 7),
    _CtIfInBroadcastPkts_Type()
)
ctIfInBroadcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctIfInBroadcastPkts.setStatus("mandatory")
_CtIfInBroadcastPktsOverflows_Type = Counter32
_CtIfInBroadcastPktsOverflows_Object = MibTableColumn
ctIfInBroadcastPktsOverflows = _CtIfInBroadcastPktsOverflows_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 3, 3, 10, 1, 1, 8),
    _CtIfInBroadcastPktsOverflows_Type()
)
ctIfInBroadcastPktsOverflows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctIfInBroadcastPktsOverflows.setStatus("mandatory")
_CtIfOutOctets_Type = Counter32
_CtIfOutOctets_Object = MibTableColumn
ctIfOutOctets = _CtIfOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 3, 3, 10, 1, 1, 9),
    _CtIfOutOctets_Type()
)
ctIfOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctIfOutOctets.setStatus("mandatory")
_CtIfOutOctetsOverflows_Type = Counter32
_CtIfOutOctetsOverflows_Object = MibTableColumn
ctIfOutOctetsOverflows = _CtIfOutOctetsOverflows_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 3, 3, 10, 1, 1, 10),
    _CtIfOutOctetsOverflows_Type()
)
ctIfOutOctetsOverflows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctIfOutOctetsOverflows.setStatus("mandatory")
_CtIfOutUcastPkts_Type = Counter32
_CtIfOutUcastPkts_Object = MibTableColumn
ctIfOutUcastPkts = _CtIfOutUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 3, 3, 10, 1, 1, 11),
    _CtIfOutUcastPkts_Type()
)
ctIfOutUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctIfOutUcastPkts.setStatus("mandatory")
_CtIfOutUcastPktsOverflows_Type = Counter32
_CtIfOutUcastPktsOverflows_Object = MibTableColumn
ctIfOutUcastPktsOverflows = _CtIfOutUcastPktsOverflows_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 3, 3, 10, 1, 1, 12),
    _CtIfOutUcastPktsOverflows_Type()
)
ctIfOutUcastPktsOverflows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctIfOutUcastPktsOverflows.setStatus("mandatory")
_CtIfOutMulticastPkts_Type = Counter32
_CtIfOutMulticastPkts_Object = MibTableColumn
ctIfOutMulticastPkts = _CtIfOutMulticastPkts_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 3, 3, 10, 1, 1, 13),
    _CtIfOutMulticastPkts_Type()
)
ctIfOutMulticastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctIfOutMulticastPkts.setStatus("mandatory")
_CtIfOutMulticastPktsOverflows_Type = Counter32
_CtIfOutMulticastPktsOverflows_Object = MibTableColumn
ctIfOutMulticastPktsOverflows = _CtIfOutMulticastPktsOverflows_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 3, 3, 10, 1, 1, 14),
    _CtIfOutMulticastPktsOverflows_Type()
)
ctIfOutMulticastPktsOverflows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctIfOutMulticastPktsOverflows.setStatus("mandatory")
_CtIfOutBroadcastPkts_Type = Counter32
_CtIfOutBroadcastPkts_Object = MibTableColumn
ctIfOutBroadcastPkts = _CtIfOutBroadcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 3, 3, 10, 1, 1, 15),
    _CtIfOutBroadcastPkts_Type()
)
ctIfOutBroadcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctIfOutBroadcastPkts.setStatus("mandatory")
_CtIfOutBroadcastPktsOverflows_Type = Counter32
_CtIfOutBroadcastPktsOverflows_Object = MibTableColumn
ctIfOutBroadcastPktsOverflows = _CtIfOutBroadcastPktsOverflows_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 3, 3, 10, 1, 1, 16),
    _CtIfOutBroadcastPktsOverflows_Type()
)
ctIfOutBroadcastPktsOverflows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctIfOutBroadcastPktsOverflows.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CTIF-EXT-MIB",
    **{"commonDev": commonDev,
       "comDeviceTime": comDeviceTime,
       "comDeviceDate": comDeviceDate,
       "comDeviceBoardMap": comDeviceBoardMap,
       "ctIf": ctIf,
       "ctIfTable": ctIfTable,
       "ctIfEntry": ctIfEntry,
       "ctIfNumber": ctIfNumber,
       "ctIfPortCnt": ctIfPortCnt,
       "ctIfConnectionType": ctIfConnectionType,
       "ctIfLAA": ctIfLAA,
       "ctIfDuplex": ctIfDuplex,
       "ctIfCapability": ctIfCapability,
       "ctIfRedundancy": ctIfRedundancy,
       "ctIfPort": ctIfPort,
       "ctIfPortTable": ctIfPortTable,
       "ctIfPortEntry": ctIfPortEntry,
       "ctIfPortPortNumber": ctIfPortPortNumber,
       "ctIfPortIfNumber": ctIfPortIfNumber,
       "ctIfPortType": ctIfPortType,
       "ctIfPortLinkStatus": ctIfPortLinkStatus,
       "ctIfPortTrapStatus": ctIfPortTrapStatus,
       "ctIfCp": ctIfCp,
       "ctCpTable": ctCpTable,
       "ctCpEntry": ctCpEntry,
       "ctComPort": ctComPort,
       "ctCpFunction": ctCpFunction,
       "ctIfNum": ctIfNum,
       "ctCpAdminStatus": ctCpAdminStatus,
       "ctSNMP": ctSNMP,
       "enableSNMPv1": enableSNMPv1,
       "enableSNMPv2": enableSNMPv2,
       "enableSNMPv1Counter64": enableSNMPv1Counter64,
       "ctSonet": ctSonet,
       "ctSonetTable": ctSonetTable,
       "ctSonetEntry": ctSonetEntry,
       "ctSonetIfIndex": ctSonetIfIndex,
       "ctSonetMediumType": ctSonetMediumType,
       "ctVirtual": ctVirtual,
       "ctVirtualIfTable": ctVirtualIfTable,
       "ctVirtualIfEntry": ctVirtualIfEntry,
       "ctVirtualIfIndex": ctVirtualIfIndex,
       "ctVirtualIfPhysicalInterface": ctVirtualIfPhysicalInterface,
       "ctVirtualIfType": ctVirtualIfType,
       "ctVirtualIfNumPorts": ctVirtualIfNumPorts,
       "ctVirtualIfPortTable": ctVirtualIfPortTable,
       "ctVirtualIfPortEntry": ctVirtualIfPortEntry,
       "ctVirtualIfPortIfIndex": ctVirtualIfPortIfIndex,
       "ctVirtualIfPortNumber": ctVirtualIfPortNumber,
       "ctVirtualIfPortType": ctVirtualIfPortType,
       "ctVirtualIfPortVPI": ctVirtualIfPortVPI,
       "ctVirtualIfPortVCI": ctVirtualIfPortVCI,
       "ctStats": ctStats,
       "ctStatsTable": ctStatsTable,
       "ctStatsEntry": ctStatsEntry,
       "ctStatsIfIndex": ctStatsIfIndex,
       "ctStatsIfEnable": ctStatsIfEnable,
       "ctFramerConfig": ctFramerConfig,
       "ctIfHC": ctIfHC,
       "ctIfHCStatsTable": ctIfHCStatsTable,
       "ctIfHCStatsEntry": ctIfHCStatsEntry,
       "ctIfInOctets": ctIfInOctets,
       "ctIfInOctetsOverflows": ctIfInOctetsOverflows,
       "ctIfInUcastPkts": ctIfInUcastPkts,
       "ctIfInUcastPktsOverflows": ctIfInUcastPktsOverflows,
       "ctIfInMulticastPkts": ctIfInMulticastPkts,
       "ctIfInMulticastPktsOverflows": ctIfInMulticastPktsOverflows,
       "ctIfInBroadcastPkts": ctIfInBroadcastPkts,
       "ctIfInBroadcastPktsOverflows": ctIfInBroadcastPktsOverflows,
       "ctIfOutOctets": ctIfOutOctets,
       "ctIfOutOctetsOverflows": ctIfOutOctetsOverflows,
       "ctIfOutUcastPkts": ctIfOutUcastPkts,
       "ctIfOutUcastPktsOverflows": ctIfOutUcastPktsOverflows,
       "ctIfOutMulticastPkts": ctIfOutMulticastPkts,
       "ctIfOutMulticastPktsOverflows": ctIfOutMulticastPktsOverflows,
       "ctIfOutBroadcastPkts": ctIfOutBroadcastPkts,
       "ctIfOutBroadcastPktsOverflows": ctIfOutBroadcastPktsOverflows}
)
