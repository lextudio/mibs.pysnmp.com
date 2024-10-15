# SNMP MIB module (XEDIA-POLICY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/XEDIA-POLICY-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:18:01 2024
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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TruthValue")

(xediaMibs,) = mibBuilder.importSymbols(
    "XEDIA-REG",
    "xediaMibs")


# MODULE-IDENTITY

xediaPolicyMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 838, 3, 10)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class XPolicyName(DisplayString, TextualConvention):
    status = "current"
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )



class XPriPolicyName(DisplayString, TextualConvention):
    status = "current"
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )



class XPolicyAsString(DisplayString, TextualConvention):
    status = "current"
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )



# MIB Managed Objects in the order of their OIDs

_XpolicyObjects_ObjectIdentity = ObjectIdentity
xpolicyObjects = _XpolicyObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 838, 3, 10, 1)
)
_XpolicyGeneral_ObjectIdentity = ObjectIdentity
xpolicyGeneral = _XpolicyGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 838, 3, 10, 1, 1)
)
_XpolicyCounts_ObjectIdentity = ObjectIdentity
xpolicyCounts = _XpolicyCounts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 838, 3, 10, 1, 2)
)
_XpolicyRxCounts_ObjectIdentity = ObjectIdentity
xpolicyRxCounts = _XpolicyRxCounts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 838, 3, 10, 1, 2, 1)
)
_XpolicyNumRxConfiguredTotal_Type = Integer32
_XpolicyNumRxConfiguredTotal_Object = MibScalar
xpolicyNumRxConfiguredTotal = _XpolicyNumRxConfiguredTotal_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 10, 1, 2, 1, 1),
    _XpolicyNumRxConfiguredTotal_Type()
)
xpolicyNumRxConfiguredTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xpolicyNumRxConfiguredTotal.setStatus("current")
_XpolicyNumRxConfiguredValid_Type = Integer32
_XpolicyNumRxConfiguredValid_Object = MibScalar
xpolicyNumRxConfiguredValid = _XpolicyNumRxConfiguredValid_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 10, 1, 2, 1, 2),
    _XpolicyNumRxConfiguredValid_Type()
)
xpolicyNumRxConfiguredValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xpolicyNumRxConfiguredValid.setStatus("current")
_XpolicyNumRxConfiguredInValid_Type = Integer32
_XpolicyNumRxConfiguredInValid_Object = MibScalar
xpolicyNumRxConfiguredInValid = _XpolicyNumRxConfiguredInValid_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 10, 1, 2, 1, 3),
    _XpolicyNumRxConfiguredInValid_Type()
)
xpolicyNumRxConfiguredInValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xpolicyNumRxConfiguredInValid.setStatus("current")
_XpolicyNumRxInUseTotal_Type = Integer32
_XpolicyNumRxInUseTotal_Object = MibScalar
xpolicyNumRxInUseTotal = _XpolicyNumRxInUseTotal_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 10, 1, 2, 1, 4),
    _XpolicyNumRxInUseTotal_Type()
)
xpolicyNumRxInUseTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xpolicyNumRxInUseTotal.setStatus("current")
_XpolicyNumRxInUseBGP_Type = Integer32
_XpolicyNumRxInUseBGP_Object = MibScalar
xpolicyNumRxInUseBGP = _XpolicyNumRxInUseBGP_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 10, 1, 2, 1, 5),
    _XpolicyNumRxInUseBGP_Type()
)
xpolicyNumRxInUseBGP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xpolicyNumRxInUseBGP.setStatus("current")
_XpolicyNumRxInUseOSPF_Type = Integer32
_XpolicyNumRxInUseOSPF_Object = MibScalar
xpolicyNumRxInUseOSPF = _XpolicyNumRxInUseOSPF_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 10, 1, 2, 1, 6),
    _XpolicyNumRxInUseOSPF_Type()
)
xpolicyNumRxInUseOSPF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xpolicyNumRxInUseOSPF.setStatus("current")
_XpolicyNumRxInUseRIP_Type = Integer32
_XpolicyNumRxInUseRIP_Object = MibScalar
xpolicyNumRxInUseRIP = _XpolicyNumRxInUseRIP_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 10, 1, 2, 1, 7),
    _XpolicyNumRxInUseRIP_Type()
)
xpolicyNumRxInUseRIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xpolicyNumRxInUseRIP.setStatus("current")
_XpolicyNumRxInUseStatic_Type = Integer32
_XpolicyNumRxInUseStatic_Object = MibScalar
xpolicyNumRxInUseStatic = _XpolicyNumRxInUseStatic_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 10, 1, 2, 1, 8),
    _XpolicyNumRxInUseStatic_Type()
)
xpolicyNumRxInUseStatic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xpolicyNumRxInUseStatic.setStatus("current")
_XpolicyTxCounts_ObjectIdentity = ObjectIdentity
xpolicyTxCounts = _XpolicyTxCounts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 838, 3, 10, 1, 2, 2)
)
_XpolicyNumTxConfiguredTotal_Type = Integer32
_XpolicyNumTxConfiguredTotal_Object = MibScalar
xpolicyNumTxConfiguredTotal = _XpolicyNumTxConfiguredTotal_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 10, 1, 2, 2, 1),
    _XpolicyNumTxConfiguredTotal_Type()
)
xpolicyNumTxConfiguredTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xpolicyNumTxConfiguredTotal.setStatus("current")
_XpolicyNumTxConfiguredValid_Type = Integer32
_XpolicyNumTxConfiguredValid_Object = MibScalar
xpolicyNumTxConfiguredValid = _XpolicyNumTxConfiguredValid_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 10, 1, 2, 2, 2),
    _XpolicyNumTxConfiguredValid_Type()
)
xpolicyNumTxConfiguredValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xpolicyNumTxConfiguredValid.setStatus("current")
_XpolicyNumTxConfiguredInValid_Type = Integer32
_XpolicyNumTxConfiguredInValid_Object = MibScalar
xpolicyNumTxConfiguredInValid = _XpolicyNumTxConfiguredInValid_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 10, 1, 2, 2, 3),
    _XpolicyNumTxConfiguredInValid_Type()
)
xpolicyNumTxConfiguredInValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xpolicyNumTxConfiguredInValid.setStatus("current")
_XpolicyNumTxInUseTotal_Type = Integer32
_XpolicyNumTxInUseTotal_Object = MibScalar
xpolicyNumTxInUseTotal = _XpolicyNumTxInUseTotal_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 10, 1, 2, 2, 4),
    _XpolicyNumTxInUseTotal_Type()
)
xpolicyNumTxInUseTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xpolicyNumTxInUseTotal.setStatus("current")
_XpolicyNumTxInUseBGP_Type = Integer32
_XpolicyNumTxInUseBGP_Object = MibScalar
xpolicyNumTxInUseBGP = _XpolicyNumTxInUseBGP_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 10, 1, 2, 2, 5),
    _XpolicyNumTxInUseBGP_Type()
)
xpolicyNumTxInUseBGP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xpolicyNumTxInUseBGP.setStatus("current")
_XpolicyNumTxInUseOSPF_Type = Integer32
_XpolicyNumTxInUseOSPF_Object = MibScalar
xpolicyNumTxInUseOSPF = _XpolicyNumTxInUseOSPF_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 10, 1, 2, 2, 6),
    _XpolicyNumTxInUseOSPF_Type()
)
xpolicyNumTxInUseOSPF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xpolicyNumTxInUseOSPF.setStatus("current")
_XpolicyNumTxInUseRIP_Type = Integer32
_XpolicyNumTxInUseRIP_Object = MibScalar
xpolicyNumTxInUseRIP = _XpolicyNumTxInUseRIP_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 10, 1, 2, 2, 7),
    _XpolicyNumTxInUseRIP_Type()
)
xpolicyNumTxInUseRIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xpolicyNumTxInUseRIP.setStatus("current")
_XpolicyTables_ObjectIdentity = ObjectIdentity
xpolicyTables = _XpolicyTables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 838, 3, 10, 2)
)
_XpolicyRouting_ObjectIdentity = ObjectIdentity
xpolicyRouting = _XpolicyRouting_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 838, 3, 10, 2, 1)
)
_XpolicyReceiveTable_Object = MibTable
xpolicyReceiveTable = _XpolicyReceiveTable_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 10, 2, 1, 1)
)
if mibBuilder.loadTexts:
    xpolicyReceiveTable.setStatus("current")
_XpolicyReceiveEntry_Object = MibTableRow
xpolicyReceiveEntry = _XpolicyReceiveEntry_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 10, 2, 1, 1, 1)
)
xpolicyReceiveEntry.setIndexNames(
    (0, "XEDIA-POLICY-MIB", "xpolicyRxProtocol"),
    (0, "XEDIA-POLICY-MIB", "xpolicyRxPeer"),
    (0, "XEDIA-POLICY-MIB", "xpolicyRxName"),
)
if mibBuilder.loadTexts:
    xpolicyReceiveEntry.setStatus("current")


class _XpolicyRxProtocol_Type(Integer32):
    """Custom type xpolicyRxProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("bgp", 1),
          ("ospf", 2),
          ("rip", 3))
    )


_XpolicyRxProtocol_Type.__name__ = "Integer32"
_XpolicyRxProtocol_Object = MibTableColumn
xpolicyRxProtocol = _XpolicyRxProtocol_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 10, 2, 1, 1, 1, 1),
    _XpolicyRxProtocol_Type()
)
xpolicyRxProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xpolicyRxProtocol.setStatus("current")
_XpolicyRxPeer_Type = IpAddress
_XpolicyRxPeer_Object = MibTableColumn
xpolicyRxPeer = _XpolicyRxPeer_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 10, 2, 1, 1, 1, 2),
    _XpolicyRxPeer_Type()
)
xpolicyRxPeer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xpolicyRxPeer.setStatus("current")
_XpolicyRxName_Type = XPolicyName
_XpolicyRxName_Object = MibTableColumn
xpolicyRxName = _XpolicyRxName_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 10, 2, 1, 1, 1, 3),
    _XpolicyRxName_Type()
)
xpolicyRxName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xpolicyRxName.setStatus("current")


class _XpolicyRxAddrStart_Type(IpAddress):
    """Custom type xpolicyRxAddrStart based on IpAddress"""
    defaultHexValue = "00000000"


_XpolicyRxAddrStart_Object = MibTableColumn
xpolicyRxAddrStart = _XpolicyRxAddrStart_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 10, 2, 1, 1, 1, 4),
    _XpolicyRxAddrStart_Type()
)
xpolicyRxAddrStart.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xpolicyRxAddrStart.setStatus("current")


class _XpolicyRxAddrEnd_Type(IpAddress):
    """Custom type xpolicyRxAddrEnd based on IpAddress"""
    defaultHexValue = "ffffffff"


_XpolicyRxAddrEnd_Object = MibTableColumn
xpolicyRxAddrEnd = _XpolicyRxAddrEnd_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 10, 2, 1, 1, 1, 5),
    _XpolicyRxAddrEnd_Type()
)
xpolicyRxAddrEnd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xpolicyRxAddrEnd.setStatus("current")
_XpolicyRxAsString_Type = XPolicyAsString
_XpolicyRxAsString_Object = MibTableColumn
xpolicyRxAsString = _XpolicyRxAsString_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 10, 2, 1, 1, 1, 6),
    _XpolicyRxAsString_Type()
)
xpolicyRxAsString.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xpolicyRxAsString.setStatus("current")


class _XpolicyRxCommunityId_Type(Integer32):
    """Custom type xpolicyRxCommunityId based on Integer32"""
    defaultHexValue = 65536

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_XpolicyRxCommunityId_Type.__name__ = "Integer32"
_XpolicyRxCommunityId_Object = MibTableColumn
xpolicyRxCommunityId = _XpolicyRxCommunityId_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 10, 2, 1, 1, 1, 7),
    _XpolicyRxCommunityId_Type()
)
xpolicyRxCommunityId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xpolicyRxCommunityId.setStatus("current")


class _XpolicyRxReceiveOption_Type(Integer32):
    """Custom type xpolicyRxReceiveOption based on Integer32"""
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
        *(("drop", 3),
          ("ignore", 1),
          ("receive", 2))
    )


_XpolicyRxReceiveOption_Type.__name__ = "Integer32"
_XpolicyRxReceiveOption_Object = MibTableColumn
xpolicyRxReceiveOption = _XpolicyRxReceiveOption_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 10, 2, 1, 1, 1, 8),
    _XpolicyRxReceiveOption_Type()
)
xpolicyRxReceiveOption.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xpolicyRxReceiveOption.setStatus("current")


class _XpolicyRxLocalPref_Type(Integer32):
    """Custom type xpolicyRxLocalPref based on Integer32"""
    defaultValue = -1


_XpolicyRxLocalPref_Object = MibTableColumn
xpolicyRxLocalPref = _XpolicyRxLocalPref_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 10, 2, 1, 1, 1, 9),
    _XpolicyRxLocalPref_Type()
)
xpolicyRxLocalPref.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xpolicyRxLocalPref.setStatus("current")
_XpolicyRxRowStatus_Type = RowStatus
_XpolicyRxRowStatus_Object = MibTableColumn
xpolicyRxRowStatus = _XpolicyRxRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 10, 2, 1, 1, 1, 10),
    _XpolicyRxRowStatus_Type()
)
xpolicyRxRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xpolicyRxRowStatus.setStatus("current")


class _XpolicyRxPrefixMin_Type(Integer32):
    """Custom type xpolicyRxPrefixMin based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_XpolicyRxPrefixMin_Type.__name__ = "Integer32"
_XpolicyRxPrefixMin_Object = MibTableColumn
xpolicyRxPrefixMin = _XpolicyRxPrefixMin_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 10, 2, 1, 1, 1, 11),
    _XpolicyRxPrefixMin_Type()
)
xpolicyRxPrefixMin.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xpolicyRxPrefixMin.setStatus("current")


class _XpolicyRxPrefixMax_Type(Integer32):
    """Custom type xpolicyRxPrefixMax based on Integer32"""
    defaultValue = 32

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_XpolicyRxPrefixMax_Type.__name__ = "Integer32"
_XpolicyRxPrefixMax_Object = MibTableColumn
xpolicyRxPrefixMax = _XpolicyRxPrefixMax_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 10, 2, 1, 1, 1, 12),
    _XpolicyRxPrefixMax_Type()
)
xpolicyRxPrefixMax.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xpolicyRxPrefixMax.setStatus("current")
_XpolicySendTable_Object = MibTable
xpolicySendTable = _XpolicySendTable_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 10, 2, 1, 2)
)
if mibBuilder.loadTexts:
    xpolicySendTable.setStatus("current")
_XpolicySendEntry_Object = MibTableRow
xpolicySendEntry = _XpolicySendEntry_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 10, 2, 1, 2, 1)
)
xpolicySendEntry.setIndexNames(
    (0, "XEDIA-POLICY-MIB", "xpolicyTxProtocol"),
    (0, "XEDIA-POLICY-MIB", "xpolicyTxPeer"),
    (0, "XEDIA-POLICY-MIB", "xpolicyTxName"),
)
if mibBuilder.loadTexts:
    xpolicySendEntry.setStatus("current")


class _XpolicyTxProtocol_Type(Integer32):
    """Custom type xpolicyTxProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("bgp", 1),
          ("ospf", 2),
          ("rip", 3))
    )


_XpolicyTxProtocol_Type.__name__ = "Integer32"
_XpolicyTxProtocol_Object = MibTableColumn
xpolicyTxProtocol = _XpolicyTxProtocol_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 10, 2, 1, 2, 1, 1),
    _XpolicyTxProtocol_Type()
)
xpolicyTxProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xpolicyTxProtocol.setStatus("current")
_XpolicyTxPeer_Type = IpAddress
_XpolicyTxPeer_Object = MibTableColumn
xpolicyTxPeer = _XpolicyTxPeer_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 10, 2, 1, 2, 1, 2),
    _XpolicyTxPeer_Type()
)
xpolicyTxPeer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xpolicyTxPeer.setStatus("current")
_XpolicyTxName_Type = XPolicyName
_XpolicyTxName_Object = MibTableColumn
xpolicyTxName = _XpolicyTxName_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 10, 2, 1, 2, 1, 3),
    _XpolicyTxName_Type()
)
xpolicyTxName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xpolicyTxName.setStatus("current")


class _XpolicyTxSrcProtocol_Type(Integer32):
    """Custom type xpolicyTxSrcProtocol based on Integer32"""
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
        *(("bgp", 1),
          ("local", 4),
          ("ospf", 2),
          ("rip", 3),
          ("static", 5))
    )


_XpolicyTxSrcProtocol_Type.__name__ = "Integer32"
_XpolicyTxSrcProtocol_Object = MibTableColumn
xpolicyTxSrcProtocol = _XpolicyTxSrcProtocol_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 10, 2, 1, 2, 1, 4),
    _XpolicyTxSrcProtocol_Type()
)
xpolicyTxSrcProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xpolicyTxSrcProtocol.setStatus("current")


class _XpolicyTxSrcProtSubType_Type(Integer32):
    """Custom type xpolicyTxSrcProtSubType based on Integer32"""
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
        *(("any", 1),
          ("external", 3),
          ("internal", 2))
    )


_XpolicyTxSrcProtSubType_Type.__name__ = "Integer32"
_XpolicyTxSrcProtSubType_Object = MibTableColumn
xpolicyTxSrcProtSubType = _XpolicyTxSrcProtSubType_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 10, 2, 1, 2, 1, 5),
    _XpolicyTxSrcProtSubType_Type()
)
xpolicyTxSrcProtSubType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xpolicyTxSrcProtSubType.setStatus("current")


class _XpolicyTxAddrStart_Type(IpAddress):
    """Custom type xpolicyTxAddrStart based on IpAddress"""
    defaultHexValue = "00000000"


_XpolicyTxAddrStart_Object = MibTableColumn
xpolicyTxAddrStart = _XpolicyTxAddrStart_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 10, 2, 1, 2, 1, 6),
    _XpolicyTxAddrStart_Type()
)
xpolicyTxAddrStart.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xpolicyTxAddrStart.setStatus("current")


class _XpolicyTxAddrEnd_Type(IpAddress):
    """Custom type xpolicyTxAddrEnd based on IpAddress"""
    defaultHexValue = "ffffffff"


_XpolicyTxAddrEnd_Object = MibTableColumn
xpolicyTxAddrEnd = _XpolicyTxAddrEnd_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 10, 2, 1, 2, 1, 7),
    _XpolicyTxAddrEnd_Type()
)
xpolicyTxAddrEnd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xpolicyTxAddrEnd.setStatus("current")
_XpolicyTxAsString_Type = XPolicyAsString
_XpolicyTxAsString_Object = MibTableColumn
xpolicyTxAsString = _XpolicyTxAsString_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 10, 2, 1, 2, 1, 8),
    _XpolicyTxAsString_Type()
)
xpolicyTxAsString.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xpolicyTxAsString.setStatus("current")


class _XpolicyTxCommunityId_Type(Integer32):
    """Custom type xpolicyTxCommunityId based on Integer32"""
    defaultHexValue = 65536

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_XpolicyTxCommunityId_Type.__name__ = "Integer32"
_XpolicyTxCommunityId_Object = MibTableColumn
xpolicyTxCommunityId = _XpolicyTxCommunityId_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 10, 2, 1, 2, 1, 9),
    _XpolicyTxCommunityId_Type()
)
xpolicyTxCommunityId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xpolicyTxCommunityId.setStatus("current")


class _XpolicyTxSendOption_Type(Integer32):
    """Custom type xpolicyTxSendOption based on Integer32"""
    defaultValue = 3

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
        *(("aggregate", 4),
          ("ignore", 1),
          ("never", 2),
          ("normal", 3))
    )


_XpolicyTxSendOption_Type.__name__ = "Integer32"
_XpolicyTxSendOption_Object = MibTableColumn
xpolicyTxSendOption = _XpolicyTxSendOption_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 10, 2, 1, 2, 1, 10),
    _XpolicyTxSendOption_Type()
)
xpolicyTxSendOption.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xpolicyTxSendOption.setStatus("current")


class _XpolicyTxMED_Type(Integer32):
    """Custom type xpolicyTxMED based on Integer32"""
    defaultHexValue = 4294967295


_XpolicyTxMED_Object = MibTableColumn
xpolicyTxMED = _XpolicyTxMED_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 10, 2, 1, 2, 1, 11),
    _XpolicyTxMED_Type()
)
xpolicyTxMED.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xpolicyTxMED.setStatus("current")


class _XpolicyTxMEDAuto_Type(Integer32):
    """Custom type xpolicyTxMEDAuto based on Integer32"""
    defaultValue = 1

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


_XpolicyTxMEDAuto_Type.__name__ = "Integer32"
_XpolicyTxMEDAuto_Object = MibTableColumn
xpolicyTxMEDAuto = _XpolicyTxMEDAuto_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 10, 2, 1, 2, 1, 12),
    _XpolicyTxMEDAuto_Type()
)
xpolicyTxMEDAuto.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xpolicyTxMEDAuto.setStatus("current")


class _XpolicyTxAsPrepend_Type(Integer32):
    """Custom type xpolicyTxAsPrepend based on Integer32"""
    defaultValue = 0


_XpolicyTxAsPrepend_Object = MibTableColumn
xpolicyTxAsPrepend = _XpolicyTxAsPrepend_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 10, 2, 1, 2, 1, 13),
    _XpolicyTxAsPrepend_Type()
)
xpolicyTxAsPrepend.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xpolicyTxAsPrepend.setStatus("current")


class _XpolicyTxSendCommunityId_Type(Integer32):
    """Custom type xpolicyTxSendCommunityId based on Integer32"""
    defaultHexValue = 65536

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_XpolicyTxSendCommunityId_Type.__name__ = "Integer32"
_XpolicyTxSendCommunityId_Object = MibTableColumn
xpolicyTxSendCommunityId = _XpolicyTxSendCommunityId_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 10, 2, 1, 2, 1, 14),
    _XpolicyTxSendCommunityId_Type()
)
xpolicyTxSendCommunityId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xpolicyTxSendCommunityId.setStatus("current")


class _XpolicyTxIgpMetric_Type(Integer32):
    """Custom type xpolicyTxIgpMetric based on Integer32"""
    defaultValue = 0


_XpolicyTxIgpMetric_Object = MibTableColumn
xpolicyTxIgpMetric = _XpolicyTxIgpMetric_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 10, 2, 1, 2, 1, 15),
    _XpolicyTxIgpMetric_Type()
)
xpolicyTxIgpMetric.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xpolicyTxIgpMetric.setStatus("current")


class _XpolicyTxIgpMetricType_Type(Integer32):
    """Custom type xpolicyTxIgpMetricType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ospfExtType1", 1),
          ("ospfExtType2", 2))
    )


_XpolicyTxIgpMetricType_Type.__name__ = "Integer32"
_XpolicyTxIgpMetricType_Object = MibTableColumn
xpolicyTxIgpMetricType = _XpolicyTxIgpMetricType_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 10, 2, 1, 2, 1, 16),
    _XpolicyTxIgpMetricType_Type()
)
xpolicyTxIgpMetricType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xpolicyTxIgpMetricType.setStatus("current")


class _XpolicyTxIgpMetricAuto_Type(Integer32):
    """Custom type xpolicyTxIgpMetricAuto based on Integer32"""
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
        *(("igp", 4),
          ("localPref", 2),
          ("med", 3),
          ("off", 1))
    )


_XpolicyTxIgpMetricAuto_Type.__name__ = "Integer32"
_XpolicyTxIgpMetricAuto_Object = MibTableColumn
xpolicyTxIgpMetricAuto = _XpolicyTxIgpMetricAuto_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 10, 2, 1, 2, 1, 17),
    _XpolicyTxIgpMetricAuto_Type()
)
xpolicyTxIgpMetricAuto.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xpolicyTxIgpMetricAuto.setStatus("current")


class _XpolicyTxNextHopSelf_Type(TruthValue):
    """Custom type xpolicyTxNextHopSelf based on TruthValue"""


_XpolicyTxNextHopSelf_Object = MibTableColumn
xpolicyTxNextHopSelf = _XpolicyTxNextHopSelf_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 10, 2, 1, 2, 1, 18),
    _XpolicyTxNextHopSelf_Type()
)
xpolicyTxNextHopSelf.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xpolicyTxNextHopSelf.setStatus("current")
_XpolicyTxRowStatus_Type = RowStatus
_XpolicyTxRowStatus_Object = MibTableColumn
xpolicyTxRowStatus = _XpolicyTxRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 10, 2, 1, 2, 1, 19),
    _XpolicyTxRowStatus_Type()
)
xpolicyTxRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xpolicyTxRowStatus.setStatus("current")


class _XpolicyTxPrefixMin_Type(Integer32):
    """Custom type xpolicyTxPrefixMin based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_XpolicyTxPrefixMin_Type.__name__ = "Integer32"
_XpolicyTxPrefixMin_Object = MibTableColumn
xpolicyTxPrefixMin = _XpolicyTxPrefixMin_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 10, 2, 1, 2, 1, 20),
    _XpolicyTxPrefixMin_Type()
)
xpolicyTxPrefixMin.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xpolicyTxPrefixMin.setStatus("current")


class _XpolicyTxPrefixMax_Type(Integer32):
    """Custom type xpolicyTxPrefixMax based on Integer32"""
    defaultValue = 32

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_XpolicyTxPrefixMax_Type.__name__ = "Integer32"
_XpolicyTxPrefixMax_Object = MibTableColumn
xpolicyTxPrefixMax = _XpolicyTxPrefixMax_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 10, 2, 1, 2, 1, 21),
    _XpolicyTxPrefixMax_Type()
)
xpolicyTxPrefixMax.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xpolicyTxPrefixMax.setStatus("current")
_XpolicyDisplayTable_Object = MibTable
xpolicyDisplayTable = _XpolicyDisplayTable_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 10, 2, 2)
)
if mibBuilder.loadTexts:
    xpolicyDisplayTable.setStatus("current")
_XpolicyDisplayEntry_Object = MibTableRow
xpolicyDisplayEntry = _XpolicyDisplayEntry_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 10, 2, 2, 1)
)
xpolicyDisplayEntry.setIndexNames(
    (0, "XEDIA-POLICY-MIB", "xpolicyDisplayIndex"),
)
if mibBuilder.loadTexts:
    xpolicyDisplayEntry.setStatus("current")
_XpolicyDisplayIndex_Type = Integer32
_XpolicyDisplayIndex_Object = MibTableColumn
xpolicyDisplayIndex = _XpolicyDisplayIndex_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 10, 2, 2, 1, 1),
    _XpolicyDisplayIndex_Type()
)
xpolicyDisplayIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xpolicyDisplayIndex.setStatus("current")
_XpolicyRxDisplayString_Type = DisplayString
_XpolicyRxDisplayString_Object = MibTableColumn
xpolicyRxDisplayString = _XpolicyRxDisplayString_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 10, 2, 2, 1, 2),
    _XpolicyRxDisplayString_Type()
)
xpolicyRxDisplayString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xpolicyRxDisplayString.setStatus("current")
_XpolicyTxDisplayString_Type = DisplayString
_XpolicyTxDisplayString_Object = MibTableColumn
xpolicyTxDisplayString = _XpolicyTxDisplayString_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 10, 2, 2, 1, 3),
    _XpolicyTxDisplayString_Type()
)
xpolicyTxDisplayString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xpolicyTxDisplayString.setStatus("current")
_XpolicyPeerGroupTable_Object = MibTable
xpolicyPeerGroupTable = _XpolicyPeerGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 10, 2, 3)
)
if mibBuilder.loadTexts:
    xpolicyPeerGroupTable.setStatus("current")
_XpolicyPeerGroupEntry_Object = MibTableRow
xpolicyPeerGroupEntry = _XpolicyPeerGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 10, 2, 3, 1)
)
xpolicyPeerGroupEntry.setIndexNames(
    (0, "XEDIA-POLICY-MIB", "xpolicyPeerGroupIndex"),
    (0, "XEDIA-POLICY-MIB", "xpolicyPeerGroupPeer"),
)
if mibBuilder.loadTexts:
    xpolicyPeerGroupEntry.setStatus("current")


class _XpolicyPeerGroupIndex_Type(Integer32):
    """Custom type xpolicyPeerGroupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_XpolicyPeerGroupIndex_Type.__name__ = "Integer32"
_XpolicyPeerGroupIndex_Object = MibTableColumn
xpolicyPeerGroupIndex = _XpolicyPeerGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 10, 2, 3, 1, 1),
    _XpolicyPeerGroupIndex_Type()
)
xpolicyPeerGroupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xpolicyPeerGroupIndex.setStatus("current")
_XpolicyPeerGroupPeer_Type = IpAddress
_XpolicyPeerGroupPeer_Object = MibTableColumn
xpolicyPeerGroupPeer = _XpolicyPeerGroupPeer_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 10, 2, 3, 1, 2),
    _XpolicyPeerGroupPeer_Type()
)
xpolicyPeerGroupPeer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xpolicyPeerGroupPeer.setStatus("current")
_XpolicyPeerGroupRowStatus_Type = RowStatus
_XpolicyPeerGroupRowStatus_Object = MibTableColumn
xpolicyPeerGroupRowStatus = _XpolicyPeerGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 10, 2, 3, 1, 3),
    _XpolicyPeerGroupRowStatus_Type()
)
xpolicyPeerGroupRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xpolicyPeerGroupRowStatus.setStatus("current")
_XpolicyPriRouting_ObjectIdentity = ObjectIdentity
xpolicyPriRouting = _XpolicyPriRouting_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 838, 3, 10, 2, 4)
)
_XpolicyPriReceiveTable_Object = MibTable
xpolicyPriReceiveTable = _XpolicyPriReceiveTable_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 10, 2, 4, 1)
)
if mibBuilder.loadTexts:
    xpolicyPriReceiveTable.setStatus("current")
_XpolicyPriReceiveEntry_Object = MibTableRow
xpolicyPriReceiveEntry = _XpolicyPriReceiveEntry_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 10, 2, 4, 1, 1)
)
xpolicyPriReceiveEntry.setIndexNames(
    (0, "XEDIA-POLICY-MIB", "xpolicyRxProtocol"),
    (0, "XEDIA-POLICY-MIB", "xpolicyRxName"),
)
if mibBuilder.loadTexts:
    xpolicyPriReceiveEntry.setStatus("current")


class _XpolicyPriRxProtocol_Type(Integer32):
    """Custom type xpolicyPriRxProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              5)
        )
    )
    namedValues = NamedValues(
        *(("bgp", 1),
          ("ospf", 2),
          ("rip", 3),
          ("static", 5))
    )


_XpolicyPriRxProtocol_Type.__name__ = "Integer32"
_XpolicyPriRxProtocol_Object = MibTableColumn
xpolicyPriRxProtocol = _XpolicyPriRxProtocol_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 10, 2, 4, 1, 1, 1),
    _XpolicyPriRxProtocol_Type()
)
xpolicyPriRxProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xpolicyPriRxProtocol.setStatus("current")
_XpolicyPriRxPeer_Type = IpAddress
_XpolicyPriRxPeer_Object = MibTableColumn
xpolicyPriRxPeer = _XpolicyPriRxPeer_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 10, 2, 4, 1, 1, 2),
    _XpolicyPriRxPeer_Type()
)
xpolicyPriRxPeer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xpolicyPriRxPeer.setStatus("current")
_XpolicyPriRxName_Type = XPriPolicyName
_XpolicyPriRxName_Object = MibTableColumn
xpolicyPriRxName = _XpolicyPriRxName_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 10, 2, 4, 1, 1, 3),
    _XpolicyPriRxName_Type()
)
xpolicyPriRxName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xpolicyPriRxName.setStatus("current")


class _XpolicyPriRxAddrStart_Type(IpAddress):
    """Custom type xpolicyPriRxAddrStart based on IpAddress"""
    defaultHexValue = "00000000"


_XpolicyPriRxAddrStart_Object = MibTableColumn
xpolicyPriRxAddrStart = _XpolicyPriRxAddrStart_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 10, 2, 4, 1, 1, 4),
    _XpolicyPriRxAddrStart_Type()
)
xpolicyPriRxAddrStart.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xpolicyPriRxAddrStart.setStatus("current")


class _XpolicyPriRxAddrEnd_Type(IpAddress):
    """Custom type xpolicyPriRxAddrEnd based on IpAddress"""
    defaultHexValue = "ffffffff"


_XpolicyPriRxAddrEnd_Object = MibTableColumn
xpolicyPriRxAddrEnd = _XpolicyPriRxAddrEnd_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 10, 2, 4, 1, 1, 5),
    _XpolicyPriRxAddrEnd_Type()
)
xpolicyPriRxAddrEnd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xpolicyPriRxAddrEnd.setStatus("current")
_XpolicyPriRxAsString_Type = XPolicyAsString
_XpolicyPriRxAsString_Object = MibTableColumn
xpolicyPriRxAsString = _XpolicyPriRxAsString_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 10, 2, 4, 1, 1, 6),
    _XpolicyPriRxAsString_Type()
)
xpolicyPriRxAsString.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xpolicyPriRxAsString.setStatus("current")


class _XpolicyPriRxCommunityId_Type(Integer32):
    """Custom type xpolicyPriRxCommunityId based on Integer32"""
    defaultHexValue = 65536

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_XpolicyPriRxCommunityId_Type.__name__ = "Integer32"
_XpolicyPriRxCommunityId_Object = MibTableColumn
xpolicyPriRxCommunityId = _XpolicyPriRxCommunityId_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 10, 2, 4, 1, 1, 7),
    _XpolicyPriRxCommunityId_Type()
)
xpolicyPriRxCommunityId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xpolicyPriRxCommunityId.setStatus("current")


class _XpolicyPriRxReceiveOption_Type(Integer32):
    """Custom type xpolicyPriRxReceiveOption based on Integer32"""
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
        *(("drop", 3),
          ("ignore", 1),
          ("receive", 2))
    )


_XpolicyPriRxReceiveOption_Type.__name__ = "Integer32"
_XpolicyPriRxReceiveOption_Object = MibTableColumn
xpolicyPriRxReceiveOption = _XpolicyPriRxReceiveOption_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 10, 2, 4, 1, 1, 8),
    _XpolicyPriRxReceiveOption_Type()
)
xpolicyPriRxReceiveOption.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xpolicyPriRxReceiveOption.setStatus("current")


class _XpolicyPriRxLocalPref_Type(Integer32):
    """Custom type xpolicyPriRxLocalPref based on Integer32"""
    defaultValue = -1


_XpolicyPriRxLocalPref_Object = MibTableColumn
xpolicyPriRxLocalPref = _XpolicyPriRxLocalPref_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 10, 2, 4, 1, 1, 9),
    _XpolicyPriRxLocalPref_Type()
)
xpolicyPriRxLocalPref.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xpolicyPriRxLocalPref.setStatus("current")
_XpolicyPriRxRowStatus_Type = RowStatus
_XpolicyPriRxRowStatus_Object = MibTableColumn
xpolicyPriRxRowStatus = _XpolicyPriRxRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 10, 2, 4, 1, 1, 10),
    _XpolicyPriRxRowStatus_Type()
)
xpolicyPriRxRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xpolicyPriRxRowStatus.setStatus("current")


class _XpolicyPriRxPrefixMin_Type(Integer32):
    """Custom type xpolicyPriRxPrefixMin based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_XpolicyPriRxPrefixMin_Type.__name__ = "Integer32"
_XpolicyPriRxPrefixMin_Object = MibTableColumn
xpolicyPriRxPrefixMin = _XpolicyPriRxPrefixMin_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 10, 2, 4, 1, 1, 11),
    _XpolicyPriRxPrefixMin_Type()
)
xpolicyPriRxPrefixMin.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xpolicyPriRxPrefixMin.setStatus("current")


class _XpolicyPriRxPrefixMax_Type(Integer32):
    """Custom type xpolicyPriRxPrefixMax based on Integer32"""
    defaultValue = 32

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_XpolicyPriRxPrefixMax_Type.__name__ = "Integer32"
_XpolicyPriRxPrefixMax_Object = MibTableColumn
xpolicyPriRxPrefixMax = _XpolicyPriRxPrefixMax_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 10, 2, 4, 1, 1, 12),
    _XpolicyPriRxPrefixMax_Type()
)
xpolicyPriRxPrefixMax.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xpolicyPriRxPrefixMax.setStatus("current")


class _XpolicyPriRxDistance_Type(Integer32):
    """Custom type xpolicyPriRxDistance based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 255),
    )


_XpolicyPriRxDistance_Type.__name__ = "Integer32"
_XpolicyPriRxDistance_Object = MibTableColumn
xpolicyPriRxDistance = _XpolicyPriRxDistance_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 10, 2, 4, 1, 1, 13),
    _XpolicyPriRxDistance_Type()
)
xpolicyPriRxDistance.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xpolicyPriRxDistance.setStatus("current")
_XpolicyPriSendTable_Object = MibTable
xpolicyPriSendTable = _XpolicyPriSendTable_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 10, 2, 4, 2)
)
if mibBuilder.loadTexts:
    xpolicyPriSendTable.setStatus("current")
_XpolicyPriSendEntry_Object = MibTableRow
xpolicyPriSendEntry = _XpolicyPriSendEntry_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 10, 2, 4, 2, 1)
)
xpolicyPriSendEntry.setIndexNames(
    (0, "XEDIA-POLICY-MIB", "xpolicyTxProtocol"),
    (0, "XEDIA-POLICY-MIB", "xpolicyTxName"),
)
if mibBuilder.loadTexts:
    xpolicyPriSendEntry.setStatus("current")


class _XpolicyPriTxProtocol_Type(Integer32):
    """Custom type xpolicyPriTxProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("bgp", 1),
          ("ospf", 2),
          ("rip", 3))
    )


_XpolicyPriTxProtocol_Type.__name__ = "Integer32"
_XpolicyPriTxProtocol_Object = MibTableColumn
xpolicyPriTxProtocol = _XpolicyPriTxProtocol_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 10, 2, 4, 2, 1, 1),
    _XpolicyPriTxProtocol_Type()
)
xpolicyPriTxProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xpolicyPriTxProtocol.setStatus("current")
_XpolicyPriTxPeer_Type = IpAddress
_XpolicyPriTxPeer_Object = MibTableColumn
xpolicyPriTxPeer = _XpolicyPriTxPeer_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 10, 2, 4, 2, 1, 2),
    _XpolicyPriTxPeer_Type()
)
xpolicyPriTxPeer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xpolicyPriTxPeer.setStatus("current")
_XpolicyPriTxName_Type = XPriPolicyName
_XpolicyPriTxName_Object = MibTableColumn
xpolicyPriTxName = _XpolicyPriTxName_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 10, 2, 4, 2, 1, 3),
    _XpolicyPriTxName_Type()
)
xpolicyPriTxName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xpolicyPriTxName.setStatus("current")


class _XpolicyPriTxSrcProtocol_Type(Integer32):
    """Custom type xpolicyPriTxSrcProtocol based on Integer32"""
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
        *(("bgp", 1),
          ("local", 4),
          ("ospf", 2),
          ("rip", 3),
          ("static", 5))
    )


_XpolicyPriTxSrcProtocol_Type.__name__ = "Integer32"
_XpolicyPriTxSrcProtocol_Object = MibTableColumn
xpolicyPriTxSrcProtocol = _XpolicyPriTxSrcProtocol_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 10, 2, 4, 2, 1, 4),
    _XpolicyPriTxSrcProtocol_Type()
)
xpolicyPriTxSrcProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xpolicyPriTxSrcProtocol.setStatus("current")


class _XpolicyPriTxSrcProtSubType_Type(Integer32):
    """Custom type xpolicyPriTxSrcProtSubType based on Integer32"""
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
        *(("any", 1),
          ("external", 3),
          ("internal", 2))
    )


_XpolicyPriTxSrcProtSubType_Type.__name__ = "Integer32"
_XpolicyPriTxSrcProtSubType_Object = MibTableColumn
xpolicyPriTxSrcProtSubType = _XpolicyPriTxSrcProtSubType_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 10, 2, 4, 2, 1, 5),
    _XpolicyPriTxSrcProtSubType_Type()
)
xpolicyPriTxSrcProtSubType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xpolicyPriTxSrcProtSubType.setStatus("current")


class _XpolicyPriTxAddrStart_Type(IpAddress):
    """Custom type xpolicyPriTxAddrStart based on IpAddress"""
    defaultHexValue = "00000000"


_XpolicyPriTxAddrStart_Object = MibTableColumn
xpolicyPriTxAddrStart = _XpolicyPriTxAddrStart_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 10, 2, 4, 2, 1, 6),
    _XpolicyPriTxAddrStart_Type()
)
xpolicyPriTxAddrStart.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xpolicyPriTxAddrStart.setStatus("current")


class _XpolicyPriTxAddrEnd_Type(IpAddress):
    """Custom type xpolicyPriTxAddrEnd based on IpAddress"""
    defaultHexValue = "ffffffff"


_XpolicyPriTxAddrEnd_Object = MibTableColumn
xpolicyPriTxAddrEnd = _XpolicyPriTxAddrEnd_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 10, 2, 4, 2, 1, 7),
    _XpolicyPriTxAddrEnd_Type()
)
xpolicyPriTxAddrEnd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xpolicyPriTxAddrEnd.setStatus("current")
_XpolicyPriTxAsString_Type = XPolicyAsString
_XpolicyPriTxAsString_Object = MibTableColumn
xpolicyPriTxAsString = _XpolicyPriTxAsString_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 10, 2, 4, 2, 1, 8),
    _XpolicyPriTxAsString_Type()
)
xpolicyPriTxAsString.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xpolicyPriTxAsString.setStatus("current")


class _XpolicyPriTxCommunityId_Type(Integer32):
    """Custom type xpolicyPriTxCommunityId based on Integer32"""
    defaultHexValue = 65536

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_XpolicyPriTxCommunityId_Type.__name__ = "Integer32"
_XpolicyPriTxCommunityId_Object = MibTableColumn
xpolicyPriTxCommunityId = _XpolicyPriTxCommunityId_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 10, 2, 4, 2, 1, 9),
    _XpolicyPriTxCommunityId_Type()
)
xpolicyPriTxCommunityId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xpolicyPriTxCommunityId.setStatus("current")


class _XpolicyPriTxSendOption_Type(Integer32):
    """Custom type xpolicyPriTxSendOption based on Integer32"""
    defaultValue = 3

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
        *(("aggregate", 4),
          ("ignore", 1),
          ("never", 2),
          ("normal", 3))
    )


_XpolicyPriTxSendOption_Type.__name__ = "Integer32"
_XpolicyPriTxSendOption_Object = MibTableColumn
xpolicyPriTxSendOption = _XpolicyPriTxSendOption_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 10, 2, 4, 2, 1, 10),
    _XpolicyPriTxSendOption_Type()
)
xpolicyPriTxSendOption.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xpolicyPriTxSendOption.setStatus("current")


class _XpolicyPriTxMED_Type(Integer32):
    """Custom type xpolicyPriTxMED based on Integer32"""
    defaultHexValue = 4294967295


_XpolicyPriTxMED_Object = MibTableColumn
xpolicyPriTxMED = _XpolicyPriTxMED_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 10, 2, 4, 2, 1, 11),
    _XpolicyPriTxMED_Type()
)
xpolicyPriTxMED.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xpolicyPriTxMED.setStatus("current")


class _XpolicyPriTxMEDAuto_Type(Integer32):
    """Custom type xpolicyPriTxMEDAuto based on Integer32"""
    defaultValue = 1

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


_XpolicyPriTxMEDAuto_Type.__name__ = "Integer32"
_XpolicyPriTxMEDAuto_Object = MibTableColumn
xpolicyPriTxMEDAuto = _XpolicyPriTxMEDAuto_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 10, 2, 4, 2, 1, 12),
    _XpolicyPriTxMEDAuto_Type()
)
xpolicyPriTxMEDAuto.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xpolicyPriTxMEDAuto.setStatus("current")


class _XpolicyPriTxAsPrepend_Type(Integer32):
    """Custom type xpolicyPriTxAsPrepend based on Integer32"""
    defaultValue = 0


_XpolicyPriTxAsPrepend_Object = MibTableColumn
xpolicyPriTxAsPrepend = _XpolicyPriTxAsPrepend_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 10, 2, 4, 2, 1, 13),
    _XpolicyPriTxAsPrepend_Type()
)
xpolicyPriTxAsPrepend.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xpolicyPriTxAsPrepend.setStatus("current")


class _XpolicyPriTxSendCommunityId_Type(Integer32):
    """Custom type xpolicyPriTxSendCommunityId based on Integer32"""
    defaultHexValue = 65536

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_XpolicyPriTxSendCommunityId_Type.__name__ = "Integer32"
_XpolicyPriTxSendCommunityId_Object = MibTableColumn
xpolicyPriTxSendCommunityId = _XpolicyPriTxSendCommunityId_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 10, 2, 4, 2, 1, 14),
    _XpolicyPriTxSendCommunityId_Type()
)
xpolicyPriTxSendCommunityId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xpolicyPriTxSendCommunityId.setStatus("current")


class _XpolicyPriTxIgpMetric_Type(Integer32):
    """Custom type xpolicyPriTxIgpMetric based on Integer32"""
    defaultValue = 0


_XpolicyPriTxIgpMetric_Object = MibTableColumn
xpolicyPriTxIgpMetric = _XpolicyPriTxIgpMetric_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 10, 2, 4, 2, 1, 15),
    _XpolicyPriTxIgpMetric_Type()
)
xpolicyPriTxIgpMetric.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xpolicyPriTxIgpMetric.setStatus("current")


class _XpolicyPriTxIgpMetricType_Type(Integer32):
    """Custom type xpolicyPriTxIgpMetricType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ospfExtType1", 1),
          ("ospfExtType2", 2))
    )


_XpolicyPriTxIgpMetricType_Type.__name__ = "Integer32"
_XpolicyPriTxIgpMetricType_Object = MibTableColumn
xpolicyPriTxIgpMetricType = _XpolicyPriTxIgpMetricType_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 10, 2, 4, 2, 1, 16),
    _XpolicyPriTxIgpMetricType_Type()
)
xpolicyPriTxIgpMetricType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xpolicyPriTxIgpMetricType.setStatus("current")


class _XpolicyPriTxIgpMetricAuto_Type(Integer32):
    """Custom type xpolicyPriTxIgpMetricAuto based on Integer32"""
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
        *(("igp", 4),
          ("localPref", 2),
          ("med", 3),
          ("off", 1))
    )


_XpolicyPriTxIgpMetricAuto_Type.__name__ = "Integer32"
_XpolicyPriTxIgpMetricAuto_Object = MibTableColumn
xpolicyPriTxIgpMetricAuto = _XpolicyPriTxIgpMetricAuto_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 10, 2, 4, 2, 1, 17),
    _XpolicyPriTxIgpMetricAuto_Type()
)
xpolicyPriTxIgpMetricAuto.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xpolicyPriTxIgpMetricAuto.setStatus("current")


class _XpolicyPriTxNextHopSelf_Type(TruthValue):
    """Custom type xpolicyPriTxNextHopSelf based on TruthValue"""


_XpolicyPriTxNextHopSelf_Object = MibTableColumn
xpolicyPriTxNextHopSelf = _XpolicyPriTxNextHopSelf_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 10, 2, 4, 2, 1, 18),
    _XpolicyPriTxNextHopSelf_Type()
)
xpolicyPriTxNextHopSelf.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xpolicyPriTxNextHopSelf.setStatus("current")
_XpolicyPriTxRowStatus_Type = RowStatus
_XpolicyPriTxRowStatus_Object = MibTableColumn
xpolicyPriTxRowStatus = _XpolicyPriTxRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 10, 2, 4, 2, 1, 19),
    _XpolicyPriTxRowStatus_Type()
)
xpolicyPriTxRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xpolicyPriTxRowStatus.setStatus("current")


class _XpolicyPriTxPrefixMin_Type(Integer32):
    """Custom type xpolicyPriTxPrefixMin based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_XpolicyPriTxPrefixMin_Type.__name__ = "Integer32"
_XpolicyPriTxPrefixMin_Object = MibTableColumn
xpolicyPriTxPrefixMin = _XpolicyPriTxPrefixMin_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 10, 2, 4, 2, 1, 20),
    _XpolicyPriTxPrefixMin_Type()
)
xpolicyPriTxPrefixMin.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xpolicyPriTxPrefixMin.setStatus("current")


class _XpolicyPriTxPrefixMax_Type(Integer32):
    """Custom type xpolicyPriTxPrefixMax based on Integer32"""
    defaultValue = 32

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_XpolicyPriTxPrefixMax_Type.__name__ = "Integer32"
_XpolicyPriTxPrefixMax_Object = MibTableColumn
xpolicyPriTxPrefixMax = _XpolicyPriTxPrefixMax_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 10, 2, 4, 2, 1, 21),
    _XpolicyPriTxPrefixMax_Type()
)
xpolicyPriTxPrefixMax.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xpolicyPriTxPrefixMax.setStatus("current")
_XpolicyConformance_ObjectIdentity = ObjectIdentity
xpolicyConformance = _XpolicyConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 838, 3, 10, 3)
)
_XpolicyCompliances_ObjectIdentity = ObjectIdentity
xpolicyCompliances = _XpolicyCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 838, 3, 10, 3, 1)
)
_XpolicyGroups_ObjectIdentity = ObjectIdentity
xpolicyGroups = _XpolicyGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 838, 3, 10, 3, 2)
)

# Managed Objects groups

xpolicyAllGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 838, 3, 10, 3, 2, 1)
)
xpolicyAllGroup.setObjects(
      *(("XEDIA-POLICY-MIB", "xpolicyNumRxConfiguredTotal"),
        ("XEDIA-POLICY-MIB", "xpolicyNumRxConfiguredValid"),
        ("XEDIA-POLICY-MIB", "xpolicyNumRxConfiguredInValid"),
        ("XEDIA-POLICY-MIB", "xpolicyNumRxInUseTotal"),
        ("XEDIA-POLICY-MIB", "xpolicyNumRxInUseBGP"),
        ("XEDIA-POLICY-MIB", "xpolicyNumRxInUseOSPF"),
        ("XEDIA-POLICY-MIB", "xpolicyNumRxInUseRIP"),
        ("XEDIA-POLICY-MIB", "xpolicyNumRxInUseStatic"),
        ("XEDIA-POLICY-MIB", "xpolicyNumTxConfiguredTotal"),
        ("XEDIA-POLICY-MIB", "xpolicyNumTxConfiguredValid"),
        ("XEDIA-POLICY-MIB", "xpolicyNumTxConfiguredInValid"),
        ("XEDIA-POLICY-MIB", "xpolicyNumTxInUseTotal"),
        ("XEDIA-POLICY-MIB", "xpolicyNumTxInUseBGP"),
        ("XEDIA-POLICY-MIB", "xpolicyNumTxInUseOSPF"),
        ("XEDIA-POLICY-MIB", "xpolicyNumTxInUseRIP"),
        ("XEDIA-POLICY-MIB", "xpolicyRxProtocol"),
        ("XEDIA-POLICY-MIB", "xpolicyRxPeer"),
        ("XEDIA-POLICY-MIB", "xpolicyRxName"),
        ("XEDIA-POLICY-MIB", "xpolicyRxAddrStart"),
        ("XEDIA-POLICY-MIB", "xpolicyRxAddrEnd"),
        ("XEDIA-POLICY-MIB", "xpolicyRxAsString"),
        ("XEDIA-POLICY-MIB", "xpolicyRxCommunityId"),
        ("XEDIA-POLICY-MIB", "xpolicyRxReceiveOption"),
        ("XEDIA-POLICY-MIB", "xpolicyRxLocalPref"),
        ("XEDIA-POLICY-MIB", "xpolicyRxRowStatus"),
        ("XEDIA-POLICY-MIB", "xpolicyRxPrefixMin"),
        ("XEDIA-POLICY-MIB", "xpolicyRxPrefixMax"),
        ("XEDIA-POLICY-MIB", "xpolicyTxProtocol"),
        ("XEDIA-POLICY-MIB", "xpolicyTxPeer"),
        ("XEDIA-POLICY-MIB", "xpolicyTxName"),
        ("XEDIA-POLICY-MIB", "xpolicyTxSrcProtocol"),
        ("XEDIA-POLICY-MIB", "xpolicyTxSrcProtSubType"),
        ("XEDIA-POLICY-MIB", "xpolicyTxAddrStart"),
        ("XEDIA-POLICY-MIB", "xpolicyTxAddrEnd"),
        ("XEDIA-POLICY-MIB", "xpolicyTxAsString"),
        ("XEDIA-POLICY-MIB", "xpolicyTxCommunityId"),
        ("XEDIA-POLICY-MIB", "xpolicyTxSendOption"),
        ("XEDIA-POLICY-MIB", "xpolicyTxMED"),
        ("XEDIA-POLICY-MIB", "xpolicyTxMEDAuto"),
        ("XEDIA-POLICY-MIB", "xpolicyTxAsPrepend"),
        ("XEDIA-POLICY-MIB", "xpolicyTxSendCommunityId"),
        ("XEDIA-POLICY-MIB", "xpolicyTxIgpMetric"),
        ("XEDIA-POLICY-MIB", "xpolicyTxIgpMetricType"),
        ("XEDIA-POLICY-MIB", "xpolicyTxIgpMetricAuto"),
        ("XEDIA-POLICY-MIB", "xpolicyTxNextHopSelf"),
        ("XEDIA-POLICY-MIB", "xpolicyTxRowStatus"),
        ("XEDIA-POLICY-MIB", "xpolicyTxPrefixMin"),
        ("XEDIA-POLICY-MIB", "xpolicyTxPrefixMax"),
        ("XEDIA-POLICY-MIB", "xpolicyRxDisplayString"),
        ("XEDIA-POLICY-MIB", "xpolicyTxDisplayString"),
        ("XEDIA-POLICY-MIB", "xpolicyPeerGroupIndex"),
        ("XEDIA-POLICY-MIB", "xpolicyPeerGroupPeer"),
        ("XEDIA-POLICY-MIB", "xpolicyPeerGroupRowStatus"),
        ("XEDIA-POLICY-MIB", "xpolicyPriRxProtocol"),
        ("XEDIA-POLICY-MIB", "xpolicyPriRxPeer"),
        ("XEDIA-POLICY-MIB", "xpolicyPriRxName"),
        ("XEDIA-POLICY-MIB", "xpolicyPriRxAddrStart"),
        ("XEDIA-POLICY-MIB", "xpolicyPriRxAddrEnd"),
        ("XEDIA-POLICY-MIB", "xpolicyPriRxAsString"),
        ("XEDIA-POLICY-MIB", "xpolicyPriRxCommunityId"),
        ("XEDIA-POLICY-MIB", "xpolicyPriRxReceiveOption"),
        ("XEDIA-POLICY-MIB", "xpolicyPriRxLocalPref"),
        ("XEDIA-POLICY-MIB", "xpolicyPriRxRowStatus"),
        ("XEDIA-POLICY-MIB", "xpolicyPriRxPrefixMin"),
        ("XEDIA-POLICY-MIB", "xpolicyPriRxPrefixMax"),
        ("XEDIA-POLICY-MIB", "xpolicyPriTxProtocol"),
        ("XEDIA-POLICY-MIB", "xpolicyPriTxPeer"),
        ("XEDIA-POLICY-MIB", "xpolicyPriTxName"),
        ("XEDIA-POLICY-MIB", "xpolicyPriTxSrcProtocol"),
        ("XEDIA-POLICY-MIB", "xpolicyPriTxSrcProtSubType"),
        ("XEDIA-POLICY-MIB", "xpolicyPriTxAddrStart"),
        ("XEDIA-POLICY-MIB", "xpolicyPriTxAddrEnd"),
        ("XEDIA-POLICY-MIB", "xpolicyPriTxAsString"),
        ("XEDIA-POLICY-MIB", "xpolicyPriTxCommunityId"),
        ("XEDIA-POLICY-MIB", "xpolicyPriTxSendOption"),
        ("XEDIA-POLICY-MIB", "xpolicyPriTxMED"),
        ("XEDIA-POLICY-MIB", "xpolicyPriTxMEDAuto"),
        ("XEDIA-POLICY-MIB", "xpolicyPriTxAsPrepend"),
        ("XEDIA-POLICY-MIB", "xpolicyPriTxSendCommunityId"),
        ("XEDIA-POLICY-MIB", "xpolicyPriTxIgpMetric"),
        ("XEDIA-POLICY-MIB", "xpolicyPriTxIgpMetricType"),
        ("XEDIA-POLICY-MIB", "xpolicyPriTxIgpMetricAuto"),
        ("XEDIA-POLICY-MIB", "xpolicyPriTxNextHopSelf"),
        ("XEDIA-POLICY-MIB", "xpolicyPriTxRowStatus"),
        ("XEDIA-POLICY-MIB", "xpolicyPriTxPrefixMin"),
        ("XEDIA-POLICY-MIB", "xpolicyPriTxPrefixMax"))
)
if mibBuilder.loadTexts:
    xpolicyAllGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

xpolicyCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 838, 3, 10, 3, 1, 1)
)
if mibBuilder.loadTexts:
    xpolicyCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "XEDIA-POLICY-MIB",
    **{"XPolicyName": XPolicyName,
       "XPriPolicyName": XPriPolicyName,
       "XPolicyAsString": XPolicyAsString,
       "xediaPolicyMIB": xediaPolicyMIB,
       "xpolicyObjects": xpolicyObjects,
       "xpolicyGeneral": xpolicyGeneral,
       "xpolicyCounts": xpolicyCounts,
       "xpolicyRxCounts": xpolicyRxCounts,
       "xpolicyNumRxConfiguredTotal": xpolicyNumRxConfiguredTotal,
       "xpolicyNumRxConfiguredValid": xpolicyNumRxConfiguredValid,
       "xpolicyNumRxConfiguredInValid": xpolicyNumRxConfiguredInValid,
       "xpolicyNumRxInUseTotal": xpolicyNumRxInUseTotal,
       "xpolicyNumRxInUseBGP": xpolicyNumRxInUseBGP,
       "xpolicyNumRxInUseOSPF": xpolicyNumRxInUseOSPF,
       "xpolicyNumRxInUseRIP": xpolicyNumRxInUseRIP,
       "xpolicyNumRxInUseStatic": xpolicyNumRxInUseStatic,
       "xpolicyTxCounts": xpolicyTxCounts,
       "xpolicyNumTxConfiguredTotal": xpolicyNumTxConfiguredTotal,
       "xpolicyNumTxConfiguredValid": xpolicyNumTxConfiguredValid,
       "xpolicyNumTxConfiguredInValid": xpolicyNumTxConfiguredInValid,
       "xpolicyNumTxInUseTotal": xpolicyNumTxInUseTotal,
       "xpolicyNumTxInUseBGP": xpolicyNumTxInUseBGP,
       "xpolicyNumTxInUseOSPF": xpolicyNumTxInUseOSPF,
       "xpolicyNumTxInUseRIP": xpolicyNumTxInUseRIP,
       "xpolicyTables": xpolicyTables,
       "xpolicyRouting": xpolicyRouting,
       "xpolicyReceiveTable": xpolicyReceiveTable,
       "xpolicyReceiveEntry": xpolicyReceiveEntry,
       "xpolicyRxProtocol": xpolicyRxProtocol,
       "xpolicyRxPeer": xpolicyRxPeer,
       "xpolicyRxName": xpolicyRxName,
       "xpolicyRxAddrStart": xpolicyRxAddrStart,
       "xpolicyRxAddrEnd": xpolicyRxAddrEnd,
       "xpolicyRxAsString": xpolicyRxAsString,
       "xpolicyRxCommunityId": xpolicyRxCommunityId,
       "xpolicyRxReceiveOption": xpolicyRxReceiveOption,
       "xpolicyRxLocalPref": xpolicyRxLocalPref,
       "xpolicyRxRowStatus": xpolicyRxRowStatus,
       "xpolicyRxPrefixMin": xpolicyRxPrefixMin,
       "xpolicyRxPrefixMax": xpolicyRxPrefixMax,
       "xpolicySendTable": xpolicySendTable,
       "xpolicySendEntry": xpolicySendEntry,
       "xpolicyTxProtocol": xpolicyTxProtocol,
       "xpolicyTxPeer": xpolicyTxPeer,
       "xpolicyTxName": xpolicyTxName,
       "xpolicyTxSrcProtocol": xpolicyTxSrcProtocol,
       "xpolicyTxSrcProtSubType": xpolicyTxSrcProtSubType,
       "xpolicyTxAddrStart": xpolicyTxAddrStart,
       "xpolicyTxAddrEnd": xpolicyTxAddrEnd,
       "xpolicyTxAsString": xpolicyTxAsString,
       "xpolicyTxCommunityId": xpolicyTxCommunityId,
       "xpolicyTxSendOption": xpolicyTxSendOption,
       "xpolicyTxMED": xpolicyTxMED,
       "xpolicyTxMEDAuto": xpolicyTxMEDAuto,
       "xpolicyTxAsPrepend": xpolicyTxAsPrepend,
       "xpolicyTxSendCommunityId": xpolicyTxSendCommunityId,
       "xpolicyTxIgpMetric": xpolicyTxIgpMetric,
       "xpolicyTxIgpMetricType": xpolicyTxIgpMetricType,
       "xpolicyTxIgpMetricAuto": xpolicyTxIgpMetricAuto,
       "xpolicyTxNextHopSelf": xpolicyTxNextHopSelf,
       "xpolicyTxRowStatus": xpolicyTxRowStatus,
       "xpolicyTxPrefixMin": xpolicyTxPrefixMin,
       "xpolicyTxPrefixMax": xpolicyTxPrefixMax,
       "xpolicyDisplayTable": xpolicyDisplayTable,
       "xpolicyDisplayEntry": xpolicyDisplayEntry,
       "xpolicyDisplayIndex": xpolicyDisplayIndex,
       "xpolicyRxDisplayString": xpolicyRxDisplayString,
       "xpolicyTxDisplayString": xpolicyTxDisplayString,
       "xpolicyPeerGroupTable": xpolicyPeerGroupTable,
       "xpolicyPeerGroupEntry": xpolicyPeerGroupEntry,
       "xpolicyPeerGroupIndex": xpolicyPeerGroupIndex,
       "xpolicyPeerGroupPeer": xpolicyPeerGroupPeer,
       "xpolicyPeerGroupRowStatus": xpolicyPeerGroupRowStatus,
       "xpolicyPriRouting": xpolicyPriRouting,
       "xpolicyPriReceiveTable": xpolicyPriReceiveTable,
       "xpolicyPriReceiveEntry": xpolicyPriReceiveEntry,
       "xpolicyPriRxProtocol": xpolicyPriRxProtocol,
       "xpolicyPriRxPeer": xpolicyPriRxPeer,
       "xpolicyPriRxName": xpolicyPriRxName,
       "xpolicyPriRxAddrStart": xpolicyPriRxAddrStart,
       "xpolicyPriRxAddrEnd": xpolicyPriRxAddrEnd,
       "xpolicyPriRxAsString": xpolicyPriRxAsString,
       "xpolicyPriRxCommunityId": xpolicyPriRxCommunityId,
       "xpolicyPriRxReceiveOption": xpolicyPriRxReceiveOption,
       "xpolicyPriRxLocalPref": xpolicyPriRxLocalPref,
       "xpolicyPriRxRowStatus": xpolicyPriRxRowStatus,
       "xpolicyPriRxPrefixMin": xpolicyPriRxPrefixMin,
       "xpolicyPriRxPrefixMax": xpolicyPriRxPrefixMax,
       "xpolicyPriRxDistance": xpolicyPriRxDistance,
       "xpolicyPriSendTable": xpolicyPriSendTable,
       "xpolicyPriSendEntry": xpolicyPriSendEntry,
       "xpolicyPriTxProtocol": xpolicyPriTxProtocol,
       "xpolicyPriTxPeer": xpolicyPriTxPeer,
       "xpolicyPriTxName": xpolicyPriTxName,
       "xpolicyPriTxSrcProtocol": xpolicyPriTxSrcProtocol,
       "xpolicyPriTxSrcProtSubType": xpolicyPriTxSrcProtSubType,
       "xpolicyPriTxAddrStart": xpolicyPriTxAddrStart,
       "xpolicyPriTxAddrEnd": xpolicyPriTxAddrEnd,
       "xpolicyPriTxAsString": xpolicyPriTxAsString,
       "xpolicyPriTxCommunityId": xpolicyPriTxCommunityId,
       "xpolicyPriTxSendOption": xpolicyPriTxSendOption,
       "xpolicyPriTxMED": xpolicyPriTxMED,
       "xpolicyPriTxMEDAuto": xpolicyPriTxMEDAuto,
       "xpolicyPriTxAsPrepend": xpolicyPriTxAsPrepend,
       "xpolicyPriTxSendCommunityId": xpolicyPriTxSendCommunityId,
       "xpolicyPriTxIgpMetric": xpolicyPriTxIgpMetric,
       "xpolicyPriTxIgpMetricType": xpolicyPriTxIgpMetricType,
       "xpolicyPriTxIgpMetricAuto": xpolicyPriTxIgpMetricAuto,
       "xpolicyPriTxNextHopSelf": xpolicyPriTxNextHopSelf,
       "xpolicyPriTxRowStatus": xpolicyPriTxRowStatus,
       "xpolicyPriTxPrefixMin": xpolicyPriTxPrefixMin,
       "xpolicyPriTxPrefixMax": xpolicyPriTxPrefixMax,
       "xpolicyConformance": xpolicyConformance,
       "xpolicyCompliances": xpolicyCompliances,
       "xpolicyCompliance": xpolicyCompliance,
       "xpolicyGroups": xpolicyGroups,
       "xpolicyAllGroup": xpolicyAllGroup}
)
