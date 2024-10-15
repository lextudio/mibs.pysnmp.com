# SNMP MIB module (TPLINK-ETHERNETOAMDISCINFO-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/TPLINK-ETHERNETOAMDISCINFO-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:06:01 2024
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

(ethernetOamDiscoveryInfo,) = mibBuilder.importSymbols(
    "TPLINK-ETHERNETOAM-MIB",
    "ethernetOamDiscoveryInfo")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_EthernetOamDiscInfoTable_Object = MibTable
ethernetOamDiscInfoTable = _EthernetOamDiscInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 60, 1, 5, 1)
)
if mibBuilder.loadTexts:
    ethernetOamDiscInfoTable.setStatus("current")
_EthernetOamDiscInfoEntry_Object = MibTableRow
ethernetOamDiscInfoEntry = _EthernetOamDiscInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 60, 1, 5, 1, 1)
)
ethernetOamDiscInfoEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    ethernetOamDiscInfoEntry.setStatus("current")
_EthernetOamDiscInfoPort_Type = DisplayString
_EthernetOamDiscInfoPort_Object = MibTableColumn
ethernetOamDiscInfoPort = _EthernetOamDiscInfoPort_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 60, 1, 5, 1, 1, 1),
    _EthernetOamDiscInfoPort_Type()
)
ethernetOamDiscInfoPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetOamDiscInfoPort.setStatus("current")


class _EthernetOamDiscInfoLocOAM_Type(Integer32):
    """Custom type ethernetOamDiscInfoLocOAM based on Integer32"""
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


_EthernetOamDiscInfoLocOAM_Type.__name__ = "Integer32"
_EthernetOamDiscInfoLocOAM_Object = MibTableColumn
ethernetOamDiscInfoLocOAM = _EthernetOamDiscInfoLocOAM_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 60, 1, 5, 1, 1, 2),
    _EthernetOamDiscInfoLocOAM_Type()
)
ethernetOamDiscInfoLocOAM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetOamDiscInfoLocOAM.setStatus("current")


class _EthernetOamDiscInfoLocMode_Type(Integer32):
    """Custom type ethernetOamDiscInfoLocMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("passive", 0))
    )


_EthernetOamDiscInfoLocMode_Type.__name__ = "Integer32"
_EthernetOamDiscInfoLocMode_Object = MibTableColumn
ethernetOamDiscInfoLocMode = _EthernetOamDiscInfoLocMode_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 60, 1, 5, 1, 1, 3),
    _EthernetOamDiscInfoLocMode_Type()
)
ethernetOamDiscInfoLocMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetOamDiscInfoLocMode.setStatus("current")
_EthernetOamDiscInfoLocMaxOAMPDU_Type = Integer32
_EthernetOamDiscInfoLocMaxOAMPDU_Object = MibTableColumn
ethernetOamDiscInfoLocMaxOAMPDU = _EthernetOamDiscInfoLocMaxOAMPDU_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 60, 1, 5, 1, 1, 4),
    _EthernetOamDiscInfoLocMaxOAMPDU_Type()
)
ethernetOamDiscInfoLocMaxOAMPDU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetOamDiscInfoLocMaxOAMPDU.setStatus("current")


class _EthernetOamDiscInfoLocRemoteLoopback_Type(Integer32):
    """Custom type ethernetOamDiscInfoLocRemoteLoopback based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("not-supported", 0),
          ("supported", 1))
    )


_EthernetOamDiscInfoLocRemoteLoopback_Type.__name__ = "Integer32"
_EthernetOamDiscInfoLocRemoteLoopback_Object = MibTableColumn
ethernetOamDiscInfoLocRemoteLoopback = _EthernetOamDiscInfoLocRemoteLoopback_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 60, 1, 5, 1, 1, 5),
    _EthernetOamDiscInfoLocRemoteLoopback_Type()
)
ethernetOamDiscInfoLocRemoteLoopback.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetOamDiscInfoLocRemoteLoopback.setStatus("current")


class _EthernetOamDiscInfoLocUnidirection_Type(Integer32):
    """Custom type ethernetOamDiscInfoLocUnidirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("not-supported", 0),
          ("supported", 1))
    )


_EthernetOamDiscInfoLocUnidirection_Type.__name__ = "Integer32"
_EthernetOamDiscInfoLocUnidirection_Object = MibTableColumn
ethernetOamDiscInfoLocUnidirection = _EthernetOamDiscInfoLocUnidirection_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 60, 1, 5, 1, 1, 6),
    _EthernetOamDiscInfoLocUnidirection_Type()
)
ethernetOamDiscInfoLocUnidirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetOamDiscInfoLocUnidirection.setStatus("current")


class _EthernetOamDiscInfoLocLinkMonitoring_Type(Integer32):
    """Custom type ethernetOamDiscInfoLocLinkMonitoring based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("not-supported", 0),
          ("supported", 1))
    )


_EthernetOamDiscInfoLocLinkMonitoring_Type.__name__ = "Integer32"
_EthernetOamDiscInfoLocLinkMonitoring_Object = MibTableColumn
ethernetOamDiscInfoLocLinkMonitoring = _EthernetOamDiscInfoLocLinkMonitoring_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 60, 1, 5, 1, 1, 7),
    _EthernetOamDiscInfoLocLinkMonitoring_Type()
)
ethernetOamDiscInfoLocLinkMonitoring.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetOamDiscInfoLocLinkMonitoring.setStatus("current")


class _EthernetOamDiscInfoLocVariableRequest_Type(Integer32):
    """Custom type ethernetOamDiscInfoLocVariableRequest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("not-supported", 0),
          ("supported", 1))
    )


_EthernetOamDiscInfoLocVariableRequest_Type.__name__ = "Integer32"
_EthernetOamDiscInfoLocVariableRequest_Object = MibTableColumn
ethernetOamDiscInfoLocVariableRequest = _EthernetOamDiscInfoLocVariableRequest_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 60, 1, 5, 1, 1, 8),
    _EthernetOamDiscInfoLocVariableRequest_Type()
)
ethernetOamDiscInfoLocVariableRequest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetOamDiscInfoLocVariableRequest.setStatus("current")
_EthernetOamDiscInfoLocPduRevision_Type = Integer32
_EthernetOamDiscInfoLocPduRevision_Object = MibTableColumn
ethernetOamDiscInfoLocPduRevision = _EthernetOamDiscInfoLocPduRevision_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 60, 1, 5, 1, 1, 9),
    _EthernetOamDiscInfoLocPduRevision_Type()
)
ethernetOamDiscInfoLocPduRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetOamDiscInfoLocPduRevision.setStatus("current")


class _EthernetOamDiscInfoLocOperationStatus_Type(OctetString):
    """Custom type ethernetOamDiscInfoLocOperationStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 25),
    )


_EthernetOamDiscInfoLocOperationStatus_Type.__name__ = "OctetString"
_EthernetOamDiscInfoLocOperationStatus_Object = MibTableColumn
ethernetOamDiscInfoLocOperationStatus = _EthernetOamDiscInfoLocOperationStatus_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 60, 1, 5, 1, 1, 10),
    _EthernetOamDiscInfoLocOperationStatus_Type()
)
ethernetOamDiscInfoLocOperationStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetOamDiscInfoLocOperationStatus.setStatus("current")


class _EthernetOamDiscInfoLocLoopbackStatus_Type(OctetString):
    """Custom type ethernetOamDiscInfoLocLoopbackStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_EthernetOamDiscInfoLocLoopbackStatus_Type.__name__ = "OctetString"
_EthernetOamDiscInfoLocLoopbackStatus_Object = MibTableColumn
ethernetOamDiscInfoLocLoopbackStatus = _EthernetOamDiscInfoLocLoopbackStatus_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 60, 1, 5, 1, 1, 11),
    _EthernetOamDiscInfoLocLoopbackStatus_Type()
)
ethernetOamDiscInfoLocLoopbackStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetOamDiscInfoLocLoopbackStatus.setStatus("current")


class _EthernetOamDiscInfoRmtMode_Type(Integer32):
    """Custom type ethernetOamDiscInfoRmtMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("passive", 0))
    )


_EthernetOamDiscInfoRmtMode_Type.__name__ = "Integer32"
_EthernetOamDiscInfoRmtMode_Object = MibTableColumn
ethernetOamDiscInfoRmtMode = _EthernetOamDiscInfoRmtMode_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 60, 1, 5, 1, 1, 12),
    _EthernetOamDiscInfoRmtMode_Type()
)
ethernetOamDiscInfoRmtMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetOamDiscInfoRmtMode.setStatus("current")


class _EthernetOamDiscInfoRmtMacAddress_Type(OctetString):
    """Custom type ethernetOamDiscInfoRmtMacAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 18),
    )


_EthernetOamDiscInfoRmtMacAddress_Type.__name__ = "OctetString"
_EthernetOamDiscInfoRmtMacAddress_Object = MibTableColumn
ethernetOamDiscInfoRmtMacAddress = _EthernetOamDiscInfoRmtMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 60, 1, 5, 1, 1, 13),
    _EthernetOamDiscInfoRmtMacAddress_Type()
)
ethernetOamDiscInfoRmtMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetOamDiscInfoRmtMacAddress.setStatus("current")


class _EthernetOamDiscInfoRmtVendorOUI_Type(OctetString):
    """Custom type ethernetOamDiscInfoRmtVendorOUI based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 7),
    )


_EthernetOamDiscInfoRmtVendorOUI_Type.__name__ = "OctetString"
_EthernetOamDiscInfoRmtVendorOUI_Object = MibTableColumn
ethernetOamDiscInfoRmtVendorOUI = _EthernetOamDiscInfoRmtVendorOUI_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 60, 1, 5, 1, 1, 14),
    _EthernetOamDiscInfoRmtVendorOUI_Type()
)
ethernetOamDiscInfoRmtVendorOUI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetOamDiscInfoRmtVendorOUI.setStatus("current")
_EthernetOamDiscInfoRmtMaxOAMPDU_Type = Integer32
_EthernetOamDiscInfoRmtMaxOAMPDU_Object = MibTableColumn
ethernetOamDiscInfoRmtMaxOAMPDU = _EthernetOamDiscInfoRmtMaxOAMPDU_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 60, 1, 5, 1, 1, 15),
    _EthernetOamDiscInfoRmtMaxOAMPDU_Type()
)
ethernetOamDiscInfoRmtMaxOAMPDU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetOamDiscInfoRmtMaxOAMPDU.setStatus("current")


class _EthernetOamDiscInfoRmtRemoteLoopback_Type(Integer32):
    """Custom type ethernetOamDiscInfoRmtRemoteLoopback based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("not-supported", 0),
          ("supported", 1))
    )


_EthernetOamDiscInfoRmtRemoteLoopback_Type.__name__ = "Integer32"
_EthernetOamDiscInfoRmtRemoteLoopback_Object = MibTableColumn
ethernetOamDiscInfoRmtRemoteLoopback = _EthernetOamDiscInfoRmtRemoteLoopback_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 60, 1, 5, 1, 1, 16),
    _EthernetOamDiscInfoRmtRemoteLoopback_Type()
)
ethernetOamDiscInfoRmtRemoteLoopback.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetOamDiscInfoRmtRemoteLoopback.setStatus("current")


class _EthernetOamDiscInfoRmtUnidirection_Type(Integer32):
    """Custom type ethernetOamDiscInfoRmtUnidirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("not-supported", 0),
          ("supported", 1))
    )


_EthernetOamDiscInfoRmtUnidirection_Type.__name__ = "Integer32"
_EthernetOamDiscInfoRmtUnidirection_Object = MibTableColumn
ethernetOamDiscInfoRmtUnidirection = _EthernetOamDiscInfoRmtUnidirection_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 60, 1, 5, 1, 1, 17),
    _EthernetOamDiscInfoRmtUnidirection_Type()
)
ethernetOamDiscInfoRmtUnidirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetOamDiscInfoRmtUnidirection.setStatus("current")


class _EthernetOamDiscInfoRmtLinkMonitoring_Type(Integer32):
    """Custom type ethernetOamDiscInfoRmtLinkMonitoring based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("not-supported", 0),
          ("supported", 1))
    )


_EthernetOamDiscInfoRmtLinkMonitoring_Type.__name__ = "Integer32"
_EthernetOamDiscInfoRmtLinkMonitoring_Object = MibTableColumn
ethernetOamDiscInfoRmtLinkMonitoring = _EthernetOamDiscInfoRmtLinkMonitoring_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 60, 1, 5, 1, 1, 18),
    _EthernetOamDiscInfoRmtLinkMonitoring_Type()
)
ethernetOamDiscInfoRmtLinkMonitoring.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetOamDiscInfoRmtLinkMonitoring.setStatus("current")


class _EthernetOamDiscInfoRmtVariableRequest_Type(Integer32):
    """Custom type ethernetOamDiscInfoRmtVariableRequest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("not-supported", 0),
          ("supported", 1))
    )


_EthernetOamDiscInfoRmtVariableRequest_Type.__name__ = "Integer32"
_EthernetOamDiscInfoRmtVariableRequest_Object = MibTableColumn
ethernetOamDiscInfoRmtVariableRequest = _EthernetOamDiscInfoRmtVariableRequest_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 60, 1, 5, 1, 1, 19),
    _EthernetOamDiscInfoRmtVariableRequest_Type()
)
ethernetOamDiscInfoRmtVariableRequest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetOamDiscInfoRmtVariableRequest.setStatus("current")
_EthernetOamDiscInfoRmtPduRevision_Type = Integer32
_EthernetOamDiscInfoRmtPduRevision_Object = MibTableColumn
ethernetOamDiscInfoRmtPduRevision = _EthernetOamDiscInfoRmtPduRevision_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 60, 1, 5, 1, 1, 20),
    _EthernetOamDiscInfoRmtPduRevision_Type()
)
ethernetOamDiscInfoRmtPduRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetOamDiscInfoRmtPduRevision.setStatus("current")


class _EthernetOamDiscInfoRmtVendorInfo_Type(OctetString):
    """Custom type ethernetOamDiscInfoRmtVendorInfo based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 9),
    )


_EthernetOamDiscInfoRmtVendorInfo_Type.__name__ = "OctetString"
_EthernetOamDiscInfoRmtVendorInfo_Object = MibTableColumn
ethernetOamDiscInfoRmtVendorInfo = _EthernetOamDiscInfoRmtVendorInfo_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 60, 1, 5, 1, 1, 21),
    _EthernetOamDiscInfoRmtVendorInfo_Type()
)
ethernetOamDiscInfoRmtVendorInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetOamDiscInfoRmtVendorInfo.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TPLINK-ETHERNETOAMDISCINFO-MIB",
    **{"ethernetOamDiscInfoTable": ethernetOamDiscInfoTable,
       "ethernetOamDiscInfoEntry": ethernetOamDiscInfoEntry,
       "ethernetOamDiscInfoPort": ethernetOamDiscInfoPort,
       "ethernetOamDiscInfoLocOAM": ethernetOamDiscInfoLocOAM,
       "ethernetOamDiscInfoLocMode": ethernetOamDiscInfoLocMode,
       "ethernetOamDiscInfoLocMaxOAMPDU": ethernetOamDiscInfoLocMaxOAMPDU,
       "ethernetOamDiscInfoLocRemoteLoopback": ethernetOamDiscInfoLocRemoteLoopback,
       "ethernetOamDiscInfoLocUnidirection": ethernetOamDiscInfoLocUnidirection,
       "ethernetOamDiscInfoLocLinkMonitoring": ethernetOamDiscInfoLocLinkMonitoring,
       "ethernetOamDiscInfoLocVariableRequest": ethernetOamDiscInfoLocVariableRequest,
       "ethernetOamDiscInfoLocPduRevision": ethernetOamDiscInfoLocPduRevision,
       "ethernetOamDiscInfoLocOperationStatus": ethernetOamDiscInfoLocOperationStatus,
       "ethernetOamDiscInfoLocLoopbackStatus": ethernetOamDiscInfoLocLoopbackStatus,
       "ethernetOamDiscInfoRmtMode": ethernetOamDiscInfoRmtMode,
       "ethernetOamDiscInfoRmtMacAddress": ethernetOamDiscInfoRmtMacAddress,
       "ethernetOamDiscInfoRmtVendorOUI": ethernetOamDiscInfoRmtVendorOUI,
       "ethernetOamDiscInfoRmtMaxOAMPDU": ethernetOamDiscInfoRmtMaxOAMPDU,
       "ethernetOamDiscInfoRmtRemoteLoopback": ethernetOamDiscInfoRmtRemoteLoopback,
       "ethernetOamDiscInfoRmtUnidirection": ethernetOamDiscInfoRmtUnidirection,
       "ethernetOamDiscInfoRmtLinkMonitoring": ethernetOamDiscInfoRmtLinkMonitoring,
       "ethernetOamDiscInfoRmtVariableRequest": ethernetOamDiscInfoRmtVariableRequest,
       "ethernetOamDiscInfoRmtPduRevision": ethernetOamDiscInfoRmtPduRevision,
       "ethernetOamDiscInfoRmtVendorInfo": ethernetOamDiscInfoRmtVendorInfo}
)
