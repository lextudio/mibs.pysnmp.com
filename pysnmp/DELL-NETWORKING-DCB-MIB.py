# SNMP MIB module (DELL-NETWORKING-DCB-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/DELL-NETWORKING-DCB-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:23:51 2024
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

(dellNetMgmt,) = mibBuilder.importSymbols(
    "DELL-NETWORKING-SMI",
    "dellNetMgmt")

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

dellNetDcb = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 3, 15)
)
dellNetDcb.setRevisions(
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

_DellNetDcbSystem_ObjectIdentity = ObjectIdentity
dellNetDcbSystem = _DellNetDcbSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 3, 15, 1)
)


class _DellNetDcbPfcMinThreshold_Type(Unsigned32):
    """Custom type dellNetDcbPfcMinThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_DellNetDcbPfcMinThreshold_Type.__name__ = "Unsigned32"
_DellNetDcbPfcMinThreshold_Object = MibScalar
dellNetDcbPfcMinThreshold = _DellNetDcbPfcMinThreshold_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 15, 1, 1),
    _DellNetDcbPfcMinThreshold_Type()
)
dellNetDcbPfcMinThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetDcbPfcMinThreshold.setStatus("current")


class _DellNetDcbPfcMaxThreshold_Type(Unsigned32):
    """Custom type dellNetDcbPfcMaxThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_DellNetDcbPfcMaxThreshold_Type.__name__ = "Unsigned32"
_DellNetDcbPfcMaxThreshold_Object = MibScalar
dellNetDcbPfcMaxThreshold = _DellNetDcbPfcMaxThreshold_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 15, 1, 2),
    _DellNetDcbPfcMaxThreshold_Type()
)
dellNetDcbPfcMaxThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetDcbPfcMaxThreshold.setStatus("current")


class _DellNetDcbMaxPfcProfiles_Type(Unsigned32):
    """Custom type dellNetDcbMaxPfcProfiles based on Unsigned32"""
    defaultValue = 256

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_DellNetDcbMaxPfcProfiles_Type.__name__ = "Unsigned32"
_DellNetDcbMaxPfcProfiles_Object = MibScalar
dellNetDcbMaxPfcProfiles = _DellNetDcbMaxPfcProfiles_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 15, 1, 3),
    _DellNetDcbMaxPfcProfiles_Type()
)
dellNetDcbMaxPfcProfiles.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetDcbMaxPfcProfiles.setStatus("current")
_DellNetDcbObjects_ObjectIdentity = ObjectIdentity
dellNetDcbObjects = _DellNetDcbObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 3, 15, 2)
)
_DellNetDcbPortTable_Object = MibTable
dellNetDcbPortTable = _DellNetDcbPortTable_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 15, 2, 1)
)
if mibBuilder.loadTexts:
    dellNetDcbPortTable.setStatus("obsolete")
_DellNetDcbPortEntry_Object = MibTableRow
dellNetDcbPortEntry = _DellNetDcbPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 15, 2, 1, 1)
)
dellNetDcbPortEntry.setIndexNames(
    (0, "DELL-NETWORKING-DCB-MIB", "dellNetDcbPortNumber"),
)
if mibBuilder.loadTexts:
    dellNetDcbPortEntry.setStatus("obsolete")
_DellNetDcbPortNumber_Type = InterfaceIndex
_DellNetDcbPortNumber_Object = MibTableColumn
dellNetDcbPortNumber = _DellNetDcbPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 15, 2, 1, 1, 1),
    _DellNetDcbPortNumber_Type()
)
dellNetDcbPortNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dellNetDcbPortNumber.setStatus("obsolete")


class _DellNetDcbETSAdminStatus_Type(EnabledStatus):
    """Custom type dellNetDcbETSAdminStatus based on EnabledStatus"""


_DellNetDcbETSAdminStatus_Object = MibTableColumn
dellNetDcbETSAdminStatus = _DellNetDcbETSAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 15, 2, 1, 1, 2),
    _DellNetDcbETSAdminStatus_Type()
)
dellNetDcbETSAdminStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetDcbETSAdminStatus.setStatus("obsolete")


class _DellNetDcbPFCAdminStatus_Type(EnabledStatus):
    """Custom type dellNetDcbPFCAdminStatus based on EnabledStatus"""


_DellNetDcbPFCAdminStatus_Object = MibTableColumn
dellNetDcbPFCAdminStatus = _DellNetDcbPFCAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 15, 2, 1, 1, 3),
    _DellNetDcbPFCAdminStatus_Type()
)
dellNetDcbPFCAdminStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetDcbPFCAdminStatus.setStatus("obsolete")
_DellNetDcbApplicationObjects_ObjectIdentity = ObjectIdentity
dellNetDcbApplicationObjects = _DellNetDcbApplicationObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 3, 15, 3)
)
_DellNetDCBXObjects_ObjectIdentity = ObjectIdentity
dellNetDCBXObjects = _DellNetDCBXObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 3, 15, 3, 1)
)
_DellNetDCBXScalars_ObjectIdentity = ObjectIdentity
dellNetDCBXScalars = _DellNetDCBXScalars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 3, 15, 3, 1, 1)
)
_DellNetDcbxGlobalTraceLevel_Type = Integer32
_DellNetDcbxGlobalTraceLevel_Object = MibScalar
dellNetDcbxGlobalTraceLevel = _DellNetDcbxGlobalTraceLevel_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 15, 3, 1, 1, 1),
    _DellNetDcbxGlobalTraceLevel_Type()
)
dellNetDcbxGlobalTraceLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dellNetDcbxGlobalTraceLevel.setStatus("current")


class _DellNetDCBXGlobalVersion_Type(DcbxVersion):
    """Custom type dellNetDCBXGlobalVersion based on DcbxVersion"""
    defaultValue = 1


_DellNetDCBXGlobalVersion_Object = MibScalar
dellNetDCBXGlobalVersion = _DellNetDCBXGlobalVersion_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 15, 3, 1, 1, 2),
    _DellNetDCBXGlobalVersion_Type()
)
dellNetDCBXGlobalVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dellNetDCBXGlobalVersion.setStatus("current")
_DellNetDCBXPortTable_Object = MibTable
dellNetDCBXPortTable = _DellNetDCBXPortTable_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 15, 3, 1, 2)
)
if mibBuilder.loadTexts:
    dellNetDCBXPortTable.setStatus("current")
_DellNetDCBXPortEntry_Object = MibTableRow
dellNetDCBXPortEntry = _DellNetDCBXPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 15, 3, 1, 2, 1)
)
dellNetDCBXPortEntry.setIndexNames(
    (0, "DELL-NETWORKING-DCB-MIB", "dellNetDCBXPortNumber"),
)
if mibBuilder.loadTexts:
    dellNetDCBXPortEntry.setStatus("current")
_DellNetDCBXPortNumber_Type = InterfaceIndex
_DellNetDCBXPortNumber_Object = MibTableColumn
dellNetDCBXPortNumber = _DellNetDCBXPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 15, 3, 1, 2, 1, 1),
    _DellNetDCBXPortNumber_Type()
)
dellNetDCBXPortNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dellNetDCBXPortNumber.setStatus("current")


class _DellNetDCBXAdminStatus_Type(EnabledStatus):
    """Custom type dellNetDCBXAdminStatus based on EnabledStatus"""


_DellNetDCBXAdminStatus_Object = MibTableColumn
dellNetDCBXAdminStatus = _DellNetDCBXAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 15, 3, 1, 2, 1, 2),
    _DellNetDCBXAdminStatus_Type()
)
dellNetDCBXAdminStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetDCBXAdminStatus.setStatus("current")


class _DellNetDCBXAutoCfgPortRole_Type(DcbxPortRole):
    """Custom type dellNetDCBXAutoCfgPortRole based on DcbxPortRole"""
    defaultValue = 1


_DellNetDCBXAutoCfgPortRole_Object = MibTableColumn
dellNetDCBXAutoCfgPortRole = _DellNetDCBXAutoCfgPortRole_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 15, 3, 1, 2, 1, 3),
    _DellNetDCBXAutoCfgPortRole_Type()
)
dellNetDCBXAutoCfgPortRole.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dellNetDCBXAutoCfgPortRole.setStatus("current")


class _DellNetDCBXPortVersion_Type(DcbxVersion):
    """Custom type dellNetDCBXPortVersion based on DcbxVersion"""
    defaultValue = 1


_DellNetDCBXPortVersion_Object = MibTableColumn
dellNetDCBXPortVersion = _DellNetDCBXPortVersion_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 15, 3, 1, 2, 1, 4),
    _DellNetDCBXPortVersion_Type()
)
dellNetDCBXPortVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dellNetDCBXPortVersion.setStatus("current")


class _DellNetDCBXPortSupportedTLVs_Type(Bits):
    """Custom type dellNetDCBXPortSupportedTLVs based on Bits"""
    namedValues = NamedValues(
        *(("applicationPriorityFCOE", 3),
          ("applicationPriorityISCSI", 4),
          ("etsConfig", 1),
          ("etsRecom", 2),
          ("pfc", 0))
    )

_DellNetDCBXPortSupportedTLVs_Type.__name__ = "Bits"
_DellNetDCBXPortSupportedTLVs_Object = MibTableColumn
dellNetDCBXPortSupportedTLVs = _DellNetDCBXPortSupportedTLVs_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 15, 3, 1, 2, 1, 5),
    _DellNetDCBXPortSupportedTLVs_Type()
)
dellNetDCBXPortSupportedTLVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetDCBXPortSupportedTLVs.setStatus("current")


class _DellNetDCBXPortConfigTLVsTxEnable_Type(Bits):
    """Custom type dellNetDCBXPortConfigTLVsTxEnable based on Bits"""
    namedValues = NamedValues(
        *(("applicationPriorityFCOE", 3),
          ("applicationPriorityISCSI", 4),
          ("etsConfig", 1),
          ("etsRecom", 2),
          ("pfc", 0))
    )

_DellNetDCBXPortConfigTLVsTxEnable_Type.__name__ = "Bits"
_DellNetDCBXPortConfigTLVsTxEnable_Object = MibTableColumn
dellNetDCBXPortConfigTLVsTxEnable = _DellNetDCBXPortConfigTLVsTxEnable_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 15, 3, 1, 2, 1, 6),
    _DellNetDCBXPortConfigTLVsTxEnable_Type()
)
dellNetDCBXPortConfigTLVsTxEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dellNetDCBXPortConfigTLVsTxEnable.setStatus("current")
_DellNetDCBXPortStatusTable_Object = MibTable
dellNetDCBXPortStatusTable = _DellNetDCBXPortStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 15, 3, 1, 3)
)
if mibBuilder.loadTexts:
    dellNetDCBXPortStatusTable.setStatus("current")
_DellNetDCBXPortStatusEntry_Object = MibTableRow
dellNetDCBXPortStatusEntry = _DellNetDCBXPortStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 15, 3, 1, 3, 1)
)
if mibBuilder.loadTexts:
    dellNetDCBXPortStatusEntry.setStatus("current")


class _DellNetDCBXPortOperVersion_Type(DcbxVersion):
    """Custom type dellNetDCBXPortOperVersion based on DcbxVersion"""
    defaultValue = 1


_DellNetDCBXPortOperVersion_Object = MibTableColumn
dellNetDCBXPortOperVersion = _DellNetDCBXPortOperVersion_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 15, 3, 1, 3, 1, 2),
    _DellNetDCBXPortOperVersion_Type()
)
dellNetDCBXPortOperVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetDCBXPortOperVersion.setStatus("current")
_DellNetDCBXPortPeerMACaddress_Type = MacAddress
_DellNetDCBXPortPeerMACaddress_Object = MibTableColumn
dellNetDCBXPortPeerMACaddress = _DellNetDCBXPortPeerMACaddress_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 15, 3, 1, 3, 1, 3),
    _DellNetDCBXPortPeerMACaddress_Type()
)
dellNetDCBXPortPeerMACaddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetDCBXPortPeerMACaddress.setStatus("current")


class _DellNetDCBXPortCfgSource_Type(Integer32):
    """Custom type dellNetDCBXPortCfgSource based on Integer32"""
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


_DellNetDCBXPortCfgSource_Type.__name__ = "Integer32"
_DellNetDCBXPortCfgSource_Object = MibTableColumn
dellNetDCBXPortCfgSource = _DellNetDCBXPortCfgSource_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 15, 3, 1, 3, 1, 4),
    _DellNetDCBXPortCfgSource_Type()
)
dellNetDCBXPortCfgSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetDCBXPortCfgSource.setStatus("current")
_DellNetDCBXOperStatus_Type = EnabledStatus
_DellNetDCBXOperStatus_Object = MibTableColumn
dellNetDCBXOperStatus = _DellNetDCBXOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 15, 3, 1, 3, 1, 5),
    _DellNetDCBXOperStatus_Type()
)
dellNetDCBXOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetDCBXOperStatus.setStatus("current")
_DellNetDCBXPortMultiplePeerCount_Type = Counter32
_DellNetDCBXPortMultiplePeerCount_Object = MibTableColumn
dellNetDCBXPortMultiplePeerCount = _DellNetDCBXPortMultiplePeerCount_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 15, 3, 1, 3, 1, 6),
    _DellNetDCBXPortMultiplePeerCount_Type()
)
dellNetDCBXPortMultiplePeerCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetDCBXPortMultiplePeerCount.setStatus("current")
_DellNetDCBXPortPeerRemovedCount_Type = Counter32
_DellNetDCBXPortPeerRemovedCount_Object = MibTableColumn
dellNetDCBXPortPeerRemovedCount = _DellNetDCBXPortPeerRemovedCount_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 15, 3, 1, 3, 1, 7),
    _DellNetDCBXPortPeerRemovedCount_Type()
)
dellNetDCBXPortPeerRemovedCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetDCBXPortPeerRemovedCount.setStatus("current")
_DellNetDCBXPortPeerOperVersionNum_Type = Unsigned32
_DellNetDCBXPortPeerOperVersionNum_Object = MibTableColumn
dellNetDCBXPortPeerOperVersionNum = _DellNetDCBXPortPeerOperVersionNum_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 15, 3, 1, 3, 1, 8),
    _DellNetDCBXPortPeerOperVersionNum_Type()
)
dellNetDCBXPortPeerOperVersionNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetDCBXPortPeerOperVersionNum.setStatus("current")
_DellNetDCBXPortPeerMaxVersion_Type = Unsigned32
_DellNetDCBXPortPeerMaxVersion_Object = MibTableColumn
dellNetDCBXPortPeerMaxVersion = _DellNetDCBXPortPeerMaxVersion_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 15, 3, 1, 3, 1, 9),
    _DellNetDCBXPortPeerMaxVersion_Type()
)
dellNetDCBXPortPeerMaxVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetDCBXPortPeerMaxVersion.setStatus("current")
_DellNetDCBXPortSeqNum_Type = Unsigned32
_DellNetDCBXPortSeqNum_Object = MibTableColumn
dellNetDCBXPortSeqNum = _DellNetDCBXPortSeqNum_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 15, 3, 1, 3, 1, 10),
    _DellNetDCBXPortSeqNum_Type()
)
dellNetDCBXPortSeqNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetDCBXPortSeqNum.setStatus("current")
_DellNetDCBXPortAckNum_Type = Unsigned32
_DellNetDCBXPortAckNum_Object = MibTableColumn
dellNetDCBXPortAckNum = _DellNetDCBXPortAckNum_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 15, 3, 1, 3, 1, 11),
    _DellNetDCBXPortAckNum_Type()
)
dellNetDCBXPortAckNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetDCBXPortAckNum.setStatus("current")
_DellNetDCBXPortPeerRcvdAckNum_Type = Unsigned32
_DellNetDCBXPortPeerRcvdAckNum_Object = MibTableColumn
dellNetDCBXPortPeerRcvdAckNum = _DellNetDCBXPortPeerRcvdAckNum_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 15, 3, 1, 3, 1, 12),
    _DellNetDCBXPortPeerRcvdAckNum_Type()
)
dellNetDCBXPortPeerRcvdAckNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetDCBXPortPeerRcvdAckNum.setStatus("current")
_DellNetDCBXPortTxCount_Type = Counter32
_DellNetDCBXPortTxCount_Object = MibTableColumn
dellNetDCBXPortTxCount = _DellNetDCBXPortTxCount_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 15, 3, 1, 3, 1, 13),
    _DellNetDCBXPortTxCount_Type()
)
dellNetDCBXPortTxCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetDCBXPortTxCount.setStatus("current")
_DellNetDCBXPortRxCount_Type = Counter32
_DellNetDCBXPortRxCount_Object = MibTableColumn
dellNetDCBXPortRxCount = _DellNetDCBXPortRxCount_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 15, 3, 1, 3, 1, 14),
    _DellNetDCBXPortRxCount_Type()
)
dellNetDCBXPortRxCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetDCBXPortRxCount.setStatus("current")
_DellNetDCBXPortErrorFramesCount_Type = Counter32
_DellNetDCBXPortErrorFramesCount_Object = MibTableColumn
dellNetDCBXPortErrorFramesCount = _DellNetDCBXPortErrorFramesCount_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 15, 3, 1, 3, 1, 15),
    _DellNetDCBXPortErrorFramesCount_Type()
)
dellNetDCBXPortErrorFramesCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetDCBXPortErrorFramesCount.setStatus("current")
_DellNetETSObjects_ObjectIdentity = ObjectIdentity
dellNetETSObjects = _DellNetETSObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 3, 15, 3, 2)
)
_DellNetETSScalars_ObjectIdentity = ObjectIdentity
dellNetETSScalars = _DellNetETSScalars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 3, 15, 3, 2, 1)
)


class _DellNetETSSystemControl_Type(Integer32):
    """Custom type dellNetETSSystemControl based on Integer32"""
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


_DellNetETSSystemControl_Type.__name__ = "Integer32"
_DellNetETSSystemControl_Object = MibScalar
dellNetETSSystemControl = _DellNetETSSystemControl_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 15, 3, 2, 1, 1),
    _DellNetETSSystemControl_Type()
)
dellNetETSSystemControl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetETSSystemControl.setStatus("current")


class _DellNetETSModuleStatus_Type(EnabledStatus):
    """Custom type dellNetETSModuleStatus based on EnabledStatus"""


_DellNetETSModuleStatus_Object = MibScalar
dellNetETSModuleStatus = _DellNetETSModuleStatus_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 15, 3, 2, 1, 2),
    _DellNetETSModuleStatus_Type()
)
dellNetETSModuleStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetETSModuleStatus.setStatus("current")


class _DellNetETSClearCounters_Type(TruthValue):
    """Custom type dellNetETSClearCounters based on TruthValue"""


_DellNetETSClearCounters_Object = MibScalar
dellNetETSClearCounters = _DellNetETSClearCounters_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 15, 3, 2, 1, 3),
    _DellNetETSClearCounters_Type()
)
dellNetETSClearCounters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dellNetETSClearCounters.setStatus("current")


class _DellNetETSGlobalEnableTrap_Type(Integer32):
    """Custom type dellNetETSGlobalEnableTrap based on Integer32"""
    defaultValue = 0


_DellNetETSGlobalEnableTrap_Object = MibScalar
dellNetETSGlobalEnableTrap = _DellNetETSGlobalEnableTrap_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 15, 3, 2, 1, 4),
    _DellNetETSGlobalEnableTrap_Type()
)
dellNetETSGlobalEnableTrap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetETSGlobalEnableTrap.setStatus("current")
_DellNetETSPortTable_Object = MibTable
dellNetETSPortTable = _DellNetETSPortTable_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 15, 3, 2, 2)
)
if mibBuilder.loadTexts:
    dellNetETSPortTable.setStatus("current")
_DellNetETSPortEntry_Object = MibTableRow
dellNetETSPortEntry = _DellNetETSPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 15, 3, 2, 2, 1)
)
dellNetETSPortEntry.setIndexNames(
    (0, "DELL-NETWORKING-DCB-MIB", "dellNetETSPortNumber"),
)
if mibBuilder.loadTexts:
    dellNetETSPortEntry.setStatus("current")
_DellNetETSPortNumber_Type = InterfaceIndex
_DellNetETSPortNumber_Object = MibTableColumn
dellNetETSPortNumber = _DellNetETSPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 15, 3, 2, 2, 1, 1),
    _DellNetETSPortNumber_Type()
)
dellNetETSPortNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dellNetETSPortNumber.setStatus("current")


class _DellNetETSAdminMode_Type(DcbAdminMode):
    """Custom type dellNetETSAdminMode based on DcbAdminMode"""


_DellNetETSAdminMode_Object = MibTableColumn
dellNetETSAdminMode = _DellNetETSAdminMode_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 15, 3, 2, 2, 1, 2),
    _DellNetETSAdminMode_Type()
)
dellNetETSAdminMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetETSAdminMode.setStatus("current")
_DellNetETSDcbxOperState_Type = DcbState
_DellNetETSDcbxOperState_Object = MibTableColumn
dellNetETSDcbxOperState = _DellNetETSDcbxOperState_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 15, 3, 2, 2, 1, 3),
    _DellNetETSDcbxOperState_Type()
)
dellNetETSDcbxOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetETSDcbxOperState.setStatus("current")
_DellNetETSDcbxStateMachine_Type = DcbStateMachineType
_DellNetETSDcbxStateMachine_Object = MibTableColumn
dellNetETSDcbxStateMachine = _DellNetETSDcbxStateMachine_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 15, 3, 2, 2, 1, 4),
    _DellNetETSDcbxStateMachine_Type()
)
dellNetETSDcbxStateMachine.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetETSDcbxStateMachine.setStatus("current")
_DellNetETSOperStatus_Type = EnabledStatus
_DellNetETSOperStatus_Object = MibTableColumn
dellNetETSOperStatus = _DellNetETSOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 15, 3, 2, 2, 1, 5),
    _DellNetETSOperStatus_Type()
)
dellNetETSOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetETSOperStatus.setStatus("current")


class _DellNetETSClearTLVCounters_Type(TruthValue):
    """Custom type dellNetETSClearTLVCounters based on TruthValue"""


_DellNetETSClearTLVCounters_Object = MibTableColumn
dellNetETSClearTLVCounters = _DellNetETSClearTLVCounters_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 15, 3, 2, 2, 1, 6),
    _DellNetETSClearTLVCounters_Type()
)
dellNetETSClearTLVCounters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dellNetETSClearTLVCounters.setStatus("current")
_DellNetETSConfTxTLVCounter_Type = Counter32
_DellNetETSConfTxTLVCounter_Object = MibTableColumn
dellNetETSConfTxTLVCounter = _DellNetETSConfTxTLVCounter_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 15, 3, 2, 2, 1, 7),
    _DellNetETSConfTxTLVCounter_Type()
)
dellNetETSConfTxTLVCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetETSConfTxTLVCounter.setStatus("current")
_DellNetETSConfRxTLVCounter_Type = Counter32
_DellNetETSConfRxTLVCounter_Object = MibTableColumn
dellNetETSConfRxTLVCounter = _DellNetETSConfRxTLVCounter_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 15, 3, 2, 2, 1, 8),
    _DellNetETSConfRxTLVCounter_Type()
)
dellNetETSConfRxTLVCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetETSConfRxTLVCounter.setStatus("current")
_DellNetETSConfRxTLVErrors_Type = Counter32
_DellNetETSConfRxTLVErrors_Object = MibTableColumn
dellNetETSConfRxTLVErrors = _DellNetETSConfRxTLVErrors_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 15, 3, 2, 2, 1, 9),
    _DellNetETSConfRxTLVErrors_Type()
)
dellNetETSConfRxTLVErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetETSConfRxTLVErrors.setStatus("current")
_DellNetETSRecoTxTLVCounter_Type = Counter32
_DellNetETSRecoTxTLVCounter_Object = MibTableColumn
dellNetETSRecoTxTLVCounter = _DellNetETSRecoTxTLVCounter_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 15, 3, 2, 2, 1, 10),
    _DellNetETSRecoTxTLVCounter_Type()
)
dellNetETSRecoTxTLVCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetETSRecoTxTLVCounter.setStatus("current")
_DellNetETSRecoRxTLVCounter_Type = Counter32
_DellNetETSRecoRxTLVCounter_Object = MibTableColumn
dellNetETSRecoRxTLVCounter = _DellNetETSRecoRxTLVCounter_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 15, 3, 2, 2, 1, 11),
    _DellNetETSRecoRxTLVCounter_Type()
)
dellNetETSRecoRxTLVCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetETSRecoRxTLVCounter.setStatus("current")
_DellNetETSRecoRxTLVErrors_Type = Counter32
_DellNetETSRecoRxTLVErrors_Object = MibTableColumn
dellNetETSRecoRxTLVErrors = _DellNetETSRecoRxTLVErrors_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 15, 3, 2, 2, 1, 12),
    _DellNetETSRecoRxTLVErrors_Type()
)
dellNetETSRecoRxTLVErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetETSRecoRxTLVErrors.setStatus("current")
_DellNetPFCObjects_ObjectIdentity = ObjectIdentity
dellNetPFCObjects = _DellNetPFCObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 3, 15, 3, 3)
)
_DellNetPFCScalars_ObjectIdentity = ObjectIdentity
dellNetPFCScalars = _DellNetPFCScalars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 3, 15, 3, 3, 1)
)


class _DellNetPFCSystemControl_Type(Integer32):
    """Custom type dellNetPFCSystemControl based on Integer32"""
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


_DellNetPFCSystemControl_Type.__name__ = "Integer32"
_DellNetPFCSystemControl_Object = MibScalar
dellNetPFCSystemControl = _DellNetPFCSystemControl_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 15, 3, 3, 1, 1),
    _DellNetPFCSystemControl_Type()
)
dellNetPFCSystemControl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetPFCSystemControl.setStatus("current")


class _DellNetPFCModuleStatus_Type(EnabledStatus):
    """Custom type dellNetPFCModuleStatus based on EnabledStatus"""


_DellNetPFCModuleStatus_Object = MibScalar
dellNetPFCModuleStatus = _DellNetPFCModuleStatus_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 15, 3, 3, 1, 2),
    _DellNetPFCModuleStatus_Type()
)
dellNetPFCModuleStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetPFCModuleStatus.setStatus("current")


class _DellNetPFCClearCounters_Type(TruthValue):
    """Custom type dellNetPFCClearCounters based on TruthValue"""


_DellNetPFCClearCounters_Object = MibScalar
dellNetPFCClearCounters = _DellNetPFCClearCounters_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 15, 3, 3, 1, 3),
    _DellNetPFCClearCounters_Type()
)
dellNetPFCClearCounters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dellNetPFCClearCounters.setStatus("current")


class _DellNetPFCGlobalEnableTrap_Type(Integer32):
    """Custom type dellNetPFCGlobalEnableTrap based on Integer32"""
    defaultValue = 0


_DellNetPFCGlobalEnableTrap_Object = MibScalar
dellNetPFCGlobalEnableTrap = _DellNetPFCGlobalEnableTrap_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 15, 3, 3, 1, 4),
    _DellNetPFCGlobalEnableTrap_Type()
)
dellNetPFCGlobalEnableTrap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetPFCGlobalEnableTrap.setStatus("current")
_DellNetPFCPortTable_Object = MibTable
dellNetPFCPortTable = _DellNetPFCPortTable_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 15, 3, 3, 2)
)
if mibBuilder.loadTexts:
    dellNetPFCPortTable.setStatus("current")
_DellNetPFCPortEntry_Object = MibTableRow
dellNetPFCPortEntry = _DellNetPFCPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 15, 3, 3, 2, 1)
)
dellNetPFCPortEntry.setIndexNames(
    (0, "DELL-NETWORKING-DCB-MIB", "dellNetPFCPortNumber"),
)
if mibBuilder.loadTexts:
    dellNetPFCPortEntry.setStatus("current")
_DellNetPFCPortNumber_Type = InterfaceIndex
_DellNetPFCPortNumber_Object = MibTableColumn
dellNetPFCPortNumber = _DellNetPFCPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 15, 3, 3, 2, 1, 1),
    _DellNetPFCPortNumber_Type()
)
dellNetPFCPortNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dellNetPFCPortNumber.setStatus("current")


class _DellNetPFCAdminMode_Type(DcbAdminMode):
    """Custom type dellNetPFCAdminMode based on DcbAdminMode"""


_DellNetPFCAdminMode_Object = MibTableColumn
dellNetPFCAdminMode = _DellNetPFCAdminMode_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 15, 3, 3, 2, 1, 2),
    _DellNetPFCAdminMode_Type()
)
dellNetPFCAdminMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetPFCAdminMode.setStatus("current")
_DellNetPFCDcbxOperState_Type = DcbState
_DellNetPFCDcbxOperState_Object = MibTableColumn
dellNetPFCDcbxOperState = _DellNetPFCDcbxOperState_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 15, 3, 3, 2, 1, 3),
    _DellNetPFCDcbxOperState_Type()
)
dellNetPFCDcbxOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetPFCDcbxOperState.setStatus("current")
_DellNetPFCDcbxStateMachine_Type = DcbStateMachineType
_DellNetPFCDcbxStateMachine_Object = MibTableColumn
dellNetPFCDcbxStateMachine = _DellNetPFCDcbxStateMachine_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 15, 3, 3, 2, 1, 4),
    _DellNetPFCDcbxStateMachine_Type()
)
dellNetPFCDcbxStateMachine.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetPFCDcbxStateMachine.setStatus("current")
_DellNetPFCOperStatus_Type = EnabledStatus
_DellNetPFCOperStatus_Object = MibTableColumn
dellNetPFCOperStatus = _DellNetPFCOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 15, 3, 3, 2, 1, 5),
    _DellNetPFCOperStatus_Type()
)
dellNetPFCOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetPFCOperStatus.setStatus("current")


class _DellNetPFCClearTLVCounters_Type(TruthValue):
    """Custom type dellNetPFCClearTLVCounters based on TruthValue"""


_DellNetPFCClearTLVCounters_Object = MibTableColumn
dellNetPFCClearTLVCounters = _DellNetPFCClearTLVCounters_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 15, 3, 3, 2, 1, 6),
    _DellNetPFCClearTLVCounters_Type()
)
dellNetPFCClearTLVCounters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dellNetPFCClearTLVCounters.setStatus("current")
_DellNetPFCTxTLVCounter_Type = Counter32
_DellNetPFCTxTLVCounter_Object = MibTableColumn
dellNetPFCTxTLVCounter = _DellNetPFCTxTLVCounter_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 15, 3, 3, 2, 1, 7),
    _DellNetPFCTxTLVCounter_Type()
)
dellNetPFCTxTLVCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetPFCTxTLVCounter.setStatus("current")
_DellNetPFCRxTLVCounter_Type = Counter32
_DellNetPFCRxTLVCounter_Object = MibTableColumn
dellNetPFCRxTLVCounter = _DellNetPFCRxTLVCounter_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 15, 3, 3, 2, 1, 8),
    _DellNetPFCRxTLVCounter_Type()
)
dellNetPFCRxTLVCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetPFCRxTLVCounter.setStatus("current")
_DellNetPFCRxTLVErrors_Type = Counter32
_DellNetPFCRxTLVErrors_Object = MibTableColumn
dellNetPFCRxTLVErrors = _DellNetPFCRxTLVErrors_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 15, 3, 3, 2, 1, 9),
    _DellNetPFCRxTLVErrors_Type()
)
dellNetPFCRxTLVErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetPFCRxTLVErrors.setStatus("current")
_DellNetDcbNotificationObjects_ObjectIdentity = ObjectIdentity
dellNetDcbNotificationObjects = _DellNetDcbNotificationObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 3, 15, 4)
)
_DellNetDCBTraps_ObjectIdentity = ObjectIdentity
dellNetDCBTraps = _DellNetDCBTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 3, 15, 4, 0)
)
_DellNetDCBTrapObjects_ObjectIdentity = ObjectIdentity
dellNetDCBTrapObjects = _DellNetDCBTrapObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 3, 15, 4, 1)
)
_DellNetDcbTrapPortNumber_Type = TruthValue
_DellNetDcbTrapPortNumber_Object = MibScalar
dellNetDcbTrapPortNumber = _DellNetDcbTrapPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 15, 4, 1, 1),
    _DellNetDcbTrapPortNumber_Type()
)
dellNetDcbTrapPortNumber.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    dellNetDcbTrapPortNumber.setStatus("current")
_DellNetDcbPeerUpStatus_Type = TruthValue
_DellNetDcbPeerUpStatus_Object = MibScalar
dellNetDcbPeerUpStatus = _DellNetDcbPeerUpStatus_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 15, 4, 1, 2),
    _DellNetDcbPeerUpStatus_Type()
)
dellNetDcbPeerUpStatus.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    dellNetDcbPeerUpStatus.setStatus("current")
_DellNetDCBMibConformance_ObjectIdentity = ObjectIdentity
dellNetDCBMibConformance = _DellNetDCBMibConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 3, 15, 5)
)
_DellNetDCBMibCompliances_ObjectIdentity = ObjectIdentity
dellNetDCBMibCompliances = _DellNetDCBMibCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 3, 15, 5, 1)
)
_DellNetDCBMibGroups_ObjectIdentity = ObjectIdentity
dellNetDCBMibGroups = _DellNetDCBMibGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 3, 15, 5, 2)
)
dellNetDCBXPortEntry.registerAugmentions(
    ("DELL-NETWORKING-DCB-MIB",
     "dellNetDCBXPortStatusEntry")
)
dellNetDCBXPortStatusEntry.setIndexNames(*dellNetDCBXPortEntry.getIndexNames())

# Managed Objects groups

dellNetDcbSystemObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6027, 3, 15, 5, 2, 1)
)
dellNetDcbSystemObjectGroup.setObjects(
      *(("DELL-NETWORKING-DCB-MIB", "dellNetDcbPfcMinThreshold"),
        ("DELL-NETWORKING-DCB-MIB", "dellNetDcbPfcMaxThreshold"),
        ("DELL-NETWORKING-DCB-MIB", "dellNetDcbMaxPfcProfiles"))
)
if mibBuilder.loadTexts:
    dellNetDcbSystemObjectGroup.setStatus("current")

dellNetDcbObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6027, 3, 15, 5, 2, 2)
)
dellNetDcbObjectGroup.setObjects(
      *(("DELL-NETWORKING-DCB-MIB", "dellNetDcbETSAdminStatus"),
        ("DELL-NETWORKING-DCB-MIB", "dellNetDcbPFCAdminStatus"))
)
if mibBuilder.loadTexts:
    dellNetDcbObjectGroup.setStatus("obsolete")

dellNetDcbxScalarsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6027, 3, 15, 5, 2, 3)
)
dellNetDcbxScalarsGroup.setObjects(
      *(("DELL-NETWORKING-DCB-MIB", "dellNetDcbxGlobalTraceLevel"),
        ("DELL-NETWORKING-DCB-MIB", "dellNetDCBXGlobalVersion"))
)
if mibBuilder.loadTexts:
    dellNetDcbxScalarsGroup.setStatus("current")

dellNetDCBXPortTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6027, 3, 15, 5, 2, 4)
)
dellNetDCBXPortTableGroup.setObjects(
      *(("DELL-NETWORKING-DCB-MIB", "dellNetDCBXAdminStatus"),
        ("DELL-NETWORKING-DCB-MIB", "dellNetDCBXAutoCfgPortRole"),
        ("DELL-NETWORKING-DCB-MIB", "dellNetDCBXPortVersion"),
        ("DELL-NETWORKING-DCB-MIB", "dellNetDCBXPortSupportedTLVs"),
        ("DELL-NETWORKING-DCB-MIB", "dellNetDCBXPortConfigTLVsTxEnable"),
        ("DELL-NETWORKING-DCB-MIB", "dellNetDCBXPortOperVersion"),
        ("DELL-NETWORKING-DCB-MIB", "dellNetDCBXPortPeerMACaddress"),
        ("DELL-NETWORKING-DCB-MIB", "dellNetDCBXPortCfgSource"),
        ("DELL-NETWORKING-DCB-MIB", "dellNetDCBXOperStatus"),
        ("DELL-NETWORKING-DCB-MIB", "dellNetDCBXPortMultiplePeerCount"),
        ("DELL-NETWORKING-DCB-MIB", "dellNetDCBXPortPeerRemovedCount"),
        ("DELL-NETWORKING-DCB-MIB", "dellNetDCBXPortPeerOperVersionNum"),
        ("DELL-NETWORKING-DCB-MIB", "dellNetDCBXPortPeerMaxVersion"),
        ("DELL-NETWORKING-DCB-MIB", "dellNetDCBXPortSeqNum"),
        ("DELL-NETWORKING-DCB-MIB", "dellNetDCBXPortAckNum"),
        ("DELL-NETWORKING-DCB-MIB", "dellNetDCBXPortPeerRcvdAckNum"),
        ("DELL-NETWORKING-DCB-MIB", "dellNetDCBXPortTxCount"),
        ("DELL-NETWORKING-DCB-MIB", "dellNetDCBXPortRxCount"),
        ("DELL-NETWORKING-DCB-MIB", "dellNetDCBXPortErrorFramesCount"))
)
if mibBuilder.loadTexts:
    dellNetDCBXPortTableGroup.setStatus("current")

dellNetETSScalarsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6027, 3, 15, 5, 2, 5)
)
dellNetETSScalarsGroup.setObjects(
      *(("DELL-NETWORKING-DCB-MIB", "dellNetETSSystemControl"),
        ("DELL-NETWORKING-DCB-MIB", "dellNetETSModuleStatus"),
        ("DELL-NETWORKING-DCB-MIB", "dellNetETSClearCounters"),
        ("DELL-NETWORKING-DCB-MIB", "dellNetETSGlobalEnableTrap"))
)
if mibBuilder.loadTexts:
    dellNetETSScalarsGroup.setStatus("current")

dellNetETSPortTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6027, 3, 15, 5, 2, 6)
)
dellNetETSPortTableGroup.setObjects(
      *(("DELL-NETWORKING-DCB-MIB", "dellNetETSAdminMode"),
        ("DELL-NETWORKING-DCB-MIB", "dellNetETSDcbxOperState"),
        ("DELL-NETWORKING-DCB-MIB", "dellNetETSDcbxStateMachine"),
        ("DELL-NETWORKING-DCB-MIB", "dellNetETSOperStatus"),
        ("DELL-NETWORKING-DCB-MIB", "dellNetETSClearTLVCounters"),
        ("DELL-NETWORKING-DCB-MIB", "dellNetETSConfTxTLVCounter"),
        ("DELL-NETWORKING-DCB-MIB", "dellNetETSConfRxTLVCounter"),
        ("DELL-NETWORKING-DCB-MIB", "dellNetETSConfRxTLVErrors"),
        ("DELL-NETWORKING-DCB-MIB", "dellNetETSRecoTxTLVCounter"),
        ("DELL-NETWORKING-DCB-MIB", "dellNetETSRecoRxTLVCounter"),
        ("DELL-NETWORKING-DCB-MIB", "dellNetETSRecoRxTLVErrors"))
)
if mibBuilder.loadTexts:
    dellNetETSPortTableGroup.setStatus("current")

dellNetPFCScalarsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6027, 3, 15, 5, 2, 7)
)
dellNetPFCScalarsGroup.setObjects(
      *(("DELL-NETWORKING-DCB-MIB", "dellNetPFCSystemControl"),
        ("DELL-NETWORKING-DCB-MIB", "dellNetPFCModuleStatus"),
        ("DELL-NETWORKING-DCB-MIB", "dellNetPFCClearCounters"),
        ("DELL-NETWORKING-DCB-MIB", "dellNetPFCGlobalEnableTrap"))
)
if mibBuilder.loadTexts:
    dellNetPFCScalarsGroup.setStatus("current")

dellNetPFCPortTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6027, 3, 15, 5, 2, 8)
)
dellNetPFCPortTableGroup.setObjects(
      *(("DELL-NETWORKING-DCB-MIB", "dellNetPFCAdminMode"),
        ("DELL-NETWORKING-DCB-MIB", "dellNetPFCDcbxOperState"),
        ("DELL-NETWORKING-DCB-MIB", "dellNetPFCDcbxStateMachine"),
        ("DELL-NETWORKING-DCB-MIB", "dellNetPFCOperStatus"),
        ("DELL-NETWORKING-DCB-MIB", "dellNetPFCClearTLVCounters"),
        ("DELL-NETWORKING-DCB-MIB", "dellNetPFCTxTLVCounter"),
        ("DELL-NETWORKING-DCB-MIB", "dellNetPFCRxTLVCounter"),
        ("DELL-NETWORKING-DCB-MIB", "dellNetPFCRxTLVErrors"))
)
if mibBuilder.loadTexts:
    dellNetPFCPortTableGroup.setStatus("current")

dellNetDCBNotificationObjectsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6027, 3, 15, 5, 2, 9)
)
dellNetDCBNotificationObjectsGroup.setObjects(
      *(("DELL-NETWORKING-DCB-MIB", "dellNetDcbTrapPortNumber"),
        ("DELL-NETWORKING-DCB-MIB", "dellNetDcbPeerUpStatus"))
)
if mibBuilder.loadTexts:
    dellNetDCBNotificationObjectsGroup.setStatus("current")


# Notification objects

dellNetETSModuleStatusTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 6027, 3, 15, 4, 0, 1)
)
dellNetETSModuleStatusTrap.setObjects(
    ("DELL-NETWORKING-DCB-MIB", "dellNetETSModuleStatus")
)
if mibBuilder.loadTexts:
    dellNetETSModuleStatusTrap.setStatus(
        "current"
    )

dellNetETSPortAdminStatusTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 6027, 3, 15, 4, 0, 2)
)
dellNetETSPortAdminStatusTrap.setObjects(
      *(("DELL-NETWORKING-DCB-MIB", "dellNetDcbTrapPortNumber"),
        ("DELL-NETWORKING-DCB-MIB", "dellNetETSAdminMode"))
)
if mibBuilder.loadTexts:
    dellNetETSPortAdminStatusTrap.setStatus(
        "current"
    )

dellNetETSPortPeerStatusTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 6027, 3, 15, 4, 0, 3)
)
dellNetETSPortPeerStatusTrap.setObjects(
      *(("DELL-NETWORKING-DCB-MIB", "dellNetDcbTrapPortNumber"),
        ("DELL-NETWORKING-DCB-MIB", "dellNetDcbPeerUpStatus"))
)
if mibBuilder.loadTexts:
    dellNetETSPortPeerStatusTrap.setStatus(
        "current"
    )

dellNetETSPortDcbxOperStateTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 6027, 3, 15, 4, 0, 4)
)
dellNetETSPortDcbxOperStateTrap.setObjects(
      *(("DELL-NETWORKING-DCB-MIB", "dellNetDcbTrapPortNumber"),
        ("DELL-NETWORKING-DCB-MIB", "dellNetETSDcbxOperState"))
)
if mibBuilder.loadTexts:
    dellNetETSPortDcbxOperStateTrap.setStatus(
        "current"
    )

dellNetPFCModuleStatusTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 6027, 3, 15, 4, 0, 5)
)
dellNetPFCModuleStatusTrap.setObjects(
    ("DELL-NETWORKING-DCB-MIB", "dellNetPFCModuleStatus")
)
if mibBuilder.loadTexts:
    dellNetPFCModuleStatusTrap.setStatus(
        "current"
    )

dellNetPFCPortAdminStatusTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 6027, 3, 15, 4, 0, 6)
)
dellNetPFCPortAdminStatusTrap.setObjects(
      *(("DELL-NETWORKING-DCB-MIB", "dellNetDcbTrapPortNumber"),
        ("DELL-NETWORKING-DCB-MIB", "dellNetPFCAdminMode"))
)
if mibBuilder.loadTexts:
    dellNetPFCPortAdminStatusTrap.setStatus(
        "current"
    )

dellNetPFCPortPeerStatusTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 6027, 3, 15, 4, 0, 7)
)
dellNetPFCPortPeerStatusTrap.setObjects(
      *(("DELL-NETWORKING-DCB-MIB", "dellNetDcbTrapPortNumber"),
        ("DELL-NETWORKING-DCB-MIB", "dellNetDcbPeerUpStatus"))
)
if mibBuilder.loadTexts:
    dellNetPFCPortPeerStatusTrap.setStatus(
        "current"
    )

dellNetPFCPortDcbxOperStateTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 6027, 3, 15, 4, 0, 8)
)
dellNetPFCPortDcbxOperStateTrap.setObjects(
      *(("DELL-NETWORKING-DCB-MIB", "dellNetDcbTrapPortNumber"),
        ("DELL-NETWORKING-DCB-MIB", "dellNetPFCDcbxOperState"))
)
if mibBuilder.loadTexts:
    dellNetPFCPortDcbxOperStateTrap.setStatus(
        "current"
    )


# Notifications groups

dellNetDCBNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6027, 3, 15, 5, 2, 10)
)
dellNetDCBNotificationsGroup.setObjects(
      *(("DELL-NETWORKING-DCB-MIB", "dellNetETSModuleStatusTrap"),
        ("DELL-NETWORKING-DCB-MIB", "dellNetETSPortAdminStatusTrap"),
        ("DELL-NETWORKING-DCB-MIB", "dellNetETSPortPeerStatusTrap"),
        ("DELL-NETWORKING-DCB-MIB", "dellNetETSPortDcbxOperStateTrap"),
        ("DELL-NETWORKING-DCB-MIB", "dellNetPFCModuleStatusTrap"),
        ("DELL-NETWORKING-DCB-MIB", "dellNetPFCPortAdminStatusTrap"),
        ("DELL-NETWORKING-DCB-MIB", "dellNetPFCPortPeerStatusTrap"),
        ("DELL-NETWORKING-DCB-MIB", "dellNetPFCPortDcbxOperStateTrap"))
)
if mibBuilder.loadTexts:
    dellNetDCBNotificationsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

dellNetDCBMibComplianceRev1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6027, 3, 15, 5, 1, 1)
)
if mibBuilder.loadTexts:
    dellNetDCBMibComplianceRev1.setStatus(
        "current"
    )

dellNetDCBMibCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6027, 3, 15, 5, 1, 2)
)
if mibBuilder.loadTexts:
    dellNetDCBMibCompliance.setStatus(
        "obsolete"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DELL-NETWORKING-DCB-MIB",
    **{"EnabledStatus": EnabledStatus,
       "DcbAdminMode": DcbAdminMode,
       "DcbState": DcbState,
       "DcbStateMachineType": DcbStateMachineType,
       "DcbxPortRole": DcbxPortRole,
       "DcbxVersion": DcbxVersion,
       "dellNetDcb": dellNetDcb,
       "dellNetDcbSystem": dellNetDcbSystem,
       "dellNetDcbPfcMinThreshold": dellNetDcbPfcMinThreshold,
       "dellNetDcbPfcMaxThreshold": dellNetDcbPfcMaxThreshold,
       "dellNetDcbMaxPfcProfiles": dellNetDcbMaxPfcProfiles,
       "dellNetDcbObjects": dellNetDcbObjects,
       "dellNetDcbPortTable": dellNetDcbPortTable,
       "dellNetDcbPortEntry": dellNetDcbPortEntry,
       "dellNetDcbPortNumber": dellNetDcbPortNumber,
       "dellNetDcbETSAdminStatus": dellNetDcbETSAdminStatus,
       "dellNetDcbPFCAdminStatus": dellNetDcbPFCAdminStatus,
       "dellNetDcbApplicationObjects": dellNetDcbApplicationObjects,
       "dellNetDCBXObjects": dellNetDCBXObjects,
       "dellNetDCBXScalars": dellNetDCBXScalars,
       "dellNetDcbxGlobalTraceLevel": dellNetDcbxGlobalTraceLevel,
       "dellNetDCBXGlobalVersion": dellNetDCBXGlobalVersion,
       "dellNetDCBXPortTable": dellNetDCBXPortTable,
       "dellNetDCBXPortEntry": dellNetDCBXPortEntry,
       "dellNetDCBXPortNumber": dellNetDCBXPortNumber,
       "dellNetDCBXAdminStatus": dellNetDCBXAdminStatus,
       "dellNetDCBXAutoCfgPortRole": dellNetDCBXAutoCfgPortRole,
       "dellNetDCBXPortVersion": dellNetDCBXPortVersion,
       "dellNetDCBXPortSupportedTLVs": dellNetDCBXPortSupportedTLVs,
       "dellNetDCBXPortConfigTLVsTxEnable": dellNetDCBXPortConfigTLVsTxEnable,
       "dellNetDCBXPortStatusTable": dellNetDCBXPortStatusTable,
       "dellNetDCBXPortStatusEntry": dellNetDCBXPortStatusEntry,
       "dellNetDCBXPortOperVersion": dellNetDCBXPortOperVersion,
       "dellNetDCBXPortPeerMACaddress": dellNetDCBXPortPeerMACaddress,
       "dellNetDCBXPortCfgSource": dellNetDCBXPortCfgSource,
       "dellNetDCBXOperStatus": dellNetDCBXOperStatus,
       "dellNetDCBXPortMultiplePeerCount": dellNetDCBXPortMultiplePeerCount,
       "dellNetDCBXPortPeerRemovedCount": dellNetDCBXPortPeerRemovedCount,
       "dellNetDCBXPortPeerOperVersionNum": dellNetDCBXPortPeerOperVersionNum,
       "dellNetDCBXPortPeerMaxVersion": dellNetDCBXPortPeerMaxVersion,
       "dellNetDCBXPortSeqNum": dellNetDCBXPortSeqNum,
       "dellNetDCBXPortAckNum": dellNetDCBXPortAckNum,
       "dellNetDCBXPortPeerRcvdAckNum": dellNetDCBXPortPeerRcvdAckNum,
       "dellNetDCBXPortTxCount": dellNetDCBXPortTxCount,
       "dellNetDCBXPortRxCount": dellNetDCBXPortRxCount,
       "dellNetDCBXPortErrorFramesCount": dellNetDCBXPortErrorFramesCount,
       "dellNetETSObjects": dellNetETSObjects,
       "dellNetETSScalars": dellNetETSScalars,
       "dellNetETSSystemControl": dellNetETSSystemControl,
       "dellNetETSModuleStatus": dellNetETSModuleStatus,
       "dellNetETSClearCounters": dellNetETSClearCounters,
       "dellNetETSGlobalEnableTrap": dellNetETSGlobalEnableTrap,
       "dellNetETSPortTable": dellNetETSPortTable,
       "dellNetETSPortEntry": dellNetETSPortEntry,
       "dellNetETSPortNumber": dellNetETSPortNumber,
       "dellNetETSAdminMode": dellNetETSAdminMode,
       "dellNetETSDcbxOperState": dellNetETSDcbxOperState,
       "dellNetETSDcbxStateMachine": dellNetETSDcbxStateMachine,
       "dellNetETSOperStatus": dellNetETSOperStatus,
       "dellNetETSClearTLVCounters": dellNetETSClearTLVCounters,
       "dellNetETSConfTxTLVCounter": dellNetETSConfTxTLVCounter,
       "dellNetETSConfRxTLVCounter": dellNetETSConfRxTLVCounter,
       "dellNetETSConfRxTLVErrors": dellNetETSConfRxTLVErrors,
       "dellNetETSRecoTxTLVCounter": dellNetETSRecoTxTLVCounter,
       "dellNetETSRecoRxTLVCounter": dellNetETSRecoRxTLVCounter,
       "dellNetETSRecoRxTLVErrors": dellNetETSRecoRxTLVErrors,
       "dellNetPFCObjects": dellNetPFCObjects,
       "dellNetPFCScalars": dellNetPFCScalars,
       "dellNetPFCSystemControl": dellNetPFCSystemControl,
       "dellNetPFCModuleStatus": dellNetPFCModuleStatus,
       "dellNetPFCClearCounters": dellNetPFCClearCounters,
       "dellNetPFCGlobalEnableTrap": dellNetPFCGlobalEnableTrap,
       "dellNetPFCPortTable": dellNetPFCPortTable,
       "dellNetPFCPortEntry": dellNetPFCPortEntry,
       "dellNetPFCPortNumber": dellNetPFCPortNumber,
       "dellNetPFCAdminMode": dellNetPFCAdminMode,
       "dellNetPFCDcbxOperState": dellNetPFCDcbxOperState,
       "dellNetPFCDcbxStateMachine": dellNetPFCDcbxStateMachine,
       "dellNetPFCOperStatus": dellNetPFCOperStatus,
       "dellNetPFCClearTLVCounters": dellNetPFCClearTLVCounters,
       "dellNetPFCTxTLVCounter": dellNetPFCTxTLVCounter,
       "dellNetPFCRxTLVCounter": dellNetPFCRxTLVCounter,
       "dellNetPFCRxTLVErrors": dellNetPFCRxTLVErrors,
       "dellNetDcbNotificationObjects": dellNetDcbNotificationObjects,
       "dellNetDCBTraps": dellNetDCBTraps,
       "dellNetETSModuleStatusTrap": dellNetETSModuleStatusTrap,
       "dellNetETSPortAdminStatusTrap": dellNetETSPortAdminStatusTrap,
       "dellNetETSPortPeerStatusTrap": dellNetETSPortPeerStatusTrap,
       "dellNetETSPortDcbxOperStateTrap": dellNetETSPortDcbxOperStateTrap,
       "dellNetPFCModuleStatusTrap": dellNetPFCModuleStatusTrap,
       "dellNetPFCPortAdminStatusTrap": dellNetPFCPortAdminStatusTrap,
       "dellNetPFCPortPeerStatusTrap": dellNetPFCPortPeerStatusTrap,
       "dellNetPFCPortDcbxOperStateTrap": dellNetPFCPortDcbxOperStateTrap,
       "dellNetDCBTrapObjects": dellNetDCBTrapObjects,
       "dellNetDcbTrapPortNumber": dellNetDcbTrapPortNumber,
       "dellNetDcbPeerUpStatus": dellNetDcbPeerUpStatus,
       "dellNetDCBMibConformance": dellNetDCBMibConformance,
       "dellNetDCBMibCompliances": dellNetDCBMibCompliances,
       "dellNetDCBMibComplianceRev1": dellNetDCBMibComplianceRev1,
       "dellNetDCBMibCompliance": dellNetDCBMibCompliance,
       "dellNetDCBMibGroups": dellNetDCBMibGroups,
       "dellNetDcbSystemObjectGroup": dellNetDcbSystemObjectGroup,
       "dellNetDcbObjectGroup": dellNetDcbObjectGroup,
       "dellNetDcbxScalarsGroup": dellNetDcbxScalarsGroup,
       "dellNetDCBXPortTableGroup": dellNetDCBXPortTableGroup,
       "dellNetETSScalarsGroup": dellNetETSScalarsGroup,
       "dellNetETSPortTableGroup": dellNetETSPortTableGroup,
       "dellNetPFCScalarsGroup": dellNetPFCScalarsGroup,
       "dellNetPFCPortTableGroup": dellNetPFCPortTableGroup,
       "dellNetDCBNotificationObjectsGroup": dellNetDCBNotificationObjectsGroup,
       "dellNetDCBNotificationsGroup": dellNetDCBNotificationsGroup}
)
