# SNMP MIB module (ZXR10-PROTOCOL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ZXR10-PROTOCOL-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:21:00 2024
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
 TimeTicks,
 Unsigned32,
 enterprises,
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
    "enterprises",
    "iso")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions



class DisplayString(OctetString):
    """Custom type DisplayString based on OctetString"""



# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Zte_ObjectIdentity = ObjectIdentity
zte = _Zte_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902)
)
_Zxr10_ObjectIdentity = ObjectIdentity
zxr10 = _Zxr10_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 3)
)
_Zxr10protocol_ObjectIdentity = ObjectIdentity
zxr10protocol = _Zxr10protocol_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 3, 101)
)
_Zxr10ip_ObjectIdentity = ObjectIdentity
zxr10ip = _Zxr10ip_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 3, 101, 1)
)
_Zxr10ipvrfaddrTable_Object = MibTable
zxr10ipvrfaddrTable = _Zxr10ipvrfaddrTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 101, 1, 1)
)
if mibBuilder.loadTexts:
    zxr10ipvrfaddrTable.setStatus("current")
_Zxr10ipvrfaddrEntry_Object = MibTableRow
zxr10ipvrfaddrEntry = _Zxr10ipvrfaddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 101, 1, 1, 1)
)
zxr10ipvrfaddrEntry.setIndexNames(
    (0, "ZXR10-PROTOCOL-MIB", "zxr10ipVrfVpnName"),
    (0, "ZXR10-PROTOCOL-MIB", "zxr10ipVrfAddr"),
)
if mibBuilder.loadTexts:
    zxr10ipvrfaddrEntry.setStatus("current")


class _Zxr10ipVrfVpnName_Type(DisplayString):
    """Custom type zxr10ipVrfVpnName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Zxr10ipVrfVpnName_Type.__name__ = "DisplayString"
_Zxr10ipVrfVpnName_Object = MibTableColumn
zxr10ipVrfVpnName = _Zxr10ipVrfVpnName_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 101, 1, 1, 1, 1),
    _Zxr10ipVrfVpnName_Type()
)
zxr10ipVrfVpnName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10ipVrfVpnName.setStatus("current")
_Zxr10ipVrfAddr_Type = IpAddress
_Zxr10ipVrfAddr_Object = MibTableColumn
zxr10ipVrfAddr = _Zxr10ipVrfAddr_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 101, 1, 1, 1, 2),
    _Zxr10ipVrfAddr_Type()
)
zxr10ipVrfAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10ipVrfAddr.setStatus("current")
_Zxr10ipVrfNetMask_Type = IpAddress
_Zxr10ipVrfNetMask_Object = MibTableColumn
zxr10ipVrfNetMask = _Zxr10ipVrfNetMask_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 101, 1, 1, 1, 3),
    _Zxr10ipVrfNetMask_Type()
)
zxr10ipVrfNetMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10ipVrfNetMask.setStatus("current")
_Zxr10ipVrfIfIndex_Type = Integer32
_Zxr10ipVrfIfIndex_Object = MibTableColumn
zxr10ipVrfIfIndex = _Zxr10ipVrfIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 101, 1, 1, 1, 4),
    _Zxr10ipVrfIfIndex_Type()
)
zxr10ipVrfIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10ipVrfIfIndex.setStatus("current")
_Zxr10ipVrfBcastAddr_Type = Integer32
_Zxr10ipVrfBcastAddr_Object = MibTableColumn
zxr10ipVrfBcastAddr = _Zxr10ipVrfBcastAddr_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 101, 1, 1, 1, 5),
    _Zxr10ipVrfBcastAddr_Type()
)
zxr10ipVrfBcastAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10ipVrfBcastAddr.setStatus("current")


class _Zxr10ipVrfReasmMaxSize_Type(Integer32):
    """Custom type zxr10ipVrfReasmMaxSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Zxr10ipVrfReasmMaxSize_Type.__name__ = "Integer32"
_Zxr10ipVrfReasmMaxSize_Object = MibTableColumn
zxr10ipVrfReasmMaxSize = _Zxr10ipVrfReasmMaxSize_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 101, 1, 1, 1, 6),
    _Zxr10ipVrfReasmMaxSize_Type()
)
zxr10ipVrfReasmMaxSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10ipVrfReasmMaxSize.setStatus("current")
_Zxr10tcp_ObjectIdentity = ObjectIdentity
zxr10tcp = _Zxr10tcp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 3, 101, 2)
)
_Zxr10tcpConnTable_Object = MibTable
zxr10tcpConnTable = _Zxr10tcpConnTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 101, 2, 1)
)
if mibBuilder.loadTexts:
    zxr10tcpConnTable.setStatus("current")
_Zxr10tcpconnEntry_Object = MibTableRow
zxr10tcpconnEntry = _Zxr10tcpconnEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 101, 2, 1, 1)
)
zxr10tcpconnEntry.setIndexNames(
    (0, "ZXR10-PROTOCOL-MIB", "zxr10tcpConnVrfVpnName"),
    (0, "ZXR10-PROTOCOL-MIB", "zxr10tcpConnLocalAddress"),
    (0, "ZXR10-PROTOCOL-MIB", "zxr10tcpConnLocalPort"),
    (0, "ZXR10-PROTOCOL-MIB", "zxr10tcpConnRemAddress"),
    (0, "ZXR10-PROTOCOL-MIB", "zxr10tcpConnRemPort"),
)
if mibBuilder.loadTexts:
    zxr10tcpconnEntry.setStatus("current")


class _Zxr10tcpConnVrfVpnName_Type(DisplayString):
    """Custom type zxr10tcpConnVrfVpnName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Zxr10tcpConnVrfVpnName_Type.__name__ = "DisplayString"
_Zxr10tcpConnVrfVpnName_Object = MibTableColumn
zxr10tcpConnVrfVpnName = _Zxr10tcpConnVrfVpnName_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 101, 2, 1, 1, 1),
    _Zxr10tcpConnVrfVpnName_Type()
)
zxr10tcpConnVrfVpnName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10tcpConnVrfVpnName.setStatus("current")


class _Zxr10tcpConnState_Type(Integer32):
    """Custom type zxr10tcpConnState based on Integer32"""
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
              10,
              11,
              12)
        )
    )
    namedValues = NamedValues(
        *(("closeWait", 8),
          ("closed", 1),
          ("closing", 10),
          ("deleteTCB", 12),
          ("established", 5),
          ("finWait1", 6),
          ("finWait2", 7),
          ("lastAck", 9),
          ("listen", 2),
          ("synReceived", 4),
          ("synSent", 3),
          ("timeWait", 11))
    )


_Zxr10tcpConnState_Type.__name__ = "Integer32"
_Zxr10tcpConnState_Object = MibTableColumn
zxr10tcpConnState = _Zxr10tcpConnState_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 101, 2, 1, 1, 2),
    _Zxr10tcpConnState_Type()
)
zxr10tcpConnState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxr10tcpConnState.setStatus("current")
_Zxr10tcpConnLocalAddress_Type = IpAddress
_Zxr10tcpConnLocalAddress_Object = MibTableColumn
zxr10tcpConnLocalAddress = _Zxr10tcpConnLocalAddress_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 101, 2, 1, 1, 3),
    _Zxr10tcpConnLocalAddress_Type()
)
zxr10tcpConnLocalAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10tcpConnLocalAddress.setStatus("current")


class _Zxr10tcpConnLocalPort_Type(Integer32):
    """Custom type zxr10tcpConnLocalPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Zxr10tcpConnLocalPort_Type.__name__ = "Integer32"
_Zxr10tcpConnLocalPort_Object = MibTableColumn
zxr10tcpConnLocalPort = _Zxr10tcpConnLocalPort_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 101, 2, 1, 1, 4),
    _Zxr10tcpConnLocalPort_Type()
)
zxr10tcpConnLocalPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10tcpConnLocalPort.setStatus("current")
_Zxr10tcpConnRemAddress_Type = IpAddress
_Zxr10tcpConnRemAddress_Object = MibTableColumn
zxr10tcpConnRemAddress = _Zxr10tcpConnRemAddress_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 101, 2, 1, 1, 5),
    _Zxr10tcpConnRemAddress_Type()
)
zxr10tcpConnRemAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10tcpConnRemAddress.setStatus("current")


class _Zxr10tcpConnRemPort_Type(Integer32):
    """Custom type zxr10tcpConnRemPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Zxr10tcpConnRemPort_Type.__name__ = "Integer32"
_Zxr10tcpConnRemPort_Object = MibTableColumn
zxr10tcpConnRemPort = _Zxr10tcpConnRemPort_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 101, 2, 1, 1, 6),
    _Zxr10tcpConnRemPort_Type()
)
zxr10tcpConnRemPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10tcpConnRemPort.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZXR10-PROTOCOL-MIB",
    **{"DisplayString": DisplayString,
       "zte": zte,
       "zxr10": zxr10,
       "zxr10protocol": zxr10protocol,
       "zxr10ip": zxr10ip,
       "zxr10ipvrfaddrTable": zxr10ipvrfaddrTable,
       "zxr10ipvrfaddrEntry": zxr10ipvrfaddrEntry,
       "zxr10ipVrfVpnName": zxr10ipVrfVpnName,
       "zxr10ipVrfAddr": zxr10ipVrfAddr,
       "zxr10ipVrfNetMask": zxr10ipVrfNetMask,
       "zxr10ipVrfIfIndex": zxr10ipVrfIfIndex,
       "zxr10ipVrfBcastAddr": zxr10ipVrfBcastAddr,
       "zxr10ipVrfReasmMaxSize": zxr10ipVrfReasmMaxSize,
       "zxr10tcp": zxr10tcp,
       "zxr10tcpConnTable": zxr10tcpConnTable,
       "zxr10tcpconnEntry": zxr10tcpconnEntry,
       "zxr10tcpConnVrfVpnName": zxr10tcpConnVrfVpnName,
       "zxr10tcpConnState": zxr10tcpConnState,
       "zxr10tcpConnLocalAddress": zxr10tcpConnLocalAddress,
       "zxr10tcpConnLocalPort": zxr10tcpConnLocalPort,
       "zxr10tcpConnRemAddress": zxr10tcpConnRemAddress,
       "zxr10tcpConnRemPort": zxr10tcpConnRemPort}
)
