# SNMP MIB module (GRPEXT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/GRPEXT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:48:53 2024
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

(grpExt,) = mibBuilder.importSymbols(
    "APENT-MIB",
    "grpExt")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

apGrpExtMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2467, 1, 17, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ApGrpTable_Object = MibTable
apGrpTable = _ApGrpTable_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 17, 2)
)
if mibBuilder.loadTexts:
    apGrpTable.setStatus("current")
_ApGrpEntry_Object = MibTableRow
apGrpEntry = _ApGrpEntry_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 17, 2, 1)
)
apGrpEntry.setIndexNames(
    (0, "GRPEXT-MIB", "apGrpName"),
)
if mibBuilder.loadTexts:
    apGrpEntry.setStatus("current")


class _ApGrpName_Type(DisplayString):
    """Custom type apGrpName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_ApGrpName_Type.__name__ = "DisplayString"
_ApGrpName_Object = MibTableColumn
apGrpName = _ApGrpName_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 17, 2, 1, 1),
    _ApGrpName_Type()
)
apGrpName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apGrpName.setStatus("current")
_ApGrpIndex_Type = Integer32
_ApGrpIndex_Object = MibTableColumn
apGrpIndex = _ApGrpIndex_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 17, 2, 1, 2),
    _ApGrpIndex_Type()
)
apGrpIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apGrpIndex.setStatus("current")
_ApGrpIPAddress_Type = IpAddress
_ApGrpIPAddress_Object = MibTableColumn
apGrpIPAddress = _ApGrpIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 17, 2, 1, 3),
    _ApGrpIPAddress_Type()
)
apGrpIPAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apGrpIPAddress.setStatus("current")


class _ApGrpIPProtocol_Type(Integer32):
    """Custom type apGrpIPProtocol based on Integer32"""
    defaultValue = 6

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(6,
              17)
        )
    )
    namedValues = NamedValues(
        *(("tcp", 6),
          ("udp", 17))
    )


_ApGrpIPProtocol_Type.__name__ = "Integer32"
_ApGrpIPProtocol_Object = MibTableColumn
apGrpIPProtocol = _ApGrpIPProtocol_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 17, 2, 1, 4),
    _ApGrpIPProtocol_Type()
)
apGrpIPProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apGrpIPProtocol.setStatus("current")


class _ApGrpPort_Type(Integer32):
    """Custom type apGrpPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ApGrpPort_Type.__name__ = "Integer32"
_ApGrpPort_Object = MibTableColumn
apGrpPort = _ApGrpPort_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 17, 2, 1, 5),
    _ApGrpPort_Type()
)
apGrpPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apGrpPort.setStatus("current")


class _ApGrpEnable_Type(Integer32):
    """Custom type apGrpEnable based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_ApGrpEnable_Type.__name__ = "Integer32"
_ApGrpEnable_Object = MibTableColumn
apGrpEnable = _ApGrpEnable_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 17, 2, 1, 6),
    _ApGrpEnable_Type()
)
apGrpEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apGrpEnable.setStatus("current")
_ApGrpStatus_Type = RowStatus
_ApGrpStatus_Object = MibTableColumn
apGrpStatus = _ApGrpStatus_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 17, 2, 1, 7),
    _ApGrpStatus_Type()
)
apGrpStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apGrpStatus.setStatus("current")


class _ApPortMapCrateBasePort_Type(Integer32):
    """Custom type apPortMapCrateBasePort based on Integer32"""
    defaultValue = 8192

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(8192, 65530),
    )


_ApPortMapCrateBasePort_Type.__name__ = "Integer32"
_ApPortMapCrateBasePort_Object = MibTableColumn
apPortMapCrateBasePort = _ApPortMapCrateBasePort_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 17, 2, 1, 8),
    _ApPortMapCrateBasePort_Type()
)
apPortMapCrateBasePort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apPortMapCrateBasePort.setStatus("current")


class _ApPortMapAvailPortsPerSfp_Type(Integer32):
    """Custom type apPortMapAvailPortsPerSfp based on Integer32"""
    defaultValue = 1024

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10000),
    )


_ApPortMapAvailPortsPerSfp_Type.__name__ = "Integer32"
_ApPortMapAvailPortsPerSfp_Object = MibTableColumn
apPortMapAvailPortsPerSfp = _ApPortMapAvailPortsPerSfp_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 17, 2, 1, 9),
    _ApPortMapAvailPortsPerSfp_Type()
)
apPortMapAvailPortsPerSfp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apPortMapAvailPortsPerSfp.setStatus("current")
_ApGrpHitCount_Type = Counter32
_ApGrpHitCount_Object = MibTableColumn
apGrpHitCount = _ApGrpHitCount_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 17, 2, 1, 10),
    _ApGrpHitCount_Type()
)
apGrpHitCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apGrpHitCount.setStatus("current")
_ApGrpByteCount_Type = Counter32
_ApGrpByteCount_Object = MibTableColumn
apGrpByteCount = _ApGrpByteCount_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 17, 2, 1, 11),
    _ApGrpByteCount_Type()
)
apGrpByteCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apGrpByteCount.setStatus("current")
_ApGrpFrameCount_Type = Counter32
_ApGrpFrameCount_Object = MibTableColumn
apGrpFrameCount = _ApGrpFrameCount_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 17, 2, 1, 12),
    _ApGrpFrameCount_Type()
)
apGrpFrameCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apGrpFrameCount.setStatus("current")
_ApGrpCurConnections_Type = Counter32
_ApGrpCurConnections_Object = MibTableColumn
apGrpCurConnections = _ApGrpCurConnections_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 17, 2, 1, 13),
    _ApGrpCurConnections_Type()
)
apGrpCurConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apGrpCurConnections.setStatus("current")
_ApGrpTotConnections_Type = Counter32
_ApGrpTotConnections_Object = MibTableColumn
apGrpTotConnections = _ApGrpTotConnections_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 17, 2, 1, 14),
    _ApGrpTotConnections_Type()
)
apGrpTotConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apGrpTotConnections.setStatus("current")
_ApGrpCurFTPControl_Type = Counter32
_ApGrpCurFTPControl_Object = MibTableColumn
apGrpCurFTPControl = _ApGrpCurFTPControl_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 17, 2, 1, 15),
    _ApGrpCurFTPControl_Type()
)
apGrpCurFTPControl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apGrpCurFTPControl.setStatus("current")
_ApGrpTotFTPControl_Type = Counter32
_ApGrpTotFTPControl_Object = MibTableColumn
apGrpTotFTPControl = _ApGrpTotFTPControl_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 17, 2, 1, 16),
    _ApGrpTotFTPControl_Type()
)
apGrpTotFTPControl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apGrpTotFTPControl.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "GRPEXT-MIB",
    **{"apGrpExtMib": apGrpExtMib,
       "apGrpTable": apGrpTable,
       "apGrpEntry": apGrpEntry,
       "apGrpName": apGrpName,
       "apGrpIndex": apGrpIndex,
       "apGrpIPAddress": apGrpIPAddress,
       "apGrpIPProtocol": apGrpIPProtocol,
       "apGrpPort": apGrpPort,
       "apGrpEnable": apGrpEnable,
       "apGrpStatus": apGrpStatus,
       "apPortMapCrateBasePort": apPortMapCrateBasePort,
       "apPortMapAvailPortsPerSfp": apPortMapAvailPortsPerSfp,
       "apGrpHitCount": apGrpHitCount,
       "apGrpByteCount": apGrpByteCount,
       "apGrpFrameCount": apGrpFrameCount,
       "apGrpCurConnections": apGrpCurConnections,
       "apGrpTotConnections": apGrpTotConnections,
       "apGrpCurFTPControl": apGrpCurFTPControl,
       "apGrpTotFTPControl": apGrpTotFTPControl}
)
