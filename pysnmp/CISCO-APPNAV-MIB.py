# SNMP MIB module (CISCO-APPNAV-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-APPNAV-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:55:40 2024
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

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

ciscoAppNavMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 791)
)
ciscoAppNavMIB.setRevisions(
        ("2012-06-07 00:00",
         "2012-05-22 00:00",
         "2012-04-10 00:00",
         "2012-03-26 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class CAppNavServContextJoinStates(Integer32, TextualConvention):
    status = "current"
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
        *(("aborted", 4),
          ("completed", 5),
          ("notConfigured", 2),
          ("started", 3),
          ("unknown", 1))
    )



class CAppNavCMStates(Integer32, TextualConvention):
    status = "current"
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
        *(("alive", 2),
          ("dead", 1),
          ("excluded", 3),
          ("inactive", 7),
          ("na", 5),
          ("partial", 4),
          ("zombie", 6))
    )



class CAppNavIRStates(Integer32, TextualConvention):
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
        *(("na", 3),
          ("notReady", 2),
          ("ready", 1))
    )



class CAppNavServContextOpStates(Integer32, TextualConvention):
    status = "current"
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("adminDisabled", 6),
          ("converging", 2),
          ("convergingJoining", 8),
          ("degraded", 4),
          ("degradedJoining", 10),
          ("initializing", 1),
          ("initializingJoining", 7),
          ("internalError", 3),
          ("operational", 5),
          ("operationalJoining", 9))
    )



# MIB Managed Objects in the order of their OIDs

_CiscoAppNavMIBObjects_ObjectIdentity = ObjectIdentity
ciscoAppNavMIBObjects = _CiscoAppNavMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 791, 0)
)
_CAppNavServContext_ObjectIdentity = ObjectIdentity
cAppNavServContext = _CAppNavServContext_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 791, 0, 1)
)
_CAppNavServContextTable_Object = MibTable
cAppNavServContextTable = _CAppNavServContextTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 791, 0, 1, 1)
)
if mibBuilder.loadTexts:
    cAppNavServContextTable.setStatus("current")
_CAppNavServContextEntry_Object = MibTableRow
cAppNavServContextEntry = _CAppNavServContextEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 791, 0, 1, 1, 1)
)
cAppNavServContextEntry.setIndexNames(
    (0, "CISCO-APPNAV-MIB", "cAppNavServContextIndex"),
)
if mibBuilder.loadTexts:
    cAppNavServContextEntry.setStatus("current")


class _CAppNavServContextIndex_Type(Unsigned32):
    """Custom type cAppNavServContextIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_CAppNavServContextIndex_Type.__name__ = "Unsigned32"
_CAppNavServContextIndex_Object = MibTableColumn
cAppNavServContextIndex = _CAppNavServContextIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 791, 0, 1, 1, 1, 1),
    _CAppNavServContextIndex_Type()
)
cAppNavServContextIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cAppNavServContextIndex.setStatus("current")


class _CAppNavServContextName_Type(OctetString):
    """Custom type cAppNavServContextName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_CAppNavServContextName_Type.__name__ = "OctetString"
_CAppNavServContextName_Object = MibTableColumn
cAppNavServContextName = _CAppNavServContextName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 791, 0, 1, 1, 1, 2),
    _CAppNavServContextName_Type()
)
cAppNavServContextName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cAppNavServContextName.setStatus("current")
_CAppNavServContextCurrOpState_Type = CAppNavServContextOpStates
_CAppNavServContextCurrOpState_Object = MibTableColumn
cAppNavServContextCurrOpState = _CAppNavServContextCurrOpState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 791, 0, 1, 1, 1, 3),
    _CAppNavServContextCurrOpState_Type()
)
cAppNavServContextCurrOpState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cAppNavServContextCurrOpState.setStatus("current")
_CAppNavServContextLastOpState_Type = CAppNavServContextOpStates
_CAppNavServContextLastOpState_Object = MibTableColumn
cAppNavServContextLastOpState = _CAppNavServContextLastOpState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 791, 0, 1, 1, 1, 4),
    _CAppNavServContextLastOpState_Type()
)
cAppNavServContextLastOpState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cAppNavServContextLastOpState.setStatus("current")
_CAppNavServContextIRState_Type = CAppNavIRStates
_CAppNavServContextIRState_Object = MibTableColumn
cAppNavServContextIRState = _CAppNavServContextIRState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 791, 0, 1, 1, 1, 5),
    _CAppNavServContextIRState_Type()
)
cAppNavServContextIRState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cAppNavServContextIRState.setStatus("current")
_CAppNavServContextJoinState_Type = CAppNavServContextJoinStates
_CAppNavServContextJoinState_Object = MibTableColumn
cAppNavServContextJoinState = _CAppNavServContextJoinState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 791, 0, 1, 1, 1, 6),
    _CAppNavServContextJoinState_Type()
)
cAppNavServContextJoinState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cAppNavServContextJoinState.setStatus("current")
_CAppNavACG_ObjectIdentity = ObjectIdentity
cAppNavACG = _CAppNavACG_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 791, 0, 2)
)
_CAppNavACGTable_Object = MibTable
cAppNavACGTable = _CAppNavACGTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 791, 0, 2, 1)
)
if mibBuilder.loadTexts:
    cAppNavACGTable.setStatus("current")
_CAppNavACGEntry_Object = MibTableRow
cAppNavACGEntry = _CAppNavACGEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 791, 0, 2, 1, 1)
)
cAppNavACGEntry.setIndexNames(
    (0, "CISCO-APPNAV-MIB", "cAppNavACGIndex"),
)
if mibBuilder.loadTexts:
    cAppNavACGEntry.setStatus("current")


class _CAppNavACGIndex_Type(Unsigned32):
    """Custom type cAppNavACGIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_CAppNavACGIndex_Type.__name__ = "Unsigned32"
_CAppNavACGIndex_Object = MibTableColumn
cAppNavACGIndex = _CAppNavACGIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 791, 0, 2, 1, 1, 1),
    _CAppNavACGIndex_Type()
)
cAppNavACGIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cAppNavACGIndex.setStatus("current")


class _CAppNavACGName_Type(OctetString):
    """Custom type cAppNavACGName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_CAppNavACGName_Type.__name__ = "OctetString"
_CAppNavACGName_Object = MibTableColumn
cAppNavACGName = _CAppNavACGName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 791, 0, 2, 1, 1, 2),
    _CAppNavACGName_Type()
)
cAppNavACGName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cAppNavACGName.setStatus("current")


class _CAppNavACGServContextName_Type(OctetString):
    """Custom type cAppNavACGServContextName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 96),
    )


_CAppNavACGServContextName_Type.__name__ = "OctetString"
_CAppNavACGServContextName_Object = MibTableColumn
cAppNavACGServContextName = _CAppNavACGServContextName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 791, 0, 2, 1, 1, 3),
    _CAppNavACGServContextName_Type()
)
cAppNavACGServContextName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cAppNavACGServContextName.setStatus("current")
_CAppNavSNG_ObjectIdentity = ObjectIdentity
cAppNavSNG = _CAppNavSNG_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 791, 0, 3)
)
_CAppNavSNGTable_Object = MibTable
cAppNavSNGTable = _CAppNavSNGTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 791, 0, 3, 1)
)
if mibBuilder.loadTexts:
    cAppNavSNGTable.setStatus("current")
_CAppNavSNGEntry_Object = MibTableRow
cAppNavSNGEntry = _CAppNavSNGEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 791, 0, 3, 1, 1)
)
cAppNavSNGEntry.setIndexNames(
    (0, "CISCO-APPNAV-MIB", "cAppNavSNGIndex"),
)
if mibBuilder.loadTexts:
    cAppNavSNGEntry.setStatus("current")


class _CAppNavSNGIndex_Type(Unsigned32):
    """Custom type cAppNavSNGIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_CAppNavSNGIndex_Type.__name__ = "Unsigned32"
_CAppNavSNGIndex_Object = MibTableColumn
cAppNavSNGIndex = _CAppNavSNGIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 791, 0, 3, 1, 1, 1),
    _CAppNavSNGIndex_Type()
)
cAppNavSNGIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cAppNavSNGIndex.setStatus("current")


class _CAppNavSNGName_Type(OctetString):
    """Custom type cAppNavSNGName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_CAppNavSNGName_Type.__name__ = "OctetString"
_CAppNavSNGName_Object = MibTableColumn
cAppNavSNGName = _CAppNavSNGName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 791, 0, 3, 1, 1, 2),
    _CAppNavSNGName_Type()
)
cAppNavSNGName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cAppNavSNGName.setStatus("current")


class _CAppNavSNGServContextName_Type(OctetString):
    """Custom type cAppNavSNGServContextName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_CAppNavSNGServContextName_Type.__name__ = "OctetString"
_CAppNavSNGServContextName_Object = MibTableColumn
cAppNavSNGServContextName = _CAppNavSNGServContextName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 791, 0, 3, 1, 1, 3),
    _CAppNavSNGServContextName_Type()
)
cAppNavSNGServContextName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cAppNavSNGServContextName.setStatus("current")
_CAppNavAC_ObjectIdentity = ObjectIdentity
cAppNavAC = _CAppNavAC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 791, 0, 4)
)
_CAppNavACTable_Object = MibTable
cAppNavACTable = _CAppNavACTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 791, 0, 4, 1)
)
if mibBuilder.loadTexts:
    cAppNavACTable.setStatus("current")
_CAppNavACEntry_Object = MibTableRow
cAppNavACEntry = _CAppNavACEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 791, 0, 4, 1, 1)
)
cAppNavACEntry.setIndexNames(
    (0, "CISCO-APPNAV-MIB", "cAppNavACIndex"),
)
if mibBuilder.loadTexts:
    cAppNavACEntry.setStatus("current")


class _CAppNavACIndex_Type(Unsigned32):
    """Custom type cAppNavACIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_CAppNavACIndex_Type.__name__ = "Unsigned32"
_CAppNavACIndex_Object = MibTableColumn
cAppNavACIndex = _CAppNavACIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 791, 0, 4, 1, 1, 1),
    _CAppNavACIndex_Type()
)
cAppNavACIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cAppNavACIndex.setStatus("current")
_CAppNavACIpAddrType_Type = InetAddressType
_CAppNavACIpAddrType_Object = MibTableColumn
cAppNavACIpAddrType = _CAppNavACIpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 791, 0, 4, 1, 1, 2),
    _CAppNavACIpAddrType_Type()
)
cAppNavACIpAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cAppNavACIpAddrType.setStatus("current")
_CAppNavACIpAddr_Type = InetAddress
_CAppNavACIpAddr_Object = MibTableColumn
cAppNavACIpAddr = _CAppNavACIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 791, 0, 4, 1, 1, 3),
    _CAppNavACIpAddr_Type()
)
cAppNavACIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cAppNavACIpAddr.setStatus("current")


class _CAppNavACServContextName_Type(OctetString):
    """Custom type cAppNavACServContextName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_CAppNavACServContextName_Type.__name__ = "OctetString"
_CAppNavACServContextName_Object = MibTableColumn
cAppNavACServContextName = _CAppNavACServContextName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 791, 0, 4, 1, 1, 4),
    _CAppNavACServContextName_Type()
)
cAppNavACServContextName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cAppNavACServContextName.setStatus("current")


class _CAppNavACACGName_Type(OctetString):
    """Custom type cAppNavACACGName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_CAppNavACACGName_Type.__name__ = "OctetString"
_CAppNavACACGName_Object = MibTableColumn
cAppNavACACGName = _CAppNavACACGName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 791, 0, 4, 1, 1, 5),
    _CAppNavACACGName_Type()
)
cAppNavACACGName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cAppNavACACGName.setStatus("current")
_CAppNavACCurrentCMState_Type = CAppNavCMStates
_CAppNavACCurrentCMState_Object = MibTableColumn
cAppNavACCurrentCMState = _CAppNavACCurrentCMState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 791, 0, 4, 1, 1, 6),
    _CAppNavACCurrentCMState_Type()
)
cAppNavACCurrentCMState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cAppNavACCurrentCMState.setStatus("current")
_CAppNavSN_ObjectIdentity = ObjectIdentity
cAppNavSN = _CAppNavSN_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 791, 0, 5)
)
_CAppNavSNTable_Object = MibTable
cAppNavSNTable = _CAppNavSNTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 791, 0, 5, 1)
)
if mibBuilder.loadTexts:
    cAppNavSNTable.setStatus("current")
_CAppNavSNEntry_Object = MibTableRow
cAppNavSNEntry = _CAppNavSNEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 791, 0, 5, 1, 1)
)
cAppNavSNEntry.setIndexNames(
    (0, "CISCO-APPNAV-MIB", "cAppNavSNIndex"),
)
if mibBuilder.loadTexts:
    cAppNavSNEntry.setStatus("current")


class _CAppNavSNIndex_Type(Unsigned32):
    """Custom type cAppNavSNIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_CAppNavSNIndex_Type.__name__ = "Unsigned32"
_CAppNavSNIndex_Object = MibTableColumn
cAppNavSNIndex = _CAppNavSNIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 791, 0, 5, 1, 1, 1),
    _CAppNavSNIndex_Type()
)
cAppNavSNIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cAppNavSNIndex.setStatus("current")
_CAppNavSNIpAddrType_Type = InetAddressType
_CAppNavSNIpAddrType_Object = MibTableColumn
cAppNavSNIpAddrType = _CAppNavSNIpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 791, 0, 5, 1, 1, 2),
    _CAppNavSNIpAddrType_Type()
)
cAppNavSNIpAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cAppNavSNIpAddrType.setStatus("current")
_CAppNavSNIpAddr_Type = InetAddress
_CAppNavSNIpAddr_Object = MibTableColumn
cAppNavSNIpAddr = _CAppNavSNIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 791, 0, 5, 1, 1, 3),
    _CAppNavSNIpAddr_Type()
)
cAppNavSNIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cAppNavSNIpAddr.setStatus("current")


class _CAppNavSNServContextName_Type(OctetString):
    """Custom type cAppNavSNServContextName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_CAppNavSNServContextName_Type.__name__ = "OctetString"
_CAppNavSNServContextName_Object = MibTableColumn
cAppNavSNServContextName = _CAppNavSNServContextName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 791, 0, 5, 1, 1, 4),
    _CAppNavSNServContextName_Type()
)
cAppNavSNServContextName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cAppNavSNServContextName.setStatus("current")


class _CAppNavSNSNGName_Type(OctetString):
    """Custom type cAppNavSNSNGName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_CAppNavSNSNGName_Type.__name__ = "OctetString"
_CAppNavSNSNGName_Object = MibTableColumn
cAppNavSNSNGName = _CAppNavSNSNGName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 791, 0, 5, 1, 1, 5),
    _CAppNavSNSNGName_Type()
)
cAppNavSNSNGName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cAppNavSNSNGName.setStatus("current")
_CAppNavSNCurrentCMState_Type = CAppNavCMStates
_CAppNavSNCurrentCMState_Object = MibTableColumn
cAppNavSNCurrentCMState = _CAppNavSNCurrentCMState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 791, 0, 5, 1, 1, 6),
    _CAppNavSNCurrentCMState_Type()
)
cAppNavSNCurrentCMState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cAppNavSNCurrentCMState.setStatus("current")
_CiscoAppNavMIBConform_ObjectIdentity = ObjectIdentity
ciscoAppNavMIBConform = _CiscoAppNavMIBConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 791, 1)
)
_CiscoAppNavMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoAppNavMIBCompliances = _CiscoAppNavMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 791, 1, 1)
)
_CiscoAppNavMIBGroups_ObjectIdentity = ObjectIdentity
ciscoAppNavMIBGroups = _CiscoAppNavMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 791, 1, 2)
)

# Managed Objects groups

cAppNavServiceContextGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 791, 1, 2, 1)
)
cAppNavServiceContextGroup.setObjects(
      *(("CISCO-APPNAV-MIB", "cAppNavServContextCurrOpState"),
        ("CISCO-APPNAV-MIB", "cAppNavServContextLastOpState"),
        ("CISCO-APPNAV-MIB", "cAppNavServContextIRState"),
        ("CISCO-APPNAV-MIB", "cAppNavServContextName"))
)
if mibBuilder.loadTexts:
    cAppNavServiceContextGroup.setStatus("current")

cAppNavACGGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 791, 1, 2, 2)
)
cAppNavACGGroup.setObjects(
      *(("CISCO-APPNAV-MIB", "cAppNavACGServContextName"),
        ("CISCO-APPNAV-MIB", "cAppNavACGName"))
)
if mibBuilder.loadTexts:
    cAppNavACGGroup.setStatus("current")

cAppNavSNGGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 791, 1, 2, 3)
)
cAppNavSNGGroup.setObjects(
      *(("CISCO-APPNAV-MIB", "cAppNavSNGServContextName"),
        ("CISCO-APPNAV-MIB", "cAppNavSNGName"))
)
if mibBuilder.loadTexts:
    cAppNavSNGGroup.setStatus("current")

cAppNavACGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 791, 1, 2, 4)
)
cAppNavACGroup.setObjects(
      *(("CISCO-APPNAV-MIB", "cAppNavACServContextName"),
        ("CISCO-APPNAV-MIB", "cAppNavACACGName"),
        ("CISCO-APPNAV-MIB", "cAppNavACCurrentCMState"),
        ("CISCO-APPNAV-MIB", "cAppNavACIpAddrType"),
        ("CISCO-APPNAV-MIB", "cAppNavACIpAddr"))
)
if mibBuilder.loadTexts:
    cAppNavACGroup.setStatus("current")

cAppNavSNGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 791, 1, 2, 5)
)
cAppNavSNGroup.setObjects(
      *(("CISCO-APPNAV-MIB", "cAppNavSNServContextName"),
        ("CISCO-APPNAV-MIB", "cAppNavSNSNGName"),
        ("CISCO-APPNAV-MIB", "cAppNavSNCurrentCMState"),
        ("CISCO-APPNAV-MIB", "cAppNavSNIpAddrType"),
        ("CISCO-APPNAV-MIB", "cAppNavSNIpAddr"))
)
if mibBuilder.loadTexts:
    cAppNavSNGroup.setStatus("current")

cAppNavServiceContextGroupRev1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 791, 1, 2, 6)
)
cAppNavServiceContextGroupRev1.setObjects(
    ("CISCO-APPNAV-MIB", "cAppNavServContextJoinState")
)
if mibBuilder.loadTexts:
    cAppNavServiceContextGroupRev1.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ciscoAppNavMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 791, 1, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoAppNavMIBCompliance.setStatus(
        "deprecated"
    )

ciscoAppNavMIBComplianceRev1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 791, 1, 1, 2)
)
if mibBuilder.loadTexts:
    ciscoAppNavMIBComplianceRev1.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-APPNAV-MIB",
    **{"CAppNavServContextJoinStates": CAppNavServContextJoinStates,
       "CAppNavCMStates": CAppNavCMStates,
       "CAppNavIRStates": CAppNavIRStates,
       "CAppNavServContextOpStates": CAppNavServContextOpStates,
       "ciscoAppNavMIB": ciscoAppNavMIB,
       "ciscoAppNavMIBObjects": ciscoAppNavMIBObjects,
       "cAppNavServContext": cAppNavServContext,
       "cAppNavServContextTable": cAppNavServContextTable,
       "cAppNavServContextEntry": cAppNavServContextEntry,
       "cAppNavServContextIndex": cAppNavServContextIndex,
       "cAppNavServContextName": cAppNavServContextName,
       "cAppNavServContextCurrOpState": cAppNavServContextCurrOpState,
       "cAppNavServContextLastOpState": cAppNavServContextLastOpState,
       "cAppNavServContextIRState": cAppNavServContextIRState,
       "cAppNavServContextJoinState": cAppNavServContextJoinState,
       "cAppNavACG": cAppNavACG,
       "cAppNavACGTable": cAppNavACGTable,
       "cAppNavACGEntry": cAppNavACGEntry,
       "cAppNavACGIndex": cAppNavACGIndex,
       "cAppNavACGName": cAppNavACGName,
       "cAppNavACGServContextName": cAppNavACGServContextName,
       "cAppNavSNG": cAppNavSNG,
       "cAppNavSNGTable": cAppNavSNGTable,
       "cAppNavSNGEntry": cAppNavSNGEntry,
       "cAppNavSNGIndex": cAppNavSNGIndex,
       "cAppNavSNGName": cAppNavSNGName,
       "cAppNavSNGServContextName": cAppNavSNGServContextName,
       "cAppNavAC": cAppNavAC,
       "cAppNavACTable": cAppNavACTable,
       "cAppNavACEntry": cAppNavACEntry,
       "cAppNavACIndex": cAppNavACIndex,
       "cAppNavACIpAddrType": cAppNavACIpAddrType,
       "cAppNavACIpAddr": cAppNavACIpAddr,
       "cAppNavACServContextName": cAppNavACServContextName,
       "cAppNavACACGName": cAppNavACACGName,
       "cAppNavACCurrentCMState": cAppNavACCurrentCMState,
       "cAppNavSN": cAppNavSN,
       "cAppNavSNTable": cAppNavSNTable,
       "cAppNavSNEntry": cAppNavSNEntry,
       "cAppNavSNIndex": cAppNavSNIndex,
       "cAppNavSNIpAddrType": cAppNavSNIpAddrType,
       "cAppNavSNIpAddr": cAppNavSNIpAddr,
       "cAppNavSNServContextName": cAppNavSNServContextName,
       "cAppNavSNSNGName": cAppNavSNSNGName,
       "cAppNavSNCurrentCMState": cAppNavSNCurrentCMState,
       "ciscoAppNavMIBConform": ciscoAppNavMIBConform,
       "ciscoAppNavMIBCompliances": ciscoAppNavMIBCompliances,
       "ciscoAppNavMIBCompliance": ciscoAppNavMIBCompliance,
       "ciscoAppNavMIBComplianceRev1": ciscoAppNavMIBComplianceRev1,
       "ciscoAppNavMIBGroups": ciscoAppNavMIBGroups,
       "cAppNavServiceContextGroup": cAppNavServiceContextGroup,
       "cAppNavACGGroup": cAppNavACGGroup,
       "cAppNavSNGGroup": cAppNavSNGGroup,
       "cAppNavACGroup": cAppNavACGroup,
       "cAppNavSNGroup": cAppNavSNGroup,
       "cAppNavServiceContextGroupRev1": cAppNavServiceContextGroupRev1}
)
