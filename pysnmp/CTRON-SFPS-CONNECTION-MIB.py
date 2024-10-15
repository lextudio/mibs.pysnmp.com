# SNMP MIB module (CTRON-SFPS-CONNECTION-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CTRON-SFPS-CONNECTION-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:19:20 2024
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

(sfpsCNXPacketStats,
 sfpsConnectionAPI,
 sfpsConnectionConfigAPI,
 sfpsConnectionLookupAPI,
 sfpsConnectionQueryAPI,
 sfpsConnectionStats,
 sfpsConnectionTestAPI,
 sfpsSwitchConnections) = mibBuilder.importSymbols(
    "CTRON-SFPS-INCLUDE-MIB",
    "sfpsCNXPacketStats",
    "sfpsConnectionAPI",
    "sfpsConnectionConfigAPI",
    "sfpsConnectionLookupAPI",
    "sfpsConnectionQueryAPI",
    "sfpsConnectionStats",
    "sfpsConnectionTestAPI",
    "sfpsSwitchConnections")

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



class SfpsSwitchPort(Integer32):
    """Custom type SfpsSwitchPort based on Integer32"""




class SfpsAddress(OctetString):
    """Custom type SfpsAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SfpsConnectionTable_Object = MibTable
sfpsConnectionTable = _SfpsConnectionTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 3, 1)
)
if mibBuilder.loadTexts:
    sfpsConnectionTable.setStatus("mandatory")
_SfpsConnectionEntry_Object = MibTableRow
sfpsConnectionEntry = _SfpsConnectionEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 3, 1, 1)
)
sfpsConnectionEntry.setIndexNames(
    (0, "CTRON-SFPS-CONNECTION-MIB", "sfpsConnectionDestination"),
    (0, "CTRON-SFPS-CONNECTION-MIB", "sfpsConnectionSource"),
)
if mibBuilder.loadTexts:
    sfpsConnectionEntry.setStatus("mandatory")
_SfpsConnectionDestination_Type = SfpsAddress
_SfpsConnectionDestination_Object = MibTableColumn
sfpsConnectionDestination = _SfpsConnectionDestination_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 3, 1, 1, 1),
    _SfpsConnectionDestination_Type()
)
sfpsConnectionDestination.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsConnectionDestination.setStatus("mandatory")
_SfpsConnectionSource_Type = SfpsAddress
_SfpsConnectionSource_Object = MibTableColumn
sfpsConnectionSource = _SfpsConnectionSource_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 3, 1, 1, 2),
    _SfpsConnectionSource_Type()
)
sfpsConnectionSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsConnectionSource.setStatus("mandatory")
_SfpsConnectionPrimInPort_Type = Integer32
_SfpsConnectionPrimInPort_Object = MibTableColumn
sfpsConnectionPrimInPort = _SfpsConnectionPrimInPort_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 3, 1, 1, 3),
    _SfpsConnectionPrimInPort_Type()
)
sfpsConnectionPrimInPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsConnectionPrimInPort.setStatus("mandatory")
_SfpsConnectionPrimOutPort_Type = Integer32
_SfpsConnectionPrimOutPort_Object = MibTableColumn
sfpsConnectionPrimOutPort = _SfpsConnectionPrimOutPort_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 3, 1, 1, 4),
    _SfpsConnectionPrimOutPort_Type()
)
sfpsConnectionPrimOutPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsConnectionPrimOutPort.setStatus("mandatory")
_SfpsConnectionSecInPort_Type = Integer32
_SfpsConnectionSecInPort_Object = MibTableColumn
sfpsConnectionSecInPort = _SfpsConnectionSecInPort_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 3, 1, 1, 5),
    _SfpsConnectionSecInPort_Type()
)
sfpsConnectionSecInPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsConnectionSecInPort.setStatus("mandatory")
_SfpsConnectionSecOutPort_Type = Integer32
_SfpsConnectionSecOutPort_Object = MibTableColumn
sfpsConnectionSecOutPort = _SfpsConnectionSecOutPort_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 3, 1, 1, 6),
    _SfpsConnectionSecOutPort_Type()
)
sfpsConnectionSecOutPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsConnectionSecOutPort.setStatus("mandatory")


class _SfpsConnectionCtrlStatus_Type(Integer32):
    """Custom type sfpsConnectionCtrlStatus based on Integer32"""
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
        *(("activate", 2),
          ("delete", 3),
          ("other", 1),
          ("under-creation", 4))
    )


_SfpsConnectionCtrlStatus_Type.__name__ = "Integer32"
_SfpsConnectionCtrlStatus_Object = MibTableColumn
sfpsConnectionCtrlStatus = _SfpsConnectionCtrlStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 3, 1, 1, 7),
    _SfpsConnectionCtrlStatus_Type()
)
sfpsConnectionCtrlStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsConnectionCtrlStatus.setStatus("mandatory")


class _SfpsConnectionAdminStatus_Type(Integer32):
    """Custom type sfpsConnectionAdminStatus based on Integer32"""
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
          ("enabled", 3),
          ("other", 1))
    )


_SfpsConnectionAdminStatus_Type.__name__ = "Integer32"
_SfpsConnectionAdminStatus_Object = MibTableColumn
sfpsConnectionAdminStatus = _SfpsConnectionAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 3, 1, 1, 8),
    _SfpsConnectionAdminStatus_Type()
)
sfpsConnectionAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsConnectionAdminStatus.setStatus("mandatory")
_SfpsConnectionAge_Type = TimeTicks
_SfpsConnectionAge_Object = MibTableColumn
sfpsConnectionAge = _SfpsConnectionAge_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 3, 1, 1, 9),
    _SfpsConnectionAge_Type()
)
sfpsConnectionAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsConnectionAge.setStatus("mandatory")


class _SfpsConnectionType_Type(Integer32):
    """Custom type sfpsConnectionType based on Integer32"""
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
        *(("filter", 1),
          ("mcast", 8),
          ("netport-filter", 4),
          ("provisioned", 2),
          ("self-prog-non-filter", 5),
          ("switched", 3),
          ("tap", 7),
          ("vlan", 6))
    )


_SfpsConnectionType_Type.__name__ = "Integer32"
_SfpsConnectionType_Object = MibTableColumn
sfpsConnectionType = _SfpsConnectionType_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 3, 1, 1, 10),
    _SfpsConnectionType_Type()
)
sfpsConnectionType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsConnectionType.setStatus("mandatory")
_SfpsConnectionPkts_Type = Counter32
_SfpsConnectionPkts_Object = MibTableColumn
sfpsConnectionPkts = _SfpsConnectionPkts_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 3, 1, 1, 11),
    _SfpsConnectionPkts_Type()
)
sfpsConnectionPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsConnectionPkts.setStatus("mandatory")
_SfpsConnectionBytes_Type = Counter32
_SfpsConnectionBytes_Object = MibTableColumn
sfpsConnectionBytes = _SfpsConnectionBytes_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 3, 1, 1, 12),
    _SfpsConnectionBytes_Type()
)
sfpsConnectionBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsConnectionBytes.setStatus("mandatory")
_SfpsConnectionCanAge_Type = Integer32
_SfpsConnectionCanAge_Object = MibTableColumn
sfpsConnectionCanAge = _SfpsConnectionCanAge_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 3, 1, 1, 13),
    _SfpsConnectionCanAge_Type()
)
sfpsConnectionCanAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsConnectionCanAge.setStatus("mandatory")
_SfpsConnectionPrimOutPorts_Type = DisplayString
_SfpsConnectionPrimOutPorts_Object = MibTableColumn
sfpsConnectionPrimOutPorts = _SfpsConnectionPrimOutPorts_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 3, 1, 1, 14),
    _SfpsConnectionPrimOutPorts_Type()
)
sfpsConnectionPrimOutPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsConnectionPrimOutPorts.setStatus("mandatory")
_SfpsConnectionSecOutPorts_Type = DisplayString
_SfpsConnectionSecOutPorts_Object = MibTableColumn
sfpsConnectionSecOutPorts = _SfpsConnectionSecOutPorts_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 3, 1, 1, 15),
    _SfpsConnectionSecOutPorts_Type()
)
sfpsConnectionSecOutPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsConnectionSecOutPorts.setStatus("mandatory")


class _SfpsConnectionLookupAPIVerb_Type(Integer32):
    """Custom type sfpsConnectionLookupAPIVerb based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("getEntry", 1)
    )


_SfpsConnectionLookupAPIVerb_Type.__name__ = "Integer32"
_SfpsConnectionLookupAPIVerb_Object = MibScalar
sfpsConnectionLookupAPIVerb = _SfpsConnectionLookupAPIVerb_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 3, 2, 1),
    _SfpsConnectionLookupAPIVerb_Type()
)
sfpsConnectionLookupAPIVerb.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsConnectionLookupAPIVerb.setStatus("mandatory")
_SfpsConnectionLookupAPIMacAddr_Type = SfpsAddress
_SfpsConnectionLookupAPIMacAddr_Object = MibScalar
sfpsConnectionLookupAPIMacAddr = _SfpsConnectionLookupAPIMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 3, 2, 2),
    _SfpsConnectionLookupAPIMacAddr_Type()
)
sfpsConnectionLookupAPIMacAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsConnectionLookupAPIMacAddr.setStatus("mandatory")
_SfpsConnectionLookupAPIDestAddr_Type = SfpsAddress
_SfpsConnectionLookupAPIDestAddr_Object = MibScalar
sfpsConnectionLookupAPIDestAddr = _SfpsConnectionLookupAPIDestAddr_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 3, 2, 3),
    _SfpsConnectionLookupAPIDestAddr_Type()
)
sfpsConnectionLookupAPIDestAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsConnectionLookupAPIDestAddr.setStatus("mandatory")
_SfpsConnectionLookupAPISourceAddr_Type = SfpsAddress
_SfpsConnectionLookupAPISourceAddr_Object = MibScalar
sfpsConnectionLookupAPISourceAddr = _SfpsConnectionLookupAPISourceAddr_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 3, 2, 4),
    _SfpsConnectionLookupAPISourceAddr_Type()
)
sfpsConnectionLookupAPISourceAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsConnectionLookupAPISourceAddr.setStatus("mandatory")
_SfpsConnectionLookupAPIPrimInPort_Type = Integer32
_SfpsConnectionLookupAPIPrimInPort_Object = MibScalar
sfpsConnectionLookupAPIPrimInPort = _SfpsConnectionLookupAPIPrimInPort_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 3, 2, 5),
    _SfpsConnectionLookupAPIPrimInPort_Type()
)
sfpsConnectionLookupAPIPrimInPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsConnectionLookupAPIPrimInPort.setStatus("mandatory")
_SfpsConnectionLookupAPIPrimOutPort_Type = Integer32
_SfpsConnectionLookupAPIPrimOutPort_Object = MibScalar
sfpsConnectionLookupAPIPrimOutPort = _SfpsConnectionLookupAPIPrimOutPort_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 3, 2, 6),
    _SfpsConnectionLookupAPIPrimOutPort_Type()
)
sfpsConnectionLookupAPIPrimOutPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsConnectionLookupAPIPrimOutPort.setStatus("mandatory")
_SfpsConnectionLookupAPISecInPort_Type = Integer32
_SfpsConnectionLookupAPISecInPort_Object = MibScalar
sfpsConnectionLookupAPISecInPort = _SfpsConnectionLookupAPISecInPort_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 3, 2, 7),
    _SfpsConnectionLookupAPISecInPort_Type()
)
sfpsConnectionLookupAPISecInPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsConnectionLookupAPISecInPort.setStatus("mandatory")
_SfpsConnectionLookupAPISecOutPort_Type = Integer32
_SfpsConnectionLookupAPISecOutPort_Object = MibScalar
sfpsConnectionLookupAPISecOutPort = _SfpsConnectionLookupAPISecOutPort_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 3, 2, 8),
    _SfpsConnectionLookupAPISecOutPort_Type()
)
sfpsConnectionLookupAPISecOutPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsConnectionLookupAPISecOutPort.setStatus("mandatory")


class _SfpsConnectionLookupAPICtrlStatus_Type(Integer32):
    """Custom type sfpsConnectionLookupAPICtrlStatus based on Integer32"""
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
        *(("activate", 2),
          ("delete", 3),
          ("other", 1),
          ("under-creation", 4))
    )


_SfpsConnectionLookupAPICtrlStatus_Type.__name__ = "Integer32"
_SfpsConnectionLookupAPICtrlStatus_Object = MibScalar
sfpsConnectionLookupAPICtrlStatus = _SfpsConnectionLookupAPICtrlStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 3, 2, 9),
    _SfpsConnectionLookupAPICtrlStatus_Type()
)
sfpsConnectionLookupAPICtrlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsConnectionLookupAPICtrlStatus.setStatus("mandatory")


class _SfpsConnectionLookupAPIAdminStatus_Type(Integer32):
    """Custom type sfpsConnectionLookupAPIAdminStatus based on Integer32"""
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
          ("enabled", 3),
          ("other", 1))
    )


_SfpsConnectionLookupAPIAdminStatus_Type.__name__ = "Integer32"
_SfpsConnectionLookupAPIAdminStatus_Object = MibScalar
sfpsConnectionLookupAPIAdminStatus = _SfpsConnectionLookupAPIAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 3, 2, 10),
    _SfpsConnectionLookupAPIAdminStatus_Type()
)
sfpsConnectionLookupAPIAdminStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsConnectionLookupAPIAdminStatus.setStatus("mandatory")
_SfpsConnectionLookupAPIAge_Type = TimeTicks
_SfpsConnectionLookupAPIAge_Object = MibScalar
sfpsConnectionLookupAPIAge = _SfpsConnectionLookupAPIAge_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 3, 2, 11),
    _SfpsConnectionLookupAPIAge_Type()
)
sfpsConnectionLookupAPIAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsConnectionLookupAPIAge.setStatus("mandatory")


class _SfpsConnectionLookupAPIType_Type(Integer32):
    """Custom type sfpsConnectionLookupAPIType based on Integer32"""
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
        *(("flood", 9),
          ("mcast", 8),
          ("other", 1),
          ("provisioned", 2),
          ("self-prog-filter", 4),
          ("self-prog-non-filter", 5),
          ("switched", 3),
          ("tap", 7),
          ("vlan", 6))
    )


_SfpsConnectionLookupAPIType_Type.__name__ = "Integer32"
_SfpsConnectionLookupAPIType_Object = MibScalar
sfpsConnectionLookupAPIType = _SfpsConnectionLookupAPIType_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 3, 2, 12),
    _SfpsConnectionLookupAPIType_Type()
)
sfpsConnectionLookupAPIType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsConnectionLookupAPIType.setStatus("mandatory")
_SfpsConnectionLookupAPIPkts_Type = Integer32
_SfpsConnectionLookupAPIPkts_Object = MibScalar
sfpsConnectionLookupAPIPkts = _SfpsConnectionLookupAPIPkts_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 3, 2, 13),
    _SfpsConnectionLookupAPIPkts_Type()
)
sfpsConnectionLookupAPIPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsConnectionLookupAPIPkts.setStatus("mandatory")
_SfpsConnectionLookupAPIBytes_Type = Integer32
_SfpsConnectionLookupAPIBytes_Object = MibScalar
sfpsConnectionLookupAPIBytes = _SfpsConnectionLookupAPIBytes_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 3, 2, 14),
    _SfpsConnectionLookupAPIBytes_Type()
)
sfpsConnectionLookupAPIBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsConnectionLookupAPIBytes.setStatus("mandatory")
_SfpsConnectionLookupAPICanAge_Type = Integer32
_SfpsConnectionLookupAPICanAge_Object = MibScalar
sfpsConnectionLookupAPICanAge = _SfpsConnectionLookupAPICanAge_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 3, 2, 15),
    _SfpsConnectionLookupAPICanAge_Type()
)
sfpsConnectionLookupAPICanAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsConnectionLookupAPICanAge.setStatus("mandatory")
_SfpsConnectionLookupAPIPrimOutPorts_Type = DisplayString
_SfpsConnectionLookupAPIPrimOutPorts_Object = MibScalar
sfpsConnectionLookupAPIPrimOutPorts = _SfpsConnectionLookupAPIPrimOutPorts_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 3, 2, 16),
    _SfpsConnectionLookupAPIPrimOutPorts_Type()
)
sfpsConnectionLookupAPIPrimOutPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsConnectionLookupAPIPrimOutPorts.setStatus("mandatory")
_SfpsConnectionLookupAPISecOutPorts_Type = DisplayString
_SfpsConnectionLookupAPISecOutPorts_Object = MibScalar
sfpsConnectionLookupAPISecOutPorts = _SfpsConnectionLookupAPISecOutPorts_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 3, 2, 17),
    _SfpsConnectionLookupAPISecOutPorts_Type()
)
sfpsConnectionLookupAPISecOutPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsConnectionLookupAPISecOutPorts.setStatus("mandatory")


class _SfpsConnectionConfigAPIVerb_Type(Integer32):
    """Custom type sfpsConnectionConfigAPIVerb based on Integer32"""
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
        *(("ageFilters", 4),
          ("ageFull", 2),
          ("agePartial", 1),
          ("setParameter", 3),
          ("stopAging", 5))
    )


_SfpsConnectionConfigAPIVerb_Type.__name__ = "Integer32"
_SfpsConnectionConfigAPIVerb_Object = MibScalar
sfpsConnectionConfigAPIVerb = _SfpsConnectionConfigAPIVerb_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 3, 3, 1),
    _SfpsConnectionConfigAPIVerb_Type()
)
sfpsConnectionConfigAPIVerb.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsConnectionConfigAPIVerb.setStatus("mandatory")


class _SfpsConnectionConfigAPICnxHiMark_Type(Integer32):
    """Custom type sfpsConnectionConfigAPICnxHiMark based on Integer32"""
    defaultValue = 95


_SfpsConnectionConfigAPICnxHiMark_Object = MibScalar
sfpsConnectionConfigAPICnxHiMark = _SfpsConnectionConfigAPICnxHiMark_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 3, 3, 2),
    _SfpsConnectionConfigAPICnxHiMark_Type()
)
sfpsConnectionConfigAPICnxHiMark.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsConnectionConfigAPICnxHiMark.setStatus("mandatory")


class _SfpsConnectionConfigAPICnxNumToAge_Type(Integer32):
    """Custom type sfpsConnectionConfigAPICnxNumToAge based on Integer32"""
    defaultValue = 100


_SfpsConnectionConfigAPICnxNumToAge_Object = MibScalar
sfpsConnectionConfigAPICnxNumToAge = _SfpsConnectionConfigAPICnxNumToAge_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 3, 3, 3),
    _SfpsConnectionConfigAPICnxNumToAge_Type()
)
sfpsConnectionConfigAPICnxNumToAge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsConnectionConfigAPICnxNumToAge.setStatus("mandatory")


class _SfpsConnectionConfigAPIAgePeriod_Type(Integer32):
    """Custom type sfpsConnectionConfigAPIAgePeriod based on Integer32"""
    defaultValue = 0


_SfpsConnectionConfigAPIAgePeriod_Object = MibScalar
sfpsConnectionConfigAPIAgePeriod = _SfpsConnectionConfigAPIAgePeriod_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 3, 3, 4),
    _SfpsConnectionConfigAPIAgePeriod_Type()
)
sfpsConnectionConfigAPIAgePeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsConnectionConfigAPIAgePeriod.setStatus("mandatory")
_SfpsConnectionConfigAPIAgePassInProgress_Type = Integer32
_SfpsConnectionConfigAPIAgePassInProgress_Object = MibScalar
sfpsConnectionConfigAPIAgePassInProgress = _SfpsConnectionConfigAPIAgePassInProgress_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 3, 3, 5),
    _SfpsConnectionConfigAPIAgePassInProgress_Type()
)
sfpsConnectionConfigAPIAgePassInProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsConnectionConfigAPIAgePassInProgress.setStatus("mandatory")
_SfpsConnectionConfigAPICurCapacity_Type = Integer32
_SfpsConnectionConfigAPICurCapacity_Object = MibScalar
sfpsConnectionConfigAPICurCapacity = _SfpsConnectionConfigAPICurCapacity_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 3, 3, 6),
    _SfpsConnectionConfigAPICurCapacity_Type()
)
sfpsConnectionConfigAPICurCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsConnectionConfigAPICurCapacity.setStatus("mandatory")
_SfpsConnectionConfigAPILastPassTime_Type = TimeTicks
_SfpsConnectionConfigAPILastPassTime_Object = MibScalar
sfpsConnectionConfigAPILastPassTime = _SfpsConnectionConfigAPILastPassTime_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 3, 3, 7),
    _SfpsConnectionConfigAPILastPassTime_Type()
)
sfpsConnectionConfigAPILastPassTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsConnectionConfigAPILastPassTime.setStatus("mandatory")
_SfpsConnectionConfigAPITimeSinceLastPass_Type = TimeTicks
_SfpsConnectionConfigAPITimeSinceLastPass_Object = MibScalar
sfpsConnectionConfigAPITimeSinceLastPass = _SfpsConnectionConfigAPITimeSinceLastPass_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 3, 3, 8),
    _SfpsConnectionConfigAPITimeSinceLastPass_Type()
)
sfpsConnectionConfigAPITimeSinceLastPass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsConnectionConfigAPITimeSinceLastPass.setStatus("mandatory")
_SfpsConnectionConfigAPIAgePassDelta_Type = TimeTicks
_SfpsConnectionConfigAPIAgePassDelta_Object = MibScalar
sfpsConnectionConfigAPIAgePassDelta = _SfpsConnectionConfigAPIAgePassDelta_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 3, 3, 9),
    _SfpsConnectionConfigAPIAgePassDelta_Type()
)
sfpsConnectionConfigAPIAgePassDelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsConnectionConfigAPIAgePassDelta.setStatus("mandatory")
_SfpsConnectionConfigAPIAgePassCount_Type = Integer32
_SfpsConnectionConfigAPIAgePassCount_Object = MibScalar
sfpsConnectionConfigAPIAgePassCount = _SfpsConnectionConfigAPIAgePassCount_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 3, 3, 10),
    _SfpsConnectionConfigAPIAgePassCount_Type()
)
sfpsConnectionConfigAPIAgePassCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsConnectionConfigAPIAgePassCount.setStatus("mandatory")
_SfpsConnectionConfigAPIAgeStatsHiMark_Type = Integer32
_SfpsConnectionConfigAPIAgeStatsHiMark_Object = MibScalar
sfpsConnectionConfigAPIAgeStatsHiMark = _SfpsConnectionConfigAPIAgeStatsHiMark_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 3, 3, 11),
    _SfpsConnectionConfigAPIAgeStatsHiMark_Type()
)
sfpsConnectionConfigAPIAgeStatsHiMark.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsConnectionConfigAPIAgeStatsHiMark.setStatus("mandatory")
_SfpsConnectionConfigAPIStatsAgingEnable_Type = Integer32
_SfpsConnectionConfigAPIStatsAgingEnable_Object = MibScalar
sfpsConnectionConfigAPIStatsAgingEnable = _SfpsConnectionConfigAPIStatsAgingEnable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 3, 3, 12),
    _SfpsConnectionConfigAPIStatsAgingEnable_Type()
)
sfpsConnectionConfigAPIStatsAgingEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsConnectionConfigAPIStatsAgingEnable.setStatus("mandatory")
_SfpsConnectionConfigAPIAgeStatsAgingSupported_Type = Integer32
_SfpsConnectionConfigAPIAgeStatsAgingSupported_Object = MibScalar
sfpsConnectionConfigAPIAgeStatsAgingSupported = _SfpsConnectionConfigAPIAgeStatsAgingSupported_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 3, 3, 13),
    _SfpsConnectionConfigAPIAgeStatsAgingSupported_Type()
)
sfpsConnectionConfigAPIAgeStatsAgingSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsConnectionConfigAPIAgeStatsAgingSupported.setStatus("mandatory")
_SfpsConnectionConfigAPIIdleCnxs_Type = Integer32
_SfpsConnectionConfigAPIIdleCnxs_Object = MibScalar
sfpsConnectionConfigAPIIdleCnxs = _SfpsConnectionConfigAPIIdleCnxs_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 3, 3, 14),
    _SfpsConnectionConfigAPIIdleCnxs_Type()
)
sfpsConnectionConfigAPIIdleCnxs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsConnectionConfigAPIIdleCnxs.setStatus("mandatory")
_SfpsConnectionConfigAPIActiveCnxs_Type = Integer32
_SfpsConnectionConfigAPIActiveCnxs_Object = MibScalar
sfpsConnectionConfigAPIActiveCnxs = _SfpsConnectionConfigAPIActiveCnxs_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 3, 3, 15),
    _SfpsConnectionConfigAPIActiveCnxs_Type()
)
sfpsConnectionConfigAPIActiveCnxs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsConnectionConfigAPIActiveCnxs.setStatus("mandatory")
_SfpsConnectionStatsMaxCnxs_Type = Integer32
_SfpsConnectionStatsMaxCnxs_Object = MibScalar
sfpsConnectionStatsMaxCnxs = _SfpsConnectionStatsMaxCnxs_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 3, 4, 1),
    _SfpsConnectionStatsMaxCnxs_Type()
)
sfpsConnectionStatsMaxCnxs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsConnectionStatsMaxCnxs.setStatus("mandatory")
_SfpsConnectionStatsTotalCnxs_Type = Integer32
_SfpsConnectionStatsTotalCnxs_Object = MibScalar
sfpsConnectionStatsTotalCnxs = _SfpsConnectionStatsTotalCnxs_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 3, 4, 2),
    _SfpsConnectionStatsTotalCnxs_Type()
)
sfpsConnectionStatsTotalCnxs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsConnectionStatsTotalCnxs.setStatus("mandatory")
_SfpsConnectionStatsSwitchedCnxs_Type = Integer32
_SfpsConnectionStatsSwitchedCnxs_Object = MibScalar
sfpsConnectionStatsSwitchedCnxs = _SfpsConnectionStatsSwitchedCnxs_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 3, 4, 3),
    _SfpsConnectionStatsSwitchedCnxs_Type()
)
sfpsConnectionStatsSwitchedCnxs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsConnectionStatsSwitchedCnxs.setStatus("mandatory")
_SfpsConnectionStatsVlanCnxs_Type = Integer32
_SfpsConnectionStatsVlanCnxs_Object = MibScalar
sfpsConnectionStatsVlanCnxs = _SfpsConnectionStatsVlanCnxs_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 3, 4, 4),
    _SfpsConnectionStatsVlanCnxs_Type()
)
sfpsConnectionStatsVlanCnxs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsConnectionStatsVlanCnxs.setStatus("mandatory")
_SfpsConnectionStatsFilterCnxs_Type = Integer32
_SfpsConnectionStatsFilterCnxs_Object = MibScalar
sfpsConnectionStatsFilterCnxs = _SfpsConnectionStatsFilterCnxs_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 3, 4, 5),
    _SfpsConnectionStatsFilterCnxs_Type()
)
sfpsConnectionStatsFilterCnxs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsConnectionStatsFilterCnxs.setStatus("mandatory")
_SfpsConnectionStatsSelfProgCnxs_Type = Integer32
_SfpsConnectionStatsSelfProgCnxs_Object = MibScalar
sfpsConnectionStatsSelfProgCnxs = _SfpsConnectionStatsSelfProgCnxs_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 3, 4, 6),
    _SfpsConnectionStatsSelfProgCnxs_Type()
)
sfpsConnectionStatsSelfProgCnxs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsConnectionStatsSelfProgCnxs.setStatus("mandatory")
_SfpsConnectionStatsProvsnedCnxs_Type = Integer32
_SfpsConnectionStatsProvsnedCnxs_Object = MibScalar
sfpsConnectionStatsProvsnedCnxs = _SfpsConnectionStatsProvsnedCnxs_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 3, 4, 7),
    _SfpsConnectionStatsProvsnedCnxs_Type()
)
sfpsConnectionStatsProvsnedCnxs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsConnectionStatsProvsnedCnxs.setStatus("mandatory")
_SfpsConnectionStatsTapCnxs_Type = Integer32
_SfpsConnectionStatsTapCnxs_Object = MibScalar
sfpsConnectionStatsTapCnxs = _SfpsConnectionStatsTapCnxs_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 3, 4, 8),
    _SfpsConnectionStatsTapCnxs_Type()
)
sfpsConnectionStatsTapCnxs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsConnectionStatsTapCnxs.setStatus("mandatory")
_SfpsConnectionStatsMcastCnxs_Type = Integer32
_SfpsConnectionStatsMcastCnxs_Object = MibScalar
sfpsConnectionStatsMcastCnxs = _SfpsConnectionStatsMcastCnxs_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 3, 4, 9),
    _SfpsConnectionStatsMcastCnxs_Type()
)
sfpsConnectionStatsMcastCnxs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsConnectionStatsMcastCnxs.setStatus("mandatory")
_SfpsConnectionStatsNetPortFilterCnxs_Type = Integer32
_SfpsConnectionStatsNetPortFilterCnxs_Object = MibScalar
sfpsConnectionStatsNetPortFilterCnxs = _SfpsConnectionStatsNetPortFilterCnxs_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 3, 4, 10),
    _SfpsConnectionStatsNetPortFilterCnxs_Type()
)
sfpsConnectionStatsNetPortFilterCnxs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsConnectionStatsNetPortFilterCnxs.setStatus("mandatory")
_SfpsConnectionStatsNonCriticalVlans_Type = Integer32
_SfpsConnectionStatsNonCriticalVlans_Object = MibScalar
sfpsConnectionStatsNonCriticalVlans = _SfpsConnectionStatsNonCriticalVlans_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 3, 4, 11),
    _SfpsConnectionStatsNonCriticalVlans_Type()
)
sfpsConnectionStatsNonCriticalVlans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsConnectionStatsNonCriticalVlans.setStatus("mandatory")
_SfpsConnectionStatsAddErrors_Type = Integer32
_SfpsConnectionStatsAddErrors_Object = MibScalar
sfpsConnectionStatsAddErrors = _SfpsConnectionStatsAddErrors_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 3, 4, 12),
    _SfpsConnectionStatsAddErrors_Type()
)
sfpsConnectionStatsAddErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsConnectionStatsAddErrors.setStatus("mandatory")
_SfpsConnectionStatsDeleteErrors_Type = Integer32
_SfpsConnectionStatsDeleteErrors_Object = MibScalar
sfpsConnectionStatsDeleteErrors = _SfpsConnectionStatsDeleteErrors_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 3, 4, 13),
    _SfpsConnectionStatsDeleteErrors_Type()
)
sfpsConnectionStatsDeleteErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsConnectionStatsDeleteErrors.setStatus("mandatory")


class _SfpsConnectionQueryAPIVerb_Type(Integer32):
    """Custom type sfpsConnectionQueryAPIVerb based on Integer32"""
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
        *(("add", 2),
          ("delete", 3),
          ("lookup", 1),
          ("mapPort", 4),
          ("mapPorts", 7),
          ("reapCnxsGivenMac", 6),
          ("unMapPorts", 8),
          ("unmapPort", 5))
    )


_SfpsConnectionQueryAPIVerb_Type.__name__ = "Integer32"
_SfpsConnectionQueryAPIVerb_Object = MibScalar
sfpsConnectionQueryAPIVerb = _SfpsConnectionQueryAPIVerb_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 3, 5, 1),
    _SfpsConnectionQueryAPIVerb_Type()
)
sfpsConnectionQueryAPIVerb.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsConnectionQueryAPIVerb.setStatus("mandatory")
_SfpsConnectionQueryAPIDestAddr_Type = SfpsAddress
_SfpsConnectionQueryAPIDestAddr_Object = MibScalar
sfpsConnectionQueryAPIDestAddr = _SfpsConnectionQueryAPIDestAddr_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 3, 5, 2),
    _SfpsConnectionQueryAPIDestAddr_Type()
)
sfpsConnectionQueryAPIDestAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsConnectionQueryAPIDestAddr.setStatus("mandatory")
_SfpsConnectionQueryAPISourceAddr_Type = SfpsAddress
_SfpsConnectionQueryAPISourceAddr_Object = MibScalar
sfpsConnectionQueryAPISourceAddr = _SfpsConnectionQueryAPISourceAddr_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 3, 5, 3),
    _SfpsConnectionQueryAPISourceAddr_Type()
)
sfpsConnectionQueryAPISourceAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsConnectionQueryAPISourceAddr.setStatus("mandatory")
_SfpsConnectionQueryAPIInPort_Type = Integer32
_SfpsConnectionQueryAPIInPort_Object = MibScalar
sfpsConnectionQueryAPIInPort = _SfpsConnectionQueryAPIInPort_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 3, 5, 4),
    _SfpsConnectionQueryAPIInPort_Type()
)
sfpsConnectionQueryAPIInPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsConnectionQueryAPIInPort.setStatus("mandatory")
_SfpsConnectionQueryAPIOutPort_Type = Integer32
_SfpsConnectionQueryAPIOutPort_Object = MibScalar
sfpsConnectionQueryAPIOutPort = _SfpsConnectionQueryAPIOutPort_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 3, 5, 5),
    _SfpsConnectionQueryAPIOutPort_Type()
)
sfpsConnectionQueryAPIOutPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsConnectionQueryAPIOutPort.setStatus("mandatory")


class _SfpsConnectionQueryAPICtrlStatus_Type(Integer32):
    """Custom type sfpsConnectionQueryAPICtrlStatus based on Integer32"""
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
        *(("activate", 2),
          ("delete", 3),
          ("other", 1),
          ("under-creation", 4))
    )


_SfpsConnectionQueryAPICtrlStatus_Type.__name__ = "Integer32"
_SfpsConnectionQueryAPICtrlStatus_Object = MibScalar
sfpsConnectionQueryAPICtrlStatus = _SfpsConnectionQueryAPICtrlStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 3, 5, 6),
    _SfpsConnectionQueryAPICtrlStatus_Type()
)
sfpsConnectionQueryAPICtrlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsConnectionQueryAPICtrlStatus.setStatus("mandatory")


class _SfpsConnectionQueryAPIAdminStatus_Type(Integer32):
    """Custom type sfpsConnectionQueryAPIAdminStatus based on Integer32"""
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
          ("enabled", 3),
          ("other", 1))
    )


_SfpsConnectionQueryAPIAdminStatus_Type.__name__ = "Integer32"
_SfpsConnectionQueryAPIAdminStatus_Object = MibScalar
sfpsConnectionQueryAPIAdminStatus = _SfpsConnectionQueryAPIAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 3, 5, 7),
    _SfpsConnectionQueryAPIAdminStatus_Type()
)
sfpsConnectionQueryAPIAdminStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsConnectionQueryAPIAdminStatus.setStatus("mandatory")
_SfpsConnectionQueryAPIAge_Type = Integer32
_SfpsConnectionQueryAPIAge_Object = MibScalar
sfpsConnectionQueryAPIAge = _SfpsConnectionQueryAPIAge_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 3, 5, 8),
    _SfpsConnectionQueryAPIAge_Type()
)
sfpsConnectionQueryAPIAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsConnectionQueryAPIAge.setStatus("mandatory")


class _SfpsConnectionQueryAPIQueryType_Type(Integer32):
    """Custom type sfpsConnectionQueryAPIQueryType based on Integer32"""
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
        *(("filter", 1),
          ("mcast", 8),
          ("netport-filter", 4),
          ("provisioned", 2),
          ("self-prog-non-filter", 5),
          ("switched", 3),
          ("tap", 7),
          ("vlan", 6))
    )


_SfpsConnectionQueryAPIQueryType_Type.__name__ = "Integer32"
_SfpsConnectionQueryAPIQueryType_Object = MibScalar
sfpsConnectionQueryAPIQueryType = _SfpsConnectionQueryAPIQueryType_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 3, 5, 9),
    _SfpsConnectionQueryAPIQueryType_Type()
)
sfpsConnectionQueryAPIQueryType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsConnectionQueryAPIQueryType.setStatus("mandatory")
_SfpsConnectionQueryAPIOwner_Type = Integer32
_SfpsConnectionQueryAPIOwner_Object = MibScalar
sfpsConnectionQueryAPIOwner = _SfpsConnectionQueryAPIOwner_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 3, 5, 10),
    _SfpsConnectionQueryAPIOwner_Type()
)
sfpsConnectionQueryAPIOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsConnectionQueryAPIOwner.setStatus("mandatory")
_SfpsConnectionQueryAPIPkts_Type = Counter32
_SfpsConnectionQueryAPIPkts_Object = MibScalar
sfpsConnectionQueryAPIPkts = _SfpsConnectionQueryAPIPkts_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 3, 5, 11),
    _SfpsConnectionQueryAPIPkts_Type()
)
sfpsConnectionQueryAPIPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsConnectionQueryAPIPkts.setStatus("mandatory")
_SfpsConnectionQueryAPIBytes_Type = Counter32
_SfpsConnectionQueryAPIBytes_Object = MibScalar
sfpsConnectionQueryAPIBytes = _SfpsConnectionQueryAPIBytes_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 3, 5, 12),
    _SfpsConnectionQueryAPIBytes_Type()
)
sfpsConnectionQueryAPIBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsConnectionQueryAPIBytes.setStatus("mandatory")
_SfpsConnectionQueryAPICanAge_Type = Integer32
_SfpsConnectionQueryAPICanAge_Object = MibScalar
sfpsConnectionQueryAPICanAge = _SfpsConnectionQueryAPICanAge_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 3, 5, 13),
    _SfpsConnectionQueryAPICanAge_Type()
)
sfpsConnectionQueryAPICanAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsConnectionQueryAPICanAge.setStatus("mandatory")
_SfpsConnectionQueryAPIOutPorts_Type = DisplayString
_SfpsConnectionQueryAPIOutPorts_Object = MibScalar
sfpsConnectionQueryAPIOutPorts = _SfpsConnectionQueryAPIOutPorts_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 3, 5, 14),
    _SfpsConnectionQueryAPIOutPorts_Type()
)
sfpsConnectionQueryAPIOutPorts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsConnectionQueryAPIOutPorts.setStatus("mandatory")
_SfpsConnectionQueryAPIMacAddr_Type = SfpsAddress
_SfpsConnectionQueryAPIMacAddr_Object = MibScalar
sfpsConnectionQueryAPIMacAddr = _SfpsConnectionQueryAPIMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 3, 5, 15),
    _SfpsConnectionQueryAPIMacAddr_Type()
)
sfpsConnectionQueryAPIMacAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsConnectionQueryAPIMacAddr.setStatus("mandatory")
_SfpsConnectionQueryAPISecInPort_Type = Integer32
_SfpsConnectionQueryAPISecInPort_Object = MibScalar
sfpsConnectionQueryAPISecInPort = _SfpsConnectionQueryAPISecInPort_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 3, 5, 16),
    _SfpsConnectionQueryAPISecInPort_Type()
)
sfpsConnectionQueryAPISecInPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsConnectionQueryAPISecInPort.setStatus("mandatory")
_SfpsConnectionQueryAPISecOutPort_Type = Integer32
_SfpsConnectionQueryAPISecOutPort_Object = MibScalar
sfpsConnectionQueryAPISecOutPort = _SfpsConnectionQueryAPISecOutPort_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 3, 5, 17),
    _SfpsConnectionQueryAPISecOutPort_Type()
)
sfpsConnectionQueryAPISecOutPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsConnectionQueryAPISecOutPort.setStatus("mandatory")
_SfpsConnectionQueryAPISecOutPorts_Type = DisplayString
_SfpsConnectionQueryAPISecOutPorts_Object = MibScalar
sfpsConnectionQueryAPISecOutPorts = _SfpsConnectionQueryAPISecOutPorts_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 3, 5, 18),
    _SfpsConnectionQueryAPISecOutPorts_Type()
)
sfpsConnectionQueryAPISecOutPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsConnectionQueryAPISecOutPorts.setStatus("mandatory")


class _SfpsConnectionTestAPIVerb_Type(Integer32):
    """Custom type sfpsConnectionTestAPIVerb based on Integer32"""
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
        *(("fillTable", 1),
          ("reapAllCnxs", 2),
          ("reapCnxsGivenMac", 3),
          ("reapCnxsGivenPort", 4))
    )


_SfpsConnectionTestAPIVerb_Type.__name__ = "Integer32"
_SfpsConnectionTestAPIVerb_Object = MibScalar
sfpsConnectionTestAPIVerb = _SfpsConnectionTestAPIVerb_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 3, 6, 1),
    _SfpsConnectionTestAPIVerb_Type()
)
sfpsConnectionTestAPIVerb.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsConnectionTestAPIVerb.setStatus("mandatory")


class _SfpsConnectionTestAPIType_Type(Integer32):
    """Custom type sfpsConnectionTestAPIType based on Integer32"""
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
        *(("filter", 1),
          ("mcast", 8),
          ("netport-filter", 4),
          ("provisioned", 2),
          ("self-prog-non-filter", 5),
          ("switched", 3),
          ("tap", 7),
          ("vlan", 6))
    )


_SfpsConnectionTestAPIType_Type.__name__ = "Integer32"
_SfpsConnectionTestAPIType_Object = MibScalar
sfpsConnectionTestAPIType = _SfpsConnectionTestAPIType_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 3, 6, 2),
    _SfpsConnectionTestAPIType_Type()
)
sfpsConnectionTestAPIType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsConnectionTestAPIType.setStatus("mandatory")
_SfpsConnectionTestAPINumCnxs_Type = Integer32
_SfpsConnectionTestAPINumCnxs_Object = MibScalar
sfpsConnectionTestAPINumCnxs = _SfpsConnectionTestAPINumCnxs_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 3, 6, 3),
    _SfpsConnectionTestAPINumCnxs_Type()
)
sfpsConnectionTestAPINumCnxs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsConnectionTestAPINumCnxs.setStatus("mandatory")
_SfpsConnectionTestAPIMacAddr_Type = SfpsAddress
_SfpsConnectionTestAPIMacAddr_Object = MibScalar
sfpsConnectionTestAPIMacAddr = _SfpsConnectionTestAPIMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 3, 6, 4),
    _SfpsConnectionTestAPIMacAddr_Type()
)
sfpsConnectionTestAPIMacAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsConnectionTestAPIMacAddr.setStatus("mandatory")
_SfpsConnectionTestAPIPort_Type = Integer32
_SfpsConnectionTestAPIPort_Object = MibScalar
sfpsConnectionTestAPIPort = _SfpsConnectionTestAPIPort_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 3, 6, 5),
    _SfpsConnectionTestAPIPort_Type()
)
sfpsConnectionTestAPIPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsConnectionTestAPIPort.setStatus("mandatory")


class _SfpsAPIVerb_Type(Integer32):
    """Custom type sfpsAPIVerb based on Integer32"""
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
        *(("map", 2),
          ("other", 1),
          ("unmap", 3),
          ("unmapall", 4))
    )


_SfpsAPIVerb_Type.__name__ = "Integer32"
_SfpsAPIVerb_Object = MibScalar
sfpsAPIVerb = _SfpsAPIVerb_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 4, 1),
    _SfpsAPIVerb_Type()
)
sfpsAPIVerb.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsAPIVerb.setStatus("mandatory")
_SfpsAPIInPort_Type = SfpsSwitchPort
_SfpsAPIInPort_Object = MibScalar
sfpsAPIInPort = _SfpsAPIInPort_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 4, 2),
    _SfpsAPIInPort_Type()
)
sfpsAPIInPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsAPIInPort.setStatus("mandatory")


class _SfpsAPIInHeaderType_Type(Integer32):
    """Custom type sfpsAPIInHeaderType based on Integer32"""
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
        *(("atm-vpi-vci", 3),
          ("mac-da-sa", 2),
          ("other", 1))
    )


_SfpsAPIInHeaderType_Type.__name__ = "Integer32"
_SfpsAPIInHeaderType_Object = MibScalar
sfpsAPIInHeaderType = _SfpsAPIInHeaderType_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 4, 3),
    _SfpsAPIInHeaderType_Type()
)
sfpsAPIInHeaderType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsAPIInHeaderType.setStatus("mandatory")


class _SfpsAPIInHeaderLength_Type(Integer32):
    """Custom type sfpsAPIInHeaderLength based on Integer32"""
    defaultValue = 12

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 12),
    )


_SfpsAPIInHeaderLength_Type.__name__ = "Integer32"
_SfpsAPIInHeaderLength_Object = MibScalar
sfpsAPIInHeaderLength = _SfpsAPIInHeaderLength_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 4, 4),
    _SfpsAPIInHeaderLength_Type()
)
sfpsAPIInHeaderLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsAPIInHeaderLength.setStatus("mandatory")
_SfpsAPIInHeaderValue_Type = OctetString
_SfpsAPIInHeaderValue_Object = MibScalar
sfpsAPIInHeaderValue = _SfpsAPIInHeaderValue_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 4, 5),
    _SfpsAPIInHeaderValue_Type()
)
sfpsAPIInHeaderValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsAPIInHeaderValue.setStatus("mandatory")
_SfpsAPIOutPort_Type = SfpsSwitchPort
_SfpsAPIOutPort_Object = MibScalar
sfpsAPIOutPort = _SfpsAPIOutPort_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 4, 6),
    _SfpsAPIOutPort_Type()
)
sfpsAPIOutPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsAPIOutPort.setStatus("mandatory")


class _SfpsAPIOutHeaderType_Type(Integer32):
    """Custom type sfpsAPIOutHeaderType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("atm-vpi-vci", 3),
          ("mac-da-sa", 2),
          ("other", 1))
    )


_SfpsAPIOutHeaderType_Type.__name__ = "Integer32"
_SfpsAPIOutHeaderType_Object = MibScalar
sfpsAPIOutHeaderType = _SfpsAPIOutHeaderType_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 4, 7),
    _SfpsAPIOutHeaderType_Type()
)
sfpsAPIOutHeaderType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsAPIOutHeaderType.setStatus("mandatory")
_SfpsAPIOutHeaderLength_Type = Integer32
_SfpsAPIOutHeaderLength_Object = MibScalar
sfpsAPIOutHeaderLength = _SfpsAPIOutHeaderLength_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 4, 8),
    _SfpsAPIOutHeaderLength_Type()
)
sfpsAPIOutHeaderLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsAPIOutHeaderLength.setStatus("mandatory")
_SfpsAPIOutHeaderValue_Type = OctetString
_SfpsAPIOutHeaderValue_Object = MibScalar
sfpsAPIOutHeaderValue = _SfpsAPIOutHeaderValue_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 4, 9),
    _SfpsAPIOutHeaderValue_Type()
)
sfpsAPIOutHeaderValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsAPIOutHeaderValue.setStatus("mandatory")


class _SfpsAPIArgumentDirection_Type(Integer32):
    """Custom type sfpsAPIArgumentDirection based on Integer32"""
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
        *(("bi-directional", 2),
          ("other", 1),
          ("uni-directional", 3))
    )


_SfpsAPIArgumentDirection_Type.__name__ = "Integer32"
_SfpsAPIArgumentDirection_Object = MibScalar
sfpsAPIArgumentDirection = _SfpsAPIArgumentDirection_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 4, 10),
    _SfpsAPIArgumentDirection_Type()
)
sfpsAPIArgumentDirection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsAPIArgumentDirection.setStatus("mandatory")


class _SfpsAPIArgumentOwner_Type(Integer32):
    """Custom type sfpsAPIArgumentOwner based on Integer32"""
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
        *(("dont-own-the-call", 3),
          ("other", 1),
          ("own-the-call", 2))
    )


_SfpsAPIArgumentOwner_Type.__name__ = "Integer32"
_SfpsAPIArgumentOwner_Object = MibScalar
sfpsAPIArgumentOwner = _SfpsAPIArgumentOwner_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 4, 11),
    _SfpsAPIArgumentOwner_Type()
)
sfpsAPIArgumentOwner.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsAPIArgumentOwner.setStatus("mandatory")


class _SfpsAPIArgumentPriority_Type(Integer32):
    """Custom type sfpsAPIArgumentPriority based on Integer32"""
    defaultValue = 1

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
        *(("other", 1),
          ("priority-1", 2),
          ("priority-2", 3),
          ("priority-3", 4),
          ("priority-4", 5),
          ("priority-5", 6))
    )


_SfpsAPIArgumentPriority_Type.__name__ = "Integer32"
_SfpsAPIArgumentPriority_Object = MibScalar
sfpsAPIArgumentPriority = _SfpsAPIArgumentPriority_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 4, 12),
    _SfpsAPIArgumentPriority_Type()
)
sfpsAPIArgumentPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsAPIArgumentPriority.setStatus("mandatory")


class _SfpsAPIType_Type(Integer32):
    """Custom type sfpsAPIType based on Integer32"""
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
        *(("filtered", 3),
          ("other", 1),
          ("provisioned", 4),
          ("switched", 2))
    )


_SfpsAPIType_Type.__name__ = "Integer32"
_SfpsAPIType_Object = MibScalar
sfpsAPIType = _SfpsAPIType_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 4, 13),
    _SfpsAPIType_Type()
)
sfpsAPIType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsAPIType.setStatus("mandatory")
_SfpsCNXPacketStatsVer1Tx_Type = Integer32
_SfpsCNXPacketStatsVer1Tx_Object = MibScalar
sfpsCNXPacketStatsVer1Tx = _SfpsCNXPacketStatsVer1Tx_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 15, 1),
    _SfpsCNXPacketStatsVer1Tx_Type()
)
sfpsCNXPacketStatsVer1Tx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsCNXPacketStatsVer1Tx.setStatus("mandatory")
_SfpsCNXPacketStatsVer2Tx_Type = Integer32
_SfpsCNXPacketStatsVer2Tx_Object = MibScalar
sfpsCNXPacketStatsVer2Tx = _SfpsCNXPacketStatsVer2Tx_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 15, 2),
    _SfpsCNXPacketStatsVer2Tx_Type()
)
sfpsCNXPacketStatsVer2Tx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsCNXPacketStatsVer2Tx.setStatus("mandatory")
_SfpsCNXPacketStatsVer1Rx_Type = Integer32
_SfpsCNXPacketStatsVer1Rx_Object = MibScalar
sfpsCNXPacketStatsVer1Rx = _SfpsCNXPacketStatsVer1Rx_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 15, 3),
    _SfpsCNXPacketStatsVer1Rx_Type()
)
sfpsCNXPacketStatsVer1Rx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsCNXPacketStatsVer1Rx.setStatus("mandatory")
_SfpsCNXPacketStatsVer2Rx_Type = Integer32
_SfpsCNXPacketStatsVer2Rx_Object = MibScalar
sfpsCNXPacketStatsVer2Rx = _SfpsCNXPacketStatsVer2Rx_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 15, 4),
    _SfpsCNXPacketStatsVer2Rx_Type()
)
sfpsCNXPacketStatsVer2Rx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsCNXPacketStatsVer2Rx.setStatus("mandatory")
_SfpsCNXPacketStatsOpCode1Tx_Type = Integer32
_SfpsCNXPacketStatsOpCode1Tx_Object = MibScalar
sfpsCNXPacketStatsOpCode1Tx = _SfpsCNXPacketStatsOpCode1Tx_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 15, 5),
    _SfpsCNXPacketStatsOpCode1Tx_Type()
)
sfpsCNXPacketStatsOpCode1Tx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsCNXPacketStatsOpCode1Tx.setStatus("mandatory")
_SfpsCNXPacketStatsOpCode2Tx_Type = Integer32
_SfpsCNXPacketStatsOpCode2Tx_Object = MibScalar
sfpsCNXPacketStatsOpCode2Tx = _SfpsCNXPacketStatsOpCode2Tx_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 15, 6),
    _SfpsCNXPacketStatsOpCode2Tx_Type()
)
sfpsCNXPacketStatsOpCode2Tx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsCNXPacketStatsOpCode2Tx.setStatus("mandatory")
_SfpsCNXPacketStatsOpCode1Rx_Type = Integer32
_SfpsCNXPacketStatsOpCode1Rx_Object = MibScalar
sfpsCNXPacketStatsOpCode1Rx = _SfpsCNXPacketStatsOpCode1Rx_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 15, 7),
    _SfpsCNXPacketStatsOpCode1Rx_Type()
)
sfpsCNXPacketStatsOpCode1Rx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsCNXPacketStatsOpCode1Rx.setStatus("mandatory")
_SfpsCNXPacketStatsOpCode2Rx_Type = Integer32
_SfpsCNXPacketStatsOpCode2Rx_Object = MibScalar
sfpsCNXPacketStatsOpCode2Rx = _SfpsCNXPacketStatsOpCode2Rx_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 15, 8),
    _SfpsCNXPacketStatsOpCode2Rx_Type()
)
sfpsCNXPacketStatsOpCode2Rx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsCNXPacketStatsOpCode2Rx.setStatus("mandatory")
_SfpsCNXPacketStatsRxErrors_Type = Integer32
_SfpsCNXPacketStatsRxErrors_Object = MibScalar
sfpsCNXPacketStatsRxErrors = _SfpsCNXPacketStatsRxErrors_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 15, 9),
    _SfpsCNXPacketStatsRxErrors_Type()
)
sfpsCNXPacketStatsRxErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsCNXPacketStatsRxErrors.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CTRON-SFPS-CONNECTION-MIB",
    **{"SfpsSwitchPort": SfpsSwitchPort,
       "SfpsAddress": SfpsAddress,
       "sfpsConnectionTable": sfpsConnectionTable,
       "sfpsConnectionEntry": sfpsConnectionEntry,
       "sfpsConnectionDestination": sfpsConnectionDestination,
       "sfpsConnectionSource": sfpsConnectionSource,
       "sfpsConnectionPrimInPort": sfpsConnectionPrimInPort,
       "sfpsConnectionPrimOutPort": sfpsConnectionPrimOutPort,
       "sfpsConnectionSecInPort": sfpsConnectionSecInPort,
       "sfpsConnectionSecOutPort": sfpsConnectionSecOutPort,
       "sfpsConnectionCtrlStatus": sfpsConnectionCtrlStatus,
       "sfpsConnectionAdminStatus": sfpsConnectionAdminStatus,
       "sfpsConnectionAge": sfpsConnectionAge,
       "sfpsConnectionType": sfpsConnectionType,
       "sfpsConnectionPkts": sfpsConnectionPkts,
       "sfpsConnectionBytes": sfpsConnectionBytes,
       "sfpsConnectionCanAge": sfpsConnectionCanAge,
       "sfpsConnectionPrimOutPorts": sfpsConnectionPrimOutPorts,
       "sfpsConnectionSecOutPorts": sfpsConnectionSecOutPorts,
       "sfpsConnectionLookupAPIVerb": sfpsConnectionLookupAPIVerb,
       "sfpsConnectionLookupAPIMacAddr": sfpsConnectionLookupAPIMacAddr,
       "sfpsConnectionLookupAPIDestAddr": sfpsConnectionLookupAPIDestAddr,
       "sfpsConnectionLookupAPISourceAddr": sfpsConnectionLookupAPISourceAddr,
       "sfpsConnectionLookupAPIPrimInPort": sfpsConnectionLookupAPIPrimInPort,
       "sfpsConnectionLookupAPIPrimOutPort": sfpsConnectionLookupAPIPrimOutPort,
       "sfpsConnectionLookupAPISecInPort": sfpsConnectionLookupAPISecInPort,
       "sfpsConnectionLookupAPISecOutPort": sfpsConnectionLookupAPISecOutPort,
       "sfpsConnectionLookupAPICtrlStatus": sfpsConnectionLookupAPICtrlStatus,
       "sfpsConnectionLookupAPIAdminStatus": sfpsConnectionLookupAPIAdminStatus,
       "sfpsConnectionLookupAPIAge": sfpsConnectionLookupAPIAge,
       "sfpsConnectionLookupAPIType": sfpsConnectionLookupAPIType,
       "sfpsConnectionLookupAPIPkts": sfpsConnectionLookupAPIPkts,
       "sfpsConnectionLookupAPIBytes": sfpsConnectionLookupAPIBytes,
       "sfpsConnectionLookupAPICanAge": sfpsConnectionLookupAPICanAge,
       "sfpsConnectionLookupAPIPrimOutPorts": sfpsConnectionLookupAPIPrimOutPorts,
       "sfpsConnectionLookupAPISecOutPorts": sfpsConnectionLookupAPISecOutPorts,
       "sfpsConnectionConfigAPIVerb": sfpsConnectionConfigAPIVerb,
       "sfpsConnectionConfigAPICnxHiMark": sfpsConnectionConfigAPICnxHiMark,
       "sfpsConnectionConfigAPICnxNumToAge": sfpsConnectionConfigAPICnxNumToAge,
       "sfpsConnectionConfigAPIAgePeriod": sfpsConnectionConfigAPIAgePeriod,
       "sfpsConnectionConfigAPIAgePassInProgress": sfpsConnectionConfigAPIAgePassInProgress,
       "sfpsConnectionConfigAPICurCapacity": sfpsConnectionConfigAPICurCapacity,
       "sfpsConnectionConfigAPILastPassTime": sfpsConnectionConfigAPILastPassTime,
       "sfpsConnectionConfigAPITimeSinceLastPass": sfpsConnectionConfigAPITimeSinceLastPass,
       "sfpsConnectionConfigAPIAgePassDelta": sfpsConnectionConfigAPIAgePassDelta,
       "sfpsConnectionConfigAPIAgePassCount": sfpsConnectionConfigAPIAgePassCount,
       "sfpsConnectionConfigAPIAgeStatsHiMark": sfpsConnectionConfigAPIAgeStatsHiMark,
       "sfpsConnectionConfigAPIStatsAgingEnable": sfpsConnectionConfigAPIStatsAgingEnable,
       "sfpsConnectionConfigAPIAgeStatsAgingSupported": sfpsConnectionConfigAPIAgeStatsAgingSupported,
       "sfpsConnectionConfigAPIIdleCnxs": sfpsConnectionConfigAPIIdleCnxs,
       "sfpsConnectionConfigAPIActiveCnxs": sfpsConnectionConfigAPIActiveCnxs,
       "sfpsConnectionStatsMaxCnxs": sfpsConnectionStatsMaxCnxs,
       "sfpsConnectionStatsTotalCnxs": sfpsConnectionStatsTotalCnxs,
       "sfpsConnectionStatsSwitchedCnxs": sfpsConnectionStatsSwitchedCnxs,
       "sfpsConnectionStatsVlanCnxs": sfpsConnectionStatsVlanCnxs,
       "sfpsConnectionStatsFilterCnxs": sfpsConnectionStatsFilterCnxs,
       "sfpsConnectionStatsSelfProgCnxs": sfpsConnectionStatsSelfProgCnxs,
       "sfpsConnectionStatsProvsnedCnxs": sfpsConnectionStatsProvsnedCnxs,
       "sfpsConnectionStatsTapCnxs": sfpsConnectionStatsTapCnxs,
       "sfpsConnectionStatsMcastCnxs": sfpsConnectionStatsMcastCnxs,
       "sfpsConnectionStatsNetPortFilterCnxs": sfpsConnectionStatsNetPortFilterCnxs,
       "sfpsConnectionStatsNonCriticalVlans": sfpsConnectionStatsNonCriticalVlans,
       "sfpsConnectionStatsAddErrors": sfpsConnectionStatsAddErrors,
       "sfpsConnectionStatsDeleteErrors": sfpsConnectionStatsDeleteErrors,
       "sfpsConnectionQueryAPIVerb": sfpsConnectionQueryAPIVerb,
       "sfpsConnectionQueryAPIDestAddr": sfpsConnectionQueryAPIDestAddr,
       "sfpsConnectionQueryAPISourceAddr": sfpsConnectionQueryAPISourceAddr,
       "sfpsConnectionQueryAPIInPort": sfpsConnectionQueryAPIInPort,
       "sfpsConnectionQueryAPIOutPort": sfpsConnectionQueryAPIOutPort,
       "sfpsConnectionQueryAPICtrlStatus": sfpsConnectionQueryAPICtrlStatus,
       "sfpsConnectionQueryAPIAdminStatus": sfpsConnectionQueryAPIAdminStatus,
       "sfpsConnectionQueryAPIAge": sfpsConnectionQueryAPIAge,
       "sfpsConnectionQueryAPIQueryType": sfpsConnectionQueryAPIQueryType,
       "sfpsConnectionQueryAPIOwner": sfpsConnectionQueryAPIOwner,
       "sfpsConnectionQueryAPIPkts": sfpsConnectionQueryAPIPkts,
       "sfpsConnectionQueryAPIBytes": sfpsConnectionQueryAPIBytes,
       "sfpsConnectionQueryAPICanAge": sfpsConnectionQueryAPICanAge,
       "sfpsConnectionQueryAPIOutPorts": sfpsConnectionQueryAPIOutPorts,
       "sfpsConnectionQueryAPIMacAddr": sfpsConnectionQueryAPIMacAddr,
       "sfpsConnectionQueryAPISecInPort": sfpsConnectionQueryAPISecInPort,
       "sfpsConnectionQueryAPISecOutPort": sfpsConnectionQueryAPISecOutPort,
       "sfpsConnectionQueryAPISecOutPorts": sfpsConnectionQueryAPISecOutPorts,
       "sfpsConnectionTestAPIVerb": sfpsConnectionTestAPIVerb,
       "sfpsConnectionTestAPIType": sfpsConnectionTestAPIType,
       "sfpsConnectionTestAPINumCnxs": sfpsConnectionTestAPINumCnxs,
       "sfpsConnectionTestAPIMacAddr": sfpsConnectionTestAPIMacAddr,
       "sfpsConnectionTestAPIPort": sfpsConnectionTestAPIPort,
       "sfpsAPIVerb": sfpsAPIVerb,
       "sfpsAPIInPort": sfpsAPIInPort,
       "sfpsAPIInHeaderType": sfpsAPIInHeaderType,
       "sfpsAPIInHeaderLength": sfpsAPIInHeaderLength,
       "sfpsAPIInHeaderValue": sfpsAPIInHeaderValue,
       "sfpsAPIOutPort": sfpsAPIOutPort,
       "sfpsAPIOutHeaderType": sfpsAPIOutHeaderType,
       "sfpsAPIOutHeaderLength": sfpsAPIOutHeaderLength,
       "sfpsAPIOutHeaderValue": sfpsAPIOutHeaderValue,
       "sfpsAPIArgumentDirection": sfpsAPIArgumentDirection,
       "sfpsAPIArgumentOwner": sfpsAPIArgumentOwner,
       "sfpsAPIArgumentPriority": sfpsAPIArgumentPriority,
       "sfpsAPIType": sfpsAPIType,
       "sfpsCNXPacketStatsVer1Tx": sfpsCNXPacketStatsVer1Tx,
       "sfpsCNXPacketStatsVer2Tx": sfpsCNXPacketStatsVer2Tx,
       "sfpsCNXPacketStatsVer1Rx": sfpsCNXPacketStatsVer1Rx,
       "sfpsCNXPacketStatsVer2Rx": sfpsCNXPacketStatsVer2Rx,
       "sfpsCNXPacketStatsOpCode1Tx": sfpsCNXPacketStatsOpCode1Tx,
       "sfpsCNXPacketStatsOpCode2Tx": sfpsCNXPacketStatsOpCode2Tx,
       "sfpsCNXPacketStatsOpCode1Rx": sfpsCNXPacketStatsOpCode1Rx,
       "sfpsCNXPacketStatsOpCode2Rx": sfpsCNXPacketStatsOpCode2Rx,
       "sfpsCNXPacketStatsRxErrors": sfpsCNXPacketStatsRxErrors}
)
