# SNMP MIB module (DF10-DCB-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/DF10-DCB-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:26:14 2024
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

(f10Mgmt,) = mibBuilder.importSymbols(
    "FORCE10-SMI",
    "f10Mgmt")

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

dF10Dcb = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 3, 15)
)
dF10Dcb.setRevisions(
        ("2012-04-16 00:00",
         "2011-11-24 00:00",
         "2010-09-25 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class EnabledStatus(Integer32, TextualConvention):
    status = "current"
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



class DcbAdminMode(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )



class DcbState(Integer32, TextualConvention):
    status = "current"
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
        *(("init", 1),
          ("internallypropagated", 3),
          ("off", 0),
          ("rxrecommended", 2))
    )



class DcbStateMachineType(Integer32, TextualConvention):
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
        *(("asymmetric", 1),
          ("feature", 3),
          ("symmetric", 2))
    )



class DcbxPortRole(Integer32, TextualConvention):
    status = "current"
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
        *(("autodown", 3),
          ("autoup", 2),
          ("configSource", 4),
          ("manual", 1))
    )



class DcbxVersion(Integer32, TextualConvention):
    status = "current"
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
        *(("auto", 1),
          ("cee", 4),
          ("cin", 3),
          ("ieee", 2))
    )



# MIB Managed Objects in the order of their OIDs

_DF10DcbSystem_ObjectIdentity = ObjectIdentity
dF10DcbSystem = _DF10DcbSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 3, 15, 1)
)


class _DF10DcbPfcMinThreshold_Type(Unsigned32):
    """Custom type dF10DcbPfcMinThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_DF10DcbPfcMinThreshold_Type.__name__ = "Unsigned32"
_DF10DcbPfcMinThreshold_Object = MibScalar
dF10DcbPfcMinThreshold = _DF10DcbPfcMinThreshold_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 15, 1, 1),
    _DF10DcbPfcMinThreshold_Type()
)
dF10DcbPfcMinThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dF10DcbPfcMinThreshold.setStatus("current")


class _DF10DcbPfcMaxThreshold_Type(Unsigned32):
    """Custom type dF10DcbPfcMaxThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_DF10DcbPfcMaxThreshold_Type.__name__ = "Unsigned32"
_DF10DcbPfcMaxThreshold_Object = MibScalar
dF10DcbPfcMaxThreshold = _DF10DcbPfcMaxThreshold_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 15, 1, 2),
    _DF10DcbPfcMaxThreshold_Type()
)
dF10DcbPfcMaxThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dF10DcbPfcMaxThreshold.setStatus("current")


class _DF10DcbMaxPfcProfiles_Type(Unsigned32):
    """Custom type dF10DcbMaxPfcProfiles based on Unsigned32"""
    defaultValue = 256

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_DF10DcbMaxPfcProfiles_Type.__name__ = "Unsigned32"
_DF10DcbMaxPfcProfiles_Object = MibScalar
dF10DcbMaxPfcProfiles = _DF10DcbMaxPfcProfiles_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 15, 1, 3),
    _DF10DcbMaxPfcProfiles_Type()
)
dF10DcbMaxPfcProfiles.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dF10DcbMaxPfcProfiles.setStatus("current")
_DF10DcbObjects_ObjectIdentity = ObjectIdentity
dF10DcbObjects = _DF10DcbObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 3, 15, 2)
)
_DF10DcbPortTable_Object = MibTable
dF10DcbPortTable = _DF10DcbPortTable_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 15, 2, 1)
)
if mibBuilder.loadTexts:
    dF10DcbPortTable.setStatus("obsolete")
_DF10DcbPortEntry_Object = MibTableRow
dF10DcbPortEntry = _DF10DcbPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 15, 2, 1, 1)
)
dF10DcbPortEntry.setIndexNames(
    (0, "DF10-DCB-MIB", "dF10DcbPortNumber"),
)
if mibBuilder.loadTexts:
    dF10DcbPortEntry.setStatus("obsolete")
_DF10DcbPortNumber_Type = InterfaceIndex
_DF10DcbPortNumber_Object = MibTableColumn
dF10DcbPortNumber = _DF10DcbPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 15, 2, 1, 1, 1),
    _DF10DcbPortNumber_Type()
)
dF10DcbPortNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dF10DcbPortNumber.setStatus("obsolete")


class _DF10DcbETSAdminStatus_Type(EnabledStatus):
    """Custom type dF10DcbETSAdminStatus based on EnabledStatus"""


_DF10DcbETSAdminStatus_Object = MibTableColumn
dF10DcbETSAdminStatus = _DF10DcbETSAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 15, 2, 1, 1, 2),
    _DF10DcbETSAdminStatus_Type()
)
dF10DcbETSAdminStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dF10DcbETSAdminStatus.setStatus("obsolete")


class _DF10DcbPFCAdminStatus_Type(EnabledStatus):
    """Custom type dF10DcbPFCAdminStatus based on EnabledStatus"""


_DF10DcbPFCAdminStatus_Object = MibTableColumn
dF10DcbPFCAdminStatus = _DF10DcbPFCAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 15, 2, 1, 1, 3),
    _DF10DcbPFCAdminStatus_Type()
)
dF10DcbPFCAdminStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dF10DcbPFCAdminStatus.setStatus("obsolete")
_DF10DcbApplicationObjects_ObjectIdentity = ObjectIdentity
dF10DcbApplicationObjects = _DF10DcbApplicationObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 3, 15, 3)
)
_DF10DCBXObjects_ObjectIdentity = ObjectIdentity
dF10DCBXObjects = _DF10DCBXObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 3, 15, 3, 1)
)
_DF10DCBXScalars_ObjectIdentity = ObjectIdentity
dF10DCBXScalars = _DF10DCBXScalars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 3, 15, 3, 1, 1)
)
_DF10DcbxGlobalTraceLevel_Type = Integer32
_DF10DcbxGlobalTraceLevel_Object = MibScalar
dF10DcbxGlobalTraceLevel = _DF10DcbxGlobalTraceLevel_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 15, 3, 1, 1, 1),
    _DF10DcbxGlobalTraceLevel_Type()
)
dF10DcbxGlobalTraceLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dF10DcbxGlobalTraceLevel.setStatus("current")


class _DF10DCBXGlobalVersion_Type(DcbxVersion):
    """Custom type dF10DCBXGlobalVersion based on DcbxVersion"""
    defaultValue = 1


_DF10DCBXGlobalVersion_Object = MibScalar
dF10DCBXGlobalVersion = _DF10DCBXGlobalVersion_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 15, 3, 1, 1, 2),
    _DF10DCBXGlobalVersion_Type()
)
dF10DCBXGlobalVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dF10DCBXGlobalVersion.setStatus("current")
_DF10DCBXPortTable_Object = MibTable
dF10DCBXPortTable = _DF10DCBXPortTable_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 15, 3, 1, 2)
)
if mibBuilder.loadTexts:
    dF10DCBXPortTable.setStatus("current")
_DF10DCBXPortEntry_Object = MibTableRow
dF10DCBXPortEntry = _DF10DCBXPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 15, 3, 1, 2, 1)
)
dF10DCBXPortEntry.setIndexNames(
    (0, "DF10-DCB-MIB", "dF10DCBXPortNumber"),
)
if mibBuilder.loadTexts:
    dF10DCBXPortEntry.setStatus("current")
_DF10DCBXPortNumber_Type = InterfaceIndex
_DF10DCBXPortNumber_Object = MibTableColumn
dF10DCBXPortNumber = _DF10DCBXPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 15, 3, 1, 2, 1, 1),
    _DF10DCBXPortNumber_Type()
)
dF10DCBXPortNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dF10DCBXPortNumber.setStatus("current")


class _DF10DCBXAdminStatus_Type(EnabledStatus):
    """Custom type dF10DCBXAdminStatus based on EnabledStatus"""


_DF10DCBXAdminStatus_Object = MibTableColumn
dF10DCBXAdminStatus = _DF10DCBXAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 15, 3, 1, 2, 1, 2),
    _DF10DCBXAdminStatus_Type()
)
dF10DCBXAdminStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dF10DCBXAdminStatus.setStatus("current")


class _DF10DCBXAutoCfgPortRole_Type(DcbxPortRole):
    """Custom type dF10DCBXAutoCfgPortRole based on DcbxPortRole"""
    defaultValue = 1


_DF10DCBXAutoCfgPortRole_Object = MibTableColumn
dF10DCBXAutoCfgPortRole = _DF10DCBXAutoCfgPortRole_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 15, 3, 1, 2, 1, 3),
    _DF10DCBXAutoCfgPortRole_Type()
)
dF10DCBXAutoCfgPortRole.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dF10DCBXAutoCfgPortRole.setStatus("current")


class _DF10DCBXPortVersion_Type(DcbxVersion):
    """Custom type dF10DCBXPortVersion based on DcbxVersion"""
    defaultValue = 1


_DF10DCBXPortVersion_Object = MibTableColumn
dF10DCBXPortVersion = _DF10DCBXPortVersion_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 15, 3, 1, 2, 1, 4),
    _DF10DCBXPortVersion_Type()
)
dF10DCBXPortVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dF10DCBXPortVersion.setStatus("current")


class _DF10DCBXPortSupportedTLVs_Type(Bits):
    """Custom type dF10DCBXPortSupportedTLVs based on Bits"""
    namedValues = NamedValues(
        *(("applicationPriorityFCOE", 3),
          ("applicationPriorityISCSI", 4),
          ("etsConfig", 1),
          ("etsRecom", 2),
          ("pfc", 0))
    )

_DF10DCBXPortSupportedTLVs_Type.__name__ = "Bits"
_DF10DCBXPortSupportedTLVs_Object = MibTableColumn
dF10DCBXPortSupportedTLVs = _DF10DCBXPortSupportedTLVs_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 15, 3, 1, 2, 1, 5),
    _DF10DCBXPortSupportedTLVs_Type()
)
dF10DCBXPortSupportedTLVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dF10DCBXPortSupportedTLVs.setStatus("current")


class _DF10DCBXPortConfigTLVsTxEnable_Type(Bits):
    """Custom type dF10DCBXPortConfigTLVsTxEnable based on Bits"""
    namedValues = NamedValues(
        *(("applicationPriorityFCOE", 3),
          ("applicationPriorityISCSI", 4),
          ("etsConfig", 1),
          ("etsRecom", 2),
          ("pfc", 0))
    )

_DF10DCBXPortConfigTLVsTxEnable_Type.__name__ = "Bits"
_DF10DCBXPortConfigTLVsTxEnable_Object = MibTableColumn
dF10DCBXPortConfigTLVsTxEnable = _DF10DCBXPortConfigTLVsTxEnable_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 15, 3, 1, 2, 1, 6),
    _DF10DCBXPortConfigTLVsTxEnable_Type()
)
dF10DCBXPortConfigTLVsTxEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dF10DCBXPortConfigTLVsTxEnable.setStatus("current")
_DF10DCBXPortStatusTable_Object = MibTable
dF10DCBXPortStatusTable = _DF10DCBXPortStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 15, 3, 1, 3)
)
if mibBuilder.loadTexts:
    dF10DCBXPortStatusTable.setStatus("current")
_DF10DCBXPortStatusEntry_Object = MibTableRow
dF10DCBXPortStatusEntry = _DF10DCBXPortStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 15, 3, 1, 3, 1)
)
if mibBuilder.loadTexts:
    dF10DCBXPortStatusEntry.setStatus("current")


class _DF10DCBXPortOperVersion_Type(DcbxVersion):
    """Custom type dF10DCBXPortOperVersion based on DcbxVersion"""
    defaultValue = 1


_DF10DCBXPortOperVersion_Object = MibTableColumn
dF10DCBXPortOperVersion = _DF10DCBXPortOperVersion_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 15, 3, 1, 3, 1, 2),
    _DF10DCBXPortOperVersion_Type()
)
dF10DCBXPortOperVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dF10DCBXPortOperVersion.setStatus("current")
_DF10DCBXPortPeerMACaddress_Type = MacAddress
_DF10DCBXPortPeerMACaddress_Object = MibTableColumn
dF10DCBXPortPeerMACaddress = _DF10DCBXPortPeerMACaddress_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 15, 3, 1, 3, 1, 3),
    _DF10DCBXPortPeerMACaddress_Type()
)
dF10DCBXPortPeerMACaddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dF10DCBXPortPeerMACaddress.setStatus("current")


class _DF10DCBXPortCfgSource_Type(Integer32):
    """Custom type dF10DCBXPortCfgSource based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_DF10DCBXPortCfgSource_Type.__name__ = "Integer32"
_DF10DCBXPortCfgSource_Object = MibTableColumn
dF10DCBXPortCfgSource = _DF10DCBXPortCfgSource_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 15, 3, 1, 3, 1, 4),
    _DF10DCBXPortCfgSource_Type()
)
dF10DCBXPortCfgSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dF10DCBXPortCfgSource.setStatus("current")
_DF10DCBXOperStatus_Type = EnabledStatus
_DF10DCBXOperStatus_Object = MibTableColumn
dF10DCBXOperStatus = _DF10DCBXOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 15, 3, 1, 3, 1, 5),
    _DF10DCBXOperStatus_Type()
)
dF10DCBXOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dF10DCBXOperStatus.setStatus("current")
_DF10DCBXPortMultiplePeerCount_Type = Counter32
_DF10DCBXPortMultiplePeerCount_Object = MibTableColumn
dF10DCBXPortMultiplePeerCount = _DF10DCBXPortMultiplePeerCount_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 15, 3, 1, 3, 1, 6),
    _DF10DCBXPortMultiplePeerCount_Type()
)
dF10DCBXPortMultiplePeerCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dF10DCBXPortMultiplePeerCount.setStatus("current")
_DF10DCBXPortPeerRemovedCount_Type = Counter32
_DF10DCBXPortPeerRemovedCount_Object = MibTableColumn
dF10DCBXPortPeerRemovedCount = _DF10DCBXPortPeerRemovedCount_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 15, 3, 1, 3, 1, 7),
    _DF10DCBXPortPeerRemovedCount_Type()
)
dF10DCBXPortPeerRemovedCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dF10DCBXPortPeerRemovedCount.setStatus("current")
_DF10DCBXPortPeerOperVersionNum_Type = Unsigned32
_DF10DCBXPortPeerOperVersionNum_Object = MibTableColumn
dF10DCBXPortPeerOperVersionNum = _DF10DCBXPortPeerOperVersionNum_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 15, 3, 1, 3, 1, 8),
    _DF10DCBXPortPeerOperVersionNum_Type()
)
dF10DCBXPortPeerOperVersionNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dF10DCBXPortPeerOperVersionNum.setStatus("current")
_DF10DCBXPortPeerMaxVersion_Type = Unsigned32
_DF10DCBXPortPeerMaxVersion_Object = MibTableColumn
dF10DCBXPortPeerMaxVersion = _DF10DCBXPortPeerMaxVersion_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 15, 3, 1, 3, 1, 9),
    _DF10DCBXPortPeerMaxVersion_Type()
)
dF10DCBXPortPeerMaxVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dF10DCBXPortPeerMaxVersion.setStatus("current")
_DF10DCBXPortSeqNum_Type = Unsigned32
_DF10DCBXPortSeqNum_Object = MibTableColumn
dF10DCBXPortSeqNum = _DF10DCBXPortSeqNum_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 15, 3, 1, 3, 1, 10),
    _DF10DCBXPortSeqNum_Type()
)
dF10DCBXPortSeqNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dF10DCBXPortSeqNum.setStatus("current")
_DF10DCBXPortAckNum_Type = Unsigned32
_DF10DCBXPortAckNum_Object = MibTableColumn
dF10DCBXPortAckNum = _DF10DCBXPortAckNum_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 15, 3, 1, 3, 1, 11),
    _DF10DCBXPortAckNum_Type()
)
dF10DCBXPortAckNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dF10DCBXPortAckNum.setStatus("current")
_DF10DCBXPortPeerRcvdAckNum_Type = Unsigned32
_DF10DCBXPortPeerRcvdAckNum_Object = MibTableColumn
dF10DCBXPortPeerRcvdAckNum = _DF10DCBXPortPeerRcvdAckNum_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 15, 3, 1, 3, 1, 12),
    _DF10DCBXPortPeerRcvdAckNum_Type()
)
dF10DCBXPortPeerRcvdAckNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dF10DCBXPortPeerRcvdAckNum.setStatus("current")
_DF10DCBXPortTxCount_Type = Counter32
_DF10DCBXPortTxCount_Object = MibTableColumn
dF10DCBXPortTxCount = _DF10DCBXPortTxCount_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 15, 3, 1, 3, 1, 13),
    _DF10DCBXPortTxCount_Type()
)
dF10DCBXPortTxCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dF10DCBXPortTxCount.setStatus("current")
_DF10DCBXPortRxCount_Type = Counter32
_DF10DCBXPortRxCount_Object = MibTableColumn
dF10DCBXPortRxCount = _DF10DCBXPortRxCount_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 15, 3, 1, 3, 1, 14),
    _DF10DCBXPortRxCount_Type()
)
dF10DCBXPortRxCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dF10DCBXPortRxCount.setStatus("current")
_DF10DCBXPortErrorFramesCount_Type = Counter32
_DF10DCBXPortErrorFramesCount_Object = MibTableColumn
dF10DCBXPortErrorFramesCount = _DF10DCBXPortErrorFramesCount_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 15, 3, 1, 3, 1, 15),
    _DF10DCBXPortErrorFramesCount_Type()
)
dF10DCBXPortErrorFramesCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dF10DCBXPortErrorFramesCount.setStatus("current")
_DF10ETSObjects_ObjectIdentity = ObjectIdentity
dF10ETSObjects = _DF10ETSObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 3, 15, 3, 2)
)
_DF10ETSScalars_ObjectIdentity = ObjectIdentity
dF10ETSScalars = _DF10ETSScalars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 3, 15, 3, 2, 1)
)


class _DF10ETSSystemControl_Type(Integer32):
    """Custom type dF10ETSSystemControl based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("running", 1),
          ("shutdown", 2))
    )


_DF10ETSSystemControl_Type.__name__ = "Integer32"
_DF10ETSSystemControl_Object = MibScalar
dF10ETSSystemControl = _DF10ETSSystemControl_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 15, 3, 2, 1, 1),
    _DF10ETSSystemControl_Type()
)
dF10ETSSystemControl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dF10ETSSystemControl.setStatus("current")


class _DF10ETSModuleStatus_Type(EnabledStatus):
    """Custom type dF10ETSModuleStatus based on EnabledStatus"""


_DF10ETSModuleStatus_Object = MibScalar
dF10ETSModuleStatus = _DF10ETSModuleStatus_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 15, 3, 2, 1, 2),
    _DF10ETSModuleStatus_Type()
)
dF10ETSModuleStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dF10ETSModuleStatus.setStatus("current")


class _DF10ETSClearCounters_Type(TruthValue):
    """Custom type dF10ETSClearCounters based on TruthValue"""


_DF10ETSClearCounters_Object = MibScalar
dF10ETSClearCounters = _DF10ETSClearCounters_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 15, 3, 2, 1, 3),
    _DF10ETSClearCounters_Type()
)
dF10ETSClearCounters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dF10ETSClearCounters.setStatus("current")


class _DF10ETSGlobalEnableTrap_Type(Integer32):
    """Custom type dF10ETSGlobalEnableTrap based on Integer32"""
    defaultValue = 0


_DF10ETSGlobalEnableTrap_Object = MibScalar
dF10ETSGlobalEnableTrap = _DF10ETSGlobalEnableTrap_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 15, 3, 2, 1, 4),
    _DF10ETSGlobalEnableTrap_Type()
)
dF10ETSGlobalEnableTrap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dF10ETSGlobalEnableTrap.setStatus("current")
_DF10ETSPortTable_Object = MibTable
dF10ETSPortTable = _DF10ETSPortTable_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 15, 3, 2, 2)
)
if mibBuilder.loadTexts:
    dF10ETSPortTable.setStatus("current")
_DF10ETSPortEntry_Object = MibTableRow
dF10ETSPortEntry = _DF10ETSPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 15, 3, 2, 2, 1)
)
dF10ETSPortEntry.setIndexNames(
    (0, "DF10-DCB-MIB", "dF10ETSPortNumber"),
)
if mibBuilder.loadTexts:
    dF10ETSPortEntry.setStatus("current")
_DF10ETSPortNumber_Type = InterfaceIndex
_DF10ETSPortNumber_Object = MibTableColumn
dF10ETSPortNumber = _DF10ETSPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 15, 3, 2, 2, 1, 1),
    _DF10ETSPortNumber_Type()
)
dF10ETSPortNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dF10ETSPortNumber.setStatus("current")


class _DF10ETSAdminMode_Type(DcbAdminMode):
    """Custom type dF10ETSAdminMode based on DcbAdminMode"""


_DF10ETSAdminMode_Object = MibTableColumn
dF10ETSAdminMode = _DF10ETSAdminMode_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 15, 3, 2, 2, 1, 2),
    _DF10ETSAdminMode_Type()
)
dF10ETSAdminMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dF10ETSAdminMode.setStatus("current")
_DF10ETSDcbxOperState_Type = DcbState
_DF10ETSDcbxOperState_Object = MibTableColumn
dF10ETSDcbxOperState = _DF10ETSDcbxOperState_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 15, 3, 2, 2, 1, 3),
    _DF10ETSDcbxOperState_Type()
)
dF10ETSDcbxOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dF10ETSDcbxOperState.setStatus("current")
_DF10ETSDcbxStateMachine_Type = DcbStateMachineType
_DF10ETSDcbxStateMachine_Object = MibTableColumn
dF10ETSDcbxStateMachine = _DF10ETSDcbxStateMachine_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 15, 3, 2, 2, 1, 4),
    _DF10ETSDcbxStateMachine_Type()
)
dF10ETSDcbxStateMachine.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dF10ETSDcbxStateMachine.setStatus("current")
_DF10ETSOperStatus_Type = EnabledStatus
_DF10ETSOperStatus_Object = MibTableColumn
dF10ETSOperStatus = _DF10ETSOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 15, 3, 2, 2, 1, 5),
    _DF10ETSOperStatus_Type()
)
dF10ETSOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dF10ETSOperStatus.setStatus("current")


class _DF10ETSClearTLVCounters_Type(TruthValue):
    """Custom type dF10ETSClearTLVCounters based on TruthValue"""


_DF10ETSClearTLVCounters_Object = MibTableColumn
dF10ETSClearTLVCounters = _DF10ETSClearTLVCounters_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 15, 3, 2, 2, 1, 6),
    _DF10ETSClearTLVCounters_Type()
)
dF10ETSClearTLVCounters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dF10ETSClearTLVCounters.setStatus("current")
_DF10ETSConfTxTLVCounter_Type = Counter32
_DF10ETSConfTxTLVCounter_Object = MibTableColumn
dF10ETSConfTxTLVCounter = _DF10ETSConfTxTLVCounter_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 15, 3, 2, 2, 1, 7),
    _DF10ETSConfTxTLVCounter_Type()
)
dF10ETSConfTxTLVCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dF10ETSConfTxTLVCounter.setStatus("current")
_DF10ETSConfRxTLVCounter_Type = Counter32
_DF10ETSConfRxTLVCounter_Object = MibTableColumn
dF10ETSConfRxTLVCounter = _DF10ETSConfRxTLVCounter_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 15, 3, 2, 2, 1, 8),
    _DF10ETSConfRxTLVCounter_Type()
)
dF10ETSConfRxTLVCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dF10ETSConfRxTLVCounter.setStatus("current")
_DF10ETSConfRxTLVErrors_Type = Counter32
_DF10ETSConfRxTLVErrors_Object = MibTableColumn
dF10ETSConfRxTLVErrors = _DF10ETSConfRxTLVErrors_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 15, 3, 2, 2, 1, 9),
    _DF10ETSConfRxTLVErrors_Type()
)
dF10ETSConfRxTLVErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dF10ETSConfRxTLVErrors.setStatus("current")
_DF10ETSRecoTxTLVCounter_Type = Counter32
_DF10ETSRecoTxTLVCounter_Object = MibTableColumn
dF10ETSRecoTxTLVCounter = _DF10ETSRecoTxTLVCounter_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 15, 3, 2, 2, 1, 10),
    _DF10ETSRecoTxTLVCounter_Type()
)
dF10ETSRecoTxTLVCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dF10ETSRecoTxTLVCounter.setStatus("current")
_DF10ETSRecoRxTLVCounter_Type = Counter32
_DF10ETSRecoRxTLVCounter_Object = MibTableColumn
dF10ETSRecoRxTLVCounter = _DF10ETSRecoRxTLVCounter_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 15, 3, 2, 2, 1, 11),
    _DF10ETSRecoRxTLVCounter_Type()
)
dF10ETSRecoRxTLVCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dF10ETSRecoRxTLVCounter.setStatus("current")
_DF10ETSRecoRxTLVErrors_Type = Counter32
_DF10ETSRecoRxTLVErrors_Object = MibTableColumn
dF10ETSRecoRxTLVErrors = _DF10ETSRecoRxTLVErrors_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 15, 3, 2, 2, 1, 12),
    _DF10ETSRecoRxTLVErrors_Type()
)
dF10ETSRecoRxTLVErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dF10ETSRecoRxTLVErrors.setStatus("current")
_DF10PFCObjects_ObjectIdentity = ObjectIdentity
dF10PFCObjects = _DF10PFCObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 3, 15, 3, 3)
)
_DF10PFCScalars_ObjectIdentity = ObjectIdentity
dF10PFCScalars = _DF10PFCScalars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 3, 15, 3, 3, 1)
)


class _DF10PFCSystemControl_Type(Integer32):
    """Custom type dF10PFCSystemControl based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("running", 1),
          ("shutdown", 2))
    )


_DF10PFCSystemControl_Type.__name__ = "Integer32"
_DF10PFCSystemControl_Object = MibScalar
dF10PFCSystemControl = _DF10PFCSystemControl_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 15, 3, 3, 1, 1),
    _DF10PFCSystemControl_Type()
)
dF10PFCSystemControl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dF10PFCSystemControl.setStatus("current")


class _DF10PFCModuleStatus_Type(EnabledStatus):
    """Custom type dF10PFCModuleStatus based on EnabledStatus"""


_DF10PFCModuleStatus_Object = MibScalar
dF10PFCModuleStatus = _DF10PFCModuleStatus_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 15, 3, 3, 1, 2),
    _DF10PFCModuleStatus_Type()
)
dF10PFCModuleStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dF10PFCModuleStatus.setStatus("current")


class _DF10PFCClearCounters_Type(TruthValue):
    """Custom type dF10PFCClearCounters based on TruthValue"""


_DF10PFCClearCounters_Object = MibScalar
dF10PFCClearCounters = _DF10PFCClearCounters_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 15, 3, 3, 1, 3),
    _DF10PFCClearCounters_Type()
)
dF10PFCClearCounters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dF10PFCClearCounters.setStatus("current")


class _DF10PFCGlobalEnableTrap_Type(Integer32):
    """Custom type dF10PFCGlobalEnableTrap based on Integer32"""
    defaultValue = 0


_DF10PFCGlobalEnableTrap_Object = MibScalar
dF10PFCGlobalEnableTrap = _DF10PFCGlobalEnableTrap_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 15, 3, 3, 1, 4),
    _DF10PFCGlobalEnableTrap_Type()
)
dF10PFCGlobalEnableTrap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dF10PFCGlobalEnableTrap.setStatus("current")
_DF10PFCPortTable_Object = MibTable
dF10PFCPortTable = _DF10PFCPortTable_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 15, 3, 3, 2)
)
if mibBuilder.loadTexts:
    dF10PFCPortTable.setStatus("current")
_DF10PFCPortEntry_Object = MibTableRow
dF10PFCPortEntry = _DF10PFCPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 15, 3, 3, 2, 1)
)
dF10PFCPortEntry.setIndexNames(
    (0, "DF10-DCB-MIB", "dF10PFCPortNumber"),
)
if mibBuilder.loadTexts:
    dF10PFCPortEntry.setStatus("current")
_DF10PFCPortNumber_Type = InterfaceIndex
_DF10PFCPortNumber_Object = MibTableColumn
dF10PFCPortNumber = _DF10PFCPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 15, 3, 3, 2, 1, 1),
    _DF10PFCPortNumber_Type()
)
dF10PFCPortNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dF10PFCPortNumber.setStatus("current")


class _DF10PFCAdminMode_Type(DcbAdminMode):
    """Custom type dF10PFCAdminMode based on DcbAdminMode"""


_DF10PFCAdminMode_Object = MibTableColumn
dF10PFCAdminMode = _DF10PFCAdminMode_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 15, 3, 3, 2, 1, 2),
    _DF10PFCAdminMode_Type()
)
dF10PFCAdminMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dF10PFCAdminMode.setStatus("current")
_DF10PFCDcbxOperState_Type = DcbState
_DF10PFCDcbxOperState_Object = MibTableColumn
dF10PFCDcbxOperState = _DF10PFCDcbxOperState_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 15, 3, 3, 2, 1, 3),
    _DF10PFCDcbxOperState_Type()
)
dF10PFCDcbxOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dF10PFCDcbxOperState.setStatus("current")
_DF10PFCDcbxStateMachine_Type = DcbStateMachineType
_DF10PFCDcbxStateMachine_Object = MibTableColumn
dF10PFCDcbxStateMachine = _DF10PFCDcbxStateMachine_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 15, 3, 3, 2, 1, 4),
    _DF10PFCDcbxStateMachine_Type()
)
dF10PFCDcbxStateMachine.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dF10PFCDcbxStateMachine.setStatus("current")
_DF10PFCOperStatus_Type = EnabledStatus
_DF10PFCOperStatus_Object = MibTableColumn
dF10PFCOperStatus = _DF10PFCOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 15, 3, 3, 2, 1, 5),
    _DF10PFCOperStatus_Type()
)
dF10PFCOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dF10PFCOperStatus.setStatus("current")


class _DF10PFCClearTLVCounters_Type(TruthValue):
    """Custom type dF10PFCClearTLVCounters based on TruthValue"""


_DF10PFCClearTLVCounters_Object = MibTableColumn
dF10PFCClearTLVCounters = _DF10PFCClearTLVCounters_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 15, 3, 3, 2, 1, 6),
    _DF10PFCClearTLVCounters_Type()
)
dF10PFCClearTLVCounters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dF10PFCClearTLVCounters.setStatus("current")
_DF10PFCTxTLVCounter_Type = Counter32
_DF10PFCTxTLVCounter_Object = MibTableColumn
dF10PFCTxTLVCounter = _DF10PFCTxTLVCounter_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 15, 3, 3, 2, 1, 7),
    _DF10PFCTxTLVCounter_Type()
)
dF10PFCTxTLVCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dF10PFCTxTLVCounter.setStatus("current")
_DF10PFCRxTLVCounter_Type = Counter32
_DF10PFCRxTLVCounter_Object = MibTableColumn
dF10PFCRxTLVCounter = _DF10PFCRxTLVCounter_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 15, 3, 3, 2, 1, 8),
    _DF10PFCRxTLVCounter_Type()
)
dF10PFCRxTLVCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dF10PFCRxTLVCounter.setStatus("current")
_DF10PFCRxTLVErrors_Type = Counter32
_DF10PFCRxTLVErrors_Object = MibTableColumn
dF10PFCRxTLVErrors = _DF10PFCRxTLVErrors_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 15, 3, 3, 2, 1, 9),
    _DF10PFCRxTLVErrors_Type()
)
dF10PFCRxTLVErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dF10PFCRxTLVErrors.setStatus("current")
_DF10DcbNotificationObjects_ObjectIdentity = ObjectIdentity
dF10DcbNotificationObjects = _DF10DcbNotificationObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 3, 15, 4)
)
_DF10DCBTraps_ObjectIdentity = ObjectIdentity
dF10DCBTraps = _DF10DCBTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 3, 15, 4, 0)
)
_DF10DCBTrapObjects_ObjectIdentity = ObjectIdentity
dF10DCBTrapObjects = _DF10DCBTrapObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 3, 15, 4, 1)
)
_DF10DcbTrapPortNumber_Type = TruthValue
_DF10DcbTrapPortNumber_Object = MibScalar
dF10DcbTrapPortNumber = _DF10DcbTrapPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 15, 4, 1, 1),
    _DF10DcbTrapPortNumber_Type()
)
dF10DcbTrapPortNumber.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    dF10DcbTrapPortNumber.setStatus("current")
_DF10DcbPeerUpStatus_Type = TruthValue
_DF10DcbPeerUpStatus_Object = MibScalar
dF10DcbPeerUpStatus = _DF10DcbPeerUpStatus_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 15, 4, 1, 2),
    _DF10DcbPeerUpStatus_Type()
)
dF10DcbPeerUpStatus.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    dF10DcbPeerUpStatus.setStatus("current")
_DF10DCBMibConformance_ObjectIdentity = ObjectIdentity
dF10DCBMibConformance = _DF10DCBMibConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 3, 15, 5)
)
_DF10DCBMibCompliances_ObjectIdentity = ObjectIdentity
dF10DCBMibCompliances = _DF10DCBMibCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 3, 15, 5, 1)
)
_DF10DCBMibGroups_ObjectIdentity = ObjectIdentity
dF10DCBMibGroups = _DF10DCBMibGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 3, 15, 5, 2)
)
dF10DCBXPortEntry.registerAugmentions(
    ("DF10-DCB-MIB",
     "dF10DCBXPortStatusEntry")
)
dF10DCBXPortStatusEntry.setIndexNames(*dF10DCBXPortEntry.getIndexNames())

# Managed Objects groups

dF10DcbSystemObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6027, 3, 15, 5, 2, 1)
)
dF10DcbSystemObjectGroup.setObjects(
      *(("DF10-DCB-MIB", "dF10DcbPfcMinThreshold"),
        ("DF10-DCB-MIB", "dF10DcbPfcMaxThreshold"),
        ("DF10-DCB-MIB", "dF10DcbMaxPfcProfiles"))
)
if mibBuilder.loadTexts:
    dF10DcbSystemObjectGroup.setStatus("current")

dF10DcbObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6027, 3, 15, 5, 2, 2)
)
dF10DcbObjectGroup.setObjects(
      *(("DF10-DCB-MIB", "dF10DcbETSAdminStatus"),
        ("DF10-DCB-MIB", "dF10DcbPFCAdminStatus"))
)
if mibBuilder.loadTexts:
    dF10DcbObjectGroup.setStatus("obsolete")

dF10DcbxScalarsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6027, 3, 15, 5, 2, 3)
)
dF10DcbxScalarsGroup.setObjects(
      *(("DF10-DCB-MIB", "dF10DcbxGlobalTraceLevel"),
        ("DF10-DCB-MIB", "dF10DCBXGlobalVersion"))
)
if mibBuilder.loadTexts:
    dF10DcbxScalarsGroup.setStatus("current")

dF10DCBXPortTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6027, 3, 15, 5, 2, 4)
)
dF10DCBXPortTableGroup.setObjects(
      *(("DF10-DCB-MIB", "dF10DCBXAdminStatus"),
        ("DF10-DCB-MIB", "dF10DCBXAutoCfgPortRole"),
        ("DF10-DCB-MIB", "dF10DCBXPortVersion"),
        ("DF10-DCB-MIB", "dF10DCBXPortSupportedTLVs"),
        ("DF10-DCB-MIB", "dF10DCBXPortConfigTLVsTxEnable"),
        ("DF10-DCB-MIB", "dF10DCBXPortOperVersion"),
        ("DF10-DCB-MIB", "dF10DCBXPortPeerMACaddress"),
        ("DF10-DCB-MIB", "dF10DCBXPortCfgSource"),
        ("DF10-DCB-MIB", "dF10DCBXOperStatus"),
        ("DF10-DCB-MIB", "dF10DCBXPortMultiplePeerCount"),
        ("DF10-DCB-MIB", "dF10DCBXPortPeerRemovedCount"),
        ("DF10-DCB-MIB", "dF10DCBXPortPeerOperVersionNum"),
        ("DF10-DCB-MIB", "dF10DCBXPortPeerMaxVersion"),
        ("DF10-DCB-MIB", "dF10DCBXPortSeqNum"),
        ("DF10-DCB-MIB", "dF10DCBXPortAckNum"),
        ("DF10-DCB-MIB", "dF10DCBXPortPeerRcvdAckNum"),
        ("DF10-DCB-MIB", "dF10DCBXPortTxCount"),
        ("DF10-DCB-MIB", "dF10DCBXPortRxCount"),
        ("DF10-DCB-MIB", "dF10DCBXPortErrorFramesCount"))
)
if mibBuilder.loadTexts:
    dF10DCBXPortTableGroup.setStatus("current")

dF10ETSScalarsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6027, 3, 15, 5, 2, 5)
)
dF10ETSScalarsGroup.setObjects(
      *(("DF10-DCB-MIB", "dF10ETSSystemControl"),
        ("DF10-DCB-MIB", "dF10ETSModuleStatus"),
        ("DF10-DCB-MIB", "dF10ETSClearCounters"),
        ("DF10-DCB-MIB", "dF10ETSGlobalEnableTrap"))
)
if mibBuilder.loadTexts:
    dF10ETSScalarsGroup.setStatus("current")

dF10ETSPortTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6027, 3, 15, 5, 2, 6)
)
dF10ETSPortTableGroup.setObjects(
      *(("DF10-DCB-MIB", "dF10ETSAdminMode"),
        ("DF10-DCB-MIB", "dF10ETSDcbxOperState"),
        ("DF10-DCB-MIB", "dF10ETSDcbxStateMachine"),
        ("DF10-DCB-MIB", "dF10ETSOperStatus"),
        ("DF10-DCB-MIB", "dF10ETSClearTLVCounters"),
        ("DF10-DCB-MIB", "dF10ETSConfTxTLVCounter"),
        ("DF10-DCB-MIB", "dF10ETSConfRxTLVCounter"),
        ("DF10-DCB-MIB", "dF10ETSConfRxTLVErrors"),
        ("DF10-DCB-MIB", "dF10ETSRecoTxTLVCounter"),
        ("DF10-DCB-MIB", "dF10ETSRecoRxTLVCounter"),
        ("DF10-DCB-MIB", "dF10ETSRecoRxTLVErrors"))
)
if mibBuilder.loadTexts:
    dF10ETSPortTableGroup.setStatus("current")

dF10PFCScalarsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6027, 3, 15, 5, 2, 7)
)
dF10PFCScalarsGroup.setObjects(
      *(("DF10-DCB-MIB", "dF10PFCSystemControl"),
        ("DF10-DCB-MIB", "dF10PFCModuleStatus"),
        ("DF10-DCB-MIB", "dF10PFCClearCounters"),
        ("DF10-DCB-MIB", "dF10PFCGlobalEnableTrap"))
)
if mibBuilder.loadTexts:
    dF10PFCScalarsGroup.setStatus("current")

dF10PFCPortTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6027, 3, 15, 5, 2, 8)
)
dF10PFCPortTableGroup.setObjects(
      *(("DF10-DCB-MIB", "dF10PFCAdminMode"),
        ("DF10-DCB-MIB", "dF10PFCDcbxOperState"),
        ("DF10-DCB-MIB", "dF10PFCDcbxStateMachine"),
        ("DF10-DCB-MIB", "dF10PFCOperStatus"),
        ("DF10-DCB-MIB", "dF10PFCClearTLVCounters"),
        ("DF10-DCB-MIB", "dF10PFCTxTLVCounter"),
        ("DF10-DCB-MIB", "dF10PFCRxTLVCounter"),
        ("DF10-DCB-MIB", "dF10PFCRxTLVErrors"))
)
if mibBuilder.loadTexts:
    dF10PFCPortTableGroup.setStatus("current")

dF10DCBNotificationObjectsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6027, 3, 15, 5, 2, 9)
)
dF10DCBNotificationObjectsGroup.setObjects(
      *(("DF10-DCB-MIB", "dF10DcbTrapPortNumber"),
        ("DF10-DCB-MIB", "dF10DcbPeerUpStatus"))
)
if mibBuilder.loadTexts:
    dF10DCBNotificationObjectsGroup.setStatus("current")


# Notification objects

dF10ETSModuleStatusTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 6027, 3, 15, 4, 0, 1)
)
dF10ETSModuleStatusTrap.setObjects(
    ("DF10-DCB-MIB", "dF10ETSModuleStatus")
)
if mibBuilder.loadTexts:
    dF10ETSModuleStatusTrap.setStatus(
        "current"
    )

dF10ETSPortAdminStatusTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 6027, 3, 15, 4, 0, 2)
)
dF10ETSPortAdminStatusTrap.setObjects(
      *(("DF10-DCB-MIB", "dF10DcbTrapPortNumber"),
        ("DF10-DCB-MIB", "dF10ETSAdminMode"))
)
if mibBuilder.loadTexts:
    dF10ETSPortAdminStatusTrap.setStatus(
        "current"
    )

dF10ETSPortPeerStatusTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 6027, 3, 15, 4, 0, 3)
)
dF10ETSPortPeerStatusTrap.setObjects(
      *(("DF10-DCB-MIB", "dF10DcbTrapPortNumber"),
        ("DF10-DCB-MIB", "dF10DcbPeerUpStatus"))
)
if mibBuilder.loadTexts:
    dF10ETSPortPeerStatusTrap.setStatus(
        "current"
    )

dF10ETSPortDcbxOperStateTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 6027, 3, 15, 4, 0, 4)
)
dF10ETSPortDcbxOperStateTrap.setObjects(
      *(("DF10-DCB-MIB", "dF10DcbTrapPortNumber"),
        ("DF10-DCB-MIB", "dF10ETSDcbxOperState"))
)
if mibBuilder.loadTexts:
    dF10ETSPortDcbxOperStateTrap.setStatus(
        "current"
    )

dF10PFCModuleStatusTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 6027, 3, 15, 4, 0, 5)
)
dF10PFCModuleStatusTrap.setObjects(
    ("DF10-DCB-MIB", "dF10PFCModuleStatus")
)
if mibBuilder.loadTexts:
    dF10PFCModuleStatusTrap.setStatus(
        "current"
    )

dF10PFCPortAdminStatusTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 6027, 3, 15, 4, 0, 6)
)
dF10PFCPortAdminStatusTrap.setObjects(
      *(("DF10-DCB-MIB", "dF10DcbTrapPortNumber"),
        ("DF10-DCB-MIB", "dF10PFCAdminMode"))
)
if mibBuilder.loadTexts:
    dF10PFCPortAdminStatusTrap.setStatus(
        "current"
    )

dF10PFCPortPeerStatusTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 6027, 3, 15, 4, 0, 7)
)
dF10PFCPortPeerStatusTrap.setObjects(
      *(("DF10-DCB-MIB", "dF10DcbTrapPortNumber"),
        ("DF10-DCB-MIB", "dF10DcbPeerUpStatus"))
)
if mibBuilder.loadTexts:
    dF10PFCPortPeerStatusTrap.setStatus(
        "current"
    )

dF10PFCPortDcbxOperStateTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 6027, 3, 15, 4, 0, 8)
)
dF10PFCPortDcbxOperStateTrap.setObjects(
      *(("DF10-DCB-MIB", "dF10DcbTrapPortNumber"),
        ("DF10-DCB-MIB", "dF10PFCDcbxOperState"))
)
if mibBuilder.loadTexts:
    dF10PFCPortDcbxOperStateTrap.setStatus(
        "current"
    )


# Notifications groups

dF10DCBNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6027, 3, 15, 5, 2, 10)
)
dF10DCBNotificationsGroup.setObjects(
      *(("DF10-DCB-MIB", "dF10ETSModuleStatusTrap"),
        ("DF10-DCB-MIB", "dF10ETSPortAdminStatusTrap"),
        ("DF10-DCB-MIB", "dF10ETSPortPeerStatusTrap"),
        ("DF10-DCB-MIB", "dF10ETSPortDcbxOperStateTrap"),
        ("DF10-DCB-MIB", "dF10PFCModuleStatusTrap"),
        ("DF10-DCB-MIB", "dF10PFCPortAdminStatusTrap"),
        ("DF10-DCB-MIB", "dF10PFCPortPeerStatusTrap"),
        ("DF10-DCB-MIB", "dF10PFCPortDcbxOperStateTrap"))
)
if mibBuilder.loadTexts:
    dF10DCBNotificationsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

dF10DCBMibComplianceRev1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6027, 3, 15, 5, 1, 1)
)
if mibBuilder.loadTexts:
    dF10DCBMibComplianceRev1.setStatus(
        "current"
    )

dF10DCBMibCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6027, 3, 15, 5, 1, 2)
)
if mibBuilder.loadTexts:
    dF10DCBMibCompliance.setStatus(
        "obsolete"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DF10-DCB-MIB",
    **{"EnabledStatus": EnabledStatus,
       "DcbAdminMode": DcbAdminMode,
       "DcbState": DcbState,
       "DcbStateMachineType": DcbStateMachineType,
       "DcbxPortRole": DcbxPortRole,
       "DcbxVersion": DcbxVersion,
       "dF10Dcb": dF10Dcb,
       "dF10DcbSystem": dF10DcbSystem,
       "dF10DcbPfcMinThreshold": dF10DcbPfcMinThreshold,
       "dF10DcbPfcMaxThreshold": dF10DcbPfcMaxThreshold,
       "dF10DcbMaxPfcProfiles": dF10DcbMaxPfcProfiles,
       "dF10DcbObjects": dF10DcbObjects,
       "dF10DcbPortTable": dF10DcbPortTable,
       "dF10DcbPortEntry": dF10DcbPortEntry,
       "dF10DcbPortNumber": dF10DcbPortNumber,
       "dF10DcbETSAdminStatus": dF10DcbETSAdminStatus,
       "dF10DcbPFCAdminStatus": dF10DcbPFCAdminStatus,
       "dF10DcbApplicationObjects": dF10DcbApplicationObjects,
       "dF10DCBXObjects": dF10DCBXObjects,
       "dF10DCBXScalars": dF10DCBXScalars,
       "dF10DcbxGlobalTraceLevel": dF10DcbxGlobalTraceLevel,
       "dF10DCBXGlobalVersion": dF10DCBXGlobalVersion,
       "dF10DCBXPortTable": dF10DCBXPortTable,
       "dF10DCBXPortEntry": dF10DCBXPortEntry,
       "dF10DCBXPortNumber": dF10DCBXPortNumber,
       "dF10DCBXAdminStatus": dF10DCBXAdminStatus,
       "dF10DCBXAutoCfgPortRole": dF10DCBXAutoCfgPortRole,
       "dF10DCBXPortVersion": dF10DCBXPortVersion,
       "dF10DCBXPortSupportedTLVs": dF10DCBXPortSupportedTLVs,
       "dF10DCBXPortConfigTLVsTxEnable": dF10DCBXPortConfigTLVsTxEnable,
       "dF10DCBXPortStatusTable": dF10DCBXPortStatusTable,
       "dF10DCBXPortStatusEntry": dF10DCBXPortStatusEntry,
       "dF10DCBXPortOperVersion": dF10DCBXPortOperVersion,
       "dF10DCBXPortPeerMACaddress": dF10DCBXPortPeerMACaddress,
       "dF10DCBXPortCfgSource": dF10DCBXPortCfgSource,
       "dF10DCBXOperStatus": dF10DCBXOperStatus,
       "dF10DCBXPortMultiplePeerCount": dF10DCBXPortMultiplePeerCount,
       "dF10DCBXPortPeerRemovedCount": dF10DCBXPortPeerRemovedCount,
       "dF10DCBXPortPeerOperVersionNum": dF10DCBXPortPeerOperVersionNum,
       "dF10DCBXPortPeerMaxVersion": dF10DCBXPortPeerMaxVersion,
       "dF10DCBXPortSeqNum": dF10DCBXPortSeqNum,
       "dF10DCBXPortAckNum": dF10DCBXPortAckNum,
       "dF10DCBXPortPeerRcvdAckNum": dF10DCBXPortPeerRcvdAckNum,
       "dF10DCBXPortTxCount": dF10DCBXPortTxCount,
       "dF10DCBXPortRxCount": dF10DCBXPortRxCount,
       "dF10DCBXPortErrorFramesCount": dF10DCBXPortErrorFramesCount,
       "dF10ETSObjects": dF10ETSObjects,
       "dF10ETSScalars": dF10ETSScalars,
       "dF10ETSSystemControl": dF10ETSSystemControl,
       "dF10ETSModuleStatus": dF10ETSModuleStatus,
       "dF10ETSClearCounters": dF10ETSClearCounters,
       "dF10ETSGlobalEnableTrap": dF10ETSGlobalEnableTrap,
       "dF10ETSPortTable": dF10ETSPortTable,
       "dF10ETSPortEntry": dF10ETSPortEntry,
       "dF10ETSPortNumber": dF10ETSPortNumber,
       "dF10ETSAdminMode": dF10ETSAdminMode,
       "dF10ETSDcbxOperState": dF10ETSDcbxOperState,
       "dF10ETSDcbxStateMachine": dF10ETSDcbxStateMachine,
       "dF10ETSOperStatus": dF10ETSOperStatus,
       "dF10ETSClearTLVCounters": dF10ETSClearTLVCounters,
       "dF10ETSConfTxTLVCounter": dF10ETSConfTxTLVCounter,
       "dF10ETSConfRxTLVCounter": dF10ETSConfRxTLVCounter,
       "dF10ETSConfRxTLVErrors": dF10ETSConfRxTLVErrors,
       "dF10ETSRecoTxTLVCounter": dF10ETSRecoTxTLVCounter,
       "dF10ETSRecoRxTLVCounter": dF10ETSRecoRxTLVCounter,
       "dF10ETSRecoRxTLVErrors": dF10ETSRecoRxTLVErrors,
       "dF10PFCObjects": dF10PFCObjects,
       "dF10PFCScalars": dF10PFCScalars,
       "dF10PFCSystemControl": dF10PFCSystemControl,
       "dF10PFCModuleStatus": dF10PFCModuleStatus,
       "dF10PFCClearCounters": dF10PFCClearCounters,
       "dF10PFCGlobalEnableTrap": dF10PFCGlobalEnableTrap,
       "dF10PFCPortTable": dF10PFCPortTable,
       "dF10PFCPortEntry": dF10PFCPortEntry,
       "dF10PFCPortNumber": dF10PFCPortNumber,
       "dF10PFCAdminMode": dF10PFCAdminMode,
       "dF10PFCDcbxOperState": dF10PFCDcbxOperState,
       "dF10PFCDcbxStateMachine": dF10PFCDcbxStateMachine,
       "dF10PFCOperStatus": dF10PFCOperStatus,
       "dF10PFCClearTLVCounters": dF10PFCClearTLVCounters,
       "dF10PFCTxTLVCounter": dF10PFCTxTLVCounter,
       "dF10PFCRxTLVCounter": dF10PFCRxTLVCounter,
       "dF10PFCRxTLVErrors": dF10PFCRxTLVErrors,
       "dF10DcbNotificationObjects": dF10DcbNotificationObjects,
       "dF10DCBTraps": dF10DCBTraps,
       "dF10ETSModuleStatusTrap": dF10ETSModuleStatusTrap,
       "dF10ETSPortAdminStatusTrap": dF10ETSPortAdminStatusTrap,
       "dF10ETSPortPeerStatusTrap": dF10ETSPortPeerStatusTrap,
       "dF10ETSPortDcbxOperStateTrap": dF10ETSPortDcbxOperStateTrap,
       "dF10PFCModuleStatusTrap": dF10PFCModuleStatusTrap,
       "dF10PFCPortAdminStatusTrap": dF10PFCPortAdminStatusTrap,
       "dF10PFCPortPeerStatusTrap": dF10PFCPortPeerStatusTrap,
       "dF10PFCPortDcbxOperStateTrap": dF10PFCPortDcbxOperStateTrap,
       "dF10DCBTrapObjects": dF10DCBTrapObjects,
       "dF10DcbTrapPortNumber": dF10DcbTrapPortNumber,
       "dF10DcbPeerUpStatus": dF10DcbPeerUpStatus,
       "dF10DCBMibConformance": dF10DCBMibConformance,
       "dF10DCBMibCompliances": dF10DCBMibCompliances,
       "dF10DCBMibComplianceRev1": dF10DCBMibComplianceRev1,
       "dF10DCBMibCompliance": dF10DCBMibCompliance,
       "dF10DCBMibGroups": dF10DCBMibGroups,
       "dF10DcbSystemObjectGroup": dF10DcbSystemObjectGroup,
       "dF10DcbObjectGroup": dF10DcbObjectGroup,
       "dF10DcbxScalarsGroup": dF10DcbxScalarsGroup,
       "dF10DCBXPortTableGroup": dF10DCBXPortTableGroup,
       "dF10ETSScalarsGroup": dF10ETSScalarsGroup,
       "dF10ETSPortTableGroup": dF10ETSPortTableGroup,
       "dF10PFCScalarsGroup": dF10PFCScalarsGroup,
       "dF10PFCPortTableGroup": dF10PFCPortTableGroup,
       "dF10DCBNotificationObjectsGroup": dF10DCBNotificationObjectsGroup,
       "dF10DCBNotificationsGroup": dF10DCBNotificationsGroup}
)
